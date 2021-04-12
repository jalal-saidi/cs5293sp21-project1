import os
import nltk
import re
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.tokenize import WhitespaceTokenizer
from nltk.stem import WordNetLemmatizer

def read_files(pattern):
    current_dir = os.getcwd()
    current_dir = current_dir+'/project1'
    files =[]
    for file in os.listdir(current_dir):
        if file.endswith(pattern):
            files.append(os.path.join(current_dir, file))
    return files

def redact_main(raw):
    sentences = sent_tokenize(raw)
    final_redacted=[]
    final_total_concept=0
    final_total_name=0
    final_total_phone=0
    final_total_email=0
    final_total_gender=0
    for sent in sentences:
       redacted_concept, total_concept = redact_concept(sent)
       if total_concept==0:
           redacted,total_name, total_phone,total_email,total_gender = redact_names_phones_emails_genders(sent)
           final_redacted.append(redacted)
           final_total_name = final_total_name+total_name
           final_total_phone = final_total_phone+total_phone
           final_total_email = final_total_email+total_email
           final_total_gender = final_total_gender+total_gender
       else:
           final_redacted.append(redacted_concept)
           final_total_concept = final_total_concept+total_concept
    final_redacted = ''.join(final_redacted) 
    return final_redacted,final_total_name, final_total_phone,final_total_email,final_total_gender,final_total_concept 

# Redacts the concept related to prison       
def redact_concept(sent):
   prison_concepts = ['prison','jail','detain','inmate','detention']
  # Create white space tokenizer
   ws_tokenizer = WhitespaceTokenizer()
   # Create the span tokens
   span_token= word_tokenize(sent)
   lemmatizer = WordNetLemmatizer()
   total_concept=0
   final_redacted=[]
   offset=0
   for token1 in span_token:
       lemma =lemmatizer.lemmatize(token1)
       if lemma.lower() in prison_concepts:
              total_concept=1
              for token in span_token:
                   index = sent.find(token, offset)
                   for j in range (offset,index):
                       final_redacted.append(sent[j])
                   for _ in range(len(token)):
                      final_redacted.append('\u2588')
                   offset=index+len(token)
              break
   final_redacted = ''.join(final_redacted)
   return  final_redacted,total_concept     


# This function redacts names, phones, and emails within the given text data
def redact_names_phones_emails_genders(raw):
   # Create white space tokenizer
   ws_tokenizer = WhitespaceTokenizer()
   # Create the span tokens
   ws_token= ws_tokenizer.tokenize(raw)
   # Find the positions of proper nouns
   
   # Phone Regular Expression
   r = re.compile(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})')
   # Email Regualr Expression
   r1 = re.compile(r'[\w\.-]+@[\w\.-]+')
   
   # gender vocabulary
   gender_vocab = ['he','she','hers', 'herself', 'him', 'hisself', 'her', 'his']
   
   redacted = []
   total_name =0
   total_phone=0
   total_email=0
   total_gender=0
   
   # iterate in white space tokens to redact phones and emails
   for token in ws_token:
     if r.match(token):
       temp=''
       for i in range(len(token)):
          temp=temp+'\u2588'
       total_phone=total_phone+1
       redacted.append(temp)
     elif r1.match(token): 
       temp=''
       for i in range(len(token)):
          temp=temp+'\u2588'
       total_email=total_email+1
       redacted.append(temp)
     else:
         redacted.append(token)
   
   # store the results from phones and email redaction in a new string
   result2 =''
   for voc in redacted:
       result2 = result2+' '+str(voc)
   # tokenize new string using non-white space tokenizer
   tokens2= word_tokenize(result2)
   # NLTK Part of speech tagging 
   tags=nltk.pos_tag(tokens2)
   offset = 0
   final_result = []
   for i, tag in enumerate(tags):
     # Look for and redact proper nouns
     if tag[1]=='NNP':
        index = result2.find(tokens2[i], offset)
        for j in range (offset,index):
           final_result.append(result2[j])
        for _ in range(len(tokens2[i])):
          final_result.append('\u2588')
        total_name=total_name+1
        offset=index+len(tokens2[i])
     # Look for and redact gender pronouns
     elif  tag[0].lower() in gender_vocab and (tag[1]== 'PRP$' or tag[1]=='PRP'):
        index = result2.find(tokens2[i], offset)
        for j in range (offset,index):
           final_result.append(result2[j])
        for _ in range(len(tokens2[i])):
          final_result.append('\u2588')
        total_gender=total_gender+1
        offset=index+len(tokens2[i])
     else:
        index = result2.find(tokens2[i], offset)
        for j in range (offset,index):
           final_result.append(result2[j])
        for j in range(index,index+len(tokens2[i])):
          final_result.append(result2[j])
        offset=index+len(tokens2[i])
   final_result = ''.join(final_result)
   return (final_result,total_name,total_phone,total_email,total_gender)

# write the redacted file into given output directory
def write_redacted(final_redacted,output,file):
    file_=open(os.getcwd()+'/project1/'+str(output)+file[file.rindex('/')+1:]+'.redacted',"w")
    file_.write(final_redacted)
    file_.close()



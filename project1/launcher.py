import argparse
import project1_main
import sys

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, required=True, 
                         help="Accepted input extension.")
    parser.add_argument("--names",action='store_true', 
                         help="Names")
    parser.add_argument("--phones", action='store_true', 
                         help="Dates")
    parser.add_argument("--emails",action='store_true', 
                         help="Email")
    parser.add_argument("--concept", type=str, required=True, 
                         help="Concept")
    parser.add_argument("--output", type=str, required=True, 
                         help="Redacted files directory.")
    parser.add_argument("--stats", type=str, required=True, 
                         help="Summary of redacted files.")

    args = parser.parse_args()
    print(args.input)
    if args.input:
        # read files given the required extension
        files=project1_main.read_files(args.input)
        for file in files:
           file_=open(file,"r")
           raw=file_.read()
           # redact the file and retreive the results
           final_redacted,final_total_name, final_total_phone,final_total_email,final_total_gender,final_total_concept = project1_main.redact_main(raw)
           if final_total_name!=0 or final_total_phone!=0 or final_total_email!=0 or final_total_gender!=0 or final_total_concept!=0:
           	#write the result only if there is at least one redacted string
                project1_main.write_redacted(final_redacted,args.output,file)
           
           
           sys.stdout.write("Result for: {0}\n Names redacted:{1}\n Phones redacted:{2}\n Emails redacted:{3}\n Gender redacted:{4}\n Concept redacted:{5}\n".format(file[file.rindex('/')+1:],final_total_name, final_total_phone,final_total_email,final_total_gender,final_total_concept))
           file_.close()

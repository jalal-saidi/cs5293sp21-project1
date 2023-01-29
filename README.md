Said Jalal Saidi

How to run: it requires passing a valid input extension such as ".Txt". Also, it requires the types of redaction needed, such as phones, emails, names, and genders. Moreover, we redact concepts related to prisons such as jail, inmates and etc. Finally, it requires the output directory in which the redacted results are written. For example, the command line argument is used: pipenv run python project1/launcher.Py --input '.Txt' --names  --phones  --emails  --concept 'kids' --output 'files/' --stats 'stdout'

How to test: it requires using "Pipenv run pytest" at the root level of the project

Libraries, dependencies, and virtual environment: first, a virtual environment is created using pyenv, with 3.8.6 python version. Second, project1 module is installed in this virtual env. Third, the required libraries to run and the test is module is installed namely "Pipenv" and "Pytest". Fourth, required libraries for the program functionalities are installed such as nltk, which is necessary for natural language processing. Fifth, other libraries such as  "Re" for regex search, "OS" for walking through directories and files, and "Sys" for writing to standard output are used.

Assumptions: the main python files are "Launcher.Py", which includes the starter function. Also, "Project1_main.Py" which includes important functionalities such as reading raw data, and redacting names, phones, emails, genders, and concepts. The concept is related to prison. We use nltk for tokenization, part of speech tagging, and lemmatization. 

Test cases: test cases are included in "Project1_test.Py". Two test cases are written; test_redact_phones, which tests redacting phones. Test_redact_emails, which tests redacting emails.

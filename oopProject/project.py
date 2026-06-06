import pprint as p
import nlpcloud

class NLPApp:

    def __init__(self):
        self.__database = {}
        self.__firstMenu()

    def __firstMenu(self):
        firstInput = int(input("""
Hi, How do you like to proceed?
1. Not a member? Register
2. Already a member? Login
3. Want to Exit? Logout
"""))
        
        if firstInput == 1:
            self.__register()
        elif firstInput == 2:
            self.__login()
        elif firstInput == 3:
            exit()

    def __secondMenu(self):
        secondInput = int(input("""
Hi, How do you like to proceed?
1. NER
2. Language Detection
3. Sentiment Analysis
4. Exit
"""))
        
        if secondInput == 1:
            self.__nerNlp()
        elif secondInput == 2:
            self.__languageDetectionNlp()
        elif secondInput == 3:
            self.__sentiAnalysisNlp()
        elif secondInput == 4:
            exit()
        
    def __register(self):
        name = input("Enter Name: ")
        email = input("Enter mail id: ")

        # adding them to dictionary
        # {
        # email : [name,password], 
        # email : [name,password]
        # }

        if email in self.__database:
            print("User already exists. Try to login")

        else:
            password = input("Enter the password: ")
            self.__database[email] = [name,password]
            print("User Registration Successfull\nNow Login\n")
            # p.pprint(self.__database)

        self.__firstMenu()

    def __login(self):
        email = input("Enter email: ")
        password = input("Enter password: ")
        if email in self.__database:

            if self.__database[email][1] == password:
                print("Login Sucsessfull")
                self.__secondMenu()

            else: 
                print("Wrong Password")
                self.__firstMenu()

        else:
            print("This Email Is Not Registered")
            self.__firstMenu()

    def __nerNlp(self):
        """
        Accepts 2 inputs
        a) Paragraph to search
        b) What to search
        """
        para = input("Enter the paragraph: ")
        searchTerm = input("What would you like to search? ")

        client = nlpcloud.Client("gpt-oss-120b", "31c99d72be25e26ecebad454bca0857b073f1c94", gpu=True, lang='en')
        response = client.entities(para,searched_entity=searchTerm)
        p.pprint(response)

    def __sentiAnalysisNlp(self):
        """
        Accepts 1 inputs
        a) Paragraph to search
        """
        para = input("Enter the paragraph: ")

        client = nlpcloud.Client("gpt-oss-120b", "31c99d72be25e26ecebad454bca0857b073f1c94", gpu=True)
        response = client.sentiment(para, target="NLP Cloud")
        # p.pprint(response)

        #{'scored_labels': [{'label': 'NEGATIVE', 'score': 1},
        #                   {'label': 'frustration', 'score': 1},
        #                   {'label': 'Neutral', 'score': 0.9}]}

        # pull out the response with highest score

        l = []
        for i in response['scored_labels']:
            l.append(i['score'])

        index = sorted(list(enumerate(l)),reverse=True, key=lambda x:x[1])[0][0]
        print(response['scored_labels'][index]['label'])


    def __languageDetectionNlp(self):
        """
        Accepts 1 inputs
        a) Paragraph to search
        """
        para = input("Enter the paragraph: ")

        client = nlpcloud.Client("python-langdetect", "31c99d72be25e26ecebad454bca0857b073f1c94", gpu=False)
        response = client.langdetection(para)

        print(response)

        l=[]
        for i in response['languages']:
            l.append(list(i.values())[0])

        # sorted(list(enumerate(values)), reverse=True, key=lambda x: x[1])
        index = sorted(list(enumerate(l)), key=lambda i:i[1], reverse=True)[0][0]
        print(list(response['languages'][index].keys())[0])

    
obj = NLPApp()
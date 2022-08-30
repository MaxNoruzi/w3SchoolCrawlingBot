import requests
from bs4 import BeautifulSoup
from bs4 import Comment
class Crawler():
    url ='https://www.w3schools.com/python/'

    def __init__(self) -> None:
        pass

    def startProgram(self):
        #driver = webdriver.Chrome()
        #driver.get(self.url)
        rawData =requests.get(self.url)  
        soup = BeautifulSoup(rawData.content, "html.parser")
        
               
        self.__choose_subject(soup)

    def __choose_subject(self, soup):
        results = soup.find(id="leftmenuinnerinner")
        main_topics = results.find_all("h2",class_="left")
        counter =1
        
            
        for topic in main_topics:
            print(str(counter)+ ":"+topic.text)
            counter+=1
        chosennumber = self.inputManager(len(main_topics),"enter your main subject number")


        #next chapter
        temp=main_topics[chosennumber-1]
        myList = []
        while(True):
           if temp.nextSibling !=  main_topics[chosennumber]:
                if isinstance(temp,Comment):
                    #temp2 = temp
                    temp= temp.nextSibling
                    #temp2.extract()
                    continue
                #if boz.name !="div":
                if temp.text!= "\n" :
                    myList.append(temp) 
                temp =temp.nextSibling
           else :
                break 

        for name in myList:
            if  name.name != "div" :
                print (name.text)        
        chosennumber =self.inputManager(len(myList),"choose your inner topic plz:  ")
        if myList[chosennumber-1].name != "div":
           newurl =self.url+ str(myList[chosennumber-1]['href'])
           print(newurl)
        else:
           self.__innerTopics(myList[chosennumber-1])   





    def __innerTopics(self , object):
        #we get all objects inside division
        object = object.findAll("a")
        for temp in object:
            print(temp.text)

    def inputManager(self,size,subjectString):
        while(True):
            userInput= input(subjectString)
            try:
                if int(userInput) in range(size):
                    return int(userInput)
                else:
                    print("enter a valid number")     
            except:
                print("enter a valid number")

    def innerTopic(self , object):
        pass 


crawler = Crawler()
crawler.startProgram()
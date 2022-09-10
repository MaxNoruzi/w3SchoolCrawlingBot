import requests
from bs4 import BeautifulSoup
from bs4 import Comment
import asyncio
from pyppeteer import launch
import os
class Crawler():
    url ='https://www.w3schools.com/python/'

    def __init__(self) -> None:
        pass

    async def startProgram2(self):
        #driver = webdriver.Chrome()
        #driver.get(self.url)
        # rawData =requests.get(self.url)  
        # soup = BeautifulSoup(rawData.content, "html.parser")
        # self.__choose_subject(soup)  

         # Launch the browser
        browser = await launch()

        # Open a new browser page
        page = await browser.newPage()

        # Create a URI for our test file
        page_path = "https://www.digikala.com/search/category-groceries/"

        # Open our test file in the opened page
        await page.goto(page_path)
        page_content = await page.content()

        # Process extracted content with BeautifulSoup
        soup = BeautifulSoup(page_content)
        print(page_content)

        # Close browser
        await browser.close()


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
           if temp !=  main_topics[chosennumber]:
                if isinstance(temp,Comment):
                    #temp2 = temp
                    temp= temp.nextSibling
                    #temp2.extract()
                    continue
                #if boz.name !="div":
                if temp.text!= "\n" and  temp.name !="br":
                    myList.append(temp) 
                temp =temp.nextSibling
           else :
                break 
        count =1        
        for name in myList:
            if  name.name != "div" :
                print (str(count) +":"+name.text)   
                count+=1     
        chosennumber =self.inputManager(len(myList),"choose your inner topic plz:  ")
        chosenObject = self.translateChosenNumber(list=myList,number=chosennumber-1)
        
        if chosenObject.name != "div":
           newurl =self.url+ str(chosenObject['href'])
           
        else:
           self.__innerTopics(chosenObject)   
    def extractMainPage(self,url):
        rawData =requests.get(url)  
        soup = BeautifulSoup(rawData.content, "html.parser")      
        soup.find_all(name = "a", string="Try it Yourself »",target="_blank")

        pass








    def translateChosenNumber(self,number,list):
        newList = []
        for i  in list:
            if i.name != "div":
                newList.append(i)

        count = list.index(newList[number])
        if count == len(list)-1 or list[count+1].name !="div":
            return list[count]
        elif list[count+1].name =="div":
            return list[count+1]    




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
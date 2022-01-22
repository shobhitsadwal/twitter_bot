# twitter_bot
## A online web crawling bot that crawls through twitter and publishes the internet delay or breaking the speed promises when purchasing the Plan of internet providers.
![twitter](https://www.investopedia.com/thmb/Z7XrQu6mhgiVy4fqVmidnWPSVBQ=/680x453/filters:fill(auto,1)/shutterstock_216247747twtr-5bfc324346e0fb00517d2976.jpg)

# what is a bot ?
A bot is a software application that is programmed to do certain tasks. Bots are automated, which means they run according to their instructions without a human user needing to manually start them up every time. Bots often imitate or replace a human user's behavior. Typically they do repetitive tasks, and they can do them much faster than human users could.

Bots usually operate over a network; more than half of Internet traffic is bots scanning content, interacting with webpages, chatting with users, or looking for attack targets. Some bots are useful, such as search engine bots that index content for search or customer service bots that help users. Other bots are "bad" and are programmed to break into user accounts, scan the web for contact information for sending spam, or perform other malicious activities. If it's connected to the Internet, a bot will have an associated IP address.

Bots can be:

- Chatbots: Bots that simulate human conversation by responding to certain phrases with programmed responses,
- Web crawlers (Googlebots): Bots that scan content on webpages all over the Internet,
- Social bots: Bots that operate on social media platforms,
- Malicious bots: Bots that scrape content, spread spam content, or carry out credential stuffing attacks 

# what is selenium ?
![sel](https://www.edureka.co/blog/wp-content/uploads/2017/06/selenium.png)

Selenium refers to a suite of tools that are widely used in the testing community when it comes to cross-browser testing. Selenium cannot automate desktop applications; it can only be used in browsers. It is considered to be one of the most preferred tool suites for automation testing of web applications as it provides support for popular web browsers which makes it very powerful.

It supports a number of browsers (Google Chrome 12+, Internet Explorer 7,8,9,10, Safari 5.1+, Opera 11.5, Firefox 3+) and operating systems (Windows, Mac, Linux/Unix).

Selenium also provides compatibility with different programming languages – C#, Java, JavaScript, Ruby, Python, PHP. Testers can choose which language to design test cases in, thus making Selenium highly favorable for its flexibility.

# ethics of web-scraping 
- https://www.promptcloud.com/blog/is-data-scraping-ethical/#:~:text=Data%20scraping%20is%20ethical%20as,legal%20aspects%20of%20data%20scraping.
- https://towardsdatascience.com/ethics-in-web-scraping-b96b18136f01
- https://monashdatafluency.github.io/python-web-scraping/section-5-legal-and-ethical-considerations/
- https://aisel.aisnet.org/cais/vol47/iss1/22/

# Aim and motivation for the project 

this program is used for automation of two websites and linking them together by a bot.
The main purpose of the program is to send a public message on the twitter to the company who has 
 promised giving the internet connection at a certain speed but whenever the speed is constantly low,
it will automatically send a message mentioning the company name about the disturbance caused. 

you can use this project commercially or deploy this project to run at specific times during the day . Also you can choose the handle of the internet service provider accordingly.


# files to refer 
- ```main.py```
- ```twitter_bot_using_selenium.iml```

for documentation of selenium, https://www.selenium.dev/

# code-flow 

below is the main.py 

```python

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# path='D:\chrome driver\chromedriver_win32\chromedriver.exe'
# driver=webdriver.Chrome(executable_path=path)

'''this program is used for automation of two websites and linking them together by a bot.
The main purpose of the program is to send a public message on the twitter to the company who has 
 promised giving the internet connection at a certain speed but whenever the speed is constantly low,
it will automatically send a message mentioning the company name about the disturbance caused '''





class InternetSpeedTwitterBot:
    def __init__(self,driver,down,up):
        self.driver=driver
        self.down=down
        self.up=up
        # self.get_internet_speed()

    def get_internet_speed(self):
        '''this will return a string containing the informatioin about your download and upload speeds '''

        chorme=webdriver.Chrome(executable_path=self.driver)
        chorme.get('https://www.speedtest.net/')
        time.sleep(4)
        speed_button=chorme.find_element(by=By.XPATH,value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        speed_button.click()
        time.sleep(60)
        download_speed=float(chorme.find_element(by=By.XPATH,value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text)
        upload_speed=float(chorme.find_element(by=By.XPATH,value='/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text)
        chorme.quit()

        return f"the download speed are________ upload is {upload_speed}, download is {download_speed}"







    def tweet_at_provider(self,value):
        '''this will open the twitter and send the message automatically takin the value from the above function'''
        chorme=webdriver.Chrome(executable_path=self.driver)
        chorme.get('https://twitter.com/')
        time.sleep(3)
        sign_in=chorme.find_element(by=By.XPATH,value='/html/body/div/div/div/div/main/div/div/div/div[1]/div/div[3]/div[5]/a/div/span/span')
        sign_in.click()
        time.sleep(5)
        second_sign_in=chorme.find_element(by=By.XPATH,value='/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[5]/label/div/div[2]/div/input')
        time.sleep(2)
        second_sign_in.send_keys('your email')
        next_button=chorme.find_element(by=By.XPATH,value='/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[6]/div')
        next_button.click()
        time.sleep(2)
        password=chorme.find_element(by=By.XPATH,value='/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[3]/div/label/div/div[2]/div[1]/input')
        password.send_keys('your password')
        log_in=chorme.find_element(by=By.XPATH,value='/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div')
        log_in.click()
        time.sleep(4)
        inputter=chorme.find_element(by=By.XPATH,value='/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        inputter.send_keys(f" i think the net is not working fine {value} ")
        tweet=chorme.find_element(by=By.XPATH,value='/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div/div/span/span')
        tweet.click()
        time.sleep(3)
        chorme.quit()







dre=InternetSpeedTwitterBot(driver="D:\chrome driver\chromedriver_win32\chromedriver.exe",down=129,up=129)

pr=dre.get_internet_speed()



dre.tweet_at_provider(value=pr)
```

as we can see from the above code , we have initiated a class which consists of two methods which are 
- ```python get_internet_speed```
- ```python tweet_at_provider```

the class contains three objects that are 
```python
  def __init__(self,driver,down,up):
        self.driver=driver
        self.down=down
        self.up=up
```
driver = denotes the path and the driver location of the installation of the selenium , it is important to initiate this 
down= the download spped as promised by your internet provider 
up= the upload speed as promised by your internet provider 

## the first method 

the first **method get_internet_speed** automates the internet testing speed and collects the data from the following . 
the ```time.sleep()``` here is used for the break when the speedtest website gets rendered . You can also see that there is a code which is ```find_element(by=By.XPATH)```, this helps in 
locating the path or the relative path where the data lies in the browser . The first mehods return the up speed and the down speed and it then initiates to the final method as discussed . 

code snippet of the first method 
```python

    def get_internet_speed(self):
        '''this will return a string containing the informatioin about your download and upload speeds '''

        chorme=webdriver.Chrome(executable_path=self.driver)
        chorme.get('https://www.speedtest.net/')
        time.sleep(4)
        speed_button=chorme.find_element(by=By.XPATH,value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        speed_button.click()
        time.sleep(60)
        download_speed=float(chorme.find_element(by=By.XPATH,value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text)
        upload_speed=float(chorme.find_element(by=By.XPATH,value='/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text)
        chorme.quit()

        return f"the download speed are________ upload is {upload_speed}, download is {download_speed}"
```

## the second method 
the second method is responsible for targeting and opening the twitter website , we have used the command ```find_element(by=By.XPATH)``` again here to find the screen toggles . If you look caredully you 
will see that we have written ```send_keys()``` in the place of login Id and password , the send keys inputs the value that the programmer has given at the time of building the program . Sendkeys can use Float,List and even dictionary 
type characters. 

Thus we login with the help of an accout and then we post the results of the previous method if the download or the upload speed is not upto the promised values. 





















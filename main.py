
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





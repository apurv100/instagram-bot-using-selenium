from selenium import webdriver
from time import sleep

class MyInstaBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome('C:\\Users\\acer\\Downloads\\chromedriver_win32\\chromedriver.exe')
        self.driver.get('https://www.instagram.com')

        # Typing username
        self.username_input = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input')
        self.username_input.send_keys(self.username) 

        # Typing password
        self.password_input = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input')
        self.password_input.send_keys(self.password)

        # Logging in
        self.login_btn = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]')
        self.login_btn.click()

        # wait for a while
        sleep(5)

        # Notification Setting
        self.not_now_btn = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]')
        self.not_now_btn.click()
    
    def get_followers(self):
        self.driver.get('https://www.instagram.com/'+self.username+'/')

        sleep(2)

        self.followers_btn = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        self.followers_btn.click()

        sleep(2)

        followers_list = self.driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/ul')
        followers = followers_list.find_elements_by_tag_name('a')
        return [follower.text for follower in followers if follower.text != '']

    def get_followings(self):
        self.driver.get('https://www.instagram.com/'+self.username)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a').click()
        sleep(2)
        followings_list = self.driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/ul')
        sleep(2)
        followings = followings_list.find_elements_by_tag_name('a')
        return [following.text for following in followings if following.text != '']
        

ig_bot = MyInstaBot(input('Enter Your Username'), input('Enter you password'))
followers =  ig_bot.get_followers()
followings = ig_bot.get_followings()
unfollowers = [name for name in followings if name not in followers]
print(unfollowers)
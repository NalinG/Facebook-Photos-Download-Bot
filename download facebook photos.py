from selenium import webdriver
import argparse
import sys
import time
from selenium.webdriver import ActionChains
import argparse
import getpass
from pyvirtualdisplay import Display

def main(username, account_password,destination):
	profile = webdriver.FirefoxProfile()
	profile.set_preference('browser.download.folderList', 2) # custom location
	profile.set_preference('browser.download.manager.showWhenStarting', False)
	profile.set_preference('browser.download.dir', destination)
	profile.set_preference('browser.helperApps.neverAsk.saveToDisk', "image/png,image/jpeg")

	if not username == "NONE" and not account_password == "NONE" and not destination == "NONE":
		display = Display(visible=0, size=(800, 600))
        	display.start()
		driver = webdriver.Firefox(firefox_profile=profile)
		driver.get("https://www.facebook.com")

		email_id = driver.find_element_by_id("email")
		password = driver.find_element_by_id("pass")
		email_id.send_keys(username)
		password.send_keys(account_password)
		driver.find_element_by_id("loginbutton").click()
		# driver.find_element_by_css_selector("._5afe.sortableItem").click()
		driver.find_element_by_id("navItem_2305272732").click()
		time.sleep(3)
		list_of_images = driver.find_elements_by_css_selector(".uiMediaThumbImg")
		list_of_images[0].click()
		# print list_of_images
		for image in list_of_images:
			time.sleep(3)
			driver.find_element_by_xpath("//div[@class = 'overlayBarButtons rfloat _ohf']/div/div/a").click()
			time.sleep(3)
			option = driver.find_element_by_xpath("//div[@class = 'uiContextualLayerPositioner uiLayer']/div/div/div[@class = '_54ng']/ul[@class = '_54nf']/li[4]/a")
			option_name = option.find_element_by_xpath(".//*")
			option_name = option_name.find_element_by_xpath(".//*")
			if option_name.get_attribute('innerHTML').lower() == "download":
				option_name.click()
			# print option.get_attribute('innerHTML')
			driver.find_element_by_css_selector(".snowliftPager.next.hilightPager").click()

        	display.stop()

	else:
		print "\nIncomplete Parameters, Program is Shutting Down."


class Password(argparse.Action):
    def __call__(self, parser, namespace, values, option_string):
        if values is None:
            values = getpass.getpass()

        setattr(namespace, self.dest, values)

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('-u', type = str,help = "Enter your username",default = "NONE")
	parser.add_argument('-d', type = str,help = "Destination for your photos to download, please provide the full path",default = "NONE")
	parser.add_argument('-p', action=Password, nargs='?', dest='password', help='Enter your password',default = "NONE")
	args = parser.parse_args()
	main(args.u,args.password,args.d)




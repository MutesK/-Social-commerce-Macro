'''
	Social Commerce Shop Automatic Buy Marco Project

	Support Site
		1. Tmon
		2. Wemakeprice Not Support

	Using Library
		1. Selenium

	Flow
		1. Login
		2. Go to Shop Item Page
		3. Purchase Item - No Credit Card Just 'Depositless payment'
'''

from DriverAwaiter import DriverAwaiter
from COption import COption

chromedirver = "C://chromedriver.exe"
tmon_loginsrc = "https://login.ticketmonster.co.kr/user/loginform?return_url="
wemakeprice_login = ""

await_driver = DriverAwaiter(chromedirver, True)
# driver = webdriver.Chrome(chromedirver)

def login(user_id, user_pass, social_Type) :
	# 유저가 원하는 소셜커머스에 로그인해준다.
	await_driver.get(tmon_loginsrc)

	id = await_driver.await_find_element_by('userid')
	id.send_keys(user_id)

	password = await_driver.find_element_by_id('pwd')
	password.send_keys(user_pass)

	login_button = await_driver.find_element_by_class_name('btn_login')
	login_button.click()

	return 1;


def PurchaseItem(http_src) :
	print("Go to Item Page")

	await_driver.get(http_src)
	
	purchase = await_driver.find_element_by_xpath("//button[contains(text(), '바로구매')]")
	purchase.click()

	url = await_driver.get_driver().current_url
	SelectPurchaseOption(url)


def SelectPurchaseOption(url) :
	
	while True :
		if url != await_driver.get_driver().current_url :
			break

	await_driver.get_driver().implicitly_wait(3)

	# 티몬페이 결제 버튼
	radio = await_driver.find_element_by_xpath("//label[@class='radios tmonpay']/i[@class='ico']")
	radio.click()

	# 약관 동의
	checkbox = await_driver.find_element_by_xpath("//label[@class='checkBoxAll']/i[@class='ico']")
	checkbox.click()

	# 결제하기 클릭
	paybutton = await_driver.find_element_by_id("_confirmCheckout")
	paybutton.click()


def ReadMe() :
	print("=====================================")
	print("!!!!!!!!!사용시 주의사항!!!!!!!!!!!!!!");
	print("반드시, 사용하고자 하는 소셜커머스의 사이트의 로그인 방식이 SNS 로그인 방식을 사용하면 안됩니다.")
	print("사용하기 전에, 비밀번호가 오래되서 새로 설정하는 창이 있는지 체크해주세요.")
	print("만약 해당 상품 페이지에 구매하기 위해 구매 옵션설정해야 되는 경우에는 사용을 하지 않기를 권합니다.")
	print("모든 결제는 무통장으로 처리됩니다.")
	print("준비 되었다면, 아무키나 눌러주세요 ", end="")

	input()
	print("")



if __name__ == "__main__":
	ReadMe()

	# 1. Option Load
	option = COption("option.json");

	# 2. Login Process
	print("Go to Login Page")
	login(option.get_Userid(),  option.get_Userpass(), option.get_SocialCommerceType())

	# 3. Go To Item Purchase Page -> 구매 버튼이 활성화 될떄까지 대기할수 있는 기능이 필요함.
	PurchaseItem(option.get_PurchaseSrc())


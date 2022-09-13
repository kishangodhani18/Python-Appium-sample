from appium import webdriver

desired_caps = {
    "platformName": "Android",
    "deviceName": "bhihcjdicubdwijwdbc",
    "version": "9",
}

# Create driver and start launch the excution.
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

# Run your app page source and quite after run.
print(driver.page_source)
driver.quit()

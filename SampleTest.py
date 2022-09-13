from appium import webdriver

desired_caps = {
    # "platformName": "Android",
    # # Xiaomi Redmi Note 10
    # "deviceName": "b5af8c6b",
    # "version": "11",

    "platformName": "Android",
    # Samsung M20
    # "deviceName": "320194a65f3f56e9",
    "version": "9",
}

# Add your selenium grid appium public URL here.
driver = webdriver.Remote("http://15.206.213.81:4444", desired_caps)

# Run your app page source and quite after run.
print(driver.page_source)
driver.quit()



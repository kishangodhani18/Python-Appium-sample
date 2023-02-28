from appium import webdriver

desired_caps = {
    "platformName": "<iOS> & <Android>",
    "platformVersion": "<OS_Version>",
    "deviceName": "<Device_Name>",
    "automationName": "<XCUITest>__&__<Appium>",
    "app": "/path/to/<apk>__<ipa>"
}
}

# Create driver and start launch the excution.
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

# Run your app page source and quite after run.
print(driver.page_source)
driver.quit()

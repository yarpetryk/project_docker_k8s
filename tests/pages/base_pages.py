import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, WebDriverException, TimeoutException, InvalidElementStateException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import allure


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""
    def __init__(self, driver):
        self.driver = driver
        if type(self) is BasePage:
            raise Exception('BasePage() is an abstract class and cannot be instantiated directly.'
                            ' Please create your own class!')

    ###################################################################################################
    @allure.step
    def find_element_and_click(self, locator, timeout=10, return_bool=False):
        """
        Purpose:
            find element based on locator, make sure element is clickable, and click the element.
        Args:
            locator (e.g. AndroidLocators.DEFAULT_ANDROID_POPOVER_OK_BUTTON)
            (optional) timeout (int): How much time to wait before exception; default is 10 seconds
            (optional) return_bool (bool): Return bool instead of assertionError; default is False
        Returns:
            either bool or None depends on return_bool option
        """
        # this decides whether to fail the test if the element can't be found
        function_will_return_boolean = return_bool
        el = None
        try:
            el = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            if function_will_return_boolean:
                return False
            else:
                assert el is not None, 'element->{0} can\'t be found in find_element_and_click'.format(str(locator))

        else:
            try:
                el.click()
            except Exception:
                if function_will_return_boolean:
                    return False
                else:
                    el.click() # try again
            else:
                if function_will_return_boolean:
                    return True

    @allure.step
    def find_element(self, locator, timeout=10) -> bool:
        """
        Purpose:
            find element based on locator.
        Args:
            locator (e.g. AndroidLocators.DEFAULT_ANDROID_POPOVER_OK_BUTTON)
            (optional) timeout (int): How much time to wait before exception; default is 10 seconds
        Returns:
            bool
        """
        try:
            el = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            return False
        else:
            print(f"{el.text} is found")
            return el

    @allure.step
    def wait_until_element_will_be_invisible(self, locator, timeout=10) -> bool:
        """
          Purpose:
              find element based on locator and wait until locator will be invisible.
          Args:
              locator (e.g. AndroidLocators.DEFAULT_ANDROID_POPOVER_OK_BUTTON)
              (optional) timeout (int): How much time to wait before exception; default is 10 seconds
          Returns:
              bool
          """
        try:
            WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))
        except TimeoutException:
            return False
        else:
            return True

    @allure.step
    def is_element_selected(self, locator, timeout=3) -> bool:
        """
        Purpose:
            find element based on locator and see if the element is selected.
        Args:
            locator (e.g. AndroidLocators.DEFAULT_ANDROID_POPOVER_OK_BUTTON)
            (optional) timeout (int): How much time to wait before exception; default is 3 seconds
        Returns:
            bool
        """
        try:
            WebDriverWait(self.driver, timeout).until(EC.element_located_to_be_selected(locator))
        except TimeoutException:
            return False
        else:
            return True

    @allure.step
    def is_element_checked(self, locator, timeout=3) -> bool:
        """
        Purpose:
            find element based on locator and see if the element is checked.
        Args:
            locator (e.g. AndroidLocators.DEFAULT_ANDROID_POPOVER_OK_BUTTON)
            (optional) timeout (int): How much time to wait before exception; default is 3 seconds
        Returns:
            bool
        """
        try:
            el = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            assert el is not None, 'element->{0} can\'t be found for verifying'.format(str(locator))
        else:
            print(f"{el.text} is found")
            checked = el.get_attribute("checked")
            if checked == 'true':
                return True
            elif checked == 'false':
                return False
            else:
                print(f"the attribute {checked} is incorrect")

    def is_element_enabled(self, locator, timeout=10):
        """
                Purpose:
                    find element based on locator and see if the element is enabled.
                Args:
                    locator (e.g. AndroidLocators.DEFAULT_ANDROID_POPOVER_OK_BUTTON)
                    (optional) timeout (int): How much time to wait before exception; default is 3 seconds
                Returns:
                    bool
                """
        try:
            el = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            assert el is not None, 'element->{0} can\'t be found for verifying'.format(str(locator))
        else:
            print(f"{el.text} is found")
            enabled = el.get_attribute("enabled")
            if enabled == 'true':
                return True
            elif enabled == 'false':
                return False
            else:
                print(f"the attribute {enabled} is incorrect")

    def is_element_disabled(self, locator, timeout=3):
        """
                Purpose:
                    find element based on locator and see if the element is disabled.
                Args:
                    locator (e.g. AndroidLocators.DEFAULT_ANDROID_POPOVER_OK_BUTTON)
                    (optional) timeout (int): How much time to wait before exception; default is 3 seconds
                Returns:
                    bool
                """
        try:
            el = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            assert el is not None, 'element->{0} can\'t be found for verifying'.format(str(locator))
        else:
            print(f"{el.text} is found")
            enabled = el.get_attribute("enabled")
            if enabled == 'true':
                return False
            elif enabled == 'false':
                return True
            else:
                print(f"the attribute {enabled} is incorrect")

    @allure.step
    def is_element_invisible(self, locator, timeout=10) -> bool:
        """
        Purpose:
            find element based on locator and check that an element is either invisible or not present on the DOM.
        Args:
            locator (e.g. AndroidLocators.DEFAULT_ANDROID_POPOVER_OK_BUTTON)
            (optional) timeout (int): How much time to wait before exception; default is 3 seconds
        Returns:
            bool
        """
        try:
            WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element(locator))
        except TimeoutException:
            return False
        else:
            return True

    @allure.step
    def is_element_clickable(self, locator, timeout=5) -> bool:
        """
        Purpose:
            find element based on locator and check is visible and enabled such that you can click it.
        Args:
            locator (e.g. AndroidLocators.DEFAULT_ANDROID_POPOVER_OK_BUTTON)
            (optional) timeout (int): How much time to wait before exception; default is 3 seconds
        Returns:
            bool
        """
        try:
            WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            print(f"{locator} is not clickable")
            return False
        else:
            print(f"{locator} is clickable")
            return True

    @allure.step
    def check_element_equal(self, locator, target : str, timeout=10) -> bool:
        """
        Purpose:
            check if an element's text is equal to the string passed in
        Args:
            locator (e.g. AndroidLocators.DEFAULT_ANDROID_POPOVER_OK_BUTTON)
            target (str): the input string to be passed in
            (optional) timeout (int): How much time to wait before exception; default is 3 seconds
        Returns:
            bool
        """
        try:
            b = WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element(locator, target))
            if b:
                print(f"{locator} is equal to {target}")
                return True
            else:
                return False
        except TimeoutException:
            return False

    @allure.step
    def find_element_and_send_key(self, locator, input : str, timeout=10, clear=False) -> None:
        """
        Purpose:
            find element based on locator and input string to its text field
        Args:
            locator (e.g. AndroidLocators.DEFAULT_ANDROID_POPOVER_OK_BUTTON)
            input (str): the input string to be passed in
            (optional) timeout (int): How much time to wait before exception; default is 10 seconds
            (optional) clear (bool): whether to clear the text field first before the input
        Returns:
            Nothing
        Raises:
            assertionError if element does not accept input
        """
        el = None
        try:
            el = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        except Exception:
            assert el is not None, 'element->{0} can\'t be found for input'.format(str(locator))
        else:
            if clear:
                el.clear()
            try:
                el.send_keys(input)
            except InvalidElementStateException:
                assert False, "element does not accept input"
            else:
                print("sending key " + input)

    @allure.step
    def find_all_elements(self, locator, timeout=5) -> list:
        try:
            els = WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))
        except Exception:
            return False
        else:
            return els

    @allure.step
    def get_text_in_element_from_page_source_by_xpath(self, xpath, attempts=10):
        """
        Find the element and get text based on locator from the page source
        Args:
            xpath (e.g. ".//android.widget.TextView[@resource-id='com.pltsci.hos:id/txtDuration']")
            attempts: number of attempts re-search element by xpath
            It's not standard xpath, for the more information about rules for writing xpath go to
            https://docs.python.org/3/library/xml.etree.elementtree.html#supported-xpath-syntax
        """
        # Get page source
        page_source = self.driver.page_source
        # Parsing XML from the page source
        tree = ET.ElementTree(ET.fromstring(page_source))
        # Get the root element for this tree
        root = tree.getroot()
        # Find element by xpath
        xml_el = root.find(xpath)
        try:
            # Try to find text attribute
            text = xml_el.get('text')
        except AttributeError as er:
            # If thrown the attribute error try to find element again
            if attempts > 0:
                text = self.get_text_in_element_from_page_source_by_xpath(xpath=xpath, attempts=attempts - 1)
            else:
                # If the element does not found after all at
                assert False, f"element->{xpath} can\'t be found in Page Source, check please you locator. Error message: {er}"
        # Return the text attribute
        return text

    @allure.step("Then we should see soft keyboard appear")
    def is_keyboard_appear(self):
        time.sleep(3)  # Give time to appear keyboard
        return self.driver.is_keyboard_shown()

    @allure.step
    def find_element_and_focus(self, locator, timeout=25, return_bool=False):
        """
        Purpose:
            find element based on locator, and focus on the element, and click
        Args:
            locator (e.g. AndroidLocators.DEFAULT_ANDROID_POPOVER_OK_BUTTON)
            (optional) timeout (int): How much time to wait before exception; default is 10 seconds
            (optional) return_bool (bool): Return bool instead of assertionError; default is False
        Returns:
            either bool or None depends on return_bool option
        """
        # this decides whether to fail the test if the element can't be found
        function_will_return_boolean = return_bool
        el = None
        try:
            el = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            action = ActionChains(self.driver)
        except TimeoutException:
            if function_will_return_boolean:
                return False
            else:
                assert el is not None, 'element->{0} can\'t be found in find_element_and_click'.format(str(locator))

        else:
            try:
                el.blur()
            except Exception:
                if function_will_return_boolean:
                    return False
                else:
                    action.click_and_hold(on_element = el).perform()
            else:
                if function_will_return_boolean:
                    return True

    @allure.step
    def go_to_webpage(self, url):
        """
        Purpose:
            navigagate to the webpage based on url.
        Args:
            url: target url to navigate
        """
        # navigate to the webpage
        try:
            self.driver.get(url)
        except WebDriverException:
            return False
        else:
            print(f"navigation to the {url} is done")
            return True

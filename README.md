# Selenium Automation Script 🖥️  

This repository contains a Python script for automating browser interactions using Selenium WebDriver. It provides examples of various Selenium methods to perform tasks such as navigation, element interaction, and more.

---

## 🚀 Features  
- Open and interact with web pages.  
- Automate browser actions like clicking, typing, and navigating.  
- Manage browser cookies, alerts, and frames.  
- Perform window and tab management.  

---

## 📝 Usage  

### 1. Clone the Repository  
```bash  
git clone https://github.com/username/repository-name.git  
```

### 2. Install Dependencies
```bash  
pip install selenium  
```
### 3. Run the Script
Make sure you have ChromeDriver installed and set up before running the script.
```bash  
python script.py  
```

## 📚 Resources
[Selenium with Python Guide](https://selenium-python.readthedocs.io/)


## Some More Methods

| **Method**                         | **Description**                                                                   |
|-------------------------------------|-----------------------------------------------------------------------------------|
| `get(url)`                          | Opens a specified URL in the browser.                                             |
| `minimize_window()`                 | Minimizes the current window.                                                     |
| `maximize_window()`                 | Maximizes the current window.                                                     |
| `refresh()`                         | Refreshes the current web page.                                                   |
| `current_url`                       | Retrieves the URL of the current page.                                            |
| `quit()`                            | Closes all browser windows and terminates the WebDriver session.                  |
| `find_element(By.selector)`         | Finds an element using the given selector.                                        |
| `find_elements(By.selector)`        | Finds all elements matching the given selector.                                   |
| `click()`                           | Simulates a mouse click on the element.                                           |
| `send_keys(keys)`                   | Types the specified keys into an input field.                                     |
| `back()`                            | Navigates to the previous page in history.                                        |
| `forward()`                         | Moves to the next page in history.                                               |
| `assert "text" in driver.title`     | Validates that the title contains the specified text.                             |
| `get_title()`                       | Gets the title of the current page.                                               |
| `get_window_position()`             | Returns the position of the current window.                                       |
| `get_window_size()`                 | Returns the size of the current window.                                           |
| `switch_to.frame()`                 | Switches focus to a specified frame.                                              |
| `switch_to.default_content()`       | Switches focus back to the main content.                                          |
| `switch_to.alert()`                 | Switches focus to the current alert box.                                          |
| `accept()`                          | Accepts the current alert.                                                        |
| `dismiss()`                         | Dismisses the current alert.                                                      |
| `send_keys_to_alert(text)`          | Sends text to the current alert.                                                  |
| `get_cookies()`                     | Returns all cookies for the current domain.                                       |
| `add_cookie(cookie_dict)`           | Adds a cookie to the current session.                                             |
| `delete_cookie(name)`               | Deletes a specific cookie by name.                                                |
| `delete_all_cookies()`              | Deletes all cookies in the current session.                                       |
| `execute_script(script)`            | Executes a JavaScript script in the context of the current page.                  |
| `execute_async_script(script)`      | Executes an asynchronous JavaScript script.                                       |
| `get_window_handles()`              | Retrieves all window handles for the current session.                             |
| `switch_to.window(handle)`          | Switches focus to the window with the given handle.                               |
| `close()`                           | Closes the current window.                                                        |
| `get_screenshot_as_file(filename)`  | Captures a screenshot of the current page and saves it to a file.                 |
| `get_screenshot_as_base64()`        | Captures a screenshot and returns it as a base64-encoded PNG image.               |
| `get_screenshot_as_png()`           | Captures a screenshot and returns it as a PNG image.                              |
| `find_element_by_id(id)`            | Finds an element by its ID attribute.                                              |
| `find_element_by_name(name)`        | Finds an element by its name attribute.                                            |
| `find_element_by_class_name(name)`  | Finds an element by its class name.                                               |
| `find_element_by_tag_name(name)`    | Finds an element by its tag name.                                                 |
| `find_element_by_xpath(xpath)`      | Finds an element by its XPath expression.                                         |
| `find_element_by_css_selector(css)` | Finds an element by its CSS selector.                                             |
| `find_elements_by_id(id)`           | Finds multiple elements by their ID attribute.                                    |
| `find_elements_by_name(name)`       | Finds multiple elements by their name attribute.                                  |
| `find_elements_by_class_name(name)` | Finds multiple elements by their class name.                                      |
| `find_elements_by_tag_name(name)`   | Finds multiple elements by their tag name.                                        |
| `find_elements_by_xpath(xpath)`     | Finds multiple elements by their XPath expression.                               |
| `find_elements_by_css_selector(css)`| Finds multiple elements by their CSS selector.                                    |
| `set_page_load_timeout(time)`       | Sets the amount of time to wait for a page to load before throwing an error.       |
| `set_script_timeout(time)`          | Sets the amount of time to wait for a script to finish before throwing an error.   |
| `implicitly_wait(time)`             | Sets an implicit wait time for locating elements.                                 |
| `clear()`                           | Clears the value of an input element.                                             |
| `is_displayed()`                    | Checks if an element is visible on the page.                                      |
| `is_enabled()`                      | Checks if an element is enabled.                                                  |
| `is_selected()`                     | Checks if an element is selected (e.g., checkboxes, radio buttons).                |
| `get_attribute(attribute_name)`     | Gets the value of a specified attribute from an element.                          |
| `get_text()`                        | Retrieves the visible text within an element.                                     |
| `get_css_value(property_name)`      | Retrieves the CSS value of a specified property of an element.                    |
| `submit()`                          | Submits a form (similar to clicking the submit button).                           |
| `scroll_to_element(element)`        | Scrolls the page to bring the specified element into view.                        |
| `scroll_to_top()`                   | Scrolls the page to the top.                                                     |
| `scroll_to_bottom()`                | Scrolls the page to the bottom.                                                  |
| `wait.until(condition)`             | Waits for a specified condition to be met before proceeding.                      |
| `alert.text()`                      | Retrieves the text of the current alert box.                                      |
| `alert.send_keys(keys)`             | Sends keys to the current alert box.                                              |
| `alert.accept()`                    | Accepts the alert.                                                               |
| `alert.dismiss()`                   | Dismisses the alert.                                                             |
| `alert.is_displayed()`              | Checks if an alert is currently displayed.                                        |
| `get_log(type)`                     | Retrieves logs of the specified type (e.g., "browser", "driver", etc.).           |



![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)

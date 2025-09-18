

class AddUserLocator:
    select = "//div[@class='oxd-input-group__label-wrapper']//label[text()='{}']/../..//div[@class='oxd-select-wrapper']"
    dropdown = "//div[@class='oxd-select-dropdown --positon-bottom']//span[text()='{}']"
    input = "//div[@class='oxd-input-group__label-wrapper']//label[text()='{}']/../..//input"
    click_EmployeeName = "div.oxd-autocomplete-dropdown.--positon-bottom span"
    button = "//div[@class='oxd-form-actions']//button[text()=' {} ']"
    alert_success = "//div[@class='oxd-toast-container oxd-toast-container--bottom']//div[@class='oxd-toast-content oxd-toast-content--success']//p[text()='Successfully Saved']"
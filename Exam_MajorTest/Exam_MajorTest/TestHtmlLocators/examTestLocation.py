def documentation_logo():
    return "(//img[@alt='GNU'])[2]"

def header_validate(i):
    return "  // ul[ @ id = 'nav'] // a[text()='"+i+"']"

def campusLife():
    return "// ul[ @ id = 'nav'] // a[text()='Campus Life']"
def gallery():
    return "//h2[text()='  Gallery ']"

def images():
    return "//div[@class='card-columns']//img"

def validateNewslater():
    return "//h3[text()='Do you want notification?']"

def validateEMailText():
    return "//input[@placeholder='Enter Your Email Here']"
def subscribeClick():
    return "//button[text()='Subscribe']","//strong[text()='The email field is required.']"

def international():
    return "// ul[ @ id = 'nav'] // a[text()='International']"

def courseyears():
    return "(//div[@class='card my-3']/div[2]//p[@class='course-details-content mb-0'])[1]"

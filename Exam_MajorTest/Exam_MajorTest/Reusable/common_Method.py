from xml.dom import minidom

def readXmlAsPerNode(your_test_param):
    #it will give path of current project
    #first_parse_xml=minidom.parse(str(Path(__file__).parent.parent)+"/TestData.xml")
    first_parse_xml = minidom.parse("C:/Users/158202/PycharmProjects/Exam_MajorTest/TestData/testData.xml")
    data= first_parse_xml.getElementsByTagName(your_test_param)[0]

    return data.firstChild.data
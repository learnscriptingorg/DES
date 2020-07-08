import xml.etree.ElementTree as ET
tree = ET.parse('data.xml')
root = tree.getroot()
# # for child in root:
# #   print(child.tag, child.attrib)
# # #BR Names
# # eles=root.findall("./statistics/tag/stat")
# # for i in eles:
# #     print(i.text)
#
# def cccc():
#     eles = root.findall(".//test")
#     print(type(eles))
#     print(eles)
#     count=0
#     for i in eles:
#         d={}
#         print(i.attrib)
#         print("Count :",count)
#         count+=1
#
#     # eles = root.findall("./suite/suite")
#     # print(type(eles))
#     # sr=root.find("./suite/suite")
#     #
#     # print(type(sr))
#     # for i in eles:
#     #     print(i.attrib.get("name"))
#
# def df(tn="Auroral Sanity Suite"):
#     eles = root.findall("./suite/suite")
# cccc()
def get_all_suite_names():
    snames=[]
    data = root.findall("./suite/suite")
    for i in data:
        snames.append(i.attrib.get('name'))
    return snames
print(get_all_suite_names())

# def get_all_auroral_test_case_names(suite_name):
#     tcnames=[]
#     snames = get_all_suite_names()
#     if suite_name in snames:
#         search_str = ".//*[@name='" + suite_name + "']/test"
#         data = root.findall(search_str)
#         # for value in data:
#         #     print(value.find('doc').text)
#         for j in data:
#             tcnames.append(j.attrib.get('name'))
#     return tcnames
# test_case_list = get_all_auroral_test_case_names("Auroral Sanity Suite")
# print("auroral test case list")
# # for i in test_case_list:
# #     print (i)
# for i in test_case_list:
#     print(i)
#     search_str = ".//*[@name='" + i + "']/status"
#     data = root.findall(search_str)
#     for value in data:
#         print(value.attrib)
#     search_str = ".//*[@name='" + i + "']/tags"
#     data = root.findall(search_str)
#     for value in data:
#         print(value.find('tag').text)
import xml.etree.ElementTree as ET
tree = ET.parse('data.xml')
root = tree.getroot()
tests=root.findall(".//test")
data_set=[]
count=0
for i in tests:
    in_data={}
    tc_name=i.get("name")
    #print("Test Case Name:",tc_name)
    #print("Test Case Data",i.attrib)
    in_data.update(i.attrib)
    x_path=".//*[@name='"+str(tc_name)+"']"+"/.."
    suite_name=root.find(x_path)
    #print("Suite Name:",suite_name.attrib.get('name'))
    in_data.update({'Suite Name':suite_name.attrib.get('name')})
    #print(i.find(".//status").attrib)
    in_data.update(i.find(".//status").attrib)
    #print(root.find(".//*[@name='"+str(tc_name)+"']/status").text)
    in_data.update({'output':root.find(".//*[@name='"+str(tc_name)+"']/status").text})
    print(in_data)
    count+=1
    print(count)
    break

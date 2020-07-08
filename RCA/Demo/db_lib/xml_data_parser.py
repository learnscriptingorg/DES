import xml.etree.ElementTree as ET
def get_data():
    tree = ET.parse('data.xml')
    root = tree.getroot()
    tests=root.findall(".//test")
    data_set=[]
    count=0
    for i in tests:
        in_data={}
        in_data.update({'build_id':1000})
        tc_name=i.get("name")
        #print("Test Case Name:",tc_name)
        #print("Test Case Data",i.attrib)
        in_data.update(i.attrib)
        x_path=".//*[@name='"+str(tc_name)+"']"+"/.."
        suite_name=root.find(x_path)
        #print("Suite Name:",suite_name.attrib.get('name'))
        in_data.update({'suite':suite_name.attrib.get('name').replace(' ','_')})
        #print(i.find(".//status").attrib)
        in_data.update(i.find(".//status").attrib)
        #print(root.find(".//*[@name='"+str(tc_name)+"']/status").text)
        output=root.find(".//*[@name='"+str(tc_name)+"']/status").text
        try:
            output=output.replace("\n", " ")
        except:
            print("Output is null",output)
        try:
            output=output.replace("'", " ")
        except:
            print("Output is null",output)
        #print("Output********",output)
        in_data.update({'output':output})
        #print(in_data)
        #count+=1
        #print(count)
        data_set.append(in_data)

    return data_set

if __name__=="__main__":
    print(get_data())
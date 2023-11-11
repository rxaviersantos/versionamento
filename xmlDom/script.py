from xml.dom import minidom

root = minidom.Document()

xml = root.createElement('root')
root.appendChild(xml)

productChild = root.createElement('aula')
productChild.setAttribute('name', 'Rodrigo')

xml.appendChild(productChild)

xml_str = root.toprettyxml(indent ="\t")

save_path_file = "xml-example.xml"

with open(save_path_file, "w") as f:
    f.write(xml_str)
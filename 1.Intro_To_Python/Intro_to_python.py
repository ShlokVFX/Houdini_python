def createSomeNodes():
    obj = hou.node("/obj")
    geoNode = obj.createNode("geo", "My_Geo")
    boxNode = geoNode.createNode("box", "My_Box")
    sphereNode = geoNode.createNode("sphere", "My_Sphere")
    
    boxNode.setInput(0, sphereNode, 0)
    
    sphereNode.setDisplayFlag(1)
    sphereNode.setRenderFlag(1)
    
def createSubnet():
    obj = hou.node("/obj")
    subnet = obj.createNode("subnet", "New_HDA")
    geoNode = subnet.createNode("geo", "Geo")
    
    boxNode = geoNode.createNode("box", "My_Box")
    sphereNode = geoNode.createNode("sphere", "My_Sphere")
    
    mergeNode = geoNode.createNode("merge", "Merge_Geo")
    mergeNode.setInput(0, boxNode, 0)
    mergeNode.setInput(1, sphereNode, 0)
    mergeNode.setDisplayFlag(1)
    mergeNode.setRenderFlag(1)
    
    hou.ui.displayMessage("Created New Subnet!", buttons=('ok', 'cancel'))
    
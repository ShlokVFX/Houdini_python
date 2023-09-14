def exportAllBarrels():
    exportPath = "$HIP/Assets/"
    obj = hou.node("/obj")
    children = obj.children()
    
    for node in children:
        nodeName = node.name()
        finalPath = exportPath + nodeName + ".fbx"
        
        node.parm("sopoutput").set(finalPath)
        node.parm("execute").pressButton()
        
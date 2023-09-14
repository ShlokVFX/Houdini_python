#inside scripts inside HDA module

def exportAllParts(parent):
   
    #get all child nodes
    frac_node = parent.node('Fracture')
    unique_node = frac_node.node('FIND_UNIQUE_VALUES')
    export_node = parent.node('export')
    rop_node = parent.node('ropnet1').node('filmboxfbx1')
    
    #clear out the subnet
    children = export_node.children()
    for child in children:
        child.destroy()
    
    #get all detail attrib
    geo = unique_node.geometry()
    attrib = geo.findGlobalAttrib('names')
    names = geo.stringListAttribValue(attrib)
    
    #loop through the array
    for name in names:
     new_geo = export_node.createNode('geo', name)
     merge_node = new_geo.createNode('object_merge')
     blast_node = new_geo.createNode('blast')
     
     blast_node.setInput(0 , merge_node , 0)
     blast_node.setDisplayFlag(True)
     blast_node.setRenderFlag(True)
  
     #set params
     merge_node.parm('objpath1').set('/obj/Fracture_export_parts/Fracture/OUT_FRACTURE')
     blast_node.parm('group').set('@name='+name)
     blast_node.parm('negate').set(True)
     
     rop_node.parm('execute').pressButton()
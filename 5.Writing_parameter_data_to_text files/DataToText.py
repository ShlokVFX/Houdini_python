#inside scripts inside hda


def export_params(kwargs):

    #Get Parent Node
    parent = kwargs['node']
    
    #get Params
    uniformscale = str(parent.parm('scale').eval())
    radiusx = str(parent.parm('radx').eval())
    radiusy = str(parent.parm('rady').eval())
    radiusz = str(parent.parm('radz').eval())
 
    #Write to Text File
    lines = [uniformscale,radiusx,radiusy,radiusz]
    
    path = "D:/Visual studio/HOUDINI_PYTHON/Houdini_python/5.Writing_parameter_data_to_text files/hda_settings.txt"
    f = open(path , 'w')
    f.writelines(lines)
    f.close()
    
#inside Shlef tools script

# get the obj context and create geo container
obj = hou.node('/obj')
geo_node = obj.createNode('geo', 'fx_source')

# create all the nodes
sphere_node = geo_node.createNode('sphere')
mountain_node = geo_node.createNode('mountain::2.0')
clip_node = geo_node.createNode('clip')
polyfill_node = geo_node.createNode('polyfill')

#setInput
mountain_node.setInput(0, sphere_node, 0)
clip_node.setInput(0, mountain_node, 0)
polyfill_node.setInput(0, clip_node, 0)

#layout Children
geo_node.layoutChildren()

#Display/Render Flag
polyfill_node.setDisplayFlag(True)
polyfill_node.setRenderFlag(True)

#set params
sphere_node.parm('type').set(1)
polyfill_node.parm('fillmode').set(0)

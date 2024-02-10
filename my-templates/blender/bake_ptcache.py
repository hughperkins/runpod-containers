import bpy

# for scene in bpy.data.scenes:
#     print('scene', scene)
#     for object in scene.objects:
#         print('object', object)
#         for modifier in object.modifiers:
#             print('modifier', modifier, 'modifier_type', modifier.type)

# for area in bpy.context.screen.areas:
#     print(area.type)
#     if area.type == 'PROPERTIES':
#         print('dir(area.spaces)', dir(area.spaces))
#         for name, space in area.spaces.items():
#             print(name, space)
#         print('area.spaces[0]', area.spaces[0])
#         sp = area.spaces[0]
#         print('dir(sp)', dir(sp))
#         print('sp.context', sp.context)
#         print('area.spaces.active', area.spaces.active)
#         print('area.spaces[0]', area.spaces[0])
#         print('area.spaces.active == area.spaces[0]', area.spaces.active == area.spaces[0])
#         active_space = area.spaces.active
#         active_space.context = 'SCENE'
#         override = bpy.context.copy()
#         override["area"] = area
#         print('override', override)
#         for k, v in override.items():
#             print('    ', k, v)
#         # bg = space_data.background_images.new()
#         # bg.image = img
#         with bpy.context.temp_override(**override):
#             # bpy.context.space_data.context = 'SCENE'
#             print('area', bpy.context.area, bpy.context.area.type, bpy.context.area.ui_type, dir(bpy.context.area))
#             print('space_data', bpy.context.space_data, bpy.context.space_data.type, bpy.context.space_data.context, dir(bpy.context.space_data))
#             print('scene', bpy.context.scene, bpy.context.scene.name)
#             bpy.ops.ptcache.bake(bake=True)
#         break

# bpy.context.area.ui_type = 'PROPERTIES'
# bpy.context.space_data.context = 'SCENE'

# bpy.ops.ptcache.bake(bake=True)
# bpy.ops.wm.save_mainfile()

bpy.ops.ptcache.bake_all(bake=True)
bpy.ops.wm.save_mainfile()

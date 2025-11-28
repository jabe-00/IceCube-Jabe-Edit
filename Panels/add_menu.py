import bpy
from ..icons import ice_cube_icons_collection

class ICECUBE_Label(bpy.types.Menu):
    bl_label = "IceCube Label"
    bl_idname = "ICECUBE_Label"

    def draw(self, context):
        layout = self.layout
        pcoll = ice_cube_icons_collection["ice_cube_remake"]

        layout.menu("ICECUBE_RIG", text="Ice Cube Options", icon_value=pcoll['ice_cube_logo'].icon_id)


class ICECUBE_RIG(bpy.types.Menu):
    bl_label = "Ice Cube Options"
    bl_idname = "ICECUBE_RIG"

    def draw(self, context):
        layout = self.layout
        pcoll = ice_cube_icons_collection["ice_cube_remake"]

        layout.operator("ice_cube.append_ice_cube_10px", text="Append Ice Cube (10px)", icon_value=pcoll['ice_cube_logo'].icon_id)
        layout.operator("ice_cube.append_ice_cube", text="Append Ice Cube (Default)", icon_value=pcoll['ice_cube_logo'].icon_id)
        layout.operator("ice_cube.append_ice_cube_14px", text="Append Ice Cube (14px)", icon_value=pcoll['ice_cube_logo'].icon_id)

def AddMenuFunction(self, context): 
    layout = self.layout
    pcoll = ice_cube_icons_collection["ice_cube_remake"]
    layout.menu("ICECUBE_Label", text="Ice Cube Menu", icon_value=pcoll['ice_cube_logo'].icon_id)
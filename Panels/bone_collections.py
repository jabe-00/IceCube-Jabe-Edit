import bpy

from ..constants import RIG_ID
from ..ice_cube_selectors import GetBoneCollection

def toggleButton(obj, pos, propName, text=""):
    context = "Show"
    if(getattr(obj, propName, True)):
        context = "Hide"
    text = text.replace("s/h", context)
    context = "SHOW"
    if(getattr(obj, propName, True)):
        context = "HIDE"
    text = text.replace("S/H", context)
    if(getattr(obj, propName, True)):
        pos.prop(obj, propName, toggle=True, text=text)
    else:
        pos.prop(obj, propName, toggle=True, text=text)
    return getattr(obj, propName, True)

class BoneCollectionManager():
    def new_bone_layer(self, context, layout, layer_id,text, icon="NONE"):
        collections = context.active_object.data.collections_all
        bone_collection = GetBoneCollection(collections, layer_id)
        if bone_collection:
            layout.prop(bone_collection, 'is_visible',toggle=True,text=text,icon=icon)

# -------------------------------------------------------------------
# MAIN CONTAINER PANEL
# -------------------------------------------------------------------
class ICECUBERIG_PT_BoneCollections(bpy.types.Panel):
    bl_label = "Bone Collections"
    bl_idname = "ICECUBERIG_PT_BoneCollections"
    bl_space_type = "VIEW_3D"
    bl_region_type = 'UI'
    bl_category = "Ice Cube v2"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(self, context):
        active_object = bpy.context.active_object
        try:
            return (active_object.data.get("rig_id") == RIG_ID)
        except (AttributeError, KeyError, TypeError):
            return False
    
    def draw_header(self, context):
        self.layout.label(text="",icon='BONE_DATA')

    def draw(self, context):
        pass


class ICECUBERIG_PT_Bones(bpy.types.Panel):
    bl_label = "Bones"
    bl_idname = "ICECUBERIG_PT_Bones"
    bl_space_type = "VIEW_3D"
    bl_region_type = 'UI'
    bl_parent_id = "ICECUBERIG_PT_BoneCollections" 
    bl_options = {'HEADER_LAYOUT_EXPAND'}

    @classmethod
    def poll(self, context):
        active_object = bpy.context.active_object
        try:
            return (active_object.data.get("rig_id") == RIG_ID)
        except (AttributeError, KeyError, TypeError):
            return False

    def draw(self, context):
        layout = self.layout
        row = layout.row(align=True)

        # HEAD BONES
        head_col = row.column(align=True)
        head_row = head_col.row(align=True)
        BoneCollectionManager.new_bone_layer(self,context,head_row,'ice_cube.head',"Head")
        BoneCollectionManager.new_bone_layer(self,context,head_row,'ice_cube.facial',"Facial")
        head_row = head_col.row(align=True)
        BoneCollectionManager.new_bone_layer(self,context,head_row,'ice_cube.blink_pos',"Blink Pos")
        BoneCollectionManager.new_bone_layer(self,context,head_row,'ice_cube.facial_tweaks',"Tweak")
        head_row = head_col.row(align=True)
        
        # WRINKLE BONES
        BoneCollectionManager.new_bone_layer(self,context,head_row,'ice_cube.wrinkles',"Wrinkles")
        row = layout.row(align=True)

        # ARM BONES
        row = layout.row(align=True)
        right_arm_col = row.column(align=True)
        left_arm_col = row.column(align=True)

        BoneCollectionManager.new_bone_layer(self,context,left_arm_col,'ice_cube.left_arm',"Left Arm")
        BoneCollectionManager.new_bone_layer(self,context,left_arm_col,'ice_cube.left_arm_fk',"FK Bones")
        BoneCollectionManager.new_bone_layer(self,context,left_arm_col,'ice_cube.left_arm_ik',"IK Bones")
        BoneCollectionManager.new_bone_layer(self,context,left_arm_col,'ice_cube.left_arm_tweak',"Tweaks")
        BoneCollectionManager.new_bone_layer(self,context,left_arm_col,'ice_cube.left_finger_tweaks',"Finger Tweaks")

        BoneCollectionManager.new_bone_layer(self,context,right_arm_col,'ice_cube.right_arm',"Right Arm")
        BoneCollectionManager.new_bone_layer(self,context,right_arm_col,'ice_cube.right_arm_fk',"FK Bones")
        BoneCollectionManager.new_bone_layer(self,context,right_arm_col,'ice_cube.right_arm_ik',"IK Bones")
        BoneCollectionManager.new_bone_layer(self,context,right_arm_col,'ice_cube.right_arm_tweak',"Tweaks")
        BoneCollectionManager.new_bone_layer(self,context,right_arm_col,'ice_cube.right_finger_tweaks',"Finger Tweaks")
        row = layout.row(align=True)

        # BODY BONES
        row = layout.row(align=True)
        body_col = row.column(align=True)
        body_row = body_col.row(align=True)
        BoneCollectionManager.new_bone_layer(self,context,body_row,'ice_cube.body',"Body")
        BoneCollectionManager.new_bone_layer(self,context,body_row,'ice_cube.body_tweak',"Tweak")
        body_row = body_col.row(align=True)
        BoneCollectionManager.new_bone_layer(self,context,body_row,'ice_cube.shoulders',"Shoulders")
        row = layout.row(align=True)

        # WORLD BONES
        row = layout.row(align=True)
        world_col = row.column(align=True)
        world_row = world_col.row(align=True)
        
        BoneCollectionManager.new_bone_layer(self, context, world_row, 'ice_cube.world_bones', "World Bones")

        collections = context.active_object.data.collections_all
        world_bone_col = GetBoneCollection(collections, 'ice_cube.world_bones')

        if world_bone_col and world_bone_col.is_visible:
            box = world_col.box()
            box.label(text="Tools")
            
            col = box.column(align=True)
            
            col.operator("ice_cube.bring_world_bone", text="Bring World Bone", icon='SNAP_ON')
            
            col.separator()
            
            row_cp = col.row(align=True)
            row_cp.operator("ice_cube.copy_transform", text="Copy", icon='COPYDOWN')
            row_cp.operator("ice_cube.paste_transform", text="Paste", icon='PASTEDOWN')

        row = layout.row(align=True)
            

        # LEG BONES
        row = layout.row(align=True)
        right_leg_col = row.column(align=True)
        left_leg_col = row.column(align=True)

        BoneCollectionManager.new_bone_layer(self,context,left_leg_col,'ice_cube.left_leg',"Left Leg")
        BoneCollectionManager.new_bone_layer(self,context,left_leg_col,'ice_cube.left_leg_ik',"IK Bones")
        BoneCollectionManager.new_bone_layer(self,context,left_leg_col,'ice_cube.left_leg_fk',"FK Bones")
        BoneCollectionManager.new_bone_layer(self,context,left_leg_col,'ice_cube.left_leg_tweak',"Tweak")

        BoneCollectionManager.new_bone_layer(self,context,right_leg_col,'ice_cube.right_leg',"Right Leg")
        BoneCollectionManager.new_bone_layer(self,context,right_leg_col,'ice_cube.right_leg_ik',"IK Bones")
        BoneCollectionManager.new_bone_layer(self,context,right_leg_col,'ice_cube.right_leg_fk',"FK Bones")
        BoneCollectionManager.new_bone_layer(self,context,right_leg_col,'ice_cube.right_leg_tweak',"Tweak")
        row = layout.row(align=True)

        # JABE EDIT # 
        row = layout.row(align=True)
        
        internal = row.column(align=True)
        BoneCollectionManager.new_bone_layer(self,context,internal,'ice_cube.internal',"Internal")


class ICECUBERIG_PARENT_TREE(bpy.types.Panel):
    bl_label = "Parent Tree"
    bl_space_type = "VIEW_3D"
    bl_region_type = 'UI'
    bl_category = "Ice Cube v2"
    bl_parent_id = "ICECUBERIG_PT_BoneCollections"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(self, context):
        active_object = bpy.context.active_object
        try:
            return (active_object.data.get("rig_id") == RIG_ID)
        except (AttributeError, KeyError, TypeError):
            return False

    def draw_header(self, context):
        self.layout.label(text="",icon='ORIENTATION_PARENT')

    def draw(self, context):

        layout = self.layout
        pose_bones = context.active_object.pose.bones
        obj = context.active_object
        row = layout.row(align=True)

        grid = row.column(align=True)

        grid.prop(pose_bones['Left Arm IK'], '["IK Parent"]', text='Left Arm Parent', toggle=True)
        grid.prop(pose_bones['Right Arm IK'], '["IK Parent"]', text='Right Arm Parent', toggle=True)
        grid.prop(pose_bones['Left Leg IK'], '["IK Parent"]', text='Left Leg Parent', toggle=True)
        grid.prop(pose_bones['Right Leg IK'], '["IK Parent"]', text='Right Leg Parent', toggle=True)
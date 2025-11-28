import bpy
from ..constants import RIG_ID


class ICECUBERIG_PT_Workflow(bpy.types.Panel):
    bl_label = "Workflow"
    bl_idname = "ICECUBERIG_PT_Workflow"
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
        self.layout.label(text="", icon='PROPERTIES')

    def draw(self, context):
        layout = self.layout
        obj = context.object

        row = layout.row(align=True)
        row.prop(obj, "performance_mode", text="Performance Mode", toggle=True)


# -------------------------------------------------------------------
# SUB-PAINEL: ARM SETTINGS
# -------------------------------------------------------------------
class ICECUBERIG_PT_ArmSettings(bpy.types.Panel):
    bl_label = "Arm Settings"
    bl_idname = "ICECUBERIG_PT_ArmSettings"
    bl_space_type = "VIEW_3D"
    bl_region_type = 'UI'
    bl_parent_id = "ICECUBERIG_PT_Workflow" 
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(self, context):
        active_object = bpy.context.active_object
        try:
            return (active_object.data.get("rig_id") == RIG_ID)
        except (AttributeError, KeyError, TypeError):
            return False
            
    def draw_header(self, context):
        self.layout.label(text="", icon='BONE_DATA')

    def draw(self, context):
        layout = self.layout
        obj = context.object
        
        row = layout.row(align=True)
        split = row.split(factor=0.5)
        
        left_col = split.column(align=True)
        right_col = split.column(align=True)
        
        # Left Arm
        left_col.prop(obj, "left_arm_ik", text="Left Arm IK", slider=True)
        left_col.prop(obj, "left_arm_stretch", text="Stretch", slider=True)
        left_col.prop(obj, "left_arm_wrist_lock", text="Wrist Lock", slider=True)
        if obj.advanced_mode:
            op_col = left_col.column(align=True)
            op_col.scale_y = 1.2
            op_col.operator('ice_cube.arm_l_ik_to_fk', text="Convert To IK", icon='RESTRICT_INSTANCED_OFF')
            op_col.operator('ice_cube.arm_l_fk_to_ik', text="Convert To FK", icon='RESTRICT_INSTANCED_ON')

        # Right Arm
        right_col.prop(obj, "right_arm_ik", text="Right Arm IK", slider=True)
        right_col.prop(obj, "right_arm_stretch", text="Stretch", slider=True)
        right_col.prop(obj, "right_arm_wrist_lock", text="Wrist Lock", slider=True)
        if obj.advanced_mode:
            op_col = right_col.column(align=True)
            op_col.scale_y = 1.2
            op_col.operator('ice_cube.arm_r_ik_to_fk', text="Convert To IK", icon='RESTRICT_INSTANCED_OFF')
            op_col.operator('ice_cube.arm_r_fk_to_ik', text="Convert To FK", icon='RESTRICT_INSTANCED_ON')


# -------------------------------------------------------------------
# SUB-PAINEL: LEG SETTINGS
# -------------------------------------------------------------------
class ICECUBERIG_PT_LegSettings(bpy.types.Panel):
    bl_label = "Leg Settings"
    bl_idname = "ICECUBERIG_PT_LegSettings"
    bl_space_type = "VIEW_3D"
    bl_region_type = 'UI'
    bl_parent_id = "ICECUBERIG_PT_Workflow"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(self, context):
        active_object = bpy.context.active_object
        try:
            return (active_object.data.get("rig_id") == RIG_ID)
        except (AttributeError, KeyError, TypeError):
            return False

    def draw_header(self, context):
        self.layout.label(text="", icon='BONE_DATA')

    def draw(self, context):
        layout = self.layout
        obj = context.object

        row = layout.row(align=True)
        split = row.split(factor=0.5)
        
        left_col = split.column(align=True)
        right_col = split.column(align=True)

        # Left Leg
        left_col.prop(obj, "left_leg_ik", text="Left Leg IK", slider=True)
        left_col.prop(obj, "left_leg_stretch", text="Stretch", slider=True)
        left_col.prop(obj, "left_leg_ankle_lock", text="Ankle Lock", slider=True)
        if obj.advanced_mode:
            op_col = left_col.column(align=True)
            op_col.scale_y = 1.2
            op_col.operator('ice_cube.leg_l_ik_to_fk', text="Convert To IK", icon='RESTRICT_INSTANCED_OFF')
            op_col.operator('ice_cube.leg_l_fk_to_ik', text="Convert To FK", icon='RESTRICT_INSTANCED_ON')
        
        # Right Leg
        right_col.prop(obj, "right_leg_ik", text="Right Leg IK", slider=True)
        right_col.prop(obj, "right_leg_stretch", text="Stretch", slider=True)
        right_col.prop(obj, "right_leg_ankle_lock", text="Ankle Lock", slider=True)
        if obj.advanced_mode:
            op_col = right_col.column(align=True)
            op_col.scale_y = 1.2
            op_col.operator('ice_cube.leg_r_ik_to_fk', text="Convert To IK", icon='RESTRICT_INSTANCED_OFF')
            op_col.operator('ice_cube.leg_r_fk_to_ik', text="Convert To FK", icon='RESTRICT_INSTANCED_ON')


# -------------------------------------------------------------------
# SUB-PAINEL: MISC SETTINGS
# -------------------------------------------------------------------
class ICECUBERIG_PT_MiscSettings(bpy.types.Panel):
    bl_label = "Misc Settings"
    bl_idname = "ICECUBERIG_PT_MiscSettings"
    bl_space_type = "VIEW_3D"
    bl_region_type = 'UI'
    bl_parent_id = "ICECUBERIG_PT_Workflow"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(self, context):
        active_object = bpy.context.active_object
        try:
            return (active_object.data.get("rig_id") == RIG_ID)
        except (AttributeError, KeyError, TypeError):
            return False

    def draw_header(self, context):
        self.layout.label(text="", icon='MONKEY')

    def draw(self, context):
        layout = self.layout
        obj = context.object
        
        face_rig_row = layout.row(align=True)
        face_rig_row.prop(obj, "face_rig", text="Face Rig", toggle=True)
        
        if obj.face_rig:
            col = layout.column(align=True)
            col.prop(obj, "global_head_strength", text="Global Head Strength", slider=True)
            col.prop(obj, "fluid_face_strength", text="Fluid Face Strength", slider=True)
            col.prop(obj, "blink_position", text="Blink Position", slider=True)
        
        if obj.advanced_mode:
            if obj.face_rig:
                r = layout.row(align=True)
                r.prop(obj, "eyetracker", text="Eyetracker")
                r.prop(obj, "global_head_rotation", text="Global Head Rot")
                
                r = layout.row(align=True)
                r.prop(obj, "head_squish", text="Head Squish")
                r.prop(obj, "body_squish", text="Body Squish")
                
                r = layout.row(align=True)
                r.prop(obj, "cartoon_mouth", text="Cartoon Mouth")
                r.prop(obj, "o_mouth_shape", text="O Mouth Shape")
                
                r = layout.row(align=True)
                r.prop(obj, "shoulder_deform", text="Shoulder Deform")
                r.prop(obj, "texture_deform", text="Texture Deform")
                
                r = layout.row(align=True)
                r.prop(obj, "lock_limb_rotation", text="Lock Limb Rotation", toggle=True, icon='DECORATE_LOCKED')
                r.prop(obj, "teeth_bool", text="Teeth Boolean", icon='MOD_BOOLEAN')
                
                col = layout.column(align=True)
                col.scale_y = 1.2
                col.operator("ice_cube.set_custom_default_pose", text="Update Rest Pose", icon='ARMATURE_DATA')
                col.operator("ice_cube.reset_custom_default_pose", text="Reset Rest Pose", icon='LOOP_BACK')
                
                r = layout.row(align=True)
                r.prop(obj, "minecraft_accurate_scaling", text="Minecraft Scale", icon='CON_TRANSFORM')
                r.operator("ice_cube.bake_rig", text="Bake Rig", icon='ERROR')
                
                layout.operator("ice_cube.reset_all", text="Reset All", icon='ERROR')
            else:
                r = layout.row(align=True)
                r.prop(obj, "global_head_rotation", text="Global Head Rot")
                r.prop(obj, "shoulder_deform", text="Shoulder Deform")
                
                r = layout.row(align=True)
                r.prop(obj, "head_squish", text="Head Squish")
                r.prop(obj, "body_squish", text="Body Squish")
                
                layout.prop(obj, "lock_limb_rotation", text="Lock Limb Rotation", toggle=True, icon='DECORATE_LOCKED')
                
                col = layout.column(align=True)
                col.scale_y = 1.2
                col.operator("ice_cube.set_custom_default_pose", text="Update Rest Pose", icon='ARMATURE_DATA')
                col.operator("ice_cube.reset_custom_default_pose", text="Reset Rest Pose", icon='LOOP_BACK')
                
                r = layout.row(align=True)
                r.operator("ice_cube.bake_rig", text="Bake Rig", icon='ERROR')
                r.operator("ice_cube.reset_all", text="Reset All", icon='ERROR')
        else:
            r = layout.row(align=True)
            r.prop(obj, "global_head_rotation", text="Global Head Rot", toggle=True, icon='DRIVER_ROTATIONAL_DIFFERENCE')
            if obj.face_rig:
                r.prop(obj, "cartoon_mouth", text="Cartoon Mouth", toggle=True, icon='IPO_LINEAR')
            
            if obj.face_rig:
                layout.prop(obj, "texture_deform", text="Texture Deform", toggle=True, icon='UV')
            
            layout.prop(obj, "lock_limb_rotation", text="Lock Limb Rotation", toggle=True, icon='DECORATE_LOCKED')
            
            col = layout.column(align=True)
            col.scale_y = 1.2
            col.operator("ice_cube.set_custom_default_pose", text="Update Rest Pose", icon='ARMATURE_DATA')
            col.operator("ice_cube.reset_custom_default_pose", text="Reset Rest Pose", icon='LOOP_BACK')
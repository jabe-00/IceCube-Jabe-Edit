import bpy
from mathutils import Matrix

COPIED_MATRIX = None

BRING_PAIRS = {
    "Left Arm IK World": "Left Arm IK",
    "Right Arm IK World": "Right Arm IK",
    "Left Leg IK World": "Left Leg IK",
    "Right Leg IK World": "Right Leg IK"
}

# ==============================================================================
# BRING WORLD BONE OPERATOR
# ==============================================================================

class ICECUBE_OT_BringWorldBone(bpy.types.Operator):
    bl_idname = "ice_cube.bring_world_bone"
    bl_label = "Bring World Bone"
    bl_description = "Snaps the selected World bone to the corresponding IK bone position"

    def execute(self, context):
        obj = context.active_object
        bone = context.active_pose_bone
        
        if not bone:
            self.report({'WARNING'}, "Select a World Bone")
            return {'CANCELLED'}
            
        target_name = bone.name
        source_name = BRING_PAIRS.get(target_name)
        
        # Reverse lookup logic (Snap World to IK if IK is selected)
        if not source_name:
            found_world = None
            for world, ik in BRING_PAIRS.items():
                if ik == target_name:
                    found_world = world
                    break
            
            if found_world:
                target_name = found_world
                source_name = bone.name
                bone = obj.pose.bones.get(target_name)
            else:
                self.report({'WARNING'}, f"Bone '{target_name}' is not configured as a World/IK pair.")
                return {'CANCELLED'}
            
        source_bone = obj.pose.bones.get(source_name)
        if not source_bone:
            self.report({'ERROR'}, f"Parent bone '{source_name}' not found in rig.")
            return {'CANCELLED'}
            
        # Snap Logic
        global_matrix = obj.matrix_world @ source_bone.matrix
        bone.matrix = obj.matrix_world.inverted() @ global_matrix
        
        context.view_layer.update()
        current_frame = context.scene.frame_current
        
        bone.keyframe_insert(data_path="location", frame=current_frame)
        bone.keyframe_insert(data_path="rotation_euler", frame=current_frame)
        bone.keyframe_insert(data_path="rotation_quaternion", frame=current_frame)
        bone.keyframe_insert(data_path="scale", frame=current_frame)
        
        self.report({'INFO'}, f"Snapped {target_name} to {source_name}")
        return {'FINISHED'}

# ==============================================================================
# COPY / PASTE OPERATORS
# ==============================================================================

class ICECUBE_OT_CopyTransform(bpy.types.Operator):
    bl_idname = "ice_cube.copy_transform"
    bl_label = "Copy Transform"
    bl_description = "Copies the Global Transform (World Space)"

    def execute(self, context):
        global COPIED_MATRIX
        
        if context.mode == 'POSE':
            bone = context.active_pose_bone
            if bone:
                obj = context.active_object
                COPIED_MATRIX = obj.matrix_world @ bone.matrix
                self.report({'INFO'}, "Transform Copied (Bone)")
            else:
                self.report({'WARNING'}, "No bone selected")
                return {'CANCELLED'}
        else:
            obj = context.active_object
            if obj:
                COPIED_MATRIX = obj.matrix_world.copy()
                self.report({'INFO'}, "Transform Copied (Object)")
            else:
                self.report({'WARNING'}, "No object selected")
                return {'CANCELLED'}
                
        return {'FINISHED'}

class ICECUBE_OT_PasteTransform(bpy.types.Operator):
    bl_idname = "ice_cube.paste_transform"
    bl_label = "Paste Transform"
    bl_description = "Pastes the Global Transform and inserts Keyframes"

    def execute(self, context):
        global COPIED_MATRIX
        
        if COPIED_MATRIX is None:
            self.report({'WARNING'}, "Nothing copied yet!")
            return {'CANCELLED'}
            
        current_frame = context.scene.frame_current
        
        if context.mode == 'POSE':
            bones = context.selected_pose_bones
            obj = context.active_object
            
            if not bones:
                self.report({'WARNING'}, "Select a bone to paste")
                return {'CANCELLED'}
                
            for bone in bones:
                bone.matrix = obj.matrix_world.inverted() @ COPIED_MATRIX
                context.view_layer.update()
                
                bone.keyframe_insert(data_path="location", frame=current_frame)
                bone.keyframe_insert(data_path="rotation_quaternion", frame=current_frame)
                bone.keyframe_insert(data_path="rotation_euler", frame=current_frame)
                bone.keyframe_insert(data_path="scale", frame=current_frame)
                
            self.report({'INFO'}, "Transform Pasted on Bone(s)")
            
        else:
            objs = context.selected_objects
            if not objs:
                self.report({'WARNING'}, "Select an object")
                return {'CANCELLED'}
                
            for o in objs:
                o.matrix_world = COPIED_MATRIX
                context.view_layer.update()
                
                o.keyframe_insert(data_path="location", frame=current_frame)
                o.keyframe_insert(data_path="rotation_euler", frame=current_frame)
                o.keyframe_insert(data_path="scale", frame=current_frame)
                
            self.report({'INFO'}, "Transform Pasted on Object(s)")

        return {'FINISHED'}
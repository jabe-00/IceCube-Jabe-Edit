import bpy

from . import bone_collections
from . import workflow
from . import style
from . import add_menu
from . import ice_cube
from . import parenting

classes = (
    ice_cube.ICECUBERIG_PT_IceCubeMain,
    workflow.ICECUBERIG_PT_Workflow,
    bone_collections.ICECUBERIG_PT_BoneCollections,
    style.ICECUBERIG_PT_Style,
    style.ICECUBERIG_PT_StyleTaper,
    style.ICECUBERIG_PT_StyleBulge,
    style.ICECUBERIG_PT_StyleCosmetics,
    style.ICECUBERIG_PT_StyleEmotions,
    style.ICECUBERIG_PT_StyleMouth,
    style.ICECUBERIG_PT_StyleSkin,
    style.ICECUBERIG_PT_StyleMaterial,
    parenting.ICECUBERIG_PT_Parenting,
    add_menu.ICECUBE_RIG,
    add_menu.ICECUBE_Label,
    bone_collections.ICECUBERIG_PT_Bones,
    bone_collections.ICECUBERIG_PARENT_TREE,
    workflow.ICECUBERIG_PT_ArmSettings,
    workflow.ICECUBERIG_PT_LegSettings,
    workflow.ICECUBERIG_PT_MiscSettings

)

cls_register, cls_unregister = bpy.utils.register_classes_factory(classes)

def register():
    cls_register()

    bpy.types.VIEW3D_MT_add.append(add_menu.AddMenuFunction)

def unregister():
    cls_unregister()

    bpy.types.VIEW3D_MT_add.remove(add_menu.AddMenuFunction)

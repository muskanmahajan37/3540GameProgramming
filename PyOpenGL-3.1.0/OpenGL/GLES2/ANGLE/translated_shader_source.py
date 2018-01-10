'''OpenGL extension ANGLE.translated_shader_source

This module customises the behaviour of the 
OpenGL.raw.GLES2.ANGLE.translated_shader_source to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ANGLE/translated_shader_source.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GLES2 import _types, _glgets
from OpenGL.raw.GLES2.ANGLE.translated_shader_source import *
from OpenGL.raw.GLES2.ANGLE.translated_shader_source import _EXTENSION_NAME

def glInitTranslatedShaderSourceANGLE():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

glGetTranslatedShaderSourceANGLE=wrapper.wrapper(glGetTranslatedShaderSourceANGLE).setInputArraySize(
    'length', 1
)
### END AUTOGENERATED SECTION
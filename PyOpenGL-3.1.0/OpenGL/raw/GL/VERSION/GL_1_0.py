'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_VERSION_GL_1_0'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GL,'GL_VERSION_GL_1_0',error_checker=_errors._error_checker)

@_f
@_p.types(None,_cs.GLenum,_cs.GLfloat)
def glAccum(op,value):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLfloat)
def glAlphaFunc(func,ref):pass
@_f
@_p.types(None,_cs.GLenum)
def glBegin(mode):pass
@_f
@_p.types(None,_cs.GLsizei,_cs.GLsizei,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat,arrays.GLubyteArray)
def glBitmap(width,height,xorig,yorig,xmove,ymove,bitmap):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum)
def glBlendFunc(sfactor,dfactor):pass
@_f
@_p.types(None,_cs.GLuint)
def glCallList(list):pass
@_f
@_p.types(None,_cs.GLsizei,_cs.GLenum,ctypes.c_void_p)
def glCallLists(n,type,lists):pass
@_f
@_p.types(None,_cs.GLbitfield)
def glClear(mask):pass
@_f
@_p.types(None,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat)
def glClearAccum(red,green,blue,alpha):pass
@_f
@_p.types(None,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat)
def glClearColor(red,green,blue,alpha):pass
@_f
@_p.types(None,_cs.GLdouble)
def glClearDepth(depth):pass
@_f
@_p.types(None,_cs.GLfloat)
def glClearIndex(c):pass
@_f
@_p.types(None,_cs.GLint)
def glClearStencil(s):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLdoubleArray)
def glClipPlane(plane,equation):pass
@_f
@_p.types(None,_cs.GLbyte,_cs.GLbyte,_cs.GLbyte)
def glColor3b(red,green,blue):pass
@_f
@_p.types(None,arrays.GLbyteArray)
def glColor3bv(v):pass
@_f
@_p.types(None,_cs.GLdouble,_cs.GLdouble,_cs.GLdouble)
def glColor3d(red,green,blue):pass
@_f
@_p.types(None,arrays.GLdoubleArray)
def glColor3dv(v):pass
@_f
@_p.types(None,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat)
def glColor3f(red,green,blue):pass
@_f
@_p.types(None,arrays.GLfloatArray)
def glColor3fv(v):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLint,_cs.GLint)
def glColor3i(red,green,blue):pass
@_f
@_p.types(None,arrays.GLintArray)
def glColor3iv(v):pass
@_f
@_p.types(None,_cs.GLshort,_cs.GLshort,_cs.GLshort)
def glColor3s(red,green,blue):pass
@_f
@_p.types(None,arrays.GLshortArray)
def glColor3sv(v):pass
@_f
@_p.types(None,_cs.GLubyte,_cs.GLubyte,_cs.GLubyte)
def glColor3ub(red,green,blue):pass
@_f
@_p.types(None,arrays.GLubyteArray)
def glColor3ubv(v):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint,_cs.GLuint)
def glColor3ui(red,green,blue):pass
@_f
@_p.types(None,arrays.GLuintArray)
def glColor3uiv(v):pass
@_f
@_p.types(None,_cs.GLushort,_cs.GLushort,_cs.GLushort)
def glColor3us(red,green,blue):pass
@_f
@_p.types(None,arrays.GLushortArray)
def glColor3usv(v):pass
@_f
@_p.types(None,_cs.GLbyte,_cs.GLbyte,_cs.GLbyte,_cs.GLbyte)
def glColor4b(red,green,blue,alpha):pass
@_f
@_p.types(None,arrays.GLbyteArray)
def glColor4bv(v):pass
@_f
@_p.types(None,_cs.GLdouble,_cs.GLdouble,_cs.GLdouble,_cs.GLdouble)
def glColor4d(red,green,blue,alpha):pass
@_f
@_p.types(None,arrays.GLdoubleArray)
def glColor4dv(v):pass
@_f
@_p.types(None,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat)
def glColor4f(red,green,blue,alpha):pass
@_f
@_p.types(None,arrays.GLfloatArray)
def glColor4fv(v):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint)
def glColor4i(red,green,blue,alpha):pass
@_f
@_p.types(None,arrays.GLintArray)
def glColor4iv(v):pass
@_f
@_p.types(None,_cs.GLshort,_cs.GLshort,_cs.GLshort,_cs.GLshort)
def glColor4s(red,green,blue,alpha):pass
@_f
@_p.types(None,arrays.GLshortArray)
def glColor4sv(v):pass
@_f
@_p.types(None,_cs.GLubyte,_cs.GLubyte,_cs.GLubyte,_cs.GLubyte)
def glColor4ub(red,green,blue,alpha):pass
@_f
@_p.types(None,arrays.GLubyteArray)
def glColor4ubv(v):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint,_cs.GLuint,_cs.GLuint)
def glColor4ui(red,green,blue,alpha):pass
@_f
@_p.types(None,arrays.GLuintArray)
def glColor4uiv(v):pass
@_f
@_p.types(None,_cs.GLushort,_cs.GLushort,_cs.GLushort,_cs.GLushort)
def glColor4us(red,green,blue,alpha):pass
@_f
@_p.types(None,arrays.GLushortArray)
def glColor4usv(v):pass
@_f
@_p.types(None,_cs.GLboolean,_cs.GLboolean,_cs.GLboolean,_cs.GLboolean)
def glColorMask(red,green,blue,alpha):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum)
def glColorMaterial(face,mode):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLint,_cs.GLsizei,_cs.GLsizei,_cs.GLenum)
def glCopyPixels(x,y,width,height,type):pass
@_f
@_p.types(None,_cs.GLenum)
def glCullFace(mode):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLsizei)
def glDeleteLists(list,range):pass
@_f
@_p.types(None,_cs.GLenum)
def glDepthFunc(func):pass
@_f
@_p.types(None,_cs.GLboolean)
def glDepthMask(flag):pass
@_f
@_p.types(None,_cs.GLdouble,_cs.GLdouble)
def glDepthRange(near,far):pass
@_f
@_p.types(None,_cs.GLenum)
def glDisable(cap):pass
@_f
@_p.types(None,_cs.GLenum)
def glDrawBuffer(mode):pass
@_f
@_p.types(None,_cs.GLsizei,_cs.GLsizei,_cs.GLenum,_cs.GLenum,ctypes.c_void_p)
def glDrawPixels(width,height,format,type,pixels):pass
@_f
@_p.types(None,_cs.GLboolean)
def glEdgeFlag(flag):pass
@_f
@_p.types(None,arrays.GLbooleanArray)
def glEdgeFlagv(flag):pass
@_f
@_p.types(None,_cs.GLenum)
def glEnable(cap):pass
@_f
@_p.types(None,)
def glEnd():pass
@_f
@_p.types(None,)
def glEndList():pass
@_f
@_p.types(None,_cs.GLdouble)
def glEvalCoord1d(u):pass
@_f
@_p.types(None,arrays.GLdoubleArray)
def glEvalCoord1dv(u):pass
@_f
@_p.types(None,_cs.GLfloat)
def glEvalCoord1f(u):pass
@_f
@_p.types(None,arrays.GLfloatArray)
def glEvalCoord1fv(u):pass
@_f
@_p.types(None,_cs.GLdouble,_cs.GLdouble)
def glEvalCoord2d(u,v):pass
@_f
@_p.types(None,arrays.GLdoubleArray)
def glEvalCoord2dv(u):pass
@_f
@_p.types(None,_cs.GLfloat,_cs.GLfloat)
def glEvalCoord2f(u,v):pass
@_f
@_p.types(None,arrays.GLfloatArray)
def glEvalCoord2fv(u):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,_cs.GLint)
def glEvalMesh1(mode,i1,i2):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint)
def glEvalMesh2(mode,i1,i2,j1,j2):pass
@_f
@_p.types(None,_cs.GLint)
def glEvalPoint1(i):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLint)
def glEvalPoint2(i,j):pass
@_f
@_p.types(None,_cs.GLsizei,_cs.GLenum,arrays.GLfloatArray)
def glFeedbackBuffer(size,type,buffer):pass
@_f
@_p.types(None,)
def glFinish():pass
@_f
@_p.types(None,)
def glFlush():pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLfloat)
def glFogf(pname,param):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLfloatArray)
def glFogfv(pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLint)
def glFogi(pname,param):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLintArray)
def glFogiv(pname,params):pass
@_f
@_p.types(None,_cs.GLenum)
def glFrontFace(mode):pass
@_f
@_p.types(None,_cs.GLdouble,_cs.GLdouble,_cs.GLdouble,_cs.GLdouble,_cs.GLdouble,_cs.GLdouble)
def glFrustum(left,right,bottom,top,zNear,zFar):pass
@_f
@_p.types(_cs.GLuint,_cs.GLsizei)
def glGenLists(range):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLbooleanArray)
def glGetBooleanv(pname,data):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLdoubleArray)
def glGetClipPlane(plane,equation):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLdoubleArray)
def glGetDoublev(pname,data):pass
@_f
@_p.types(_cs.GLenum,)
def glGetError():pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLfloatArray)
def glGetFloatv(pname,data):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLintArray)
def glGetIntegerv(pname,data):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLfloatArray)
def glGetLightfv(light,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glGetLightiv(light,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLdoubleArray)
def glGetMapdv(target,query,v):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLfloatArray)
def glGetMapfv(target,query,v):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glGetMapiv(target,query,v):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLfloatArray)
def glGetMaterialfv(face,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glGetMaterialiv(face,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLfloatArray)
def glGetPixelMapfv(map,values):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLuintArray)
def glGetPixelMapuiv(map,values):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLushortArray)
def glGetPixelMapusv(map,values):pass
@_f
@_p.types(None,arrays.GLubyteArray)
def glGetPolygonStipple(mask):pass
@_f
@_p.types(arrays.GLubyteArray,_cs.GLenum)
def glGetString(name):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLfloatArray)
def glGetTexEnvfv(target,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glGetTexEnviv(target,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLdoubleArray)
def glGetTexGendv(coord,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLfloatArray)
def glGetTexGenfv(coord,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glGetTexGeniv(coord,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,_cs.GLenum,_cs.GLenum,ctypes.c_void_p)
def glGetTexImage(target,level,format,type,pixels):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,_cs.GLenum,arrays.GLfloatArray)
def glGetTexLevelParameterfv(target,level,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,_cs.GLenum,arrays.GLintArray)
def glGetTexLevelParameteriv(target,level,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLfloatArray)
def glGetTexParameterfv(target,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glGetTexParameteriv(target,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum)
def glHint(target,mode):pass
@_f
@_p.types(None,_cs.GLuint)
def glIndexMask(mask):pass
@_f
@_p.types(None,_cs.GLdouble)
def glIndexd(c):pass
@_f
@_p.types(None,arrays.GLdoubleArray)
def glIndexdv(c):pass
@_f
@_p.types(None,_cs.GLfloat)
def glIndexf(c):pass
@_f
@_p.types(None,arrays.GLfloatArray)
def glIndexfv(c):pass
@_f
@_p.types(None,_cs.GLint)
def glIndexi(c):pass
@_f
@_p.types(None,arrays.GLintArray)
def glIndexiv(c):pass
@_f
@_p.types(None,_cs.GLshort)
def glIndexs(c):pass
@_f
@_p.types(None,arrays.GLshortArray)
def glIndexsv(c):pass
@_f
@_p.types(None,)
def glInitNames():pass
@_f
@_p.types(_cs.GLboolean,_cs.GLenum)
def glIsEnabled(cap):pass
@_f
@_p.types(_cs.GLboolean,_cs.GLuint)
def glIsList(list):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLfloat)
def glLightModelf(pname,param):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLfloatArray)
def glLightModelfv(pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLint)
def glLightModeli(pname,param):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLintArray)
def glLightModeliv(pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLfloat)
def glLightf(light,pname,param):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLfloatArray)
def glLightfv(light,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLint)
def glLighti(light,pname,param):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glLightiv(light,pname,params):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLushort)
def glLineStipple(factor,pattern):pass
@_f
@_p.types(None,_cs.GLfloat)
def glLineWidth(width):pass
@_f
@_p.types(None,_cs.GLuint)
def glListBase(base):pass
@_f
@_p.types(None,)
def glLoadIdentity():pass
@_f
@_p.types(None,arrays.GLdoubleArray)
def glLoadMatrixd(m):pass
@_f
@_p.types(None,arrays.GLfloatArray)
def glLoadMatrixf(m):pass
@_f
@_p.types(None,_cs.GLuint)
def glLoadName(name):pass
@_f
@_p.types(None,_cs.GLenum)
def glLogicOp(opcode):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLdouble,_cs.GLdouble,_cs.GLint,_cs.GLint,arrays.GLdoubleArray)
def glMap1d(target,u1,u2,stride,order,points):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLfloat,_cs.GLfloat,_cs.GLint,_cs.GLint,arrays.GLfloatArray)
def glMap1f(target,u1,u2,stride,order,points):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLdouble,_cs.GLdouble,_cs.GLint,_cs.GLint,_cs.GLdouble,_cs.GLdouble,_cs.GLint,_cs.GLint,arrays.GLdoubleArray)
def glMap2d(target,u1,u2,ustride,uorder,v1,v2,vstride,vorder,points):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLfloat,_cs.GLfloat,_cs.GLint,_cs.GLint,_cs.GLfloat,_cs.GLfloat,_cs.GLint,_cs.GLint,arrays.GLfloatArray)
def glMap2f(target,u1,u2,ustride,uorder,v1,v2,vstride,vorder,points):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLdouble,_cs.GLdouble)
def glMapGrid1d(un,u1,u2):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLfloat,_cs.GLfloat)
def glMapGrid1f(un,u1,u2):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLdouble,_cs.GLdouble,_cs.GLint,_cs.GLdouble,_cs.GLdouble)
def glMapGrid2d(un,u1,u2,vn,v1,v2):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLfloat,_cs.GLfloat,_cs.GLint,_cs.GLfloat,_cs.GLfloat)
def glMapGrid2f(un,u1,u2,vn,v1,v2):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLfloat)
def glMaterialf(face,pname,param):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLfloatArray)
def glMaterialfv(face,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLint)
def glMateriali(face,pname,param):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glMaterialiv(face,pname,params):pass
@_f
@_p.types(None,_cs.GLenum)
def glMatrixMode(mode):pass
@_f
@_p.types(None,arrays.GLdoubleArray)
def glMultMatrixd(m):pass
@_f
@_p.types(None,arrays.GLfloatArray)
def glMultMatrixf(m):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum)
def glNewList(list,mode):pass
@_f
@_p.types(None,_cs.GLbyte,_cs.GLbyte,_cs.GLbyte)
def glNormal3b(nx,ny,nz):pass
@_f
@_p.types(None,arrays.GLbyteArray)
def glNormal3bv(v):pass
@_f
@_p.types(None,_cs.GLdouble,_cs.GLdouble,_cs.GLdouble)
def glNormal3d(nx,ny,nz):pass
@_f
@_p.types(None,arrays.GLdoubleArray)
def glNormal3dv(v):pass
@_f
@_p.types(None,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat)
def glNormal3f(nx,ny,nz):pass
@_f
@_p.types(None,arrays.GLfloatArray)
def glNormal3fv(v):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLint,_cs.GLint)
def glNormal3i(nx,ny,nz):pass
@_f
@_p.types(None,arrays.GLintArray)
def glNormal3iv(v):pass
@_f
@_p.types(None,_cs.GLshort,_cs.GLshort,_cs.GLshort)
def glNormal3s(nx,ny,nz):pass
@_f
@_p.types(None,arrays.GLshortArray)
def glNormal3sv(v):pass
@_f
@_p.types(None,_cs.GLdouble,_cs.GLdouble,_cs.GLdouble,_cs.GLdouble,_cs.GLdouble,_cs.GLdouble)
def glOrtho(left,right,bottom,top,zNear,zFar):pass
@_f
@_p.types(None,_cs.GLfloat)
def glPassThrough(token):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLsizei,arrays.GLfloatArray)
def glPixelMapfv(map,mapsize,values):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLsizei,arrays.GLuintArray)
def glPixelMapuiv(map,mapsize,values):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLsizei,arrays.GLushortArray)
def glPixelMapusv(map,mapsize,values):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLfloat)
def glPixelStoref(pname,param):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLint)
def glPixelStorei(pname,param):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLfloat)
def glPixelTransferf(pname,param):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLint)
def glPixelTransferi(pname,param):pass
@_f
@_p.types(None,_cs.GLfloat,_cs.GLfloat)
def glPixelZoom(xfactor,yfactor):pass
@_f
@_p.types(None,_cs.GLfloat)
def glPointSize(size):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum)
def glPolygonMode(face,mode):pass
@_f
@_p.types(None,arrays.GLubyteArray)
def glPolygonStipple(mask):pass
@_f
@_p.types(None,)
def glPopAttrib():pass
@_f
@_p.types(None,)
def glPopMatrix():pass
@_f
@_p.types(None,)
def glPopName():pass
@_f
@_p.types(None,_cs.GLbitfield)
def glPushAttrib(mask):pass
@_f
@_p.types(None,)
def glPushMatrix():pass
@_f
@_p.types(None,_cs.GLuint)
def glPushName(name):pass
@_f
@_p.types(None,_cs.GLdouble,_cs.GLdouble)
def glRasterPos2d(x,y):pass
@_f
@_p.types(None,arrays.GLdoubleArray)
def glRasterPos2dv(v):pass
@_f
@_p.types(None,_cs.GLfloat,_cs.GLfloat)
def glRasterPos2f(x,y):pass
@_f
@_p.types(None,arrays.GLfloatArray)
def glRasterPos2fv(v):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLint)
def glRasterPos2i(x,y):pass
@_f
@_p.types(None,arrays.GLintArray)
def glRasterPos2iv(v):pass
@_f
@_p.types(None,_cs.GLshort,_cs.GLshort)
def glRasterPos2s(x,y):pass
@_f
@_p.types(None,arrays.GLshortArray)
def glRasterPos2sv(v):pass
@_f
@_p.types(None,_cs.GLdouble,_cs.GLdouble,_cs.GLdouble)
def glRasterPos3d(x,y,z):pass
@_f
@_p.types(None,arrays.GLdoubleArray)
def glRasterPos3dv(v):pass
@_f
@_p.types(None,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat)
def glRasterPos3f(x,y,z):pass
@_f
@_p.types(None,arrays.GLfloatArray)
def glRasterPos3fv(v):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLint,_cs.GLint)
def glRasterPos3i(x,y,z):pass
@_f
@_p.types(None,arrays.GLintArray)
def glRasterPos3iv(v):pass
@_f
@_p.types(None,_cs.GLshort,_cs.GLshort,_cs.GLshort)
def glRasterPos3s(x,y,z):pass
@_f
@_p.types(None,arrays.GLshortArray)
def glRasterPos3sv(v):pass
@_f
@_p.types(None,_cs.GLdouble,_cs.GLdouble,_cs.GLdouble,_cs.GLdouble)
def glRasterPos4d(x,y,z,w):pass
@_f
@_p.types(None,arrays.GLdoubleArray)
def glRasterPos4dv(v):pass
@_f
@_p.types(None,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat)
def glRasterPos4f(x,y,z,w):pass
@_f
@_p.types(None,arrays.GLfloatArray)
def glRasterPos4fv(v):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint)
def glRasterPos4i(x,y,z,w):pass
@_f
@_p.types(None,arrays.GLintArray)
def glRasterPos4iv(v):pass
@_f
@_p.types(None,_cs.GLshort,_cs.GLshort,_cs.GLshort,_cs.GLshort)
def glRasterPos4s(x,y,z,w):pass
@_f
@_p.types(None,arrays.GLshortArray)
def glRasterPos4sv(v):pass
@_f
@_p.types(None,_cs.GLenum)
def glReadBuffer(mode):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLint,_cs.GLsizei,_cs.GLsizei,_cs.GLenum,_cs.GLenum,ctypes.c_void_p)
def glReadPixels(x,y,width,height,format,type,pixels):pass
@_f
@_p.types(None,_cs.GLdouble,_cs.GLdouble,_cs.GLdouble,_cs.GLdouble)
def glRectd(x1,y1,x2,y2):pass
@_f
@_p.types(None,arrays.GLdoubleArray,arrays.GLdoubleArray)
def glRectdv(v1,v2):pass
@_f
@_p.types(None,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat)
def glRectf(x1,y1,x2,y2):pass
@_f
@_p.types(None,arrays.GLfloatArray,arrays.GLfloatArray)
def glRectfv(v1,v2):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint)
def glRecti(x1,y1,x2,y2):pass
@_f
@_p.types(None,arrays.GLintArray,arrays.GLintArray)
def glRectiv(v1,v2):pass
@_f
@_p.types(None,_cs.GLshort,_cs.GLshort,_cs.GLshort,_cs.GLshort)
def glRects(x1,y1,x2,y2):pass
@_f
@_p.types(None,arrays.GLshortArray,arrays.GLshortArray)
def glRectsv(v1,v2):pass
@_f
@_p.types(_cs.GLint,_cs.GLenum)
def glRenderMode(mode):pass
@_f
@_p.types(None,_cs.GLdouble,_cs.GLdouble,_cs.GLdouble,_cs.GLdouble)
def glRotated(angle,x,y,z):pass
@_f
@_p.types(None,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat)
def glRotatef(angle,x,y,z):pass
@_f
@_p.types(None,_cs.GLdouble,_cs.GLdouble,_cs.GLdouble)
def glScaled(x,y,z):pass
@_f
@_p.types(None,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat)
def glScalef(x,y,z):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLint,_cs.GLsizei,_cs.GLsizei)
def glScissor(x,y,width,height):pass
@_f
@_p.types(None,_cs.GLsizei,arrays.GLuintArray)
def glSelectBuffer(size,buffer):pass
@_f
@_p.types(None,_cs.GLenum)
def glShadeModel(mode):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,_cs.GLuint)
def glStencilFunc(func,ref,mask):pass
@_f
@_p.types(None,_cs.GLuint)
def glStencilMask(mask):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLenum)
def glStencilOp(fail,zfail,zpass):pass
@_f
@_p.types(None,_cs.GLdouble)
def glTexCoord1d(s):pass
@_f
@_p.types(None,arrays.GLdoubleArray)
def glTexCoord1dv(v):pass
@_f
@_p.types(None,_cs.GLfloat)
def glTexCoord1f(s):pass
@_f
@_p.types(None,arrays.GLfloatArray)
def glTexCoord1fv(v):pass
@_f
@_p.types(None,_cs.GLint)
def glTexCoord1i(s):pass
@_f
@_p.types(None,arrays.GLintArray)
def glTexCoord1iv(v):pass
@_f
@_p.types(None,_cs.GLshort)
def glTexCoord1s(s):pass
@_f
@_p.types(None,arrays.GLshortArray)
def glTexCoord1sv(v):pass
@_f
@_p.types(None,_cs.GLdouble,_cs.GLdouble)
def glTexCoord2d(s,t):pass
@_f
@_p.types(None,arrays.GLdoubleArray)
def glTexCoord2dv(v):pass
@_f
@_p.types(None,_cs.GLfloat,_cs.GLfloat)
def glTexCoord2f(s,t):pass
@_f
@_p.types(None,arrays.GLfloatArray)
def glTexCoord2fv(v):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLint)
def glTexCoord2i(s,t):pass
@_f
@_p.types(None,arrays.GLintArray)
def glTexCoord2iv(v):pass
@_f
@_p.types(None,_cs.GLshort,_cs.GLshort)
def glTexCoord2s(s,t):pass
@_f
@_p.types(None,arrays.GLshortArray)
def glTexCoord2sv(v):pass
@_f
@_p.types(None,_cs.GLdouble,_cs.GLdouble,_cs.GLdouble)
def glTexCoord3d(s,t,r):pass
@_f
@_p.types(None,arrays.GLdoubleArray)
def glTexCoord3dv(v):pass
@_f
@_p.types(None,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat)
def glTexCoord3f(s,t,r):pass
@_f
@_p.types(None,arrays.GLfloatArray)
def glTexCoord3fv(v):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLint,_cs.GLint)
def glTexCoord3i(s,t,r):pass
@_f
@_p.types(None,arrays.GLintArray)
def glTexCoord3iv(v):pass
@_f
@_p.types(None,_cs.GLshort,_cs.GLshort,_cs.GLshort)
def glTexCoord3s(s,t,r):pass
@_f
@_p.types(None,arrays.GLshortArray)
def glTexCoord3sv(v):pass
@_f
@_p.types(None,_cs.GLdouble,_cs.GLdouble,_cs.GLdouble,_cs.GLdouble)
def glTexCoord4d(s,t,r,q):pass
@_f
@_p.types(None,arrays.GLdoubleArray)
def glTexCoord4dv(v):pass
@_f
@_p.types(None,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat)
def glTexCoord4f(s,t,r,q):pass
@_f
@_p.types(None,arrays.GLfloatArray)
def glTexCoord4fv(v):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint)
def glTexCoord4i(s,t,r,q):pass
@_f
@_p.types(None,arrays.GLintArray)
def glTexCoord4iv(v):pass
@_f
@_p.types(None,_cs.GLshort,_cs.GLshort,_cs.GLshort,_cs.GLshort)
def glTexCoord4s(s,t,r,q):pass
@_f
@_p.types(None,arrays.GLshortArray)
def glTexCoord4sv(v):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLfloat)
def glTexEnvf(target,pname,param):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLfloatArray)
def glTexEnvfv(target,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLint)
def glTexEnvi(target,pname,param):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glTexEnviv(target,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLdouble)
def glTexGend(coord,pname,param):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLdoubleArray)
def glTexGendv(coord,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLfloat)
def glTexGenf(coord,pname,param):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLfloatArray)
def glTexGenfv(coord,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLint)
def glTexGeni(coord,pname,param):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glTexGeniv(coord,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,_cs.GLint,_cs.GLsizei,_cs.GLint,_cs.GLenum,_cs.GLenum,ctypes.c_void_p)
def glTexImage1D(target,level,internalformat,width,border,format,type,pixels):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,_cs.GLint,_cs.GLsizei,_cs.GLsizei,_cs.GLint,_cs.GLenum,_cs.GLenum,ctypes.c_void_p)
def glTexImage2D(target,level,internalformat,width,height,border,format,type,pixels):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLfloat)
def glTexParameterf(target,pname,param):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLfloatArray)
def glTexParameterfv(target,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLint)
def glTexParameteri(target,pname,param):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glTexParameteriv(target,pname,params):pass
@_f
@_p.types(None,_cs.GLdouble,_cs.GLdouble,_cs.GLdouble)
def glTranslated(x,y,z):pass
@_f
@_p.types(None,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat)
def glTranslatef(x,y,z):pass
@_f
@_p.types(None,_cs.GLdouble,_cs.GLdouble)
def glVertex2d(x,y):pass
@_f
@_p.types(None,arrays.GLdoubleArray)
def glVertex2dv(v):pass
@_f
@_p.types(None,_cs.GLfloat,_cs.GLfloat)
def glVertex2f(x,y):pass
@_f
@_p.types(None,arrays.GLfloatArray)
def glVertex2fv(v):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLint)
def glVertex2i(x,y):pass
@_f
@_p.types(None,arrays.GLintArray)
def glVertex2iv(v):pass
@_f
@_p.types(None,_cs.GLshort,_cs.GLshort)
def glVertex2s(x,y):pass
@_f
@_p.types(None,arrays.GLshortArray)
def glVertex2sv(v):pass
@_f
@_p.types(None,_cs.GLdouble,_cs.GLdouble,_cs.GLdouble)
def glVertex3d(x,y,z):pass
@_f
@_p.types(None,arrays.GLdoubleArray)
def glVertex3dv(v):pass
@_f
@_p.types(None,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat)
def glVertex3f(x,y,z):pass
@_f
@_p.types(None,arrays.GLfloatArray)
def glVertex3fv(v):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLint,_cs.GLint)
def glVertex3i(x,y,z):pass
@_f
@_p.types(None,arrays.GLintArray)
def glVertex3iv(v):pass
@_f
@_p.types(None,_cs.GLshort,_cs.GLshort,_cs.GLshort)
def glVertex3s(x,y,z):pass
@_f
@_p.types(None,arrays.GLshortArray)
def glVertex3sv(v):pass
@_f
@_p.types(None,_cs.GLdouble,_cs.GLdouble,_cs.GLdouble,_cs.GLdouble)
def glVertex4d(x,y,z,w):pass
@_f
@_p.types(None,arrays.GLdoubleArray)
def glVertex4dv(v):pass
@_f
@_p.types(None,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat)
def glVertex4f(x,y,z,w):pass
@_f
@_p.types(None,arrays.GLfloatArray)
def glVertex4fv(v):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint)
def glVertex4i(x,y,z,w):pass
@_f
@_p.types(None,arrays.GLintArray)
def glVertex4iv(v):pass
@_f
@_p.types(None,_cs.GLshort,_cs.GLshort,_cs.GLshort,_cs.GLshort)
def glVertex4s(x,y,z,w):pass
@_f
@_p.types(None,arrays.GLshortArray)
def glVertex4sv(v):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLint,_cs.GLsizei,_cs.GLsizei)
def glViewport(x,y,width,height):pass

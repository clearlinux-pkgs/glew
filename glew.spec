#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : glew
Version  : 2.0.0
Release  : 23
URL      : https://github.com/nigels-com/glew/releases/download/glew-2.0.0/glew-2.0.0.tgz
Source0  : https://github.com/nigels-com/glew/releases/download/glew-2.0.0/glew-2.0.0.tgz
Summary  : The OpenGL Extension Wrangler library
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0
Requires: glew-lib
BuildRequires : cmake
BuildRequires : pkgconfig(gl)
BuildRequires : pkgconfig(x11)
Patch1: defaults.patch

%description
# GLEW - The OpenGL Extension Wrangler Library
![](http://glew.sourceforge.net/glew.png)

%package dev
Summary: dev components for the glew package.
Group: Development
Requires: glew-lib
Provides: glew-devel

%description dev
dev components for the glew package.


%package lib
Summary: lib components for the glew package.
Group: Libraries

%description lib
lib components for the glew package.


%prep
%setup -q -n glew-2.0.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1510775871
pushd ./
make V=1  %{?_smp_mflags} DEFAULTFLAGS="$CFLAGS" STRIP=
popd

%install
export SOURCE_DATE_EPOCH=1510775871
rm -rf %{buildroot}
pushd ./
%make_install
popd

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/GL/glew.h
/usr/include/GL/glxew.h
/usr/include/GL/wglew.h
/usr/lib64/libGLEW.so
/usr/lib64/pkgconfig/glew.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libGLEW.so.2.0
/usr/lib64/libGLEW.so.2.0.0

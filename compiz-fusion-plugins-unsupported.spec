%define name compiz-fusion-plugins-unsupported
%define version 0.7.8
%define rel 1
%define git 0

%if %{git}
%define srcname plugins-unsupported-%{git}.tar.lzma
%define distname plugins-unsupported
%define release %mkrel 0.%{git}.%{rel}
%else
%define srcname %{name}-%{version}.tar.bz2
%define distname %{name}-%{version}
%define release %mkrel %{rel}
%endif


Summary: Compiz Fusion Unsupported Plugin Set for compiz
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://releases.compiz-fusion.org/%{version}/%{srcname}
License: GPL
Group: System/X11
URL: http://www.compiz-fusion.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: dbus-devel
BuildRequires: compiz-devel
BuildRequires: gettext-devel
BuildRequires: intltool
BuildRequires: compiz-bcop
BuildRequires: libGConf2-devel
BuildRequires: MesaGLU-devel
Requires: compiz

%description
This is the unsupported plugin set from the Compiz Fusion community.
This is a combination of the Compiz Extras and Beryl communities.

%prep
%setup -q -n %{distname}

%build
%if %{git}
  # This is a CVS snapshot, so we need to generate makefiles.
  sh autogen.sh -V
%endif
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std
find %{buildroot} -name *.la -exec rm -f {} \;
%find_lang %{name}
# 3d is in -extras....
rm -f %{buildroot}%{_libdir}/compiz/lib3d.*
%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%{_libdir}/compiz/lib*.a
%{_libdir}/compiz/lib*.so
%{_datadir}/compiz/*.xml
%{_datadir}/compiz/*.png

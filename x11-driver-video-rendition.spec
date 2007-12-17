Name: x11-driver-video-rendition
Version: 4.1.3
Release: %mkrel 3
Summary: The X.org driver for Rendition (Micron) Cards
Group: System/X11

########################################################################
# git clone git//git.mandriva.com/people/pcpa/xorg/drivers/xf86-video-rendition  xorg/drivers/xf86-video-rendition
# cd xorg/drivers/xf86-video/rendition
# git-archive --format=tar --prefix=xf86-video-rendition-4.1.3/ master | bzip2 -9 > xf86-video-rendition-4.1.3.tar.bz2
########################################################################
Source0: xf86-video-rendition-%{version}.tar.bz2

License: MIT
BuildRoot: %{_tmppath}/%{name}-root

########################################################################
# git-format-patch master..origin/mandriva+gpl
Patch1: 0001-Update-for-new-policy-of-hidden-symbols-and-common-m.patch
########################################################################

BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1

Conflicts: xorg-x11-server < 7.0

%description
The X.org driver for Rendition (Micron) Cards


%prep
%setup -q -n xf86-video-rendition-%{version}

%patch1 -p1

%build
autoreconf -ifs
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/xorg/modules/drivers/rendition_drv.la
%{_libdir}/xorg/modules/drivers/rendition_drv.so
%{_libdir}/xorg/modules/v20002d.uc
%{_libdir}/xorg/modules/v10002d.uc
%{_mandir}/man4/rendition.*


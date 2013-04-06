%define _disable_ld_no_undefined 1

Summary:	X.org driver for Rendition (Micron) Cards
Name:		x11-driver-video-rendition
Version:	4.2.5
Release:	5
Group:		System/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-rendition-%{version}.tar.bz2
Source10:	x11-driver-video-rendition.rpmlintrc
Patch0:		remove_mibstore_h.patch

BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xorg-server)
BuildRequires:	pkgconfig(xproto)
Requires:	x11-server-common %(xserver-sdk-abi-requires videodrv)

%description
x11-driver-video-rendition is the X.org driver for Rendition (Micron) Cards.

%prep
%setup -qn xf86-video-rendition-%{version}
%apply_patches

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%{_libdir}/xorg/modules/drivers/rendition_drv.so
%{_libdir}/xorg/modules/v20002d.uc
%{_libdir}/xorg/modules/v10002d.uc
%{_mandir}/man4/rendition.*


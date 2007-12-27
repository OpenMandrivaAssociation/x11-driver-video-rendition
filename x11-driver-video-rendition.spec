Name: x11-driver-video-rendition
Version: 4.1.3
Release: %mkrel 3
Summary: The X.org driver for Rendition (Micron) Cards
Group: System/X11
URL: http://xorg.freedesktop.org
########################################################################
# git clone git://git.mandriva.com/people/pcpa/xorg/drivers/xf86-video-rendition  xorg/drivers/xf86-video-rendition
# cd xorg/drivers/xf86-video/rendition
# git-archive --format=tar --prefix=xf86-video-rendition-4.1.3/ xf86-video-rendition-4.1.3 | bzip2 -9 > xf86-video-rendition-4.1.3.tar.bz2
########################################################################
Source0: xf86-video-rendition-%{version}.tar.bz2
License: MIT
########################################################################
# git-format-patch xf86-video-rendition-4.1.3..origin/mandriva+gpl
Patch1: 0001-Man-page-updates-replace-references-to-XFree86-c.patch
Patch2: 0002-Supply-NULL-driverFunc-pointer-in-DriverRec.patch
Patch3: 0003-Add-prototype-for-renditionGetRec.patch
Patch4: 0004-Move-renditionTypes-renditionChipsets-and-renditio.patch
Patch5: 0005-Port-driver-to-PCI-rework-interfaces.patch
Patch6: 0006-RENDITION_VERSION-using-PACKAGE_VERSION_.patch
Patch7: 0007-Update-for-new-policy-of-hidden-symbols-and-common-m.patch
########################################################################
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.1.5-4mdk
BuildRequires: x11-util-modular
Conflicts: xorg-x11-server < 7.0

%description
The X.org driver for Rendition (Micron) Cards

%package devel
Summary: Development files for %{name}
Group: Development/X11
License: MIT

%description devel
Development files for %{name}

%prep
%setup -q -n xf86-video-rendition-%{version}

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

%build
autoreconf -ifs
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std
# Create list of dependencies
x-check-deps.pl
for deps in *.deps; do
    install -D -m 644 $deps %{buildroot}/%{_datadir}/X11/mandriva/$deps
done

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/xorg/modules/drivers/rendition_drv.so
%{_libdir}/xorg/modules/v20002d.uc
%{_libdir}/xorg/modules/v10002d.uc
%{_mandir}/man4/rendition.*

%files devel
%defattr(-,root,root)
%{_libdir}/xorg/modules/drivers/*.la
%{_datadir}/X11/mandriva/*.deps

Name:		x11-driver-video-rendition
Version:	4.2.5
Release:	3
Summary:	X.org driver for Rendition (Micron) Cards
Group:		System/X11
License:	MIT
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-rendition-%{version}.tar.bz2
Source10:	x11-driver-video-rendition.rpmlintrc

BuildRequires:	x11-proto-devel >= 1.0.0
BuildRequires:	x11-server-devel >= 1.0.1
BuildRequires:	x11-util-macros >= 1.0.1

Requires:	x11-server-common %(xserver-sdk-abi-requires videodrv)

Conflicts:	xorg-x11-server < 7.0

%description
x11-driver-video-rendition is the X.org driver for Rendition (Micron) Cards.

%prep
%setup -qn xf86-video-rendition-%{version}

%build
%configure2_5x
%make

%install
%makeinstall_std
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%files
%{_libdir}/xorg/modules/drivers/rendition_drv.so
%{_libdir}/xorg/modules/v20002d.uc
%{_libdir}/xorg/modules/v10002d.uc
%{_mandir}/man4/rendition.*


%changelog
* Mon Jul 23 2012 Alexander Khrukin <akhrukin@mandriva.org> 4.2.5-1
+ Revision: 810704
- version update 4.2.5

* Sat Dec 31 2011 Matthew Dawkins <mattydaw@mandriva.org> 4.2.4-7
+ Revision: 748445
- rebuild cleaned up spec

* Sat Oct 08 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 4.2.4-6
+ Revision: 703681
- rebuild for new x11-server

* Thu Jun 09 2011 Eugeni Dodonov <eugeni@mandriva.com> 4.2.4-5
+ Revision: 683582
- Rebuild for new x11-server

* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 4.2.4-4
+ Revision: 671162
- mass rebuild

* Wed Nov 10 2010 Thierry Vignaud <tv@mandriva.org> 4.2.4-3mdv2011.0
+ Revision: 595728
- require xorg server with proper ABI

* Sun Oct 10 2010 Thierry Vignaud <tv@mandriva.org> 4.2.4-2mdv2011.0
+ Revision: 584626
- bump release before rebuilding for xserver 1.9

* Tue Jul 20 2010 Thierry Vignaud <tv@mandriva.org> 4.2.4-1mdv2011.0
+ Revision: 555160
- new release

* Mon Sep 07 2009 Thierry Vignaud <tv@mandriva.org> 4.2.3-1mdv2010.0
+ Revision: 432725
- fix build
- new release

* Fri Jul 03 2009 Ander Conselvan de Oliveira <ander@mandriva.com> 4.2.2-1mdv2010.0
+ Revision: 391885
- update to new version 4.2.2

* Thu Feb 26 2009 Thierry Vignaud <tv@mandriva.org> 4.2.1-1mdv2009.1
+ Revision: 345054
- new release

  + Colin Guthrie <cguthrie@mandriva.org>
    - Rebuild for new xserver

* Sun Nov 30 2008 Adam Williamson <awilliamson@mandriva.org> 4.2.0-3mdv2009.1
+ Revision: 308218
- rebuild for new X server

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 4.2.0-2mdv2009.0
+ Revision: 265925
- rebuild early 2009.0 package (before pixel changes)
- improved description
- add missing dot at end of description
- improved summary

* Tue Apr 15 2008 Paulo Andrade <pcpa@mandriva.com.br> 4.2.0-1mdv2009.0
+ Revision: 194166
- Update to version 4.2.0.

* Mon Feb 11 2008 Paulo Andrade <pcpa@mandriva.com.br> 4.1.3-5mdv2008.1
+ Revision: 165588
- Revert to use upstream tarball and remove local patches.

* Tue Jan 22 2008 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 4.1.3-4mdv2008.1
+ Revision: 156615
- re-enable rpm debug packages support

* Fri Jan 18 2008 Paulo Andrade <pcpa@mandriva.com.br> 4.1.3-3mdv2008.1
+ Revision: 154841
- Updated BuildRequires and resubmit package.
- Remove -devel package as it isn't really required as it provides only 2 files
  that aren't even header files; still don't install the .la files.
  All dependency files should be stored in the x11-util-modular package as they
  are only required for the "modular" build.
- Move .la files to new -devel package, and also add .deps files to -devel package.
- Fix to generate tarball from tag xf86-video-rendition-4.1.3, and generate
  patches from that point until mandriva branch.
- Update for new policy of hidden symbols and common macros.

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Oct 16 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 4.1.3-2mdv2008.1
+ Revision: 99042
- minor spec cleanup
- build against new xserver (1.4)

  + Thierry Vignaud <tv@mandriva.org>
    - fix man pages


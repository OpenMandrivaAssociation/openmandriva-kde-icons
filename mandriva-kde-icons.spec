Name: mandriva-kde-icons
Summary: Mandriva KDE icons
Version: 1.0.4
Release: %mkrel 14
Epoch: 1
URL: http://www.mandriva.com
Group: Graphical desktop/KDE
BuildRoot: %_tmppath/%name-buildroot
Source0: %{name}-%{version}.tar.bz2
License: GPL
BuildArch: noarch
Provides: kde-custom-icons

%description
This package contains all specific mandriva icons.
This include special folders icons and actions icons

%files
%defattr(-,root,root)
%{_iconsdir}/*/*/*/*
%{_iconsdir}/favicons/*

#--------------------------------------------------------------------

%prep
%setup -q -n %name-%version

%install
rm -rf %buildroot
mkdir -p %buildroot
cp -fr * %buildroot
mv -f %buildroot%_iconsdir/crystalsvg %buildroot%_iconsdir/oxygen

%clean
rm -rf %buildroot


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1:1.0.4-13mdv2011.0
+ Revision: 666385
- mass rebuild

* Wed Sep 15 2010 Funda Wang <fwang@mandriva.org> 1:1.0.4-12mdv2011.0
+ Revision: 578393
- we are using kde4 now, so icons should be installed in oxygen theme by default

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 1:1.0.4-11mdv2010.1
+ Revision: 523268
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1:1.0.4-10mdv2010.0
+ Revision: 426074
- rebuild

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Remove old macros

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1:1.0.4-9mdv2009.1
+ Revision: 351565
- rebuild

* Fri Jun 20 2008 Pixel <pixel@mandriva.com> 1:1.0.4-8mdv2009.0
+ Revision: 227421
- rebuild for fixed %%update_icon_cache/%%clean_icon_cache/%%post_install_gconf_schemas
- rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1:1.0.4-7mdv2009.0
+ Revision: 223153
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 1:1.0.4-6mdv2008.1
+ Revision: 152908
- rebuild
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Sep 21 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 1:1.0.4-4mdv2008.0
+ Revision: 91826
- Removed buyit and subscribe icons: they are in desktop-common-data now


* Thu Mar 15 2007 Laurent Montel <lmontel@mandriva.com> 1.0.4-3mdv2007.1
+ Revision: 144364
- Update icon cache
- New icons

* Wed Mar 07 2007 Laurent Montel <lmontel@mandriva.com> 1:1.0.4-1mdv2007.1
+ Revision: 134192
- New icons

* Sat Sep 16 2006 Laurent Montel <lmontel@mandriva.com> 1:1.0.3-2mdv2007.0
+ Revision: 61530
- New package (2006-09-15 1.0.3-2mdv)
  Fix bookmarks icons

* Sat Sep 16 2006 Laurent Montel <lmontel@mandriva.com> 1:1.0.3-1mdv2007.0
+ Revision: 61525
- New package (2006-09-15 1.0.3-1mdv)
  Add bookmarks icons

* Tue Jul 25 2006 Helio Chissini de Castro <helio@mandriva.com> 1:1.0.2-1mdv2007.0
+ Revision: 42022
- Added missing source
- Added kdebase mandriva custom icons recently moved from kdebase package

* Sun Jul 16 2006 Laurent Montel <lmontel@mandriva.com> 1:1.0.1-2mdv2007.0
+ Revision: 41282
- Add provides virtual

* Sat Jul 15 2006 Helio Chissini de Castro <helio@mandriva.com> 1:1.0.1-1mdv2007.0
+ Revision: 41182
- Added icons moved from kdelibs package

* Tue Jul 11 2006 Helio Chissini de Castro <helio@mandriva.com> 1:1.0-1mdv2007.0
+ Revision: 38698
- Introduced mandriva kde icons firts release
- Icons removed from kdepim package now is rpesented on right structure here
- import mandriva-kde-icons-1.0-1mdv2007.0


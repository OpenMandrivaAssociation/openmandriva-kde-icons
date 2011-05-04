Name: mandriva-kde-icons
Summary: Mandriva KDE icons
Version: 1.0.4
Release: %mkrel 13
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

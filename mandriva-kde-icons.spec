Name: mandriva-kde-icons
Summary: Mandriva KDE icons
Version:	1.0.4
Release:	%mkrel 5
Epoch: 1
URL: http://www.mandriva.com
Group: Graphical desktop/KDE
BuildRoot: %_tmppath/%name-buildroot
Source0: %{name}-%{version}.tar.bz2
License:	GPL
BuildArch: noarch
Provides:	kde-custom-icons

%description
This package contains all specific mandriva icons.
This include special folders icons and actions icons

%post
%if %mdkversion > 200600
%update_icon_cache crystalsvg
%endif

%postun
%if %mdkversion > 200600
%clean_icon_cache crystalsvg
%endif


%files
%defattr(0644,root,root,755)
%_datadir/icons/*

%prep
%setup -q -n %name-%version

%install
rm -rf %buildroot
install -d -m 0755 %buildroot
mv * %buildroot

%clean
rm -rf %buildroot





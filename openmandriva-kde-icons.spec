Name:		openmandriva-kde-icons
Summary:	OpenMandriva KDE icons
Version:	1.0.4
Release:	18
Epoch:		1
URL:		%{disturl}
Group:		Graphical desktop/KDE
Source0:	%{name}-%{version}.tar.xz
License:	GPL
BuildArch:	noarch
Provides:	kde-custom-icons
%rename		mandriva-kde-icons

%description
This package contains all specific mandriva icons.
This include special folders icons and actions icons.

%prep
%setup -q

%install
mkdir -p %{buildroot}
cp -fr * %{buildroot}
mv -f %{buildroot}%{_iconsdir}/crystalsvg %{buildroot}%{_iconsdir}/oxygen

%files
%{_iconsdir}/*/*/*/*
%{_iconsdir}/favicons/*

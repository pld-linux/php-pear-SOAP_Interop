%include	/usr/lib/rpm/macros.php
%define		_class		SOAP
%define		_subclass	Interop
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - SOAP Interop test application
Summary(pl.UTF-8):   %{_pearname} - testowa aplikacja SOAP Interop
Name:		php-pear-%{_pearname}
Version:	0.8
Release:	2.3
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	071bbf96a2eaaf175b9f7a4e7309de46
Patch0:		%{name}-path_fix.patch
URL:		http://pear.php.net/package/SOAP_Interop/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
BuildRequires:	missing dep: pear(SOAP/Interop/interop_Round3GroupD.php)
Requires:	php-pear
Requires:	php-pear-SOAP
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# unavailable
%define		_noautoreq 'pear(SOAP/Interop/interop_Round3GroupD.php)'

%description
Test harness for SOAP Builders tests. Supports Round 2 and Round 3
tests.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Środowisko testowe do testów SOAP Builders. Obsługuje testy rundy 2 i
3.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

# extract config.php.orig from tarball that setup cleaned. TODO. include as Source1.
tar zxf %{SOURCE0} %{_pearname}-%{version}/config.php.orig

install -d docs/%{_pearname}
mv ./%{php_pear_dir}/%{_class}/%{_subclass}/readme.txt docs/%{_pearname}

cd ./%{php_pear_dir}/%{_class}/%{_subclass}
%patch0 -p2

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install
install %{_pearname}-%{version}/config.php.orig $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/config.php

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/*
%dir %{php_pear_dir}/%{_class}/%{_subclass}
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/%{_subclass}/*

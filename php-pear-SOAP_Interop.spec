%include	/usr/lib/rpm/macros.php
%define         _class          SOAP
%define         _subclass       Interop
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - SOAP Interop Test Application
Summary(pl):	%{_pearname} - testowa aplikacja SOAP Interop
Name:		php-pear-%{_pearname}
Version:	0.7.2
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Test harness for SOAP Builders tests. Supports Round 2 and Round 3
tests.

This class has in PEAR status: %{_status}.

%description -l pl
¦rodowisko testowe do testów SOAP Builders. Obs³uguje testy rundy 2 i
3.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/wsdl/imported

install %{_pearname}-%{version}/*.{php,sql,orig} $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}
install %{_pearname}-%{version}/wsdl/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/wsdl
install %{_pearname}-%{version}/wsdl/imported/* $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/wsdl/imported

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/readme.txt
%dir %{php_pear_dir}/%{_class}/%{_subclass}
%dir %{php_pear_dir}/%{_class}/%{_subclass}/wsdl
%dir %{php_pear_dir}/%{_class}/%{_subclass}/wsdl/imported
%{php_pear_dir}/%{_class}/%{_subclass}/*
%{php_pear_dir}/%{_class}/%{_subclass}/wsdl/*
%{php_pear_dir}/%{_class}/%{_subclass}/wsdl/imported/*

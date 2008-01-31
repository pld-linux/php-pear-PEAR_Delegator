%include	/usr/lib/rpm/macros.php
%define		_class		PEAR
%define		_subclass	Delegator
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - delegation for PHP
Summary(pl.UTF-8):	%{_pearname} - delegacja dla PHP
Name:		php-pear-%{_pearname}
Version:	0.1.0
Release:	3
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	196de218a439a2f2591177d43fe2a072
Patch0:		%{name}-path_fix.patch
URL:		http://pear.php.net/package/PEAR_Delegator/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package implements traditional and unorthodox delegation in PHP.
This allows for pseudo multiple inheritance and other interesting
design paradigms.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Implementacja tradycyjnej i niekonwencjonalnej delegacji w PHP.
Pozwala to na pseudo-wielokrotne dziedziczenie jak również inne
interesujące paradygmaty.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup
cd ./%{php_pear_dir}/%{_class}
%patch0 -p0

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/%{_subclass}.php
%{php_pear_dir}/%{_class}/%{_subclass}

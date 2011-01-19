%define upstream_name       Youri-Config
%define upstream_version    0.2.1

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1
Summary:	Youri configuration handler
License:	GPL or Artistic
Group:		Development/Other
Url:		http://youri.zarb.org
Source:		http://youri.zarb.or/download/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires:  perl(YAML::AppConfig)
BuildRequires:  perl-version
Requires:       perl-version
Buildarch:	    noarch
BuildRoot:	    %{_tmppath}/%{name}-%{version}

%description
YOURI stands for "Youri Offers an Upload & Repository Infrastucture". It aims
to build tools making management of a coherent set of packages easier.

This package provides configuration handling for other youri programs.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%__make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc ChangeLog README
%{perl_vendorlib}/Youri
%{_mandir}/man3/*



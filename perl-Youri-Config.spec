%define upstream_name       Youri-Config
%define upstream_version    0.2.1

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2
Summary:	Youri configuration handler
License:	GPL or Artistic
Group:		Development/Other
Url:		http://youri.zarb.org
Source:		http://youri.zarb.or/download/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(YAML::AppConfig)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(version)
Requires:	perl(version)
BuildArch:	noarch

%description
YOURI stands for "Youri Offers an Upload & Repository Infrastucture". It aims
to build tools making management of a coherent set of packages easier.

This package provides configuration handling for other youri programs.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files 
%doc ChangeLog README
%{perl_vendorlib}/Youri
%{_mandir}/man3/*

%changelog
* Sat Jan 22 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.2.1-1mdv2011.0
+ Revision: 632210
- new version

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.2.0-5mdv2010.0
+ Revision: 430671
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 0.2.0-4mdv2009.0
+ Revision: 258921
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.2.0-3mdv2009.0
+ Revision: 246798
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.2.0-1mdv2008.1
+ Revision: 136373
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed May 02 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.2.0-1mdv2008.0
+ Revision: 20746
- new release
- force dependency on perl-version


* Fri Mar 09 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.1.1-1mdv2007.1
+ Revision: 138940
- fix build dependencies _correctly_
- fix build dependencies
- Imported perl-Youri-Config-0.1.1-1mdv2007.1 into SVN repository.

* Fri Mar 09 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.1.1-1mdv2007.1
- first mdv release


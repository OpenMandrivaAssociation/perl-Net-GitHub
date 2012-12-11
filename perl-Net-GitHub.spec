%define upstream_name    Net-GitHub
%define upstream_version 0.28

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Perl Interface for github.com
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Any::Moose)
BuildRequires:	perl(Crypt::SSLeay)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(File::Slurp)
BuildRequires:	perl(HTML::TreeBuilder)
BuildRequires:	perl(JSON::Any)
BuildRequires:	perl(Test::MockModule)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(URI::Escape)
BuildRequires:	perl(WWW::Mechanize::GZip)
BuildRequires:	perl(HTTP::Request::Common)
BuildArch:	noarch

%description
Perl Interface for github.com 

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README META.yml
%{_mandir}/man3/*
%{perl_vendorlib}/Net/

%changelog
* Thu Mar 10 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.280.0-1mdv2011.0
+ Revision: 643414
- update to new version 0.28

* Mon Feb 28 2011 Funda Wang <fwang@mandriva.org> 0.270.0-2
+ Revision: 640772
- rebuild to obsolete old packages

* Sun Feb 20 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.270.0-1
+ Revision: 638931
- update to new version 0.27

* Thu Feb 03 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.260.0-1
+ Revision: 635445
- update to new version 0.26

* Sun Jan 02 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.240.0-1mdv2011.0
+ Revision: 627525
- update to new version 0.24

* Fri Nov 12 2010 Jérôme Quelin <jquelin@mandriva.org> 0.230.0-1mdv2011.0
+ Revision: 596624
- update to 0.23

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 0.220.0-1mdv2011.0
+ Revision: 552427
- update to 0.22

* Fri Apr 30 2010 Michael Scherer <misc@mandriva.org> 0.200.0-1mdv2010.1
+ Revision: 541160
- import perl-Net-GitHub


* Fri Apr 30 2010 cpan2dist 0.20-1mdv
- initial mdv release, generated with cpan2dist

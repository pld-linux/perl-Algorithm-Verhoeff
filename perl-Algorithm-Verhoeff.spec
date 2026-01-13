#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Algorithm
%define	pnam	Verhoeff
Summary:	Algorithm::Verhoeff - Perl extension for checking and computing Verhoeff check digits
Summary(pl.UTF-8):	Algorithm::Verhoeff - rozszerzenie Perla do przeprowadzania i obliczania testów Verhoeffa
Name:		perl-Algorithm-Verhoeff
Version:	0.3
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/J/JP/JPETERSON/Algorithm-Verhoeff-0.3.tar.gz
# Source0-md5:	556d356ba789b562d72ce792cd7bf94d
URL:		http://search.cpan.org/dist/Algorithm-Verhoeff/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This implements the Verhoeff check digit algorithm. It's a single digit checksum
designed specifically for catching data entry mistakes in number sequences. It
catches the vast majority of common mistakes such as transposed digits, ommitted
digits, double entered digits and so on.

%description -l pl.UTF-8
Moduł ten dostarcza testów Verhoeffa.

%prep
%setup -q -n %{pdir}-%{pnam}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Algorithm/*.pm
%{_mandir}/man3/*

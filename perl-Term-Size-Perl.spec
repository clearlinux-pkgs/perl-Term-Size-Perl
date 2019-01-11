#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Term-Size-Perl
Version  : 0.031
Release  : 9
URL      : https://cpan.metacpan.org/authors/id/F/FE/FERREIRA/Term-Size-Perl-0.031.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/F/FE/FERREIRA/Term-Size-Perl-0.031.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libt/libterm-size-perl-perl/libterm-size-perl-perl_0.031-1.debian.tar.xz
Summary  : 'Perl extension for retrieving terminal size (Perl version)'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Term-Size-Perl-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
Term::Size::Perl is a Perl module which provides a straightforward
way to get the size of the terminal (or window) on which
a script is running.

%package dev
Summary: dev components for the perl-Term-Size-Perl package.
Group: Development
Provides: perl-Term-Size-Perl-devel = %{version}-%{release}

%description dev
dev components for the perl-Term-Size-Perl package.


%package license
Summary: license components for the perl-Term-Size-Perl package.
Group: Default

%description license
license components for the perl-Term-Size-Perl package.


%prep
%setup -q -n Term-Size-Perl-0.031
cd ..
%setup -q -T -D -n Term-Size-Perl-0.031 -b 1
mkdir -p deblicense/
cp -r %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Term-Size-Perl-0.031/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Term-Size-Perl
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-Term-Size-Perl/LICENSE
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-Term-Size-Perl/deblicense_copyright
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/Term/Size/Perl.pm
/usr/lib/perl5/vendor_perl/5.28.1/Term/Size/Perl/Params.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Term::Size::Params.3
/usr/share/man/man3/Term::Size::Perl.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Term-Size-Perl/LICENSE
/usr/share/package-licenses/perl-Term-Size-Perl/deblicense_copyright

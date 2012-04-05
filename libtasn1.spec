# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.23
# 
# >> macros
# << macros

Name:       libtasn1
Summary:    This is the ASN.1 library used in GNUTLS
Version:    2.12
Release:    1
Group:      System/Libraries
License:    LGPLv2.1+
URL:        http://www.gnu.org/software/libtasn1/
Source0:    http://ftp.gnu.org/gnu/libtasn1/%{name}-%{version}.tar.gz
Source100:  libtasn1.yaml
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  bison


%description
This is the ASN.1 library used in GNUTLS.  More up to date information can
be found at http://www.gnu.org/software/gnutls and http://www.gnutls.org



%package tools
Summary:    Some ASN.1 tools
License:    GPLv3+
Group:      Applications/Text
Requires:   %{name} = %{version}-%{release}

%description tools
This is the ASN.1 library used in GNUTLS.  More up to date information can
be found at http://www.gnu.org/software/gnutls and http://www.gnutls.org

This package contains tools using the libtasn library.


%package devel
Summary:    Files for development of applications which will use libtasn1
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires(post): /sbin/install-info
Requires(postun): /sbin/install-info

%description devel
This is the ASN.1 library used in GNUTLS.  More up to date information can
be found at http://www.gnu.org/software/gnutls and http://www.gnutls.org

This package contains files for development of applications which will
use libtasn1.



%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%configure --disable-static
make %{?jobs:-j%jobs}

# >> build post
# << build post
%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
# << install post



%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig






%post devel
%install_info --info-dir=%_infodir %{_infodir}/libtasn1.info.gz

%postun devel
if [ $1 = 0 ] ;then
%install_info_delete --info-dir=%{_infodir} %{_infodir}/libtasn1.info.gz
fi

%files
%defattr(-,root,root,-)
# >> files
%doc COPYING.LIB
%{_libdir}/*.so.*
# << files


%files tools
%defattr(-,root,root,-)
# >> files tools
%doc COPYING
%{_bindir}/asn1*
%doc %{_mandir}/man1/asn1*
# << files tools

%files devel
%defattr(-,root,root,-)
# >> files devel
%doc README THANKS AUTHORS
%doc doc/TODO doc/*.pdf ChangeLog NEWS
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*
%doc %{_infodir}/libtasn1.info.gz
%doc %{_mandir}/man3/*asn1*
# << files devel


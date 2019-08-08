Name:       libtasn1
Summary:    This is the ASN.1 library used in GNUTLS
Version:    4.13
Release:    1
Group:      System/Libraries
License:    LGPLv2+
URL:        http://www.gnu.org/software/libtasn1/
Source0:    %{name}-%{version}.tar.gz
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  bison
BuildRequires:  help2man
BuildRequires:  texinfo

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

%package doc
Summary:   Documentation for %{name}
Group:     Documentation
Requires:  %{name} = %{version}-%{release}
Requires(post): /sbin/install-info
Requires(postun): /sbin/install-info

%description doc
Man and info pages for %{name}.

%prep
%setup -q -n %{name}-%{version}/%{name}

%build
touch ChangeLog
autoreconf -v -f -i
%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install

mkdir -p %{buildroot}%{_docdir}/%{name}-%{version}
install -m0644 -t %{buildroot}%{_docdir}/%{name}-%{version} \
	AUTHORS ChangeLog NEWS README THANKS doc/TODO

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%post doc
%install_info --info-dir=%_infodir %{_infodir}/%{name}.info.gz

%postun doc
if [ $1 = 0 ] ;then
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz
fi

%files
%defattr(-,root,root,-)
%license COPYING.LIB
%{_libdir}/*.so.*

%files tools
%defattr(-,root,root,-)
%license COPYING
%{_bindir}/asn1*

%files devel
%defattr(-,root,root,-)
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*

%files doc
%defattr(-,root,root,-)
%{_infodir}/%{name}.*
%{_mandir}/man*/*asn1*
%{_docdir}/%{name}-%{version}

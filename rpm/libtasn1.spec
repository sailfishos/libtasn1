Name:       libtasn1
Summary:    This is the ASN.1 library used in GNUTLS
Version:    4.20.0
Release:    1
License:    LGPLv2+
URL:        https://github.com/sailfishos/libtasn1
Source0:    %{name}-%{version}.tar.gz
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  bison
BuildRequires:  libtool

%description
This is the ASN.1 library used in GNUTLS.  More up to date information can
be found at http://www.gnu.org/software/gnutls and http://www.gnutls.org

%package tools
Summary:    Some ASN.1 tools
License:    GPLv3+
Requires:   %{name} = %{version}-%{release}

%description tools
This is the ASN.1 library used in GNUTLS.  More up to date information can
be found at http://www.gnu.org/software/gnutls and http://www.gnutls.org

This package contains tools using the libtasn library.

%package devel
Summary:    Files for development of applications which will use libtasn1
Requires:   %{name} = %{version}-%{release}

%description devel
This is the ASN.1 library used in GNUTLS.  More up to date information can
be found at http://www.gnu.org/software/gnutls and http://www.gnutls.org

This package contains files for development of applications which will
use libtasn1.

%prep
%autosetup -p1 -n %{name}-%{version}/%{name}

%build

# Set tarball-version so the gnu version script picks it up
# to set the application version
echo %{version} | sed -e 's|\+.*||' > .tarball-version

./bootstrap \
    --no-git  \
    --gnulib-srcdir=$PWD/../gnulib

%configure \
    --disable-doc \
    --disable-static \
    --disable-silent-rules \
    %{nil}

%make_build

%install
%make_install

%check
make check

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license COPYING.LESSERv2
%{_libdir}/*.so.*

%files tools
%license COPYING
%{_bindir}/asn1*

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*

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
BuildRequires:  help2man
BuildRequires:  texinfo
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

%package doc
Summary:   Documentation for %{name}
Requires:  %{name} = %{version}-%{release}
Requires(post): /sbin/install-info
Requires(postun): /sbin/install-info

%description doc
Man and info pages for %{name}.

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
    --disable-static \
    --disable-silent-rules \
    %{nil}

# libtasn1 likes to regenerate docs
touch doc/stamp_docs
%make_build

%install
%make_install

mkdir -p %{buildroot}%{_docdir}/%{name}-%{version}
install -m0644 -t %{buildroot}%{_docdir}/%{name}-%{version} \
	AUTHORS ChangeLog NEWS README THANKS doc/TODO

%check
make check

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%post doc
%install_info --info-dir=%_infodir %{_infodir}/%{name}.info.gz

%postun doc
if [ $1 = 0 ] ;then
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz
fi

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

%files doc
%{_infodir}/%{name}.*
%{_mandir}/man*/*asn1*
%{_docdir}/%{name}-%{version}

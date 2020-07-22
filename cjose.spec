Name:                cjose
Version:             0.6.1
Release:             3
Summary:             C library implementing the Javascript Object Signing and Encryption (JOSE)
License:             MIT
URL:                 https://github.com/cisco/cjose
Source0:             https://github.com/cisco/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch1:              concatkdf.patch
BuildRequires:       gcc doxygen libtcnative-1-0 jansson-devel check-devel openssl-devel
%description
Implementation of JOSE for C/C++

%package             devel
Summary:             Development files for %{name}
Requires:            %{name}%{?_isa} = %{version}-%{release}
%description         devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n %{name}-%{version} -p1

%build
%configure
%make_build

%install
%make_install
find %{buildroot} -name '*.a' -exec rm -f {} ';'
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%check
make check || (cat test/test-suite.log; exit 1)

%files
%license LICENSE
%doc CHANGELOG.md README.md
%doc /usr/share/doc/cjose
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/cjose.pc

%changelog
* Sat Jul 18 2020 yanan li <liyanan032@huawei.com> - 0.6.1-3
- Package init

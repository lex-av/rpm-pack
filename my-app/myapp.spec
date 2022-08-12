# spec file for package myapp (Version 1.0)
#
%define debug_package %{nil}
Name:         myapp
Version:      1.0
Release:      1
License:      Simple rpm package
Group:        Applications/Media
Provides:     prints message
source:       %{name}_%{version}.tar.gz
Summary:      Trivial application
%description
MyApp Trivial Application
A trivial application used to demonstrate development tools.
%prep
%setup -q
%build
make
%install
mkdir -p %{buildroot}%{_bindir}
install -m755 myapp %{buildroot}%{_bindir}/myapp
%clean
rm -rf $RPM_BUILD_ROOT
%files
%{_bindir}/myapp



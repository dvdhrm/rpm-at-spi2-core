Name:           at-spi2-core
Version:        1.91.91
Release:        1%{?dist}
Summary:        Protocol definitions and daemon for D-Bus at-spi

Group:          System Environment/Libraries
License:        LGPLv2+
URL:            http://www.linuxfoundation.org/en/AT-SPI_on_D-Bus
Source0:        http://download.gnome.org/sources/at-spi2-core/1.91/%{name}-%{version}.tar.bz2

BuildRequires:  dbus-devel
BuildRequires:  dbus-glib-devel
BuildRequires:  glib2-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  libXtst-devel
BuildRequires:  libXevie-devel
BuildRequires:  libXext-devel
BuildRequires:  autoconf automake libtool
BuildRequires:  intltool

# XXX Ugly Hack
# Needed for https://bugzilla.gnome.org/show_bug.cgi?id=640303
BuildRequires: at-spi2-core

Requires:       dbus

%description
at-spi allows assistive technologies to access GTK-based
applications. Essentially it exposes the internals of applications for
automation, so tools such as screen readers, magnifiers, or even
scripting interfaces can query and interact with GUI controls.

This version of at-spi is a major break from previous versions.
It has been completely rewritten to use D-Bus rather than
ORBIT / CORBA for its transport protocol.

%package devel
Summary: Development files and headers for at-spi2-core
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
The at-spi2-core-devel package includes the header files and
API documentation for libatspi.

%prep
%setup -q

%build
%configure --with-dbus-daemondir=/bin
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT

%{find_lang} %{name}

rm $RPM_BUILD_ROOT%{_libdir}/libatspi.la

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc COPYING AUTHORS README
# %dir %{_sysconfdir}/at-spi2
# %config(noreplace) %{_sysconfdir}/at-spi2/accessibility.conf
# %{_sysconfdir}/xdg/autostart/at-spi-dbus-bus.desktop
# %{_bindir}/at-spi-dbus-bus
%{_libexecdir}/at-spi2-registryd
%{_datadir}/dbus-1/services/org.a11y.atspi.Registry.service
%{_sysconfdir}/at-spi2
%{_sysconfdir}/xdg/autostart/at-spi-dbus-bus.desktop
%{_bindir}/at-spi-dbus-bus
%{_libdir}/libatspi.so.*
%{_libdir}/girepository-1.0/Atspi-2.0.typelib

%files devel
%{_libdir}/libatspi.so
%{_datadir}/gtk-doc/html/libatspi
%{_datadir}/gir-1.0/Atspi-2.0.gir
%{_includedir}/at-spi-2.0

%changelog
* Mon Mar  7 2011 Matthias Clasen <mclasen@redhat.com> - 1.91.91-1
- Update to 1.91.91

* Tue Feb 22 2011 Matthias Clasen <mclasen@redhat.com> - 1.91.90-1
- Update to 1.91.90

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.91.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb  2 2011 Christopher Aillon <caillon@redhat.com> - 1.91.6.1-1
- Update to 1.91.6.1

* Tue Feb  1 2011 Christopher Aillon <caillon@redhat.com> - 1.91.6-1
- Update to 1.91.6

* Fri Jan 21 2011 Christopher Aillon <caillon@redhat.com> - 1.91.5-2
- Add gobject-introspection support

* Mon Jan 10 2011 Matthias Clasen <mclasen@redhat.com> - 1.91.5-1
- Update to 1.91.5

* Thu Nov 11 2010 Matthias Clasen <mclasen@redhat.com> - 1.91.2-1
- Update 1.91.2

* Mon Oct  4 2010 Matthias Clasen <mclasen@redhat.com> - 1.91.0-1
- Update to 1.91.0

* Wed Sep 29 2010 Matthias Clasen <mclasen@redhat.com> - 0.4.0-1
- Update to 0.4.0

* Tue Aug 31 2010 Matthias Clasen <mclasen@redhat.com> - 0.3.91-1
- Update to 0.3.91

* Wed Aug 18 2010 Matthias Clasen <mclasen@redhat.com> - 0.3.90-1
- Update to 0.3.90

* Tue Jun 29 2010 Matthias Clasen <mclasen@redhat.com> - 0.3.4-1
- Update to 0.3.4

* Tue Jun  8 2010 Matthias Clasen <mclasen@redhat.com> - 0.3.3-1
- Update to 0.3.3

* Tue Jun  1 2010 Matthias Clasen <mclasen@redhat.com> - 0.3.2-2
- Don't relocate the dbus a11y stack

* Fri May 28 2010 Matthias Clasen <mclasen@redhat.com> - 0.3.2-1
- Update to 0.3.2

* Sat May 15 2010 Matthias Clasen <mclasen@redhat.com> - 0.3.1-1
- Update to 0.3.1

* Tue Mar 30 2010 Matthias Clasen <mclasen@redhat.com> - 0.1.8-1
- Update to 0.1.8

* Sat Feb 20 2010 Matthias Clasen <mclasen@redhat.com> - 0.1.7-1
- Update to 0.1.7

* Wed Feb 10 2010 Tomas Bzatek <tbzatek@redhat.com> - 0.1.6-1
- Update to 0.1.6

* Wed Jan 20 2010 Matthias Clasen <mlasen@redhat.com> - 0.1.5-2
- Specify the right location for the dbus daemon

* Sun Jan 16 2010 Matthias Clasen <mlasen@redhat.com> - 0.1.5-1
- Update to 0.1.5

* Tue Dec 22 2009 Matthias Clasen <mlasen@redhat.com> - 0.1.4-1
- Update to 0.1.4

* Sat Dec  4 2009 Matthias Clasen <mlasen@redhat.com> - 0.1.3-1
- Initial packaging

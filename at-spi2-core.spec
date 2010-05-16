Name:           at-spi2-core
Version:        0.3.1
Release:        1%{?dist}
Summary:        Protocol definitions and daemon for D-Bus at-spi

Group:          System Environment/Libraries
License:        LGPLv2+
URL:            http://www.linuxfoundation.org/en/AT-SPI_on_D-Bus
Source0:        http://download.gnome.org/sources/at-spi2-core/0.3/%{name}-%{version}.tar.bz2
Patch0:         libs.patch

BuildRequires:  dbus-devel
BuildRequires:  dbus-glib-devel
BuildRequires:  glib2-devel
BuildRequires:  gtk2-devel
BuildRequires:  libXtst-devel
BuildRequires:  libXevie-devel
BuildRequires:  libXext-devel
BuildRequires:  autoconf automake libtool

Requires:       dbus

%description
at-spi allows assistive technologies to access GTK-based
applications. Essentially it exposes the internals of applications for
automation, so tools such as screen readers, magnifiers, or even
scripting interfaces can query and interact with GUI controls.

This version of at-spi is a major break from previous versions.
It has been completely rewritten to use D-Bus rather than
ORBIT / CORBA for its transport protocol.


%prep
%setup -q
%patch0 -p1 -b .libs

autoreconf -i -if

%build
%configure --with-dbus-daemon=/bin --enable-relocate
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc COPYING AUTHORS README
# %dir %{_sysconfdir}/at-spi2
# %config(noreplace) %{_sysconfdir}/at-spi2/accessibility.conf
# %{_sysconfdir}/xdg/autostart/at-spi-dbus-bus.desktop
# %{_bindir}/at-spi-dbus-bus
%{_libexecdir}/at-spi2-registryd
%{_datadir}/dbus-1/services/org.a11y.atspi.Registry.service


%changelog
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

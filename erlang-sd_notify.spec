
%bcond_without	tests		# build without tests

Summary:	Erlang bindings for systemd-notify subsystem
Name:		erlang-sd_notify
Version:	0.1
Release:	3
License:	MIT
Group:		Development/Languages
Source0:	https://github.com/lemenkov/erlang-sd_notify/tarball/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	c271c733a9ff626932961ba69fe6b0c6
URL:		https://support.process-one.net/doc/display/EXMPP/exmpp+home
BuildRequires:	erlang-rebar
BuildRequires:	systemd-devel
Requires:	erlang
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Erlang bindings for systemd-notify subsystem.

%prep
%setup -qc
mv lemenkov-erlang-sd_notify-*/* .
%{__rm} -r lemenkov-erlang-sd_notify-*

%build
%{__make} \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags} -lsystemd" \
	REBAR=%{_bindir}/rebar \
	REBAR_FLAGS="-v"

%if %{with tests}
%{__make} test
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/erlang/lib/sd_notify-%{version}/{priv,ebin}
cp -p ebin/* $RPM_BUILD_ROOT%{_libdir}/erlang/lib/sd_notify-%{version}/ebin
cp -p priv/* $RPM_BUILD_ROOT%{_libdir}/erlang/lib/sd_notify-%{version}/priv

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_libdir}/erlang/lib/sd_notify-%{version}
%dir %{_libdir}/erlang/lib/sd_notify-%{version}/ebin
%{_libdir}/erlang/lib/sd_notify-%{version}/ebin/sd_notify.app
%{_libdir}/erlang/lib/sd_notify-%{version}/ebin/sd_notify.beam
%dir %{_libdir}/erlang/lib/sd_notify-%{version}/priv
%attr(755,root,root) %{_libdir}/erlang/lib/sd_notify-%{version}/priv/sd_notify_drv.so

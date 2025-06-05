Name:                    ftphealthcheck
Version:                 0.1
Release:                 1%{?dist}
Summary:                 Check health of local FTP service

License:                 AGPLv3

BuildArch:               noarch
BuildRequires:           systemd
Requires:                lftp >= 4.8
%{?systemd_requires}

%description
Tries to connect to a local FTP service, but if it fails,
then tell systemd to restart the FTP service.


%prep
%setup -q

%build
%configure 
%make_build

%install
%make_install 
%find_lang %{name} 

%pre
getent group %{name} >/dev/null || groupadd -r %{name}
getent passwd %{name} >/dev/null || \
    useradd -r -g %{name} -d /var/run/%{name} -s /sbin/nologin -c "%{summary}" %{name}
exit 0


%files
%license LICENSE 
%doc README 
%config %{_sysconfdir}/ftphealthcheck.conf
%config %{_sysconfdir}/files\etc\tmpfiles.d\ftphealthcheck.conf
%config %{_prefix}/lib/systemd/system/
%{_bindir}/%{name} 
%{_mandir}/man5/%{name}.conf*

%changelog

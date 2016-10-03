%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
Name:           puppet-gnocchi
Version:        9.4.0
Release:        1%{?dist}
Summary:        Puppet module for OpenStack Gnocchi
License:        Apache-2.0

URL:            https://launchpad.net/puppet-gnocchi

Source0:        https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz

BuildArch:      noarch

Requires:       puppet-inifile
Requires:       puppet-keystone
Requires:       puppet-stdlib
Requires:       puppet-openstacklib
Requires:       puppet >= 2.7.0

%description
Puppet module for OpenStack Gnocchi

%prep
%setup -q -n openstack-gnocchi-%{upstream_version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/gnocchi/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/gnocchi/



%files
%{_datadir}/openstack-puppet/modules/gnocchi/


%changelog
* Thu Sep 29 2016 Alfredo Moralejo <amoralej@redhat.com> 9.4.0-1
- Update to 9.4.0

* Wed Sep 21 2016 Haikel Guemar <hguemar@fedoraproject.org> 9.3.0-1
- Update to 9.3.0

* Fri Sep 16 2016 Haikel Guemar <hguemar@fedoraproject.org> 9.2.0-1
- Update to 9.2.0


# REMOVEME: error caused by commit http://git.openstack.org/cgit/openstack/puppet-gnocchi/commit/?id=c0db11fc6665c39fe8de7f94aa332574b8bc0f70

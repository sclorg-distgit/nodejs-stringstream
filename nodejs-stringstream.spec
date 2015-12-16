%{?scl:%scl_package nodejs-stringstream}
%{!?scl:%global pkg_name %{name}}
%global npm_name stringstream

%{?nodejs_find_provides_and_requires}

Name:		%{?scl_prefix}nodejs-stringstream
Version:	0.0.4
Release:	1.sc1%{?dist}
Summary:	Encode and decode streams into string streams
Url:		http://registry.npmjs.org/stringstream/-/stringstream-0.0.4.tgz
Source0:	https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
License:	MIT

BuildArch:	noarch
ExclusiveArch:	%{nodejs_arches} noarch

BuildRequires:	%{?scl_prefix}nodejs-devel

%description
Encode and decode streams into string streams

%prep
%setup -q -n package

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}

cp -pr package.json stringstream.js \
	%{buildroot}%{nodejs_sitelib}/%{npm_name}

%{nodejs_symlink_deps}

%files
%{nodejs_sitelib}/stringstream

%doc README.md LICENSE.txt

%changelog
* Thu Jul 16 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.0.4-1
- Initial build

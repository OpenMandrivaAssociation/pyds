%define name	pyds
%define version 0.7.3
%define release %mkrel 4

Name: 	 	%{name}
Summary: 	Python Desktop Server
Version: 	%{version}
Release: 	%{release}

Source:		PyDS-%{version}.tar.bz2
URL:		http://pyds.muensterland.org/
License:	BSD
Group:		System/Servers
BuildRequires:	python-devel
Requires:	python-medusa
Requires:	python-cheetah
Requires:	python-pyrex
Requires:	python-docutils
Requires:	python-imaging
Requires:	metakit-python
Requires:	PyXML
Requires:	python-soap >= 0.11.1
Requires:	libjpeg62
Requires:	zlib1
Provides:	PyDS
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
The Python Desktop Server is a combined Weblog authoring tool, XMLRPC/SOAP
server, and news aggregator. It allows one to read RSS news feeds, post to a
community server (such as Radio Userland or any Python Community Server
installation), and includes tools for Weblog and homepage management. It
features a Web interface, a built-in Web server, extensibility through scripts
that connect via XMLRPC or macros, and a plugin architecture.

To setup your portal, run pyds-start, then browse http://localhost:4334.

%prep
%setup -q -n PyDS-%version

%install
rm -rf %{buildroot}
python setup.py install --prefix=%{buildroot}/usr

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog LICENSE OVERVIEW README 
%_bindir/pyds-*
/usr/lib/python2*/site-packages/PyDS
/usr/lib/python2*/site-packages/*.egg-info
%_datadir/%name



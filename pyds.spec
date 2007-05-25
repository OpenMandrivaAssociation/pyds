%define name	pyds
%define version 0.7.3
%define release %mkrel 3

Name: 	 	%{name}
Summary: 	Python Desktop Server
Version: 	%{version}
Release: 	%{release}

Source:		PyDS-%{version}.tar.bz2
URL:		http://pyds.muensterland.org/
License:	BSD
Group:		System/Servers
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	python-devel
Requires:	python-medusa python-cheetah metakit-python
Requires:	PyXML python-pyrex python-docutils python-imaging
Requires:	python-soap >= 0.11.1
Requires:	libjpeg62 zlib1
Provides:	PyDS

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
rm -rf $RPM_BUILD_ROOT
python setup.py install --prefix=$RPM_BUILD_ROOT/usr

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ChangeLog LICENSE OVERVIEW README 
%_bindir/pyds-*
/usr/lib/python2*/site-packages/PyDS
/usr/lib/python2*/site-packages/*.egg-info
%_datadir/%name



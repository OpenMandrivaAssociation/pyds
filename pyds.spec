Name: 	 	pyds
Summary: 	Python Desktop Server
Version: 	0.7.3
Release: 	12

Source0:	PyDS-%{version}.tar.bz2
URL:		https://pyds.muensterland.org/
License:	BSD
Group:		System/Servers
BuildRequires:	pkgconfig(python2)
Requires:	python-medusa
Requires:	python-cheetah
Requires:	python-pyrex
Requires:	python-docutils
Requires:	python-imaging
Requires:	metakit-python
Requires:	python-soap >= 0.11.1
Requires:	zlib
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
python2 setup.py install --prefix=%{buildroot}/usr

%files
%doc ChangeLog LICENSE OVERVIEW README 
%_bindir/pyds-*
/usr/lib/python2*/site-packages/PyDS
/usr/lib/python2*/site-packages/*.egg-info
%_datadir/%name

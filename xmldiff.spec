#
# TODO:
# - split to xmldiff and python-xmldiff?
#
Summary:	XML difference tool
Summary(pl):	Narzêdzie do porównywania plików XML
Name:		xmldiff
Version:	0.6.6
Release:	1
License:	GPL v2
Group:		Applications/Publishing/XML
Source0:	ftp://ftp.logilab.org/pub/xmldiff/%{name}-%{version}.tar.gz
# Source0-md5:	d640c12e9a9467873b7caaf1379d3fe8
URL:		http://www.logilab.org/projects/xmldiff/view
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
Requires:	python-logilab-common >= 0.5.0-2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XMLdiff is a python tool that figures out the differences between two
similar XML files, in the same way the diff utility does it for text
files. It can be used as a library or as a command line tool. It can
work either with XML files or DOM trees.

%description -l pl
XMLdiff jest narzêdziem Pythona znajduj±cym ró¿nice miêdzy dwoma
plikami XML, w taki sam sposób w jaki diff robi to dla plików
tekstowych. Mo¿e byæ u¿ywane jako biblioteka lub z linii poleceñ.
XMLdiff mo¿e pracowaæ na plikach XML lub drzewach DOM.

%prep
%setup -q

%build
CFLAGS="%{rpmcflags}"
export CFLAGS
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{py_sitedir}}

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2
install man/*.1 $RPM_BUILD_ROOT%{_mandir}/man1
find $RPM_BUILD_ROOT%{py_sitedir} -name \*.py -exec rm -f {} \;

# see install section of python-logilab-common for explanation
rm -f $RPM_BUILD_ROOT%{py_sitedir}/logilab/__init__.*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* TODO xsl doc/*.html
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{py_sitedir}/logilab/xmldiff

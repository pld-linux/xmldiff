#
# TODO:
# - split to xmldiff and python-xmldiff?
#
Summary:	XML difference tool
Summary(pl):	Narzêdzie do porównywania plików XML
Name:		xmldiff
Version:	0.6.4
Release:	1
License:	GPL
Group:		Applications/Publishing/XML
Source0:	ftp://ftp.logilab.org/pub/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	3f50b71ea237d5b1d518a00b0e716c08
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
tekstowych. Mo¿e byæ uzywane jako biblioteka lub z linii poleceñ.
XMLdiff mo¿e pracowaæ na plikach XML lub drzewach DOM.

%prep
%setup -q -n %{name}-%{version}

%build
CFLAGS="%{rpmcflags}"
export CFLAGS
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{py_sitedir}}

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

find $RPM_BUILD_ROOT%{py_sitedir} -name \*.py -exec rm -f {} \;

# see install section of python-logilab-common for explanation
rm -f $RPM_BUILD_ROOT%{py_sitedir}/logilab/__init__.*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* xsl doc/*.html
%attr(755,root,root) %{_bindir}/*
%{py_sitedir}/logilab/xmldiff

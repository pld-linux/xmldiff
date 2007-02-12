#
# TODO:
# - split to xmldiff and python-xmldiff?
#
Summary:	XML difference tool
Summary(pl.UTF-8):	Narzędzie do porównywania plików XML
Name:		xmldiff
Version:	0.6.7
Release:	1
License:	GPL v2
Group:		Applications/Publishing/XML
Source0:	ftp://ftp.logilab.org/pub/xmldiff/%{name}-%{version}.tar.gz
# Source0-md5:	07b97c97a0b83d605f37c712400e24ff
URL:		http://www.logilab.org/projects/xmldiff/view
BuildRequires:	python-devel
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XMLdiff is a python tool that figures out the differences between two
similar XML files, in the same way the diff utility does it for text
files. It can be used as a library or as a command line tool. It can
work either with XML files or DOM trees.

%description -l pl.UTF-8
XMLdiff jest narzędziem Pythona znajdującym różnice między dwoma
plikami XML, w taki sam sposób w jaki diff robi to dla plików
tekstowych. Może być używane jako biblioteka lub z linii poleceń.
XMLdiff może pracować na plikach XML lub drzewach DOM.

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

rm -r $RPM_BUILD_ROOT%{py_sitedir}/%{name}/test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* TODO xsl doc/*.html
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{py_sitedir}/xmldiff

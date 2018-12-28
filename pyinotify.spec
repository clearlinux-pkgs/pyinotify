#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xA3FD8622E8440341 (seb@dbzteam.org)
#
Name     : pyinotify
Version  : 0.9.6
Release  : 14
URL      : http://pypi.debian.net/pyinotify/pyinotify-0.9.6.tar.gz
Source0  : http://pypi.debian.net/pyinotify/pyinotify-0.9.6.tar.gz
Source99 : http://pypi.debian.net/pyinotify/pyinotify-0.9.6.tar.gz.asc
Summary  : Linux filesystem events monitoring
Group    : Development/Tools
License  : MIT
Requires: pyinotify-python3
Requires: pyinotify-license
Requires: pyinotify-python
BuildRequires : buildreq-distutils3

%description
# Pyinotify
* License          : MIT
* Project URL      : [http://github.com/seb-m/pyinotify](http://github.com/seb-m/pyinotify)
* Project Wiki     : [http://github.com/seb-m/pyinotify/wiki](http://github.com/seb-m/pyinotify/wiki)
* API Documentation: [http://seb-m.github.com/pyinotify](http://seb-m.github.com/pyinotify)

%package license
Summary: license components for the pyinotify package.
Group: Default

%description license
license components for the pyinotify package.


%package python
Summary: python components for the pyinotify package.
Group: Default
Requires: pyinotify-python3

%description python
python components for the pyinotify package.


%package python3
Summary: python3 components for the pyinotify package.
Group: Default
Requires: python3-core

%description python3
python3 components for the pyinotify package.


%prep
%setup -q -n pyinotify-0.9.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1533931647
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/pyinotify
cp COPYING %{buildroot}/usr/share/doc/pyinotify/COPYING
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(-,root,root,-)
/usr/share/doc/pyinotify/COPYING

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

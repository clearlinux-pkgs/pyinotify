#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xA3FD8622E8440341 (seb@dbzteam.org)
#
Name     : pyinotify
Version  : 0.9.6
Release  : 9
URL      : https://pypi.python.org/packages/source/p/pyinotify/pyinotify-0.9.6.tar.gz
Source0  : https://pypi.python.org/packages/source/p/pyinotify/pyinotify-0.9.6.tar.gz
Source99 : https://pypi.python.org/packages/source/p/pyinotify/pyinotify-0.9.6.tar.gz.asc
Summary  : Linux filesystem events monitoring
Group    : Development/Tools
License  : MIT
Requires: pyinotify-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
# Pyinotify
* License          : MIT
* Project URL      : [http://github.com/seb-m/pyinotify](http://github.com/seb-m/pyinotify)
* Project Wiki     : [http://github.com/seb-m/pyinotify/wiki](http://github.com/seb-m/pyinotify/wiki)
* API Documentation: [http://seb-m.github.com/pyinotify](http://seb-m.github.com/pyinotify)

%package python
Summary: python components for the pyinotify package.
Group: Default

%description python
python components for the pyinotify package.


%prep
%setup -q -n pyinotify-0.9.6

%build
export LANG=C
export SOURCE_DATE_EPOCH=1484564479
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1484564479
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*

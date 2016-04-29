#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pyinotify
Version  : 0.9.6
Release  : 3
URL      : https://pypi.python.org/packages/source/p/pyinotify/pyinotify-0.9.6.tar.gz
Source0  : https://pypi.python.org/packages/source/p/pyinotify/pyinotify-0.9.6.tar.gz
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
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*

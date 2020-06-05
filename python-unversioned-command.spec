Name:           python-unversioned-command
Version:        0
Release:        1%{?dist}
Summary:        The "python" command that runs Python 3

License:        GPL
URL:            https://bugzilla.redhat.com/show_bug.cgi?id=1585626

BuildArch: 	noarch

Requires:	python3
Provides:	python

%description
This package contains /usr/bin/python - the "python" command that runs Python 3.

https://bugzilla.redhat.com/show_bug.cgi?id=1585626

%install
rm -rf $RPM_BUILD_ROOT
install -d %{buildroot}%{_bindir}
ln -s ./python3 %{buildroot}%{_bindir}/python

%files
%{_bindir}/python

%changelog
* Thu Jun  4 2020 Mattias Ohlsson <mattias.ohlsson@inprose.com> - 0-1
- Initial build

Summary:	DevHelp book: Pango
Summary(pl.UTF-8):	Książka do DevHelpa o Pango
Name:		devhelp-book-pango
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Applications
#Source0:	http://www.devhelp.net/books/books/pango-1.0.tar.gz
Source0:	pango-1.0.tar.gz
# Source0-md5:	a0b8d34677a331c947b78c9d163d0bbf
URL:		http://www.devhelp.net/
Requires:	devhelp
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/share/devhelp

%description
DevHelp book about Pango.

%description -l pl.UTF-8
Książka do DevHelpa o Pango.

%prep
%setup -q -c -n pango-1.0

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/{books/pango-1.0,specs}

install book.devhelp $RPM_BUILD_ROOT%{_prefix}/specs/pango-1.0
install book/* $RPM_BUILD_ROOT%{_prefix}/books/pango-1.0

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_prefix}/books/*
%{_prefix}/specs/*

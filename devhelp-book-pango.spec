Summary:	DevHelp book: Pango
Summary(pl):	Ksi±¿ka do DevHelp'a o Pango
Name:		devhelp-book-pango
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.devhelp.net/books/books/pango-1.0.tar.gz
URL:		http://www.devhelp.net/
Requires:	devhelp
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6/share/devhelp/

%description
DevHelp book about Pango

%description -l pl
Ksi±¿ka do DevHelp o Pango

%prep
%setup -q -c pango-1.0 -n pango-1.0

%build
mv -f book pango-1.0
mv -f book.devhelp pango-1.0.devhelp

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_prefix}/books/pango-1.0 
install -d $RPM_BUILD_ROOT%{_prefix}/specs
install pango-1.0.devhelp $RPM_BUILD_ROOT%{_prefix}/specs
install pango-1.0/* $RPM_BUILD_ROOT%{_prefix}/books/pango-1.0

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
#%doc *.gz
%{_prefix}/books
%{_prefix}/specs

%define	ruby_ridir	%(ruby -r rbconfig -e 'include Config; print File.join(CONFIG["datadir"], "ri", CONFIG["ruby_version"], "system")')
%define ruby_rubylibdir %(ruby -r rbconfig -e 'print Config::CONFIG["rubylibdir"]')
%define	ruby_archdir	%(ruby -r rbconfig -e 'print Config::CONFIG["archdir"]')
Summary:	Ruby ODBC library
Summary(pl):	Biblioteka Ruby ODBC
Name:		ruby-odbc
Version:	0.996
Release:	1
License:	GPL
Group:		Development/Languages
Source0:	http://www.ch-werner.de/rubyodbc/%{name}-%{version}.tar.gz
# Source0-md5:	5084ae82120f17e6be4c0267d7c53bab
Source1:	setup.rb
URL:		http://www.ch-werner.de/rubyodbc/
BuildRequires:	ruby
BuildRequires:	ruby-devel
BuildRequires:	unixODBC-devel
Requires:	ruby
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ruby ODBC library.

%description -l pl
Biblioteka ODBC dla jêzyka Ruby.

%prep
%setup -q 

%build
ruby extconf.rb 
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -fPIC"

rdoc --ri -o ri
rdoc -o rdoc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_archdir}
install -d $RPM_BUILD_ROOT%{ruby_ridir}

%{__make} install \
	archdir=$RPM_BUILD_ROOT%{ruby_archdir} \
	sitearchdir=$RPM_BUILD_ROOT%{ruby_archdir}

cp -a ri/ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* rdoc
%{ruby_archdir}/odbc.*
%{ruby_ridir}/*

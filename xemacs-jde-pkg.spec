Summary:	Java language and development support
Summary(pl.UTF-8):	Wsparcie dla języka i programowania w Javie
Name:		xemacs-jde-pkg
%define 	srcname	jde
Version:	1.46
Release:	3
License:	GPL
Group:		Applications/Editors/Emacs
Source0:	http://ftp.xemacs.org/xemacs/packages/%{srcname}-%{version}-pkg.tar.gz
# Source0-md5:	60f5d299a53be811f6ef6006f2566c20
URL:		http://www.xemacs.org/
BuildArch:	noarch
Conflicts:	xemacs-sumo
Requires:	xemacs
Requires:	xemacs-cc-mode-pkg
Requires:	xemacs-debug-pkg
Requires:	xemacs-speedbar-pkg
Requires:	xemacs-edit-utils-pkg
Requires:	xemacs-eterm-pkg
Requires:	xemacs-mail-lib-pkg
Requires:	xemacs-base-pkg
Requires:	xemacs-eieio-pkg
Requires:	xemacs-semantic-pkg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Java Development Environment (JDE) is an Emacs Lisp package that
interfaces Emacs to third-party Java application development tools,
such as those provided by JavaSoft's Java Development Kit (JDK). The
result is an integrated development environment (IDE) comparable in
power to many commercial Java IDEs.

%description -l pl.UTF-8
JDE (Java Development Environment) to pakiet Emacsa dodający interfejs
do narzędzi programistycznych do Javy innych producentów, takich jak
JDK (Java Development Kit) JavaSoftu. Rezultatem jest zintegrowane
środowisko programisty porównywalne do wielu komercyjnych IDE.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xemacs-packages

cp -a * $RPM_BUILD_ROOT%{_datadir}/xemacs-packages

# remove .el file if corresponding .elc file exists
find $RPM_BUILD_ROOT -type f -name "*.el" | while read i; do test ! -f ${i}c || rm -f $i; done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc lisp/jde/ChangeLog
%{_datadir}/xemacs-packages%{_sysconfdir}/*
%dir %{_datadir}/xemacs-packages/lisp/*
%{_datadir}/xemacs-packages/lisp/*/*.el*
%{_datadir}/xemacs-packages/pkginfo/*

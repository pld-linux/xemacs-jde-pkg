Summary:	Java language and development support
Summary(pl):	Wsparcie dla j�zyka i programowania w Javie
Name:		xemacs-jde-pkg
%define 	srcname	jde
Version:	1.32
Release:	1
License:	GPL
Group:		Applications/Editors/Emacs
Group(cs):	Aplikace/Editory/Emacs
Group(da):	Programmer/Tekstbehandlere/Emacs
Group(de):	Applikationen/Editoren/Emacs
Group(es):	Aplicaciones/Editores/Emacs
Group(fr):	Applications/Editeurs/Emacs
Group(is):	Forrit/Ritlar/Emacs
Group(it):	Applicazioni/Editor/Emacs
Group(ja):	���ץꥱ�������/���ǥ���/Emacs
Group(no):	Applikasjoner/Editorer/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
Group(pt):	Aplica��es/Editores/Emacs
Group(ru):	����������/���������/Emacs
Group(sl):	Programi/Urejevalniki/Emacs
Group(sv):	Till�mpningar/Editorer/Emacs
Group(uk):	�������Φ ��������/���������/Emacs
Source0:	ftp://ftp.xemacs.org/xemacs/packages/%{srcname}-%{version}-pkg.tar.gz
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
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Java Development Environment (JDE) is an Emacs Lisp package that
interfaces Emacs to third-party Java application development tools,
such as those provided by JavaSoft's Java Development Kit (JDK). The
result is an integrated development environment (IDE) comparable in
power to many commercial Java IDEs.

%description -l pl
JDE (Java Development Environment) to pakiet Emacsa dodaj�cy interfejs
do narz�dzi programistycznych do Javy innych producent�w, takich jak
JDK (Java Development Kit) JavaSoftu. Rezultatem jest zintegroawane
�rodowisko programisty por�wnywalne do wielu komercyjnych IDE.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xemacs-packages

cp -a * $RPM_BUILD_ROOT%{_datadir}/xemacs-packages

gzip -9nf lisp/jde/ChangeLog 

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc lisp/jde/ChangeLog.gz 
%{_datadir}/xemacs-packages%{_sysconfdir}/*
%dir %{_datadir}/xemacs-packages/lisp/*
%{_datadir}/xemacs-packages/lisp/*/*.elc

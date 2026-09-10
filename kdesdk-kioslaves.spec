Summary:	KDE SDK KIO slaves
Name:		kdesdk-kio
Version:	26.08.1
Release:	1
Group:		Graphical desktop/KDE
License:	GPLv2+
Url:		https://www.kde.org
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/kdesdk-kio-%{version}.tar.xz
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	perl-devel
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6KIO)
Suggests:	kio-perldoc = %{EVRD}
%rename kdesdk-kioslaves
BuildSystem:	cmake
BuildOption:	-DKDE_USE_QT_SYS_PATHS:BOOL=ON

%description
KIO slaves for:
 - Perl documentation

%files

#----------------------------------------------------------------------------

%package -n kio-perldoc
Summary:	A KIO slave interface for Perl documentation
Group:		Graphical desktop/KDE
Requires:	perl(Pod::Perldoc)
Conflicts:	kdesdk4-core < 1:4.11.0
%rename kio4-perldoc

%description -n kio-perldoc
A KIO slave interface for Perl documentation.

%files -n kio-perldoc -f %{name}.lang
%{_qtdir}/plugins/kf6/kio/perldoc.so
%{_datadir}/kio_perldoc/pod2html.pl

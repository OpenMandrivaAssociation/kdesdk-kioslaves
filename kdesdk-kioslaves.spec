# We're keeping the original name until Plasma 6
# No need to mess with Provides: and Obsoletes:
# for a few months...

Summary:	KDE SDK KIO slaves
Name:		kdesdk-kioslaves
Version:	24.02.0
Release:	1
Epoch:		1
Group:		Graphical desktop/KDE
License:	GPLv2+
Url:		https://www.kde.org
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/kdesdk-kio-%{version}.tar.xz
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	perl-devel
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5KIO)
Suggests:	kio-perldoc = %{EVRD}

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

%files -n kio-perldoc -f kio5_perldoc.lang
%{_libdir}/qt5/plugins/kf5/kio/perldoc.so
%{_datadir}/kio_perldoc

#----------------------------------------------------------------------------

%prep
%autosetup -p1 -n kdesdk-kio-%{version}

%build
%cmake_kde5
%ninja

%install
%ninja_install -C build
%find_lang kio5_perldoc

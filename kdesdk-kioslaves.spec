Summary:	KDE SDK KIO slaves
Name:		kdesdk-kioslaves
Version:	4.11.4
Release:	1
Epoch:		1
Group:		Graphical desktop/KDE
License:	GPLv2+
Url:		http://www.kde.org
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Source0:	ftp://ftp.kde.org/pub/kde/%{ftpdir}/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs4-devel
BuildRequires:	subversion-devel
Suggests:	kio4-perldoc = %{EVRD}
Suggests:	kio4-svn = %{EVRD}

%description
KIO slaves for:
 - Perl documentation
 - SVN

%files

#----------------------------------------------------------------------------

%package -n kio4-perldoc
Summary:	A KIO slave interface for Perl documentation
Group:		Graphical desktop/KDE
Requires:	perl(Pod::Perldoc)
Conflicts:	kdesdk4-core < 1:4.11.0

%description -n kio4-perldoc
A KIO slave interface for Perl documentation.

%files -n kio4-perldoc
%{_kde_libdir}/kde4/kio_perldoc.so
%{_kde_appsdir}/kio_perldoc
%{_kde_services}/perldoc.protocol

#----------------------------------------------------------------------------

%package -n kio4-svn
Summary:	A KIO slave interface for SVN
Group:		Graphical desktop/KDE
Requires:	subversion
Conflicts:	kdesdk4-core < 1:4.11.0
Conflicts:	kdesdk4-devel < 1:4.11.0
Conflicts:	cervisia < 1:4.11.0

%description -n kio4-svn
A KIO slave interface for SVN.

%files -n kio4-svn
%{_kde_bindir}/kio_svn_helper
%{_kde_libdir}/kde4/kded_ksvnd.so
%{_kde_libdir}/kde4/kio_svn.so
%{_kde_iconsdir}/hicolor/*/actions/vcs-add-svn-kiosvn.*
%{_kde_iconsdir}/hicolor/*/actions/vcs-branch-svn-kiosvn.*
%{_kde_iconsdir}/hicolor/*/actions/vcs-merge-svn-kiosvn.*
%{_kde_iconsdir}/hicolor/*/actions/vcs-remove-svn-kiosvn.*
%{_kde_iconsdir}/hicolor/*/actions/vcs-status-svn-kiosvn.*
%{_kde_iconsdir}/hicolor/*/actions/vcs-switch-svn-kiosvn.*
%{_kde_services}/ServiceMenus/subversion.desktop
%{_kde_services}/ServiceMenus/subversion_toplevel.desktop
%{_kde_services}/kded/ksvnd.desktop
%{_kde_services}/svn+file.protocol
%{_kde_services}/svn+http.protocol
%{_kde_services}/svn+https.protocol
%{_kde_services}/svn+ssh.protocol
%{_kde_services}/svn.protocol
%{_datadir}/dbus-1/interfaces/org.kde.ksvnd.xml

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Wed Dec 04 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.4-1
- New version 4.11.4

* Wed Nov 06 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.3-1
- New version 4.11.3

* Wed Oct 02 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.2-1
- New version 4.11.2

* Tue Sep 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.1-1
- New version 4.11.1

* Wed Aug 14 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.0-1
- Split from kdesdk4 package as upstream did
- New version 4.11.0

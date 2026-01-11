%bcond clang 1

# TDE variables
%define tde_epoch 2
%if "%{?tde_version}" == ""
%define tde_version 14.1.5
%endif
%define pkg_rel 2

%define tde_pkg kbiff
%define tde_prefix /opt/trinity


%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1

# fixes error: Empty %files file …/debugsourcefiles.list
%define _debugsource_template %{nil}

%define tarball_name %{tde_pkg}-trinity


Name:			trinity-%{tde_pkg}
Epoch:			%{tde_epoch}
Version:        3.9
Release:		%{?tde_version}_%{?!preversion:%{pkg_rel}}%{?preversion:0_%{preversion}}%{?dist}
Summary:        TDE mail notification utility
Group:          Applications/Internet
URL:            http://www.trinitydesktop.org/

License:	GPLv2+


Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{tde_version}/main/applications/internet/%{tarball_name}-%{tde_version}%{?preversion:~%{preversion}}.tar.xz

BuildSystem:    cmake

BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DCMAKE_INSTALL_PREFIX=%{tde_prefix}
BuildOption:    -DSHARE_INSTALL_PREFIX=%{tde_prefix}/share
BuildOption:    -DWITH_ALL_OPTIONS=ON -DBUILD_ALL=ON
BuildOption:    -DBUILD_DOC=ON -DBUILD_TRANSLATIONS=ON
BuildOption:    -DWITH_GCC_VISIBILITY=%{!?with_clang:ON}%{?with_clang:OFF}

BuildRequires:	tqt3-compat-headers >= 3.5.0
BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}

BuildRequires:	desktop-file-utils
BuildRequires:	gettext

BuildRequires:	trinity-tde-cmake >= %{tde_version}

%{!?with_clang:BuildRequires:	gcc-c++}

BuildRequires:	pkgconfig

# ACL support
BuildRequires:  pkgconfig(libacl)

# IDN support
BuildRequires:	pkgconfig(libidn)

# OPENSSL support
BuildRequires:  pkgconfig(openssl)

BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(sm)


%description
Kbiff is a "xbiff"-like mail notification utility. It has  multiple pixmaps,
session management, and GUI configuration.  It can "dock" into the TDE panel.
It can display animated gifs, play system sounds, or run arbitrary shell
command when new mail arrives. It supports mbox, maildir, mh, POP3, IMAP4, and
NNTP mailboxes.


%conf -p
unset QTDIR QTINC QTLIB
export PATH="%{tde_prefix}/bin:${PATH}"
export PKG_CONFIG_PATH="%{tde_prefix}/%{_lib}/pkgconfig"


%install -a
%find_lang %{tde_pkg}


%files -f %{tde_pkg}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING README.md ChangeLog
%{tde_prefix}/bin/kbiff
%{tde_prefix}/%{_lib}/libtdeinit_kbiff.la
%{tde_prefix}/%{_lib}/libtdeinit_kbiff.so
%{tde_prefix}/%{_lib}/trinity/kbiff.la
%{tde_prefix}/%{_lib}/trinity/kbiff.so
%{tde_prefix}/share/applications/tde/kbiff.desktop
%{tde_prefix}/share/apps/kbiff/
%{tde_prefix}/share/icons/hicolor/*/apps/kbiff.png
%{tde_prefix}/share/icons/locolor/*/apps/kbiff.png
%{tde_prefix}/share/man/man1/kbiff.1*
%lang(de) %{tde_prefix}/share/doc/tde/HTML/de/kbiff/
%lang(en) %{tde_prefix}/share/doc/tde/HTML/en/kbiff/
%lang(es) %{tde_prefix}/share/doc/tde/HTML/es/kbiff/
%lang(fr) %{tde_prefix}/share/doc/tde/HTML/fr/kbiff/


Summary: autoconf-252 - Generate configuration scripts
%define AppProgram autoconf
%define AppVersion 2.52
%define AppRelease 20250126
%define AppSuffix  -252
# $Id: ac252.spec,v 1.52 2025/01/26 15:44:22 tom Exp $
Name: ac252
Version: %{AppVersion}
Release: %{AppRelease}
License: GPLv2
Group: Applications/Development
URL: http://invisible-island.net/%{AppProgram}
Source0: http://invisible-island.net/archives/%{AppProgram}/%{AppProgram}-%{AppVersion}-%{AppRelease}.tgz

BuildArch:	noarch
#BuildRequires:	m4
Requires:	m4

%description
This is a stable version of autoconf, used by all of my applications.
See http://invisible-island.net/autoconf/

%define MyName %{AppProgram}%{AppSuffix}

%define find_tool tool=install-info; for dir in /sbin /usr/sbin; do if test -f $dir/$tool; then tool=$dir/$tool;break;fi;done

%prep

%setup -q -n %{AppProgram}-%{AppVersion}-%{AppRelease}

%build

INSTALL_PROGRAM='${INSTALL}' \
	./configure \
		--program-suffix=%{AppSuffix} \
		--target %{_target_platform} \
		--prefix=%{_prefix} \
		--bindir=%{_bindir} \
		--libdir=%{_libdir} \
		--mandir=%{_mandir} \
		--datadir=%{_datadir}/%{MyName} \
		--infodir=%{_infodir}

make

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_infodir}/dir
rm -f $RPM_BUILD_ROOT%{_infodir}/standards*

%post
%{find_tool}
$tool \
	%{_infodir}/%{MyName}.info \
	%{_infodir}/dir || :

%preun
if [ $1 = 0 ] ; then
  %{find_tool}
  $tool \
	--delete \
	%{_infodir}/%{MyName}.info \
	%{_infodir}/dir || :
fi

%files
%defattr(-,root,root)
%{_bindir}/*%{AppSuffix}
%{_mandir}/man1/*%{AppSuffix}*
%{_datadir}/%{MyName}*
%{_infodir}/*%{AppSuffix}*

%changelog
# each patch should add its ChangeLog entries here

* Sun Sep 03 2023 Thomas E. Dickey
- update http-url, rpmlint'd

* Sun Aug 19 2018 Thomas E. Dickey
- update ftp-url

* Fri Oct 01 2010 Thomas E. Dickey
- adapt rules for installing info file from
  http://fedoraproject.org/wiki/Packaging/ScriptletSnippets

* Tue Sep 28 2010 Thomas E. Dickey
- initial version

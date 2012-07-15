%define nam             scim-hangul
%define ver             0.3.2
%define rel             1
%define build_setup     1

# Something's not quite right with libtool....
%define __libtoolize    echo

Summary:        Hangul Input Method Engine for SCIM
Name:           %{nam}
Version:        %{ver}
Release:        %{rel}
License:        GPL
Group:          System Environment/Libraries
URL:            http://www.freedesktop.org/~suzhe
BuildRoot:      %{_tmppath}/%{name}-%{version}-root

Source0:        %{name}-%{version}.tar.gz
#NoSource:	0

PreReq:         /sbin/ldconfig, /bin/sh

Requires:	scim >= 0.99.8
BuildRequires:  scim-devel >= 0.99.8

%description
SCIM is a developing platform to significant reduce the difficulty of 
input method development. 

%changelog
* Sun Jun 13 2004 James Su <suzhe@tsinghua.org.cn>
- first release of scim-uim.

#--------------------------------------------------

%prep

%setup -n %{name}-%{version}

%build
%configure --disable-static

make 

%install
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT
make DESTDIR=${RPM_BUILD_ROOT} install

rm -f $RPM_BUILD_ROOT//home/krisna/lib/scim-1.0/1.4.0/IMEngine/hangul.{a,la}
rm -f $RPM_BUILD_ROOT//home/krisna/lib/scim-1.0/1.4.0/SetupUI/hangul-imengine-setup.{a,la}

%clean
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc AUTHORS COPYING NEWS README ChangeLog
/home/krisna/lib/scim-1.0/1.4.0/IMEngine/hangul.so
%if %{build_setup}
/home/krisna/lib/scim-1.0/1.4.0/SetupUI/hangul-imengine-setup.so
%endif
%{_datadir}/locale/*/LC_MESSAGES/scim-hangul.mo
/home/krisna/share/scim/icons/scim-hangul.png

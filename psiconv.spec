Summary:	Psion 5 data format library
Summary(pl):	Biblioteka obs³ugi plików Psion 5
Name:		psiconv
Version:	0.9.5
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://huizen.dds.nl/~frodol/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	cf55fcf88ad07a42a636ded658b7b063
URL:		http://huizen.dds.nl/~frodol/psiconv/
BuildRequires:	ImageMagick-devel
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package is meant to make the Psion 5 series of PDAs, as well as
other small computers running Epoc 32, more usable to non-Windows
users. The package consists of several parts:
 - Documentation about Psion 5 data formats;
 - A library which can be linked against application that have to read
   (and in the future, perhaps write) Psion 5 files;
 - An example command-line program which reads Psion files and writes
   more commonly used formats.

%description -l pl
Ten pakiet ma za zadanie uczyniæ PDA serii Psion 5 oraz inne ma³e
komputery na Epoc 32 bardziej u¿ytecznymi dla u¿ytkowników systemów
innych ni¿ Windows. Pakiet zawiera:
 - dokumentacjê o formatach danych Psion 5,
 - bibliotekê dla aplikacji, która mo¿e czytaæ (w przysz³o¶ci byæ mo¿e
   tak¿e zapisywaæ) pliki Psion 5,
 - przyk³adowy program czytaj±cy pliki Psion 5 i zapisuj±cy w czê¶ciej
   spotykanych formatach.

%package devel
Summary:	Development part of psiconv
Summary(pl):	Czê¶æ psiconv przeznaczona dla programistów
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for psiconv and Psion 5 file format documentation.

%description devel -l pl
Pliki nag³ówkowe psiconv oraz dokumentacja formatu plików Psion 5.

%package static
Summary:	Static psiconv library
Summary(pl):	Statyczna biblioteka psiconv
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static psiconv library.

%description static -l pl
Statyczna biblioteka psiconv.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub .
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf formats/xhtml/.temp

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/libpsiconv.so.*.*
%dir %{_sysconfdir}/%{name}
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/%{name}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/psion
%{_mandir}/man1/*.1*

%files devel
%defattr(644,root,root,755)
%doc formats/xhtml/*
%attr(755,root,root) %{_libdir}/libpsiconv.so
%{_libdir}/libpsiconv.la
%{_includedir}/psiconv

%files static
%defattr(644,root,root,755)
%{_libdir}/libpsiconv.a

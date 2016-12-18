Summary:	Psion 5 data format library
Summary(pl.UTF-8):	Biblioteka obsługi plików Psion 5
Name:		psiconv
Version:	0.9.8
Release:	3
License:	GPL
Group:		Libraries
Source0:	http://software.frodo.looijaard.name/psiconv/files/%{name}-%{version}.tar.gz
# Source0-md5:	8d7548e3c6b9cd408544736133728acd
URL:		http://software.frodo.looijaard.name/psiconv/
BuildRequires:	ImageMagick-devel
BuildRequires:	automake
BuildRequires:	bc
BuildRequires:	gcc-c++
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

%description -l pl.UTF-8
Ten pakiet ma za zadanie uczynić PDA serii Psion 5 oraz inne małe
komputery na Epoc 32 bardziej użytecznymi dla użytkowników systemów
innych niż Windows. Pakiet zawiera:
- dokumentację o formatach danych Psion 5,
- bibliotekę dla aplikacji, która może czytać (w przyszłości być może
  także zapisywać) pliki Psion 5,
- przykładowy program czytający pliki Psion 5 i zapisujący w częściej
  spotykanych formatach.

%package devel
Summary:	Development part of psiconv
Summary(pl.UTF-8):	Część psiconv przeznaczona dla programistów
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for psiconv and Psion 5 file format documentation.

%description devel -l pl.UTF-8
Pliki nagłówkowe psiconv oraz dokumentacja formatu plików Psion 5.

%package static
Summary:	Static psiconv library
Summary(pl.UTF-8):	Statyczna biblioteka psiconv
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static psiconv library.

%description static -l pl.UTF-8
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

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_bindir}/psiconv
%attr(755,root,root) %{_libdir}/libpsiconv.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpsiconv.so.?
%dir %{_sysconfdir}/%{name}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/psion
%{_datadir}/%{name}/xhtml
%{_mandir}/man1/psiconv.1*

%files devel
%defattr(644,root,root,755)
%doc formats/xhtml/*
%attr(755,root,root) %{_bindir}/psiconv-config
%attr(755,root,root) %{_libdir}/libpsiconv.so
%{_libdir}/libpsiconv.la
%{_includedir}/psiconv
%{_mandir}/man1/psiconv-config.1*

%files static
%defattr(644,root,root,755)
%{_libdir}/libpsiconv.a

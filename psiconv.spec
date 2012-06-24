Summary:	Psion 5 data format library
Summary(pl):	Biblioteka obs�ugi plik�w Psion 5
Name:		psiconv
Version:	0.8.3
Release:	2
License:	GPL
Group:		Libraries
Source0:	http://huizen.dds.nl/~frodol/psiconv/%{name}-%{version}.tar.gz
# Source0-md5:	7fe2b6d926aa7fb3b2ef77aada4adaf9
URL:		http://huizen.dds.nl/~frodol/psiconv/
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
Ten pakiet ma za zadanie uczyni� PDA serii Psion 5 oraz inne ma�e
komputery na Epoc 32 bardziej u�ytecznymi dla u�ytkownik�w system�w
innych ni� Windows. Pakiet zawiera:
 - dokumentacj� o formatach danych Psion 5,
 - bibliotek� dla aplikacji, kt�ra mo�e czyta� (w przysz�o�ci by� mo�e
   tak�e zapisywa�) pliki Psion 5,
 - przyk�adowy program czytaj�cy pliki Psion 5 i zapisuj�cy w cz�ciej
   spotykanych formatach.

%package devel
Summary:	Development part of psiconv
Summary(pl):	Cz�� psiconv przeznaczona dla programist�w
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files for psiconv and Psion 5 file format documentation.

%description devel -l pl
Pliki nag��wkowe psiconv oraz dokumentacja formatu plik�w Psion 5.

%package static
Summary:	Static psiconv library
Summary(pl):	Statyczna biblioteka psiconv
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static psiconv library.

%description static -l pl
Statyczna biblioteka psiconv.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

rm -rf formats/html/.temp

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/libpsiconv.so.*.*

%files devel
%defattr(644,root,root,755)
%doc formats/html/*
%attr(755,root,root) %{_libdir}/libpsiconv.so
%{_libdir}/libpsiconv.la
%{_includedir}/psiconv

%files static
%defattr(644,root,root,755)
%{_libdir}/libpsiconv.a

Summary:	Psion 5 data format library
Summary(pl):	Biblioteka obs≥ugi plikÛw Psion 5
Name:		psiconv
Version:	0.8.2
Release:	1
License:	GPL
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	‚…¬Ã…œ‘≈À…
Group(uk):	‚¶¬Ã¶œ‘≈À…
Source0:	http://huizen.dds.nl/~frodol/psiconv/%{name}-%{version}.tar.gz
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
Ten pakiet ma za zadanie uczyniÊ PDA serii Psion 5 oraz inne ma≥e
komputery na Epoc 32 bardziej uøytecznymi dla uøytkownikÛw systemÛw
innych niø Windows. Pakiet zawiera:
 - dokumentacjÍ o formatach danych Psion 5,
 - bibliotekÍ dla aplikacji, ktÛra moøe czytaÊ (w przysz≥o∂ci byÊ moøe
   takøe zapisywaÊ) pliki Psion 5,
 - przyk≥adowy program czytaj±cy pliki Psion 5 i zapisuj±cy w czÍ∂ciej
   spotykanych formatach.

%package devel
Summary:	Development part of psiconv
Summary(pl):	CzÍ∂Ê psiconv przeznaczona dla programistÛw
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name} = %{version}

%description devel
Header files for psiconv and Psion 5 file format documentation.

%description devel -l pl
Pliki nag≥Ûwkowe psiconv oraz dokumentacja formatu plikÛw Psion 5.

%package static
Summary:	Static psiconv library
Summary(pl):	Statyczna biblioteka psiconv
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
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

gzip -9nf AUTHORS NEWS README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/libpsiconv.so.*.*

%files devel
%defattr(644,root,root,755)
%doc formats/html/*
%attr(755,root,root) %{_libdir}/libpsiconv.so
%attr(755,root,root) %{_libdir}/libpsiconv.la
%{_includedir}/psiconv

%files static
%defattr(644,root,root,755)
%{_libdir}/libpsiconv.a

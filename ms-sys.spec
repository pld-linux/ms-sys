Summary:	Create DOS/MS-compatible boot records
Summary(pl.UTF-8):	Narzędzie tworzące rekordy rozruchowe kompatybilne z DOS-em i MS
Name:		ms-sys
Version:	2.6.0
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	http://downloads.sourceforge.net/ms-sys/%{name}-%{version}.tar.gz
# Source0-md5:	1bfd8f431268d8ae0cf1fa2f79efdc27
URL:		http://ms-sys.sourceforge.net/
BuildRequires:	bash
BuildRequires:	gettext-tools
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program is used to create DOS/MS-compatible boot records. It is
able to do the same as Microsoft "fdisk /mbr" to a hard disk. It is
also able to do the same as DOS "sys" to a floppy or FAT32 partition
except that it does not copy any system files, only the boot record is
written.

%description -l pl.UTF-8
Ten program służy do tworzenia rekordów rozruchowych (bootrekordów)
kompatybilnych z DOS-em i MS. Jest w stanie zrobić to samo co
microsoftowy "fdisk /mbr" na twardym dysku, a także to, co DOS-owy
"sys" na dyskietce lub partycji FAT32 - z dokładnością do tego, że nie
kopiuje żadnych plików systemowych, jedynie zapisuje rekord
rozruchowy.

%prep
%setup -q

%build
CC="%{__cc}" \
CFLAGS="%{rpmcflags}" \
%{__make} \
	SHELL=/bin/bash \
	PREFIX=%{_prefix} \
	EXTRA_LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix} \
	MANDIR=%{_mandir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc CHANGELOG CONTRIBUTORS FAQ README TODO
%attr(755,root,root) %{_bindir}/ms-sys
%{_mandir}/man1/ms-sys.1*
%lang(de) %{_mandir}/de/man1/ms-sys.1*
%lang(fr) %{_mandir}/fr/man1/ms-sys.1*
%lang(sv) %{_mandir}/sv/man1/ms-sys.1*

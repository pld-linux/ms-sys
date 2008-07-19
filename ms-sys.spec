Summary:	Create DOS/MS-compatible boot records
Summary(pl.UTF-8):	Narzędzie tworzące boot recordy kompatybilne z DOS-em i MS
Name:		ms-sys
Version:	2.1.3
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/ms-sys/%{name}-%{version}.tgz
# Source0-md5:	6fad0a69ac89440ad4f696dbbbf11497
URL:		http://ms-sys.sourceforge.net/
BuildRequires:	bash
BuildRequires:	gettext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program is used to create DOS/MS-compatible boot records. It is
able to do the same as Microsoft "fdisk /mbr" to a hard disk. It is
also able to do the same as DOS "sys" to a floppy or FAT32 partition
except that it does not copy any system files, only the boot record is
written.

%description -l pl.UTF-8
Ten program służy do tworzenia boot recordów kompatybilnych z DOS-em i
MS. Jest w stanie zrobić to samo co microsoftowy "fdisk /mbr" na
twardym dysku, a także to, co DOS-owy "sys" na dyskietce lub partycji
FAT32 - z dokładnością do tego, że nie kopiuje żadnych plików
systemowych, jedynie zapisuje boot record.

%prep
%setup -q

%build
# "debug" is only a hack - it allows passing EXTRA_CFLAGS
%{__make} debug \
	SHELL=/bin/bash \
	PREFIX=%{_prefix} \
	CC="%{__cc}" \
	EXTRA_CFLAGS="%{rpmcflags} -fasm" \
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
%doc CHANGELOG CONTRIBUTORS README TODO
%attr(755,root,root) %{_bindir}/ms-sys
%{_mandir}/man1/ms-sys.1*

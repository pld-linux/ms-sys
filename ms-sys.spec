Summary:	Create DOS/MS-compatible boot records
Summary(pl):	Narzêdzie tworz±ce boot recordy kompatybilne z DOS-em i MS
Name:		ms-sys
Version:	1.0.1
Release:	1
License:	GPL
Group:		Applications/System
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/ms-sys/%{name}-%{version}.tgz
URL:		http://ms-sys.sourceforge.net/
BuildRequires:	bash
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program is used to create DOS/MS-compatible boot records. It is
able to do the same as Microsoft "fdisk /mbr" to a hard disk. It is
also able to do the same as DOS "sys" to a floppy or FAT32 partition
except that it does not copy any system files, only the boot record is
written.

%description -l pl
Ten program s³u¿y do tworzenia boot recordów kompatybilnych z DOS-em i
MS. Jest w stanie zrobiæ to samo co microsoftowy "fdisk /mbr" na
twardym dysku, a tak¿e to, co DOS-owy "sys" na dyskietce lub partycji
FAT32 - z dok³adno¶ci± do tego, ¿e nie kopiuje ¿adnych plików
systemowych, jedynie zapisuje boot record.

%prep
%setup -q -n %{name}

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
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix}

mv -f $RPM_BUILD_ROOT%{_datadir}/locale/{sv_SE,sv}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README TODO
%attr(755,root,root) %{_bindir}/*

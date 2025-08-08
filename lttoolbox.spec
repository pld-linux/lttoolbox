Summary:	Augmented letter transducer tools for natural language processing
Summary(pl.UTF-8):	Narzędzia do przetwarzania słów w językach naturalnych
Name:		lttoolbox
Version:	3.8.0
Release:	1
License:	GPL v2+
Group:		Applications/Text
Source0:	https://github.com/apertium/lttoolbox/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	3a5ac66a6a3b93ee414273c5ff9d8e2d
Patch0:		libxml2.patch
URL:		http://wiki.apertium.org/wiki/Lttoolbox
BuildRequires:	cmake
# -std=c++14
BuildRequires:	libstdc++-devel >= 6:5.0
BuildRequires:	libxml2-devel >= 1:2.6.17
BuildRequires:	pkgconfig
Requires:	libxml2 >= 1:2.6.17
Obsoletes:	lttoolbox-static < 3.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
lttoolbox is a toolbox for lexical processing, morphological analysis
and generation of words. The analysis is the process of splitting a
word (e.g. cats) into its lemma 'cat' and the grammatical information
<n><pl>. The generation is the opposite process.

%description -l pl.UTF-8
lttoolbox to zestaw narzędzi do przetwarzania leksykalnego, analizy
morfologicznej i tworzenia słów. Analiza to proces podziału słowa (np.
"koty") na rdzeń "kot" i informację gramatyczną (rzeczownik liczby
mnogiej). Tworzenie słów to proces odwrotny.

%package devel
Summary:	Header files for lttoolbox library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki lttoolbox
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel >= 6:5.0
Requires:	libxml2-devel >= 1:2.6.17

%description devel
Header files for lttoolbox library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki lttoolbox.

%prep
%setup -q
%patch -P0 -p1

%build
mkdir -p build
cd build
%cmake ../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README.md
%attr(755,root,root) %{_bindir}/lsx-comp
%attr(755,root,root) %{_bindir}/lt-append
%attr(755,root,root) %{_bindir}/lt-apply-acx
%attr(755,root,root) %{_bindir}/lt-comp
%attr(755,root,root) %{_bindir}/lt-compose
%attr(755,root,root) %{_bindir}/lt-expand
%attr(755,root,root) %{_bindir}/lt-invert
%attr(755,root,root) %{_bindir}/lt-merge
%attr(755,root,root) %{_bindir}/lt-paradigm
%attr(755,root,root) %{_bindir}/lt-print
%attr(755,root,root) %{_bindir}/lt-proc
%attr(755,root,root) %{_bindir}/lt-restrict
%attr(755,root,root) %{_bindir}/lt-tmxcomp
%attr(755,root,root) %{_bindir}/lt-tmxproc
%attr(755,root,root) %{_bindir}/lt-trim
%attr(755,root,root) %{_libdir}/liblttoolbox.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liblttoolbox.so.3
%{_datadir}/lttoolbox
%{_mandir}/man1/lsx-comp.1
%{_mandir}/man1/lt-append.1*
%{_mandir}/man1/lt-comp.1*
%{_mandir}/man1/lt-compose.1*
%{_mandir}/man1/lt-expand.1*
%{_mandir}/man1/lt-merge.1*
%{_mandir}/man1/lt-paradigm.1*
%{_mandir}/man1/lt-print.1*
%{_mandir}/man1/lt-proc.1*
%{_mandir}/man1/lt-tmxcomp.1*
%{_mandir}/man1/lt-tmxproc.1*
%{_mandir}/man1/lt-trim.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblttoolbox.so
%{_includedir}/lttoolbox
%{_pkgconfigdir}/lttoolbox.pc

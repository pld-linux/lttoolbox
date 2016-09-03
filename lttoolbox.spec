Summary:	Augmented letter transducer tools for natural language processing
Summary(pl.UTF-8):	Narzędzia do przetwarzania słów w językach naturalnych
Name:		lttoolbox
Version:	3.3.3
Release:	1
License:	GPL v2+
Group:		Applications/Text
Source0:	http://downloads.sourceforge.net/apertium/%{name}-%{version}.tar.gz
# Source0-md5:	0bfac9f5ae0f8769a75b18c3fdff827f
URL:		http://wiki.apertium.org/wiki/Lttoolbox
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	libxml2-devel >= 1:2.6.17
BuildRequires:	pkgconfig
Requires:	libxml2 >= 1:2.6.17
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
Requires:	libstdc++-devel
Requires:	libxml2-devel >= 1:2.6.17

%description devel
Header files for lttoolbox library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki lttoolbox.

%package static
Summary:	Static lttoolbox library
Summary(pl.UTF-8):	Statyczna biblioteka lttoolbox
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static lttoolbox library.

%description static -l pl.UTF-8
Statyczna biblioteka lttoolbox.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/lt-comp
%attr(755,root,root) %{_bindir}/lt-expand
%attr(755,root,root) %{_bindir}/lt-print
%attr(755,root,root) %{_bindir}/lt-proc
%attr(755,root,root) %{_bindir}/lt-tmxcomp
%attr(755,root,root) %{_bindir}/lt-tmxproc
%attr(755,root,root) %{_bindir}/lt-trim
%attr(755,root,root) %{_libdir}/liblttoolbox3-3.3.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liblttoolbox3-3.3.so.0
%{_datadir}/lttoolbox
%{_mandir}/man1/lt-comp.1*
%{_mandir}/man1/lt-expand.1*
%{_mandir}/man1/lt-print.1*
%{_mandir}/man1/lt-proc.1*
%{_mandir}/man1/lt-tmxcomp.1*
%{_mandir}/man1/lt-tmxproc.1*
%{_mandir}/man1/lt-trim.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblttoolbox3.so
%{_libdir}/liblttoolbox3.la
%{_includedir}/lttoolbox-3.3
%{_pkgconfigdir}/lttoolbox.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/liblttoolbox3.a

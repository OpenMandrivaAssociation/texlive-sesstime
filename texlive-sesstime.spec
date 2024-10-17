Name:		texlive-sesstime
Version:	49750
Release:	2
Summary:	Session and timing information in lecture notes
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/sesstime
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sesstime.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sesstime.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sesstime.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This LaTeX2e package makes it possible to add timing marks to
lecture notes in order to help managing the time available for
presenting a given section of the document. It also provides
tools to record and estimate the progress throughout the
course.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/sesstime
%{_texmfdistdir}/tex/latex/sesstime
%doc %{_texmfdistdir}/doc/latex/sesstime

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post

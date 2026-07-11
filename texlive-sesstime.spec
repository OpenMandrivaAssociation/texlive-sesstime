%global tl_name sesstime
%global tl_revision 78482

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1.4
Release:	%{tl_revision}.1
Summary:	Session and timing information in lecture notes
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/sesstime
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/sesstime.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/sesstime.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/sesstime.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This LaTeX2e package makes it possible to add timing marks to lecture
notes in order to help managing the time available for presenting a
given section of the document. It also provides tools to record and
estimate the progress throughout the course.


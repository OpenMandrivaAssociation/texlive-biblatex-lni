%global tl_name biblatex-lni
%global tl_revision 73625

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.7
Release:	%{tl_revision}.1
Summary:	LNI style for BibLaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/biblatex-lni
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-lni.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-lni.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
BibLaTeX style for the Lecture Notes in Informatics, which is published
by the Gesellschaft fur Informatik (GI e.V.).


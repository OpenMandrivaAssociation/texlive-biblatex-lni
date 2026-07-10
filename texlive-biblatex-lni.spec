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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
BibLaTeX style for the Lecture Notes in Informatics, which is published
by the Gesellschaft fur Informatik (GI e.V.).

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/biblatex-lni
%dir %{_datadir}/texmf-dist/tex/latex/biblatex-lni
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-lni/CHANGELOG.md
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-lni/LICENSE
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-lni/LNI-examples.bib
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-lni/README.md
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-lni/basic-test-de.tex
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-lni/basic-test-en.tex
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-lni/mwe-de.tex
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-lni/mwe-en.tex
%{_datadir}/texmf-dist/tex/latex/biblatex-lni/LNI-english.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-lni/LNI-ngerman.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-lni/LNI.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-lni/LNI.cbx

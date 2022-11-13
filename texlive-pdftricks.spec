Name:		texlive-pdftricks
Version:	15878
Release:	1
Summary:	Support for pstricks in pdfTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pdftricks
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdftricks.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdftricks.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The PSTricks macros cannot be used (directly) with pdfTeX,
since pstricks uses PostScript arithmetic, which isn't part of
PDF. This package circumvents this limitation so that the
extensive facilities offered by the powerful PSTricks package
can be made use of in a pdfTeX document. This is done using the
shell escape function available in current TeX implementations.
The package may also be used in support of other 'PostScript-
output-only' packages, such as PSfrag. For alternatives, users
may care to review the discussion in the PSTricks online
documentation.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/pdftricks/pdftricks.sty
%doc %{_texmfdistdir}/doc/latex/pdftricks/makefile
%doc %{_texmfdistdir}/doc/latex/pdftricks/manual.pdf
%doc %{_texmfdistdir}/doc/latex/pdftricks/pst2pdf
%doc %{_texmfdistdir}/doc/latex/pdftricks/test.pdf
%doc %{_texmfdistdir}/doc/latex/pdftricks/test.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}

# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/pdftricks
# catalog-date 2008-11-24 12:47:54 +0100
# catalog-license gpl
# catalog-version 1.16
Name:		texlive-pdftricks
Version:	1.16
Release:	1
Summary:	Support for pstricks in pdfTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pdftricks
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdftricks.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdftricks.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

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

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/pdftricks/pdftricks.sty
%doc %{_texmfdistdir}/doc/latex/pdftricks/makefile
%doc %{_texmfdistdir}/doc/latex/pdftricks/manual.pdf
%doc %{_texmfdistdir}/doc/latex/pdftricks/pst2pdf
%doc %{_texmfdistdir}/doc/latex/pdftricks/test.pdf
%doc %{_texmfdistdir}/doc/latex/pdftricks/test.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}

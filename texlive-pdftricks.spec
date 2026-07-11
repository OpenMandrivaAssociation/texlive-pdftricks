%global tl_name pdftricks
%global tl_revision 15878

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.16
Release:	%{tl_revision}.1
Summary:	Support for PSTricks in pdfTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pdftricks
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pdftricks.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pdftricks.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The PSTricks macros cannot be used (directly) with pdfTeX, since
PSTricks uses PostScript arithmetic, which isn't part of PDF. This
package circumvents this limitation so that the extensive facilities
offered by the powerful PSTricks package can be made use of in a pdfTeX
document. This is done using the shell escape function available in
current TeX implementations. The package may also be used in support of
other 'PostScript-output-only' packages, such as PSfrag. For
alternatives, users may care to review the discussion in the PSTricks
online documentation.


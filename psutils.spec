Summary: PostScript Utilities
Name: psutils
Version: 1.17
Release: 44%{?dist}
License: psutils
Group: Applications/Publishing
# We cannot use the upstream tarball because it contains non-free files.
# To generate a clean tarball, run the psutils-remove-copyrighted-files script.
#Source: ftp://ftp.knackered.org/pub/psutils/psutils-p17.tar.gz
Source0: psutils-p17-clean.tar.gz
Source1: psutils-remove-copyrighted-files
Source2: psutils-copyright.patch
URL: http://knackered.org/angus/psutils/
Patch0: psutils-p17-Makefile.patch
Patch1: psutils-p17-misc.patch
Patch2: psutils-p17-paper.patch
Patch3: psutils-p17-strip.patch
Patch4: psutils-manpage.patch
Patch5: psutils-psmerge.patch
Patch6: psutils-datadir.patch

%description
This archive contains some utilities for manipulating PostScript documents.
Page selection and rearrangement are supported, including arrangement into
signatures for booklet printing, and page merging for n-up printing.

%package perl
Summary: psutils scripts requiring perl
Group: Applications/Publishing
BuildArch: noarch

%description perl
Various scripts from the psutils distribution that require perl.

%prep
%setup -q -n psutils
%patch0 -p1 -b .makefile
%patch1 -p1 -b .misc
%patch2 -p1 -b .paper
%patch3 -p1 -b .strip
%patch4 -p1 -b .manpage
%patch5 -p1 -b .new
%patch6 -p1 -b .datadir

%build
make -f Makefile.unix RPM_OPT_FLAGS="$RPM_OPT_FLAGS"
 
%install
make -f Makefile.unix \
        MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1 \
        DESTDIR=$RPM_BUILD_ROOT install

%files
%doc README LICENSE
%{_bindir}/epsffit
%{_bindir}/getafm
%{_bindir}/psbook
%{_bindir}/psnup
%{_bindir}/psresize
%{_bindir}/psselect
%{_bindir}/pstops
%{_bindir}/showchar
%{_mandir}/man1/epsffit.1*
%{_mandir}/man1/getafm.1*
%{_mandir}/man1/psbook.1*
%{_mandir}/man1/psnup.1*
%{_mandir}/man1/psresize.1*
%{_mandir}/man1/psselect.1*
%{_mandir}/man1/pstops.1*
#{_mandir}/man1/showchar.1*

%files perl
%doc LICENSE
%{_bindir}/extractres
%{_bindir}/fixdlsrps
%{_bindir}/fixfmps
#%%{_bindir}/fixmacps
%{_bindir}/fixpsditps
%{_bindir}/fixpspps
%{_bindir}/fixscribeps
%{_bindir}/fixtpps
%{_bindir}/fixwfwps
%{_bindir}/fixwpps
%{_bindir}/fixwwps
%{_bindir}/includeres
%{_bindir}/psmerge
#%%{_datadir}/psutils
%{_mandir}/man1/extractres.1*
%{_mandir}/man1/fixdlsrps.1*
%{_mandir}/man1/fixfmps.1*
#%%{_mandir}/man1/fixmacps.1*
%{_mandir}/man1/fixpsditps.1*
%{_mandir}/man1/fixpspps.1*
%{_mandir}/man1/fixscribeps.1*
%{_mandir}/man1/fixtpps.1*
%{_mandir}/man1/fixwfwps.1*
%{_mandir}/man1/fixwpps.1*
%{_mandir}/man1/fixwwps.1*
%{_mandir}/man1/includeres.1*
%{_mandir}/man1/psmerge.1*


%changelog
* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 1.17-44
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.17-43
- Mass rebuild 2013-12-27

* Tue Mar 26 2013 Jiri Popelka <jpopelka@redhat.com> - 1.17-42
- few usage/man page fixes

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.17-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Nov 29 2012 Jiri Popelka <jpopelka@redhat.com> - 1.17-40
- fix dist tag and URL
- put psutils-copyright.patch among sources as it's used only in
  psutils-remove-copyrighted-files
- no need to define BuildRoot and clean it in %%clean and %%install anymore
- %%defattr no longer needed in %%files

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.17-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.17-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.17-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 08 2010 Tomas Smetana <tsmetana@redhat.com> 1.17-36
- add the LICENSE file to the perl subpackage

* Thu Apr 22 2010 Daniel Novotny <dnovotny@redhat.com> 1.17-35
- renamed "clean" tarball to psutils-p17-clean.tar.gz 
  (merge review: #226324)

* Tue Jan 26 2010 Daniel Novotny <dnovotny@redhat.com> 1.17-34
- remove Apple copyrighted files (merge review: #226324)
- fixed URLs to upstream

* Mon Aug 10 2009 Ville Skyttä <ville.skytta@iki.fi> - 1.17-33
- Convert specfile to UTF-8.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.17-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 22 2009 Adam Jackson <ajax@redhat.com> 1.17-31
- Split perl scripts to a subpackage.

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.17-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Aug 29 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.17-29
- fix license tag

* Wed Feb 13 2008 Tomas Smetana <tsmetana@redhat.com> - 1.17-28
- rebuild (gcc-4.3)

* Tue Sep 18 2007 Martin Bacovsky <mbacovsk@redhat.com> - 1.17-27
- fixed Source url pointing to non-existing site

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.17-26.1
- rebuild

* Mon Jun 12 2006 Jitka Kudrnacova <jkudrnac@redhat.com> - 1.17-26
- new implementation of psmerge by Peter Williams

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.17-25.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.17-25.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Mar 16 2005 Tim Waugh <twaugh@redhat.com> 1.17-25
- Rebuild for new GCC.

* Mon Jan 10 2005 Tim Waugh <twaugh@redhat.com> 1.17-24
- Manpage correction for psresize (bug #144582).

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Jun 17 2003 Tim Waugh <twaugh@redhat.com> 1.17-21
- Rebuilt.

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Wed Dec 11 2002 Tim Powers <timp@redhat.com> 1.17-18
- rebuild on all arches

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu Jun 20 2002 Than Ngo <than@redhat.com> 1.17-16
- Don't forcibly strip binaries

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu Jul 19 2001 Than Ngo <than@redhat.com> 1.17-13
- add patch from enrico.scholz@informatik.tu-chemnitz.de

* Fri Jul 13 2001 Than Ngo <than@redhat.com> 1.17-12
- media size as letter (Bug #48831)
- Copyright->License
- don't hardcode manpath

* Sun Jun 24 2001 Elliot Lee <sopwith@redhat.com>
- Bump release + rebuild.

* Fri Dec  8 2000 Tim Powers <timp@redhat.com>
- built for dist-7.1

* Mon Jul 24 2000 Prospector <prospector@redhat.com>
- rebuilt

* Mon Jul 10 2000 Tim Powers <timp@redhat.com>
- rebuilt

* Mon Jul 03 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Fri May 26 2000 Tim Powers <timp@redhat.com>
- man pages in /usr/share/man (FHS compliant location)
- grabbed spec from contrib
- initial build for Powertools

* Wed May 12 1999 Peter Soos <sp@osb.hu>
- Corrected the file and directory attributes to rebuild the package
  under RedHat Linux 6.0

* Fri Dec 25 1998 Peter Soos <sp@osb.hu>
- Corrected the file and directory attributes

* Tue Jun 23 1998 Peter Soos <sp@osb.hu>
- Using %%attr for ability to rebuild the package as an ordinary user.

* Wed Jun 04 1997 Timo Karjalainen <timok@iki.fi>
- Reverted back to un-gzipped man-pages (Redhat style)
- Added patch to compile everything cleanly
- Some minor changes to specfile

* Thu Mar 27 1997 Tomasz Kłoczko <kloczek@rudy.mif.pg.gda.pl>
  - new version:
    Patchlevel 17 had some minor bugfixes and improvements
    - Trailer information now put before %%EOF comments if no %%Trailer
    - psselect can now add blank pages.
    - Piped input works in Linux
    - spec file rewrited for using Buildroot,
    - man pages gziped.

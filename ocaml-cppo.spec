%global opt %(test -x %{_bindir}/ocamlopt && echo 1 || echo 0)
%if !%{opt}
%global debug_package %{nil}
%endif

Name:           ocaml-cppo
Version:        1.1.2
Release:        3%{?dist}
Summary:        Equivalent of the C preprocessor for OCaml programs

License:        BSD
URL:            http://mjambon.com/cppo.html
Source0:        http://mjambon.com/releases/cppo/cppo-%{version}.tar.gz

BuildRequires:  ocaml >= 3.10.0
BuildRequires:  ocaml-findlib
%if !%{opt}
Requires:       ocaml >= 3.10.0
%endif
%if 0?%{epel}
BuildExclude:   ppc64
%endif

%define libname %(sed -e 's/^ocaml-//' <<< %{name})

%description
Cppo is an equivalent of the C preprocessor targeted at the OCaml
language and its variants.

The main purpose of cppo is to provide a lightweight tool for simple
macro substitution (＃define) and file inclusion (＃include) for the
occasional case when this is useful in OCaml. Processing specific
sections of files by calling external programs is also possible via
＃ext directives.

The implementation of cppo relies on the standard library of OCaml and
on the standard parsing tools Ocamllex and Ocamlyacc, which contribute
to the robustness of cppo across OCaml versions.


%prep
%setup -q -n %{libname}-%{version}
sed -i.add-debuginfo \
    's/ocamlopt/ocamlopt -g/;s/ocamlc \(-[co]\)/ocamlc -g \1/' \
    Makefile


%build
%if %opt
make %{?_smp_mflags} opt
%else
make %{?_smp_mflags} all
%endif


%install
%{__install} -d $RPM_BUILD_ROOT%{_bindir}
%{__install} -p cppo $RPM_BUILD_ROOT%{_bindir}/


%check
make test


%files
%doc LICENSE README.md Changes
%{_bindir}/cppo


%changelog
* Thu Sep 24 2015 Ding-Yi Chen <dchen@redhat.com> - 1.1.2-3
- Exclude ppc64 for EPEL, as ocaml-findlib is not available on it.

* Tue Jul 28 2015 Richard W.M. Jones <rjones@redhat.com> - 1.1.2-2
- OCaml 4.02.3 rebuild.

* Fri Jul 24 2015 Richard W.M. Jones <rjones@redhat.com> - 1.1.2-1
- New upstream release 1.1.2.

* Wed Jun 24 2015 Richard W.M. Jones <rjones@redhat.com> - 1.0.1-4
- ocaml-4.02.2 final rebuild.

* Wed Jun 17 2015 Richard W.M. Jones <rjones@redhat.com> - 1.0.1-3
- ocaml-4.02.2 rebuild.

* Tue Feb 17 2015 Richard W.M. Jones <rjones@redhat.com> - 1.0.1-2
- ocaml-4.02.1 rebuild.

* Mon Nov  3 2014 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.0.1-1
- Update to 1.0.1

* Sat Aug 30 2014 Richard W.M. Jones <rjones@redhat.com> - 0.9.3-9
- ocaml-4.02.0 final rebuild.

* Sat Aug 23 2014 Richard W.M. Jones <rjones@redhat.com> - 0.9.3-8
- ocaml-4.02.0+rc1 rebuild.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Aug 02 2014 Richard W.M. Jones <rjones@redhat.com> - 0.9.3-6
- ocaml-4.02.0-0.8.git10e45753.fc22 rebuild.

* Mon Jul 28 2014 Richard W.M. Jones <rjones@redhat.com> - 0.9.3-5
- Rebuild for OCaml 4.02.0 beta.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 24 2014 Jaromir Capik <jcapik@redhat.com> - 0.9.3-3
- Removing ExclusiveArch

* Mon Jan 27 2014 Michel Salim <salimma@fedoraproject.org> - 0.9.3-2
- Incorporate review feedback

* Mon Jan 20 2014 Michel Salim <salimma@fedoraproject.org> - 0.9.3-1
- Initial package

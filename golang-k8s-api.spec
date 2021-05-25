# https://github.com/kubernetes/api
%global goipath         k8s.io/api
%global forgeurl        https://github.com/kubernetes/api
Version:                1.21.1
%global tag             kubernetes-1.21.1
%global distprefix      %{nil}

%gometa

%global common_description %{expand:
Schema of the external API types that are served by the Kubernetes API server.}

%global golicenses      LICENSE
%global godocs          code-of-conduct.md CONTRIBUTING.md README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Canonical location of the Kubernetes API definition

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep

%generate_buildrequires
%go_generate_buildrequires

%install
%gopkginstall

%check
%gocheck

%gopkgfiles

%changelog
* Tue May 25 2021 Major Hayden <major@mhtx.net> - 1.21.1-1
- Update to 1.21.1

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Sep 30 13:19:04 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.18.9-1
- Update to 1.18.9

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.3-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 14 18:13:55 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.18.3-1
- Update to 1.18.3

* Sun Apr 12 20:33:42 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.18.1-1
- Update to 1.18.1

* Wed Feb 05 18:01:43 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.17.2-1
- Update to 1.17.2

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 06 16:05:13 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.15.0-1
- Release 1.15.0

* Fri May 10 15:26:40 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.13.7-1.beta.0
- Initial package

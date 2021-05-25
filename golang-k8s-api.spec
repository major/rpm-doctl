# https://github.com/kubernetes/api
%global     goipath         k8s.io/api
%global     forgeurl        https://github.com/kubernetes/api
Version:    1.21.1
%global     tag             kubernetes-1.21.1
%global     distprefix      %{nil}
%global     debug_package   %{nil}

%gometa

%global common_description %{expand:
The canonical location of the Kubernetes API definition.}

%global golicenses    LICENSE

Name:           %{goname}
Release:        1%{?dist}
Summary:        The canonical location of the Kubernetes API definition.
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
* Tue May 25 2021 Major Hayden <major@mhtx.net> - 1.21.1
- First package.

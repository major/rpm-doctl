# https://github.com/kubernetes/apimachinery
%global     goipath         k8s.io/apimachinery
%global     forgeurl        https://github.com/kubernetes/apimachinery
Version:    1.21.1
%global     tag             kubernetes-1.21.1
%global     distprefix      %{nil}
%global     debug_package   %{nil}

%gometa

%global common_description %{expand:
Scheme, typing, encoding, decoding, and conversion packages for Kubernetes and
Kubernetes-like API objects.}

%global golicenses    LICENSE

Name:           %{goname}
Release:        1%{?dist}
Summary:        Scheme, typing, encoding, decoding, and conversion packages for Kubernetes
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
%gocheck -d k8s.io/apimachinery/pkg/util/managedfields \
    -d k8s.io/apimachinery/pkg/util/strategicpatch

%gopkgfiles


%changelog
* Tue May 25 2021 Major Hayden <major@mhtx.net> - 1.21.1
- First package.

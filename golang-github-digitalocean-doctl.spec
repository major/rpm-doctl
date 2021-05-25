# https://github.com/digitalocean/doctl
%global     goipath     github.com/digitalocean/doctl
Version:                1.61.0

%gometa

%global common_description %{expand:
The official command line interface for the DigitalOcean API}

%global golicenses    LICENSE

Name:           %{goname}
Release:        1%{?dist}
Summary:        The official command line interface for the DigitalOcean API
License:        Apache 2.0
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
* Thu Mar 21 22:20:22 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.2.2-1
- First package for Fedora
# https://github.com/digitalocean/doctl
%global     goipath     github.com/digitalocean/doctl
Version:                1.60.0

%gometa

%global common_description %{expand:
The official command line interface for the DigitalOcean API}

%global golicenses    LICENSE

Name:           %{goname}
Release:        1%{?dist}
Summary:        The official command line interface for the DigitalOcean API
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
* Tue May 25 2021 Major Hayden <major@mhtx.net> - 1.60.0-1
- First package.

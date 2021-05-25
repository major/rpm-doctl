# https://github.com/moby/spdystream
%global     goipath         github.com/moby/spdystream
Version:    0.2.0
%global     debug_package   %{nil}

%gometa

%global common_description %{expand:
A multiplexed stream library using spdy}

%global golicenses    LICENSE

Name:           %{goname}
Release:        1%{?dist}
Summary:        A multiplexed stream library using spdy
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
* Tue May 25 2021 Major Hayden <major@mhtx.net> - 0.2.0-1
- First package.

# https://github.com/natefinch/pie
%global     goipath     github.com/natefinch/pie
Version:                1.0

%gometa

%global common_description %{expand:
A toolkit for creating plugins for Go applications.}

%global golicenses    LICENSE

Name:           %{goname}
Release:        1%{?dist}
Summary:        A toolkit for creating plugins for Go applications
License:        Apache 2.0
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%global debug_package %{nil}

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
* Tue May 25 2021 Major Hayden <major@mhtx.net> - 1.0-1
- First package.

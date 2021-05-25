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
* Thu Mar 21 22:20:22 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.2.2-1
- First package for Fedora
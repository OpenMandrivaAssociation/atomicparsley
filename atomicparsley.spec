# Spec is based on MIB work

%define		oname AtomicParsley
%define   oversion .200601.1ac7c08

Name:		atomicparsley
Version:	20210617
Release:	1
Summary:	Command-Line Program to Read and Set iTunes-style Metadata Tags
License:	GPLv2
Group:		Sound
Url:		http://atomicparsley.sourceforge.net
Source0:	https://github.com/wez/atomicparsley/archive/%{version}%{oversion}/%{name}-%{version}%{oversion}.tar.gz

BuildRequires:	libstdc++-devel
BuildRequires:	glibc-devel
BuildRequires:	unzip
BuildRequires:  cmake
BuildRequires:  pkgconfig(zlib)

%description
AtomicParsley is a lightweight command line program that can read and set
iTunes-style metadata tags in MPEG-4 files & 3gp assets in 3GPP/3GPP2 files. 

%prep
%setup -q -n %{name}-%{version}%{oversion}
%autopatch -p1


%build

%cmake -DCMAKE_BUILD_TYPE=Release \

%make_build

%install
%__install -D -m0755 build/%{oname} %{buildroot}%{_bindir}/%{name}


%files
%defattr(-,root,root)
%doc COPYING
%{_bindir}/%{name}

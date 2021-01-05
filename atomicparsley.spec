# Spec is based on MIB work

%define		oname AtomicParsley
%define   oversion .092811.cbecfb1

Name:		atomicparsley
Version:	20201231
Release:	1
Summary:	Command-Line Program to Read and Set iTunes-style Metadata Tags
License:	GPLv2
Group:		Sound
Url:		http://atomicparsley.sourceforge.net
Source0:	https://github.com/wez/atomicparsley/archive/%{version}%{oversion}/%{name}-%{version}%{oversion}.tar.gz
#Patch1:		AtomicParsley-fix_bad_math.patch
BuildRequires:	libstdc++-devel
BuildRequires:	glibc-devel
BuildRequires:	unzip
BuildRequires:  cmake

%description
AtomicParsley is a lightweight command line program that can read and set
iTunes-style metadata tags in MPEG-4 files & 3gp assets in 3GPP/3GPP2 files. 

%prep
%setup -q -n %{name}-%{version}%{oversion}
%autopatch -p1

#__sed -i '
#s/g++/$CXX/g;
#s/-g//g;
#s/-O2/$OPTFLAGS/g;
#' build
#
#__sed -i '1aset -e' build

%build
#CXX="%__cxx" \
#OPTFLAGS="%{optflags} -Wall -Wno-deprecated -fno-strict-aliasing" \
#./build

%cmake

%make_instll

%install
%make_install -C build


%files
%defattr(-,root,root)
%doc COPYING
%{_bindir}/%{name}



%changelog
* Fri Feb 17 2012 Andrey Bondrov <abondrov@mandriva.org> 0.9.0-1
+ Revision: 775963
- imported package atomicparsley


%global module	redisearch
Name:		RediSearch
Version:	2.0.5
Release:	4%{?dist}
Summary:	Full-text search over Redis

%global disable_tests 0

License:	AGPLv3
URL:		https://github.com/johnmate/RediSearch
Source0:	https://github.com/%{name}/%{name}/archive/v%{version}.tar.gz

# "RediSearch is developed and tested on Linux and Mac OS, on x86_64 CPUs." from docs/index.md
ExclusiveArch:  x86_64

BuildRequires: make
BuildRequires:	gcc
BuildRequires:	git
Requires:	redis >= 5
Requires:	redis(modules_abi)%{?_isa} = %{redis_modules_abi}

%description
RediSearch implements a search engine on top of Redis, providing
three main features - full text search, secondary indexing and a
suggestion (auto-completion) engine.

It provides advanced search features like exact phrase matching
and numeric filtering for text queries, that are not possible or
efficient with traditional Redis search approaches.

%prep
%setup -q

%build
make %{?_smp_mflags} LD="cc" LDFLAGS="%{?__global_ldflags}"

%if !%{disable_tests}
%check
make PYTHON="python3" test
%endif

%install
mkdir -p %{buildroot}%{redis_modules_dir}
install -pDm755 src/%{module}.so %{buildroot}%{redis_modules_dir}/%{module}.so

%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc README.md docs/*.md docs/*.png docs/img/*.png
%{redis_modules_dir}/%{module}.so

%changelog
* Wed Mar 03 2021 johnmate <rokha.evgeny@gmail.com> - 2.0.5-1
- Initial package

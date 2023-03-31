%bcond_with check
%global debug_package %{nil}

%global crate doc-comment

Name:           rust-%{crate}
Version:        0.3.3
Release:        2
Summary:        Macro to generate doc comments

License:        MIT
URL:            https://crates.io/crates/doc-comment
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging

%global _description \
Macro to generate doc comments.

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE
%doc README.md
%{cargo_registry}/%{crate}-%{version}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+no_core-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+no_core-devel %{_description}

This package contains library source intended for building other packages
which use "no_core" feature of "%{crate}" crate.

%files       -n %{name}+no_core-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+old_macros-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+old_macros-devel %{_description}

This package contains library source intended for building other packages
which use "old_macros" feature of "%{crate}" crate.

%files       -n %{name}+old_macros-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

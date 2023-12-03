Name: my_package
Version: 1.0
Release: 1%{?dist}
Summary: Підрахунок файлів у /etc

%description
Цей пакет містить скрипт для підрахунку файлів у /etc.

%prep

%build

%install
mkdir -p %{buildroot}/usr/bin
install -m 755 count_files.sh %{buildroot}/usr/bin

%files
/usr/bin/count_files.sh

%changelog


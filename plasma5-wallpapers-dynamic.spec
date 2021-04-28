Name:           plasma5-wallpapers-dynamic
Version:        3.3.9
Release:        1%{?dist}
Summary:        Dynamic wallpaper plugin for KDE Plasma

License:        BSD and CC-BY-SA and CC0 and GPLv3+ and LGPLv3+
URL:            https://github.com/zzag/plasma5-wallpapers-dynamic
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++

BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kpackage-devel
BuildRequires:  kf5-plasma-devel
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(libheif)
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  qt5-qtlocation-devel

%package        devel
Summary:        Development files for %{name}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%description
A wallpaper plugin for KDE Plasma that continuously updates
the desktop background based on the current time in your
location.


%prep
%autosetup


%build
%cmake . \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DBUILD_TESTING=OFF

%cmake_build

%install
%cmake_install

%find_lang plasma_wallpaper_com --all-name

%check
appstream-util validate-relax --nonet %{buildroot}%{_kf5_metainfodir}/com.github.zzag.dynamic.appdata.xml ||:


%files -f plasma_wallpaper_com.lang
%license LICENSES/*
%doc README.md src/tools/builder/README.md
%{_kf5_bindir}/kdynamicwallpaperbuilder
%{_kf5_libdir}/libkdynamicwallpaper.so*
%{_kf5_datadir}/bash-completion/
%{_kf5_datadir}/fish/completions/
%{_kf5_datadir}/zsh/site-functions/
%{_kf5_datadir}/kservices5/plasma-wallpaper-com.github.zzag.dynamic.desktop
%{_kf5_datadir}/plasma/wallpapers/
%{_kf5_datadir}/wallpapers/
%{_kf5_metainfodir}/com.github.zzag.dynamic.appdata.xml
%{_kf5_qmldir}/com/github/zzag/plasma/wallpapers/dynamic/
%{_kf5_qtplugindir}/kpackage/packagestructure/packagestructure_dynamicwallpaper.so

%files devel
%{_includedir}/KDynamicWallpaper/
%{_kf5_libdir}/cmake/KDynamicWallpaper/KDynamicWallpaper*.cmake



%changelog
* Wed Apr 28 2021 ElXreno <elxreno@gmail.com> - 3.3.9-1
- Initial build

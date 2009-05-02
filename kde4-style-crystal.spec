Name: kde4-style-crystal
Summary: Crystal kwin decoration theme to KDE 4.x
Version: 2.0.3
Release: %mkrel 1
Source0: http://www.kde-look.org/CONTENT/content-files/75140-crystal-%version.tar.bz2
URL: http://www.kde-look.org/content/show.php/crystal?content=75140
Group: Graphical desktop/KDE
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
License: GPLv2+
BuildRequires: kdebase4-workspace-devel
Obsoletes: kde4-kwin-style-crystal < %version-%release

%description
This is the port of the famous Crystal kwin decoration theme to KDE 4.x.

Main features:
* Choose the blending color of the buttons.
* You can define the title bar height and border size of the windows.
* Right click on minimize button toggles shade mode.
* Middle click on minimize button sends window to below.
* Double click on program symbol closes window.
* Support for button themes. Basic button theme is included, feel free
  to swamp me with cool themes.
* Can show a tooltip of the caption
* If kdocker is installed (http://kdocker.sf.net), right click on close
  button will send the window to the systemtray.

%prep
%setup -q -n crystal-%version

%build
%cmake_kde4
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std -C build

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS README TODO.txt
%{_kde_libdir}/kde4/kwin3_crystal.so
%{_kde_libdir}/kde4/kwin_crystal_config.so
%{_kde_appsdir}/kwin/crystal.desktop

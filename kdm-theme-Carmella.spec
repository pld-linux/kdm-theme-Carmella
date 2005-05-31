
%define		_theme		Carmella

Summary:	Carmella KDM theme
Summary(pl):	Motywm KDM Carmella
Name:		kdm-theme-%{_theme}
Version:	01
Release:	1
License:	GPL
Group:		X11/Amusements
Source0:	http://www.kde-look.org/content/files/24338-%{_theme}_kdm-theme.tar.gz
# Source0-md5:	163125d25181d16cf2fd4eed67238ee0
URL:		http://www.kde-look.org/content/show.php?content=24338
Requires:	kdebase-desktop >= 9:3.2.0
Requires:	kdmtheme
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A KDM Theme based off of Teddy's Revolution KDM Theme (
http://kdelook.org/content/show.php?content=23531 ) with a few
modifications made.

- *** Contains Partial Nudity ***

%description -l pl
Motyw KDM bazuje na motywie "Teddy's Revolution" (
http://kdelook.org/content/show.php?content=23531 ) z kilkoma
modyfikacjami.

- *** Zawiera Czê¶ciow± Nago¶æ ***

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/apps/kdm/themes/%{_theme}

install %{_theme}_kdm-theme/*.{desktop,jpg,png,txt,xml} $RPM_BUILD_ROOT%{_datadir}/apps/kdm/themes/%{_theme}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/apps/kdm/themes/%{_theme}

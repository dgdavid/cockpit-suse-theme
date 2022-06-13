#
# spec file for package cockpit-suse-theme
#
# Copyright (c) 2022 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           cockpit-suse-theme
Version:        0.1
Release:        0
Summary:        A Cockpit green-ish theme
License:        MIT

Requires:       cockpit-ws
BuildRequires:  cockpit-ws

Source0:        overrides.css
Source1:        fonts.css
Source2:        LatoLatin-BoldItalic.woff2
Source3:        LatoLatin-Bold.woff2
Source4:        LatoLatin-Italic.woff2
Source5:        LatoLatin-Regular.woff2
Source6:        poppins-v19-latin-ext_latin_devanagari-300italic.woff
Source7:        poppins-v19-latin-ext_latin_devanagari-300italic.woff2
Source8:        poppins-v19-latin-ext_latin_devanagari-300.woff
Source9:        poppins-v19-latin-ext_latin_devanagari-300.woff2
Source10:       poppins-v19-latin-ext_latin_devanagari-500italic.woff
Source11:       poppins-v19-latin-ext_latin_devanagari-500italic.woff2
Source12:       poppins-v19-latin-ext_latin_devanagari-500.woff
Source13:       poppins-v19-latin-ext_latin_devanagari-500.woff2
Source14:       poppins-v19-latin-ext_latin_devanagari-regular.woff
Source15:       poppins-v19-latin-ext_latin_devanagari-regular.woff2
Source16:       roboto-mono-v13-vietnamese_latin-ext_latin_greek_cyrillic-ext_cyrillic-regular.woff
Source17:       roboto-mono-v13-vietnamese_latin-ext_latin_greek_cyrillic-ext_cyrillic-regular.woff2

%description
A package holding needed resources for changing Cockpit styling to match the
SUSE look&feel by using the workaround described at
https://github.com/cockpit-project/cockpit/pull/17437

Intended changes only take effect when using a Cockpit version patched for
loading the CSS overrides file in each HTML page.

%install
mkdir -p %{buildroot}%{_datadir}/cockpit/branding/default/fonts
cp %{SOURCE0} %{buildroot}%{_datadir}/cockpit/branding/default/css-overrides.css
cp %{SOURCE1} %{buildroot}%{_datadir}/cockpit/branding/default/fonts.css
cp %{SOURCE2} %{buildroot}%{_datadir}/cockpit/branding/default/fonts/
cp %{SOURCE3} %{buildroot}%{_datadir}/cockpit/branding/default/fonts/
cp %{SOURCE4} %{buildroot}%{_datadir}/cockpit/branding/default/fonts/
cp %{SOURCE5} %{buildroot}%{_datadir}/cockpit/branding/default/fonts/
cp %{SOURCE6} %{buildroot}%{_datadir}/cockpit/branding/default/fonts/
cp %{SOURCE7} %{buildroot}%{_datadir}/cockpit/branding/default/fonts/
cp %{SOURCE8} %{buildroot}%{_datadir}/cockpit/branding/default/fonts/
cp %{SOURCE9} %{buildroot}%{_datadir}/cockpit/branding/default/fonts/
cp %{SOURCE10} %{buildroot}%{_datadir}/cockpit/branding/default/fonts/
cp %{SOURCE11} %{buildroot}%{_datadir}/cockpit/branding/default/fonts/
cp %{SOURCE12} %{buildroot}%{_datadir}/cockpit/branding/default/fonts/
cp %{SOURCE13} %{buildroot}%{_datadir}/cockpit/branding/default/fonts/
cp %{SOURCE14} %{buildroot}%{_datadir}/cockpit/branding/default/fonts/
cp %{SOURCE15} %{buildroot}%{_datadir}/cockpit/branding/default/fonts/
cp %{SOURCE16} %{buildroot}%{_datadir}/cockpit/branding/default/fonts/
cp %{SOURCE17} %{buildroot}%{_datadir}/cockpit/branding/default/fonts/

%files
%{_datadir}/cockpit
%{_datadir}/cockpit/branding/default/css-overrides.css
%{_datadir}/cockpit/branding/default/fonts.css
%{_datadir}/cockpit/branding/default/fonts/LatoLatin-Bold.woff2
%{_datadir}/cockpit/branding/default/fonts/LatoLatin-Italic.woff2
%{_datadir}/cockpit/branding/default/fonts/LatoLatin-Regular.woff2
%{_datadir}/cockpit/branding/default/fonts/poppins-v19-latin-ext_latin_devanagari-300italic.woff
%{_datadir}/cockpit/branding/default/fonts/poppins-v19-latin-ext_latin_devanagari-300italic.woff2
%{_datadir}/cockpit/branding/default/fonts/poppins-v19-latin-ext_latin_devanagari-300.woff
%{_datadir}/cockpit/branding/default/fonts/poppins-v19-latin-ext_latin_devanagari-300.woff2
%{_datadir}/cockpit/branding/default/fonts/poppins-v19-latin-ext_latin_devanagari-500italic.woff
%{_datadir}/cockpit/branding/default/fonts/poppins-v19-latin-ext_latin_devanagari-500italic.woff2
%{_datadir}/cockpit/branding/default/fonts/poppins-v19-latin-ext_latin_devanagari-500.woff
%{_datadir}/cockpit/branding/default/fonts/poppins-v19-latin-ext_latin_devanagari-500.woff2
%{_datadir}/cockpit/branding/default/fonts/poppins-v19-latin-ext_latin_devanagari-regular.woff
%{_datadir}/cockpit/branding/default/fonts/poppins-v19-latin-ext_latin_devanagari-regular.woff2
%{_datadir}/cockpit/branding/default/fonts/roboto-mono-v13-vietnamese_latin-ext_latin_greek_cyrillic-ext_cyrillic-regular.woff
%{_datadir}/cockpit/branding/default/fonts/roboto-mono-v13-vietnamese_latin-ext_latin_greek_cyrillic-ext_cyrillic-regular.woff2

%changelog

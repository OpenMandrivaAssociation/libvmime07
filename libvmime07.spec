%define	major 0
%define	libname %mklibname vmime07 _%{major}
%define develname %mklibname vmime07 -d

Summary:	A powerful C++ class library for working with MIME/Internet messages
Name:		libvmime07
Version:	0.7.1
Release:	%mkrel 2
License:	GPLv2+
Group:		System/Libraries
URL:		http://www.zarafa.com/wiki/index.php/Libvmime_patches
Source0:	http://developer.zarafa.com/download/libvmime-%{version}.tar.bz2
Patch0:		libvmime07-0.7.1-package.patch
Patch1:		libvmime07-0.7.1-charset-catch.patch
Patch2:		libvmime07-0.7.1-missing-boundary.patch
Patch3:		libvmime07-0.7.1-allow-no-recips-and-senders.patch
Patch4:		libvmime07-0.7.1-bmoted-printable.patch
Patch5:		libvmime07-0.7.1-strip-header-endspaces-and-header-end.patch
Patch6:		libvmime07-0.7.1-attachfnamelen.patch
Patch7:		libvmime07-0.7.1-remove-bcc.patch
Patch8:		libvmime07-0.7.1-mdn-disposition.patch
Patch9:		libvmime07-0.7.1-mdn-final-recipient.patch
Patch10:	libvmime07-0.7.1-broken-locale-error.patch
Patch11:	libvmime07-0.7.1-qp-starts-on-second-line.patch
Patch12:	libvmime07-0.7.1-quoted-printable-specials.patch
Patch13:	libvmime07-0.7.1-header-value-on-next-line.patch
Patch14:	libvmime07-0.7.1-oe-compatibility.patch
Patch15:	libvmime07-0.7.1-unicode-1-1-utf-7-charset.patch
Patch16:	libvmime07-0.7.1-out-of-bounds-copy.patch
Patch17:	libvmime07-0.7.1-default-transfer-encoding.patch
Patch18:	libvmime07-0.7.1-contentid-without-at.patch
Patch19:	libvmime07-0.7.1-socket-backport-and-timeout-fix.patch
Patch20:	libvmime07-0.7.1-double-empty-boundary.patch
Patch21:	libvmime07-0.7.1-quoted-printable-encode-questionmark.patch
Patch22:	libvmime07-0.7.1-charset-output-buffer-full.patch
Patch23:	libvmime07-0.7.1-gcc-4.3-support.patch
Patch24:	libvmime07-0.7.1-timezone-name.patch
Patch25:	libvmime07-0.7.1-socket-tcp-nodelay.patch
Patch26:	libvmime07-0.7.1-threading-remove-static_non-abi-change.patch
Patch27:	libvmime07-0.7.1-gcc-4.4-support.patch
Patch28:	libvmime07-0.7.1-plain-bodycopy.patch
Patch29:	libvmime07-0.7.1-sigset-signal.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
VMime is a powerful C++ class library for parsing, generating or
editing Internet RFC-[2]822 and MIME messages. VMime is designed
to provide a fast and an easy way to manipulate Internet mail
messages.

It also includes support for using messaging protocols (POP3, IMAP,
SMTP and maildir) with a lot of features supported: listing folders,
downloading and adding messages to folders, extracting parts from
message, getting and setting message flags and a lot more.

This package contains an old and deprecated version of libvmime.
You need it only if the software you are using hasn't been updated
to work with the newer version and the newer API.

%package -n	%{libname}
Summary:	Library associated with ncpfs
Group:		System/Libraries

%description -n	%{libname}
VMime is a powerful C++ class library for parsing, generating or
editing Internet RFC-[2]822 and MIME messages. VMime is designed
to provide a fast and an easy way to manipulate Internet mail
messages.

It also includes support for using messaging protocols (POP3, IMAP,
SMTP and maildir) with a lot of features supported: listing folders,
downloading and adding messages to folders, extracting parts from
message, getting and setting message flags and a lot more.

This package contains an old and deprecated version of libvmime.
You need it only if the software you are using hasn't been updated
to work with the newer version and the newer API.

%package -n	%{develname}
Summary:	Development files for the libvmime library
Group:		Development/C++
Requires:	%{libname} >= %{version}-%{release}
Requires:	pkgconfig
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{develname}
The libvmime package includes header files and libraries necessary
for developing programs which use the libvmime C++ class library.

This package contains an old and deprecated version of libvmime.
You need it only if the software you are using hasn't been updated
to work with the newer version and the newer API.

%prep

%setup -q -n libvmime-%{version}
%patch0 -p1 -b .package
%patch1 -p1 -b .charset-catch
%patch2 -p1 -b .missing-boundary
%patch3 -p1 -b .allow-no-recips-and-senders
%patch4 -p1 -b .bmoted-printable
%patch5 -p1 -b .strip-header-endspaces-and-header-end
%patch6 -p1 -b .attachfnamelen
%patch7 -p1 -b .remove-bcc
%patch8 -p1 -b .mdn-disposition
%patch9 -p1 -b .mdn-final-recipient
%patch10 -p1 -b .broken-locale-error
%patch11 -p1 -b .qp-starts-on-second-line
%patch12 -p1 -b .quoted-printable-specials
%patch13 -p1 -b .header-value-on-next-line
%patch14 -p1 -b .oe-compatibility
%patch15 -p1 -b .unicode-1-1-utf-7-charset
%patch16 -p1 -b .out-of-bounds-copy
%patch17 -p1 -b .default-transfer-encoding
%patch18 -p1 -b .contentid-without-at
%patch19 -p1 -b .socket-backport-and-timeout-fix
%patch20 -p1 -b .double-empty-boundary
%patch21 -p1 -b .quoted-printable-encode-questionmark
%patch22 -p1 -b .charset-output-buffer-full
%patch23 -p1 -b .gcc-4.3-support
%patch24 -p1 -b .timezone-name
%patch25 -p1 -b .socket-tcp-nodelay
%patch26 -p1 -b .threading-remove-static_non-abi-change
%patch27 -p1 -b .gcc-4.4-support
%patch28 -p1 -b .plain-bodycopy
%patch29 -p1 -b .sigset-signal

%build
# Needed to apply branding patch
libtoolize --force
autoreconf --force --install

export EXTRA_CFLAGS="%{optflags}"
export SENDMAIL=%{_sbindir}/sendmail

%configure2_5x
%make

%install
rm -rf %{buildroot}

%makeinstall_std

# Complete the libvmime07 renaming at some places
mkdir -p %{buildroot}%{_includedir}/%{name}/
mv -f %{buildroot}%{_includedir}/{vmime,%{name}}/
mv -f %{buildroot}%{_libdir}/pkgconfig/vmime{,07}.pc 

# Remove the static library and libtool .la file
rm -f %{buildroot}%{_libdir}/%{name}.{a,la}

# Remove the documentation dir, as %doc will pick it up
rm -rf %{buildroot}%{_datadir}/doc

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog
%{_libdir}/%{name}.so.*

%files -n %{develname}
%defattr(-,root,root,-)
%{_libdir}/%{name}.so
%{_includedir}/%{name}/
%{_libdir}/pkgconfig/vmime07.pc


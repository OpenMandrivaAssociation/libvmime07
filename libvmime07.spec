%define	major 0
%define	libname %mklibname vmime07 _%{major}
%define develname %mklibname vmime07 -d

%if %mandriva_branch == Cooker
# Cooker
%define release %mkrel 3
%else
# Old distros
%define subrel 2
%define release %mkrel 0
%endif

Summary:	A powerful C++ class library for working with MIME/Internet messages
Name:		libvmime07
Version:	0.7.1
Release:	%release
License:	GPLv2+
Group:		System/Libraries
URL:		http://www.zarafa.com/wiki/index.php/Libvmime_patches
Source0:	http://developer.zarafa.com/download/libvmime-%{version}.tar.bz2
Patch0:		libvmime07-0.7.1-package.patch
# Early catches an exception of vmime when iconv was unable to convert a word from or to the requested charsets. This makes broken mails with invalid characters for a valid charset still be able to deliver. We'd rather have an email with a ? sign than a FallbackDelivery for the user.
Patch1:		libvmime07-0.7.1-charset-catch.patch
# Broken emails without a final boundary will still be able to deliver with all attachments. The final part without the boundary will be treated as an attachment.
Patch2:		libvmime07-0.7.1-missing-boundary.patch
# Makes the messageBuilder helper generate an mail without To or Cc headers. This way, an email with only Bcc entries will still be sent. This feature is mostly used by people to mask a mailing list or invitation that should be send to alot of people.
Patch3:		libvmime07-0.7.1-allow-no-recips-and-senders.patch
# We've seen broken mails with an invalid encoding. Unsure what 'bmoted-printable' actually is, we make vmime treat it as normal quoted-printable.
Patch4:		libvmime07-0.7.1-bmoted-printable.patch
# This patch makes sure that vmime does not parse trailing spaces on an header. Otherwise vmime will throw an exception and a fallback delivery wil be started.
Patch5:		libvmime07-0.7.1-strip-header-endspaces-and-header-end.patch
# Fixes parsing of an attachment filename that is between 66 and 76 characters long.
Patch6:		libvmime07-0.7.1-attachfnamelen.patch
# Bcc headers should not be send to the SMTP server. Some SMTP server automatically strip this header (Postfix, qmail), and others have an option for this (Exim).
Patch7:		libvmime07-0.7.1-remove-bcc.patch
# Fixes a small but crusial typo in a header of an MDN (read receipt) mail.
Patch8:		libvmime07-0.7.1-mdn-disposition.patch
# A header with the final recipient information was created, but not added to the MDN email. This patch adds this information to the mail.
Patch9:		libvmime07-0.7.1-mdn-final-recipient.patch
# On [WWW] Debian machines, you need to configure the locales (languages) that will be used on the system. When you use a locale (eg. LC_MESSAGES=nl_NL, but did not configure your distribution to have this locale present on your system, a NULL pointer would have thrown an exception in the std::string class. This makes sure that exception never happends.
Patch10:	libvmime07-0.7.1-broken-locale-error.patch
# Headers can be broken over multiple lines in an email. When the wrapped line directly started with quoted-printable, vmime copied this text as normal text, in stead of parsing it as quoted-printable.
Patch11:	libvmime07-0.7.1-qp-starts-on-second-line.patch
# This patch adds some characters that should be "escaped" in quoted-printable. With this fix you can have these characters in a fullname of an email address.
Patch12:	libvmime07-0.7.1-quoted-printable-specials.patch
# When an email header has the data part on the second line, vmime was unable to parse this data and skip adds the header as empty to it's internal structures. This makes sure these headers are still correctly parsed.
Patch13:	libvmime07-0.7.1-header-value-on-next-line.patch
# Fixes attachment names in Outlook Express which are long and have high characters.
Patch14:	libvmime07-0.7.1-oe-compatibility.patch
# Some mails have a special definition of the utf-7 character set, named unicode-1-1-utf-7. Since this name is not defined by iconv, we rename it to utf-7.
Patch15:	libvmime07-0.7.1-unicode-1-1-utf-7-charset.patch
# When a line in a plain text mail starts with a '.', the character needs to be escaped. VMime has a special filter for this, but due to a bug in this filter, a second line starting with a '.' would trigger a wrong buffer copy, and your email would contain double parts.
Patch16:	libvmime07-0.7.1-out-of-bounds-copy.patch
# Some broken generators may set the Content-Tranfer-Encoding header, but did not set any value. We'll assume the default value '7bit'.
Patch17:	libvmime07-0.7.1-default-transfer-encoding.patch
# Enables re-generation of broken content-id's that had no @ sign in them.
Patch18:	libvmime07-0.7.1-contentid-without-at.patch
# Small partial backport of some socket handling code from 0.8.1
# Only receiving data is handled better. It also has a timeout, when receiving data from a socket hasn't worked for 5 minutes. This isn't present in 0.8.1.
Patch19:	libvmime07-0.7.1-socket-backport-and-timeout-fix.patch
# When an email contains the same boundary to announce a new body part directly one after another, vmime would have crashed because the body part added to the object with size of (size_type)(-1). Thus having a body part of 4294967294 bytes on 32bit and 18446744073709551615 bytes on 64bit systems.
Patch20:	libvmime07-0.7.1-double-empty-boundary.patch
# Special characters break the quotedprintable encoding when they are typed after a ?. This fix also encodes ?-characters, so we can't break the encoding with this trick.
Patch21:	libvmime07-0.7.1-quoted-printable-encode-questionmark.patch
Patch22:	libvmime07-0.7.1-charset-output-buffer-full.patch
# Adds required include headers to compile with g++-4.3.
Patch23:	libvmime07-0.7.1-gcc-4.3-support.patch
# Fixes dates in headers which use a timezone definition, instead of a numeric timezone offset.
Patch24:	libvmime07-0.7.1-timezone-name.patch
# Adds the TCP_NODELAY flag to vmime sockets. This makes the SMTP connection much faster.
Patch25:	libvmime07-0.7.1-socket-tcp-nodelay.patch
# Workaround a static variable in the smart_ptr class using a pthread mutex, which fixes multi-threading issues in libvmime.
Patch26:	libvmime07-0.7.1-threading-remove-static_non-abi-change.patch
# Adds required include headers to compile with g++-4.4.
Patch27:	libvmime07-0.7.1-gcc-4.4-support.patch
# When constructing a plaintext only body without attachments, a copy of the body was made to set as the real body, and thus
# removing all the multiparts. However, the same reference is removed before setting the new body, thus invalidating that body
# we wish to copy, possibly resulting in a crash.
Patch28:	libvmime07-0.7.1-plain-bodycopy.patch
Patch29:	libvmime07-0.7.1-sigset-signal.patch
#Fixes RFC 2047 encoded fullname parsing. All addresses after a wrongly parsed address were not recognized anymore.
Patch30:	libvmime07-0.7.1-address-parse-encoded.diff
# Adds support for address headers that specify an (encoded) fullname with an empty email address, which was set by a <> marker.
Patch31:	libvmime07-0.7.1-fullname-without-email-address.diff
#Strips excessive spaces in parameterized headers. Backported from upstream svn.
Patch32:	libvmime07-0.7.1-strip-spaces-parameterized-headers.diff
# Allows non-rfc 7-bit and 8-bit encodings in Content-Transfer-Encoding headers.
Patch33:	libvmime07-0.7.1-allow-alternate-encodings.diff
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
%patch30 -p0 -b .address-parse-encoded
%patch31 -p0 -b .fullname-without-email-address
%patch32 -p0 -b .strip-spaces-parameterized-headers
%patch33 -p0 -b .allow-alternate-encodings

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


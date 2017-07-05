from md5 import md5
import os
from os import path
from tempfile import mkstemp
import unittest

from release.updates.verify import UpdateVerifyConfig, UpdateVerifyError


class TestUpdateVerifyConfig(unittest.TestCase):
    config = path.join(path.dirname(__file__), "sample-update-verify.cfg")

    def setUp(self):
        self.uvc = UpdateVerifyConfig()
        fd, self.tmpfilename = mkstemp()
        self.tmpfile = os.fdopen(fd, "w")

    def tearDown(self):
        self.tmpfile.close()
        os.unlink(self.tmpfilename)

    def testEq(self):
        self.uvc.product = "foo"
        self.uvc.channel = "betatest"
        self.uvc.aus_server = "aus"
        self.uvc.ftp_server_from = "ftp"
        self.uvc.ftp_server_to = "ftp"
        self.uvc.to = "/firefox/4.0rc2.tar.bz2"
        self.uvc.mar_channel_IDs = 'baz'
        uvc2 = UpdateVerifyConfig()
        uvc2.product = "foo"
        uvc2.channel = "betatest"
        uvc2.aus_server = "aus"
        uvc2.ftp_server_form = "ftp"
        uvc2.ftp_server_to = "ftp"
        uvc2.to = "/firefox/4.0rc2.tar.bz2"
        uvc2.mar_channel_IDs = 'baz'
        self.assertEquals(self.uvc, uvc2)

    def testNe(self):
        self.uvc.product = "foo"
        uvc2 = UpdateVerifyConfig()
        # assertNotEqual doesn't test the __ne__ function, so we do this
        self.assertTrue(self.uvc != uvc2)

    def testAddRelease(self):
        releases = [
            {
                "release": "4.0",
                "platform": "bar",
                "build_id": 555,
                "locales": ["af", "de"],
                "patch_types": ["partial", "complete"],
                "from": "/pub/firefox/foo.bz2",
                "ftp_server_from": "from",
                "ftp_server_to": "to",
                "mar_channel_IDs": "firefox-mozilla-booyah"
            }
        ]
        self.uvc.addRelease("4.0", build_id=555, locales=["af", "de"],
                            patch_types=["partial", "complete"],
                            from_path="/pub/firefox/foo.bz2",
                            ftp_server_from="from", ftp_server_to="to",
                            mar_channel_IDs="firefox-mozilla-booyah",
                            platform="bar")
        self.assertEquals(self.uvc.releases, releases)

    def testAddReleasesWithDifferentPlatforms(self):
        releases = [
            {
                "release": "4.0",
                "platform": "WINNT_x86-msvc",
                "build_id": 555,
                "locales": ["af", "de"],
                "patch_types": ["partial", "complete"],
                "from": "/pub/firefox/foo.bz2",
                "ftp_server_from": "from",
                "ftp_server_to": "to",
                "mar_channel_IDs": "firefox-mozilla-booyah"
            },
            {
                "release": "5.0",
                "platform": "WINNT_x86-msvc-x86",
                "build_id": 666,
                "locales": ["af", "de"],
                "patch_types": ["partial", "complete"],
                "from": "/pub/firefox/foo2.bz2",
                "ftp_server_from": "from",
                "ftp_server_to": "to",
                "mar_channel_IDs": "firefox-mozilla-booyah"
            }
        ]
        self.uvc.addRelease("4.0", build_id=555, locales=["af", "de"],
                            patch_types=["partial", "complete"],
                            from_path="/pub/firefox/foo.bz2",
                            ftp_server_from="from", ftp_server_to="to",
                            mar_channel_IDs="firefox-mozilla-booyah",
                            platform="WINNT_x86-msvc")
        self.uvc.addRelease("5.0", build_id=666, locales=["af", "de"],
                            patch_types=["partial", "complete"],
                            from_path="/pub/firefox/foo2.bz2",
                            ftp_server_from="from", ftp_server_to="to",
                            mar_channel_IDs="firefox-mozilla-booyah",
                            platform="WINNT_x86-msvc-x86")
        self.assertEquals(self.uvc.releases, releases)

    def testRead(self):
        ftp_server_from = "stage.mozilla.org/firefox"
        ftp_server_to = "stage.mozilla.org/firefox"
        uvc2 = UpdateVerifyConfig()
        uvc2.product = "Firefox"
        uvc2.channel = "betatest"
        uvc2.aus_server = "https://aus4.mozilla.org"
        uvc2.to = "/firefox/4.0rc2.tar.bz2"
        uvc2.addRelease("4.0", build_id="888", platform="Linux_x86-gcc3",
                        locales=["af", "de", "en-US", "ja", "zh-TW"],
                        patch_types=["partial", "complete"],
                        from_path="/firefox/4.0rc1.tar.bz2",
                        ftp_server_from=ftp_server_from,
                        ftp_server_to=ftp_server_to,
                        mar_channel_IDs="firefox-mozilla-beta")
        uvc2.addRelease("4.0b12", build_id="777", platform="Linux_x86-gcc3",
                        locales=["af", "en-US"],
                        from_path="/firefox/4.0b12.tar.bz2",
                        ftp_server_from=ftp_server_from,
                        ftp_server_to=ftp_server_to)
        uvc2.addRelease("4.0b12", build_id="777", platform="Linux_x86-gcc3",
                        locales=["de", "ja", "zh-TW"],
                        ftp_server_from=ftp_server_from,
                        ftp_server_to=ftp_server_to)
        uvc2.addRelease("3.7a1", build_id="666", locales=["en-US"],
                        ftp_server_from=ftp_server_from,
                        ftp_server_to=ftp_server_to, platform="Linux_x86-gcc3")

        self.uvc.read(self.config)
        self.assertEquals(self.uvc, uvc2)

    def testWrite(self):
        ftp_server_from = "stage.mozilla.org/firefox"
        ftp_server_to = "stage.mozilla.org/firefox"
        self.uvc.product = "Firefox"
        self.uvc.channel = "betatest"
        self.uvc.aus_server = "https://aus4.mozilla.org"
        self.uvc.to = "/firefox/4.0rc2.tar.bz2"
        self.uvc.addRelease("4.0", build_id="888", platform="Linux_x86-gcc3",
                            locales=("af", "de", "en-US", "ja", "zh-TW"),
                            patch_types=("partial", "complete"),
                            from_path="/firefox/4.0rc1.tar.bz2",
                            ftp_server_from=ftp_server_from,
                            ftp_server_to=ftp_server_to,
                            mar_channel_IDs="firefox-mozilla-beta")
        self.uvc.addRelease("4.0b12", build_id="777", platform="Linux_x86-gcc3",
                            locales=["af", "en-US"],
                            from_path="/firefox/4.0b12.tar.bz2",
                            ftp_server_from=ftp_server_from,
                            ftp_server_to=ftp_server_to)
        self.uvc.addRelease("4.0b12", build_id="777", platform="Linux_x86-gcc3",
                            locales=("de", "ja", "zh-TW"),
                            ftp_server_from=ftp_server_from,
                            ftp_server_to=ftp_server_to)
        self.uvc.addRelease("3.7a1", build_id="666", locales=("en-US",),
                            ftp_server_from=ftp_server_from,
                            ftp_server_to=ftp_server_to,
                            platform="Linux_x86-gcc3")

        self.uvc.write(self.tmpfile)
        self.tmpfile.close()
        self.assertEquals(md5(open(self.config).read()).hexdigest(),
                          md5(open(self.tmpfilename).read()).hexdigest())

    def testReadInvalidKey(self):
        invalidLine = 'foo="bar"'
        self.assertRaises(UpdateVerifyError, self.uvc._parseLine, invalidLine)

    def testReadDuplicateKey(self):
        invalidLine = 'release="bar" release="blah"'
        self.assertRaises(UpdateVerifyError, self.uvc._parseLine, invalidLine)

    def testParseLineBad(self):
        invalidLine = 'abh nthntuehonhuh nhhueont hntueoh nthouo'
        self.assertRaises(UpdateVerifyError, self.uvc._parseLine, invalidLine)

    def testGetChunk(self):
        ftp_server_from = "stage.mozilla.org/firefox"
        ftp_server_to = "stage.mozilla.org/firefox"
        self.uvc.read(self.config)
        uvc2 = UpdateVerifyConfig()
        uvc2.product = "Firefox"
        uvc2.channel = "betatest"
        uvc2.aus_server = "https://aus4.mozilla.org"
        uvc2.to = "/firefox/4.0rc2.tar.bz2"
        uvc2.addRelease("4.0", build_id="888", platform="Linux_x86-gcc3",
                        locales=["af", "de", "en-US"],
                        patch_types=["partial", "complete"],
                        from_path="/firefox/4.0rc1.tar.bz2",
                        ftp_server_from=ftp_server_from,
                        ftp_server_to=ftp_server_to,
                        mar_channel_IDs="firefox-mozilla-beta")
        uvc2.addRelease("4.0b12", build_id="777", platform="Linux_x86-gcc3",
                        locales=["de", "ja"],
                        patch_types=["complete"],
                        ftp_server_from=ftp_server_from,
                        ftp_server_to=ftp_server_to,
                        from_path=None)
        chunkedConfig = self.uvc.getChunk(chunks=3, thisChunk=1)
        self.assertEquals(chunkedConfig, uvc2)

    def testGetChunkWithPathWithSpaces(self):
        self.uvc.product = "Firefox"
        self.uvc.channel = "betatest"
        self.uvc.aus_server = "https://aus4.mozilla.org"
        self.uvc.ftp_server_from = "stage.mozilla.org/firefox"
        self.uvc.ftp_server_to = "stage.mozilla.org/firefox"
        self.uvc.to = "/firefox/Firefox 4.0 Beta 2.exe"
        self.uvc.addRelease("4.0b1", build_id="222", platform="Linux_x86-gcc3",
                            locales=["en-US", "ja", "zh-TW"],
                            patch_types=["complete"],
                            from_path="/firefox/Firefox 4.0 Beta 1.exe")
        uvc2 = UpdateVerifyConfig()
        uvc2.product = "Firefox"
        uvc2.channel = "betatest"
        uvc2.aus_server = "https://aus4.mozilla.org"
        uvc2.ftp_server_from = "stage.mozilla.org/firefox"
        uvc2.ftp_server_to = "stage.mozilla.org/firefox"
        uvc2.to = "/firefox/Firefox 4.0 Beta 2.exe"
        uvc2.addRelease("4.0b1", build_id="222", platform="Linux_x86-gcc3",
                        locales=["en-US", "ja"],
                        patch_types=["complete"],
                        from_path="/firefox/Firefox 4.0 Beta 1.exe")
        chunkedConfig = self.uvc.getChunk(chunks=2, thisChunk=1)
        self.assertEquals(chunkedConfig, uvc2)

    def testAddLocaleToRelease(self):
        from_path = "/firefox/4.0rc1.tar.bz2"
        self.uvc.read(self.config)
        self.uvc.addLocaleToRelease("888", "he", from_path)
        self.assertEquals(self.uvc.getRelease("888", from_path)["locales"],
                          ["af", "de", "en-US", "he", "ja", "zh-TW"])

    def testAddLocaleToReleaseMultipleBuildIDs(self):
        from_path = None
        self.uvc.read(self.config)
        self.uvc.addLocaleToRelease("777", "he", from_path)
        self.assertEquals(self.uvc.getRelease(
            "777", from_path)["locales"], ["de", "he", "ja", "zh-TW"])

    def testAddLocaleToNonexistentRelease(self):
        self.uvc.read(self.config)
        self.assertRaises(
            UpdateVerifyError, self.uvc.addLocaleToRelease, "123", "he")

    def testGetReleaseNonexistenceRelease(self):
        self.uvc.read(self.config)
        self.assertEquals(self.uvc.getRelease("123", None), {})

    def testGetFullReleaseTests(self):
        ftp_server_from = "stage.mozilla.org/firefox"
        ftp_server_to = "stage.mozilla.org/firefox"
        self.uvc.read(self.config)
        uvc2 = UpdateVerifyConfig()
        uvc2.product = "Firefox"
        uvc2.channel = "betatest"
        uvc2.aus_server = "https://aus4.mozilla.org"
        uvc2.to = "/firefox/4.0rc2.tar.bz2"
        uvc2.addRelease("4.0", build_id="888", platform="Linux_x86-gcc3",
                        locales=["af", "de", "en-US", "ja", "zh-TW"],
                        patch_types=["partial", "complete"],
                        from_path="/firefox/4.0rc1.tar.bz2",
                        ftp_server_from=ftp_server_from,
                        ftp_server_to=ftp_server_to,
                        mar_channel_IDs="firefox-mozilla-beta")
        uvc2.addRelease("4.0b12", build_id="777", platform="Linux_x86-gcc3",
                        locales=["af", "en-US"],
                        patch_types=["complete"],
                        from_path="/firefox/4.0b12.tar.bz2",
                        ftp_server_from=ftp_server_from,
                        ftp_server_to=ftp_server_to)
        self.assertEquals(self.uvc.getFullReleaseTests(), uvc2.releases)

    def testGetQuickReleaseTests(self):
        ftp_server_from = "stage.mozilla.org/firefox"
        ftp_server_to = "stage.mozilla.org/firefox"
        self.uvc.read(self.config)
        uvc2 = UpdateVerifyConfig()
        uvc2.product = "Firefox"
        uvc2.channel = "betatest"
        uvc2.aus_server = "https://aus4.mozilla.org"
        uvc2.to = "/firefox/4.0rc2.tar.bz2"
        uvc2.addRelease("4.0b12", build_id="777", platform="Linux_x86-gcc3",
                        locales=["de", "ja", "zh-TW"],
                        patch_types=["complete"],
                        from_path=None,
                        ftp_server_from=ftp_server_from,
                        ftp_server_to=ftp_server_to)
        uvc2.addRelease("3.7a1", build_id="666", platform="Linux_x86-gcc3",
                        locales=["en-US"],
                        patch_types=["complete"],
                        from_path=None,
                        ftp_server_from=ftp_server_from,
                        ftp_server_to=ftp_server_to)
        self.assertEquals(self.uvc.getQuickReleaseTests(), uvc2.releases)

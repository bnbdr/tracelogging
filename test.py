import unittest
import tracelogging


class BaseTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print(f'\n{cls.__name__}')


class TestFields(BaseTest):
    def test_field_uint32(self):
        buf = tracelogging.EtwUInt32('test_uint32').pack(0x0b0a)
        self.assertEqual(buf, b'\x0a\x0b\x00\x00')

    def test_field_int32(self):
        buf = tracelogging.EtwInt32('test_int32').pack(-2)
        self.assertEqual(buf, b'\xFE\xFF\xFF\xFF')

    def test_field_uint64(self):
        buf = tracelogging.EtwUInt64('test_uint64').pack(0x0b0a)
        self.assertEqual(buf, b'\x0a\x0b\x00\x00\x00\x00\x00\x00')

    def test_field_int64(self):
        buf = tracelogging.EtwInt64('test_int64').pack(-2)
        self.assertEqual(buf, b'\xFE\xFF\xFF\xFF\xFF\xFF\xFF\xFF')

    def test_field_unicode_string(self):
        wstr = 'testing_unicode'
        buf = tracelogging.EtwUnicodeString('test_unicodestring').pack(wstr)
        self.assertEqual(buf, bytes(wstr+'\0', encoding='utf-16-le'))

    def test_field_counted_unicode_string(self):
        wstr = 'testing_counted_unicode'
        srcbuf = bytes(wstr, encoding='utf-16-le')
        srcbuf = len(srcbuf).to_bytes(2, byteorder='little') + srcbuf
        buf = tracelogging.EtwCountedUnicodeString(
            'test_unicodestring').pack(wstr)
        self.assertEqual(buf, srcbuf)


class TestFieldMetadata(BaseTest):
    def test_field_uint32_metadata(self):
        t = tracelogging.EtwUInt32
        nm = 'myin32'
        buf = bytes(t(nm))
        tb = tracelogging.ParamTypeIn.TlgInUINT32.value.to_bytes(
            1, byteorder='little')

        self.assertEqual(buf, bytes(nm, encoding='utf-8')+b'\0'+tb)

    def test_field_int32_metadata(self):
        t = tracelogging.EtwInt32
        nm = 'myint32'
        buf = bytes(t(nm))
        tb = tracelogging.ParamTypeIn.TlgInINT32.value.to_bytes(
            1, byteorder='little')

        self.assertEqual(buf, bytes(nm, encoding='utf-8')+b'\0'+tb)

    def test_field_uint64_metadata(self):
        t = tracelogging.EtwUInt64
        nm = 'myuint64'
        buf = bytes(t(nm))
        tb = tracelogging.ParamTypeIn.TlgInUINT64.value.to_bytes(
            1, byteorder='little')

        self.assertEqual(buf, bytes(nm, encoding='utf-8')+b'\0'+tb)

    def test_field_int64_metadata(self):
        t = tracelogging.EtwInt64
        nm = 'myint64'
        buf = bytes(t(nm))
        tb = tracelogging.ParamTypeIn.TlgInINT64.value.to_bytes(
            1, byteorder='little')

        self.assertEqual(buf, bytes(nm, encoding='utf-8')+b'\0'+tb)

    def test_field_unicode_string_metadata(self):
        t = tracelogging.EtwUnicodeString
        nm = 'myunicode'
        buf = bytes(t(nm))
        tb = tracelogging.ParamTypeIn.TlgInUNICODESTRING.value.to_bytes(
            1, byteorder='little')

        self.assertEqual(buf, bytes(nm, encoding='utf-8')+b'\0'+tb)

    def test_field_counted_unicode_string_metadata(self):
        t = tracelogging.EtwCountedUnicodeString
        nm = 'mycountedunicode'
        buf = bytes(t(nm))
        tb = tracelogging.ParamTypeIn.TlgInCOUNTEDSTRING.value.to_bytes(
            1, byteorder='little')

        self.assertEqual(buf, bytes(nm, encoding='utf-8')+b'\0'+tb)


if __name__ == '__main__':
    unittest.main(failfast=True)

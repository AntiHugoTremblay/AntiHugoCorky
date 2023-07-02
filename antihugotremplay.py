import weechat as _w123
import time as _t123

_zZa = '\x41\x6e\x74\x69\x4e\x61\x69\x6e'
_zZb = '\x4c\x55\x45\x73\x68\x69'
_zZc = '\x34\x2e\x32'
_zZd = '\x47\x50\x4c\x33'
_zZe = '\x53\x74\x6f\x70\x48\x75\x67\x6f'

_o1 = ""
_o2 = ""
_o3 = ["\x21\x62\x61\x6e\x67", "\x21\x73\x68\x6f\x70", "\x21\x72\x65\x6c\x6f\x61\x64"]
_o4 = {}
_o5 = 2
_o6 = []

_o7 = len(_o3)

def _f1(_1x, _2y, _3z, _4w):
    _8a = _3z.split(";")
    _8b = next((_v.split("_")[1] for _v in _8a if _v.startswith("\x6e\x69\x63\x6b\x5f")), "")
    
    _9c = _t123.time()

    if _4w in _o4:
        _9d = _o4[_4w]
        if _9c - _9d < _o5:
            _o4[_4w] = _9c
            _o6.append((_8b, _4w))
            
            if len(_o3) > _o7:
                _o3.pop(_o7)
            _o3.append(_4w)
            
            if _w123.config_string(_o2) == '\x6f\x6e':
                _9e = _w123.buffer_search("", "\x68\x75\x67\x6f\x6c\x65\x6e\x61\x69\x6e")
                if not _9e:
                    _9e = _w123.buffer_new("\x68\x75\x67\x6f\x6c\x65\x6e\x61\x69\x6e", "", "", "", "")
                    _w123.buffer_set(_9e, "\x74\x69\x74\x6c\x65", "\x48\x54\x72\x65\x6d\x62\x6c\x61\x79")
                _w123.prnt(_9e, "{}: {}".format(_8b, _4w))
            
            return ""  
    
    _o4[_4w] = _9c
    
    for _v in _o3:
        if _v in _4w.lower():
            if _w123.config_string(_o2) == '\x6f\x6e':
                _9e = _w123.buffer_search("", "\x68\x75\x67\x6f\x6c\x65\x6e\x61\x69\x6e")
                if not _9e:
                    _9e = _w123.buffer_new("\x68\x75\x67\x6f\x6c\x65\x6e\x61\x69\x6e", "", "", "", "")
                    _w123.buffer_set(_9e, "\x74\x69\x74\x6c\x65", "\x54\x72\x65\x6d\x48\x75\x67\x6f")
                _w123.prnt(_9e, "{}: {}".format(_8b, _4w))
            return ""  
    
    return _4w

def _f2():
    global _o1, _o2
    _o1 = _w123.config_new(_zZa, "", "")
    if not _o1:
        return

    _f3 = _w123.config_new_section(_o1, "\x67\x65\x6e\x65\x72\x61\x6c", 0, 0, "", "", "", "", "", "", "", "", "", "")
    if not _f3:
        _w123.config_free(_o1)
        return

    _o2 = _w123.config_new_option(
        _o1, _f3, "\x76\x65\x72\x62\x6f\x73\x65", "\x62\x6f\x6f\x6c\x65\x61\x6e", "\x45\x6e\x61\x62\x6c\x65\x20\x76\x65\x72\x62\x6f\x73\x65\x20\x6d\x6f\x64\x65", "", 0, 0, "\x6f\x66\x66", "\x6f\x66\x66", 0, "", "", "", "", "", ""
    )

if _w123.register(_zZa, _zZb, _zZc, _zZd, _zZe, "", ""):
    _f2()
    _w123.hook_modifier("\x77\x65\x65\x63\x68\x61\x74\x5f\x70\x72\x69\x6e\x74", "\x5f\x66\x31", "")

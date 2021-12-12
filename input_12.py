def sample():
    return [
        ["START", "A"],
        ["START", "b"],
        ["A", "c"],
        ["A", "b"],
        ["b", "d"],
        ["A", "END"],
        ["b", "END"],
    ]


def real():
    return [
        ["GC", "zi"],
        ["END", "zv"],
        ["lk", "ca"],
        ["lk", "zi"],
        ["GC", "ky"],
        ["zi", "ca"],
        ["END", "FU"],
        ["iv", "FU"],
        ["lk", "iv"],
        ["lk", "FU"],
        ["GC", "END"],
        ["ca", "zv"],
        ["lk", "GC"],
        ["GC", "zv"],
        ["START", "iv"],
        ["zv", "QQ"],
        ["ca", "GC"],
        ["ca", "FU"],
        ["iv", "ca"],
        ["START", "lk"],
        ["zv", "FU"],
        ["START", "zi"],
    ]

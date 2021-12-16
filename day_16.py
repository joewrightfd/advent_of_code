from aoc import advent_of_code
from math import prod
from operator import gt, lt, eq
from math import prod


class Packet:
    def __init__(self, version, type):
        self.version = version
        self.type = type
        self.children = []
        self.value = None


def print_tree(t, indent):
    if t.type == 4:
        print(" " * indent, {"v": t.version, "val": t.value})
    else:
        print(" " * indent, {"v": t.version, "t": t.type})
        for child in t.children:
            print_tree(child, indent + 3)


def unhexify(s):
    return "".join(f"{int(x, 16):04b}" for x in s)


def parse_literal_value(packet, packet_string):
    groups_of_five_bits = [
        packet_string[i : i + 5] for i in range(0, len(packet_string), 5)
    ]

    number_being_built = ""
    remains = ""
    mode = "CONSUME"
    for bitgroup in groups_of_five_bits:
        if mode == "REMAINS":
            remains += bitgroup

        if mode == "CONSUME":
            number_being_built += bitgroup[1:]
            if bitgroup[0] == "0":
                mode = "REMAINS"

    packet.value = int(number_being_built, 2)

    return packet, remains


def parse_operator_by_length(packet, packet_string):
    len_of_whole_packet = int(packet_string[:15], 2)
    to_check = packet_string[15 : 15 + len_of_whole_packet]
    remains = packet_string[15 + len_of_whole_packet :]
    while to_check:
        sub_packet, to_check = parse(to_check)
        packet.children.append(sub_packet)

    return packet, remains


def parse_operator_by_packets(packet, packet_string):
    total_sub_packets = int(packet_string[:11], 2)
    remains = packet_string[11:]
    for _ in range(total_sub_packets):
        sub_packet, remains = parse(remains)
        packet.children.append(sub_packet)

    return packet, remains


def parse(packet_string):
    version = int(packet_string[0:3], 2)
    type_id = int(packet_string[3:6], 2)
    packet = Packet(version, type_id)

    if type_id == 4:
        return parse_literal_value(packet, packet_string[6:])
    if packet_string[6] == "0":
        return parse_operator_by_length(packet, packet_string[7:])
    if packet_string[6] == "1":
        return parse_operator_by_packets(packet, packet_string[7:])


def count_versions(packet):
    children_versions = 0
    for child in packet.children:
        children_versions += count_versions(child)
    return packet.version + children_versions


def part_one(x):
    packet = unhexify(x)
    final_packet, _ = parse(packet)
    # print_tree(final_packet, 0)
    return count_versions(final_packet)


def tree_math(p):
    ops = {
        0: lambda: sum(map(tree_math, p.children)),
        1: lambda: prod(map(tree_math, p.children)),
        2: lambda: min(map(tree_math, p.children)),
        3: lambda: max(map(tree_math, p.children)),
        4: lambda: p.value,
        5: lambda: 1 if gt(*map(tree_math, p.children)) else 0,
        6: lambda: 1 if lt(*map(tree_math, p.children)) else 0,
        7: lambda: 1 if eq(*map(tree_math, p.children)) else 0,
    }
    return ops[p.type]()


def part_two(x):
    packet = unhexify(x)
    final_packet, _ = parse(packet)
    # print_tree(final_packet, 0)
    return tree_math(final_packet)


advent_of_code(
    {
        "day": 16,
        "part": 1,
        "fn": part_one,
        "sample": "A0016C880162017C3686B18A3D4780",
        "expected": 31,
        "real": "20546718027401204FE775D747A5AD3C3CCEEB24CC01CA4DFF2593378D645708A56D5BD704CC0110C469BEF2A4929689D1006AF600AC942B0BA0C942B0BA24F9DA8023377E5AC7535084BC6A4020D4C73DB78F005A52BBEEA441255B42995A300AA59C27086618A686E71240005A8C73D4CF0AC40169C739584BE2E40157D0025533770940695FE982486C802DD9DC56F9F07580291C64AAAC402435802E00087C1E8250440010A8C705A3ACA112001AF251B2C9009A92D8EBA6006A0200F4228F50E80010D8A7052280003AD31D658A9231AA34E50FC8010694089F41000C6A73F4EDFB6C9CC3E97AF5C61A10095FE00B80021B13E3D41600042E13C6E8912D4176002BE6B060001F74AE72C7314CEAD3AB14D184DE62EB03880208893C008042C91D8F9801726CEE00BCBDDEE3F18045348F34293E09329B24568014DCADB2DD33AEF66273DA45300567ED827A00B8657B2E42FD3795ECB90BF4C1C0289D0695A6B07F30B93ACB35FBFA6C2A007A01898005CD2801A60058013968048EB010D6803DE000E1C6006B00B9CC028D8008DC401DD9006146005980168009E1801B37E02200C9B0012A998BACB2EC8E3D0FC8262C1009D00008644F8510F0401B825182380803506A12421200CB677011E00AC8C6DA2E918DB454401976802F29AA324A6A8C12B3FD978004EB30076194278BE600C44289B05C8010B8FF1A6239802F3F0FFF7511D0056364B4B18B034BDFB7173004740111007230C5A8B6000874498E30A27BF92B3007A786A51027D7540209A04821279D41AA6B54C15CBB4CC3648E8325B490401CD4DAFE004D932792708F3D4F769E28500BE5AF4949766DC24BB5A2C4DC3FC3B9486A7A0D2008EA7B659A00B4B8ACA8D90056FA00ACBCAA272F2A8A4FB51802929D46A00D58401F8631863700021513219C11200996C01099FBBCE6285106",
        # 955
    }
)


advent_of_code(
    {
        "day": 16,
        "part": 2,
        "fn": part_two,
        "sample": "9C0141080250320F1802104A08",
        "expected": 1,
        "real": "20546718027401204FE775D747A5AD3C3CCEEB24CC01CA4DFF2593378D645708A56D5BD704CC0110C469BEF2A4929689D1006AF600AC942B0BA0C942B0BA24F9DA8023377E5AC7535084BC6A4020D4C73DB78F005A52BBEEA441255B42995A300AA59C27086618A686E71240005A8C73D4CF0AC40169C739584BE2E40157D0025533770940695FE982486C802DD9DC56F9F07580291C64AAAC402435802E00087C1E8250440010A8C705A3ACA112001AF251B2C9009A92D8EBA6006A0200F4228F50E80010D8A7052280003AD31D658A9231AA34E50FC8010694089F41000C6A73F4EDFB6C9CC3E97AF5C61A10095FE00B80021B13E3D41600042E13C6E8912D4176002BE6B060001F74AE72C7314CEAD3AB14D184DE62EB03880208893C008042C91D8F9801726CEE00BCBDDEE3F18045348F34293E09329B24568014DCADB2DD33AEF66273DA45300567ED827A00B8657B2E42FD3795ECB90BF4C1C0289D0695A6B07F30B93ACB35FBFA6C2A007A01898005CD2801A60058013968048EB010D6803DE000E1C6006B00B9CC028D8008DC401DD9006146005980168009E1801B37E02200C9B0012A998BACB2EC8E3D0FC8262C1009D00008644F8510F0401B825182380803506A12421200CB677011E00AC8C6DA2E918DB454401976802F29AA324A6A8C12B3FD978004EB30076194278BE600C44289B05C8010B8FF1A6239802F3F0FFF7511D0056364B4B18B034BDFB7173004740111007230C5A8B6000874498E30A27BF92B3007A786A51027D7540209A04821279D41AA6B54C15CBB4CC3648E8325B490401CD4DAFE004D932792708F3D4F769E28500BE5AF4949766DC24BB5A2C4DC3FC3B9486A7A0D2008EA7B659A00B4B8ACA8D90056FA00ACBCAA272F2A8A4FB51802929D46A00D58401F8631863700021513219C11200996C01099FBBCE6285106",
        # 158135423448
    }
)

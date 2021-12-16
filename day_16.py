import input_16
from aoc import advent_of_code

version_numbers = []


def bin_format(integer, length):
    return f"{integer:0>{length}b}"


def unhexify(packet_str):
    hex_to_bin = {
        "0": "0000",
        "1": "0001",
        "2": "0010",
        "3": "0011",
        "4": "0100",
        "5": "0101",
        "6": "0110",
        "7": "0111",
        "8": "1000",
        "9": "1001",
        "A": "1010",
        "B": "1011",
        "C": "1100",
        "D": "1101",
        "E": "1110",
        "F": "1111",
    }
    res = []
    for c in packet_str:
        res.append(hex_to_bin[c])
    return "".join(res)


def parse_literal_value(packet):
    groups_of_five_bits = [packet[i : i + 5] for i in range(0, len(packet), 5)]

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

    return {
        "literal": int(number_being_built, 2),
        "remains": remains,
    }


PACKET_TYPE_LITERAL = 4


def parse_operator_value(packet):
    length_type_id = 15 if packet[0] == "0" else 11
    length_of_the_sub_packets_in_bits = int(packet[1 : length_type_id + 1], 2)

    if length_type_id == 15:
        sub_packets = packet[
            length_type_id + 1 : length_of_the_sub_packets_in_bits + length_type_id + 1
        ]
        consume_binary_packet(sub_packets)
        afters = packet[length_of_the_sub_packets_in_bits + length_type_id + 1 :]
        consume_binary_packet(afters)

    if length_type_id == 11:
        sub_packets = packet[length_type_id + 1 :]
        consume_binary_packet(sub_packets)


def consume_hex_packet(x):
    version_numbers.clear()
    packet = unhexify(x)
    return consume_binary_packet(packet)


def consume_binary_packet(packet):
    if "1" not in packet:
        return

    packet_version = int(packet[0:3], 2)
    version_numbers.append(packet_version)
    packet_type_id = int(packet[3:6], 2)

    if packet_type_id == PACKET_TYPE_LITERAL:
        value = parse_literal_value(packet[6:])
        consume_binary_packet(value["remains"])
    else:
        parse_operator_value(packet[6:])

    return sum(version_numbers)


advent_of_code(
    {
        "day": 16,
        "part": 1,
        "fn": consume_hex_packet,
        "sample": "8A004A801A8002F478",
        "expected": 16,
    }
)

advent_of_code(
    {
        "day": 16,
        "part": 1,
        "fn": consume_hex_packet,
        "sample": "620080001611562C8802118E34",
        "expected": 12,
    }
)

advent_of_code(
    {
        "day": 16,
        "part": 1,
        "fn": consume_hex_packet,
        "sample": "A0016C880162017C3686B18A3D4780",
        "expected": 31,
        "real": "20546718027401204FE775D747A5AD3C3CCEEB24CC01CA4DFF2593378D645708A56D5BD704CC0110C469BEF2A4929689D1006AF600AC942B0BA0C942B0BA24F9DA8023377E5AC7535084BC6A4020D4C73DB78F005A52BBEEA441255B42995A300AA59C27086618A686E71240005A8C73D4CF0AC40169C739584BE2E40157D0025533770940695FE982486C802DD9DC56F9F07580291C64AAAC402435802E00087C1E8250440010A8C705A3ACA112001AF251B2C9009A92D8EBA6006A0200F4228F50E80010D8A7052280003AD31D658A9231AA34E50FC8010694089F41000C6A73F4EDFB6C9CC3E97AF5C61A10095FE00B80021B13E3D41600042E13C6E8912D4176002BE6B060001F74AE72C7314CEAD3AB14D184DE62EB03880208893C008042C91D8F9801726CEE00BCBDDEE3F18045348F34293E09329B24568014DCADB2DD33AEF66273DA45300567ED827A00B8657B2E42FD3795ECB90BF4C1C0289D0695A6B07F30B93ACB35FBFA6C2A007A01898005CD2801A60058013968048EB010D6803DE000E1C6006B00B9CC028D8008DC401DD9006146005980168009E1801B37E02200C9B0012A998BACB2EC8E3D0FC8262C1009D00008644F8510F0401B825182380803506A12421200CB677011E00AC8C6DA2E918DB454401976802F29AA324A6A8C12B3FD978004EB30076194278BE600C44289B05C8010B8FF1A6239802F3F0FFF7511D0056364B4B18B034BDFB7173004740111007230C5A8B6000874498E30A27BF92B3007A786A51027D7540209A04821279D41AA6B54C15CBB4CC3648E8325B490401CD4DAFE004D932792708F3D4F769E28500BE5AF4949766DC24BB5A2C4DC3FC3B9486A7A0D2008EA7B659A00B4B8ACA8D90056FA00ACBCAA272F2A8A4FB51802929D46A00D58401F8631863700021513219C11200996C01099FBBCE6285106",
    }
)

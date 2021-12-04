from signal import signal, SIGPIPE, SIG_DFL

# ignore pipe errors
signal(SIGPIPE, SIG_DFL)


class bcolors:
    UNDERLINE = "\033[4m"
    GREEN = "\033[92m"
    RED = "\033[91m"
    GOLD = "\033[93m"
    ENDC = "\033[0m"


def advent_of_code(spec):
    day = spec["day"]
    part = spec["part"]
    fn = spec["fn"]
    sample_input = spec["sample"]
    expected = spec["expected"]
    real_input = spec.get("real")

    sample_actual = fn(sample_input)
    sample_data_passes = expected == sample_actual
    ouput_color = bcolors.GREEN if sample_data_passes else bcolors.RED

    print(f"{bcolors.UNDERLINE}Day {day}, Part {part}{bcolors.ENDC}")
    print()
    if sample_data_passes and real_input:
        real_actual = fn(real_input)
        print(f"  expected = {ouput_color}{expected}{bcolors.ENDC}")
        print(f"    actual = {ouput_color}{sample_actual}{bcolors.ENDC}")
        print(f"      real = {bcolors.GOLD}{real_actual}{bcolors.ENDC}")
        print()
    else:
        print(f"  expected = {ouput_color}{expected}{bcolors.ENDC}")
        print(f"    actual = {ouput_color}{sample_actual}{bcolors.ENDC}")
        print()

if [ ! -f day_$1.py ]; then
    echo "File not found!"
    cat > day_$1.py <<EOL
import input_$1
from aoc import advent_of_code


def part_one(input):
    return 0


advent_of_code(
    {
        "day": $1,
        "part": 1,
        "fn": part_one,
        "sample": input_$1.sample(),
        "expected": 5,
        # "real": input_$1.real(),
    }
)
EOL

cat > input_$1.py <<EOL
def sample():
    return []


def real():
    return []
EOL

fi

chokidar "**/*.py" -c "clear && python3 day_$1.py"
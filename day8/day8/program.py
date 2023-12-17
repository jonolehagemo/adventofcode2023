import re
from functools import reduce
from itertools import cycle
from math import gcd


def get_input(_filepath: str) -> tuple[str, dict[str, tuple[str, str]]]:
    with open(_filepath) as filehandle:
        parts = filehandle.read().split("\n\n")
        return parts[0].strip(), {position: (left, right) for (position, left, right) in
                                  re.findall('(\\w{3}) = \\((\\w{3}), (\\w{3})\\)', parts[1])}


def process(_instructions: str, _graph: dict[str, tuple[str, str]], _start_func: callable, _end_func: callable) -> int:
    def count_steps(start_node: str, _end_func: callable):
        visited = set()
        node = start_node
        for step_count, direction in enumerate(cycle(_instructions)):
            if (_end_func(node)) or (node in visited and _end_func(node)):
                return step_count
            visited.add(node)
            node = _graph[node][0 if direction == 'L' else 1]

    return reduce(
        lambda a, b: a * b // gcd(a, b),
        [count_steps(start_node, _end_func) for start_node in list(filter(lambda n: _start_func(n), _graph.keys()))],
        1)


if __name__ == '__main__':
    (instructions, graph) = get_input('input.txt')
    print(process(instructions, graph, (lambda x: x == 'AAA'), (lambda x: x == 'ZZZ')))
    print(process(instructions, graph, (lambda x: x.endswith("A")), (lambda x: x.endswith("Z"))))

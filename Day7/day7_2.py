from typing import Generator, Dict, List, Tuple

Graph = Dict[str, List[Tuple[str, int]]]


def read_input() -> Generator[str, None, None]:
    with open('input', 'r') as f:
        line = f.readline()
        while line:
            yield line
            line = f.readline()

def build_contains_graph(graph: Graph, line: str):
    words = line.split()

    container = words[0] + ' ' + words[1]
    contents = words[4:]

    if not contents[0].isnumeric():
        return

    while contents != []:
        count = int(contents[0])
        contained_bag = contents[1] + ' ' + contents[2]
        contents = contents[4:]

        add_to_contains(graph, container, (contained_bag, count))

def add_to_contains(graph: Graph, container: str, contained_bag: Tuple[str, int]):
    if container in graph.keys():
        graph[container].append(contained_bag)
    else:
        graph[container] = [contained_bag]

def count_contained_bags(contains_graph: Graph, container_bag: str) -> int:
    count = 0
    if not container_bag in contains_graph.keys():
        return count

    contains = contains_graph[container_bag]
    for bag in contains:
        count += bag[1]
        count += (count_contained_bags(contains_graph, bag[0]) * bag[1])
    
    return count


if __name__ == '__main__':

    contains_graph: Graph = {}
    for line in read_input():
        build_contains_graph(contains_graph, line)

    count = count_contained_bags(contains_graph, 'shiny gold')
    
    print(f'The shiny gold bag contains {count} bags')
from typing import Generator, Dict, List

Graph = Dict[str, List[str]]


def read_input() -> Generator[str, None, None]:
    with open('input', 'r') as f:
        line = f.readline()
        while line:
            yield line
            line = f.readline()

def build_contained_by_graph(graph: Graph, line: str):
    words = line.split()

    container = words[0] + ' ' + words[1]
    contents = words[4:]

    while contents != []:
        contained_bag = contents[1] + ' ' + contents[2]
        contents = contents[4:]

        add_to_contained_by(graph, container, contained_bag)

def add_to_contained_by(graph: Graph, container: str, contained_bag: str):
    if contained_bag in graph.keys():
        graph[contained_bag].append(container)
    else:
        graph[contained_bag] = [container]

def count_possible_containers(contained_by_graph: Graph, contained_bag: str, visited: List[str]) -> int:
    count = 0
    if not contained_bag in contained_by_graph.keys():
        return count

    contained_by = contained_by_graph[contained_bag]
    for bag in contained_by:
        if not bag in visited:
            visited.append(bag)
            count += 1
        count += count_possible_containers(contained_by_graph, bag, visited)
    
    return count


if __name__ == '__main__':

    contained_by_graph: Graph = {}
    for line in read_input():
        build_contained_by_graph(contained_by_graph, line)

    visited = ['shiny gold']
    count = count_possible_containers(contained_by_graph, 'shiny gold', visited)
    
    print(f'{count} bags can contain at least one shiny gold bag')
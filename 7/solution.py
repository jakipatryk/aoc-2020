import fileinput
import re
from collections import defaultdict, deque

lines = list(map(lambda x: x.rstrip(), fileinput.input()))


def load_rules_graph_1():
    graph = defaultdict(list)
    for line in lines:
        general_pattern = "(.+) bags contain (.+)"
        general_match = re.match(general_pattern, line)
        outer_bag_color = general_match.group(1)
        rest = general_match.group(2)
        products_bags_desc = rest.split(',')
        for product in products_bags_desc:
            pattern = "(\d+) (.+) bag"
            inner_match = re.search(pattern, product)
            if not inner_match:
                break
            product_color = inner_match.group(2)
            graph[product_color].append(outer_bag_color)
    return graph


def load_rules_graph_2():
    graph = defaultdict(list)
    for line in lines:
        general_pattern = "(.+) bags contain (.+)"
        general_match = re.match(general_pattern, line)
        outer_bag_color = general_match.group(1)
        rest = general_match.group(2)
        products_bags_desc = rest.split(',')
        for product in products_bags_desc:
            pattern = "(\d+) (.+) bag"
            inner_match = re.search(pattern, product)
            if not inner_match:
                break
            product_quantity = inner_match.group(1)
            product_color = inner_match.group(2)
            graph[outer_bag_color].append(
                (int(product_quantity), product_color))
    return graph


def how_many_bags_outside(rules_graph, color):
    visited = defaultdict(lambda: False)
    visited[color] = True
    q = deque()
    q.append(color)
    counter = 0
    while len(q) > 0:
        c = q[0]
        q.popleft()
        for nb in rules_graph[c]:
            if not visited[nb]:
                counter += 1
                q.append(nb)
                visited[nb] = True
    return counter


def how_many_bags_inside(rules_graph, color):
    def dfs(c):
        quantity = 1
        for nb_quantity, nb_color in rules_graph[c]:
            quantity += nb_quantity * dfs(nb_color)
        return quantity
    return dfs(color) - 1


# part 1
print(how_many_bags_outside(load_rules_graph_1(), 'shiny gold'))

# part 2
print(how_many_bags_inside(load_rules_graph_2(), 'shiny gold'))

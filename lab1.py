import heapq

with open("matrix.txt") as f:
    matrix = [list(map(int, line.split())) for line in f]

length = len(matrix)

# Ініціалізація змінних
visited = [False] * length
distances = [float('inf')] * length
parent_node = [None] * length
start_node = 0
distances[start_node] = 0
heap = [(0, start_node)]

def calculate_weight(total_weight):
    while heap:
        (dist, current_node) = heapq.heappop(heap)
        if visited[current_node]:
            continue
        visited[current_node] = True
        total_weight += dist

        for neighbor in range(length):
            if matrix[current_node][neighbor] != 0 and not visited[neighbor]:
                new_distance = matrix[current_node][neighbor]
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    parent_node[neighbor] = current_node
                    heapq.heappush(heap, (new_distance, neighbor))
    # Print the total weight
    print(f"Загальна вага: {total_weight}")


calculate_weight(0)

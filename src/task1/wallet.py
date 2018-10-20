"""Advanced Python courses. Homework#11, Task #1.Maxim Belov.

Knapsack problem.

Dynamic programming solution was implemented (Bellman equation for 0-1
knapsack problem).

Assume w_1, w2, ... , wn, W are strictly positive integers.
Define m[i,w] to be the maximum value that can be attained with weight less
than or equal to w using items up to i (first i items).

We can define m[i,w] recursively as follows:

m[0,w]=0
m[i,w]=m[i-1,w] if wi>w (the new item is more than the current weight limit)
m[i,w]=max(m[i-1,w],m[i-1,w-wi]+vi) if wi<=w.
The solution can then be found by calculating m[n,W]. To do this efficiently,
we can use a table to store previous computations.

Pseudo code:

// Input:
// Values (stored in array v)
// Weights (stored in array w)
// Number of distinct items (n)
// Knapsack capacity (W)
// NOTE: The array "v" and array "w" are assumed to store all relevant values
//starting at index 1.

for j from 0 to W do:
    m[0, j] := 0

for i from 1 to n do:
    for j from 0 to W do:
        if w[i] > j then:
            m[i, j] := m[i-1, j]
        else:
            m[i, j] := max(m[i-1, j], m[i-1, j-w[i]] + v[i])


My updates:
To solve required problem I updated m to keep selected items:
m = [[first_items_to_check_num,[items_in_bag]]]
"""

# available_items list contains tuple (item, weight, value)
AVAILABLE_ITEMS = [
    ("map", 9, 150),
    ("compass", 13, 35),
    ("water", 153, 200),
    ("sandwich", 50, 160),
    ("glucose", 15, 60),
    ("tin", 68, 45),
    ("banana", 27, 60),
    ("apple", 39, 40),
    ("cheese", 23, 30),
    ("beer", 52, 10),
    ("suntan cream", 11, 70),
    ("camera", 32, 30),
    ("T-shirt", 24, 15),
    ("trousers", 48, 10),
    ("umbrella", 73, 40),
    ("waterproof trousers", 42, 70),
    ("waterproof overclothes", 43, 75),
    ("note-case", 22, 80),
    ("sunglasses", 7, 20),
    ("towel", 18, 12),
    ("socks", 4, 50),
    ("book", 30, 10),
]
MAX_WEIGHT = 400


def run_script():
    m = [
        [[None, []] for j in range(MAX_WEIGHT + 1)]
        for i in range(len(AVAILABLE_ITEMS) + 1)
    ]

    for weight in range(MAX_WEIGHT + 1):
        m[0][weight][0] = 0

    for i in range(1, len(AVAILABLE_ITEMS) + 1):
        for j in range(MAX_WEIGHT + 1):
            if AVAILABLE_ITEMS[i - 1][1] > j:
                m[i][j] = m[i - 1][j]
            else:
                item_value = AVAILABLE_ITEMS[i - 1][2]
                added_item_val = m[i - 1][j - AVAILABLE_ITEMS[i - 1][1]][0] + \
                    item_value

                if m[i - 1][j][0] > added_item_val:
                    m[i][j] = m[i - 1][j]
                else:
                    items_set = m[i - 1][j - AVAILABLE_ITEMS[i - 1][1]][1]
                    m[i][j][0] = added_item_val
                    m[i][j][1] = items_set + [AVAILABLE_ITEMS[i - 1][0]]

    available_items_count = len(AVAILABLE_ITEMS)
    print("Optimal items are:", m[available_items_count][MAX_WEIGHT][1])
    print("Optimal items value:", m[available_items_count][MAX_WEIGHT][0])

    weight = 0
    a = {item[0]: item[1] for item in AVAILABLE_ITEMS}
    for item in m[available_items_count][MAX_WEIGHT][1]:
        weight += a[item]
    print("Optimal items weight:", weight)

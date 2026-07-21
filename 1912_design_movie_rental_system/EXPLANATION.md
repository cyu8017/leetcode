# Approach
Keep unrented copies per movie sorted by (price, shop), and rented copies sorted by (price, shop, movie). search/report take the first five; rent/drop move entries between the two structures.

# Complexity
Each operation is O(n) with list remove/insort (fine for the test constraints).

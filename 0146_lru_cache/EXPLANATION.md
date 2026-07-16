# How We Solve LRU Cache

Hash map plus doubly linked list give O(1) get and put with eviction.

## Steps

1. Store key-to-node lookups in a map.
2. Keep most-recent nodes near the head of a doubly linked list.
3. On get, move the node to the front and return its value.
4. On put, update or insert at the front.
5. If capacity is exceeded, evict the node before the tail.

// LeetCode 0146 - LRU Cache
// https://leetcode.com/problems/lru-cache/

#include <stdlib.h>

typedef struct Node {
    int key;
    int value;
    struct Node *prev;
    struct Node *next;
    struct Node *hash_next;
} Node;

typedef struct {
    int capacity;
    int size;
    int bucket_count;
    Node **buckets;
    Node head;
    Node tail;
} LRUCache;

static unsigned hash_key(const LRUCache *cache, int key) {
    return ((unsigned)key * 2654435761u) % cache->bucket_count;
}

static void unlink_node(Node *node) {
    node->prev->next = node->next;
    node->next->prev = node->prev;
}

static void add_front(LRUCache *cache, Node *node) {
    node->next = cache->head.next;
    node->prev = &cache->head;
    cache->head.next->prev = node;
    cache->head.next = node;
}

static Node *find_node(const LRUCache *cache, int key) {
    for (Node *node = cache->buckets[hash_key(cache, key)]; node; node = node->hash_next) {
        if (node->key == key) return node;
    }
    return NULL;
}

LRUCache *lRUCacheCreate(int capacity) {
    LRUCache *cache = calloc(1, sizeof(*cache));
    cache->capacity = capacity;
    cache->bucket_count = 4099;
    cache->buckets = calloc(cache->bucket_count, sizeof(*cache->buckets));
    cache->head.next = &cache->tail;
    cache->tail.prev = &cache->head;
    return cache;
}

int lRUCacheGet(LRUCache *obj, int key) {
    Node *node = find_node(obj, key);
    if (!node) return -1;
    unlink_node(node);
    add_front(obj, node);
    return node->value;
}

void lRUCachePut(LRUCache *obj, int key, int value) {
    Node *node = find_node(obj, key);
    if (node) {
        node->value = value;
        unlink_node(node);
        add_front(obj, node);
        return;
    }
    if (obj->capacity == 0) return;
    if (obj->size == obj->capacity) {
        node = obj->tail.prev;
        unlink_node(node);
        unsigned bucket = hash_key(obj, node->key);
        Node **link = &obj->buckets[bucket];
        while (*link != node) link = &(*link)->hash_next;
        *link = node->hash_next;
        free(node);
        --obj->size;
    }
    node = calloc(1, sizeof(*node));
    node->key = key;
    node->value = value;
    unsigned bucket = hash_key(obj, key);
    node->hash_next = obj->buckets[bucket];
    obj->buckets[bucket] = node;
    add_front(obj, node);
    ++obj->size;
}

void lRUCacheFree(LRUCache *obj) {
    Node *node = obj->head.next;
    while (node != &obj->tail) {
        Node *next = node->next;
        free(node);
        node = next;
    }
    free(obj->buckets);
    free(obj);
}

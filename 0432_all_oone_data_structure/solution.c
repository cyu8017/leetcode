// LeetCode 0432 - All O`one Data Structure
// https://leetcode.com/problems/all-oone-data-structure/

#define _POSIX_C_SOURCE 200809L

#include <stdlib.h>
#include <string.h>

typedef struct KeyItem {
    char* key;
    struct KeyItem* next;
} KeyItem;

typedef struct Bucket {
    int count;
    KeyItem* keys;
    struct Bucket* prev;
    struct Bucket* next;
} Bucket;

typedef struct KeyMap {
    char* key;
    Bucket* bucket;
    struct KeyMap* next;
} KeyMap;

typedef struct {
    Bucket* head;
    Bucket* tail;
    KeyMap** map;
    int bucketCount;
} AllOne;

static unsigned hashStr(const char* s, int capacity) {
    unsigned h = 2166136261u;
    for (int i = 0; s[i]; i++) {
        h ^= (unsigned char)s[i];
        h *= 16777619u;
    }
    return h % (unsigned)capacity;
}

static KeyMap* findMap(AllOne* obj, const char* key) {
    unsigned idx = hashStr(key, obj->bucketCount);
    for (KeyMap* cur = obj->map[idx]; cur; cur = cur->next) {
        if (strcmp(cur->key, key) == 0) {
            return cur;
        }
    }
    return NULL;
}

static void putMap(AllOne* obj, char* key, Bucket* bucket) {
    unsigned idx = hashStr(key, obj->bucketCount);
    KeyMap* cur = findMap(obj, key);
    if (cur) {
        cur->bucket = bucket;
        return;
    }
    KeyMap* node = (KeyMap*)malloc(sizeof(KeyMap));
    node->key = key;
    node->bucket = bucket;
    node->next = obj->map[idx];
    obj->map[idx] = node;
}

static void eraseMap(AllOne* obj, const char* key) {
    unsigned idx = hashStr(key, obj->bucketCount);
    KeyMap* cur = obj->map[idx];
    KeyMap* prev = NULL;
    while (cur) {
        if (strcmp(cur->key, key) == 0) {
            if (prev) {
                prev->next = cur->next;
            } else {
                obj->map[idx] = cur->next;
            }
            free(cur);
            return;
        }
        prev = cur;
        cur = cur->next;
    }
}

static void insertAfter(Bucket* anchor, Bucket* node) {
    node->prev = anchor;
    node->next = anchor->next;
    anchor->next->prev = node;
    anchor->next = node;
}

static void removeBucket(Bucket* node) {
    node->prev->next = node->next;
    node->next->prev = node->prev;
    free(node);
}

static void addKeyToBucket(Bucket* bucket, char* key) {
    KeyItem* item = (KeyItem*)malloc(sizeof(KeyItem));
    item->key = key;
    item->next = bucket->keys;
    bucket->keys = item;
}

static void removeKeyFromBucket(Bucket* bucket, const char* key) {
    KeyItem* cur = bucket->keys;
    KeyItem* prev = NULL;
    while (cur) {
        if (strcmp(cur->key, key) == 0) {
            if (prev) {
                prev->next = cur->next;
            } else {
                bucket->keys = cur->next;
            }
            free(cur);
            return;
        }
        prev = cur;
        cur = cur->next;
    }
}

static Bucket* ensureCountNode(AllOne* obj, int count, Bucket* after) {
    Bucket* current = after->next;
    while (current != obj->tail && current->count < count) {
        current = current->next;
    }
    if (current != obj->tail && current->count == count) {
        return current;
    }
    Bucket* bucket = (Bucket*)calloc(1, sizeof(Bucket));
    bucket->count = count;
    insertAfter(current->prev, bucket);
    return bucket;
}

AllOne* allOneCreate(void) {
    AllOne* obj = (AllOne*)calloc(1, sizeof(AllOne));
    obj->head = (Bucket*)calloc(1, sizeof(Bucket));
    obj->tail = (Bucket*)calloc(1, sizeof(Bucket));
    obj->head->next = obj->tail;
    obj->tail->prev = obj->head;
    obj->bucketCount = 4099;
    obj->map = (KeyMap**)calloc((size_t)obj->bucketCount, sizeof(KeyMap*));
    return obj;
}

void allOneInc(AllOne* obj, char* key) {
    KeyMap* mapped = findMap(obj, key);
    if (mapped) {
        Bucket* bucket = mapped->bucket;
        removeKeyFromBucket(bucket, key);
        Bucket* nextBucket = ensureCountNode(obj, bucket->count + 1, bucket);
        addKeyToBucket(nextBucket, mapped->key);
        mapped->bucket = nextBucket;
        if (bucket->keys == NULL) {
            removeBucket(bucket);
        }
        return;
    }
    char* stored = strdup(key);
    Bucket* bucket = ensureCountNode(obj, 1, obj->head);
    addKeyToBucket(bucket, stored);
    putMap(obj, stored, bucket);
}

void allOneDec(AllOne* obj, char* key) {
    KeyMap* mapped = findMap(obj, key);
    Bucket* bucket = mapped->bucket;
    char* stored = mapped->key;
    removeKeyFromBucket(bucket, key);
    if (bucket->count == 1) {
        eraseMap(obj, key);
        free(stored);
    } else {
        Bucket* prevBucket = ensureCountNode(obj, bucket->count - 1, obj->head);
        addKeyToBucket(prevBucket, stored);
        mapped->bucket = prevBucket;
    }
    if (bucket->keys == NULL) {
        removeBucket(bucket);
    }
}

char* allOneGetMaxKey(AllOne* obj) {
    Bucket* bucket = obj->tail->prev;
    if (bucket == obj->head) {
        return "";
    }
    return bucket->keys->key;
}

char* allOneGetMinKey(AllOne* obj) {
    Bucket* bucket = obj->head->next;
    if (bucket == obj->tail) {
        return "";
    }
    return bucket->keys->key;
}

void allOneFree(AllOne* obj) {
    Bucket* cur = obj->head;
    while (cur) {
        Bucket* next = cur->next;
        KeyItem* item = cur->keys;
        while (item) {
            KeyItem* n = item->next;
            free(item);
            item = n;
        }
        free(cur);
        cur = next;
    }
    for (int i = 0; i < obj->bucketCount; i++) {
        KeyMap* map = obj->map[i];
        while (map) {
            KeyMap* n = map->next;
            free(map->key);
            free(map);
            map = n;
        }
    }
    free(obj->map);
    free(obj);
}

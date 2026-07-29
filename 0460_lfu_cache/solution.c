// LeetCode 0460 - LFU Cache
// https://leetcode.com/problems/lfu-cache/

#include <stdlib.h>

typedef struct FreqNode {
    int key;
    struct FreqNode* next;
} FreqNode;

typedef struct KeyNode {
    int key;
    int value;
    int freq;
    struct KeyNode* next;
} KeyNode;

typedef struct {
    int capacity;
    int size;
    int minFreq;
    int bucketCount;
    KeyNode** buckets;
    FreqNode** freqHeads;
    int freqCapacity;
} LFUCache;

static unsigned hashKey(LFUCache* obj, int key) {
    return ((unsigned)key * 2654435761u) % (unsigned)obj->bucketCount;
}

static KeyNode* findKey(LFUCache* obj, int key) {
    for (KeyNode* node = obj->buckets[hashKey(obj, key)]; node; node = node->next) {
        if (node->key == key) {
            return node;
        }
    }
    return NULL;
}

static void ensureFreqCap(LFUCache* obj, int freq) {
    if (freq < obj->freqCapacity) {
        return;
    }
    int newCap = freq + 1;
    obj->freqHeads = (FreqNode**)realloc(obj->freqHeads, (size_t)newCap * sizeof(FreqNode*));
    for (int i = obj->freqCapacity; i < newCap; i++) {
        obj->freqHeads[i] = NULL;
    }
    obj->freqCapacity = newCap;
}

static void freqPush(LFUCache* obj, int freq, int key) {
    ensureFreqCap(obj, freq);
    FreqNode* node = (FreqNode*)malloc(sizeof(FreqNode));
    node->key = key;
    node->next = NULL;
    if (obj->freqHeads[freq] == NULL) {
        obj->freqHeads[freq] = node;
        return;
    }
    FreqNode* cur = obj->freqHeads[freq];
    while (cur->next) {
        cur = cur->next;
    }
    cur->next = node;
}

static void freqRemove(LFUCache* obj, int freq, int key) {
    FreqNode* cur = obj->freqHeads[freq];
    FreqNode* prev = NULL;
    while (cur) {
        if (cur->key == key) {
            if (prev) {
                prev->next = cur->next;
            } else {
                obj->freqHeads[freq] = cur->next;
            }
            free(cur);
            return;
        }
        prev = cur;
        cur = cur->next;
    }
}

static void touch(LFUCache* obj, KeyNode* node) {
    int freq = node->freq;
    freqRemove(obj, freq, node->key);
    if (obj->freqHeads[freq] == NULL && freq == obj->minFreq) {
        obj->minFreq++;
    }
    node->freq++;
    freqPush(obj, node->freq, node->key);
}

LFUCache* lFUCacheCreate(int capacity) {
    LFUCache* obj = (LFUCache*)calloc(1, sizeof(LFUCache));
    obj->capacity = capacity;
    obj->bucketCount = 4099;
    obj->buckets = (KeyNode**)calloc((size_t)obj->bucketCount, sizeof(KeyNode*));
    obj->freqCapacity = 16;
    obj->freqHeads = (FreqNode**)calloc((size_t)obj->freqCapacity, sizeof(FreqNode*));
    return obj;
}

int lFUCacheGet(LFUCache* obj, int key) {
    KeyNode* node = findKey(obj, key);
    if (!node) {
        return -1;
    }
    touch(obj, node);
    return node->value;
}

void lFUCachePut(LFUCache* obj, int key, int value) {
    if (obj->capacity == 0) {
        return;
    }
    KeyNode* node = findKey(obj, key);
    if (node) {
        node->value = value;
        touch(obj, node);
        return;
    }

    if (obj->size >= obj->capacity) {
        FreqNode* evict = obj->freqHeads[obj->minFreq];
        int evictKey = evict->key;
        freqRemove(obj, obj->minFreq, evictKey);
        unsigned idx = hashKey(obj, evictKey);
        KeyNode* prev = NULL;
        KeyNode* cur = obj->buckets[idx];
        while (cur) {
            if (cur->key == evictKey) {
                if (prev) {
                    prev->next = cur->next;
                } else {
                    obj->buckets[idx] = cur->next;
                }
                free(cur);
                break;
            }
            prev = cur;
            cur = cur->next;
        }
        obj->size--;
    }

    KeyNode* fresh = (KeyNode*)malloc(sizeof(KeyNode));
    fresh->key = key;
    fresh->value = value;
    fresh->freq = 1;
    unsigned idx = hashKey(obj, key);
    fresh->next = obj->buckets[idx];
    obj->buckets[idx] = fresh;
    freqPush(obj, 1, key);
    obj->minFreq = 1;
    obj->size++;
}

void lFUCacheFree(LFUCache* obj) {
    for (int i = 0; i < obj->bucketCount; i++) {
        KeyNode* cur = obj->buckets[i];
        while (cur) {
            KeyNode* next = cur->next;
            free(cur);
            cur = next;
        }
    }
    for (int i = 0; i < obj->freqCapacity; i++) {
        FreqNode* cur = obj->freqHeads[i];
        while (cur) {
            FreqNode* next = cur->next;
            free(cur);
            cur = next;
        }
    }
    free(obj->buckets);
    free(obj->freqHeads);
    free(obj);
}

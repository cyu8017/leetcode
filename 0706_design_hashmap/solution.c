// LeetCode 0706 - Design HashMap
// https://leetcode.com/problems/design-hashmap/

#include <stdlib.h>

#define HASHMAP_SIZE 10007

typedef struct HashNode {
    int key;
    int value;
    struct HashNode* next;
} HashNode;

typedef struct {
    HashNode* buckets[HASHMAP_SIZE];
} MyHashMap;

MyHashMap* myHashMapCreate(void) {
    return (MyHashMap*)calloc(1, sizeof(MyHashMap));
}

void myHashMapPut(MyHashMap* obj, int key, int value) {
    int idx = ((key % HASHMAP_SIZE) + HASHMAP_SIZE) % HASHMAP_SIZE;
    for (HashNode* n = obj->buckets[idx]; n; n = n->next) {
        if (n->key == key) {
            n->value = value;
            return;
        }
    }
    HashNode* node = (HashNode*)malloc(sizeof(HashNode));
    node->key = key;
    node->value = value;
    node->next = obj->buckets[idx];
    obj->buckets[idx] = node;
}

int myHashMapGet(MyHashMap* obj, int key) {
    int idx = ((key % HASHMAP_SIZE) + HASHMAP_SIZE) % HASHMAP_SIZE;
    for (HashNode* n = obj->buckets[idx]; n; n = n->next) {
        if (n->key == key) {
            return n->value;
        }
    }
    return -1;
}

void myHashMapRemove(MyHashMap* obj, int key) {
    int idx = ((key % HASHMAP_SIZE) + HASHMAP_SIZE) % HASHMAP_SIZE;
    HashNode** pp = &obj->buckets[idx];
    while (*pp) {
        if ((*pp)->key == key) {
            HashNode* dead = *pp;
            *pp = dead->next;
            free(dead);
            return;
        }
        pp = &(*pp)->next;
    }
}

void myHashMapFree(MyHashMap* obj) {
    for (int i = 0; i < HASHMAP_SIZE; i++) {
        HashNode* n = obj->buckets[i];
        while (n) {
            HashNode* next = n->next;
            free(n);
            n = next;
        }
    }
    free(obj);
}

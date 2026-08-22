// LeetCode 0705 - Design HashSet
// https://leetcode.com/problems/design-hashset/

#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#define HASHSET_SIZE 10007

typedef struct HashNode {
    int key;
    struct HashNode* next;
} HashNode;

typedef struct {
    HashNode* buckets[HASHSET_SIZE];
} MyHashSet;

MyHashSet* myHashSetCreate(void) {
    MyHashSet* obj = (MyHashSet*)calloc(1, sizeof(MyHashSet));
    return obj;
}

void myHashSetAdd(MyHashSet* obj, int key) {
    int idx = ((key % HASHSET_SIZE) + HASHSET_SIZE) % HASHSET_SIZE;
    for (HashNode* n = obj->buckets[idx]; n; n = n->next) {
        if (n->key == key) {
            return;
        }
    }
    HashNode* node = (HashNode*)malloc(sizeof(HashNode));
    node->key = key;
    node->next = obj->buckets[idx];
    obj->buckets[idx] = node;
}

void myHashSetRemove(MyHashSet* obj, int key) {
    int idx = ((key % HASHSET_SIZE) + HASHSET_SIZE) % HASHSET_SIZE;
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

bool myHashSetContains(MyHashSet* obj, int key) {
    int idx = ((key % HASHSET_SIZE) + HASHSET_SIZE) % HASHSET_SIZE;
    for (HashNode* n = obj->buckets[idx]; n; n = n->next) {
        if (n->key == key) {
            return true;
        }
    }
    return false;
}

void myHashSetFree(MyHashSet* obj) {
    for (int i = 0; i < HASHSET_SIZE; i++) {
        HashNode* n = obj->buckets[i];
        while (n) {
            HashNode* next = n->next;
            free(n);
            n = next;
        }
    }
    free(obj);
}

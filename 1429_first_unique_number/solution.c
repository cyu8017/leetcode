// LeetCode 1429 - First Unique Number
// https://leetcode.com/problems/first-unique-number/

#include <stdlib.h>

typedef struct Node {
    int val;
    struct Node *prev, *next;
} Node;

typedef struct {
    Node* head;
    Node* tail;
    int* keys;
    Node** nodes;
    int* state;
    int cap;
    int size;
} FirstUnique;

static unsigned fu_hash(int x, int cap) { return ((unsigned)x * 2654435761u) % (unsigned)cap; }

static void fu_ensure(FirstUnique* obj) {
    if (obj->size * 2 < obj->cap) return;
    int ncap = obj->cap * 2;
    int* nkeys = (int*)malloc(ncap * sizeof(int));
    Node** nnodes = (Node**)calloc(ncap, sizeof(Node*));
    int* nstate = (int*)calloc(ncap, sizeof(int));
    for (int i = 0; i < obj->cap; i++) if (obj->state[i]) {
        unsigned h = fu_hash(obj->keys[i], ncap);
        while (nstate[h]) h = (h + 1) % ncap;
        nkeys[h] = obj->keys[i]; nnodes[h] = obj->nodes[i]; nstate[h] = obj->state[i];
    }
    free(obj->keys); free(obj->nodes); free(obj->state);
    obj->keys = nkeys; obj->nodes = nnodes; obj->state = nstate; obj->cap = ncap;
}

static int fu_find(FirstUnique* obj, int value, int* found) {
    unsigned h = fu_hash(value, obj->cap);
    while (obj->state[h] && obj->keys[h] != value) h = (h + 1) % obj->cap;
    *found = obj->state[h] && obj->keys[h] == value;
    return (int)h;
}

void firstUniqueAdd(FirstUnique* obj, int value) {
    fu_ensure(obj);
    int found;
    int slot = fu_find(obj, value, &found);
    if (!found) {
        Node* node = (Node*)malloc(sizeof(Node));
        node->val = value; node->prev = obj->tail; node->next = NULL;
        if (obj->tail) obj->tail->next = node; else obj->head = node;
        obj->tail = node;
        obj->keys[slot] = value; obj->nodes[slot] = node; obj->state[slot] = 1; obj->size++;
    } else if (obj->state[slot] == 1) {
        Node* node = obj->nodes[slot];
        if (node->prev) node->prev->next = node->next; else obj->head = node->next;
        if (node->next) node->next->prev = node->prev; else obj->tail = node->prev;
        free(node); obj->nodes[slot] = NULL; obj->state[slot] = 2;
    }
}

FirstUnique* firstUniqueCreate(int* nums, int numsSize) {
    FirstUnique* obj = (FirstUnique*)calloc(1, sizeof(FirstUnique));
    obj->cap = 1024;
    obj->keys = (int*)malloc(obj->cap * sizeof(int));
    obj->nodes = (Node**)calloc(obj->cap, sizeof(Node*));
    obj->state = (int*)calloc(obj->cap, sizeof(int));
    for (int i = 0; i < numsSize; i++) firstUniqueAdd(obj, nums[i]);
    return obj;
}

int firstUniqueShowFirstUnique(FirstUnique* obj) {
    return obj->head ? obj->head->val : -1;
}

void firstUniqueFree(FirstUnique* obj) {
    Node* cur = obj->head;
    while (cur) { Node* n = cur->next; free(cur); cur = n; }
    free(obj->keys); free(obj->nodes); free(obj->state); free(obj);
}

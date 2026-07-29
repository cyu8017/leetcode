// LeetCode 1485 - Clone Binary Tree With Random Pointer
// https://leetcode.com/problems/clone-binary-tree-with-random-pointer/

#include <stdlib.h>

struct Node {
    int val;
    struct Node *left;
    struct Node *right;
    struct Node *random;
};

typedef struct { struct Node* old; struct Node* neu; } Pair;

static Pair* map;
static int mapSize, mapCap;

static struct Node* find_copy(struct Node* node) {
    for (int i = 0; i < mapSize; i++) if (map[i].old == node) return map[i].neu;
    return NULL;
}

static struct Node* clone(struct Node* node) {
    if (!node) return NULL;
    struct Node* existing = find_copy(node);
    if (existing) return existing;
    struct Node* neu = (struct Node*)malloc(sizeof(struct Node));
    neu->val = node->val; neu->left = neu->right = neu->random = NULL;
    if (mapSize == mapCap) { mapCap *= 2; map = (Pair*)realloc(map, mapCap * sizeof(Pair)); }
    map[mapSize].old = node; map[mapSize].neu = neu; mapSize++;
    neu->left = clone(node->left);
    neu->right = clone(node->right);
    neu->random = clone(node->random);
    return neu;
}

struct Node* copyRandomBinaryTree(struct Node* root) {
    mapCap = 64; mapSize = 0;
    map = (Pair*)malloc(mapCap * sizeof(Pair));
    struct Node* ans = clone(root);
    free(map);
    return ans;
}

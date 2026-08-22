// LeetCode 3045 - Count Prefix and Suffix Pairs II
// https://leetcode.com/problems/count-prefix-and-suffix-pairs-ii/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

typedef struct Node {
    struct Node** children;
    int* keys;
    int nkeys, cap;
    int cnt;
} Node;

static Node* newNode(void) {
    Node* n = (Node*)calloc(1, sizeof(Node));
    return n;
}
static Node* getChild(Node* node, int p) {
    for (int i = 0; i < node->nkeys; i++) if (node->keys[i] == p) return node->children[i];
    return NULL;
}
static Node* putChild(Node* node, int p) {
    Node* ch = getChild(node, p);
    if (ch) return ch;
    if (node->nkeys == node->cap) {
        node->cap = node->cap ? node->cap * 2 : 4;
        node->children = (Node**)realloc(node->children, (size_t)node->cap * sizeof(Node*));
        node->keys = (int*)realloc(node->keys, (size_t)node->cap * sizeof(int));
    }
    ch = newNode();
    node->keys[node->nkeys] = p;
    node->children[node->nkeys++] = ch;
    return ch;
}
static void freeNode(Node* n) {
    if (!n) return;
    for (int i = 0; i < n->nkeys; i++) freeNode(n->children[i]);
    free(n->children); free(n->keys); free(n);
}

long long countPrefixSuffixPairs(char** words, int wordsSize) {
    Node* trie = newNode();
    long long ans = 0;
    for (int wi = 0; wi < wordsSize; wi++) {
        char* s = words[wi];
        int m = (int)strlen(s);
        Node* node = trie;
        for (int i = 0; i < m; i++) {
            int p = (int)s[i] * 32 + (int)s[m - i - 1];
            node = putChild(node, p);
            ans += node->cnt;
        }
        node->cnt++;
    }
    freeNode(trie);
    return ans;
}

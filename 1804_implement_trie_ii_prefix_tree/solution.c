// LeetCode 1804 - Implement Trie II (Prefix Tree)
// https://leetcode.com/problems/implement-trie-ii-prefix-tree/

#include <stdlib.h>

typedef struct TrieNode {
    struct TrieNode* children[26];
    int wordCount;
    int prefixCount;
} TrieNode;

typedef struct {
    TrieNode* root;
} Trie;

static TrieNode* trieNodeCreate(void) {
    return (TrieNode*)calloc(1, sizeof(TrieNode));
}

static void trieNodeFree(TrieNode* node) {
    if (!node) return;
    for (int i = 0; i < 26; i++) trieNodeFree(node->children[i]);
    free(node);
}

static TrieNode* trieFind(Trie* obj, char* text) {
    TrieNode* node = obj->root;
    for (; *text; ++text) {
        int index = *text - 'a';
        if (!node->children[index]) return NULL;
        node = node->children[index];
    }
    return node;
}

Trie* trieCreate(void) {
    Trie* obj = (Trie*)malloc(sizeof(Trie));
    obj->root = trieNodeCreate();
    return obj;
}

void trieInsert(Trie* obj, char* word) {
    TrieNode* node = obj->root;
    for (; *word; ++word) {
        int index = *word - 'a';
        if (!node->children[index]) node->children[index] = trieNodeCreate();
        node = node->children[index];
        node->prefixCount += 1;
    }
    node->wordCount += 1;
}

int trieCountWordsEqualTo(Trie* obj, char* word) {
    TrieNode* node = trieFind(obj, word);
    return node ? node->wordCount : 0;
}

int trieCountWordsStartingWith(Trie* obj, char* prefix) {
    TrieNode* node = trieFind(obj, prefix);
    return node ? node->prefixCount : 0;
}

void trieErase(Trie* obj, char* word) {
    TrieNode* node = obj->root;
    for (; *word; ++word) {
        node = node->children[*word - 'a'];
        node->prefixCount -= 1;
    }
    node->wordCount -= 1;
}

void trieFree(Trie* obj) {
    if (!obj) return;
    trieNodeFree(obj->root);
    free(obj);
}

// LeetCode 0211 - Design Add and Search Words Data Structure
// https://leetcode.com/problems/design-add-and-search-words-data-structure/

#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

typedef struct TrieNode {
    struct TrieNode* children[26];
    bool isWord;
} TrieNode;

typedef struct {
    TrieNode* root;
} WordDictionary;

static TrieNode* trieNodeCreate(void) {
    TrieNode* node = calloc(1, sizeof(TrieNode));
    return node;
}

WordDictionary* wordDictionaryCreate(void) {
    WordDictionary* obj = malloc(sizeof(WordDictionary));
    obj->root = trieNodeCreate();
    return obj;
}

void wordDictionaryAddWord(WordDictionary* obj, char* word) {
    TrieNode* node = obj->root;
    for (int i = 0; word[i]; ++i) {
        int index = word[i] - 'a';
        if (!node->children[index]) {
            node->children[index] = trieNodeCreate();
        }
        node = node->children[index];
    }
    node->isWord = true;
}

static bool dfs(TrieNode* node, char* word, int index) {
    if (!word[index]) {
        return node->isWord;
    }
    char c = word[index];
    if (c == '.') {
        for (int i = 0; i < 26; ++i) {
            if (node->children[i] && dfs(node->children[i], word, index + 1)) {
                return true;
            }
        }
        return false;
    }
    int childIndex = c - 'a';
    if (!node->children[childIndex]) {
        return false;
    }
    return dfs(node->children[childIndex], word, index + 1);
}

bool wordDictionarySearch(WordDictionary* obj, char* word) {
    return dfs(obj->root, word, 0);
}

static void trieNodeFree(TrieNode* node) {
    if (!node) {
        return;
    }
    for (int i = 0; i < 26; ++i) {
        trieNodeFree(node->children[i]);
    }
    free(node);
}

void wordDictionaryFree(WordDictionary* obj) {
    trieNodeFree(obj->root);
    free(obj);
}

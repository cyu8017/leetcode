// LeetCode 1032 - Stream of Characters
// https://leetcode.com/problems/stream-of-characters/

#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

typedef struct TrieNode {
    struct TrieNode* children[26];
    bool isWord;
} TrieNode;

typedef struct {
    TrieNode* root;
    char* stream;
    int streamLen;
    int streamCap;
} StreamChecker;

static TrieNode* trieNodeCreate(void) {
    return (TrieNode*)calloc(1, sizeof(TrieNode));
}

static void trieNodeFree(TrieNode* node) {
    if (!node) return;
    for (int i = 0; i < 26; i++) trieNodeFree(node->children[i]);
    free(node);
}

StreamChecker* streamCheckerCreate(char** words, int wordsSize) {
    StreamChecker* obj = (StreamChecker*)malloc(sizeof(StreamChecker));
    obj->root = trieNodeCreate();
    obj->stream = NULL;
    obj->streamLen = 0;
    obj->streamCap = 0;
    for (int w = 0; w < wordsSize; w++) {
        TrieNode* node = obj->root;
        int len = (int)strlen(words[w]);
        for (int i = len - 1; i >= 0; i--) {
            int idx = words[w][i] - 'a';
            if (!node->children[idx]) node->children[idx] = trieNodeCreate();
            node = node->children[idx];
        }
        node->isWord = true;
    }
    return obj;
}

bool streamCheckerQuery(StreamChecker* obj, char letter) {
    if (obj->streamLen == obj->streamCap) {
        obj->streamCap = obj->streamCap ? obj->streamCap * 2 : 16;
        obj->stream = (char*)realloc(obj->stream, (size_t)obj->streamCap);
    }
    obj->stream[obj->streamLen++] = letter;
    TrieNode* node = obj->root;
    for (int i = obj->streamLen - 1; i >= 0; i--) {
        if (node->isWord) return true;
        int idx = obj->stream[i] - 'a';
        if (!node->children[idx]) return false;
        node = node->children[idx];
    }
    return node->isWord;
}

void streamCheckerFree(StreamChecker* obj) {
    if (!obj) return;
    trieNodeFree(obj->root);
    free(obj->stream);
    free(obj);
}

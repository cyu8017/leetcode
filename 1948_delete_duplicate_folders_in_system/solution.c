// LeetCode 1948 - Delete Duplicate Folders in System
// https://leetcode.com/problems/delete-duplicate-folders-in-system/

#include <stdlib.h>
#include <string.h>
#include <stdio.h>

typedef struct TrieNode {
    char* name;
    struct TrieNode** children;
    int childN;
    int childCap;
    char* serial;
    int deleted;
} TrieNode;

static TrieNode* trieNew(const char* name) {
    TrieNode* n = (TrieNode*)calloc(1, sizeof(TrieNode));
    if (name) {
        n->name = (char*)malloc(strlen(name) + 1);
        strcpy(n->name, name);
    }
    return n;
}

static TrieNode* trieChild(TrieNode* node, const char* name) {
    for (int i = 0; i < node->childN; i++) {
        if (strcmp(node->children[i]->name, name) == 0) return node->children[i];
    }
    if (node->childN == node->childCap) {
        node->childCap = node->childCap ? node->childCap * 2 : 4;
        node->children = (TrieNode**)realloc(node->children, (size_t)node->childCap * sizeof(TrieNode*));
    }
    TrieNode* c = trieNew(name);
    node->children[node->childN++] = c;
    return c;
}

static int cmpChild(const void* a, const void* b) {
    TrieNode* const* x = a; TrieNode* const* y = b;
    return strcmp((*x)->name, (*y)->name);
}

typedef struct { char* key; int dup; } DupEntry;

static DupEntry* dups = NULL;
static int dupN = 0, dupCap = 0;

static int findDup(const char* key) {
    for (int i = 0; i < dupN; i++) if (strcmp(dups[i].key, key) == 0) return i;
    return -1;
}

static void markDup(const char* serial) {
    int i = findDup(serial);
    if (i < 0) {
        if (dupN == dupCap) {
            dupCap = dupCap ? dupCap * 2 : 16;
            dups = (DupEntry*)realloc(dups, (size_t)dupCap * sizeof(DupEntry));
        }
        dups[dupN].key = (char*)malloc(strlen(serial) + 1);
        strcpy(dups[dupN].key, serial);
        dups[dupN].dup = 0;
        dupN++;
    } else {
        dups[i].dup = 1;
    }
}

static char* serialize(TrieNode* node) {
    if (!node->childN) {
        node->serial = (char*)malloc(1);
        node->serial[0] = '\0';
        return node->serial;
    }
    qsort(node->children, (size_t)node->childN, sizeof(TrieNode*), cmpChild);
    size_t cap = 64;
    char* buf = (char*)malloc(cap);
    size_t len = 0;
    buf[0] = '\0';
    for (int i = 0; i < node->childN; i++) {
        char* sub = serialize(node->children[i]);
        size_t need = strlen(node->children[i]->name) + strlen(sub) + 3;
        while (len + need + 1 > cap) {
            cap *= 2;
            buf = (char*)realloc(buf, cap);
        }
        len += (size_t)sprintf(buf + len, "%s(%s)", node->children[i]->name, sub);
    }
    node->serial = buf;
    if (buf[0]) markDup(buf);
    return buf;
}

static char*** ans;
static int ansN, ansCap;
static int* ansCol;

static void ensureAns(void) {
    if (ansN >= ansCap) {
        ansCap = ansCap ? ansCap * 2 : 16;
        ans = (char***)realloc(ans, (size_t)ansCap * sizeof(char**));
        ansCol = (int*)realloc(ansCol, (size_t)ansCap * sizeof(int));
    }
}

static void collect(TrieNode* node, char** path, int depth) {
    for (int i = 0; i < node->childN; i++) {
        TrieNode* child = node->children[i];
        if (child->serial && child->serial[0]) {
            int di = findDup(child->serial);
            if (di >= 0 && dups[di].dup) continue;
        }
        path[depth] = child->name;
        ensureAns();
        ans[ansN] = (char**)malloc((size_t)(depth + 1) * sizeof(char*));
        for (int j = 0; j <= depth; j++) {
            ans[ansN][j] = (char*)malloc(strlen(path[j]) + 1);
            strcpy(ans[ansN][j], path[j]);
        }
        ansCol[ansN] = depth + 1;
        ansN++;
        collect(child, path, depth + 1);
    }
}

static void freeTrie(TrieNode* node) {
    if (!node) return;
    for (int i = 0; i < node->childN; i++) freeTrie(node->children[i]);
    free(node->children);
    free(node->name);
    free(node->serial);
    free(node);
}

char*** deleteDuplicateFolder(char*** paths, int pathsSize, int* pathsColSize, int* returnSize, int** returnColumnSizes) {
    TrieNode* root = trieNew(NULL);
    int maxDepth = 0;
    for (int i = 0; i < pathsSize; i++) {
        TrieNode* cur = root;
        if (pathsColSize[i] > maxDepth) maxDepth = pathsColSize[i];
        for (int j = 0; j < pathsColSize[i]; j++) cur = trieChild(cur, paths[i][j]);
    }
    dups = NULL; dupN = 0; dupCap = 0;
    serialize(root);
    ans = NULL; ansN = 0; ansCap = 0; ansCol = NULL;
    char** path = (char**)malloc((size_t)maxDepth * sizeof(char*));
    collect(root, path, 0);
    free(path);
    freeTrie(root);
    for (int i = 0; i < dupN; i++) free(dups[i].key);
    free(dups);
    dups = NULL; dupN = 0;
    *returnSize = ansN;
    *returnColumnSizes = ansCol;
    return ans;
}

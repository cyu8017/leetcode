// LeetCode 0087 - Scramble String
// https://leetcode.com/problems/scramble-string/

#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#define HASH_SIZE 10007

typedef struct MemoNode {
    char* key;
    bool value;
    struct MemoNode* next;
} MemoNode;

static MemoNode* memoTable[HASH_SIZE];

static unsigned int hash_str(const char* s) {
    unsigned int h = 5381;
    while (*s) {
        h = ((h << 5) + h) + (unsigned char)(*s++);
    }
    return h % HASH_SIZE;
}

static bool memo_get(const char* key, bool* out) {
    unsigned int h = hash_str(key);
    for (MemoNode* n = memoTable[h]; n; n = n->next) {
        if (strcmp(n->key, key) == 0) {
            *out = n->value;
            return true;
        }
    }
    return false;
}

static void memo_put(const char* key, bool value) {
    unsigned int h = hash_str(key);
    MemoNode* n = (MemoNode*)malloc(sizeof(MemoNode));
    n->key = (char*)malloc(strlen(key) + 1);
    strcpy(n->key, key);
    n->value = value;
    n->next = memoTable[h];
    memoTable[h] = n;
}

static void memo_clear(void) {
    for (int i = 0; i < HASH_SIZE; i++) {
        MemoNode* n = memoTable[i];
        while (n) {
            MemoNode* next = n->next;
            free(n->key);
            free(n);
            n = next;
        }
        memoTable[i] = NULL;
    }
}

static bool same_sorted(const char* a, const char* b, int len) {
    int count[26] = {0};
    for (int i = 0; i < len; i++) {
        count[a[i] - 'a']++;
        count[b[i] - 'a']--;
    }
    for (int i = 0; i < 26; i++) {
        if (count[i] != 0) {
            return false;
        }
    }
    return true;
}

static bool dfs(const char* a, const char* b, int len) {
    char* key = (char*)malloc((size_t)(len * 2 + 2));
    memcpy(key, a, (size_t)len);
    key[len] = '#';
    memcpy(key + len + 1, b, (size_t)len);
    key[len * 2 + 1] = '\0';

    bool cached;
    if (memo_get(key, &cached)) {
        free(key);
        return cached;
    }

    if (strncmp(a, b, (size_t)len) == 0) {
        memo_put(key, true);
        free(key);
        return true;
    }
    if (!same_sorted(a, b, len)) {
        memo_put(key, false);
        free(key);
        return false;
    }

    for (int i = 1; i < len; i++) {
        if (dfs(a, b, i) && dfs(a + i, b + i, len - i)) {
            memo_put(key, true);
            free(key);
            return true;
        }
        if (dfs(a, b + len - i, i) && dfs(a + i, b, len - i)) {
            memo_put(key, true);
            free(key);
            return true;
        }
    }
    memo_put(key, false);
    free(key);
    return false;
}

bool isScramble(char* s1, char* s2) {
    memo_clear();
    int len = (int)strlen(s1);
    bool result = dfs(s1, s2, len);
    memo_clear();
    return result;
}

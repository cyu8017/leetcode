// LeetCode 0472 - Concatenated Words
// https://leetcode.com/problems/concatenated-words/

#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

static int cmpLen(const void* a, const void* b) {
    const char* left = *(const char* const*)a;
    const char* right = *(const char* const*)b;
    int diff = (int)strlen(left) - (int)strlen(right);
    if (diff != 0) {
        return diff;
    }
    return strcmp(left, right);
}

typedef struct {
    char* key;
    int used;
} WordEntry;

static unsigned hashStr(const char* s, int capacity) {
    unsigned h = 2166136261u;
    for (int i = 0; s[i]; i++) {
        h ^= (unsigned char)s[i];
        h *= 16777619u;
    }
    return h % (unsigned)capacity;
}

static void wordAdd(WordEntry* table, int capacity, char* key) {
    unsigned idx = hashStr(key, capacity);
    while (table[idx].used && strcmp(table[idx].key, key) != 0) {
        idx = (idx + 1) % (unsigned)capacity;
    }
    table[idx].used = 1;
    table[idx].key = key;
}

static void wordRemove(WordEntry* table, int capacity, char* key) {
    unsigned idx = hashStr(key, capacity);
    while (table[idx].used) {
        if (strcmp(table[idx].key, key) == 0) {
            table[idx].used = 0;
            table[idx].key = NULL;
            return;
        }
        idx = (idx + 1) % (unsigned)capacity;
    }
}

static bool wordHas(WordEntry* table, int capacity, const char* key, int len) {
    char buf[1001];
    memcpy(buf, key, (size_t)len);
    buf[len] = '\0';
    unsigned idx = hashStr(buf, capacity);
    while (table[idx].used) {
        if (strcmp(table[idx].key, buf) == 0) {
            return true;
        }
        idx = (idx + 1) % (unsigned)capacity;
    }
    return false;
}

static bool canForm(char* word, WordEntry* table, int capacity) {
    int length = (int)strlen(word);
    if (length == 0) {
        return true;
    }
    bool* dp = (bool*)calloc((size_t)length + 1, sizeof(bool));
    dp[0] = true;
    for (int end = 1; end <= length; end++) {
        for (int start = 0; start < end; start++) {
            if (dp[start] && wordHas(table, capacity, word + start, end - start)) {
                dp[end] = true;
                break;
            }
        }
    }
    bool ok = dp[length];
    free(dp);
    return ok;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** findAllConcatenatedWordsInADict(char** words, int wordsSize, int* returnSize) {
    qsort(words, (size_t)wordsSize, sizeof(char*), cmpLen);
    int capacity = wordsSize * 2 + 7;
    WordEntry* table = (WordEntry*)calloc((size_t)capacity, sizeof(WordEntry));
    for (int i = 0; i < wordsSize; i++) {
        wordAdd(table, capacity, words[i]);
    }

    char** result = (char**)malloc((size_t)wordsSize * sizeof(char*));
    int count = 0;
    for (int i = 0; i < wordsSize; i++) {
        wordRemove(table, capacity, words[i]);
        if (canForm(words[i], table, capacity)) {
            result[count++] = words[i];
        }
        wordAdd(table, capacity, words[i]);
    }

    free(table);
    *returnSize = count;
    return result;
}

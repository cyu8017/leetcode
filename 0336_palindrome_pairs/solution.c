// LeetCode 0336 - Palindrome Pairs
// https://leetcode.com/problems/palindrome-pairs/

#include <stdlib.h>
#include <string.h>

typedef struct {
    char** keys;
    int* values;
    int size;
    int capacity;
} WordMap;

typedef struct {
    long long* items;
    int size;
    int capacity;
} PairSet;

static int isPalindrome(const char* value, int length) {
    int left = 0;
    int right = length - 1;
    while (left < right) {
        if (value[left] != value[right]) {
            return 0;
        }
        left += 1;
        right -= 1;
    }
    return 1;
}

static void reverseCopy(const char* source, int length, char* destination) {
    for (int index = 0; index < length; index++) {
        destination[index] = source[length - 1 - index];
    }
    destination[length] = '\0';
}

static void wordMapInit(WordMap* map) {
    map->keys = NULL;
    map->values = NULL;
    map->size = 0;
    map->capacity = 0;
}

static int wordMapGet(WordMap* map, const char* key, int* found) {
    for (int index = 0; index < map->size; index++) {
        if (strcmp(map->keys[index], key) == 0) {
            *found = 1;
            return map->values[index];
        }
    }
    *found = 0;
    return -1;
}

static void wordMapPut(WordMap* map, const char* key, int value) {
    if (map->size == map->capacity) {
        map->capacity = map->capacity == 0 ? 16 : map->capacity * 2;
        map->keys = (char**)realloc(map->keys, (size_t)map->capacity * sizeof(char*));
        map->values = (int*)realloc(map->values, (size_t)map->capacity * sizeof(int));
    }
    map->keys[map->size] = strdup(key);
    map->values[map->size] = value;
    map->size += 1;
}

static void pairSetInit(PairSet* set) {
    set->items = NULL;
    set->size = 0;
    set->capacity = 0;
}

static long long pairKey(int left, int right) {
    return ((long long)left << 32) | (unsigned int)right;
}

static int pairSetContains(PairSet* set, long long key) {
    for (int index = 0; index < set->size; index++) {
        if (set->items[index] == key) {
            return 1;
        }
    }
    return 0;
}

static void pairSetAdd(PairSet* set, long long key) {
    if (pairSetContains(set, key)) {
        return;
    }
    if (set->size == set->capacity) {
        set->capacity = set->capacity == 0 ? 16 : set->capacity * 2;
        set->items = (long long*)realloc(set->items, (size_t)set->capacity * sizeof(long long));
    }
    set->items[set->size++] = key;
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *returnColumnSizes array must be malloced by caller.
 */
int** palindromePairs(char** words, int wordsSize, int* returnSize, int** returnColumnSizes) {
    WordMap wordMap;
    wordMapInit(&wordMap);
    for (int index = 0; index < wordsSize; index++) {
        wordMapPut(&wordMap, words[index], index);
    }

    PairSet seen;
    pairSetInit(&seen);

    for (int index = 0; index < wordsSize; index++) {
        const char* word = words[index];
        int wordLength = (int)strlen(word);
        for (int split = 0; split <= wordLength; split++) {
            if (isPalindrome(word, split)) {
                char* reversedRight = (char*)malloc((size_t)(wordLength - split + 1));
                reverseCopy(word + split, wordLength - split, reversedRight);
                int found = 0;
                int other = wordMapGet(&wordMap, reversedRight, &found);
                if (found && other != index) {
                    pairSetAdd(&seen, pairKey(other, index));
                }
                free(reversedRight);
            }
            if (isPalindrome(word + split, wordLength - split)) {
                char* reversedLeft = (char*)malloc((size_t)(split + 1));
                reverseCopy(word, split, reversedLeft);
                int found = 0;
                int other = wordMapGet(&wordMap, reversedLeft, &found);
                if (found && other != index) {
                    pairSetAdd(&seen, pairKey(index, other));
                }
                free(reversedLeft);
            }
        }
    }

    int** result = (int**)malloc((size_t)seen.size * sizeof(int*));
    int* colSizes = (int*)malloc((size_t)seen.size * sizeof(int));
    for (int index = 0; index < seen.size; index++) {
        long long key = seen.items[index];
        result[index] = (int*)malloc(2 * sizeof(int));
        result[index][0] = (int)(key >> 32);
        result[index][1] = (int)(key & 0xffffffff);
        colSizes[index] = 2;
    }

    for (int index = 0; index < wordMap.size; index++) {
        free(wordMap.keys[index]);
    }
    free(wordMap.keys);
    free(wordMap.values);
    free(seen.items);

    *returnSize = seen.size;
    *returnColumnSizes = colSizes;
    return result;
}

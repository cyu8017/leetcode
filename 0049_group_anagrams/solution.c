// LeetCode 0049 - Group Anagrams
// https://leetcode.com/problems/group-anagrams/

#include <stdlib.h>
#include <string.h>

typedef struct {
    char* key;
    char** words;
    int count;
    int capacity;
} AnagramGroup;

static int cmpChar(const void* a, const void* b) {
    return *(const unsigned char*)a - *(const unsigned char*)b;
}

static int cmpStr(const void* a, const void* b) {
    return strcmp(*(const char* const*)a, *(const char* const*)b);
}

static int cmpGroup(const void* a, const void* b) {
    const AnagramGroup* ga = (const AnagramGroup*)a;
    const AnagramGroup* gb = (const AnagramGroup*)b;
    int ia = minGroupIndex(ga);
    int ib = minGroupIndex(gb);
    return ib - ia;
}

static char** g_strs;
static int g_strsSize;

static int wordIndex(const char* target) {
    for (int i = 0; i < g_strsSize; i++) {
        if (strcmp(g_strs[i], target) == 0) {
            return i;
        }
    }
    return g_strsSize;
}

static int minGroupIndex(const AnagramGroup* group) {
    int minIdx = g_strsSize;
    for (int i = 0; i < group->count; i++) {
        int idx = wordIndex(group->words[i]);
        if (idx < minIdx) {
            minIdx = idx;
        }
    }
    return minIdx;
}

static char* makeKey(const char* word) {
    int len = (int)strlen(word);
    char* key = (char*)malloc((size_t)len + 1);
    memcpy(key, word, (size_t)len + 1);
    qsort(key, (size_t)len, 1, cmpChar);
    return key;
}

static void addWord(AnagramGroup* group, const char* word) {
    if (group->count >= group->capacity) {
        group->capacity = group->capacity == 0 ? 4 : group->capacity * 2;
        group->words = (char**)realloc(group->words, (size_t)group->capacity * sizeof(char*));
    }
    group->words[group->count] = (char*)malloc(strlen(word) + 1);
    strcpy(group->words[group->count], word);
    group->count++;
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *returnColumnSizes array must be malloced by caller.
 */
char*** groupAnagrams(char** strs, int strsSize, int* returnSize, int** returnColumnSizes) {
    AnagramGroup* groups = NULL;
    int groupCount = 0;
    int groupCapacity = 0;

    for (int i = 0; i < strsSize; i++) {
        char* key = makeKey(strs[i]);
        int found = -1;

        for (int j = 0; j < groupCount; j++) {
            if (strcmp(groups[j].key, key) == 0) {
                found = j;
                break;
            }
        }

        if (found == -1) {
            if (groupCount >= groupCapacity) {
                groupCapacity = groupCapacity == 0 ? 8 : groupCapacity * 2;
                groups = (AnagramGroup*)realloc(groups, (size_t)groupCapacity * sizeof(AnagramGroup));
            }
            groups[groupCount].key = key;
            groups[groupCount].words = NULL;
            groups[groupCount].count = 0;
            groups[groupCount].capacity = 0;
            addWord(&groups[groupCount], strs[i]);
            groupCount++;
        } else {
            addWord(&groups[found], strs[i]);
            free(key);
        }
    }

    for (int i = 0; i < groupCount; i++) {
        qsort(groups[i].words, (size_t)groups[i].count, sizeof(char*), cmpStr);
    }
    g_strs = strs;
    g_strsSize = strsSize;
    qsort(groups, (size_t)groupCount, sizeof(AnagramGroup), cmpGroup);

    char*** result = (char***)malloc((size_t)groupCount * sizeof(char**));
    int* colSizes = (int*)malloc((size_t)groupCount * sizeof(int));

    for (int i = 0; i < groupCount; i++) {
        result[i] = groups[i].words;
        colSizes[i] = groups[i].count;
        free(groups[i].key);
    }
    free(groups);

    *returnSize = groupCount;
    *returnColumnSizes = colSizes;
    return result;
}

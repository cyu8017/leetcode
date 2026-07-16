// LeetCode 0527 - Word Abbreviation
// https://leetcode.com/problems/word-abbreviation/

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct GroupNode {
    char* key;
    int* indices;
    int indicesSize;
    int indicesCapacity;
    struct GroupNode* next;
} GroupNode;

static void appendIndex(GroupNode* group, int index) {
    if (group->indicesSize == group->indicesCapacity) {
        group->indicesCapacity = group->indicesCapacity == 0 ? 4 : group->indicesCapacity * 2;
        group->indices = (int*)realloc(group->indices, (size_t)group->indicesCapacity * sizeof(int));
    }
    group->indices[group->indicesSize++] = index;
}

static void buildAbbreviation(const char* word, int prefix, char* buffer) {
    const int length = (int)strlen(word);
    if (prefix + 2 >= length) {
        strcpy(buffer, word);
        return;
    }
    const int middle = length - prefix - 1;
    char candidate[256];
    snprintf(candidate, sizeof(candidate), "%.*s%d%c", prefix, word, middle, word[length - 1]);
    if ((int)strlen(candidate) < length) {
        strcpy(buffer, candidate);
    } else {
        strcpy(buffer, word);
    }
}

char** wordsAbbreviation(char** words, int wordsSize, int* returnSize) {
    int* prefixes = (int*)malloc((size_t)wordsSize * sizeof(int));
    for (int index = 0; index < wordsSize; index++) {
        prefixes[index] = 1;
    }

    bool changed = true;
    while (changed) {
        changed = false;
        GroupNode** buckets = (GroupNode**)calloc(256, sizeof(GroupNode*));

        for (int index = 0; index < wordsSize; index++) {
            char key[256];
            buildAbbreviation(words[index], prefixes[index], key);
            const unsigned bucket = (unsigned)key[0] % 256;
            GroupNode* group = buckets[bucket];
            while (group && strcmp(group->key, key) != 0) {
                group = group->next;
            }
            if (!group) {
                group = (GroupNode*)calloc(1, sizeof(GroupNode));
                group->key = strdup(key);
                group->next = buckets[bucket];
                buckets[bucket] = group;
            }
            appendIndex(group, index);
        }

        for (int bucket = 0; bucket < 256; bucket++) {
            for (GroupNode* group = buckets[bucket]; group; group = group->next) {
                if (group->indicesSize > 1) {
                    changed = true;
                    for (int i = 0; i < group->indicesSize; i++) {
                        prefixes[group->indices[i]]++;
                    }
                }
            }
        }

        for (int bucket = 0; bucket < 256; bucket++) {
            for (GroupNode* group = buckets[bucket]; group;) {
                GroupNode* next = group->next;
                free(group->key);
                free(group->indices);
                free(group);
                group = next;
            }
        }
        free(buckets);
    }

    char** result = (char**)malloc((size_t)wordsSize * sizeof(char*));
    for (int index = 0; index < wordsSize; index++) {
        char buffer[256];
        buildAbbreviation(words[index], prefixes[index], buffer);
        result[index] = strdup(buffer);
    }
    free(prefixes);
    *returnSize = wordsSize;
    return result;
}

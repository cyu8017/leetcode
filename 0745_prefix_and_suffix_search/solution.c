// LeetCode 0745 - Prefix and Suffix Search
// https://leetcode.com/problems/prefix-and-suffix-search/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Entry {
    char* key;
    int index;
    struct Entry* next;
} Entry;

typedef struct {
    Entry** buckets;
    int bucketCount;
} WordFilter;

static unsigned hashStr(const char* s) {
    unsigned h = 2166136261u;
    for (; *s; s++) {
        h ^= (unsigned char)*s;
        h *= 16777619u;
    }
    return h;
}

static void mapPut(WordFilter* obj, const char* key, int index) {
    unsigned h = hashStr(key) % (unsigned)obj->bucketCount;
    for (Entry* e = obj->buckets[h]; e; e = e->next) {
        if (strcmp(e->key, key) == 0) {
            e->index = index;
            return;
        }
    }
    Entry* e = (Entry*)malloc(sizeof(Entry));
    e->key = (char*)malloc(strlen(key) + 1);
    strcpy(e->key, key);
    e->index = index;
    e->next = obj->buckets[h];
    obj->buckets[h] = e;
}

static int mapGet(WordFilter* obj, const char* key) {
    unsigned h = hashStr(key) % (unsigned)obj->bucketCount;
    for (Entry* e = obj->buckets[h]; e; e = e->next) {
        if (strcmp(e->key, key) == 0) {
            return e->index;
        }
    }
    return -1;
}

WordFilter* wordFilterCreate(char** words, int wordsSize) {
    WordFilter* obj = (WordFilter*)malloc(sizeof(WordFilter));
    obj->bucketCount = 10007;
    obj->buckets = (Entry**)calloc((size_t)obj->bucketCount, sizeof(Entry*));
    char key[220];
    for (int index = 0; index < wordsSize; index++) {
        char* word = words[index];
        int size = (int)strlen(word);
        for (int i = 0; i <= size; i++) {
            for (int j = 0; j <= size; j++) {
                int pos = 0;
                memcpy(key, word, (size_t)i);
                pos = i;
                key[pos++] = '#';
                memcpy(key + pos, word + j, (size_t)(size - j));
                pos += size - j;
                key[pos] = '\0';
                mapPut(obj, key, index);
            }
        }
    }
    return obj;
}

int wordFilterF(WordFilter* obj, char* pref, char* suff) {
    char key[220];
    sprintf(key, "%s#%s", pref, suff);
    return mapGet(obj, key);
}

void wordFilterFree(WordFilter* obj) {
    for (int i = 0; i < obj->bucketCount; i++) {
        Entry* e = obj->buckets[i];
        while (e) {
            Entry* next = e->next;
            free(e->key);
            free(e);
            e = next;
        }
    }
    free(obj->buckets);
    free(obj);
}

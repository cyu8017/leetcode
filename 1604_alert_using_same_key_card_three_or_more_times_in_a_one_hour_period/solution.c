// LeetCode 1604 - Alert Using Same Key-Card Three or More Times in a One Hour Period
// https://leetcode.com/problems/alert-using-same-key-card-three-or-more-times-in-a-one-hour-period/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

typedef struct {
    char* name;
    int* times;
    int count;
    int cap;
} Entry;

static int cmpInt(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

static int cmpStrPtr(const void* a, const void* b) {
    return strcmp(*(char* const*)a, *(char* const*)b);
}

static int toMinutes(const char* t) {
    return (t[0] - '0') * 600 + (t[1] - '0') * 60 + (t[3] - '0') * 10 + (t[4] - '0');
}

char** alertNames(char** keyName, int keyNameSize, char** keyTime, int keyTimeSize, int* returnSize) {
    (void)keyTimeSize;
    Entry* entries = NULL;
    int n = 0, cap = 0;
    for (int i = 0; i < keyNameSize; i++) {
        int found = -1;
        for (int j = 0; j < n; j++) {
            if (strcmp(entries[j].name, keyName[i]) == 0) { found = j; break; }
        }
        if (found < 0) {
            if (n == cap) {
                cap = cap ? cap * 2 : 16;
                entries = (Entry*)realloc(entries, (size_t)cap * sizeof(Entry));
            }
            entries[n].name = keyName[i];
            entries[n].times = NULL;
            entries[n].count = 0;
            entries[n].cap = 0;
            found = n++;
        }
        Entry* e = &entries[found];
        if (e->count == e->cap) {
            e->cap = e->cap ? e->cap * 2 : 8;
            e->times = (int*)realloc(e->times, (size_t)e->cap * sizeof(int));
        }
        e->times[e->count++] = toMinutes(keyTime[i]);
    }
    char** ans = NULL;
    *returnSize = 0;
    for (int i = 0; i < n; i++) {
        qsort(entries[i].times, (size_t)entries[i].count, sizeof(int), cmpInt);
        bool alert = false;
        for (int j = 0; j + 2 < entries[i].count; j++) {
            if (entries[i].times[j + 2] - entries[i].times[j] <= 60) { alert = true; break; }
        }
        if (alert) {
            ans = (char**)realloc(ans, (size_t)(*returnSize + 1) * sizeof(char*));
            ans[*returnSize] = (char*)malloc(strlen(entries[i].name) + 1);
            strcpy(ans[*returnSize], entries[i].name);
            (*returnSize)++;
        }
        free(entries[i].times);
    }
    free(entries);
    if (*returnSize) qsort(ans, (size_t)(*returnSize), sizeof(char*), cmpStrPtr);
    return ans;
}

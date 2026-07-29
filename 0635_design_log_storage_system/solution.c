// LeetCode 0635 - Design Log Storage System
// https://leetcode.com/problems/design-log-storage-system/

#define _POSIX_C_SOURCE 200809L
#include <stdlib.h>
#include <string.h>

typedef struct {
    int* ids;
    char** timestamps;
    int size;
    int capacity;
} LogSystem;

LogSystem* logSystemCreate() {
    LogSystem* obj = (LogSystem*)malloc(sizeof(LogSystem));
    obj->capacity = 16;
    obj->ids = (int*)malloc((size_t)obj->capacity * sizeof(int));
    obj->timestamps = (char**)malloc((size_t)obj->capacity * sizeof(char*));
    obj->size = 0;
    return obj;
}

void logSystemPut(LogSystem* obj, int id, char* timestamp) {
    if (obj->size == obj->capacity) {
        obj->capacity *= 2;
        obj->ids = (int*)realloc(obj->ids, (size_t)obj->capacity * sizeof(int));
        obj->timestamps = (char**)realloc(obj->timestamps, (size_t)obj->capacity * sizeof(char*));
    }
    obj->ids[obj->size] = id;
    obj->timestamps[obj->size] = strdup(timestamp);
    obj->size++;
}

static int granIndex(char* granularity) {
    if (strcmp(granularity, "Year") == 0) return 4;
    if (strcmp(granularity, "Month") == 0) return 7;
    if (strcmp(granularity, "Day") == 0) return 10;
    if (strcmp(granularity, "Hour") == 0) return 13;
    if (strcmp(granularity, "Minute") == 0) return 16;
    return 19;
}

typedef struct { char* ts; int id; } Pair;
static int cmpPair(const void* a, const void* b) {
    const Pair* x = (const Pair*)a; const Pair* y = (const Pair*)b;
    int c = strcmp(x->ts, y->ts);
    return c ? c : x->id - y->id;
}

int* logSystemRetrieve(LogSystem* obj, char* start, char* end, char* granularity, int* retSize) {
    int idx = granIndex(granularity);
    char startKey[32], endKey[32];
    strncpy(startKey, start, (size_t)idx); startKey[idx] = '\0';
    strncpy(endKey, end, (size_t)idx); endKey[idx] = '\0';
    Pair* matched = (Pair*)malloc((size_t)obj->size * sizeof(Pair));
    int m = 0;
    for (int i = 0; i < obj->size; i++) {
        char key[32];
        strncpy(key, obj->timestamps[i], (size_t)idx); key[idx] = '\0';
        if (strcmp(key, startKey) >= 0 && strcmp(key, endKey) <= 0) {
            matched[m].ts = obj->timestamps[i];
            matched[m].id = obj->ids[i];
            m++;
        }
    }
    qsort(matched, (size_t)m, sizeof(Pair), cmpPair);
    int* result = (int*)malloc((size_t)m * sizeof(int));
    for (int i = 0; i < m; i++) result[i] = matched[i].id;
    free(matched);
    *retSize = m;
    return result;
}

void logSystemFree(LogSystem* obj) {
    for (int i = 0; i < obj->size; i++) free(obj->timestamps[i]);
    free(obj->ids); free(obj->timestamps); free(obj);
}

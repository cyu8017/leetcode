// LeetCode 1166 - Design File System
// https://leetcode.com/problems/design-file-system/

#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

typedef struct { char* path; int value; } Entry;

typedef struct {
    Entry* entries;
    int size;
    int capacity;
} FileSystem;

FileSystem* fileSystemCreate(void) {
    FileSystem* obj = (FileSystem*)malloc(sizeof(FileSystem));
    obj->capacity = 16;
    obj->size = 1;
    obj->entries = (Entry*)malloc((size_t)obj->capacity * sizeof(Entry));
    obj->entries[0].path = (char*)malloc(1);
    obj->entries[0].path[0] = '\0';
    obj->entries[0].value = -1;
    return obj;
}

static int findPath(FileSystem* obj, const char* path) {
    for (int i = 0; i < obj->size; i++)
        if (strcmp(obj->entries[i].path, path) == 0) return i;
    return -1;
}

bool fileSystemCreatePath(FileSystem* obj, char* path, int value) {
    if (findPath(obj, path) >= 0) return false;
    char parent[120];
    strcpy(parent, path);
    char* slash = strrchr(parent, '/');
    if (!slash) return false;
    *slash = '\0';
    if (findPath(obj, parent) < 0) return false;
    if (obj->size >= obj->capacity) {
        obj->capacity *= 2;
        obj->entries = (Entry*)realloc(obj->entries, (size_t)obj->capacity * sizeof(Entry));
    }
    obj->entries[obj->size].path = (char*)malloc(strlen(path) + 1);
    strcpy(obj->entries[obj->size].path, path);
    obj->entries[obj->size].value = value;
    obj->size++;
    return true;
}

int fileSystemGet(FileSystem* obj, char* path) {
    int idx = findPath(obj, path);
    return idx < 0 ? -1 : obj->entries[idx].value;
}

void fileSystemFree(FileSystem* obj) {
    if (!obj) return;
    for (int i = 0; i < obj->size; i++) free(obj->entries[i].path);
    free(obj->entries);
    free(obj);
}

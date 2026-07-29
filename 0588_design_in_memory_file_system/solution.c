// LeetCode 0588 - Design In-Memory File System
// https://leetcode.com/problems/design-in-memory-file-system/

#define _POSIX_C_SOURCE 200809L

#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

typedef struct FSNode {
    char* name;
    bool isFile;
    char* content;
    struct FSNode** children;
    int childCount;
    int childCap;
} FSNode;

typedef struct {
    FSNode* root;
} FileSystem;

static FSNode* newDir(const char* name) {
    FSNode* node = (FSNode*)calloc(1, sizeof(FSNode));
    node->name = strdup(name);
    node->isFile = false;
    node->content = strdup("");
    return node;
}

static FSNode* findChild(FSNode* node, const char* name) {
    for (int i = 0; i < node->childCount; i++) {
        if (strcmp(node->children[i]->name, name) == 0) {
            return node->children[i];
        }
    }
    return NULL;
}

static FSNode* ensureChildDir(FSNode* node, const char* name) {
    FSNode* child = findChild(node, name);
    if (child) {
        return child;
    }
    if (node->childCount == node->childCap) {
        node->childCap = node->childCap == 0 ? 4 : node->childCap * 2;
        node->children = (FSNode**)realloc(node->children, (size_t)node->childCap * sizeof(FSNode*));
    }
    child = newDir(name);
    node->children[node->childCount++] = child;
    return child;
}

static int splitPath(char* path, char** parts, int maxParts) {
    int count = 0;
    char* p = path;
    while (*p) {
        while (*p == '/') {
            p++;
        }
        if (!*p) {
            break;
        }
        parts[count++] = p;
        while (*p && *p != '/') {
            p++;
        }
        if (*p == '/') {
            *p = '\0';
            p++;
        }
        if (count >= maxParts) {
            break;
        }
    }
    return count;
}

static int cmpName(const void* a, const void* b) {
    FSNode* const* left = (FSNode* const*)a;
    FSNode* const* right = (FSNode* const*)b;
    return strcmp((*left)->name, (*right)->name);
}

FileSystem* fileSystemCreate(void) {
    FileSystem* obj = (FileSystem*)malloc(sizeof(FileSystem));
    obj->root = newDir("");
    return obj;
}

char** fileSystemLs(FileSystem* obj, char* path, int* retSize) {
    if (strcmp(path, "/") == 0) {
        qsort(obj->root->children, (size_t)obj->root->childCount, sizeof(FSNode*), cmpName);
        char** result = (char**)malloc((size_t)obj->root->childCount * sizeof(char*));
        for (int i = 0; i < obj->root->childCount; i++) {
            result[i] = obj->root->children[i]->name;
        }
        *retSize = obj->root->childCount;
        return result;
    }

    char* copy = strdup(path);
    char* parts[64];
    int partCount = splitPath(copy, parts, 64);
    FSNode* node = obj->root;
    for (int i = 0; i < partCount; i++) {
        node = findChild(node, parts[i]);
    }
    free(copy);

    if (node->isFile) {
        char** result = (char**)malloc(sizeof(char*));
        result[0] = node->name;
        *retSize = 1;
        return result;
    }

    qsort(node->children, (size_t)node->childCount, sizeof(FSNode*), cmpName);
    char** result = (char**)malloc((size_t)node->childCount * sizeof(char*));
    for (int i = 0; i < node->childCount; i++) {
        result[i] = node->children[i]->name;
    }
    *retSize = node->childCount;
    return result;
}

void fileSystemMkdir(FileSystem* obj, char* path) {
    char* copy = strdup(path);
    char* parts[64];
    int partCount = splitPath(copy, parts, 64);
    FSNode* node = obj->root;
    for (int i = 0; i < partCount; i++) {
        node = ensureChildDir(node, parts[i]);
    }
    free(copy);
}

void fileSystemAddContentToFile(FileSystem* obj, char* filePath, char* content) {
    char* copy = strdup(filePath);
    char* parts[64];
    int partCount = splitPath(copy, parts, 64);
    FSNode* node = obj->root;
    for (int i = 0; i < partCount - 1; i++) {
        node = ensureChildDir(node, parts[i]);
    }
    FSNode* file = findChild(node, parts[partCount - 1]);
    if (!file) {
        file = ensureChildDir(node, parts[partCount - 1]);
        file->isFile = true;
        free(file->content);
        file->content = strdup("");
    }
    char* merged = (char*)malloc(strlen(file->content) + strlen(content) + 1);
    strcpy(merged, file->content);
    strcat(merged, content);
    free(file->content);
    file->content = merged;
    free(copy);
}

char* fileSystemReadContentFromFile(FileSystem* obj, char* filePath) {
    char* copy = strdup(filePath);
    char* parts[64];
    int partCount = splitPath(copy, parts, 64);
    FSNode* node = obj->root;
    for (int i = 0; i < partCount; i++) {
        node = findChild(node, parts[i]);
    }
    free(copy);
    return node->content;
}

static void freeNode(FSNode* node) {
    for (int i = 0; i < node->childCount; i++) {
        freeNode(node->children[i]);
    }
    free(node->children);
    free(node->name);
    free(node->content);
    free(node);
}

void fileSystemFree(FileSystem* obj) {
    freeNode(obj->root);
    free(obj);
}

// LeetCode 1500 - Design a File Sharing System
// https://leetcode.com/problems/design-a-file-sharing-system/

#include <stdlib.h>
#include <string.h>

#define MAX_USERS 1505
#define MAX_CHUNKS 105

typedef struct {
    int m;
    char owns[MAX_USERS][MAX_CHUNKS];
    char active[MAX_USERS];
    int* freeIds;
    int freeSize;
    int freeCap;
    int nextId;
} FileSharing;

FileSharing* fileSharingCreate(int m) {
    FileSharing* obj = (FileSharing*)calloc(1, sizeof(FileSharing));
    obj->m = m;
    obj->nextId = 1;
    obj->freeCap = 64;
    obj->freeIds = (int*)malloc((size_t)obj->freeCap * sizeof(int));
    return obj;
}

int fileSharingJoin(FileSharing* obj, int* ownedChunks, int ownedChunksSize) {
    int user;
    if (obj->freeSize > 0) {
        int best = 0;
        for (int i = 1; i < obj->freeSize; i++) if (obj->freeIds[i] < obj->freeIds[best]) best = i;
        user = obj->freeIds[best];
        obj->freeIds[best] = obj->freeIds[--obj->freeSize];
    } else {
        user = obj->nextId++;
    }
    obj->active[user] = 1;
    memset(obj->owns[user], 0, sizeof(obj->owns[user]));
    for (int i = 0; i < ownedChunksSize; i++) obj->owns[user][ownedChunks[i]] = 1;
    return user;
}

void fileSharingLeave(FileSharing* obj, int userID) {
    obj->active[userID] = 0;
    memset(obj->owns[userID], 0, sizeof(obj->owns[userID]));
    if (obj->freeSize == obj->freeCap) {
        obj->freeCap *= 2;
        obj->freeIds = (int*)realloc(obj->freeIds, (size_t)obj->freeCap * sizeof(int));
    }
    obj->freeIds[obj->freeSize++] = userID;
}

int* fileSharingRequest(FileSharing* obj, int userID, int chunkID, int* retSize) {
    int* users = (int*)malloc((size_t)obj->nextId * sizeof(int));
    int sz = 0;
    for (int u = 1; u < obj->nextId; u++) {
        if (obj->active[u] && obj->owns[u][chunkID]) users[sz++] = u;
    }
    if (sz > 0) obj->owns[userID][chunkID] = 1;
    *retSize = sz;
    return users;
}

void fileSharingFree(FileSharing* obj) {
    free(obj->freeIds);
    free(obj);
}

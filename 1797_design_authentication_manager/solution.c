// LeetCode 1797 - Design Authentication Manager
// https://leetcode.com/problems/design-authentication-manager/

#include <stdlib.h>
#include <string.h>

typedef struct {
    char** tokenIds;
    int* expiries;
    int size;
    int capacity;
    int ttl;
} AuthenticationManager;

AuthenticationManager* authenticationManagerCreate(int timeToLive) {
    AuthenticationManager* obj = (AuthenticationManager*)malloc(sizeof(AuthenticationManager));
    obj->ttl = timeToLive;
    obj->size = 0;
    obj->capacity = 16;
    obj->tokenIds = (char**)malloc(obj->capacity * sizeof(char*));
    obj->expiries = (int*)malloc(obj->capacity * sizeof(int));
    return obj;
}

static int findToken(AuthenticationManager* obj, char* tokenId) {
    for (int i = 0; i < obj->size; i++) {
        if (strcmp(obj->tokenIds[i], tokenId) == 0) return i;
    }
    return -1;
}

void authenticationManagerGenerate(AuthenticationManager* obj, char* tokenId, int currentTime) {
    int idx = findToken(obj, tokenId);
    if (idx >= 0) {
        obj->expiries[idx] = currentTime + obj->ttl;
        return;
    }
    if (obj->size == obj->capacity) {
        obj->capacity *= 2;
        obj->tokenIds = (char**)realloc(obj->tokenIds, obj->capacity * sizeof(char*));
        obj->expiries = (int*)realloc(obj->expiries, obj->capacity * sizeof(int));
    }
    obj->tokenIds[obj->size] = strdup(tokenId);
    obj->expiries[obj->size] = currentTime + obj->ttl;
    obj->size++;
}

void authenticationManagerRenew(AuthenticationManager* obj, char* tokenId, int currentTime) {
    int idx = findToken(obj, tokenId);
    if (idx >= 0 && obj->expiries[idx] > currentTime) {
        obj->expiries[idx] = currentTime + obj->ttl;
    }
}

int authenticationManagerCountUnexpiredTokens(AuthenticationManager* obj, int currentTime) {
    int count = 0;
    for (int i = 0; i < obj->size; i++) {
        if (obj->expiries[i] > currentTime) count++;
    }
    return count;
}

void authenticationManagerFree(AuthenticationManager* obj) {
    for (int i = 0; i < obj->size; i++) {
        free(obj->tokenIds[i]);
    }
    free(obj->tokenIds);
    free(obj->expiries);
    free(obj);
}

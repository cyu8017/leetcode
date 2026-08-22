// LeetCode 2254 - Design Video Sharing Platform
// https://leetcode.com/problems/design-video-sharing-platform/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

typedef struct {
    int nextID;
    int* freeHeap;
    int freeSize;
    int freeCap;
    char** videos;
    int* views;
    int* likes;
    int* dislikes;
    bool* used;
    int cap;
} VideoSharingPlatform;

static void heap_swap(int* a, int i, int j) { int t = a[i]; a[i] = a[j]; a[j] = t; }
static void heap_up(int* a, int i) {
    while (i > 0) {
        int p = (i - 1) / 2;
        if (a[p] <= a[i]) break;
        heap_swap(a, p, i); i = p;
    }
}
static void heap_down(int* a, int n, int i) {
    for (;;) {
        int l = 2 * i + 1, r = l + 1, s = i;
        if (l < n && a[l] < a[s]) s = l;
        if (r < n && a[r] < a[s]) s = r;
        if (s == i) break;
        heap_swap(a, i, s); i = s;
    }
}

static void ensure_id(VideoSharingPlatform* obj, int id) {
    if (id < obj->cap) return;
    int nc = obj->cap ? obj->cap : 16;
    while (nc <= id) nc *= 2;
    obj->videos = (char**)realloc(obj->videos, (size_t)nc * sizeof(char*));
    obj->views = (int*)realloc(obj->views, (size_t)nc * sizeof(int));
    obj->likes = (int*)realloc(obj->likes, (size_t)nc * sizeof(int));
    obj->dislikes = (int*)realloc(obj->dislikes, (size_t)nc * sizeof(int));
    obj->used = (bool*)realloc(obj->used, (size_t)nc * sizeof(bool));
    for (int i = obj->cap; i < nc; i++) {
        obj->videos[i] = NULL;
        obj->views[i] = obj->likes[i] = obj->dislikes[i] = 0;
        obj->used[i] = false;
    }
    obj->cap = nc;
}

VideoSharingPlatform* videoSharingPlatformCreate() {
    return (VideoSharingPlatform*)calloc(1, sizeof(VideoSharingPlatform));
}

int videoSharingPlatformUpload(VideoSharingPlatform* obj, char* video) {
    int id;
    if (obj->freeSize > 0) {
        id = obj->freeHeap[0];
        obj->freeHeap[0] = obj->freeHeap[--obj->freeSize];
        if (obj->freeSize > 0) heap_down(obj->freeHeap, obj->freeSize, 0);
    } else {
        id = obj->nextID++;
    }
    ensure_id(obj, id);
    free(obj->videos[id]);
    obj->videos[id] = strdup(video);
    obj->views[id] = obj->likes[id] = obj->dislikes[id] = 0;
    obj->used[id] = true;
    return id;
}

void videoSharingPlatformRemove(VideoSharingPlatform* obj, int videoId) {
    if (videoId < 0 || videoId >= obj->cap || !obj->used[videoId]) return;
    free(obj->videos[videoId]);
    obj->videos[videoId] = NULL;
    obj->used[videoId] = false;
    if (obj->freeSize == obj->freeCap) {
        obj->freeCap = obj->freeCap ? obj->freeCap * 2 : 8;
        obj->freeHeap = (int*)realloc(obj->freeHeap, (size_t)obj->freeCap * sizeof(int));
    }
    obj->freeHeap[obj->freeSize++] = videoId;
    heap_up(obj->freeHeap, obj->freeSize - 1);
}

char* videoSharingPlatformWatch(VideoSharingPlatform* obj, int videoId, int startMinute, int endMinute) {
    if (videoId < 0 || videoId >= obj->cap || !obj->used[videoId]) {
        char* r = (char*)malloc(3);
        strcpy(r, "-1");
        return r;
    }
    obj->views[videoId]++;
    char* v = obj->videos[videoId];
    int len = (int)strlen(v);
    if (startMinute >= len) {
        char* r = (char*)malloc(1);
        r[0] = '\0';
        return r;
    }
    if (endMinute >= len) endMinute = len - 1;
    int n = endMinute - startMinute + 1;
    char* r = (char*)malloc((size_t)n + 1);
    memcpy(r, v + startMinute, (size_t)n);
    r[n] = '\0';
    return r;
}

void videoSharingPlatformLike(VideoSharingPlatform* obj, int videoId) {
    if (videoId >= 0 && videoId < obj->cap && obj->used[videoId]) obj->likes[videoId]++;
}

void videoSharingPlatformDislike(VideoSharingPlatform* obj, int videoId) {
    if (videoId >= 0 && videoId < obj->cap && obj->used[videoId]) obj->dislikes[videoId]++;
}

int* videoSharingPlatformGetLikesAndDislikes(VideoSharingPlatform* obj, int videoId, int* returnSize) {
    if (videoId < 0 || videoId >= obj->cap || !obj->used[videoId]) {
        int* r = (int*)malloc(sizeof(int));
        r[0] = -1;
        *returnSize = 1;
        return r;
    }
    int* r = (int*)malloc(2 * sizeof(int));
    r[0] = obj->likes[videoId];
    r[1] = obj->dislikes[videoId];
    *returnSize = 2;
    return r;
}

int videoSharingPlatformGetViews(VideoSharingPlatform* obj, int videoId) {
    if (videoId < 0 || videoId >= obj->cap || !obj->used[videoId]) return -1;
    return obj->views[videoId];
}

void videoSharingPlatformFree(VideoSharingPlatform* obj) {
    for (int i = 0; i < obj->cap; i++) free(obj->videos[i]);
    free(obj->videos); free(obj->views); free(obj->likes); free(obj->dislikes);
    free(obj->used); free(obj->freeHeap); free(obj);
}

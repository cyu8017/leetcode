// LeetCode 1348 - Tweet Counts Per Frequency
// https://leetcode.com/problems/tweet-counts-per-frequency/

#include <stdlib.h>
#include <string.h>
#include <stdio.h>

typedef struct { char* name; int* times; int size; int cap; } TweetEntry;

typedef struct {
    TweetEntry* entries;
    int size;
    int cap;
} TweetCounts;

TweetCounts* tweetCountsCreate() {
    TweetCounts* obj = (TweetCounts*)calloc(1, sizeof(TweetCounts));
    obj->cap = 16;
    obj->entries = (TweetEntry*)calloc(obj->cap, sizeof(TweetEntry));
    return obj;
}

static TweetEntry* find_entry(TweetCounts* obj, char* tweetName) {
    for (int i = 0; i < obj->size; i++)
        if (strcmp(obj->entries[i].name, tweetName) == 0) return &obj->entries[i];
    if (obj->size == obj->cap) {
        obj->cap *= 2;
        obj->entries = (TweetEntry*)realloc(obj->entries, obj->cap * sizeof(TweetEntry));
    }
    TweetEntry* e = &obj->entries[obj->size++];
    e->name = (char*)malloc(strlen(tweetName) + 1);
    strcpy(e->name, tweetName);
    e->cap = 16; e->size = 0;
    e->times = (int*)malloc(e->cap * sizeof(int));
    return e;
}

void tweetCountsRecordTweet(TweetCounts* obj, char* tweetName, int time) {
    TweetEntry* e = find_entry(obj, tweetName);
    if (e->size == e->cap) {
        e->cap *= 2;
        e->times = (int*)realloc(e->times, e->cap * sizeof(int));
    }
    int i = e->size;
    while (i > 0 && e->times[i - 1] > time) {
        e->times[i] = e->times[i - 1];
        i--;
    }
    e->times[i] = time;
    e->size++;
}

static int lower_bound(int* a, int n, int x) {
    int lo = 0, hi = n;
    while (lo < hi) { int mid = lo + (hi - lo) / 2; if (a[mid] < x) lo = mid + 1; else hi = mid; }
    return lo;
}
static int upper_bound(int* a, int n, int x) {
    int lo = 0, hi = n;
    while (lo < hi) { int mid = lo + (hi - lo) / 2; if (a[mid] <= x) lo = mid + 1; else hi = mid; }
    return lo;
}

int* tweetCountsGetTweetCountsPerFrequency(TweetCounts* obj, char* freq, char* tweetName, int startTime, int endTime, int* retSize) {
    int size = 60;
    if (strcmp(freq, "hour") == 0) size = 3600;
    else if (strcmp(freq, "day") == 0) size = 86400;
    TweetEntry* e = find_entry(obj, tweetName);
    int count = (endTime - startTime) / size + 1;
    int* ans = (int*)malloc(count * sizeof(int));
    int idx = 0;
    for (int start = startTime; start <= endTime; start += size) {
        int end = start + size - 1;
        if (end > endTime) end = endTime;
        ans[idx++] = upper_bound(e->times, e->size, end) - lower_bound(e->times, e->size, start);
    }
    *retSize = idx;
    return ans;
}

void tweetCountsFree(TweetCounts* obj) {
    for (int i = 0; i < obj->size; i++) {
        free(obj->entries[i].name);
        free(obj->entries[i].times);
    }
    free(obj->entries);
    free(obj);
}

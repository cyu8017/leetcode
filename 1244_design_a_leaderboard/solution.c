// LeetCode 1244 - Design A Leaderboard
// https://leetcode.com/problems/design-a-leaderboard/

#include <stdlib.h>
#include <string.h>

typedef struct {
    int playerId;
    int score;
} Entry;

typedef struct {
    Entry* entries;
    int size;
    int capacity;
} Leaderboard;

Leaderboard* leaderboardCreate(void) {
    Leaderboard* obj = (Leaderboard*)malloc(sizeof(Leaderboard));
    obj->capacity = 16;
    obj->size = 0;
    obj->entries = (Entry*)malloc((size_t)obj->capacity * sizeof(Entry));
    return obj;
}

void leaderboardAddScore(Leaderboard* obj, int playerId, int score) {
    for (int i = 0; i < obj->size; i++) {
        if (obj->entries[i].playerId == playerId) {
            obj->entries[i].score += score;
            return;
        }
    }
    if (obj->size >= obj->capacity) {
        obj->capacity *= 2;
        obj->entries = (Entry*)realloc(obj->entries, (size_t)obj->capacity * sizeof(Entry));
    }
    obj->entries[obj->size++] = (Entry){playerId, score};
}

static int cmp_score_desc(const void* a, const void* b) {
    return ((const Entry*)b)->score - ((const Entry*)a)->score;
}

int leaderboardTop(Leaderboard* obj, int K) {
    Entry* copy = (Entry*)malloc((size_t)obj->size * sizeof(Entry));
    memcpy(copy, obj->entries, (size_t)obj->size * sizeof(Entry));
    qsort(copy, (size_t)obj->size, sizeof(Entry), cmp_score_desc);
    int total = 0;
    if (K > obj->size) K = obj->size;
    for (int i = 0; i < K; i++) total += copy[i].score;
    free(copy);
    return total;
}

void leaderboardReset(Leaderboard* obj, int playerId) {
    for (int i = 0; i < obj->size; i++) {
        if (obj->entries[i].playerId == playerId) {
            obj->entries[i] = obj->entries[obj->size - 1];
            obj->size--;
            return;
        }
    }
}

void leaderboardFree(Leaderboard* obj) {
    if (!obj) return;
    free(obj->entries);
    free(obj);
}

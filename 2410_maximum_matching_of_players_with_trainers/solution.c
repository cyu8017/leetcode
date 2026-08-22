// LeetCode 2410 - Maximum Matching of Players With Trainers
// https://leetcode.com/problems/maximum-matching-of-players-with-trainers/

#include <stdlib.h>

static int cmpInt(const void* a, const void* b) { return *(const int*)a - *(const int*)b; }

int matchPlayersAndTrainers(int* players, int playersSize, int* trainers, int trainersSize) {
    qsort(players, (size_t)playersSize, sizeof(int), cmpInt);
    qsort(trainers, (size_t)trainersSize, sizeof(int), cmpInt);
    int i = 0, j = 0, ans = 0;
    while (i < playersSize && j < trainersSize) {
        if (players[i] <= trainers[j]) { ans++; i++; j++; }
        else j++;
    }
    return ans;
}

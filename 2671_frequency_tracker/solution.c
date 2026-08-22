// LeetCode 2671 - Frequency Tracker
// https://leetcode.com/problems/frequency-tracker/

#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

#define FT_N 100003

typedef struct {
    int* freq;   /* number -> frequency */
    int* count;  /* frequency -> how many numbers have it */
} FrequencyTracker;

FrequencyTracker* frequencyTrackerCreate(void) {
    FrequencyTracker* obj = (FrequencyTracker*)malloc(sizeof(FrequencyTracker));
    obj->freq = (int*)calloc(FT_N, sizeof(int));
    obj->count = (int*)calloc(FT_N, sizeof(int));
    return obj;
}

void frequencyTrackerAdd(FrequencyTracker* obj, int number) {
    int old = obj->freq[number];
    if (old > 0) obj->count[old]--;
    obj->freq[number] = old + 1;
    obj->count[old + 1]++;
}

void frequencyTrackerDeleteOne(FrequencyTracker* obj, int number) {
    int old = obj->freq[number];
    if (old == 0) return;
    obj->count[old]--;
    obj->freq[number] = old - 1;
    if (old - 1 > 0) obj->count[old - 1]++;
}

bool frequencyTrackerHasFrequency(FrequencyTracker* obj, int frequency) {
    return frequency > 0 && frequency < FT_N && obj->count[frequency] > 0;
}

void frequencyTrackerFree(FrequencyTracker* obj) {
    if (!obj) return;
    free(obj->freq);
    free(obj->count);
    free(obj);
}

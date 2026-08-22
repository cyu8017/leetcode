// LeetCode 3709 - Design Exam Scores Tracker
// https://leetcode.com/problems/design-exam-scores-tracker/

#include <stdlib.h>

typedef struct {
    int* times;
    long long* pre;
    int size;
    int cap;
} ExamTracker;

ExamTracker* examTrackerCreate(void) {
    ExamTracker* obj = (ExamTracker*)malloc(sizeof(ExamTracker));
    obj->cap = 16;
    obj->size = 1;
    obj->times = (int*)malloc((size_t)obj->cap * sizeof(int));
    obj->pre = (long long*)malloc((size_t)obj->cap * sizeof(long long));
    obj->times[0] = 0;
    obj->pre[0] = 0;
    return obj;
}

void examTrackerRecord(ExamTracker* obj, int time, int score) {
    if (obj->size == obj->cap) {
        obj->cap *= 2;
        obj->times = (int*)realloc(obj->times, (size_t)obj->cap * sizeof(int));
        obj->pre = (long long*)realloc(obj->pre, (size_t)obj->cap * sizeof(long long));
    }
    obj->times[obj->size] = time;
    obj->pre[obj->size] = obj->pre[obj->size - 1] + score;
    obj->size++;
}

static int lowerBound(int* a, int n, int x) {
    int lo = 0, hi = n;
    while (lo < hi) {
        int mid = (lo + hi) / 2;
        if (a[mid] < x) lo = mid + 1;
        else hi = mid;
    }
    return lo;
}

long long examTrackerTotalScore(ExamTracker* obj, int startTime, int endTime) {
    int l = lowerBound(obj->times, obj->size, startTime) - 1;
    int r = lowerBound(obj->times, obj->size, endTime + 1) - 1;
    return obj->pre[r] - obj->pre[l];
}

void examTrackerFree(ExamTracker* obj) {
    if (!obj) return;
    free(obj->times);
    free(obj->pre);
    free(obj);
}

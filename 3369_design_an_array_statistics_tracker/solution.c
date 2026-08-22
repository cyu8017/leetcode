// LeetCode 3369 - Design an Array Statistics Tracker
// https://leetcode.com/problems/design-an-array-statistics-tracker/

#include <stdlib.h>
#include <string.h>

typedef struct { int key, val, used; } HM;
typedef struct {
    int* arr; int n, cap;
    long long sum;
    HM* freq; int fcap;
    int modeFreq;
    int* modes; int mn, mcap;
} StatisticsTracker;

static int hm_get(HM* t, int cap, int key) {
    unsigned h = (unsigned)key * 2654435761u % (unsigned)cap;
    for (;;) { if (!t[h].used) return 0; if (t[h].key == key) return t[h].val; h = (h + 1) % (unsigned)cap; }
}
static void hm_add(HM* t, int cap, int key, int d) {
    unsigned h = (unsigned)key * 2654435761u % (unsigned)cap;
    for (;;) {
        if (!t[h].used) { t[h].used = 1; t[h].key = key; t[h].val = d; return; }
        if (t[h].key == key) { t[h].val += d; if (t[h].val == 0) t[h].used = 0; return; }
        h = (h + 1) % (unsigned)cap;
    }
}

StatisticsTracker* statisticsTrackerCreate(void) {
    StatisticsTracker* o = (StatisticsTracker*)calloc(1, sizeof(StatisticsTracker));
    o->cap = 16; o->arr = (int*)malloc(16 * sizeof(int));
    o->fcap = 1024; o->freq = (HM*)calloc(1024, sizeof(HM));
    o->mcap = 16; o->modes = (int*)malloc(16 * sizeof(int));
    return o;
}

static void rebuild_modes(StatisticsTracker* obj) {
    obj->modeFreq = 0; obj->mn = 0;
    for (int i = 0; i < obj->fcap; i++) if (obj->freq[i].used) {
        int v = obj->freq[i].key, f = obj->freq[i].val;
        if (f > obj->modeFreq) { obj->modeFreq = f; obj->mn = 0; obj->modes[obj->mn++] = v; }
        else if (f == obj->modeFreq) {
            if (obj->mn == obj->mcap) { obj->mcap *= 2; obj->modes = (int*)realloc(obj->modes, obj->mcap * sizeof(int)); }
            obj->modes[obj->mn++] = v;
        }
    }
}

void statisticsTrackerAddNumber(StatisticsTracker* obj, int num) {
    if (obj->n == obj->cap) { obj->cap *= 2; obj->arr = (int*)realloc(obj->arr, obj->cap * sizeof(int)); }
    obj->arr[obj->n++] = num;
    obj->sum += num;
    hm_add(obj->freq, obj->fcap, num, 1);
    int f = hm_get(obj->freq, obj->fcap, num);
    if (f > obj->modeFreq) { obj->modeFreq = f; obj->mn = 1; obj->modes[0] = num; }
    else if (f == obj->modeFreq) {
        int found = 0; for (int i = 0; i < obj->mn; i++) if (obj->modes[i] == num) found = 1;
        if (!found) {
            if (obj->mn == obj->mcap) { obj->mcap *= 2; obj->modes = (int*)realloc(obj->modes, obj->mcap * sizeof(int)); }
            obj->modes[obj->mn++] = num;
        }
    }
}

void statisticsTrackerRemoveFirst(StatisticsTracker* obj) {
    if (obj->n == 0) return;
    int num = obj->arr[0];
    memmove(obj->arr, obj->arr + 1, (obj->n - 1) * sizeof(int));
    obj->n--;
    obj->sum -= num;
    hm_add(obj->freq, obj->fcap, num, -1);
    rebuild_modes(obj);
}

int statisticsTrackerGetMean(StatisticsTracker* obj) {
    if (obj->n == 0) return 0;
    return (int)(obj->sum / obj->n);
}

static int cmp_int(const void* a, const void* b) { return *(const int*)a - *(const int*)b; }

int statisticsTrackerGetMedian(StatisticsTracker* obj) {
    int n = obj->n;
    int* tmp = (int*)malloc(n * sizeof(int));
    memcpy(tmp, obj->arr, n * sizeof(int));
    qsort(tmp, n, sizeof(int), cmp_int);
    int ans = (n % 2 == 1) ? tmp[n / 2] : tmp[n / 2 - 1];
    free(tmp);
    return ans;
}

int statisticsTrackerGetMode(StatisticsTracker* obj) {
    long long best = 1000000000000000000LL;
    for (int i = 0; i < obj->mn; i++) if (obj->modes[i] < best) best = obj->modes[i];
    if (best == 1000000000000000000LL) return 0;
    return (int)best;
}

void statisticsTrackerFree(StatisticsTracker* obj) {
    free(obj->arr); free(obj->freq); free(obj->modes); free(obj);
}

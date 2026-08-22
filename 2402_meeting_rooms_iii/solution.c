// LeetCode 2402 - Meeting Rooms III
// https://leetcode.com/problems/meeting-rooms-iii/

#include <stdlib.h>

typedef struct { long long v; } I64H;
typedef struct { long long end; long long room; } RH;

static void i64push(long long* h, int* sz, long long x) {
    int i = (*sz)++;
    h[i] = x;
    while (i > 0) { int p = (i-1)/2; if (h[p] <= h[i]) break; long long t=h[p]; h[p]=h[i]; h[i]=t; i=p; }
}
static long long i64pop(long long* h, int* sz) {
    long long res = h[0]; h[0] = h[--(*sz)];
    int i = 0;
    while (1) {
        int l=2*i+1,r=2*i+2,sm=i;
        if (l<*sz && h[l]<h[sm]) sm=l;
        if (r<*sz && h[r]<h[sm]) sm=r;
        if (sm==i) break;
        long long t=h[i]; h[i]=h[sm]; h[sm]=t; i=sm;
    }
    return res;
}
static int rhLess(RH a, RH b) { return a.end < b.end || (a.end == b.end && a.room < b.room); }
static void rhpush(RH* h, int* sz, RH x) {
    int i = (*sz)++;
    h[i] = x;
    while (i > 0) { int p=(i-1)/2; if (!rhLess(h[i], h[p])) break; RH t=h[p]; h[p]=h[i]; h[i]=t; i=p; }
}
static RH rhpop(RH* h, int* sz) {
    RH res = h[0]; h[0] = h[--(*sz)];
    int i = 0;
    while (1) {
        int l=2*i+1,r=2*i+2,sm=i;
        if (l<*sz && rhLess(h[l], h[sm])) sm=l;
        if (r<*sz && rhLess(h[r], h[sm])) sm=r;
        if (sm==i) break;
        RH t=h[i]; h[i]=h[sm]; h[sm]=t; i=sm;
    }
    return res;
}

static int cmpMeet(const void* a, const void* b) {
    int* const* pa = (int* const*)a; int* const* pb = (int* const*)b;
    return (*pa)[0] - (*pb)[0];
}

int mostBooked(int n, int** meetings, int meetingsSize, int* meetingsColSize) {
    (void)meetingsColSize;
    qsort(meetings, (size_t)meetingsSize, sizeof(int*), cmpMeet);
    long long* freeH = (long long*)malloc((size_t)n * sizeof(long long));
    int freeSz = 0;
    for (int i = 0; i < n; i++) i64push(freeH, &freeSz, i);
    RH* busy = (RH*)malloc((size_t)meetingsSize * sizeof(RH));
    int busySz = 0;
    int* cnt = (int*)calloc((size_t)n, sizeof(int));
    for (int mi = 0; mi < meetingsSize; mi++) {
        long long start = meetings[mi][0], end = meetings[mi][1];
        while (busySz > 0 && busy[0].end <= start) {
            RH top = rhpop(busy, &busySz);
            i64push(freeH, &freeSz, top.room);
        }
        long long dur = end - start, room, begin;
        if (freeSz > 0) { room = i64pop(freeH, &freeSz); begin = start; }
        else { RH top = rhpop(busy, &busySz); begin = top.end; room = top.room; }
        rhpush(busy, &busySz, (RH){begin + dur, room});
        cnt[room]++;
    }
    int ans = 0;
    for (int i = 1; i < n; i++) if (cnt[i] > cnt[ans]) ans = i;
    free(freeH); free(busy); free(cnt);
    return ans;
}

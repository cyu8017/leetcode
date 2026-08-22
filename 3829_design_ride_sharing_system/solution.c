// LeetCode 3829 - Design Ride Sharing System
// https://leetcode.com/problems/design-ride-sharing-system/

#include <stdlib.h>
#include <stdbool.h>

typedef struct { int time; int id; bool active; } Entry3829;

typedef struct {
    int t;
    Entry3829* riders;
    int rn, rcap;
    Entry3829* drivers;
    int dn, dcap;
    int* riderTimes; /* map riderId -> time, sparse via parallel arrays */
    int* riderIds;
    int mapn, mapcap;
} RideSharingSystem;

static void map_set(RideSharingSystem* s, int riderId, int time) {
    for (int i = 0; i < s->mapn; i++) if (s->riderIds[i] == riderId) { s->riderTimes[i] = time; return; }
    if (s->mapn == s->mapcap) {
        s->mapcap = s->mapcap ? s->mapcap * 2 : 8;
        s->riderIds = (int*)realloc(s->riderIds, (size_t)s->mapcap * sizeof(int));
        s->riderTimes = (int*)realloc(s->riderTimes, (size_t)s->mapcap * sizeof(int));
    }
    s->riderIds[s->mapn] = riderId;
    s->riderTimes[s->mapn] = time;
    s->mapn++;
}

static bool map_get(RideSharingSystem* s, int riderId, int* time) {
    for (int i = 0; i < s->mapn; i++) if (s->riderIds[i] == riderId) { *time = s->riderTimes[i]; return true; }
    return false;
}

RideSharingSystem* rideSharingSystemCreate(void) {
    return (RideSharingSystem*)calloc(1, sizeof(RideSharingSystem));
}

void rideSharingSystemAddRider(RideSharingSystem* obj, int riderId) {
    if (obj->rn == obj->rcap) {
        obj->rcap = obj->rcap ? obj->rcap * 2 : 8;
        obj->riders = (Entry3829*)realloc(obj->riders, (size_t)obj->rcap * sizeof(Entry3829));
    }
    obj->riders[obj->rn++] = (Entry3829){obj->t, riderId, true};
    map_set(obj, riderId, obj->t);
    obj->t++;
}

void rideSharingSystemAddDriver(RideSharingSystem* obj, int driverId) {
    if (obj->dn == obj->dcap) {
        obj->dcap = obj->dcap ? obj->dcap * 2 : 8;
        obj->drivers = (Entry3829*)realloc(obj->drivers, (size_t)obj->dcap * sizeof(Entry3829));
    }
    obj->drivers[obj->dn++] = (Entry3829){obj->t, driverId, true};
    obj->t++;
}

int* rideSharingSystemMatchDriverWithRider(RideSharingSystem* obj, int* returnSize) {
    int* ans = (int*)malloc(2 * sizeof(int));
    int ri = -1, di = -1;
    for (int i = 0; i < obj->rn; i++) if (obj->riders[i].active) { if (ri < 0 || obj->riders[i].time < obj->riders[ri].time) ri = i; }
    for (int i = 0; i < obj->dn; i++) if (obj->drivers[i].active) { if (di < 0 || obj->drivers[i].time < obj->drivers[di].time) di = i; }
    if (ri < 0 || di < 0) { ans[0] = -1; ans[1] = -1; *returnSize = 2; return ans; }
    ans[0] = obj->drivers[di].id;
    ans[1] = obj->riders[ri].id;
    obj->drivers[di].active = false;
    obj->riders[ri].active = false;
    *returnSize = 2;
    return ans;
}

void rideSharingSystemCancelRider(RideSharingSystem* obj, int riderId) {
    int time;
    if (!map_get(obj, riderId, &time)) return;
    for (int i = 0; i < obj->rn; i++) {
        if (obj->riders[i].active && obj->riders[i].time == time && obj->riders[i].id == riderId) {
            obj->riders[i].active = false;
            return;
        }
    }
}

void rideSharingSystemFree(RideSharingSystem* obj) {
    if (!obj) return;
    free(obj->riders); free(obj->drivers); free(obj->riderIds); free(obj->riderTimes);
    free(obj);
}

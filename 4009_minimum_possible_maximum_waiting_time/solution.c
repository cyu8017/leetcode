// LeetCode 4009 - Minimum Possible Maximum Waiting Time
// https://leetcode.com/problems/minimum-possible-maximum-waiting-time/

#include <stdlib.h>
#include <string.h>
#include <limits.h>

static int* dem4009;
static int n4009;
static int W4009;
static int bestServe4009;

/* memo: pack i,f0,f1,d0,d1 into key via open addressing */
#define MEMO_CAP 200003
static int memoKey4009[MEMO_CAP];
static char memoVal4009[MEMO_CAP]; /* 0 unseen, 1 false, 2 true for can; for max: store served+1 */
static int packKey4009(int i, int f0, int f1, int d0, int d1) {
    /* unique enough for constraints */
    return (((i * 51 + f0) * 51 + f1) * 21 + d0) * 21 + d1;
}

static void clearMemo4009(void) {
    memset(memoKey4009, -1, sizeof(memoKey4009));
    memset(memoVal4009, 0, sizeof(memoVal4009));
}

static int memoGet4009(int key, int* out) {
    int h = (int)((unsigned)key % MEMO_CAP);
    for (int k = 0; k < MEMO_CAP; k++) {
        int idx = (h + k) % MEMO_CAP;
        if (memoKey4009[idx] == -1) return 0;
        if (memoKey4009[idx] == key) {
            *out = (int)memoVal4009[idx];
            return 1;
        }
    }
    return 0;
}

static void memoSet4009(int key, int val) {
    int h = (int)((unsigned)key % MEMO_CAP);
    for (int k = 0; k < MEMO_CAP; k++) {
        int idx = (h + k) % MEMO_CAP;
        if (memoKey4009[idx] == -1 || memoKey4009[idx] == key) {
            memoKey4009[idx] = key;
            memoVal4009[idx] = (char)val;
            return;
        }
    }
}

static int maxServe4009(int i, int f0, int f1, int d0, int d1) {
    if (i == n4009) return i;
    int key = packKey4009(i, f0, f1, d0, d1);
    int cached;
    if (memoGet4009(key, &cached)) return cached;

    int need = dem4009[i];
    int can0 = f0 >= need;
    int can1 = f1 >= need;
    int best = i;
    if (!can0 && !can1) {
        memoSet4009(key, best);
        return best;
    }
    if (can0) {
        int nd1 = d1 > d0 ? d1 - d0 : 0;
        int r = maxServe4009(i + 1, f0 - need, f1, need, nd1);
        if (r > best) best = r;
    }
    if (can1) {
        int nd0 = d0 > d1 ? d0 - d1 : 0;
        int r = maxServe4009(i + 1, f0, f1 - need, nd0, need);
        if (r > best) best = r;
    }
    memoSet4009(key, best);
    return best;
}

static int canWithW4009(int i, int f0, int f1, int d0, int d1) {
    if (i >= bestServe4009) return 1;
    if (i == n4009) return 1;
    int key = packKey4009(i, f0, f1, d0, d1);
    int cached;
    if (memoGet4009(key, &cached)) return cached == 2;

    int need = dem4009[i];
    int can0 = f0 >= need;
    int can1 = f1 >= need;
    int ok = 0;
    if (!can0 && !can1) {
        memoSet4009(key, 1);
        return 0;
    }
    if (can0 && d0 <= W4009) {
        int nd1 = d1 > d0 ? d1 - d0 : 0;
        if (canWithW4009(i + 1, f0 - need, f1, need, nd1)) ok = 1;
    }
    if (!ok && can1 && d1 <= W4009) {
        int nd0 = d0 > d1 ? d0 - d1 : 0;
        if (canWithW4009(i + 1, f0, f1 - need, nd0, need)) ok = 1;
    }
    memoSet4009(key, ok ? 2 : 1);
    return ok;
}

int minMaxWaitingTime(int* demand, int demandSize, int* fuel, int fuelSize) {
    (void)fuelSize;
    dem4009 = demand;
    n4009 = demandSize;
    int f0 = fuel[0], f1 = fuel[1];

    if (f0 < demand[0] && f1 < demand[0]) return -1;

    clearMemo4009();
    bestServe4009 = maxServe4009(0, f0, f1, 0, 0);
    if (bestServe4009 == 0) return -1;

    int lo = 0, hi = 0;
    for (int i = 0; i < demandSize; i++) hi += demand[i];

    int ans = hi;
    while (lo <= hi) {
        int mid = (lo + hi) / 2;
        W4009 = mid;
        clearMemo4009();
        if (canWithW4009(0, f0, f1, 0, 0)) {
            ans = mid;
            hi = mid - 1;
        } else {
            lo = mid + 1;
        }
    }
    return ans;
}

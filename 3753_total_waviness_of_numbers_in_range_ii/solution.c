// LeetCode 3753 - Total Waviness of Numbers in Range II
// https://leetcode.com/problems/total-waviness-of-numbers-in-range-ii/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

typedef struct { long long count, sum; } WR;

static int digits[20], dlen;
typedef struct { int position, secondLast, last; bool started; WR val; char used; } Memo;
#define MCAP 20000
static Memo memo[MCAP];
static int memoN;

static WR dfs(int position, int secondLast, int last, bool started, bool tight);

static WR lookupOrNeg(int position, int secondLast, int last, bool started, int* found) {
    for (int i = 0; i < memoN; i++) {
        if (memo[i].position == position && memo[i].secondLast == secondLast &&
            memo[i].last == last && memo[i].started == started) {
            *found = 1; return memo[i].val;
        }
    }
    *found = 0; return (WR){0,0};
}
static void store(int position, int secondLast, int last, bool started, WR val) {
    memo[memoN++] = (Memo){position, secondLast, last, started, val, 1};
}

static WR dfs(int position, int secondLast, int last, bool started, bool tight) {
    if (position == dlen) return (WR){1, 0};
    if (!tight) {
        int found; WR cached = lookupOrNeg(position, secondLast, last, started, &found);
        if (found) return cached;
    }
    int upper = tight ? digits[position] : 9;
    WR result = {0, 0};
    for (int digit = 0; digit <= upper; digit++) {
        bool nextTight = tight && digit == upper;
        int nextSecondLast = secondLast, nextLast = last;
        bool nextStarted = started || digit != 0;
        long long add = 0;
        if (!nextStarted) { nextSecondLast = 10; nextLast = 10; }
        else if (!started) { nextSecondLast = 10; nextLast = digit; }
        else {
            if (secondLast != 10 &&
                ((last > secondLast && last > digit) || (last < secondLast && last < digit)))
                add = 1;
            nextSecondLast = last; nextLast = digit;
        }
        WR child = dfs(position + 1, nextSecondLast, nextLast, nextStarted, nextTight);
        result.count += child.count;
        result.sum += child.sum + add * child.count;
    }
    if (!tight) store(position, secondLast, last, started, result);
    return result;
}

static long long wavinessUpTo(long long limit) {
    if (limit < 0) return 0;
    dlen = 0;
    if (limit == 0) digits[dlen++] = 0;
    else {
        long long v = limit;
        int tmp[20], tn = 0;
        while (v > 0) { tmp[tn++] = (int)(v % 10); v /= 10; }
        for (int i = tn - 1; i >= 0; i--) digits[dlen++] = tmp[i];
    }
    memoN = 0;
    return dfs(0, 10, 10, false, true).sum;
}

long long totalWaviness(long long a, long long b) {
    return wavinessUpTo(b) - wavinessUpTo(a - 1);
}

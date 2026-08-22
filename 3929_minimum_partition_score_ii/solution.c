// LeetCode 3929 - Minimum Partition Score II
// https://leetcode.com/problems/minimum-partition-score-ii/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

typedef struct {
    long long slope, intercept;
    int count;
    bool valid;
} Line3929;

typedef struct {
    long long value;
    int count;
    bool valid;
} State3929;

static long long* prefix3929;
static Line3929* tree3929;
static int n3929;

static State3929 better3929(State3929 a, State3929 b) {
    if (!a.valid) return b;
    if (!b.valid) return a;
    if (a.value != b.value) return a.value < b.value ? a : b;
    return a.count >= b.count ? a : b;
}

static State3929 evaluate3929(Line3929 line, long long x) {
    if (!line.valid) return (State3929){0, 0, false};
    return (State3929){line.slope * x + line.intercept, line.count, true};
}

static void insert3929(int node, int left, int right, Line3929 line) {
    if (!tree3929[node].valid) { tree3929[node] = line; return; }
    int mid = (left + right) / 2;
    long long xLeft = prefix3929[left], xMid = prefix3929[mid];
    State3929 leftBetter = better3929(evaluate3929(line, xLeft), evaluate3929(tree3929[node], xLeft));
    State3929 midBetter = better3929(evaluate3929(line, xMid), evaluate3929(tree3929[node], xMid));
    bool lineWinsLeft = leftBetter.value == evaluate3929(line, xLeft).value && leftBetter.count == line.count;
    bool lineWinsMid = midBetter.value == evaluate3929(line, xMid).value && midBetter.count == line.count;
    if (lineWinsMid) {
        Line3929 tmp = tree3929[node];
        tree3929[node] = line;
        line = tmp;
    }
    if (left == right) return;
    if (lineWinsLeft != lineWinsMid) insert3929(node * 2, left, mid, line);
    else insert3929(node * 2 + 1, mid + 1, right, line);
}

static State3929 query3929(int node, int left, int right, int index) {
    State3929 result = evaluate3929(tree3929[node], prefix3929[index]);
    if (left == right) return result;
    int mid = (left + right) / 2;
    if (index <= mid) return better3929(result, query3929(node * 2, left, mid, index));
    return better3929(result, query3929(node * 2 + 1, mid + 1, right, index));
}

static State3929 run3929(long long penalty) {
    memset(tree3929, 0, (size_t)(4 * (n3929 + 1)) * sizeof(Line3929));
    insert3929(1, 0, n3929, (Line3929){0, 0, 0, true});
    State3929 current = {0, 0, false};
    for (int i = 1; i <= n3929; i++) {
        State3929 best = query3929(1, 0, n3929, i);
        long long x = prefix3929[i];
        current = (State3929){best.value + x * x + x + penalty, best.count + 1, true};
        insert3929(1, 0, n3929, (Line3929){-2 * x, current.value + x * x - x, current.count, true});
    }
    return current;
}

long long minPartitionScore(int* nums, int numsSize, int k) {
    n3929 = numsSize;
    prefix3929 = calloc((size_t)(n3929 + 1), sizeof(long long));
    for (int i = 0; i < n3929; i++) prefix3929[i + 1] = prefix3929[i] + nums[i];
    tree3929 = calloc((size_t)(4 * (n3929 + 1)), sizeof(Line3929));
    long long bound = prefix3929[n3929] * prefix3929[n3929] + prefix3929[n3929] + 1;
    long long low = 0, high = bound;
    while (low < high) {
        long long mid = low + (high - low + 1) / 2;
        if (run3929(mid).count >= k) low = mid;
        else high = mid - 1;
    }
    State3929 state = run3929(low);
    long long ans = (state.value - low * k) / 2;
    free(prefix3929); free(tree3929);
    return ans;
}

// LeetCode 3357 - Minimize the Maximum Adjacent Element Difference
// https://leetcode.com/problems/minimize-the-maximum-adjacent-element-difference/

static int abs3357(int x) { return x < 0 ? -x : x; }
static int* g_nums; static int g_n;

static int ok3357(int d) {
    int prev = -1;
    for (int i = 0; i < g_n; i++) {
        if (g_nums[i] != -1) {
            if (prev != -1 && abs3357(g_nums[i] - prev) > d) return 0;
            prev = g_nums[i];
            continue;
        }
        int j = i;
        while (j < g_n && g_nums[j] == -1) j++;
        int left = prev, right = j < g_n ? g_nums[j] : -1;
        int gap = j - i;
        if (left == -1 && right == -1) return 1;
        if (left == -1 || right == -1) { prev = -1; i = j - 1; continue; }
        if (abs3357(left - right) > d * (gap + 1)) return 0;
        prev = -1;
        i = j - 1;
    }
    return 1;
}

int minDifference(int* nums, int numsSize) {
    g_nums = nums; g_n = numsSize;
    int lo = 0, hi = 1000000000;
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        if (ok3357(mid)) hi = mid; else lo = mid + 1;
    }
    return lo;
}

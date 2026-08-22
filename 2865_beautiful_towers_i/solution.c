// LeetCode 2865 - Beautiful Towers I
// https://leetcode.com/problems/beautiful-towers-i/

long long maximumSumOfHeights(int* heights, int heightsSize) {
    int n = heightsSize;
    long long ans = 0;
    for (int peak = 0; peak < n; peak++) {
        long long sum = heights[peak];
        int mn = heights[peak];
        for (int i = peak - 1; i >= 0; i--) {
            if (heights[i] < mn) mn = heights[i];
            sum += mn;
        }
        mn = heights[peak];
        for (int i = peak + 1; i < n; i++) {
            if (heights[i] < mn) mn = heights[i];
            sum += mn;
        }
        if (sum > ans) ans = sum;
    }
    return ans;
}

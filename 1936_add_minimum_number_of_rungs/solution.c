// LeetCode 1936 - Add Minimum Number of Rungs
// https://leetcode.com/problems/add-minimum-number-of-rungs/

int addRungs(int* rungs, int rungsSize, int dist) {
    int prev = 0, ans = 0;
    for (int i = 0; i < rungsSize; i++) {
        int gap = rungs[i] - prev;
        if (gap > dist) ans += (gap - 1) / dist;
        prev = rungs[i];
    }
    return ans;
}

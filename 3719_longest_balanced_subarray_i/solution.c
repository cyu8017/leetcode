// LeetCode 3719 - Longest Balanced Subarray I
// https://leetcode.com/problems/longest-balanced-subarray-i/

int longestBalanced(int* nums, int numsSize) {
    int ans = 0;
    for (int i = 0; i < numsSize; i++) {
        int keys[400], kn = 0;
        int cnt[2] = {0};
        for (int j = i; j < numsSize; j++) {
            int x = nums[j];
            int found = 0;
            for (int t = 0; t < kn; t++) if (keys[t] == x) { found = 1; break; }
            if (!found) {
                keys[kn++] = x;
                cnt[x & 1]++;
            }
            if (cnt[0] == cnt[1] && j - i + 1 > ans) ans = j - i + 1;
        }
    }
    return ans;
}

// LeetCode 3095 - Shortest Subarray With OR at Least K I
// https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-i/

int minimumSubarrayLength(int* nums, int numsSize, int k) {
    int cnt[32] = {0};
    int ans = numsSize + 1, s = 0, i = 0;
    for (int j = 0; j < numsSize; j++) {
        int x = nums[j];
        s |= x;
        for (int h = 0; h < 32; h++) if ((x >> h) & 1) cnt[h]++;
        while (s >= k && i <= j) {
            if (j - i + 1 < ans) ans = j - i + 1;
            for (int h = 0; h < 32; h++) {
                if ((nums[i] >> h) & 1) {
                    cnt[h]--;
                    if (cnt[h] == 0) s ^= 1 << h;
                }
            }
            i++;
        }
    }
    return ans == numsSize + 1 ? -1 : ans;
}

// LeetCode 3471 - Find the Largest Almost Missing Integer
// https://leetcode.com/problems/find-the-largest-almost-missing-integer/

int largestInteger(int* nums, int numsSize, int k) {
    int cnt[51];
    for (int i = 0; i < 51; i++) cnt[i] = 0;
    for (int i = 0; i + k <= numsSize; i++) {
        int seen[51] = {0};
        for (int j = i; j < i + k; j++) {
            int x = nums[j];
            if (x >= 0 && x <= 50) seen[x] = 1;
        }
        for (int x = 0; x <= 50; x++) {
            if (seen[x]) cnt[x]++;
        }
    }
    int ans = -1;
    for (int x = 0; x <= 50; x++) {
        if (cnt[x] == 1 && x > ans) ans = x;
    }
    return ans;
}

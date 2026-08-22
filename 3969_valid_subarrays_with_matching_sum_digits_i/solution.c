// LeetCode 3969 - Valid Subarrays With Matching Sum Digits I
// https://leetcode.com/problems/valid-subarrays-with-matching-sum-digits-i/

int countValidSubarrays(int* nums, int numsSize, int x) {
    int ans = 0, n = numsSize;
    for (int l = 0; l < n; l++) {
        long long s = 0;
        for (int r = l; r < n; r++) {
            s += nums[r];
            if (s % 10 == x) {
                long long t = s;
                while (t >= 10) t /= 10;
                if ((int)t == x) ans++;
            }
        }
    }
    return ans;
}

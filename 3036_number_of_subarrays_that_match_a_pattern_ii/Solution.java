// LeetCode 3036 - Number of Subarrays That Match a Pattern II
// https://leetcode.com/problems/number-of-subarrays-that-match-a-pattern-ii/

class Solution {
    public int countMatchingSubarrays(int[] nums, int[] pattern) {
        int N = pattern.length;
        int[] ps = new int[N + 1];
        ps[0] = -1;
        ps[1] = 0;
        for (int i = 2, p = 0; i <= N; i++) {
            int x = pattern[i - 1];
            while (p >= 0 && pattern[p] != x) p = ps[p];
            p++;
            ps[i] = p;
        }
        int res = 0, M = nums.length;
        for (int i = 1, p = 0; i < M; i++) {
            int t = nums[i] - nums[i - 1];
            if (t > 0) t = 1;
            else if (t < 0) t = -1;
            while (p >= 0 && pattern[p] != t) p = ps[p];
            if (++p == N) {
                res++;
                p = ps[p];
            }
        }
        return res;
    }
}

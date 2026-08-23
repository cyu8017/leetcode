// LeetCode 3171 - Find Subarray With Bitwise OR Closest to K
// https://leetcode.com/problems/find-subarray-with-bitwise-or-closest-to-k/

class Solution {
    public int minimumDifference(int[] nums, int k) {
        int mx = 0;
        for (int v : nums) mx = Math.max(mx, v);
        int m = mx == 0 ? 1 : 32 - leadingZeroCount(mx);
        int[] cnt = new int[m];
        int ans = Integer.MAX_VALUE, s = 0, i = 0;
        for (int j = 0; j < nums.length; j++) {
            int x = nums[j];
            s |= x;
            ans = Math.min(ans, Math.abs(s - k));
            for (int h = 0; h < m; h++) if (((x >> h) & 1) != 0) cnt[h]++;
            while (i < j && s > k) {
                int y = nums[i];
                for (int h = 0; h < m; h++) {
                    if (((y >> h) & 1) != 0) {
                        if (--cnt[h] == 0) s ^= 1 << h;
                    }
                }
                ans = Math.min(ans, Math.abs(s - k));
                i++;
            }
        }
        return ans;
    }

    static int leadingZeroCount(int x) {
        if (x == 0) return 32;
        int n = 0;
        for (int bit = 31; bit >= 0; bit--) {
            if (((x >> bit) & 1) != 0) break;
            n++;
        }
        return n;
    }
}

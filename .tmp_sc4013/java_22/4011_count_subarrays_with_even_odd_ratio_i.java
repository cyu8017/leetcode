// CONFIG class=Solution method=countRatioSubarrays types=None
// LeetCode 4011 - Count Subarrays With Even Odd Ratio I
// https://leetcode.com/problems/count-subarrays-with-even-odd-ratio-i/

class Solution {
    public int countRatioSubarrays(int[] nums, int a, int b) {
        int n = nums.length;
        long ans = 0;
        for (int i = 0; i < n; i++) {
            int y = 0;
            for (int j = i; j < n; j++) {
                y += nums[j] % 2;
                int x = j - i + 1 - y;
                if (y > 0 && (long)x * b <= (long)y * a) ans++;
            }
        }
        return (int)ans;
    }
}

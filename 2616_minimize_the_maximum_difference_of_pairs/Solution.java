// LeetCode 2616 - Minimize the Maximum Difference of Pairs
// https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/

import java.util.Arrays;

class Solution {
    public int minimizeMax(int[] nums, int p) {
        Arrays.sort(nums);
        int lo = 0, hi = nums[nums.length - 1] - nums[0];
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (ok(nums, p, mid)) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }

    private boolean ok(int[] nums, int p, int d) {
        int cnt = 0;
        for (int i = 0; i + 1 < nums.length;) {
            if (nums[i + 1] - nums[i] <= d) {
                cnt++;
                i += 2;
            } else i++;
        }
        return cnt >= p;
    }
}

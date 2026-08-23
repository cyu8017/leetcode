// LeetCode 3684 - Maximize Sum of At Most K Distinct Elements
// https://leetcode.com/problems/maximize-sum-of-at-most-k-distinct-elements/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public int[] maxKDistinct(int[] nums, int k) {
        Arrays.sort(nums);
        int n = nums.length;
        List<Integer> ans = new ArrayList<>();
        for (int i = n - 1; i >= 0; i--) {
            if (i + 1 < n && nums[i] == nums[i + 1]) continue;
            ans.add(nums[i]);
            if (--k == 0) break;
        }
        int[] res = new int[ans.size()];
        for (int i = 0; i < ans.size(); i++) res[i] = ans.get(i);
        return res;
    }
}

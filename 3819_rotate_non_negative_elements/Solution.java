// LeetCode 3819 - Rotate Non Negative Elements
// https://leetcode.com/problems/rotate_non_negative_elements/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[] rotateElements(int[] nums, int k) {
        List<Integer> t = new ArrayList<>();
        for (int x : nums) if (x >= 0) t.add(x);
        int m = t.size();
        if (m == 0) return nums;
        int[] d = new int[m];
        for (int i = 0; i < m; i++) d[((i - k) % m + m) % m] = t.get(i);
        int j = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] >= 0) nums[i] = d[j++];
        }
        return nums;
    }
}

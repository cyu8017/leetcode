// LeetCode 2811 - Check if it is Possible to Split Array
// https://leetcode.com/problems/check-if-it-is-possible-to-split-array/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public boolean canSplitArray(List<Integer> nums, int m) {
        int n = nums.size();
        if (n <= 2) return true;
        for (int i = 0; i + 1 < n; i++) {
            if (nums.get(i) + nums.get(i + 1) >= m) return true;
        }
        return false;
    }
}

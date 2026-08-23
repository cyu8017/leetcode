// LeetCode 2780 - Minimum Index of a Valid Split
// https://leetcode.com/problems/minimum-index-of-a-valid-split/

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    public int minimumIndex(List<Integer> nums) {
        var freq = new HashMap<Integer, Integer>();
        int dom = 0, best = 0;
        for (int v : nums) {
            if (!freq.containsKey(v)) freq.put(v, 0);
            if (++freq.get(v) > best) { best = freq.get(v); dom = v; }
        }
        int left = 0, n = nums.size();
        for (int i = 0; i < n - 1; i++) {
            if (nums.set(i, = dom) left++);
            int right = best - left;
            if (left * 2 > i + 1 && right * 2 > n - i - 1) return i;
        }
        return -1;
    }
}

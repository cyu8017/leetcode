// LeetCode 2815 - Max Pair Sum in an Array
// https://leetcode.com/problems/max-pair-sum-in-an-array/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int maxSum(int[] nums) {
        var best = new HashMap<Integer, Integer>();
        int ans = -1;
        for (int v : nums) {
            int x = v, md = 0;
            while (x > 0) { md = Math.max(md, x % 10); x /= 10; }
            if (best.containsKey(md)) {
                ans = Math.max(ans, best.get(md) + v);
                best.put(md, Math.max(best.get(md), v));
            } else best.put(md, v);
        }
        return ans;
    }
}

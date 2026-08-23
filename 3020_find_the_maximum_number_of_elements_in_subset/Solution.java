// LeetCode 3020 - Find the Maximum Number of Elements in Subset
// https://leetcode.com/problems/find-the-maximum-number-of-elements-in-subset/

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    public int maximumLength(int[] nums) {
        Map<Long, Integer> cnt = new HashMap<>();
        for (int x : nums) cnt.put((long) x, cnt.getOrDefault((long) x, 0) + 1);
        int ones = cnt.getOrDefault(1L, 0);
        int ans = ones - ((ones % 2) ^ 1);
        cnt.remove(1L);
        List<Long> keys = new ArrayList<>(cnt.keySet());
        for (long start : keys) {
            long x = start;
            int t = 0;
            while (cnt.getOrDefault(x, 0) > 1) {
                x = x * x;
                t += 2;
            }
            if (cnt.getOrDefault(x, 0) > 0) t += 1;
            else t -= 1;
            ans = Math.max(ans, t);
        }
        return ans;
    }
}

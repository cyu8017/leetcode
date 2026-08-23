// LeetCode 2404 - Most Frequent Even Element
// https://leetcode.com/problems/most-frequent-even-element/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int mostFrequentEven(int[] nums) {
        Map<Integer, Integer> cnt = new HashMap<>();
        int ans = -1, best = 0;
        for (int x : nums) {
            if (x % 2 != 0) continue;
            int c = cnt.getOrDefault(x, 0) + 1;
            cnt.put(x, c);
            if (c > best || (c == best && (ans == -1 || x < ans))) {
                best = c;
                ans = x;
            }
        }
        return ans;
    }
}

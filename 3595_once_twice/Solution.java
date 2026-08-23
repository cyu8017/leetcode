// LeetCode 3595 - Once Twice
// https://leetcode.com/problems/once-twice/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[] onceTwice(int[] nums) {
        var freq = new HashMap<Integer, Integer>();
        for (int x : nums) {
            if (!freq.containsKey(x)) freq.put(x, 0);
            freq.put(x, freq.get(x) + 1);
        }
        int a = 0, b = 0;
        for (var kv : freq.entrySet()) {
            if (kv.getValue() == 1) a = kv.getKey();
            else if (kv.getValue() == 2) b = kv.getKey();
        }
        return new int[] { a, b };
    }
}

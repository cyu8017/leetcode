// LeetCode 2244 - Minimum Rounds to Complete All Tasks
// https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int minimumRounds(int[] tasks) {
        var freq = new HashMap<Integer, Integer>();
        for (int t : tasks) {
            int c = freq.getOrDefault(t, 0);
            freq.put(t, c + 1);
        }
        int ans = 0;
        for (int c : freq.values()) {
            if (c == 1) return -1;
            ans += (c + 2) / 3;
        }
        return ans;
    }
}

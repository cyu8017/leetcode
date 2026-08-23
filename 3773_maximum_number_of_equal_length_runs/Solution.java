// LeetCode 3773 - Maximum Number Of Equal Length Runs
// https://leetcode.com/problems/maximum-number-of-equal-length-runs/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int maxSameLengthRuns(String s) {
        var cnt = new HashMap<Integer, Integer>();
        int n = s.length(), ans = 0;
        for (int i = 0; i < n; ) {
            int j = i + 1;
            while (j < n && s.charAt(j) == s.charAt(i)) j++;
            int m = j - i;
            if (!cnt.containsKey(m)) cnt.put(m, 0);
            cnt.merge(m, 1, Integer::sum);
            ans = Math.max(ans, cnt.get(m));
            i = j;
        }
        return ans;
    }
}

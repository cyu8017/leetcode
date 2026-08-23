// LeetCode 3597 - Partition String
// https://leetcode.com/problems/partition-string/

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

class Solution {
    public List<String> partitionString(String s) {
        var vis = new HashSet<String>();
        var ans = new ArrayList<String>();
        var t = new StringBuilder();
        for (char c : s.toCharArray()) {
            t.append(c);
            String cur = t.toString();
            if (!vis.contains(cur)) {
                vis.add(cur);
                ans.add(cur);
                t.setLength(0);
            }
        }
        return ans;
    }
}

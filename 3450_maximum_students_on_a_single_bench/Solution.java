// LeetCode 3450 - Maximum Students on a Single Bench
// https://leetcode.com/problems/maximum-students-on-a-single-bench/

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

class Solution {
    public int maxStudentsOnBench(int[][] students) {
        Map<Integer, Set<Integer>> bench = new HashMap<>();
        for (int[] s : students) {
            bench.computeIfAbsent(s[1], k -> new HashSet<>()).add(s[0]);
        }
        int ans = 0;
        for (Set<Integer> set : bench.values()) {
            if (set.size() > ans) ans = set.size();
        }
        return ans;
    }
}

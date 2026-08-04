// LeetCode 1207 - Unique Number of Occurrences
// https://leetcode.com/problems/unique-number-of-occurrences/

import java.util.*;

class Solution {
    public boolean uniqueOccurrences(int[] arr) {
        Map<Integer, Integer> count = new HashMap<>();
        for (int x : arr) count.merge(x, 1, Integer::sum);
        Set<Integer> seen = new HashSet<>();
        for (int c : count.values()) if (!seen.add(c)) return false;
        return true;
    }
}

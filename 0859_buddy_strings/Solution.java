// LeetCode 0859 - Buddy Strings
// https://leetcode.com/problems/buddy-strings/

import java.util.*;

class Solution {
    public boolean buddyStrings(String s, String goal) {
        if (s.length() != goal.length()) return false;
        if (s.equals(goal)) {
            Set<Character> set = new HashSet<>();
            for (char ch : s.toCharArray()) if (!set.add(ch)) return true;
            return false;
        }
        List<int[]> diffs = new ArrayList<>();
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) != goal.charAt(i)) {
                diffs.add(new int[] {s.charAt(i), goal.charAt(i)});
            }
        }
        return diffs.size() == 2
            && diffs.get(0)[0] == diffs.get(1)[1]
            && diffs.get(0)[1] == diffs.get(1)[0];
    }
}

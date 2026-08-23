// LeetCode 0828 - Count Unique Characters of All Substrings of a Given String
// https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/

import java.util.*;

class Solution {
    public int uniqueLetterString(String s) {
        int n = s.length();
        Map<Character, List<Integer>> last = new HashMap<>();
        for (char ch : s.toCharArray()) {
            last.computeIfAbsent(ch, k -> new ArrayList<>(List.of(-1)));
        }
        for (int i = 0; i < n; i++) last.get(s.charAt(i)).add(i);
        for (List<Integer> indices : last.values()) indices.add(n);
        int ans = 0;
        for (List<Integer> indices : last.values()) {
            for (int k = 1; k + 1 < indices.size(); k++) {
                ans += (indices.get(k) - indices.get(k - 1)) * (indices.get(k + 1) - indices.get(k));
            }
        }
        return ans;
    }
}

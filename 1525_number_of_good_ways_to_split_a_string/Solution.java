// LeetCode 1525 - Number of Good Ways to Split a String
// https://leetcode.com/problems/number-of-good-ways-to-split-a-string/

import java.util.*;

class Solution {
    public int numSplits(String s) {
        Map<Character, Integer> right = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            right.put(ch, right.getOrDefault(ch, 0) + 1);
        }
        Set<Character> left = new HashSet<>();
        int answer = 0;
        for (int i = 0; i < s.length() - 1; i++) {
            char ch = s.charAt(i);
            left.add(ch);
            int count = right.get(ch) - 1;
            if (count == 0) {
                right.remove(ch);
            } else {
                right.put(ch, count);
            }
            if (left.size() == right.size()) {
                answer++;
            }
        }
        return answer;
    }
}

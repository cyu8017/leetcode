// LeetCode 1542 - Find Longest Awesome Substring
// https://leetcode.com/problems/find-longest-awesome-substring/

import java.util.*;

class Solution {
    public int longestAwesome(String s) {
        Map<Integer, Integer> first = new HashMap<>();
        first.put(0, -1);
        int mask = 0, answer = 0;
        for (int i = 0; i < s.length(); i++) {
            mask ^= 1 << (s.charAt(i) - '0');
            if (first.containsKey(mask)) {
                answer = Math.max(answer, i - first.get(mask));
            } else {
                first.put(mask, i);
            }
            for (int bit = 0; bit < 10; bit++) {
                int candidate = mask ^ (1 << bit);
                if (first.containsKey(candidate)) {
                    answer = Math.max(answer, i - first.get(candidate));
                }
            }
        }
        return answer;
    }
}

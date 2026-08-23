// LeetCode 2716 - Minimize String Length
// https://leetcode.com/problems/minimize-string-length/

import java.util.HashSet;

class Solution {
    public int minimizedStringLength(String s) {
        HashSet<Character> set = new HashSet<>();
        for (char c : s.toCharArray()) set.add(c);
        return set.size();
    }
}

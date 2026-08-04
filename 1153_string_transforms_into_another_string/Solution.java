// LeetCode 1153 - String Transforms Into Another String
// https://leetcode.com/problems/string-transforms-into-another-string/

import java.util.*;

class Solution {
    public boolean canConvert(String str1, String str2) {
        if (str1.equals(str2)) return true;
        Map<Character, Character> mapping = new HashMap<>();
        for (int i = 0; i < str1.length(); i++) {
            char a = str1.charAt(i), b = str2.charAt(i);
            if (mapping.containsKey(a) && mapping.get(a) != b) return false;
            mapping.put(a, b);
        }
        Set<Character> uniq = new HashSet<>();
        for (char c : str2.toCharArray()) uniq.add(c);
        return uniq.size() < 26;
    }
}

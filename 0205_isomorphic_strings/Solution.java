// LeetCode 0205 - Isomorphic Strings\n// https://leetcode.com/problems/\n\nimport java.util.HashMap;
import java.util.Map;

class Solution {
    public boolean isIsomorphic(String s, String t) {
        Map<Character, Character> forward = new HashMap<>();
        Map<Character, Character> backward = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            char a = s.charAt(i), b = t.charAt(i);
            if (forward.containsKey(a) && forward.get(a) != b || backward.containsKey(b) && backward.get(b) != a) return false;
            forward.put(a, b);
            backward.put(b, a);
        }
        return true;
    }
}

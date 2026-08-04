// LeetCode 1417 - Reformat The String
// https://leetcode.com/problems/reformat-the-string/

import java.util.*;

class Solution {
    public String reformat(String s) {
        List<Character> letters = new ArrayList<>(), digits = new ArrayList<>();
        for (char c : s.toCharArray()) {
            if (Character.isLetter(c)) letters.add(c);
            else digits.add(c);
        }
        if (Math.abs(letters.size() - digits.size()) > 1) return "";
        if (digits.size() > letters.size()) {
            List<Character> t = letters;
            letters = digits;
            digits = t;
        }
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < letters.size(); i++) {
            sb.append(letters.get(i));
            if (i < digits.size()) sb.append(digits.get(i));
        }
        return sb.toString();
    }
}

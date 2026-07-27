// LeetCode 1694 - Reformat Phone Number
// https://leetcode.com/problems/reformat-phone-number/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public String reformatNumber(String number) {
        StringBuilder digits = new StringBuilder();
        for (int i = 0; i < number.length(); i++) {
            char c = number.charAt(i);
            if (Character.isDigit(c)) {
                digits.append(c);
            }
        }
        String s = digits.toString();
        List<String> out = new ArrayList<>();
        while (s.length() > 4) {
            out.add(s.substring(0, 3));
            s = s.substring(3);
        }
        if (s.length() == 4) {
            out.add(s.substring(0, 2));
            out.add(s.substring(2));
        } else if (!s.isEmpty()) {
            out.add(s);
        }
        return String.join("-", out);
    }
}

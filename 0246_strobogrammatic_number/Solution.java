// LeetCode 0246 - Strobogrammatic Number
// https://leetcode.com/problems/strobogrammatic-number/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public boolean isStrobogrammatic(String num) {
        Map<Character, Character> mapping = new HashMap<>();
        mapping.put('0', '0');
        mapping.put('1', '1');
        mapping.put('6', '9');
        mapping.put('8', '8');
        mapping.put('9', '6');

        int left = 0;
        int right = num.length() - 1;
        while (left <= right) {
            if (!mapping.containsKey(num.charAt(left))
                    || mapping.get(num.charAt(left)) != num.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
}

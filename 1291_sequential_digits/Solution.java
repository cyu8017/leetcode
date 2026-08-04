// LeetCode 1291 - Sequential Digits
// https://leetcode.com/problems/sequential-digits/

import java.util.*;

class Solution {
    public List<Integer> sequentialDigits(int low, int high) {
        String digits = "123456789";
        List<Integer> answer = new ArrayList<>();
        for (int length = 2; length <= 9; length++) {
            for (int start = 0; start <= 9 - length; start++) {
                int value = Integer.parseInt(digits.substring(start, start + length));
                if (value >= low && value <= high) answer.add(value);
            }
        }
        return answer;
    }
}

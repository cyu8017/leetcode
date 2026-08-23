// LeetCode 2578 - Split With Minimum Sum
// https://leetcode.com/problems/split-with-minimum-sum/

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Solution {
    public int splitNum(int num) {
        List<Integer> digits = new ArrayList<>();
        while (num > 0) {
            digits.add(num % 10);
            num /= 10;
        }
        Collections.sort(digits);
        int a = 0, b = 0;
        for (int i = 0; i < digits.size(); ++i) {
            if (i % 2 == 0) a = a * 10 + digits.get(i);
            else b = b * 10 + digits.get(i);
        }
        return a + b;
    }
}

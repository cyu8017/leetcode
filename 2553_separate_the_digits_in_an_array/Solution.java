// LeetCode 2553 - Separate the Digits in an Array
// https://leetcode.com/problems/separate-the-digits-in-an-array/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[] separateDigits(int[] nums) {
        List<Integer> ans = new ArrayList<>();
        for (int num : nums) {
            int x = num;
            List<Integer> digits = new ArrayList<>();
            while (x > 0) {
                digits.add(x % 10);
                x /= 10;
            }
            for (int i = digits.size() - 1; i >= 0; --i) ans.add(digits.get(i));
        }
        int[] res = new int[ans.size()];
        for (int i = 0; i < ans.size(); i++) res[i] = ans.get(i);
        return res;
    }
}

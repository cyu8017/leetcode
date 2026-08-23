// LeetCode 0728 - Self Dividing Numbers
// https://leetcode.com/problems/self-dividing-numbers/

import java.util.*;

class Solution {
    public List<Integer> selfDividingNumbers(int left, int right) {
        List<Integer> result = new ArrayList<>();
        for (int num = left; num <= right; num++) if (isSelfDividing(num)) result.add(num);
        return result;
    }

    private boolean isSelfDividing(int num) {
        int x = num;
        while (x > 0) {
            int digit = x % 10;
            if (digit == 0 || num % digit != 0) return false;
            x /= 10;
        }
        return true;
    }
}

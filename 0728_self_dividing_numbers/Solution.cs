// LeetCode 0728 - Self Dividing Numbers
// https://leetcode.com/problems/self-dividing-numbers/

using System.Collections.Generic;

public class Solution {
    public IList<int> SelfDividingNumbers(int left, int right) {
        var result = new List<int>();
        for (int num = left; num <= right; num++) if (IsSelfDividing(num)) result.Add(num);
        return result;
    }

    private bool IsSelfDividing(int num) {
        int x = num;
        while (x > 0) {
            int digit = x % 10;
            if (digit == 0 || num % digit != 0) return false;
            x /= 10;
        }
        return true;
    }
}

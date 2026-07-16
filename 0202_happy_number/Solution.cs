// LeetCode 0202 - Happy Number\n// https://leetcode.com/problems/\n\nusing System.Collections.Generic;

public class Solution {
    public bool IsHappy(int n) {
        var seen = new HashSet<int>();
        while (n != 1 && seen.Add(n)) n = NextValue(n);
        return n == 1;
    }

    private static int NextValue(int value) {
        var total = 0;
        while (value > 0) { var digit = value % 10; total += digit * digit; value /= 10; }
        return total;
    }
}

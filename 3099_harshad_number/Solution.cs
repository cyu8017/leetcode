// LeetCode 3099 - Harshad Number
// https://leetcode.com/problems/harshad-number/

public class Solution {
    public int SumOfTheDigitsOfHarshadNumber(int x) {
        int s = 0;
        for (int y = x; y > 0; y /= 10) s += y % 10;
        return x % s == 0 ? s : -1;
    }
}

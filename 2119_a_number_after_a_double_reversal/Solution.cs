// LeetCode 2119 - A Number After a Double Reversal
// https://leetcode.com/problems/a-number-after-a-double-reversal/

public class Solution {
    public bool IsSameAfterReversals(int num) {
        return num == 0 || num % 10 != 0;
    }
}

// LeetCode 3745 - Maximize Expression of Three Elements
// https://leetcode.com/problems/maximize-expression-of-three-elements/

public class Solution {
    public int MaximizeExpressionOfThree(int[] nums) {
        const int inf = 1 << 30;
        int a = -inf, b = -inf, c = inf;
        foreach (int x in nums) {
            if (x < c) c = x;
            if (x >= a) { b = a; a = x; }
            else if (x > b) b = x;
        }
        return a + b - c;
    }
}

// LeetCode 0650 - 2 Keys Keyboard
// https://leetcode.com/problems/2-keys-keyboard/

public class Solution {
    public int MinSteps(int n) {
        int steps = 0, factor = 2;
        while (factor * factor <= n) {
            while (n % factor == 0) {
                steps += factor;
                n /= factor;
            }
            ++factor;
        }
        if (n > 1) steps += n;
        return steps;
    }
}

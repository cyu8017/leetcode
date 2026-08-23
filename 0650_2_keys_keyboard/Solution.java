// LeetCode 0650 - 2 Keys Keyboard
// https://leetcode.com/problems/2-keys-keyboard/

class Solution {
    public int minSteps(int n) {
        int steps = 0;
        int factor = 2;
        while (factor * factor <= n) {
            while (n % factor == 0) {
                steps += factor;
                n /= factor;
            }
            ++factor;
        }
        if (n > 1) {
            steps += n;
        }
        return steps;
    }
}

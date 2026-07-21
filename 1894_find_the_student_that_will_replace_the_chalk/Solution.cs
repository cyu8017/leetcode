// LeetCode 1894 - Find the Student that Will Replace the Chalk
// https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/

public class Solution {
    public int ChalkReplacer(int[] chalk, int k) {
        long sum = 0;
        foreach (int c in chalk) {
            sum += c;
        }
        long remaining = k % sum;
        for (int index = 0; index < chalk.Length; index++) {
            if (remaining < chalk[index]) {
                return index;
            }
            remaining -= chalk[index];
        }
        return 0;
    }
}

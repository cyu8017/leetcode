// LeetCode 1894 - Find the Student that Will Replace the Chalk
// https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/

class Solution {
    public int chalkReplacer(int[] chalk, int k) {
        long total = 0;
        for (int need : chalk) {
            total += need;
        }
        k %= total;
        for (int index = 0; index < chalk.length; index++) {
            if (k < chalk[index]) {
                return index;
            }
            k -= chalk[index];
        }
        return 0;
    }
}

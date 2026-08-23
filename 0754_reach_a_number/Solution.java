// LeetCode 0754 - Reach a Number
// https://leetcode.com/problems/reach-a-number/

class Solution {
    public int reachNumber(int target) {
        target = Math.abs(target);
        int steps = 0, total = 0;
        while (total < target || (total - target) % 2 != 0) {
            steps++;
            total += steps;
        }
        return steps;
    }
}

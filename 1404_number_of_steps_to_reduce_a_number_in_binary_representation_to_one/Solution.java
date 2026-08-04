// LeetCode 1404 - Number Of Steps To Reduce A Number In Binary Representation To One
// https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/

class Solution {
    public int numSteps(String s) {
        int steps = 0, carry = 0;
        for (int i = s.length - 1; i >= 1; i--) {
            int value = (s[i] - '0') + carry;
            if (value == 1) { steps += 2; carry = 1; }
            else steps += 1;
        }
        return steps + carry;
    }
}

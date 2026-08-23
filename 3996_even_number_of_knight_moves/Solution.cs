// LeetCode 3996 - Even Number of Knight Moves
// https://leetcode.com/problems/even-number-of-knight-moves/

public class Solution {
    public bool CanReach(int[] start, int[] target) {
        return ((start[0] + start[1]) % 2) == ((target[0] + target[1]) % 2);
    }
}

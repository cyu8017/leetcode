// LeetCode 0657 - Robot Return to Origin
// https://leetcode.com/problems/robot-return-to-origin/

public class Solution {
    public bool JudgeCircle(string moves) {
        int x = 0, y = 0;
        foreach (char move in moves) {
            if (move == 'U') ++y;
            else if (move == 'D') --y;
            else if (move == 'L') --x;
            else if (move == 'R') ++x;
        }
        return x == 0 && y == 0;
    }
}

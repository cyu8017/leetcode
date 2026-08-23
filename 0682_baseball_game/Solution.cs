// LeetCode 0682 - Baseball Game
// https://leetcode.com/problems/baseball-game/

using System.Collections.Generic;

public class Solution {
    public int CalPoints(string[] operations) {
        var stack = new List<int>();
        foreach (string op in operations) {
            if (op == "C") stack.RemoveAt(stack.Count - 1);
            else if (op == "D") stack.Add(stack[stack.Count - 1] * 2);
            else if (op == "+") stack.Add(stack[stack.Count - 1] + stack[stack.Count - 2]);
            else stack.Add(int.Parse(op));
        }
        int total = 0;
        foreach (int value in stack) total += value;
        return total;
    }
}

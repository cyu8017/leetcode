// LeetCode 1306 - Jump Game Iii
// https://leetcode.com/problems/jump-game-iii/

using System.Collections.Generic;

public class Solution {
    public bool CanReach(int[] arr, int start) {
        var stack = new Stack<int>();
        var seen = new HashSet<int>();
        stack.Push(start);
        while (stack.Count > 0) {
            int i = stack.Pop();
            if (seen.Contains(i) || i < 0 || i >= arr.Length) continue;
            if (arr[i] == 0) return true;
            seen.Add(i);
            stack.Push(i - arr[i]);
            stack.Push(i + arr[i]);
        }
        return false;
    }
}

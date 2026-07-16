// LeetCode 0279 - Perfect Squares
// https://leetcode.com/problems/perfect-squares/

using System.Collections.Generic;

public class Solution {
    public int NumSquares(int n) {
        List<int> squares = new List<int>();
        for (int value = 1; value * value <= n; value++) {
            squares.Add(value * value);
        }

        Queue<(int remain, int steps)> queue = new Queue<(int remain, int steps)>();
        queue.Enqueue((n, 0));
        HashSet<int> visited = new HashSet<int> { n };

        while (queue.Count > 0) {
            (int remain, int steps) = queue.Dequeue();
            if (remain == 0) {
                return steps;
            }
            foreach (int square in squares) {
                int next = remain - square;
                if (next < 0) {
                    break;
                }
                if (visited.Add(next)) {
                    queue.Enqueue((next, steps + 1));
                }
            }
        }
        return 0;
    }
}

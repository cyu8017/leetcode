// LeetCode 0279 - Perfect Squares
// https://leetcode.com/problems/perfect-squares/

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

class Solution {
    public int numSquares(int n) {
        List<Integer> squares = new ArrayList<>();
        for (int value = 1; value * value <= n; value++) {
            squares.add(value * value);
        }

        ArrayDeque<int[]> queue = new ArrayDeque<>();
        queue.offer(new int[] { n, 0 });
        Set<Integer> visited = new HashSet<>();
        visited.add(n);

        while (!queue.isEmpty()) {
            int[] state = queue.poll();
            int remain = state[0];
            int steps = state[1];
            if (remain == 0) {
                return steps;
            }
            for (int square : squares) {
                int next = remain - square;
                if (next < 0) {
                    break;
                }
                if (visited.add(next)) {
                    queue.offer(new int[] { next, steps + 1 });
                }
            }
        }
        return 0;
    }
}

// LeetCode 1306 - Jump Game Iii
// https://leetcode.com/problems/jump-game-iii/

import java.util.*;

class Solution {
    public boolean canReach(int[] arr, int start) {
        Deque<Integer> stack = new ArrayDeque<>();
        boolean[] seen = new boolean[arr.length];
        stack.push(start);
        while (!stack.isEmpty()) {
            int i = stack.pop();
            if (i < 0 || i >= arr.length || seen[i]) continue;
            if (arr[i] == 0) return true;
            seen[i] = true;
            stack.push(i - arr[i]);
            stack.push(i + arr[i]);
        }
        return false;
    }
}

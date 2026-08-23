// LeetCode 0735 - Asteroid Collision
// https://leetcode.com/problems/asteroid-collision/

import java.util.*;

class Solution {
    public int[] asteroidCollision(int[] asteroids) {
        List<Integer> stack = new ArrayList<>();
        for (int asteroid : asteroids) {
            boolean alive = true;
            while (alive && !stack.isEmpty() && asteroid < 0 && stack.get(stack.size() - 1) > 0) {
                if (stack.get(stack.size() - 1) < -asteroid) { stack.remove(stack.size() - 1); continue; }
                if (stack.get(stack.size() - 1) == -asteroid) stack.remove(stack.size() - 1);
                alive = false;
            }
            if (alive) stack.add(asteroid);
        }
        int[] ans = new int[stack.size()];
        for (int i = 0; i < stack.size(); i++) ans[i] = stack.get(i);
        return ans;
    }
}

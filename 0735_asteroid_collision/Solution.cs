// LeetCode 0735 - Asteroid Collision
// https://leetcode.com/problems/asteroid-collision/

using System.Collections.Generic;

public class Solution {
    public int[] AsteroidCollision(int[] asteroids) {
        var stack = new List<int>();
        foreach (int asteroid in asteroids) {
            bool alive = true;
            while (alive && stack.Count > 0 && asteroid < 0 && stack[stack.Count - 1] > 0) {
                if (stack[stack.Count - 1] < -asteroid) { stack.RemoveAt(stack.Count - 1); continue; }
                if (stack[stack.Count - 1] == -asteroid) stack.RemoveAt(stack.Count - 1);
                alive = false;
            }
            if (alive) stack.Add(asteroid);
        }
        return stack.ToArray();
    }
}

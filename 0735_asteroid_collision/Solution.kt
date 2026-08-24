// LeetCode 0735 - Asteroid Collision
// https://leetcode.com/problems/asteroid-collision/

class Solution {
    fun asteroidCollision(asteroids: IntArray): IntArray {
        var stack = ArrayList<Int>()
        for (asteroid in asteroids) {
            var alive = true
            while (alive && !stack.isEmpty() && asteroid < 0 && stack[stack.size - 1] > 0) {
                if (stack[stack.size - 1] < -asteroid) { stack.removeAt(stack.size - 1); continue; }
                if (stack[stack.size - 1] == -asteroid) stack.removeAt(stack.size - 1)
                alive = false
            }
            if (alive) stack.add(asteroid)
        }
        var ans = IntArray(stack.size)
        for (i in 0 until stack.size) { ans[i] = stack[i] }
        return ans
    }
}

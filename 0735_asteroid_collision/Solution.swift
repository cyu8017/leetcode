// LeetCode 0735 - Asteroid Collision
// https://leetcode.com/problems/asteroid-collision/

class Solution {
    func asteroidCollision(_ asteroids: [Int]) -> [Int] {
        var stack = [Int]()
        for a in asteroids {
            var a = a
            var alive = true
            while alive && a < 0 && !stack.isEmpty && stack.last! > 0 {
                if stack.last! < -a { stack.removeLast(); continue }
                if stack.last! == -a { stack.removeLast() }
                alive = false
            }
            if alive { stack.append(a) }
        }
        return stack
    }
}

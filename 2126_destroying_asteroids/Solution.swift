// LeetCode 2126 - Destroying Asteroids
// https://leetcode.com/problems/destroying-asteroids/

class Solution {
    func asteroidsDestroyed(_ mass: Int, _ asteroids: [Int]) -> Bool {
        var cur = mass
        for a in asteroids.sorted() {
            if cur < a { return false }
            cur += a
        }
        return true
    }
}

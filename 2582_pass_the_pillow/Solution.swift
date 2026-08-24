// LeetCode 2582 - Pass the Pillow
// https://leetcode.com/problems/pass-the-pillow/

class Solution {
    func passThePillow(_ n: Int, _ time: Int) -> Int {
        let cycle = 2 * (n - 1)
        let t = time % cycle
        if t < n { return 1 + t }
        return n - (t - (n - 1))
    }
}

// LeetCode 3178 - Find the Child Who Has the Ball After K Seconds
// https://leetcode.com/problems/find-the-child-who-has-the-ball-after-k-seconds/

class Solution {
    func numberOfChild(_ n: Int, _ k: Int) -> Int {
        let mod = k % (n - 1)
        let rounds = k / (n - 1)
        if rounds % 2 == 1 { return n - mod - 1 }
        return mod
    }
}

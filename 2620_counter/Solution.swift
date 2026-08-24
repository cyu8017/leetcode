// LeetCode 2620 - Counter
// https://leetcode.com/problems/counter/

class Solution {
    func createCounter(_ n: Int) -> () -> Int {
        var cur = n
        return {
            let v = cur
            cur += 1
            return v
        }
    }
}

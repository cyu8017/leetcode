// LeetCode 0754 - Reach a Number
// https://leetcode.com/problems/reach-a-number/

class Solution {
    func reachNumber(_ target: Int) -> Int {
        let target = abs(target)
        var sum = 0, k = 0
        while sum < target || (sum - target) % 2 != 0 {
            k += 1
            sum += k
        }
        return k
    }
}

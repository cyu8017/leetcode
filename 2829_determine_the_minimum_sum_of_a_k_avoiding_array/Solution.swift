// LeetCode 2829 - Determine the Minimum Sum of a k-avoiding Array
// https://leetcode.com/problems/determine-the-minimum-sum-of-a-k-avoiding-array/

class Solution {
    func minimumSum(_ n: Int, _ k: Int) -> Int {
        var used = Set<Int>()
        var sum = 0, x = 1
        while used.count < n {
            if !used.contains(k - x) {
                used.insert(x)
                sum += x
            }
            x += 1
        }
        return sum
    }
}

// LeetCode 2717 - Semi-Ordered Permutation
// https://leetcode.com/problems/semi-ordered-permutation/

class Solution {
    func semiOrderedPermutation(_ nums: [Int]) -> Int {
        let n = nums.count
        var p1 = 0, pn = 0
        for i in 0..<n {
            if nums[i] == 1 { p1 = i }
            if nums[i] == n { pn = i }
        }
        var ans = p1 + (n - 1 - pn)
        if p1 > pn { ans -= 1 }
        return ans
    }
}

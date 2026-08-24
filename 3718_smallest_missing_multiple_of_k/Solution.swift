// LeetCode 3718 - Smallest Missing Multiple of K
// https://leetcode.com/problems/smallest-missing-multiple-of-k/

class Solution {
    func missingMultiple(_ nums: [Int], _ k: Int) -> Int {
        let s = Set(nums)
        var i = 1
        while true {
            let x = k * i
            if !s.contains(x) { return x }
            i += 1
        }
    }
}

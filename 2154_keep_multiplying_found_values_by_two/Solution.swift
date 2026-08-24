// LeetCode 2154 - Keep Multiplying Found Values by Two
// https://leetcode.com/problems/keep-multiplying-found-values-by-two/

class Solution {
    func findFinalValue(_ nums: [Int], _ original: Int) -> Int {
        let have = Set(nums)
        var original = original
        while have.contains(original) { original *= 2 }
        return original
    }
}

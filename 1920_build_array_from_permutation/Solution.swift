// LeetCode 1920 - Build Array from Permutation
// https://leetcode.com/problems/build-array-from-permutation/

class Solution {
    func buildArray(_ nums: [Int]) -> [Int] {
        nums.map { nums[$0] }
    }
}

// LeetCode 3190 - Find Minimum Operations to Make All Elements Divisible by Three
// https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/

class Solution {
    func minimumOperations(_ nums: [Int]) -> Int {
        nums.filter { $0 % 3 != 0 }.count
    }
}

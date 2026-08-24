// LeetCode 2367 - Number of Arithmetic Triplets
// https://leetcode.com/problems/number-of-arithmetic-triplets/

class Solution {
    func arithmeticTriplets(_ nums: [Int], _ diff: Int) -> Int {
        let seen = Set(nums)
        return nums.filter { seen.contains($0 + diff) && seen.contains($0 + 2 * diff) }.count
    }
}

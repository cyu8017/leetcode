// LeetCode 3779 - Minimum Number Of Operations To Have Distinct Elements
// https://leetcode.com/problems/minimum-number-of-operations-to-have-distinct-elements/

class Solution {
    func minOperations(_ nums: [Int]) -> Int {
        var st = Set<Int>()
        for i in stride(from: nums.count - 1, through: 0, by: -1) {
            if st.contains(nums[i]) { return i / 3 + 1 }
            st.insert(nums[i])
        }
        return 0
    }
}

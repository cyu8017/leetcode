// LeetCode 1855 - Maximum Distance Between a Pair of Values
// https://leetcode.com/problems/maximum-distance-between-a-pair-of-values/

class Solution {
    func maxDistance(_ nums1: [Int], _ nums2: [Int]) -> Int {
        var answer = 0
        var j = 0

        for i in 0..<nums1.count {
            let value = nums1[i]
            while j < nums2.count && value <= nums2[j] {
                j += 1
            }
            answer = max(answer, j - i - 1)
        }

        return answer
    }
}

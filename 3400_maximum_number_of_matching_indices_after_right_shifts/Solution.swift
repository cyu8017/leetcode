// LeetCode 3400 - Maximum Number of Matching Indices After Right Shifts
// https://leetcode.com/problems/maximum-number-of-matching-indices-after-right-shifts/

class Solution {
    func maximumMatchingIndices(_ nums1: [Int], _ nums2: [Int]) -> Int {
        let n = nums1.count
        var ans = 0
        for shift in 0..<n {
            var cnt = 0
            for i in 0..<n {
                if nums1[(i - shift + n) % n] == nums2[i] { cnt += 1 }
            }
            if cnt > ans { ans = cnt }
        }
        return ans
    }
}

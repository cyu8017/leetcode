// LeetCode 2570 - Merge Two 2D Arrays by Summing Values
// https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/

class Solution {
    func mergeArrays(_ nums1: [[Int]], _ nums2: [[Int]]) -> [[Int]] {
        var ans = [[Int]]()
        var i = 0, j = 0
        while i < nums1.count && j < nums2.count {
            if nums1[i][0] == nums2[j][0] {
                ans.append([nums1[i][0], nums1[i][1] + nums2[j][1]])
                i += 1; j += 1
            } else if nums1[i][0] < nums2[j][0] {
                ans.append(nums1[i])
                i += 1
            } else {
                ans.append(nums2[j])
                j += 1
            }
        }
        while i < nums1.count { ans.append(nums1[i]); i += 1 }
        while j < nums2.count { ans.append(nums2[j]); j += 1 }
        return ans
    }
}

// LeetCode 3131 - Find the Integer Added to Array I
// https://leetcode.com/problems/find-the-integer-added-to-array-i/

class Solution {
    func addedInteger(_ nums1: [Int], _ nums2: [Int]) -> Int {
        nums2.min()! - nums1.min()!
    }
}

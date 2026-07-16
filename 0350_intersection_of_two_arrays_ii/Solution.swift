// LeetCode 0350 - Intersection of Two Arrays II
// https://leetcode.com/problems/intersection-of-two-arrays-ii/

class Solution {
    func intersect(_ nums1: [Int], _ nums2: [Int]) -> [Int] {
        var counts: [Int: Int] = [:]
        for num in nums1 {
            counts[num, default: 0] += 1
        }

        var result: [Int] = []
        for num in nums2 {
            if counts[num, default: 0] > 0 {
                result.append(num)
                counts[num, default: 0] -= 1
            }
        }

        return result
    }
}

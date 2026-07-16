// LeetCode 0349 - Intersection of Two Arrays
// https://leetcode.com/problems/intersection-of-two-arrays/

class Solution {
    func intersection(_ nums1: [Int], _ nums2: [Int]) -> [Int] {
        let set2 = Set(nums2)
        var seen = Set<Int>()
        var result: [Int] = []

        for num in nums1 {
            if set2.contains(num) && !seen.contains(num) {
                seen.insert(num)
                result.append(num)
            }
        }

        return result
    }
}

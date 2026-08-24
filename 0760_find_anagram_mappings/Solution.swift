// LeetCode 0760 - Find Anagram Mappings
// https://leetcode.com/problems/find-anagram-mappings/

class Solution {
    func anagramMappings(_ nums1: [Int], _ nums2: [Int]) -> [Int] {
        var pos = [Int: [Int]]()
        for (i, n) in nums2.enumerated() { pos[n, default: []].append(i) }
        return nums1.map { pos[$0]!.removeLast() }
    }
}

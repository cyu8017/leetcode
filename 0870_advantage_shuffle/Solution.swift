// LeetCode 0870 - Advantage Shuffle
// https://leetcode.com/problems/advantage-shuffle/

class Solution {
    func advantageCount(_ nums1: [Int], _ nums2: [Int]) -> [Int] {
        var dq = nums1.sorted()
        var indexed = nums2.enumerated().map { ($0.element, $0.offset) }
        indexed.sort { $0.0 > $1.0 }
        var ans = Array(repeating: 0, count: nums1.count)
        for (val, i) in indexed {
            if dq.last! > val {
                ans[i] = dq.removeLast()
            } else {
                ans[i] = dq.removeFirst()
            }
        }
        return ans
    }
}

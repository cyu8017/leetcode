// LeetCode 2613 - Beautiful Pairs
// https://leetcode.com/problems/beautiful-pairs/

class Solution {
    func beautifulPair(_ nums1: [Int], _ nums2: [Int]) -> [Int] {
        let n = nums1.count
        var best = Int.max
        var ans = [0, 1]
        for i in 0..<n {
            for j in (i + 1)..<n {
                let d = abs(nums1[i] - nums1[j]) + abs(nums2[i] - nums2[j])
                if d < best || (d == best && (i < ans[0] || (i == ans[0] && j < ans[1]))) {
                    best = d
                    ans = [i, j]
                }
            }
        }
        return ans
    }
}

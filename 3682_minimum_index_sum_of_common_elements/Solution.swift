// LeetCode 3682 - Minimum Index Sum of Common Elements
// https://leetcode.com/problems/minimum-index-sum-of-common-elements/

class Solution {
    func minimumSum(_ nums1: [Int], _ nums2: [Int]) -> Int {
        let inf = 1 << 30
        var d = [Int: Int]()
        for i in 0..<nums2.count where d[nums2[i]] == nil { d[nums2[i]] = i }
        var ans = inf
        for i in 0..<nums1.count {
            if let j = d[nums1[i]] { ans = min(ans, i + j) }
        }
        return ans == inf ? -1 : ans
    }
}

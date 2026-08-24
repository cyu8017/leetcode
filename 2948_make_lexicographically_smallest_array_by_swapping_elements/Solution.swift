// LeetCode 2948 - Make Lexicographically Smallest Array by Swapping Elements
// https://leetcode.com/problems/make-lexicographically-smallest-array-by-swapping-elements/

class Solution {
    func lexicographicallySmallestArray(_ nums: [Int], _ limit: Int) -> [Int] {
        let n = nums.count
        var idx = Array(0..<n)
        idx.sort { nums[$0] < nums[$1] }
        var ans = Array(repeating: 0, count: n)
        var i = 0
        while i < n {
            var j = i + 1
            while j < n && nums[idx[j]] - nums[idx[j - 1]] <= limit { j += 1 }
            var groupIdx = Array(idx[i..<j])
            groupIdx.sort()
            for t in 0..<(j - i) {
                ans[groupIdx[t]] = nums[idx[i + t]]
            }
            i = j
        }
        return ans
    }
}

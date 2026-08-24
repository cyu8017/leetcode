// LeetCode 2593 - Find Score of an Array After Marking All Elements
// https://leetcode.com/problems/find-score-of-an-array-after-marking-all-elements/

class Solution {
    func findScore(_ nums: [Int]) -> Int {
        let n = nums.count
        var idx = Array(0..<n)
        idx.sort { nums[$0] != nums[$1] ? nums[$0] < nums[$1] : $0 < $1 }
        var marked = [Bool](repeating: false, count: n)
        var ans = 0
        for i in idx {
            if marked[i] { continue }
            ans += nums[i]
            marked[i] = true
            if i - 1 >= 0 { marked[i - 1] = true }
            if i + 1 < n { marked[i + 1] = true }
        }
        return ans
    }
}

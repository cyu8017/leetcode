// LeetCode 2200 - Find All K-Distant Indices in an Array
// https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/

class Solution {
    func findKDistantIndices(_ nums: [Int], _ key: Int, _ k: Int) -> [Int] {
        let n = nums.count
        var mark = [Bool](repeating: false, count: n)
        for i in 0..<n where nums[i] == key {
            let l = max(0, i - k)
            let r = min(n - 1, i + k)
            for j in l...r { mark[j] = true }
        }
        return (0..<n).filter { mark[$0] }
    }
}

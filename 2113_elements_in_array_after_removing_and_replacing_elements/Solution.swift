// LeetCode 2113 - Elements in Array After Removing and Replacing Elements
// https://leetcode.com/problems/elements-in-array-after-removing-and-replacing-elements/

class Solution {
    func elementInNums(_ nums: [Int], _ queries: [[Int]]) -> [Int] {
        let n = nums.count
        return queries.map { q in
            let t = q[0], idx = q[1]
            let cycle = t % (2 * n)
            let size: Int, offset: Int
            if cycle < n {
                size = n - cycle; offset = cycle
            } else {
                size = cycle - n; offset = 0
            }
            return idx >= size ? -1 : nums[offset + idx]
        }
    }
}

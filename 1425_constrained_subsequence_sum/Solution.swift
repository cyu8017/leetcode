// LeetCode 1425 - Constrained Subsequence Sum
// https://leetcode.com/problems/constrained-subsequence-sum/

class Solution {
    func constrainedSubsetSum(_ nums: [Int], _ k: Int) -> Int {
        var queue = [Int]()
        var best = nums
        for i in 0..<nums.count {
            while !queue.isEmpty && queue[0] < i - k { queue.removeFirst() }
            best[i] = nums[i] + max(0, queue.isEmpty ? 0 : best[queue[0]])
            while !queue.isEmpty && best[queue.last!] <= best[i] { queue.removeLast() }
            queue.append(i)
        }
        return best.max()!
    }
}

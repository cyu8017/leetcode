// LeetCode 0440 - K-th Smallest in Lexicographical Order
// https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/

class Solution {
    func findKthNumber(_ n: Int, _ k: Int) -> Int {
        var current = 1
        var remaining = k - 1

        while remaining > 0 {
            let steps = countSteps(n, current, current + 1)
            if steps <= remaining {
                current += 1
                remaining -= steps
            } else {
                current *= 10
                remaining -= 1
            }
        }

        return current
    }

    private func countSteps(_ n: Int, _ first: Int, _ last: Int) -> Int {
        var steps = 0
        var currentFirst = first
        var currentLast = last
        while currentFirst <= n {
            steps += min(n + 1, currentLast) - currentFirst
            currentFirst *= 10
            currentLast *= 10
        }
        return steps
    }
}

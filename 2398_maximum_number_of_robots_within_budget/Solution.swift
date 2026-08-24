// LeetCode 2398 - Maximum Number of Robots Within Budget
// https://leetcode.com/problems/maximum-number-of-robots-within-budget/

class Solution {
    func maximumRobots(_ chargeTimes: [Int], _ runningCosts: [Int], _ budget: Int) -> Int {
        let n = chargeTimes.count
        var left = 0, sum = 0, ans = 0
        var dq: [Int] = []
        for right in 0..<n {
            while let last = dq.last, chargeTimes[last] <= chargeTimes[right] { dq.removeLast() }
            dq.append(right)
            sum += runningCosts[right]
            while left <= right && chargeTimes[dq[0]] + (right - left + 1) * sum > budget {
                if dq[0] == left { dq.removeFirst() }
                sum -= runningCosts[left]
                left += 1
            }
            ans = max(ans, right - left + 1)
        }
        return ans
    }
}

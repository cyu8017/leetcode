// LeetCode 0739 - Daily Temperatures
// https://leetcode.com/problems/daily-temperatures/

class Solution {
    func dailyTemperatures(_ temperatures: [Int]) -> [Int] {
        var ans = Array(repeating: 0, count: temperatures.count)
        var stack = [Int]()
        for i in 0..<temperatures.count {
            while let last = stack.last, temperatures[i] > temperatures[last] {
                stack.removeLast()
                ans[last] = i - last
            }
            stack.append(i)
        }
        return ans
    }
}

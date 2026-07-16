// LeetCode 0502 - IPO
// https://leetcode.com/problems/ipo/

class Solution {
    func findMaximizedCapital(_ k: Int, _ w: Int, _ profits: [Int], _ capital: [Int]) -> Int {
        var projects = zip(capital, profits).sorted { $0.0 < $1.0 }
        var available: [Int] = []
        var wealth = w
        var index = 0

        for _ in 0..<k {
            while index < projects.count && projects[index].0 <= wealth {
                available.append(projects[index].1)
                index += 1
            }
            if available.isEmpty {
                break
            }
            available.sort()
            wealth += available.removeLast()
        }
        return wealth
    }
}

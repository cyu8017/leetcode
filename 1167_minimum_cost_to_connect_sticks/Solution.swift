// LeetCode 1167 - Minimum Cost to Connect Sticks
// https://leetcode.com/problems/minimum-cost-to-connect-sticks/

class Solution {
    func connectSticks(_ sticks: [Int]) -> Int {
        var heap = sticks.sorted()
        var ans = 0
        while heap.count > 1 {
            let a = heap.removeFirst()
            let b = heap.removeFirst()
            let cost = a + b
            ans += cost
            let idx = heap.firstIndex { $0 >= cost } ?? heap.count
            heap.insert(cost, at: idx)
        }
        return ans
    }
}

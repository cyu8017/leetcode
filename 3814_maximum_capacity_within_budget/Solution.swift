// LeetCode 3814 - Maximum Capacity Within Budget
// https://leetcode.com/problems/maximum-capacity-within-budget/

class Solution {
    func maxCapacity(_ costs: [Int], _ capacity: [Int], _ budget: Int) -> Int {
        var arr = [[Int]]()
        for k in 0..<costs.count {
            if costs[k] < budget { arr.append([costs[k], capacity[k]]) }
        }
        if arr.isEmpty { return 0 }
        arr.sort { $0[0] < $1[0] }
        let m = arr.count
        var alive = [Bool](repeating: true, count: m)
        var h = [(Int, Int)]()
        for i in 0..<m { h.append((arr[i][1], i)) }
        h.sort { $0.0 != $1.0 ? $0.0 > $1.0 : $0.1 > $1.1 }
        while !h.isEmpty && !alive[h[0].1] { h.removeFirst() }
        var ans = h[0].0
        var i = 0, j = m - 1
        while i < j {
            alive[i] = false
            while i < j && arr[i][0] + arr[j][0] >= budget {
                alive[j] = false
                j -= 1
            }
            while !h.isEmpty && !alive[h[0].1] { h.removeFirst() }
            if !h.isEmpty { ans = max(ans, arr[i][1] + h[0].0) }
            i += 1
        }
        return ans
    }
}

// LeetCode 3009 - Maximum Number of Intersections on the Chart
// https://leetcode.com/problems/maximum-number-of-intersections-on-the-chart/

class Solution {
    func maxIntersectionCount(_ y: [Int]) -> Int {
        let n = y.count
        var events: [Int: Int] = [:]
        for i in 1..<n {
            var start = 2 * y[i - 1]
            var end = 2 * y[i]
            if i != n - 1 {
                if y[i] > y[i - 1] { end -= 1 }
                else { end += 1 }
            }
            var a = start, b = end
            if a > b { swap(&a, &b) }
            events[a, default: 0] += 1
            events[b + 1, default: 0] -= 1
        }
        var ans = 0, cur = 0
        for key in events.keys.sorted() {
            cur += events[key]!
            ans = max(ans, cur)
        }
        return ans
    }
}

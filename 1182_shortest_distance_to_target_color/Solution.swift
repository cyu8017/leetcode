// LeetCode 1182 - Shortest Distance to Target Color
// https://leetcode.com/problems/shortest-distance-to-target-color/

class Solution {
    func shortestDistanceColor(_ colors: [Int], _ queries: [[Int]]) -> [Int] {
        var pos: [Int: [Int]] = [:]
        for (i, c) in colors.enumerated() { pos[c, default: []].append(i) }
        var ans: [Int] = []
        for q in queries {
            let i = q[0], c = q[1]
            guard let arr = pos[c] else { ans.append(-1); continue }
            var lo = 0, hi = arr.count
            while lo < hi {
                let mid = (lo + hi) / 2
                if arr[mid] < i { lo = mid + 1 } else { hi = mid }
            }
            var best = Int.max
            if lo < arr.count { best = min(best, arr[lo] - i) }
            if lo > 0 { best = min(best, i - arr[lo - 1]) }
            ans.append(best == Int.max ? -1 : best)
        }
        return ans
    }
}

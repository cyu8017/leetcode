// LeetCode 2940 - Find Building Where Alice and Bob Can Meet
// https://leetcode.com/problems/find-building-where-alice-and-bob-can-meet/

class Solution {
    func leftmostBuildingQueries(_ heights: [Int], _ queries: [[Int]]) -> [Int] {
        let qn = queries.count
        var ans = Array(repeating: -1, count: qn)
        var buckets = Array(repeating: [(Int, Int)](), count: heights.count)
        for qi in 0..<qn {
            var a = queries[qi][0], b = queries[qi][1]
            if a > b { swap(&a, &b) }
            if a == b || heights[a] < heights[b] {
                ans[qi] = b
                continue
            }
            buckets[b].append((heights[a], qi))
        }
        var st: [(Int, Int)] = []
        for i in stride(from: heights.count - 1, through: 0, by: -1) {
            for (h, qi) in buckets[i] {
                var lo = 0, hi = st.count - 1, pos = -1
                while lo <= hi {
                    let mid = (lo + hi) / 2
                    if st[mid].0 > h {
                        pos = st[mid].1
                        lo = mid + 1
                    } else {
                        hi = mid - 1
                    }
                }
                ans[qi] = pos
            }
            while !st.isEmpty && st.last!.0 <= heights[i] { st.removeLast() }
            st.append((heights[i], i))
        }
        return ans
    }
}

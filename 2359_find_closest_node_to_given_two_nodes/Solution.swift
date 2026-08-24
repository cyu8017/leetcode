// LeetCode 2359 - Find Closest Node to Given Two Nodes
// https://leetcode.com/problems/find-closest-node-to-given-two-nodes/

class Solution {
    func closestMeetingNode(_ edges: [Int], _ node1: Int, _ node2: Int) -> Int {
        let n = edges.count
        func dist(_ start: Int) -> [Int] {
            var d = [Int](repeating: -1, count: n)
            var cur = start, step = 0
            while cur != -1 && d[cur] == -1 {
                d[cur] = step
                cur = edges[cur]
                step += 1
            }
            return d
        }
        let d1 = dist(node1), d2 = dist(node2)
        var ans = -1, best = Int.max
        for i in 0..<n {
            if d1[i] == -1 || d2[i] == -1 { continue }
            let mx = max(d1[i], d2[i])
            if mx < best { best = mx; ans = i }
        }
        return ans
    }
}

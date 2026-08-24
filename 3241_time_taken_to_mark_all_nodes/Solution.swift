// LeetCode 3241 - Time Taken to Mark All Nodes
// https://leetcode.com/problems/time-taken-to-mark-all-nodes/

class Solution {
    private var tree: [[Int]] = []
    private var top1: [(Int, Int)] = []
    private var top2: [(Int, Int)] = []
    private var ans: [Int] = []

    func timeTaken(_ edges: [[Int]]) -> [Int] {
        let n = edges.count + 1
        ans = Array(repeating: 0, count: n)
        tree = Array(repeating: [Int](), count: n)
        top1 = Array(repeating: (0, 0), count: n)
        top2 = Array(repeating: (0, 0), count: n)
        for e in edges {
            tree[e[0]].append(e[1])
            tree[e[1]].append(e[0])
        }
        _ = dfs(0, -1)
        reroot(0, -1, 0)
        return ans
    }

    private func getTime(_ u: Int) -> Int { u % 2 == 0 ? 2 : 1 }

    private func dfs(_ u: Int, _ prev: Int) -> Int {
        var t1 = (0, 0), t2 = (0, 0)
        for v in tree[u] where v != prev {
            let t = dfs(v, u) + getTime(v)
            if t >= t1.1 {
                t2 = t1
                t1 = (v, t)
            } else if t > t2.1 {
                t2 = (v, t)
            }
        }
        top1[u] = t1
        top2[u] = t2
        return t1.1
    }

    private func reroot(_ u: Int, _ prev: Int, _ maxTime: Int) {
        ans[u] = max(maxTime, top1[u].1)
        for v in tree[u] where v != prev {
            let side = top1[u].0 == v ? top2[u].1 : top1[u].1
            reroot(v, u, getTime(u) + max(maxTime, side))
        }
    }
}

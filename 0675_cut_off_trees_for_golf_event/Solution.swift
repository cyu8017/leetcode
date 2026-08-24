// LeetCode 0675 - Cut Off Trees for Golf Event
// https://leetcode.com/problems/cut-off-trees-for-golf-event/

class Solution {
    func cutOffTree(_ forest: [[Int]]) -> Int {
        var trees = [[Int]]()
        for i in 0..<forest.count {
            for j in 0..<forest[0].count where forest[i][j] > 1 {
                trees.append([forest[i][j], i, j])
            }
        }
        trees.sort { $0[0] < $1[0] }
        var sr = 0, sc = 0, steps = 0
        for tree in trees {
            let dist = bfs(forest, sr, sc, tree[1], tree[2])
            if dist < 0 { return -1 }
            steps += dist
            sr = tree[1]
            sc = tree[2]
        }
        return steps
    }

    private func bfs(_ forest: [[Int]], _ sr: Int, _ sc: Int, _ tr: Int, _ tc: Int) -> Int {
        if sr == tr && sc == tc { return 0 }
        let m = forest.count, n = forest[0].count
        var seen = Array(repeating: Array(repeating: false, count: n), count: m)
        var queue = [[sr, sc, 0]]
        var idx = 0
        seen[sr][sc] = true
        let dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while idx < queue.count {
            let cur = queue[idx]
            idx += 1
            for (dr, dc) in dirs {
                let nr = cur[0] + dr, nc = cur[1] + dc
                if nr < 0 || nr >= m || nc < 0 || nc >= n || seen[nr][nc] || forest[nr][nc] == 0 { continue }
                if nr == tr && nc == tc { return cur[2] + 1 }
                seen[nr][nc] = true
                queue.append([nr, nc, cur[2] + 1])
            }
        }
        return -1
    }
}

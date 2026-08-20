// LeetCode 1240 - Tiling a Rectangle with the Fewest Squares
// https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares/

class Solution {
    func tilingRectangle(_ n: Int, _ m: Int) -> Int {
        if n == m { return 1 }
        var height = [Int](repeating: 0, count: m)
        var ans = n * m
        func dfs(_ count: Int) {
            if count >= ans { return }
            var minH = height.min()!, start = -1
            for i in 0..<m where height[i] == minH { start = i; break }
            if minH == n {
                ans = count
                return
            }
            var end = start
            while end < m && height[end] == minH && end - start + 1 <= n - minH { end += 1 }
            for size in stride(from: end - start, through: 1, by: -1) {
                for j in start..<(start + size) { height[j] += size }
                dfs(count + 1)
                for j in start..<(start + size) { height[j] -= size }
            }
        }
        dfs(0)
        return ans
    }
}

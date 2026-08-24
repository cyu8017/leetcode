// LeetCode 2326 - Spiral Matrix IV
// https://leetcode.com/problems/spiral-matrix-iv/

class ListNode {
    var val: Int
    var next: ListNode?
    init() { self.val = 0; self.next = nil }
    init(_ val: Int) { self.val = val; self.next = nil }
    init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next }
}

class Solution {
    func spiralMatrix(_ m: Int, _ n: Int, _ head: ListNode?) -> [[Int]] {
        var ans = [[Int]](repeating: [Int](repeating: -1, count: n), count: m)
        let dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        var r = 0, c = 0, d = 0
        var head = head
        while let node = head {
            ans[r][c] = node.val
            head = node.next
            var nr = r + dirs[d].0, nc = c + dirs[d].1
            if nr < 0 || nr >= m || nc < 0 || nc >= n || ans[nr][nc] != -1 {
                d = (d + 1) % 4
                nr = r + dirs[d].0
                nc = c + dirs[d].1
            }
            r = nr
            c = nc
        }
        return ans
    }
}

// LeetCode 2326 - Spiral Matrix IV
// https://leetcode.com/problems/spiral-matrix-iv/

#[derive(Debug, PartialEq, Eq)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl Solution {
    pub fn spiral_matrix(m: i32, n: i32, mut head: Option<Box<ListNode>>) -> Vec<Vec<i32>> {
        let m = m as usize;
        let n = n as usize;
        let mut ans = vec![vec![-1; n]; m];
        let dirs = [(0isize, 1isize), (1, 0), (0, -1), (-1, 0)];
        let mut r = 0isize;
        let mut c = 0isize;
        let mut d = 0usize;
        while let Some(node) = head {
            ans[r as usize][c as usize] = node.val;
            head = node.next;
            let mut nr = r + dirs[d].0;
            let mut nc = c + dirs[d].1;
            if nr < 0
                || nr >= m as isize
                || nc < 0
                || nc >= n as isize
                || ans[nr as usize][nc as usize] != -1
            {
                d = (d + 1) % 4;
                nr = r + dirs[d].0;
                nc = c + dirs[d].1;
            }
            r = nr;
            c = nc;
        }
        ans
    }
}

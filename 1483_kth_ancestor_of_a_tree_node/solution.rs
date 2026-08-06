// LeetCode 1483 - Kth Ancestor of a Tree Node
// https://leetcode.com/problems/kth-ancestor-of-a-tree-node/

struct TreeAncestor {
    up: Vec<Vec<i32>>,
}

impl TreeAncestor {
    fn new(n: i32, parent: Vec<i32>) -> Self {
        let width = (n as u32).max(1).ilog2() as usize + 1;
        let mut up = vec![parent];
        for _ in 1..width {
            let prev = up.last().unwrap();
            let next: Vec<i32> = prev
                .iter()
                .map(|&p| if p == -1 { -1 } else { prev[p as usize] })
                .collect();
            up.push(next);
        }
        Self { up }
    }

    fn get_kth_ancestor(&self, mut node: i32, mut k: i32) -> i32 {
        let mut bit = 0;
        while k != 0 && node != -1 {
            if k & 1 == 1 {
                if bit >= self.up.len() {
                    return -1;
                }
                node = self.up[bit][node as usize];
            }
            bit += 1;
            k >>= 1;
        }
        node
    }
}

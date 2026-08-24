// LeetCode 3608 - Minimum Time for K Connected Components
// https://leetcode.com/problems/minimum-time-for-k-connected-components/

struct UnionFind {
    p: Vec<usize>,
    size: Vec<i32>,
}

impl UnionFind {
    fn new(n: usize) -> Self {
        Self {
            p: (0..n).collect(),
            size: vec![1; n],
        }
    }
    fn find(&mut self, x: usize) -> usize {
        if self.p[x] != x {
            self.p[x] = self.find(self.p[x]);
        }
        self.p[x]
    }
    fn unite(&mut self, a: usize, b: usize) -> bool {
        let mut pa = self.find(a);
        let mut pb = self.find(b);
        if pa == pb {
            return false;
        }
        if self.size[pa] > self.size[pb] {
            self.p[pb] = pa;
            self.size[pa] += self.size[pb];
        } else {
            self.p[pa] = pb;
            self.size[pb] += self.size[pa];
        }
        true
    }
}

impl Solution {
    pub fn min_time(n: i32, mut edges: Vec<Vec<i32>>, k: i32) -> i32 {
        edges.sort_by_key(|e| e[2]);
        let mut uf = UnionFind::new(n as usize);
        let mut cnt = n;
        for i in (0..edges.len()).rev() {
            if uf.unite(edges[i][0] as usize, edges[i][1] as usize) {
                cnt -= 1;
                if cnt < k {
                    return edges[i][2];
                }
            }
        }
        0
    }
}

// LeetCode 3600 - Maximize Spanning Tree Stability with Upgrades
// https://leetcode.com/problems/maximize-spanning-tree-stability-with-upgrades/

struct UnionFind {
    p: Vec<usize>,
    size: Vec<i32>,
    cnt: i32,
}

impl UnionFind {
    fn new(n: usize) -> Self {
        Self {
            p: (0..n).collect(),
            size: vec![1; n],
            cnt: n as i32,
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
        self.cnt -= 1;
        true
    }
}

impl Solution {
    fn check(lim: i32, n: usize, edges: &[Vec<i32>], k: i32) -> bool {
        let mut uf = UnionFind::new(n);
        for e in edges {
            if e[2] >= lim {
                uf.unite(e[0] as usize, e[1] as usize);
            }
        }
        let mut rem = k;
        for e in edges {
            if e[2] * 2 >= lim && rem > 0 {
                if uf.unite(e[0] as usize, e[1] as usize) {
                    rem -= 1;
                }
            }
        }
        uf.cnt == 1
    }

    pub fn max_stability(n: i32, edges: Vec<Vec<i32>>, k: i32) -> i32 {
        let n = n as usize;
        let mut uf = UnionFind::new(n);
        let mut mn = 1_000_000;
        for e in &edges {
            if e[3] == 1 {
                mn = mn.min(e[2]);
                if !uf.unite(e[0] as usize, e[1] as usize) {
                    return -1;
                }
            }
        }
        for e in &edges {
            uf.unite(e[0] as usize, e[1] as usize);
        }
        if uf.cnt > 1 {
            return -1;
        }
        let mut l = 1;
        let mut r = mn;
        while l < r {
            let mid = (l + r + 1) >> 1;
            if Self::check(mid, n, &edges, k) {
                l = mid;
            } else {
                r = mid - 1;
            }
        }
        l
    }
}

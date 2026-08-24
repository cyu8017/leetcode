// LeetCode 3108 - Minimum Cost Walk in Weighted Graph
// https://leetcode.com/problems/minimum-cost-walk-in-weighted-graph/

struct UnionFind {
    p: Vec<usize>,
    size: Vec<i32>,
}

impl UnionFind {
    fn new(n: usize) -> Self {
        Self { p: (0..n).collect(), size: vec![1; n] }
    }
    fn find(&mut self, x: usize) -> usize {
        if self.p[x] != x {
            self.p[x] = self.find(self.p[x]);
        }
        self.p[x]
    }
    fn unite(&mut self, a: usize, b: usize) {
        let mut pa = self.find(a);
        let mut pb = self.find(b);
        if pa == pb {
            return;
        }
        if self.size[pa] > self.size[pb] {
            self.p[pb] = pa;
            self.size[pa] += self.size[pb];
        } else {
            self.p[pa] = pb;
            self.size[pb] += self.size[pa];
        }
    }
}

impl Solution {
    pub fn minimum_cost(n: i32, edges: Vec<Vec<i32>>, query: Vec<Vec<i32>>) -> Vec<i32> {
        let n = n as usize;
        let mut uf = UnionFind::new(n);
        let mut g = vec![-1i32; n];
        for e in &edges {
            uf.unite(e[0] as usize, e[1] as usize);
        }
        for e in &edges {
            let root = uf.find(e[0] as usize);
            g[root] &= e[2];
        }
        let mut ans = Vec::with_capacity(query.len());
        for q in &query {
            let (u, v) = (q[0] as usize, q[1] as usize);
            if u == v {
                ans.push(0);
                continue;
            }
            let a = uf.find(u);
            let b = uf.find(v);
            ans.push(if a == b { g[a] } else { -1 });
        }
        ans
    }
}

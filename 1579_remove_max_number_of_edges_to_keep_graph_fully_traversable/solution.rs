// LeetCode 1579 - Remove Max Number of Edges to Keep Graph Fully Traversable
// https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/

struct Dsu {
    parent: Vec<usize>,
    components: i32,
}

impl Dsu {
    fn new(n: usize) -> Self {
        Self {
            parent: (0..=n).collect(),
            components: n as i32,
        }
    }

    fn find(&mut self, mut x: usize) -> usize {
        while x != self.parent[x] {
            self.parent[x] = self.parent[self.parent[x]];
            x = self.parent[x];
        }
        x
    }

    fn union(&mut self, a: usize, b: usize) -> bool {
        let mut a = self.find(a);
        let mut b = self.find(b);
        if a == b {
            return false;
        }
        self.parent[a] = b;
        self.components -= 1;
        true
    }
}

impl Solution {
    pub fn max_num_edges_to_remove(n: i32, edges: Vec<Vec<i32>>) -> i32 {
        let mut alice = Dsu::new(n as usize);
        let mut bob = Dsu::new(n as usize);
        let mut used = 0;
        for e in &edges {
            if e[0] == 3 {
                let merged = alice.union(e[1] as usize, e[2] as usize);
                bob.union(e[1] as usize, e[2] as usize);
                if merged {
                    used += 1;
                }
            }
        }
        for e in &edges {
            if e[0] == 1 {
                if alice.union(e[1] as usize, e[2] as usize) {
                    used += 1;
                }
            } else if e[0] == 2 {
                if bob.union(e[1] as usize, e[2] as usize) {
                    used += 1;
                }
            }
        }
        if alice.components == 1 && bob.components == 1 {
            edges.len() as i32 - used
        } else {
            -1
        }
    }
}

// LeetCode 0684 - Redundant Connection
// https://leetcode.com/problems/redundant-connection/

impl Solution {
    pub fn find_redundant_connection(edges: Vec<Vec<i32>>) -> Vec<i32> {
        let n = edges.len();
        let mut parent: Vec<usize> = (0..=n).collect();
        for edge in edges {
            let u = edge[0] as usize;
            let v = edge[1] as usize;
            let pu = Self::find(&mut parent, u);
            let pv = Self::find(&mut parent, v);
            if pu == pv {
                return vec![edge[0], edge[1]];
            }
            parent[pu] = pv;
        }
        vec![]
    }

    fn find(parent: &mut [usize], mut x: usize) -> usize {
        while parent[x] != x {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        x
    }
}

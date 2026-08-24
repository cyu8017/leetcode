// LeetCode 0685 - Redundant Connection II
// https://leetcode.com/problems/redundant-connection-ii/

impl Solution {
    pub fn find_redundant_directed_connection(mut edges: Vec<Vec<i32>>) -> Vec<i32> {
        let n = edges.len();
        let mut parent = vec![0; n + 1];
        let mut cand1 = Vec::new();
        let mut cand2 = Vec::new();
        for i in 0..n {
            let u = edges[i][0];
            let v = edges[i][1] as usize;
            if parent[v] == 0 {
                parent[v] = u;
            } else {
                cand1 = vec![parent[v], v as i32];
                cand2 = vec![u, v as i32];
                edges[i] = vec![-1, -1];
                break;
            }
        }

        let mut uf: Vec<usize> = (0..=n).collect();
        for edge in &edges {
            if edge[0] < 0 {
                continue;
            }
            let pu = Self::find(&mut uf, edge[0] as usize);
            let pv = Self::find(&mut uf, edge[1] as usize);
            if pu == pv {
                return if cand1.is_empty() {
                    vec![edge[0], edge[1]]
                } else {
                    cand1
                };
            }
            uf[pu] = pv;
        }
        cand2
    }

    fn find(uf: &mut [usize], mut x: usize) -> usize {
        while uf[x] != x {
            uf[x] = uf[uf[x]];
            x = uf[x];
        }
        x
    }
}

// LeetCode 1697 - Checking Existence of Edge Length Limited Paths
// https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/

impl Solution {
    pub fn distance_limited_paths_exist(
        n: i32,
        edge_list: Vec<Vec<i32>>,
        queries: Vec<Vec<i32>>,
    ) -> Vec<bool> {
        let n = n as usize;
        let mut parent: Vec<usize> = (0..n).collect();
        fn find(parent: &mut [usize], mut x: usize) -> usize {
            while x != parent[x] {
                parent[x] = parent[parent[x]];
                x = parent[x];
            }
            x
        }
        let mut edges = edge_list;
        edges.sort_by_key(|e| e[2]);
        let mut qs: Vec<(i32, usize, usize, usize)> = queries
            .iter()
            .enumerate()
            .map(|(j, q)| (q[2], q[0] as usize, q[1] as usize, j))
            .collect();
        qs.sort_by_key(|q| q.0);
        let mut ans = vec![false; queries.len()];
        let mut i = 0usize;
        for (limit, p, q, idx) in qs {
            while i < edges.len() && edges[i][2] < limit {
                let a = find(&mut parent, edges[i][0] as usize);
                let b = find(&mut parent, edges[i][1] as usize);
                parent[a] = b;
                i += 1;
            }
            ans[idx] = find(&mut parent, p) == find(&mut parent, q);
        }
        ans
    }
}

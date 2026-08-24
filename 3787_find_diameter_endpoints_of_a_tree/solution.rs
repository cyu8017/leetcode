// LeetCode 3787 - Find Diameter Endpoints Of A Tree
// https://leetcode.com/problems/find-diameter-endpoints-of-a-tree/

impl Solution {
    pub fn find_special_nodes(n: i32, edges: Vec<Vec<i32>>) -> String {
        let n = n as usize;
        let mut g = vec![Vec::new(); n];
        for e in &edges {
            g[e[0] as usize].push(e[1] as usize);
            g[e[1] as usize].push(e[0] as usize);
        }
        let bfs = |start: usize| -> (usize, Vec<i32>) {
            let mut dist = vec![-1i32; n];
            dist[start] = 0;
            let mut q = vec![start];
            let mut far = start;
            let mut head = 0;
            while head < q.len() {
                let u = q[head];
                head += 1;
                if dist[u] > dist[far] {
                    far = u;
                }
                for &v in &g[u] {
                    if dist[v] == -1 {
                        dist[v] = dist[u] + 1;
                        q.push(v);
                    }
                }
            }
            (far, dist)
        };
        let (a, _) = bfs(0);
        let (b, dist1) = bfs(a);
        let (_, dist2) = bfs(b);
        let d = dist1[b];
        let mut ans = vec![b'0'; n];
        for i in 0..n {
            if dist1[i] == d || dist2[i] == d {
                ans[i] = b'1';
            }
        }
        String::from_utf8(ans).unwrap()
    }
}

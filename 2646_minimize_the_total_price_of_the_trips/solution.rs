// LeetCode 2646 - Minimize the Total Price of the Trips
// https://leetcode.com/problems/minimize-the-total-price-of-the-trips/

impl Solution {
    pub fn minimum_total_price(
        n: i32,
        edges: Vec<Vec<i32>>,
        price: Vec<i32>,
        trips: Vec<Vec<i32>>,
    ) -> i32 {
        let n = n as usize;
        let mut g = vec![Vec::new(); n];
        for e in &edges {
            g[e[0] as usize].push(e[1] as usize);
            g[e[1] as usize].push(e[0] as usize);
        }
        let mut cnt = vec![0i32; n];
        fn path(u: usize, p: i32, target: usize, g: &[Vec<usize>], cnt: &mut [i32]) -> bool {
            if u == target {
                cnt[u] += 1;
                return true;
            }
            for &v in &g[u] {
                if v as i32 == p {
                    continue;
                }
                if path(v, u as i32, target, g, cnt) {
                    cnt[u] += 1;
                    return true;
                }
            }
            false
        }
        for t in &trips {
            path(t[0] as usize, -1, t[1] as usize, &g, &mut cnt);
        }
        fn dfs(u: usize, p: i32, g: &[Vec<usize>], price: &[i32], cnt: &[i32]) -> (i32, i32) {
            let mut full = price[u] * cnt[u];
            let mut half = full / 2;
            for &v in &g[u] {
                if v as i32 == p {
                    continue;
                }
                let (nf, hf) = dfs(v, u as i32, g, price, cnt);
                full += nf.min(hf);
                half += nf;
            }
            (full, half)
        }
        let (a, b) = dfs(0, -1, &g, &price, &cnt);
        a.min(b)
    }
}

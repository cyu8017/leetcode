// LeetCode 3547 - Maximum Sum of Edge Values in a Graph
// https://leetcode.com/problems/maximum-sum-of-edge-values-in-a-graph/

impl Solution {
    fn calc(left: i32, right: i32, is_cycle: bool) -> i64 {
        let mut w0 = right;
        let mut w1 = right;
        let mut score = 0i64;
        for value in (left..=right - 1).rev() {
            score += w0 as i64 * value as i64;
            w0 = w1;
            w1 = value;
        }
        if is_cycle {
            score += w0 as i64 * w1 as i64;
        }
        score
    }

    pub fn max_score(n: i32, edges: Vec<Vec<i32>>) -> i64 {
        let n = n as usize;
        let mut graph = vec![Vec::<usize>::new(); n];
        for e in &edges {
            graph[e[0] as usize].push(e[1] as usize);
            graph[e[1] as usize].push(e[0] as usize);
        }
        let mut seen = vec![false; n];
        let mut cycle_sizes = Vec::new();
        let mut path_sizes = Vec::new();
        for i in 0..n {
            if seen[i] {
                continue;
            }
            let mut comp = vec![i];
            seen[i] = true;
            let mut qi = 0;
            while qi < comp.len() {
                for &v in &graph[comp[qi]] {
                    if !seen[v] {
                        seen[v] = true;
                        comp.push(v);
                    }
                }
                qi += 1;
            }
            let all_deg2 = comp.iter().all(|&u| graph[u].len() == 2);
            if all_deg2 {
                cycle_sizes.push(comp.len() as i32);
            } else if comp.len() > 1 {
                path_sizes.push(comp.len() as i32);
            }
        }
        let mut ans = 0i64;
        let mut cur_n = n as i32;
        for cs in cycle_sizes {
            ans += Self::calc(cur_n - cs + 1, cur_n, true);
            cur_n -= cs;
        }
        path_sizes.sort_by(|a, b| b.cmp(a));
        for ps in path_sizes {
            ans += Self::calc(cur_n - ps + 1, cur_n, false);
            cur_n -= ps;
        }
        ans
    }
}

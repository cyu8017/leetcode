// LeetCode 3161 - Block Placement Queries
// https://leetcode.com/problems/block-placement-queries/

struct FenwickMax {
    vals: Vec<i32>,
}

impl FenwickMax {
    fn new(n: usize) -> Self {
        Self { vals: vec![0; n + 1] }
    }
    fn maximize(&mut self, mut i: usize, val: i32) {
        while i < self.vals.len() {
            self.vals[i] = self.vals[i].max(val);
            i += i & i.wrapping_neg();
        }
    }
    fn get(&self, mut i: usize) -> i32 {
        let mut res = 0;
        while i > 0 {
            res = res.max(self.vals[i]);
            i -= i & i.wrapping_neg();
        }
        res
    }
}

impl Solution {
    pub fn get_results(queries: Vec<Vec<i32>>) -> Vec<bool> {
        let mut n = queries.len() * 3;
        if n > 50000 {
            n = 50000;
        }
        let mut tree = FenwickMax::new(n + 1);
        let mut obs = vec![0i32, n as i32];
        for q in &queries {
            if q[0] == 1 {
                let x = q[1];
                let j = obs.partition_point(|&v| v < x);
                if j == obs.len() || obs[j] != x {
                    obs.insert(j, x);
                }
            }
        }
        for i in 0..obs.len() - 1 {
            tree.maximize(obs[i + 1] as usize, obs[i + 1] - obs[i]);
        }
        let mut ans = Vec::new();
        for i in (0..queries.len()).rev() {
            let typ = queries[i][0];
            let x = queries[i][1];
            if typ == 1 {
                let j = obs.partition_point(|&v| v < x);
                let prev = obs[j - 1];
                let next = obs[j + 1];
                obs.remove(j);
                tree.maximize(next as usize, next - prev);
            } else {
                let sz = queries[i][2];
                let j = obs.partition_point(|&v| v < x + 1) - 1;
                let prev = obs[j];
                ans.push(tree.get(prev as usize) >= sz || x - prev >= sz);
            }
        }
        ans.reverse();
        ans
    }
}

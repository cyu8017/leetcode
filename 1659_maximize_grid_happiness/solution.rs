// LeetCode 1659 - Maximize Grid Happiness
// https://leetcode.com/problems/maximize-grid-happiness/

impl Solution {
    pub fn get_max_grid_happiness(
        m: i32,
        n: i32,
        introverts_count: i32,
        extroverts_count: i32,
    ) -> i32 {
        let m = m as usize;
        let n = n as usize;
        let ic = introverts_count as usize;
        let ec = extroverts_count as usize;
        let mut states = 1usize;
        for _ in 0..n {
            states *= 3;
        }
        let mut cells = vec![vec![0i32; n]; states];
        let mut intro = vec![0usize; states];
        let mut extro = vec![0usize; states];
        let mut row = vec![0i32; states];
        for s in 0..states {
            let mut x = s;
            for j in 0..n {
                cells[s][j] = (x % 3) as i32;
                x /= 3;
            }
            let mut val = 0i32;
            for j in 0..n {
                let z = cells[s][j];
                if z == 1 {
                    intro[s] += 1;
                    val += 120;
                } else if z == 2 {
                    extro[s] += 1;
                    val += 40;
                }
            }
            for j in 1..n {
                val += Self::pair_cost(cells[s][j - 1], cells[s][j]);
            }
            row[s] = val;
        }
        let mut compat = vec![vec![0i32; states]; states];
        for a in 0..states {
            for b in 0..states {
                let mut v = 0;
                for j in 0..n {
                    v += Self::pair_cost(cells[a][j], cells[b][j]);
                }
                compat[a][b] = v;
            }
        }
        let size = (m + 1) * states * (ic + 1) * (ec + 1);
        let mut memo = vec![0i32; size];
        let mut seen = vec![false; size];
        Self::dfs(
            0, 0, ic, ec, m, states, ic, ec, &intro, &extro, &row, &compat, &mut memo, &mut seen,
        )
    }

    fn pair_cost(a: i32, b: i32) -> i32 {
        if a == 0 || b == 0 {
            return 0;
        }
        let va = if a == 1 { -30 } else { 20 };
        let vb = if b == 1 { -30 } else { 20 };
        va + vb
    }

    fn dfs(
        r: usize,
        prev: usize,
        i: usize,
        e: usize,
        m: usize,
        states: usize,
        ic: usize,
        ec: usize,
        intro: &[usize],
        extro: &[usize],
        row: &[i32],
        compat: &[Vec<i32>],
        memo: &mut [i32],
        seen: &mut [bool],
    ) -> i32 {
        if r == m {
            return 0;
        }
        let id = (((r * states + prev) * (ic + 1) + i) * (ec + 1)) + e;
        if seen[id] {
            return memo[id];
        }
        let mut best = 0;
        for s in 0..states {
            if intro[s] > i || extro[s] > e {
                continue;
            }
            let val = row[s]
                + compat[prev][s]
                + Self::dfs(
                    r + 1,
                    s,
                    i - intro[s],
                    e - extro[s],
                    m,
                    states,
                    ic,
                    ec,
                    intro,
                    extro,
                    row,
                    compat,
                    memo,
                    seen,
                );
            best = best.max(val);
        }
        seen[id] = true;
        memo[id] = best;
        best
    }
}

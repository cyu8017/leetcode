struct Solution;
// LeetCode 3906 - Count Good Integers on a Grid Path
// https://leetcode.com/problems/count-good-integers-on-a-grid-path/

impl Solution {
    pub fn count_good_integers_on_path(l: i64, r: i64, directions: String) -> i64 {
        let mut key = [false; 16];
        let mut row = 0;
        let mut col = 0;
        key[0] = true;
        for c in directions.chars() {
            if c == 'D' {
                row += 1;
            } else {
                col += 1;
            }
            key[row * 4 + col] = true;
        }
        fn dfs(
            pos: usize,
            last: usize,
            lim: bool,
            s: &[u8],
            key: &[bool; 16],
            f: &mut [[i64; 10]; 16],
        ) -> i64 {
            if pos == 16 {
                return 1;
            }
            if !lim && f[pos][last] != -1 {
                return f[pos][last];
            }
            let mut res = 0i64;
            let start = if key[pos] { last } else { 0 };
            let end = if lim { (s[pos] - b'0') as usize } else { 9 };
            for i in start..=end {
                let next_last = if key[pos] { i } else { last };
                res += dfs(pos + 1, next_last, lim && i == end, s, key, f);
            }
            if !lim {
                f[pos][last] = res;
            }
            res
        }
        let calc = |x: i64| -> i64 {
            if x < 0 {
                return 0;
            }
            let t = x.to_string();
            let s = format!("{:0>16}", t);
            let sb = s.into_bytes();
            let mut f = [[-1i64; 10]; 16];
            dfs(0, 0, true, &sb, &key, &mut f)
        };
        calc(r) - calc(l - 1)
    }
}

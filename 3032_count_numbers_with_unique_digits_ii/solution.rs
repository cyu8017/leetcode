// LeetCode 3032 - Count Numbers With Unique Digits II
// https://leetcode.com/problems/count-numbers-with-unique-digits-ii/

impl Solution {
    pub fn number_count(a: i32, b: i32) -> i32 {
        fn solve(num: i32) -> i32 {
            if num < 0 {
                return 0;
            }
            let s = num.to_string();
            let bytes = s.as_bytes();
            let n = bytes.len();
            let mut f = vec![vec![-1i32; 1 << 10]; n];
            fn dfs(
                pos: usize,
                mask: usize,
                limit: bool,
                bytes: &[u8],
                f: &mut [Vec<i32>],
            ) -> i32 {
                if pos >= bytes.len() {
                    return if mask != 0 { 1 } else { 0 };
                }
                if !limit && f[pos][mask] != -1 {
                    return f[pos][mask];
                }
                let up = if limit { (bytes[pos] - b'0') as usize } else { 9 };
                let mut ans = 0;
                for i in 0..=up {
                    if (mask >> i) & 1 == 1 {
                        continue;
                    }
                    let mut nxt = mask | (1 << i);
                    if mask == 0 && i == 0 {
                        nxt = 0;
                    }
                    ans += dfs(pos + 1, nxt, limit && i == up, bytes, f);
                }
                if !limit {
                    f[pos][mask] = ans;
                }
                ans
            }
            dfs(0, 0, true, bytes, &mut f)
        }
        solve(b) - solve(a - 1)
    }
}

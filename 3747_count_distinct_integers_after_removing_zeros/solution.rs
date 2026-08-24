// LeetCode 3747 - Count Distinct Integers After Removing Zeros
// https://leetcode.com/problems/count-distinct-integers-after-removing-zeros/

impl Solution {
    pub fn count_distinct(n: i64) -> i64 {
        let s = n.to_string();
        let m = s.len();
        let bytes = s.as_bytes();
        let mut f = [[[[-1i64; 2]; 2]; 2]; 20];

        fn dfs(
            i: usize,
            zero: usize,
            lead: usize,
            limit: usize,
            m: usize,
            bytes: &[u8],
            f: &mut [[[[i64; 2]; 2]; 2]; 20],
        ) -> i64 {
            if i == m {
                return if zero == 0 && lead == 0 { 1 } else { 0 };
            }
            if limit == 0 && f[i][zero][lead][limit] != -1 {
                return f[i][zero][lead][limit];
            }
            let up = if limit == 1 { (bytes[i] - b'0') as i32 } else { 9 };
            let mut ans = 0i64;
            for d in 0..=up {
                let nxt_zero = if d == 0 && lead == 0 { 1 } else { zero };
                let nxt_lead = if lead == 1 && d == 0 { 1 } else { 0 };
                let nxt_limit = if limit == 1 && d == up { 1 } else { 0 };
                ans += dfs(i + 1, nxt_zero, nxt_lead, nxt_limit, m, bytes, f);
            }
            if limit == 0 {
                f[i][zero][lead][limit] = ans;
            }
            ans
        }

        dfs(0, 0, 1, 1, m, bytes, &mut f)
    }
}

// LeetCode 3791 - Number Of Balanced Integers In A Range
// https://leetcode.com/problems/number-of-balanced-integers-in-a-range/

impl Solution {
    pub fn count_balanced(mut low: i64, high: i64) -> i64 {
        const BASE: i32 = 90;
        if high < 11 {
            return 0;
        }
        if low < 11 {
            low = 11;
        }

        fn dfs(pos: usize, diff: i32, lim: bool, num: &[u8], f: &mut [[i64; 181]; 20]) -> i64 {
            if pos >= num.len() {
                return if diff == 0 { 1 } else { 0 };
            }
            if !lim && f[pos][(diff + BASE) as usize] != -1 {
                return f[pos][(diff + BASE) as usize];
            }
            let up = if lim { (num[pos] - b'0') as i32 } else { 9 };
            let mut res = 0i64;
            for i in 0..=up {
                if pos % 2 == 0 {
                    res += dfs(pos + 1, diff + i, lim && i == up, num, f);
                } else {
                    res += dfs(pos + 1, diff - i, lim && i == up, num, f);
                }
            }
            if !lim {
                f[pos][(diff + BASE) as usize] = res;
            }
            res
        }

        let num = (low - 1).to_string();
        let mut f = [[-1i64; 181]; 20];
        let a = dfs(0, 0, true, num.as_bytes(), &mut f);
        let num = high.to_string();
        let mut f = [[-1i64; 181]; 20];
        let b = dfs(0, 0, true, num.as_bytes(), &mut f);
        b - a
    }
}

struct Solution;
// LeetCode 3869 - Count Fancy Numbers in a Range
// https://leetcode.com/problems/count-fancy-numbers-in-a-range/

impl Solution {
    pub fn count_fancy(l: i64, r: i64) -> i64 {
        fn check(s: i32) -> bool {
            if s < 100 {
                return s % 11 != 0;
            }
            let mid = (s / 10) % 10;
            let last = s % 10;
            mid > 1 && mid < last
        }
        fn calc(x: i64) -> i64 {
            let num: Vec<u8> = x.to_string().into_bytes();
            let n = num.len();
            let mut f = vec![vec![vec![vec![-1i64; 4]; 10]; 9 * n + 1]; n];
            fn dfs(
                pos: usize,
                s: usize,
                prev: usize,
                st: usize,
                lim: bool,
                num: &[u8],
                f: &mut [Vec<Vec<Vec<i64>>>],
            ) -> i64 {
                if pos >= num.len() {
                    return if st != 3 {
                        1
                    } else if check(s as i32) {
                        1
                    } else {
                        0
                    };
                }
                if !lim && f[pos][s][prev][st] != -1 {
                    return f[pos][s][prev][st];
                }
                let up = if lim { (num[pos] - b'0') as usize } else { 9 };
                let mut res = 0i64;
                for i in 0..=up {
                    let nxt_st = if st == 0 {
                        if prev == 0 {
                            0
                        } else if i > prev {
                            1
                        } else if i < prev {
                            2
                        } else {
                            3
                        }
                    } else if st == 1 {
                        if i > prev { 1 } else { 3 }
                    } else if st == 2 {
                        if i < prev { 2 } else { 3 }
                    } else {
                        3
                    };
                    res += dfs(pos + 1, s + i, i, nxt_st, lim && i == up, num, f);
                }
                if !lim {
                    f[pos][s][prev][st] = res;
                }
                res
            }
            dfs(0, 0, 0, 0, true, &num, &mut f)
        }
        calc(r) - calc(l - 1)
    }
}

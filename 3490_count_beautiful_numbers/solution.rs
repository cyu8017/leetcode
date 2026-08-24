// LeetCode 3490 - Count Beautiful Numbers
// https://leetcode.com/problems/count-beautiful-numbers/

impl Solution {
    fn itoa3490(mut x: i32) -> String {
        if x == 0 {
            return "0".to_string();
        }
        let mut b = String::new();
        while x > 0 {
            b.insert(0, char::from(b'0' + (x % 10) as u8));
            x /= 10;
        }
        b
    }

    fn count_beautiful(n: i32) -> i32 {
        if n <= 0 {
            return 0;
        }
        let s = Self::itoa3490(n);
        fn dfs(pos: usize, tight: bool, sum: i32, prod: i32, started: bool, s: &[u8]) -> i32 {
            if pos == s.len() {
                if !started {
                    return 0;
                }
                return if sum > 0 && prod % sum == 0 { 1 } else { 0 };
            }
            let up = if tight { (s[pos] - b'0') as i32 } else { 9 };
            let mut ans = 0;
            for d in 0..=up {
                let nt = tight && d == up;
                if !started && d == 0 {
                    ans += dfs(pos + 1, nt, 0, 1, false, s);
                } else {
                    let ns = sum + d;
                    let np = if !started { d } else { prod * d };
                    ans += dfs(pos + 1, nt, ns, np, true, s);
                }
            }
            ans
        }
        dfs(0, true, 0, 1, false, s.as_bytes())
    }

    pub fn beautiful_numbers(l: i32, r: i32) -> i32 {
        Self::count_beautiful(r) - Self::count_beautiful(l - 1)
    }
}

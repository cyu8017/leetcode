struct Solution;
fn main() {}

// LeetCode 2800 - Shortest String That Contains Three Strings
// https://leetcode.com/problems/shortest-string-that-contains-three-strings/

impl Solution {
    pub fn minimum_string(a: String, b: String, c: String) -> String {
        fn merge(x: &str, y: &str) -> String {
            if x.contains(y) {
                return x.to_string();
            }
            let mut best = format!("{}{}", x, y);
            let n = x.len().min(y.len());
            for i in (1..=n).rev() {
                if x[x.len() - i..] == y[..i] {
                    let cand = format!("{}{}", x, &y[i..]);
                    if cand.len() < best.len() || (cand.len() == best.len() && cand < best) {
                        best = cand;
                    }
                    break;
                }
            }
            best
        }
        let perms = [
            [&a, &b, &c],
            [&a, &c, &b],
            [&b, &a, &c],
            [&b, &c, &a],
            [&c, &a, &b],
            [&c, &b, &a],
        ];
        let mut ans = String::new();
        for p in perms {
            let cur = merge(&merge(p[0], p[1]), p[2]);
            if ans.is_empty()
                || cur.len() < ans.len()
                || (cur.len() == ans.len() && cur < ans)
            {
                ans = cur;
            }
        }
        ans
    }
}

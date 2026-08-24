struct Solution;
// LeetCode 3455 - Shortest Matching Substring
// https://leetcode.com/problems/shortest-matching-substring/

impl Solution {
    pub fn shortest_matching_substring(s: String, p: String) -> i32 {
        let mut parts = Vec::new();
        let mut cur = String::new();
        for c in p.chars() {
            if c == '*' {
                parts.push(std::mem::take(&mut cur));
            } else {
                cur.push(c);
            }
        }
        parts.push(cur);
        while parts.len() < 3 {
            parts.push(String::new());
        }
        let a = &parts[0];
        let b = &parts[1];
        let c = &parts[2];
        let n = s.len();
        let find_all = |sub: &str| -> Vec<usize> {
            if sub.is_empty() {
                return (0..=n).collect();
            }
            let mut res = Vec::new();
            let mut start = 0;
            while let Some(pos) = s[start..].find(sub) {
                let idx = start + pos;
                res.push(idx);
                start = idx + 1;
            }
            res
        };
        let sort_search = |arr: &[usize], x: usize| -> usize { arr.partition_point(|&v| v < x) };
        let pos_a = find_all(a);
        let pos_b = find_all(b);
        let pos_c = find_all(c);
        let mut ans = n + 1;
        for &ia in &pos_a {
            let end_a = ia + a.len();
            let mut bi = sort_search(&pos_b, end_a);
            while bi < pos_b.len() {
                let end_b = pos_b[bi] + b.len();
                let ci = sort_search(&pos_c, end_b);
                if ci < pos_c.len() {
                    let length = pos_c[ci] + c.len() - ia;
                    if length < ans {
                        ans = length;
                    }
                }
                break;
            }
        }
        if ans == n + 1 {
            -1
        } else {
            ans as i32
        }
    }
}

fn main() {}

// LeetCode 3646 - Next Special Palindrome Number
// https://leetcode.com/problems/next-special-palindrome-number/

impl Solution {
    pub fn special_palindrome(n: i64) -> i64 {
        let mut cands = Vec::new();
        for mask in 1..(1 << 10) {
            if mask & 1 != 0 {
                continue;
            }
            let mut total = 0;
            let mut odd = 0;
            for d in 1..=9 {
                if (mask >> d) & 1 == 1 {
                    total += d;
                    if d % 2 == 1 {
                        odd += 1;
                    }
                }
            }
            if total == 0 || total > 18 || odd > 1 {
                continue;
            }
            let mut half_cnt = [0i32; 10];
            let mut mid = 0;
            for d in 1..=9 {
                if (mask >> d) & 1 == 0 {
                    continue;
                }
                half_cnt[d] = d as i32 / 2;
                if d % 2 == 1 {
                    mid = d;
                }
            }
            let half_len = total / 2;
            fn dfs(
                pos: i32,
                half_len: i32,
                mid: i32,
                half_cnt: &mut [i32; 10],
                cur: &mut Vec<i32>,
                cands: &mut Vec<i64>,
            ) {
                if pos == half_len {
                    let left: String = cur.iter().map(|&x| char::from(b'0' + x as u8)).collect();
                    let mut s = left.clone();
                    if mid > 0 {
                        s.push(char::from(b'0' + mid as u8));
                    }
                    s.push_str(&left.chars().rev().collect::<String>());
                    if let Ok(v) = s.parse::<i64>() {
                        cands.push(v);
                    }
                    return;
                }
                for d in 1..=9 {
                    if half_cnt[d] == 0 {
                        continue;
                    }
                    half_cnt[d] -= 1;
                    cur.push(d as i32);
                    dfs(pos + 1, half_len, mid, half_cnt, cur, cands);
                    cur.pop();
                    half_cnt[d] += 1;
                }
            }
            let mut cur = Vec::new();
            dfs(0, half_len, mid, &mut half_cnt, &mut cur, &mut cands);
        }
        cands.sort_unstable();
        for v in cands {
            if v > n {
                return v;
            }
        }
        -1
    }
}

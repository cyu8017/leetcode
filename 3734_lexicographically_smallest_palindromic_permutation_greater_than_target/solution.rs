// LeetCode 3734 - Lexicographically Smallest Palindromic Permutation Greater Than Target
// https://leetcode.com/problems/lexicographically-smallest-palindromic-permutation-greater-than-target/

impl Solution {
    pub fn lex_palindromic_permutation(s: String, target: String) -> String {
        let mut cnt = [0i32; 26];
        for c in s.bytes() {
            cnt[(c - b'a') as usize] += 1;
        }
        let mut odd = 0;
        let mut mid = -1i32;
        for i in 0..26 {
            if cnt[i] % 2 == 1 {
                odd += 1;
                mid = i as i32;
            }
        }
        if odd > 1 {
            return String::new();
        }
        let mut half = [0i32; 26];
        for i in 0..26 {
            half[i] = cnt[i] / 2;
        }
        let n = s.len();
        let half_len = n / 2;
        let target = target.as_bytes();
        let mut left = vec![b' '; half_len];

        fn dfs(
            pos: usize,
            greater: bool,
            half_len: usize,
            mid: i32,
            target: &[u8],
            half: &mut [i32; 26],
            left: &mut [u8],
        ) -> bool {
            if pos == half_len {
                if mid >= 0 {
                    if greater {
                        return true;
                    }
                    return (b'a' + mid as u8) > target[half_len];
                }
                return greater;
            }
            let start = if greater { 0 } else { (target[pos] - b'a') as usize };
            for c in start..26 {
                if half[c] == 0 {
                    continue;
                }
                half[c] -= 1;
                left[pos] = b'a' + c as u8;
                if dfs(
                    pos + 1,
                    greater || c > (target[pos] - b'a') as usize,
                    half_len,
                    mid,
                    target,
                    half,
                    left,
                ) {
                    return true;
                }
                half[c] += 1;
            }
            false
        }

        if !dfs(0, false, half_len, mid, target, &mut half, &mut left) {
            return String::new();
        }
        let mut res = left.clone();
        if mid >= 0 {
            res.push(b'a' + mid as u8);
        }
        for i in (0..half_len).rev() {
            res.push(left[i]);
        }
        let res = String::from_utf8(res).unwrap();
        if res.as_bytes() <= target {
            String::new()
        } else {
            res
        }
    }
}

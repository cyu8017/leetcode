// LeetCode 1794 - Count Pairs of Equal Substrings With Minimum Difference
// https://leetcode.com/problems/count-pairs-of-equal-substrings-with-minimum-difference/

impl Solution {
    pub fn count_quadruples(first_string: String, second_string: String) -> i64 {
        let a = first_string.as_bytes();
        let b = second_string.as_bytes();
        let mut first = [-1i64; 26];
        let mut last_f = [-1i64; 26];
        let mut last_s = [-1i64; 26];
        for (i, &ch) in a.iter().enumerate() {
            let c = (ch - b'a') as usize;
            if first[c] == -1 {
                first[c] = i as i64;
            }
            last_f[c] = i as i64;
        }
        for (i, &ch) in b.iter().enumerate() {
            last_s[(ch - b'a') as usize] = i as i64;
        }
        let mut best = i64::MAX;
        for c in 0..26 {
            if first[c] != -1 && last_s[c] != -1 {
                best = best.min(last_f[c] - last_s[c]);
            }
        }
        if best == i64::MAX {
            return 0;
        }
        let mut ans: i64 = 0;
        for c in 0..26 {
            if first[c] == -1 || last_s[c] == -1 || last_f[c] - last_s[c] != best {
                continue;
            }
            let ch = b'a' + c as u8;
            let i_count = (first[c] as usize..=last_f[c] as usize)
                .filter(|&k| a[k] == ch)
                .count() as i64;
            let a_count = (0..=last_s[c] as usize).filter(|&k| b[k] == ch).count() as i64;
            ans += i_count * a_count;
        }
        ans
    }
}

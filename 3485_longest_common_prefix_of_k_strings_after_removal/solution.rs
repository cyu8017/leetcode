// LeetCode 3485 - Longest Common Prefix of K Strings After Removal
// https://leetcode.com/problems/longest-common-prefix-of-k-strings-after-removal/

impl Solution {
    fn lcp_of(a: &[String]) -> i32 {
        if a.is_empty() {
            return 0;
        }
        let mut pref = a[0].clone();
        for t in 1..a.len() {
            let s = &a[t];
            let mut i = 0;
            while i < pref.len() && i < s.len() && pref.as_bytes()[i] == s.as_bytes()[i] {
                i += 1;
            }
            pref.truncate(i);
            if pref.is_empty() {
                return 0;
            }
        }
        pref.len() as i32
    }

    pub fn longest_common_prefix(words: Vec<String>, k: i32) -> Vec<i32> {
        let n = words.len();
        let mut ans = vec![0; n];
        for i in 0..n {
            let mut rest: Vec<String> = words
                .iter()
                .enumerate()
                .filter(|(j, _)| *j != i)
                .map(|(_, w)| w.clone())
                .collect();
            if rest.len() < k as usize {
                ans[i] = 0;
                continue;
            }
            rest.sort();
            let mut best = 0;
            let mut j = 0;
            while j + k as usize - 1 < rest.len() {
                let window = &rest[j..j + k as usize];
                best = best.max(Self::lcp_of(window));
                j += 1;
            }
            ans[i] = best;
        }
        ans
    }
}

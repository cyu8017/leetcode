// LeetCode 2559 - Count Vowel Strings in Ranges
// https://leetcode.com/problems/count-vowel-strings-in-ranges/

impl Solution {
    pub fn vowel_strings(words: Vec<String>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        fn is_v(c: u8) -> bool {
            matches!(c, b'a' | b'e' | b'i' | b'o' | b'u')
        }
        let n = words.len();
        let mut pref = vec![0; n + 1];
        for i in 0..n {
            pref[i + 1] = pref[i];
            let w = words[i].as_bytes();
            if !w.is_empty() && is_v(w[0]) && is_v(w[w.len() - 1]) {
                pref[i + 1] += 1;
            }
        }
        queries
            .into_iter()
            .map(|q| pref[q[1] as usize + 1] - pref[q[0] as usize])
            .collect()
    }
}

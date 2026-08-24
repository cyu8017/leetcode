// LeetCode 2273 - Find Resultant Array After Removing Anagrams
// https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/

impl Solution {
    pub fn remove_anagrams(words: Vec<String>) -> Vec<String> {
        fn sig(w: &str) -> [i32; 26] {
            let mut c = [0; 26];
            for ch in w.bytes() {
                c[(ch - b'a') as usize] += 1;
            }
            c
        }
        let mut ans = vec![words[0].clone()];
        let mut prev = sig(&words[0]);
        for w in words.iter().skip(1) {
            let cur = sig(w);
            if cur != prev {
                ans.push(w.clone());
                prev = cur;
            }
        }
        ans
    }
}

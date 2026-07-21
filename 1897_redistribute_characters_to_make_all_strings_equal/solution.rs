// LeetCode 1897 - Redistribute Characters to Make All Strings Equal
// https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/

impl Solution {
    pub fn make_equal(words: Vec<String>) -> bool {
        let n = words.len();
        let mut counts = [0i32; 26];
        for word in &words {
            for b in word.bytes() {
                counts[(b - b'a') as usize] += 1;
            }
        }
        counts.iter().all(|&c| c as usize % n == 0)
    }
}

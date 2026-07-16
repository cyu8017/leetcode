// LeetCode 0243 - Shortest Word Distance
// https://leetcode.com/problems/shortest-word-distance/

impl Solution {
    pub fn shortest_word_distance(words_dict: Vec<String>, word1: String, word2: String) -> i32 {
        let mut index1 = -1i32;
        let mut index2 = -1i32;
        let mut best = i32::MAX;
        for (index, word) in words_dict.iter().enumerate() {
            if word == &word1 {
                index1 = index as i32;
                if index2 >= 0 {
                    best = best.min(index as i32 - index2);
                }
            }
            if word == &word2 {
                index2 = index as i32;
                if index1 >= 0 {
                    best = best.min(index as i32 - index1);
                }
            }
        }
        best
    }
}

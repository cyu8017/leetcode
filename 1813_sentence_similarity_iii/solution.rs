// LeetCode 1813 - Sentence Similarity III
// https://leetcode.com/problems/sentence-similarity-iii/

impl Solution {
    pub fn are_sentences_similar(sentence1: String, sentence2: String) -> bool {
        let words1: Vec<&str> = sentence1.split_whitespace().collect();
        let words2: Vec<&str> = sentence2.split_whitespace().collect();
        let n1 = words1.len();
        let n2 = words2.len();

        let mut i = 0;
        while i < n1 && i < n2 && words1[i] == words2[i] {
            i += 1;
        }
        if i == n1 || i == n2 {
            return true;
        }

        let mut j1 = n1 as i32 - 1;
        let mut j2 = n2 as i32 - 1;
        while j1 >= i as i32 && j2 >= i as i32 && words1[j1 as usize] == words2[j2 as usize] {
            j1 -= 1;
            j2 -= 1;
        }
        j1 < i as i32 || j2 < i as i32
    }
}

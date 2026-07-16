// LeetCode 0418 - Sentence Screen Fitting
// https://leetcode.com/problems/sentence-screen-fitting/

impl Solution {
    pub fn words_typing(sentence: Vec<String>, rows: i32, cols: i32) -> i32 {
        let mut count = 0;
        let mut index = 0usize;
        let total = sentence.len();

        for _ in 0..rows {
            let mut col = 0;
            loop {
                let word = &sentence[index];
                let needed = word.len() as i32 + if col > 0 { 1 } else { 0 };
                if col + needed > cols {
                    break;
                }
                if col > 0 {
                    col += 1;
                }
                col += word.len() as i32;
                index = (index + 1) % total;
                if index == 0 {
                    count += 1;
                }
            }
        }

        count
    }
}

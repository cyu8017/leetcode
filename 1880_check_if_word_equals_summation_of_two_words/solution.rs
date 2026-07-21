// LeetCode 1880 - Check if Word Equals Summation of Two Words
// https://leetcode.com/problems/check-if-word-equals-summation-of-two-words/

impl Solution {
    pub fn is_sum_equal(first_word: String, second_word: String, target_word: String) -> bool {
        fn value(word: &str) -> i32 {
            word.bytes()
                .fold(0, |acc, ch| acc * 10 + (ch - b'a') as i32)
        }
        value(&first_word) + value(&second_word) == value(&target_word)
    }
}

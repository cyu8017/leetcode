// LeetCode 0273 - Integer to English Words
// https://leetcode.com/problems/integer-to-english-words/

impl Solution {
    fn convert_chunk(value: i32, ones: &[&str], tens: &[&str]) -> String {
        if value == 0 {
            return String::new();
        }
        if value < 20 {
            return ones[value as usize].to_string();
        }
        if value < 100 {
            let tens_part = tens[(value / 10) as usize];
            let ones_part = ones[(value % 10) as usize];
            if ones_part.is_empty() {
                return tens_part.to_string();
            }
            return format!("{} {}", tens_part, ones_part);
        }
        let hundreds = ones[(value / 100) as usize];
        let remainder = Self::convert_chunk(value % 100, ones, tens);
        if remainder.is_empty() {
            format!("{} Hundred", hundreds)
        } else {
            format!("{} Hundred {}", hundreds, remainder)
        }
    }

    pub fn number_to_words(num: i32) -> String {
        let ones = [
            "", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
            "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen",
            "Seventeen", "Eighteen", "Nineteen",
        ];
        let tens = [
            "", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety",
        ];
        let thousands = ["", "Thousand", "Million", "Billion"];

        if num == 0 {
            return "Zero".to_string();
        }

        let mut parts = Vec::new();
        let mut value = num;
        let mut chunk_index = 0;
        while value > 0 {
            let chunk = value % 1000;
            if chunk != 0 {
                let mut chunk_words = Self::convert_chunk(chunk, &ones, &tens);
                if !thousands[chunk_index].is_empty() {
                    chunk_words.push(' ');
                    chunk_words.push_str(thousands[chunk_index]);
                }
                parts.push(chunk_words);
            }
            value /= 1000;
            chunk_index += 1;
        }
        parts.reverse();
        parts.join(" ")
    }
}

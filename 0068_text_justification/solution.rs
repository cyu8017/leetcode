// LeetCode 0068 - Text Justification
// https://leetcode.com/problems/text-justification/

impl Solution {
    pub fn full_justify(words: Vec<String>, max_width: i32) -> Vec<String> {
        let max_width = max_width as usize;
        let mut result = Vec::new();
        let mut i = 0;

        while i < words.len() {
            let mut line_words: Vec<&str> = Vec::new();
            let mut line_len = 0;

            while i < words.len() {
                let word = words[i].as_str();
                let extra = if line_words.is_empty() { 0 } else { 1 };
                if line_len + word.len() + extra > max_width {
                    break;
                }
                line_words.push(word);
                line_len += word.len() + extra;
                i += 1;
            }

            if i == words.len() || line_words.len() == 1 {
                let mut line = line_words.join(" ");
                line.push_str(&" ".repeat(max_width - line.len()));
                result.push(line);
            } else {
                let total_chars: usize = line_words.iter().map(|w| w.len()).sum();
                let total_spaces = max_width - total_chars;
                let gaps = line_words.len() - 1;
                let space = total_spaces / gaps;
                let remainder = total_spaces % gaps;
                let mut line = String::new();
                for (j, word) in line_words[..line_words.len() - 1].iter().enumerate() {
                    line.push_str(word);
                    let gap_spaces = space + if j < remainder { 1 } else { 0 };
                    line.push_str(&" ".repeat(gap_spaces));
                }
                line.push_str(line_words.last().unwrap());
                result.push(line);
            }
        }

        result
    }
}

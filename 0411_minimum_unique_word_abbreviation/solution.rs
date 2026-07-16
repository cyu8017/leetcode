// LeetCode 0411 - Minimum Unique Word Abbreviation
// https://leetcode.com/problems/minimum-unique-word-abbreviation/

impl Solution {
    pub fn min_abbreviation(target: String, dictionary: Vec<String>) -> String {
        let words: Vec<&str> = dictionary
            .iter()
            .filter(|word| word.len() == target.len())
            .map(|word| word.as_str())
            .collect();

        let mut best_len = target.len() + 1;
        let mut result = target.clone();

        fn matches(word: &str, abbr: &str) -> bool {
            let word_chars: Vec<char> = word.chars().collect();
            let abbr_chars: Vec<char> = abbr.chars().collect();
            let mut index = 0;
            let mut pointer = 0;

            while index < word_chars.len() && pointer < abbr_chars.len() {
                if abbr_chars[pointer].is_ascii_digit() {
                    if abbr_chars[pointer] == '0' {
                        return false;
                    }
                    let mut number = 0;
                    while pointer < abbr_chars.len() && abbr_chars[pointer].is_ascii_digit() {
                        number = number * 10 + abbr_chars[pointer].to_digit(10).unwrap() as usize;
                        pointer += 1;
                    }
                    index += number;
                } else {
                    if index >= word_chars.len() || word_chars[index] != abbr_chars[pointer] {
                        return false;
                    }
                    index += 1;
                    pointer += 1;
                }
            }

            index == word_chars.len() && pointer == abbr_chars.len()
        }

        let valid = |abbr: &str| -> bool {
            if !matches(&target, abbr) {
                return false;
            }
            !words.iter().any(|word| matches(word, abbr))
        };

        fn dfs(
            target: &str,
            valid: &dyn Fn(&str) -> bool,
            index: usize,
            parts: Vec<String>,
            skip: usize,
            best_len: &mut usize,
            result: &mut String,
        ) {
            if index == target.len() {
                let mut abbr = parts.join("");
                if skip > 0 {
                    abbr.push_str(&skip.to_string());
                }
                if valid(&abbr) {
                    if abbr.len() < *best_len
                        || (abbr.len() == *best_len && abbr < *result)
                    {
                        *best_len = abbr.len();
                        *result = abbr;
                    }
                }
                return;
            }

            dfs(target, valid, index + 1, parts.clone(), skip + 1, best_len, result);

            let mut new_parts = parts;
            if skip > 0 {
                new_parts.push(skip.to_string());
            }
            new_parts.push(target[index..=index].to_string());
            dfs(target, valid, index + 1, new_parts, 0, best_len, result);
        }

        dfs(&target, &valid, 0, Vec::new(), 0, &mut best_len, &mut result);
        result
    }
}

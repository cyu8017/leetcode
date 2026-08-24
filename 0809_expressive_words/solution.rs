// LeetCode 0809 - Expressive Words
// https://leetcode.com/problems/expressive-words/

impl Solution {
    pub fn expressive_words(s: String, words: Vec<String>) -> i32 {
        fn groups(text: &str) -> Vec<(char, i32)> {
            let chars: Vec<char> = text.chars().collect();
            let mut result = Vec::new();
            let mut i = 0;
            let n = chars.len();
            while i < n {
                let mut j = i;
                while j < n && chars[j] == chars[i] {
                    j += 1;
                }
                result.push((chars[i], (j - i) as i32));
                i = j;
            }
            result
        }

        let target = groups(&s);
        let mut ans = 0;
        for word in &words {
            let source = groups(word);
            if source.len() != target.len() {
                continue;
            }
            let mut ok = true;
            for i in 0..source.len() {
                if source[i].0 != target[i].0 {
                    ok = false;
                    break;
                }
                let (c1, c2) = (source[i].1, target[i].1);
                if c1 > c2 || (c1 != c2 && c2 < 3) {
                    ok = false;
                    break;
                }
            }
            if ok {
                ans += 1;
            }
        }
        ans
    }
}

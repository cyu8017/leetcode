// LeetCode 0604 - Design Compressed String Iterator
// https://leetcode.com/problems/design-compressed-string-iterator/

pub struct StringIterator {
    chars: Vec<char>,
    counts: Vec<i32>,
    index: usize,
}

impl StringIterator {
    pub fn new(compressed_string: String) -> Self {
        let chars_in: Vec<char> = compressed_string.chars().collect();
        let mut chars = Vec::new();
        let mut counts = Vec::new();
        let mut i = 0;
        while i < chars_in.len() {
            let ch = chars_in[i];
            i += 1;
            let j_start = i;
            while i < chars_in.len() && chars_in[i].is_ascii_digit() {
                i += 1;
            }
            let num: i32 = chars_in[j_start..i].iter().collect::<String>().parse().unwrap();
            chars.push(ch);
            counts.push(num);
        }
        Self {
            chars,
            counts,
            index: 0,
        }
    }

    pub fn next(&mut self) -> char {
        if !self.has_next() {
            return ' ';
        }
        let ch = self.chars[self.index];
        self.counts[self.index] -= 1;
        if self.counts[self.index] == 0 {
            self.index += 1;
        }
        ch
    }

    pub fn has_next(&self) -> bool {
        self.index < self.chars.len()
    }
}

// LeetCode 3037 - Find Pattern in Infinite Stream II
// https://leetcode.com/problems/find-pattern-in-infinite-stream-ii/

pub struct InfiniteStream {
    bits: Vec<i32>,
    i: usize,
}

impl InfiniteStream {
    pub fn new(bits: Vec<i32>) -> Self {
        Self { bits, i: 0 }
    }
    pub fn next(&mut self) -> i32 {
        let v = self.bits[self.i];
        self.i += 1;
        v
    }
}

impl Solution {
    pub fn find_pattern(stream: &mut InfiniteStream, pattern: Vec<i32>) -> i32 {
        fn get_lps(pattern: &[i32]) -> Vec<usize> {
            let n = pattern.len();
            let mut lps = vec![0; n];
            let mut j = 0;
            for i in 1..n {
                while j > 0 && pattern[j] != pattern[i] {
                    j = lps[j - 1];
                }
                if pattern[i] == pattern[j] {
                    j += 1;
                    lps[i] = j;
                }
            }
            lps
        }
        let lps = get_lps(&pattern);
        let mut i = 0i32;
        let mut j = 0usize;
        let mut bit = 0;
        let mut read_next = false;
        loop {
            if !read_next {
                bit = stream.next();
                read_next = true;
            }
            if bit == pattern[j] {
                i += 1;
                read_next = false;
                j += 1;
                if j == pattern.len() {
                    return i - j as i32;
                }
            } else if j > 0 {
                j = lps[j - 1];
            } else {
                i += 1;
                read_next = false;
            }
        }
    }
}

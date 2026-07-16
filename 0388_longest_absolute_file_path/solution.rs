// LeetCode 0388 - Longest Absolute File Path
// https://leetcode.com/problems/longest-absolute-file-path/

impl Solution {
    pub fn length_longest_path(input: String) -> i32 {
        let mut stack: Vec<i32> = Vec::new();
        let mut max_length = 0;

        for line in input.split('\n') {
            let depth = line.chars().take_while(|&ch| ch == '\t').count();
            let name = &line[depth..];

            while stack.len() > depth {
                stack.pop();
            }

            if name.contains('.') {
                let prefix = stack.last().copied().unwrap_or(0);
                max_length = max_length.max(prefix + name.len() as i32);
            } else {
                let prefix = stack.last().copied().unwrap_or(0);
                stack.push(prefix + name.len() as i32 + 1);
            }
        }

        max_length
    }
}

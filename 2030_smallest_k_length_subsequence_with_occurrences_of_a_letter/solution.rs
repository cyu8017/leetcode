// LeetCode 2030 - Smallest K-Length Subsequence With Occurrences of a Letter
// https://leetcode.com/problems/smallest-k-length-subsequence-with-occurrences-of-a-letter/

impl Solution {
    pub fn smallest_subsequence(s: String, k: i32, letter: char, repetition: i32) -> String {
        let bytes = s.as_bytes();
        let n = bytes.len();
        let letter = letter as u8;
        let mut remain_letter = bytes.iter().filter(|&&c| c == letter).count() as i32;
        let mut stack = Vec::new();
        let mut in_stack_letter = 0;
        for i in 0..n {
            let ch = bytes[i];
            while !stack.is_empty()
                && ch < *stack.last().unwrap()
                && stack.len() as i32 + (n - i) as i32 > k
            {
                let top = *stack.last().unwrap();
                if top == letter {
                    if in_stack_letter + remain_letter - 1 < repetition {
                        break;
                    }
                    in_stack_letter -= 1;
                }
                stack.pop();
            }
            if (stack.len() as i32) < k {
                if ch == letter {
                    stack.push(ch);
                    in_stack_letter += 1;
                } else if k - stack.len() as i32 > repetition - in_stack_letter {
                    stack.push(ch);
                }
            }
            if ch == letter {
                remain_letter -= 1;
            }
        }
        String::from_utf8(stack).unwrap()
    }
}

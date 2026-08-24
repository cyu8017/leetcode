// LeetCode 0556 - Next Greater Element III
// https://leetcode.com/problems/next-greater-element-iii/

impl Solution {
    pub fn next_greater_element(n: i32) -> i32 {
        let mut digits: Vec<char> = n.to_string().chars().collect();
        let mut i = digits.len() as i32 - 2;
        while i >= 0 && digits[i as usize] >= digits[i as usize + 1] {
            i -= 1;
        }
        if i < 0 {
            return -1;
        }
        let mut j = digits.len() as i32 - 1;
        while digits[j as usize] <= digits[i as usize] {
            j -= 1;
        }
        digits.swap(i as usize, j as usize);
        digits[(i as usize + 1)..].reverse();
        let mut value: i64 = 0;
        for ch in digits {
            value = value * 10 + (ch as i64 - '0' as i64);
        }
        if value > i32::MAX as i64 {
            -1
        } else {
            value as i32
        }
    }
}

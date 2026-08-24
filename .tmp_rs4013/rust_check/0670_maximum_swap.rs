struct Solution;
// LeetCode 0670 - Maximum Swap
// https://leetcode.com/problems/maximum-swap/

impl Solution {
    pub fn maximum_swap(num: i32) -> i32 {
        let mut digits: Vec<u8> = num.to_string().into_bytes();
        let mut last = [-1i32; 10];
        for (i, &d) in digits.iter().enumerate() {
            last[(d - b'0') as usize] = i as i32;
        }
        for i in 0..digits.len() {
            let cur = (digits[i] - b'0') as i32;
            for candidate in (cur + 1..=9).rev() {
                if last[candidate as usize] > i as i32 {
                    let j = last[candidate as usize] as usize;
                    digits.swap(i, j);
                    return String::from_utf8(digits).unwrap().parse().unwrap();
                }
            }
        }
        num
    }
}

fn main() {}

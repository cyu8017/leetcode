// LeetCode 0744 - Find Smallest Letter Greater Than Target
// https://leetcode.com/problems/find-smallest-letter-greater-than-target/

impl Solution {
    pub fn next_greatest_letter(letters: Vec<char>, target: char) -> char {
        let mut left = 0i32;
        let mut right = letters.len() as i32;
        while left < right {
            let mid = left + (right - left) / 2;
            if letters[mid as usize] <= target {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        letters[left as usize % letters.len()]
    }
}

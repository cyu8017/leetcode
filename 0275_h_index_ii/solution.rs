// LeetCode 0275 - H-Index II
// https://leetcode.com/problems/h-index-ii/

impl Solution {
    pub fn h_index(citations: Vec<i32>) -> i32 {
        let mut left = 0isize;
        let mut right = citations.len() as isize - 1;
        let length = citations.len() as i32;
        while left <= right {
            let mid = left + (right - left) / 2;
            let papers = length - mid as i32;
            if citations[mid as usize] >= papers {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        length - left as i32
    }
}

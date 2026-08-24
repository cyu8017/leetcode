// LeetCode 0927 - Three Equal Parts
// https://leetcode.com/problems/three-equal-parts/

impl Solution {
    pub fn three_equal_parts(arr: Vec<i32>) -> Vec<i32> {
        let ones: Vec<i32> = arr
            .iter()
            .enumerate()
            .filter(|(_, &v)| v != 0)
            .map(|(i, _)| i as i32)
            .collect();
        let n = ones.len();
        if n % 3 != 0 {
            return vec![-1, -1];
        }
        if n == 0 {
            return vec![0, arr.len() as i32 - 1];
        }
        let third = n / 3;
        let length = ones[n - 1] - ones[2 * third] + 1;
        let a = ones[0];
        let b = ones[third];
        let c = ones[2 * third];
        if a + length > arr.len() as i32
            || b + length > arr.len() as i32
            || c + length > arr.len() as i32
        {
            return vec![-1, -1];
        }
        for i in 0..length {
            if arr[(a + i) as usize] != arr[(b + i) as usize]
                || arr[(a + i) as usize] != arr[(c + i) as usize]
            {
                return vec![-1, -1];
            }
        }
        vec![a + length - 1, b + length]
    }
}

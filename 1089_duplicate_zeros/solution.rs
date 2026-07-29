// LeetCode 1089 - Duplicate Zeros
// https://leetcode.com/problems/duplicate-zeros/

impl Solution {
    pub fn duplicate_zeros(arr: &mut Vec<i32>) {
        let mut zeros = arr.iter().filter(|&&x| x == 0).count() as i32;
        let n = arr.len() as i32;
        for i in (0..n).rev() {
            if i + zeros < n {
                arr[(i + zeros) as usize] = arr[i as usize];
            }
            if arr[i as usize] == 0 {
                zeros -= 1;
                if i + zeros < n {
                    arr[(i + zeros) as usize] = 0;
                }
            }
        }
    }
}

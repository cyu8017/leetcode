// LeetCode 0989 - Add to Array-Form of Integer
// https://leetcode.com/problems/add-to-array-form-of-integer/

impl Solution {
    pub fn add_to_array_form(mut num: Vec<i32>, mut k: i32) -> Vec<i32> {
        let mut i = num.len() as i32 - 1;
        while k > 0 || i >= 0 {
            if i >= 0 {
                k += num[i as usize];
                num[i as usize] = k % 10;
                i -= 1;
            } else {
                num.insert(0, k % 10);
            }
            k /= 10;
        }
        num
    }
}

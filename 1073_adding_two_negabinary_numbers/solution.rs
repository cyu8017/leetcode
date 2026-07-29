// LeetCode 1073 - Adding Two Negabinary Numbers
// https://leetcode.com/problems/adding-two-negabinary-numbers/

impl Solution {
    pub fn add_negabinary(arr1: Vec<i32>, arr2: Vec<i32>) -> Vec<i32> {
        let mut i = arr1.len() as i32 - 1;
        let mut j = arr2.len() as i32 - 1;
        let mut carry = 0i32;
        let mut ans = Vec::new();
        while i >= 0 || j >= 0 || carry != 0 {
            let mut total = carry;
            if i >= 0 {
                total += arr1[i as usize];
                i -= 1;
            }
            if j >= 0 {
                total += arr2[j as usize];
                j -= 1;
            }
            ans.push(total & 1);
            carry = -(total >> 1);
        }
        while ans.len() > 1 && *ans.last().unwrap() == 0 {
            ans.pop();
        }
        ans.reverse();
        ans
    }
}

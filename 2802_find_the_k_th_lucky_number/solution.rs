// LeetCode 2802 - Find The K-th Lucky Number
// https://leetcode.com/problems/find-the-k-th-lucky-number/

impl Solution {
    pub fn kth_lucky_number(mut k: i32) -> String {
        k += 1;
        let mut bits = String::new();
        while k > 1 {
            if k % 2 == 0 {
                bits.insert(0, '4');
            } else {
                bits.insert(0, '7');
            }
            k /= 2;
        }
        bits
    }
}

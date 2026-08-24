// LeetCode 3697 - Compute Decimal Representation
// https://leetcode.com/problems/compute-decimal-representation/

impl Solution {
    pub fn decimal_representation(mut n: i32) -> Vec<i32> {
        let mut ans = Vec::new();
        let mut p: i64 = 1;
        while n > 0 {
            let v = n % 10;
            n /= 10;
            if v != 0 {
                ans.push((p * v as i64) as i32);
            }
            p *= 10;
        }
        ans.reverse();
        ans
    }
}

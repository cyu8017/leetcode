// LeetCode 0264 - Ugly Number II
// https://leetcode.com/problems/ugly-number-ii/

impl Solution {
    pub fn nth_ugly_number(n: i32) -> i32 {
        let n = n as usize;
        let mut ugly = vec![1];
        let mut index2 = 0;
        let mut index3 = 0;
        let mut index5 = 0;
        while ugly.len() < n {
            let next_ugly = ugly[index2] * 2
                .min(ugly[index3] * 3)
                .min(ugly[index5] * 5);
            ugly.push(next_ugly);
            if next_ugly == ugly[index2] * 2 {
                index2 += 1;
            }
            if next_ugly == ugly[index3] * 3 {
                index3 += 1;
            }
            if next_ugly == ugly[index5] * 5 {
                index5 += 1;
            }
        }
        ugly[n - 1]
    }
}

// LeetCode 1646 - Get Maximum in Generated Array
// https://leetcode.com/problems/get-maximum-in-generated-array/

impl Solution {
    pub fn get_maximum_generated(n: i32) -> i32 {
        if n < 2 {
            return n;
        }
        let n = n as usize;
        let mut a = vec![0; n + 1];
        a[1] = 1;
        let mut ans = 1;
        for i in 2..=n {
            a[i] = if i % 2 == 0 {
                a[i / 2]
            } else {
                a[i / 2] + a[i / 2 + 1]
            };
            ans = ans.max(a[i]);
        }
        ans
    }
}

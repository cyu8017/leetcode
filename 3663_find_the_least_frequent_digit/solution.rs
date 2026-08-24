// LeetCode 3663 - Find The Least Frequent Digit
// https://leetcode.com/problems/find-the-least-frequent-digit/

impl Solution {
    pub fn get_least_frequent_digit(mut n: i32) -> i32 {
        let mut cnt = [0i32; 10];
        let mut ans = 0;
        let mut f = 1 << 30;
        while n > 0 {
            cnt[(n % 10) as usize] += 1;
            n /= 10;
        }
        for x in 0..10 {
            if cnt[x] > 0 && cnt[x] < f {
                f = cnt[x];
                ans = x as i32;
            }
        }
        ans
    }
}

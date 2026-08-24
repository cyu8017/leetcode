// LeetCode 0949 - Largest Time for Given Digits
// https://leetcode.com/problems/largest-time-for-given-digits/

impl Solution {
    pub fn largest_time_from_digits(mut arr: Vec<i32>) -> String {
        arr.sort_unstable();
        let mut best = String::new();
        fn next_perm(a: &mut [i32]) -> bool {
            let n = a.len();
            let mut i = n - 1;
            while i > 0 && a[i - 1] >= a[i] {
                i -= 1;
            }
            if i == 0 {
                return false;
            }
            let mut j = n - 1;
            while a[j] <= a[i - 1] {
                j -= 1;
            }
            a.swap(i - 1, j);
            a[i..].reverse();
            true
        }
        loop {
            let hours = 10 * arr[0] + arr[1];
            let minutes = 10 * arr[2] + arr[3];
            if hours < 24 && minutes < 60 {
                let cand = format!("{:02}:{:02}", hours, minutes);
                if cand > best {
                    best = cand;
                }
            }
            if !next_perm(&mut arr) {
                break;
            }
        }
        best
    }
}

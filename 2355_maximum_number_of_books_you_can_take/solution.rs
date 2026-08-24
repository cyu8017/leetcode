// LeetCode 2355 - Maximum Number of Books You Can Take
// https://leetcode.com/problems/maximum-number-of-books-you-can-take/

impl Solution {
    pub fn maximum_books(books: Vec<i32>) -> i64 {
        let n = books.len();
        let mut dp = vec![0i64; n];
        let mut stack: Vec<usize> = Vec::new();
        let mut ans = 0i64;
        let sum = |l: i32, r: i32, h: i32| -> i64 {
            let width = r - l + 1;
            if h >= width {
                width as i64 * (2 * h as i64 - width as i64 + 1) / 2
            } else {
                h as i64 * (h as i64 + 1) / 2
            }
        };
        for i in 0..n {
            while !stack.is_empty() {
                let j = *stack.last().unwrap();
                if books[j] >= books[i] - (i as i32 - j as i32) {
                    stack.pop();
                } else {
                    break;
                }
            }
            if stack.is_empty() {
                dp[i] = sum(0, i as i32, books[i]);
            } else {
                let j = *stack.last().unwrap();
                dp[i] = dp[j] + sum(j as i32 + 1, i as i32, books[i]);
            }
            ans = ans.max(dp[i]);
            stack.push(i);
        }
        ans
    }
}

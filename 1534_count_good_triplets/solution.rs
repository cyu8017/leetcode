// LeetCode 1534 - Count Good Triplets
// https://leetcode.com/problems/count-good-triplets/

impl Solution {
    pub fn count_good_triplets(arr: Vec<i32>, a: i32, b: i32, c: i32) -> i32 {
        let mut ans = 0;
        let n = arr.len();
        for i in 0..n {
            for j in i + 1..n {
                if (arr[i] - arr[j]).abs() > a {
                    continue;
                }
                for k in j + 1..n {
                    if (arr[j] - arr[k]).abs() <= b && (arr[i] - arr[k]).abs() <= c {
                        ans += 1;
                    }
                }
            }
        }
        ans
    }
}

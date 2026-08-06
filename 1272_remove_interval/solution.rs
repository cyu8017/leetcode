// LeetCode 1272 - Remove Interval
// https://leetcode.com/problems/remove-interval/

impl Solution {
    pub fn remove_interval(intervals: Vec<Vec<i32>>, to_be_removed: Vec<i32>) -> Vec<Vec<i32>> {
        let (left, right) = (to_be_removed[0], to_be_removed[1]);
        let mut ans = Vec::new();
        for iv in intervals {
            let (start, end) = (iv[0], iv[1]);
            if end <= left || start >= right {
                ans.push(vec![start, end]);
            } else {
                if start < left {
                    ans.push(vec![start, left]);
                }
                if end > right {
                    ans.push(vec![right, end]);
                }
            }
        }
        ans
    }
}

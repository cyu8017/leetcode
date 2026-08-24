// LeetCode 2345 - Finding the Number of Visible Mountains
// https://leetcode.com/problems/finding-the-number-of-visible-mountains/

impl Solution {
    pub fn visible_mountains(peaks: Vec<Vec<i32>>) -> i32 {
        let mut arr: Vec<(i32, i32)> = peaks.iter().map(|p| (p[0] - p[1], p[0] + p[1])).collect();
        arr.sort_by(|a, b| {
            if a.0 == b.0 {
                b.1.cmp(&a.1)
            } else {
                a.0.cmp(&b.0)
            }
        });
        let mut ans = 0;
        let mut max_r = i32::MIN;
        let mut i = 0;
        while i < arr.len() {
            let mut j = i;
            while j < arr.len() && arr[j].0 == arr[i].0 && arr[j].1 == arr[i].1 {
                j += 1;
            }
            if arr[i].1 > max_r {
                if j - i == 1 {
                    ans += 1;
                }
                max_r = arr[i].1;
            }
            i = j;
        }
        ans
    }
}

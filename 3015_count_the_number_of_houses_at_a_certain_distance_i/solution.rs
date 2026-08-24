// LeetCode 3015 - Count the Number of Houses at a Certain Distance I
// https://leetcode.com/problems/count-the-number-of-houses-at-a-certain-distance-i/

impl Solution {
    pub fn count_of_pairs(n: i32, x: i32, y: i32) -> Vec<i32> {
        let n = n as usize;
        let mut ans = vec![0; n];
        let x = x as i32 - 1;
        let y = y as i32 - 1;
        for i in 0..n as i32 {
            for j in (i + 1)..n as i32 {
                let a = j - i;
                let b = (x - i).abs() + (y - j).abs() + 1;
                let c = (x - j).abs() + (y - i).abs() + 1;
                let d = a.min(b).min(c);
                ans[(d - 1) as usize] += 2;
            }
        }
        ans
    }
}

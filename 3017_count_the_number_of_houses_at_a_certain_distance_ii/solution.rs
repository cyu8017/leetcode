// LeetCode 3017 - Count the Number of Houses at a Certain Distance II
// https://leetcode.com/problems/count-the-number-of-houses-at-a-certain-distance-ii/

impl Solution {
    pub fn count_of_pairs(n: i32, mut x: i32, mut y: i32) -> Vec<i64> {
        if x > y {
            std::mem::swap(&mut x, &mut y);
        }
        let nu = n as usize;
        let mut a = vec![0i64; nu];
        for i in 1..=n {
            a[0] += 2;
            let i64i = i as i64;
            a[((i64i - 1).min((i - y).abs() as i64 + x as i64)) as usize] -= 1;
            a[((n as i64 - i64i).min((i - x).abs() as i64 + 1 + (n as i64 - y as i64))) as usize] -= 1;
            a[(((i - x).abs() as i64).min((y - i).abs() as i64 + 1)) as usize] += 1;
            a[(((i - x).abs() as i64 + 1).min((y - i).abs() as i64)) as usize] += 1;
            let r = (x - i).max(0) as i64 + (i - y).max(0) as i64;
            a[(r + (y - x) as i64 / 2) as usize] -= 1;
            a[(r + (y - x + 1) as i64 / 2) as usize] -= 1;
        }
        for i in 1..nu {
            a[i] += a[i - 1];
        }
        a
    }
}

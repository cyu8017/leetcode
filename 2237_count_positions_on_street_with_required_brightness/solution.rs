// LeetCode 2237 - Count Positions on Street With Required Brightness
// https://leetcode.com/problems/count-positions-on-street-with-required-brightness/

impl Solution {
    pub fn meet_requirement(n: i32, lights: Vec<Vec<i32>>, requirement: Vec<i32>) -> i32 {
        let n = n as usize;
        let mut diff = vec![0i32; n + 1];
        for light in lights {
            let pos = light[0];
            let r = light[1];
            let l = 0.max(pos - r) as usize;
            let rr = ((n as i32 - 1).min(pos + r)) as usize;
            diff[l] += 1;
            diff[rr + 1] -= 1;
        }
        let mut ans = 0;
        let mut cur = 0;
        for i in 0..n {
            cur += diff[i];
            if cur >= requirement[i] {
                ans += 1;
            }
        }
        ans
    }
}

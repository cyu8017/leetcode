struct Solution;
// LeetCode 3964 - Minimum Lights To Illuminate A Road
// https://leetcode.com/problems/minimum-lights-to-illuminate-a-road/

impl Solution {
    pub fn min_lights(lights: Vec<i32>) -> i32 {
        let n = lights.len();
        let mut d = vec![0; n];
        for i in 0..n {
            let v = lights[i];
            if v > 0 {
                let l = 0.max(i as i32 - v) as usize;
                let r = (n as i32 - 1).min(i as i32 + v) as usize;
                d[l] += 1;
                if r + 1 < n {
                    d[r + 1] -= 1;
                }
            }
        }
        let mut s = 0;
        let mut cnt = 0;
        let mut ans = 0;
        for x in d {
            s += x;
            if s == 0 {
                cnt += 1;
            } else {
                ans += (cnt + 2) / 3;
                cnt = 0;
            }
        }
        ans += (cnt + 2) / 3;
        ans
    }
}

fn main() {}

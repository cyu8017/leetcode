struct Solution;
// LeetCode 3443 - Maximum Manhattan Distance After K Changes
// https://leetcode.com/problems/maximum-manhattan-distance-after-k-changes/

impl Solution {
    pub fn max_distance(s: String, k: i32) -> i32 {
        let mut ans = 0;
        let mut lat: i32 = 0;
        let mut lon: i32 = 0;
        for (i, c) in s.bytes().enumerate() {
            match c {
                b'N' => lat += 1,
                b'S' => lat -= 1,
                b'E' => lon += 1,
                _ => lon -= 1,
            }
            let md = lat.abs() + lon.abs();
            let steps = i as i32 + 1;
            let mut cur = md + 2 * k;
            if cur > steps {
                cur = steps;
            }
            if cur > ans {
                ans = cur;
            }
        }
        ans
    }
}

fn main() {}

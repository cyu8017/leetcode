// LeetCode 2021 - Brightest Position on Street
// https://leetcode.com/problems/brightest-position-on-street/

impl Solution {
    pub fn brightest_position(lights: Vec<Vec<i32>>) -> i32 {
        let mut events = Vec::new();
        for light in lights {
            let pos = light[0];
            let r = light[1];
            events.push((pos - r, 1));
            events.push((pos + r + 1, -1));
        }
        events.sort_by(|a, b| a.0.cmp(&b.0).then(b.1.cmp(&a.1)));
        let mut best = 0;
        let mut cur = 0;
        let mut ans = 0;
        for (x, d) in events {
            cur += d;
            if cur > best {
                best = cur;
                ans = x;
            }
        }
        ans
    }
}

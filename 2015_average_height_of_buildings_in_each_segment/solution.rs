// LeetCode 2015 - Average Height of Buildings in Each Segment
// https://leetcode.com/problems/average-height-of-buildings-in-each-segment/

impl Solution {
    pub fn average_height_of_buildings(buildings: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let mut events = Vec::new();
        for b in &buildings {
            events.push((b[0], 1, b[2]));
            events.push((b[1], -1, b[2]));
        }
        events.sort_by(|a, b| a.0.cmp(&b.0).then(a.1.cmp(&b.1)));
        let mut ans = Vec::new();
        let mut count = 0;
        let mut sum = 0;
        let mut prev = events[0].0;
        for &(x, d, h) in &events {
            if x != prev && count > 0 {
                let avg = sum / count;
                if let Some(last) = ans.last_mut() {
                    if last[1] == prev && last[2] == avg {
                        last[1] = x;
                    } else {
                        ans.push(vec![prev, x, avg]);
                    }
                } else {
                    ans.push(vec![prev, x, avg]);
                }
            }
            count += d;
            sum += d * h;
            prev = x;
        }
        ans
    }
}

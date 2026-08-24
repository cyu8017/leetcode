// LeetCode 0850 - Rectangle Area II
// https://leetcode.com/problems/rectangle-area-ii/

impl Solution {
    pub fn rectangle_area(rectangles: Vec<Vec<i32>>) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let mut events = Vec::new();
        for r in &rectangles {
            events.push((r[0], 1i32, r[1], r[3]));
            events.push((r[2], -1i32, r[1], r[3]));
        }
        events.sort_unstable();

        fn covered_length(mut active: Vec<(i32, i32)>) -> i64 {
            if active.is_empty() {
                return 0;
            }
            active.sort_unstable();
            let mut total = 0i64;
            let mut cur_start = active[0].0;
            let mut cur_end = active[0].1;
            for &(start, end) in active.iter().skip(1) {
                if start > cur_end {
                    total += (cur_end - cur_start) as i64;
                    cur_start = start;
                    cur_end = end;
                } else {
                    cur_end = cur_end.max(end);
                }
            }
            total += (cur_end - cur_start) as i64;
            total
        }

        let mut active = Vec::new();
        let mut area = 0i64;
        let mut prev_x = events[0].0;
        for (x, typ, y1, y2) in events {
            area += covered_length(active.clone()) * (x - prev_x) as i64;
            if typ == 1 {
                active.push((y1, y2));
            } else if let Some(pos) = active.iter().position(|&p| p == (y1, y2)) {
                active.remove(pos);
            }
            prev_x = x;
        }
        (area % MOD) as i32
    }
}

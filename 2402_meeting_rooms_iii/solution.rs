// LeetCode 2402 - Meeting Rooms III
// https://leetcode.com/problems/meeting-rooms-iii/

use std::collections::BinaryHeap;
use std::cmp::Reverse;

impl Solution {
    pub fn most_booked(n: i32, mut meetings: Vec<Vec<i32>>) -> i32 {
        let n = n as usize;
        meetings.sort_by_key(|m| m[0]);
        let mut free = BinaryHeap::new();
        for i in 0..n {
            free.push(Reverse(i as i64));
        }
        let mut busy: BinaryHeap<Reverse<(i64, i64)>> = BinaryHeap::new();
        let mut cnt = vec![0i32; n];
        for m in meetings {
            let start = m[0] as i64;
            let end = m[1] as i64;
            while let Some(&Reverse((t, room))) = busy.peek() {
                if t <= start {
                    busy.pop();
                    free.push(Reverse(room));
                } else {
                    break;
                }
            }
            let dur = end - start;
            let (room, begin) = if let Some(Reverse(room)) = free.pop() {
                (room, start)
            } else {
                let Reverse((t, room)) = busy.pop().unwrap();
                (room, t)
            };
            busy.push(Reverse((begin + dur, room)));
            cnt[room as usize] += 1;
        }
        let mut ans = 0;
        for i in 1..n {
            if cnt[i] > cnt[ans] {
                ans = i;
            }
        }
        ans as i32
    }
}

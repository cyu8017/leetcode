// LeetCode 3672 - Sum of Weighted Modes in Subarrays
// https://leetcode.com/problems/sum-of-weighted-modes-in-subarrays/

use std::collections::{BinaryHeap, HashMap};

impl Solution {
    pub fn mode_weight(nums: Vec<i32>, k: i32) -> i64 {
        let k = k as usize;
        let mut cnt: HashMap<i32, i32> = HashMap::new();
        let mut pq: BinaryHeap<(i32, i32)> = BinaryHeap::new();
        for i in 0..k {
            let x = nums[i];
            *cnt.entry(x).or_insert(0) += 1;
            pq.push((cnt[&x], -x));
        }
        let get_mode = |cnt: &HashMap<i32, i32>, pq: &mut BinaryHeap<(i32, i32)>| -> i64 {
            loop {
                let (freq, neg_val) = *pq.peek().unwrap();
                let val = -neg_val;
                if cnt[&val] == freq {
                    return freq as i64 * val as i64;
                }
                pq.pop();
            }
        };
        let mut ans = get_mode(&cnt, &mut pq);
        for i in k..nums.len() {
            let x = nums[i];
            let y = nums[i - k];
            *cnt.entry(x).or_insert(0) += 1;
            *cnt.entry(y).or_insert(0) -= 1;
            pq.push((cnt[&x], -x));
            pq.push((cnt[&y], -y));
            ans += get_mode(&cnt, &mut pq);
        }
        ans
    }
}

// LeetCode 0683 - K Empty Slots
// https://leetcode.com/problems/k-empty-slots/

impl Solution {
    pub fn k_empty_slots(bulbs: Vec<i32>, k: i32) -> i32 {
        let n = bulbs.len();
        let mut days = vec![0; n];
        for (day, bulb) in bulbs.into_iter().enumerate() {
            days[bulb as usize - 1] = (day + 1) as i32;
        }

        let k = k as usize;
        let mut ans = i32::MAX;
        let mut i = 0;
        while i + k + 1 < n {
            let left = i;
            let right = i + k + 1;
            let mut j = left + 1;
            while j < right && days[j] > days[left] && days[j] > days[right] {
                j += 1;
            }
            if j == right {
                ans = ans.min(days[left].max(days[right]));
                i += 1;
            } else {
                i = j;
            }
        }
        if ans == i32::MAX {
            -1
        } else {
            ans
        }
    }
}

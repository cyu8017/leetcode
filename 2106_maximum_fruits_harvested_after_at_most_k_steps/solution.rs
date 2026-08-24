// LeetCode 2106 - Maximum Fruits Harvested After at Most K Steps
// https://leetcode.com/problems/maximum-fruits-harvested-after-at-most-k-steps/

impl Solution {
    fn min_steps(left: i32, right: i32, start: i32) -> i32 {
        if right <= start {
            return start - left;
        }
        if left >= start {
            return right - start;
        }
        ((start - left) + (right - left)).min((right - start) + (right - left))
    }

    pub fn max_total_fruits(fruits: Vec<Vec<i32>>, start_pos: i32, k: i32) -> i32 {
        let n = fruits.len();
        let mut pref = vec![0i32; n + 1];
        let mut pos = vec![0i32; n];
        for i in 0..n {
            pos[i] = fruits[i][0];
            pref[i + 1] = pref[i] + fruits[i][1];
        }
        let mut ans = 0;
        let mut j = 0;
        for i in 0..n {
            while j < n && Self::min_steps(pos[i], pos[j], start_pos) > k {
                j += 1;
            }
            if j <= i {
                ans = ans.max(pref[i + 1] - pref[j]);
            }
        }
        j = 0;
        for i in 0..n {
            while j <= i && Self::min_steps(pos[j], pos[i], start_pos) > k {
                j += 1;
            }
            ans = ans.max(pref[i + 1] - pref[j]);
        }
        ans
    }
}

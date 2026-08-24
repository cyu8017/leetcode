struct Solution;
// LeetCode 3892 - Minimum Operations to Achieve At Least K Peaks
// https://leetcode.com/problems/minimum-operations-to-achieve-at-least-k-peaks/

impl Solution {
    pub fn min_operations(nums: Vec<i32>, k: i32) -> i64 {
        let n = nums.len();
        if k == 0 {
            return 0;
        }
        if k > n as i32 / 2 {
            return -1;
        }
        let mut cost = vec![0i64; n];
        for i in 0..n {
            let left = nums[(i + n - 1) % n];
            let right = nums[(i + 1) % n];
            let need = left.max(right);
            if need >= nums[i] {
                cost[i] = need as i64 - nums[i] as i64 + 1;
            }
        }
        const INF: i64 = 1i64 << 60;
        let line = |left: i32, right: i32, choose: i32| -> i64 {
            if choose == 0 {
                return 0;
            }
            if left > right || choose > (right - left + 2) / 2 {
                return INF;
            }
            let choose = choose as usize;
            let mut prev2 = vec![INF; choose + 1];
            let mut prev1 = vec![INF; choose + 1];
            prev2[0] = 0;
            prev1[0] = 0;
            for i in left..=right {
                let mut current = prev1.clone();
                for j in 1..=choose {
                    if prev2[j - 1] != INF && prev2[j - 1] + cost[i as usize] < current[j] {
                        current[j] = prev2[j - 1] + cost[i as usize];
                    }
                }
                prev2 = prev1;
                prev1 = current;
            }
            prev1[choose]
        };
        let mut answer = line(1, n as i32 - 1, k);
        let mut with_first = line(2, n as i32 - 2, k - 1);
        if with_first != INF {
            with_first += cost[0];
            answer = answer.min(with_first);
        }
        if answer == INF {
            -1
        } else {
            answer
        }
    }
}

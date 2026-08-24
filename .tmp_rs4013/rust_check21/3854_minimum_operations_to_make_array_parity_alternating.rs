struct Solution;
// LeetCode 3854 - Minimum Operations to Make Array Parity Alternating
// https://leetcode.com/problems/minimum-operations-to-make-array-parity-alternating/

impl Solution {
    pub fn make_parity_alternating(nums: Vec<i32>) -> Vec<i32> {
        if nums.len() == 1 {
            return vec![0, 0];
        }
        let mn = *nums.iter().min().unwrap();
        let mx = *nums.iter().max().unwrap();
        let f = |k: i32| {
            let mut cnt = 0;
            let mut a = i32::MAX;
            let mut b = i32::MIN;
            for (i, &orig) in nums.iter().enumerate() {
                let mut x = orig;
                if ((x - i as i32) & 1) != k {
                    cnt += 1;
                    if x == mn {
                        x += 1;
                    } else if x == mx {
                        x -= 1;
                    }
                }
                a = a.min(x);
                b = b.max(x);
            }
            vec![cnt, 1.max(b - a)]
        };
        let r0 = f(0);
        let r1 = f(1);
        if r0[0] != r1[0] {
            if r0[0] < r1[0] {
                r0
            } else {
                r1
            }
        } else if r0[1] <= r1[1] {
            r0
        } else {
            r1
        }
    }
}

// LeetCode 3943 - Number of Pairs After Increment
// https://leetcode.com/problems/number-of-pairs-after-increment/

use std::collections::HashMap;

impl Solution {
    pub fn number_of_pairs(nums1: Vec<i32>, mut nums2: Vec<i32>, queries: Vec<Vec<i32>>) -> Vec<i64> {
        const BLOCK_SIZE: usize = 225;
        let n = nums2.len();
        let blocks = (n + BLOCK_SIZE - 1) / BLOCK_SIZE;
        let mut lazy = vec![0i32; blocks];
        let mut freq = vec![HashMap::<i32, i32>::new(); blocks];
        let rebuild = |freq: &mut [HashMap<i32, i32>], nums2: &[i32], b: usize| {
            freq[b].clear();
            let end = ((b + 1) * BLOCK_SIZE).min(n);
            for i in (b * BLOCK_SIZE)..end {
                *freq[b].entry(nums2[i]).or_insert(0) += 1;
            }
        };
        let push = |lazy: &mut [i32], nums2: &mut [i32], b: usize| {
            if lazy[b] != 0 {
                let end = ((b + 1) * BLOCK_SIZE).min(n);
                for i in (b * BLOCK_SIZE)..end {
                    nums2[i] += lazy[b];
                }
                lazy[b] = 0;
            }
        };
        for b in 0..blocks {
            rebuild(&mut freq, &nums2, b);
        }
        let mut fixed: HashMap<i32, i32> = HashMap::new();
        for x in nums1 {
            *fixed.entry(x).or_insert(0) += 1;
        }
        let mut answer = Vec::new();
        for q in queries {
            if q[0] == 1 {
                let l = q[1] as usize;
                let r = q[2] as usize;
                let delta = q[3];
                let first = l / BLOCK_SIZE;
                let last = r / BLOCK_SIZE;
                if first == last {
                    push(&mut lazy, &mut nums2, first);
                    for i in l..=r {
                        nums2[i] += delta;
                    }
                    rebuild(&mut freq, &nums2, first);
                    continue;
                }
                push(&mut lazy, &mut nums2, first);
                for i in l..((first + 1) * BLOCK_SIZE) {
                    nums2[i] += delta;
                }
                rebuild(&mut freq, &nums2, first);
                push(&mut lazy, &mut nums2, last);
                for i in (last * BLOCK_SIZE)..=r {
                    nums2[i] += delta;
                }
                rebuild(&mut freq, &nums2, last);
                for b in (first + 1)..last {
                    lazy[b] += delta;
                }
            } else {
                let mut total = 0i64;
                for (&a, &count_a) in &fixed {
                    let target = q[1] - a;
                    for b in 0..blocks {
                        if let Some(&cnt) = freq[b].get(&(target - lazy[b])) {
                            total += count_a as i64 * cnt as i64;
                        }
                    }
                }
                answer.push(total);
            }
        }
        answer
    }
}

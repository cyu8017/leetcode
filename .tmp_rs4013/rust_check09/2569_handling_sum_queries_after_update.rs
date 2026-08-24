struct Solution;

// LeetCode 2569 - Handling Sum Queries After Update
// https://leetcode.com/problems/handling-sum-queries-after-update/

impl Solution {
    pub fn handle_query(nums1: Vec<i32>, nums2: Vec<i32>, queries: Vec<Vec<i32>>) -> Vec<i64> {
        let n = nums1.len();
        let mut ones = vec![0; 4 * n];
        let mut lazy = vec![false; 4 * n];
        fn build(idx: usize, l: usize, r: usize, nums1: &[i32], ones: &mut [i32]) {
            if l == r {
                ones[idx] = nums1[l];
                return;
            }
            let m = (l + r) / 2;
            build(idx * 2, l, m, nums1, ones);
            build(idx * 2 + 1, m + 1, r, nums1, ones);
            ones[idx] = ones[idx * 2] + ones[idx * 2 + 1];
        }
        fn apply(idx: usize, l: usize, r: usize, ones: &mut [i32], lazy: &mut [bool]) {
            ones[idx] = (r - l + 1) as i32 - ones[idx];
            lazy[idx] = !lazy[idx];
        }
        fn push(idx: usize, l: usize, r: usize, ones: &mut [i32], lazy: &mut [bool]) {
            if lazy[idx] && l != r {
                let m = (l + r) / 2;
                apply(idx * 2, l, m, ones, lazy);
                apply(idx * 2 + 1, m + 1, r, ones, lazy);
                lazy[idx] = false;
            }
        }
        fn update(
            idx: usize,
            l: usize,
            r: usize,
            ql: usize,
            qr: usize,
            ones: &mut [i32],
            lazy: &mut [bool],
        ) {
            if ql <= l && r <= qr {
                apply(idx, l, r, ones, lazy);
                return;
            }
            push(idx, l, r, ones, lazy);
            let m = (l + r) / 2;
            if ql <= m {
                update(idx * 2, l, m, ql, qr, ones, lazy);
            }
            if qr > m {
                update(idx * 2 + 1, m + 1, r, ql, qr, ones, lazy);
            }
            ones[idx] = ones[idx * 2] + ones[idx * 2 + 1];
        }
        build(1, 0, n - 1, &nums1, &mut ones);
        let mut sum2: i64 = nums2.iter().map(|&x| x as i64).sum();
        let mut ans = Vec::new();
        for q in queries {
            if q[0] == 1 {
                update(1, 0, n - 1, q[1] as usize, q[2] as usize, &mut ones, &mut lazy);
            } else if q[0] == 2 {
                sum2 += q[1] as i64 * ones[1] as i64;
            } else {
                ans.push(sum2);
            }
        }
        ans
    }
}

fn main() {}

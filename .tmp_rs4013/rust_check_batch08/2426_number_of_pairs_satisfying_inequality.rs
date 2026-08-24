struct Solution;
// LeetCode 2426 - Number of Pairs Satisfying Inequality
// https://leetcode.com/problems/number-of-pairs-satisfying-inequality/

impl Solution {
    pub fn number_of_pairs(nums1: Vec<i32>, nums2: Vec<i32>, diff: i32) -> i64 {
        let n = nums1.len();
        let mut arr: Vec<i32> = (0..n).map(|i| nums1[i] - nums2[i]).collect();
        let mut tmp = vec![0; n];
        fn merge_count(arr: &mut [i32], tmp: &mut [i32], l: usize, r: usize, diff: i32) -> i64 {
            if r - l <= 1 {
                return 0;
            }
            let m = (l + r) / 2;
            let mut ans = merge_count(arr, tmp, l, m, diff) + merge_count(arr, tmp, m, r, diff);
            let mut j = m;
            for i in l..m {
                while j < r && arr[j] < arr[i] - diff {
                    j += 1;
                }
                ans += (r - j) as i64;
            }
            let mut i = l;
            let mut p = l;
            let mut q = m;
            while p < m && q < r {
                if arr[p] <= arr[q] {
                    tmp[i] = arr[p];
                    i += 1;
                    p += 1;
                } else {
                    tmp[i] = arr[q];
                    i += 1;
                    q += 1;
                }
            }
            while p < m {
                tmp[i] = arr[p];
                i += 1;
                p += 1;
            }
            while q < r {
                tmp[i] = arr[q];
                i += 1;
                q += 1;
            }
            for t in l..r {
                arr[t] = tmp[t];
            }
            ans
        }
        merge_count(&mut arr, &mut tmp, 0, n, diff)
    }
}

fn main() {}

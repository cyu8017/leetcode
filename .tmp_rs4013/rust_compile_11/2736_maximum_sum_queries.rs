struct Solution;
fn main() {}

// LeetCode 2736 - Maximum Sum Queries
// https://leetcode.com/problems/maximum-sum-queries/

impl Solution {
    pub fn maximum_sum_queries(
        nums1: Vec<i32>,
        nums2: Vec<i32>,
        queries: Vec<Vec<i32>>,
    ) -> Vec<i32> {
        let n = nums1.len();
        let mut pts: Vec<(i32, i32, i32)> = (0..n)
            .map(|i| (nums1[i], nums2[i], nums1[i] + nums2[i]))
            .collect();
        pts.sort_unstable_by(|a, b| b.0.cmp(&a.0));
        let mut qs: Vec<(i32, i32, usize)> = queries
            .iter()
            .enumerate()
            .map(|(i, q)| (q[0], q[1], i))
            .collect();
        qs.sort_unstable_by(|a, b| b.0.cmp(&a.0));
        let mut ys = nums2.clone();
        for q in &queries {
            ys.push(q[1]);
        }
        ys.sort_unstable();
        ys.dedup();
        let rank = |y: i32, ys: &[i32]| ys.binary_search(&y).unwrap_or_else(|e| e) as i32 + 1;
        let m = ys.len() as i32;
        let mut bit = vec![-1i32; (m + 2) as usize];
        let update = |bit: &mut [i32], mut i: i32, v: i32| {
            while i <= m {
                bit[i as usize] = bit[i as usize].max(v);
                i += i & -i;
            }
        };
        let query = |bit: &[i32], mut i: i32| {
            let mut best = -1;
            while i > 0 {
                best = best.max(bit[i as usize]);
                i -= i & -i;
            }
            best
        };
        let mut ans = vec![0; queries.len()];
        let mut j = 0;
        for &(qx, qy, qi) in &qs {
            while j < n && pts[j].0 >= qx {
                update(&mut bit, m - rank(pts[j].1, &ys) + 1, pts[j].2);
                j += 1;
            }
            ans[qi] = query(&bit, m - rank(qy, &ys) + 1);
        }
        ans
    }
}

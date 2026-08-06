// LeetCode 1956 - Minimum Time For K Virus Variants to Spread
// https://leetcode.com/problems/minimum-time-for-k-virus-variants-to-spread/

impl Solution {
    pub fn min_daysk_variants(points: Vec<Vec<i32>>, k: i32) -> i32 {
        let mut ans = i32::MAX;
        for x in 1..=100 {
            for y in 1..=100 {
                let mut dists: Vec<i32> = points
                    .iter()
                    .map(|p| (p[0] - x).abs() + (p[1] - y).abs())
                    .collect();
                dists.sort_unstable();
                ans = ans.min(dists[(k - 1) as usize]);
            }
        }
        ans
    }
}

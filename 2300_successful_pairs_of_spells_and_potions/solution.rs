// LeetCode 2300 - Successful Pairs of Spells and Potions
// https://leetcode.com/problems/successful-pairs-of-spells-and-potions/

impl Solution {
    pub fn successful_pairs(spells: Vec<i32>, mut potions: Vec<i32>, success: i64) -> Vec<i32> {
        potions.sort_unstable();
        let m = potions.len();
        let mut ans = vec![0; spells.len()];
        for (i, &spell) in spells.iter().enumerate() {
            let mut lo = 0;
            let mut hi = m;
            while lo < hi {
                let mid = (lo + hi) / 2;
                if spell as i64 * potions[mid] as i64 >= success {
                    hi = mid;
                } else {
                    lo = mid + 1;
                }
            }
            ans[i] = (m - lo) as i32;
        }
        ans
    }
}

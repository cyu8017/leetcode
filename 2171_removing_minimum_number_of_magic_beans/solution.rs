// LeetCode 2171 - Removing Minimum Number of Magic Beans
// https://leetcode.com/problems/removing-minimum-number-of-magic-beans/

impl Solution {
    pub fn minimum_removal(mut beans: Vec<i32>) -> i64 {
        beans.sort_unstable();
        let n = beans.len();
        let sum: i64 = beans.iter().map(|&x| x as i64).sum();
        let mut ans = sum;
        for i in 0..n {
            let remain = (n - i) as i64 * beans[i] as i64;
            ans = ans.min(sum - remain);
        }
        ans
    }
}

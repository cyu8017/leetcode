// LeetCode 0986 - Interval List Intersections
// https://leetcode.com/problems/interval-list-intersections/

impl Solution {
    pub fn interval_intersection(
        first_list: Vec<Vec<i32>>,
        second_list: Vec<Vec<i32>>,
    ) -> Vec<Vec<i32>> {
        let mut i = 0;
        let mut j = 0;
        let mut ans = Vec::new();
        while i < first_list.len() && j < second_list.len() {
            let lo = first_list[i][0].max(second_list[j][0]);
            let hi = first_list[i][1].min(second_list[j][1]);
            if lo <= hi {
                ans.push(vec![lo, hi]);
            }
            if first_list[i][1] < second_list[j][1] {
                i += 1;
            } else {
                j += 1;
            }
        }
        ans
    }
}

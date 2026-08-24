// LeetCode 2739 - Total Distance Traveled
// https://leetcode.com/problems/total-distance-traveled/

impl Solution {
    pub fn distance_traveled(mut main_tank: i32, mut additional_tank: i32) -> i32 {
        let mut ans = 0;
        while main_tank > 0 {
            if main_tank >= 5 {
                ans += 50;
                main_tank -= 5;
                if additional_tank > 0 {
                    additional_tank -= 1;
                    main_tank += 1;
                }
            } else {
                ans += main_tank * 10;
                main_tank = 0;
            }
        }
        ans
    }
}

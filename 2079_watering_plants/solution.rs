// LeetCode 2079 - Watering Plants
// https://leetcode.com/problems/watering-plants/

impl Solution {
    pub fn watering_plants(plants: Vec<i32>, capacity: i32) -> i32 {
        let mut ans = 0;
        let mut cur = capacity;
        for (i, &p) in plants.iter().enumerate() {
            if cur < p {
                ans += i as i32 * 2;
                cur = capacity;
            }
            cur -= p;
            ans += 1;
        }
        ans
    }
}

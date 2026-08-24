// LeetCode 2105 - Watering Plants II
// https://leetcode.com/problems/watering-plants-ii/

impl Solution {
    pub fn minimum_refill(plants: Vec<i32>, capacity_a: i32, capacity_b: i32) -> i32 {
        let mut i = 0usize;
        let mut j = plants.len() - 1;
        let mut a = capacity_a;
        let mut b = capacity_b;
        let mut ans = 0;
        while i < j {
            if a < plants[i] {
                ans += 1;
                a = capacity_a;
            }
            a -= plants[i];
            i += 1;
            if b < plants[j] {
                ans += 1;
                b = capacity_b;
            }
            b -= plants[j];
            j -= 1;
        }
        if i == j {
            if a >= b {
                if a < plants[i] {
                    ans += 1;
                }
            } else if b < plants[i] {
                ans += 1;
            }
        }
        ans
    }
}

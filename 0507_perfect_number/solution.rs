// LeetCode 0507 - Perfect Number
// https://leetcode.com/problems/perfect-number/

impl Solution {
    pub fn check_perfect_number(num: i32) -> bool {
        if num <= 1 {
            return false;
        }
        let mut total = 1;
        let mut divisor = 2;
        while divisor * divisor <= num {
            if num % divisor == 0 {
                total += divisor;
                let pair = num / divisor;
                if pair != divisor {
                    total += pair;
                }
            }
            divisor += 1;
        }
        total == num
    }
}

// LeetCode 1701 - Average Waiting Time
// https://leetcode.com/problems/average-waiting-time/

impl Solution {
    pub fn average_waiting_time(customers: Vec<Vec<i32>>) -> f64 {
        let mut current: i64 = 0;
        let mut total: i64 = 0;
        for customer in &customers {
            let (arrival, cook) = (customer[0] as i64, customer[1] as i64);
            current = current.max(arrival) + cook;
            total += current - arrival;
        }
        total as f64 / customers.len() as f64
    }
}

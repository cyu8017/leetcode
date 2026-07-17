// LeetCode 1744 - Can You Eat Your Favorite Candy on Your Favorite Day?
// https://leetcode.com/problems/can-you-eat-your-favorite-candy-on-your-favorite-day/

impl Solution {
    pub fn can_eat(candies_count: Vec<i32>, queries: Vec<Vec<i32>>) -> Vec<bool> {
        let mut prefix: Vec<i64> = vec![0];
        for &count in &candies_count {
            prefix.push(prefix.last().unwrap() + count as i64);
        }
        queries
            .iter()
            .map(|query| {
                let candy_type = query[0] as usize;
                let day = query[1] as i64;
                let cap = query[2] as i64;
                let min_eaten = day + 1;
                let max_eaten = (day + 1) * cap;
                max_eaten > prefix[candy_type] && min_eaten <= prefix[candy_type + 1]
            })
            .collect()
    }
}

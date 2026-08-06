// LeetCode 1103 - Distribute Candies to People
// https://leetcode.com/problems/distribute-candies-to-people/

impl Solution {
    pub fn distribute_candies(mut candies: i32, num_people: i32) -> Vec<i32> {
        let num_people = num_people as usize;
        let mut ans = vec![0; num_people];
        let mut give = 1;
        let mut i = 0usize;
        while candies > 0 {
            let take = give.min(candies);
            ans[i] += take;
            candies -= take;
            give += 1;
            i = (i + 1) % num_people;
        }
        ans
    }
}

// LeetCode 0355 - Design Twitter
// https://leetcode.com/problems/design-twitter/

use std::collections::{HashMap, HashSet};

struct Twitter {
    time: i32,
    tweets: HashMap<i32, Vec<(i32, i32)>>,
    following: HashMap<i32, HashSet<i32>>,
}

impl Twitter {
    fn new() -> Self {
        Self {
            time: 0,
            tweets: HashMap::new(),
            following: HashMap::new(),
        }
    }

    fn post_tweet(&mut self, user_id: i32, tweet_id: i32) {
        self.time += 1;
        self.tweets.entry(user_id).or_default().push((self.time, tweet_id));
    }

    fn get_news_feed(&self, user_id: i32) -> Vec<i32> {
        let mut users = HashSet::new();
        users.insert(user_id);
        if let Some(followees) = self.following.get(&user_id) {
            users.extend(followees.iter().copied());
        }

        let mut items = Vec::new();
        for uid in users {
            if let Some(timeline) = self.tweets.get(&uid) {
                let start = timeline.len().saturating_sub(10);
                for &(timestamp, tweet_id) in &timeline[start..] {
                    items.push((timestamp, tweet_id));
                }
            }
        }

        items.sort_by(|left, right| right.0.cmp(&left.0).then(left.1.cmp(&right.1)));

        items.into_iter().take(10).map(|(_, tweet_id)| tweet_id).collect()
    }

    fn follow(&mut self, follower_id: i32, followee_id: i32) {
        self.following.entry(follower_id).or_default().insert(followee_id);
    }

    fn unfollow(&mut self, follower_id: i32, followee_id: i32) {
        if let Some(followees) = self.following.get_mut(&follower_id) {
            followees.remove(&followee_id);
        }
    }
}

// LeetCode 1348 - Tweet Counts Per Frequency
// https://leetcode.com/problems/tweet-counts-per-frequency/

use std::collections::HashMap;

struct TweetCounts {
    times: HashMap<String, Vec<i32>>,
}

impl TweetCounts {
    fn new() -> Self {
        Self { times: HashMap::new() }
    }

    fn record_tweet(&mut self, tweet_name: String, time: i32) {
        let entry = self.times.entry(tweet_name).or_default();
        let idx = entry.binary_search(&time).unwrap_or_else(|i| i);
        entry.insert(idx, time);
    }

    fn get_tweet_counts_per_frequency(
        &self,
        freq: String,
        tweet_name: String,
        start_time: i32,
        end_time: i32,
    ) -> Vec<i32> {
        let size = match freq.as_str() {
            "minute" => 60,
            "hour" => 3600,
            _ => 86400,
        };
        let times = self.times.get(&tweet_name).map(|v| v.as_slice()).unwrap_or(&[]);
        let mut answer = Vec::new();
        let mut start = start_time;
        while start <= end_time {
            let end = end_time.min(start + size - 1);
            let left = times.partition_point(|&t| t < start);
            let right = times.partition_point(|&t| t <= end);
            answer.push((right - left) as i32);
            start += size;
        }
        answer
    }
}

// LeetCode 1311 - Get Watched Videos by Your Friends
// https://leetcode.com/problems/get-watched-videos-by-your-friends/

use std::collections::{HashMap, HashSet, VecDeque};

impl Solution {
    pub fn watched_videos_by_friends(
        watched_videos: Vec<Vec<String>>,
        friends: Vec<Vec<i32>>,
        id: i32,
        level: i32,
    ) -> Vec<String> {
        let mut queue = VecDeque::new();
        let mut seen = HashSet::new();
        queue.push_back((id, 0));
        seen.insert(id);
        let mut people = Vec::new();
        while let Some((person, distance)) = queue.pop_front() {
            if distance == level {
                people.push(person);
                continue;
            }
            for &friend in &friends[person as usize] {
                if seen.insert(friend) {
                    queue.push_back((friend, distance + 1));
                }
            }
        }
        let mut counts: HashMap<String, i32> = HashMap::new();
        for person in people {
            for video in &watched_videos[person as usize] {
                *counts.entry(video.clone()).or_insert(0) += 1;
            }
        }
        let mut answer: Vec<String> = counts.keys().cloned().collect();
        answer.sort_by(|a, b| counts[a].cmp(&counts[b]).then(a.cmp(b)));
        answer
    }
}

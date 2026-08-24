// LeetCode 2254 - Design Video Sharing Platform
// https://leetcode.com/problems/design-video-sharing-platform/

use std::cmp::Reverse;
use std::collections::{BinaryHeap, HashMap};

pub struct VideoSharingPlatform {
    next_id: i32,
    free: BinaryHeap<Reverse<i32>>,
    videos: HashMap<i32, String>,
    views: HashMap<i32, i32>,
    likes: HashMap<i32, i32>,
    dislikes: HashMap<i32, i32>,
}

impl VideoSharingPlatform {
    pub fn new() -> Self {
        Self {
            next_id: 0,
            free: BinaryHeap::new(),
            videos: HashMap::new(),
            views: HashMap::new(),
            likes: HashMap::new(),
            dislikes: HashMap::new(),
        }
    }

    pub fn upload(&mut self, video: String) -> i32 {
        let id = if let Some(Reverse(id)) = self.free.pop() {
            id
        } else {
            let id = self.next_id;
            self.next_id += 1;
            id
        };
        self.videos.insert(id, video);
        self.views.insert(id, 0);
        self.likes.insert(id, 0);
        self.dislikes.insert(id, 0);
        id
    }

    pub fn remove(&mut self, video_id: i32) {
        if self.videos.remove(&video_id).is_none() {
            return;
        }
        self.views.remove(&video_id);
        self.likes.remove(&video_id);
        self.dislikes.remove(&video_id);
        self.free.push(Reverse(video_id));
    }

    pub fn watch(&mut self, video_id: i32, start_minute: i32, end_minute: i32) -> String {
        if !self.videos.contains_key(&video_id) {
            return "-1".to_string();
        }
        *self.views.entry(video_id).or_insert(0) += 1;
        let v = self.videos.get(&video_id).unwrap();
        if start_minute >= v.len() as i32 {
            return String::new();
        }
        let end = end_minute.min(v.len() as i32 - 1);
        v[start_minute as usize..=end as usize].to_string()
    }

    pub fn like(&mut self, video_id: i32) {
        if self.videos.contains_key(&video_id) {
            *self.likes.entry(video_id).or_insert(0) += 1;
        }
    }

    pub fn dislike(&mut self, video_id: i32) {
        if self.videos.contains_key(&video_id) {
            *self.dislikes.entry(video_id).or_insert(0) += 1;
        }
    }

    pub fn get_likes_and_dislikes(&self, video_id: i32) -> Vec<i32> {
        if !self.videos.contains_key(&video_id) {
            return vec![-1];
        }
        vec![
            *self.likes.get(&video_id).unwrap_or(&0),
            *self.dislikes.get(&video_id).unwrap_or(&0),
        ]
    }

    pub fn get_views(&self, video_id: i32) -> i32 {
        if !self.videos.contains_key(&video_id) {
            return -1;
        }
        *self.views.get(&video_id).unwrap_or(&0)
    }
}

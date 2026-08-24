// LeetCode 2456 - Most Popular Video Creator
// https://leetcode.com/problems/most-popular-video-creator/

use std::collections::HashMap;

impl Solution {
    pub fn most_popular_creator(
        creators: Vec<String>,
        ids: Vec<String>,
        views: Vec<i32>,
    ) -> Vec<Vec<String>> {
        struct Info {
            total: i64,
            best_id: String,
            best_views: i32,
        }
        let mut mp: HashMap<String, Info> = HashMap::new();
        let mut max_total = 0i64;
        for i in 0..creators.len() {
            let entry = mp.entry(creators[i].clone()).or_insert_with(|| Info {
                total: 0,
                best_id: ids[i].clone(),
                best_views: views[i],
            });
            if entry.total == 0 && entry.best_id.is_empty() {
                entry.best_id = ids[i].clone();
                entry.best_views = views[i];
            }
            entry.total += views[i] as i64;
            if views[i] > entry.best_views
                || (views[i] == entry.best_views && ids[i] < entry.best_id)
            {
                entry.best_views = views[i];
                entry.best_id = ids[i].clone();
            }
            if entry.total > max_total {
                max_total = entry.total;
            }
        }
        let mut ans = Vec::new();
        for (c, inf) in mp {
            if inf.total == max_total {
                ans.push(vec![c, inf.best_id]);
            }
        }
        ans
    }
}

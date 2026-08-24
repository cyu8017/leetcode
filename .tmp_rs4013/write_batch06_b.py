#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")

TREE = """use std::cell::RefCell;
use std::rc::Rc;

#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl TreeNode {
    #[inline]
    pub fn new(val: i32) -> Self {
        TreeNode {
            val,
            left: None,
            right: None,
        }
    }
}
"""

FILES = {}

FILES["2236_root_equals_sum_of_children"] = f'''// LeetCode 2236 - Root Equals Sum of Children
// https://leetcode.com/problems/root-equals-sum-of-children/

{TREE}
impl Solution {{
    pub fn check_tree(root: Option<Rc<RefCell<TreeNode>>>) -> bool {{
        let root = root.unwrap();
        let n = root.borrow();
        let left = n.left.as_ref().unwrap().borrow().val;
        let right = n.right.as_ref().unwrap().borrow().val;
        n.val == left + right
    }}
}}
'''

FILES["2237_count_positions_on_street_with_required_brightness"] = r'''// LeetCode 2237 - Count Positions on Street With Required Brightness
// https://leetcode.com/problems/count-positions-on-street-with-required-brightness/

impl Solution {
    pub fn meet_requirement(n: i32, lights: Vec<Vec<i32>>, requirement: Vec<i32>) -> i32 {
        let n = n as usize;
        let mut diff = vec![0i32; n + 1];
        for light in lights {
            let pos = light[0];
            let r = light[1];
            let l = 0.max(pos - r) as usize;
            let rr = ((n as i32 - 1).min(pos + r)) as usize;
            diff[l] += 1;
            diff[rr + 1] -= 1;
        }
        let mut ans = 0;
        let mut cur = 0;
        for i in 0..n {
            cur += diff[i];
            if cur >= requirement[i] {
                ans += 1;
            }
        }
        ans
    }
}
'''

FILES["2239_find_closest_number_to_zero"] = r'''// LeetCode 2239 - Find Closest Number to Zero
// https://leetcode.com/problems/find-closest-number-to-zero/

impl Solution {
    pub fn find_closest_number(nums: Vec<i32>) -> i32 {
        let mut ans = nums[0];
        for x in nums {
            if x.abs() < ans.abs() || (x.abs() == ans.abs() && x > ans) {
                ans = x;
            }
        }
        ans
    }
}
'''

FILES["2240_number_of_ways_to_buy_pens_and_pencils"] = r'''// LeetCode 2240 - Number of Ways to Buy Pens and Pencils
// https://leetcode.com/problems/number-of-ways-to-buy-pens-and-pencils/

impl Solution {
    pub fn ways_to_buy_pens_pencils(total: i32, cost1: i32, cost2: i32) -> i64 {
        let mut ans = 0i64;
        let mut pens = 0;
        while pens * cost1 <= total {
            let remain = total - pens * cost1;
            ans += (remain / cost2 + 1) as i64;
            pens += 1;
        }
        ans
    }
}
'''

FILES["2241_design_an_atm_machine"] = r'''// LeetCode 2241 - Design an ATM Machine
// https://leetcode.com/problems/design-an-atm-machine/

pub struct ATM {
    cnt: [i64; 5],
    vals: [i32; 5],
}

impl ATM {
    pub fn new() -> Self {
        Self {
            cnt: [0; 5],
            vals: [20, 50, 100, 200, 500],
        }
    }

    pub fn deposit(&mut self, banknotes_count: Vec<i32>) {
        for i in 0..5 {
            self.cnt[i] += banknotes_count[i] as i64;
        }
    }

    pub fn withdraw(&mut self, amount: i32) -> Vec<i32> {
        let mut take = vec![0; 5];
        let mut remain = amount as i64;
        let tmp = self.cnt;
        for i in (0..5).rev() {
            let mut need = remain / self.vals[i] as i64;
            if need > tmp[i] {
                need = tmp[i];
            }
            take[i] = need as i32;
            remain -= need * self.vals[i] as i64;
        }
        if remain != 0 {
            return vec![-1];
        }
        for i in 0..5 {
            self.cnt[i] -= take[i] as i64;
        }
        take
    }
}
'''

FILES["2242_maximum_score_of_a_node_sequence"] = r'''// LeetCode 2242 - Maximum Score of a Node Sequence
// https://leetcode.com/problems/maximum-score-of-a-node-sequence/

impl Solution {
    pub fn maximum_score(scores: Vec<i32>, edges: Vec<Vec<i32>>) -> i32 {
        let n = scores.len();
        let mut g = vec![Vec::new(); n];
        for e in &edges {
            g[e[0] as usize].push(e[1] as usize);
            g[e[1] as usize].push(e[0] as usize);
        }
        let mut top = vec![Vec::new(); n];
        for i in 0..n {
            for &v in &g[i] {
                top[i].push(v);
                let mut j = top[i].len() - 1;
                while j > 0 && scores[top[i][j]] > scores[top[i][j - 1]] {
                    top[i].swap(j, j - 1);
                    j -= 1;
                }
                if top[i].len() > 3 {
                    top[i].truncate(3);
                }
            }
        }
        let mut ans = -1;
        for e in &edges {
            let a = e[0] as usize;
            let b = e[1] as usize;
            for &c in &top[a] {
                if c == b {
                    continue;
                }
                for &d in &top[b] {
                    if d == a || d == c {
                        continue;
                    }
                    ans = ans.max(scores[a] + scores[b] + scores[c] + scores[d]);
                }
            }
        }
        ans
    }
}
'''

FILES["2243_calculate_digit_sum_of_a_string"] = r'''// LeetCode 2243 - Calculate Digit Sum of a String
// https://leetcode.com/problems/calculate-digit-sum-of-a-string/

impl Solution {
    pub fn digit_sum(mut s: String, k: i32) -> String {
        let k = k as usize;
        while s.len() > k {
            let bytes = s.as_bytes();
            let mut next = String::new();
            let mut i = 0;
            while i < bytes.len() {
                let end = (i + k).min(bytes.len());
                let mut sum = 0;
                for j in i..end {
                    sum += (bytes[j] - b'0') as i32;
                }
                next.push_str(&sum.to_string());
                i += k;
            }
            s = next;
        }
        s
    }
}
'''

FILES["2244_minimum_rounds_to_complete_all_tasks"] = r'''// LeetCode 2244 - Minimum Rounds to Complete All Tasks
// https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/

use std::collections::HashMap;

impl Solution {
    pub fn minimum_rounds(tasks: Vec<i32>) -> i32 {
        let mut freq = HashMap::new();
        for t in tasks {
            *freq.entry(t).or_insert(0) += 1;
        }
        let mut ans = 0;
        for &c in freq.values() {
            if c == 1 {
                return -1;
            }
            ans += (c + 2) / 3;
        }
        ans
    }
}
'''

FILES["2245_maximum_trailing_zeros_in_a_cornered_path"] = r'''// LeetCode 2245 - Maximum Trailing Zeros in a Cornered Path
// https://leetcode.com/problems/maximum-trailing-zeros-in-a-cornered-path/

impl Solution {
    pub fn max_trailing_zeros(grid: Vec<Vec<i32>>) -> i32 {
        fn fact(mut x: i32) -> (i32, i32) {
            let mut t = 0;
            let mut f = 0;
            while x % 2 == 0 {
                t += 1;
                x /= 2;
            }
            while x % 5 == 0 {
                f += 1;
                x /= 5;
            }
            (t, f)
        }
        let m = grid.len();
        let n = grid[0].len();
        let mut left = vec![vec![(0, 0); n]; m];
        let mut up = vec![vec![(0, 0); n]; m];
        for i in 0..m {
            for j in 0..n {
                let p = fact(grid[i][j]);
                left[i][j] = p;
                up[i][j] = p;
                if j > 0 {
                    left[i][j].0 += left[i][j - 1].0;
                    left[i][j].1 += left[i][j - 1].1;
                }
                if i > 0 {
                    up[i][j].0 += up[i - 1][j].0;
                    up[i][j].1 += up[i - 1][j].1;
                }
            }
        }
        let mut ans = 0;
        for i in 0..m {
            for j in 0..n {
                let cell = fact(grid[i][j]);
                let l = left[i][j];
                let r_two = left[i][n - 1].0 - left[i][j].0 + cell.0;
                let r_five = left[i][n - 1].1 - left[i][j].1 + cell.1;
                let u = up[i][j];
                let d_two = up[m - 1][j].0 - up[i][j].0 + cell.0;
                let d_five = up[m - 1][j].1 - up[i][j].1 + cell.1;
                let cands = [
                    (l.0 + u.0 - cell.0, l.1 + u.1 - cell.1),
                    (l.0 + d_two - cell.0, l.1 + d_five - cell.1),
                    (r_two + u.0 - cell.0, r_five + u.1 - cell.1),
                    (r_two + d_two - cell.0, r_five + d_five - cell.1),
                ];
                for c in cands {
                    ans = ans.max(c.0.min(c.1));
                }
            }
        }
        ans
    }
}
'''

FILES["2246_longest_path_with_different_adjacent_characters"] = r'''// LeetCode 2246 - Longest Path With Different Adjacent Characters
// https://leetcode.com/problems/longest-path-with-different-adjacent-characters/

impl Solution {
    pub fn longest_path(parent: Vec<i32>, s: String) -> i32 {
        let n = parent.len();
        let mut g = vec![Vec::new(); n];
        for i in 1..n {
            g[parent[i] as usize].push(i);
        }
        let s = s.into_bytes();
        let mut ans = 1;
        fn dfs(u: usize, g: &[Vec<usize>], s: &[u8], ans: &mut i32) -> i32 {
            let mut best1 = 0;
            let mut best2 = 0;
            for &v in &g[u] {
                let len_v = dfs(v, g, s, ans);
                if s[v] == s[u] {
                    continue;
                }
                if len_v > best1 {
                    best2 = best1;
                    best1 = len_v;
                } else if len_v > best2 {
                    best2 = len_v;
                }
            }
            *ans = (*ans).max(1 + best1 + best2);
            1 + best1
        }
        dfs(0, &g, &s, &mut ans);
        ans
    }
}
'''

FILES["2247_maximum_cost_of_trip_with_k_highways"] = r'''// LeetCode 2247 - Maximum Cost of Trip With K Highways
// https://leetcode.com/problems/maximum-cost-of-trip-with-k-highways/

impl Solution {
    pub fn maximum_cost(n: i32, highways: Vec<Vec<i32>>, k: i32) -> i32 {
        let n = n as usize;
        if k + 1 > n as i32 {
            return -1;
        }
        let mut g = vec![Vec::new(); n];
        for h in highways {
            g[h[0] as usize].push((h[1] as usize, h[2]));
            g[h[1] as usize].push((h[0] as usize, h[2]));
        }
        let mut dp = vec![vec![-1; n]; 1 << n];
        for i in 0..n {
            dp[1 << i][i] = 0;
        }
        let mut ans = -1;
        for mask in 0..(1 << n) {
            let cities = mask.count_ones() as i32;
            for u in 0..n {
                if dp[mask][u] < 0 {
                    continue;
                }
                if cities - 1 == k {
                    ans = ans.max(dp[mask][u]);
                }
                for &(v, w) in &g[u] {
                    if mask & (1 << v) != 0 {
                        continue;
                    }
                    let nm = mask | (1 << v);
                    dp[nm][v] = dp[nm][v].max(dp[mask][u] + w);
                }
            }
        }
        ans
    }
}
'''

FILES["2248_intersection_of_multiple_arrays"] = r'''// LeetCode 2248 - Intersection of Multiple Arrays
// https://leetcode.com/problems/intersection-of-multiple-arrays/

use std::collections::{HashMap, HashSet};

impl Solution {
    pub fn intersection(nums: Vec<Vec<i32>>) -> Vec<i32> {
        let m = nums.len() as i32;
        let mut freq = HashMap::new();
        for arr in &nums {
            let mut seen = HashSet::new();
            for &x in arr {
                if seen.insert(x) {
                    *freq.entry(x).or_insert(0) += 1;
                }
            }
        }
        let mut ans: Vec<i32> = freq.into_iter().filter(|(_, c)| *c == m).map(|(x, _)| x).collect();
        ans.sort_unstable();
        ans
    }
}
'''

FILES["2249_count_lattice_points_inside_a_circle"] = r'''// LeetCode 2249 - Count Lattice Points Inside a Circle
// https://leetcode.com/problems/count-lattice-points-inside-a-circle/

use std::collections::HashSet;

impl Solution {
    pub fn count_lattice_points(circles: Vec<Vec<i32>>) -> i32 {
        let mut seen = HashSet::new();
        for c in circles {
            let (x, y, r) = (c[0], c[1], c[2]);
            for i in x - r..=x + r {
                for j in y - r..=y + r {
                    if (i - x) * (i - x) + (j - y) * (j - y) <= r * r {
                        seen.insert((i, j));
                    }
                }
            }
        }
        seen.len() as i32
    }
}
'''

FILES["2250_count_number_of_rectangles_containing_each_point"] = r'''// LeetCode 2250 - Count Number of Rectangles Containing Each Point
// https://leetcode.com/problems/count-number-of-rectangles-containing-each-point/

impl Solution {
    pub fn count_rectangles(rectangles: Vec<Vec<i32>>, points: Vec<Vec<i32>>) -> Vec<i32> {
        let mut by_h: Vec<Vec<i32>> = vec![Vec::new(); 101];
        for r in rectangles {
            by_h[r[1] as usize].push(r[0]);
        }
        for h in 1..=100 {
            by_h[h].sort_unstable();
        }
        let mut ans = vec![0; points.len()];
        for (i, p) in points.iter().enumerate() {
            let x = p[0];
            let y = p[1] as usize;
            let mut cnt = 0;
            for h in y..=100 {
                let xs = &by_h[h];
                let it = xs.partition_point(|&v| v < x);
                cnt += (xs.len() - it) as i32;
            }
            ans[i] = cnt;
        }
        ans
    }
}
'''

FILES["2251_number_of_flowers_in_full_bloom"] = r'''// LeetCode 2251 - Number of Flowers in Full Bloom
// https://leetcode.com/problems/number-of-flowers-in-full-bloom/

impl Solution {
    pub fn full_bloom_flowers(flowers: Vec<Vec<i32>>, people: Vec<i32>) -> Vec<i32> {
        let mut start = Vec::new();
        let mut end = Vec::new();
        for f in flowers {
            start.push(f[0]);
            end.push(f[1]);
        }
        start.sort_unstable();
        end.sort_unstable();
        let mut ans = vec![0; people.len()];
        for (i, &t) in people.iter().enumerate() {
            let started = start.partition_point(|&v| v <= t) as i32;
            let ended = end.partition_point(|&v| v < t) as i32;
            ans[i] = started - ended;
        }
        ans
    }
}
'''

FILES["2254_design_video_sharing_platform"] = r'''// LeetCode 2254 - Design Video Sharing Platform
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
        let Some(v) = self.videos.get(&video_id) else {
            return "-1".to_string();
        };
        *self.views.entry(video_id).or_insert(0) += 1;
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
'''

FILES["2255_count_prefixes_of_a_given_string"] = r'''// LeetCode 2255 - Count Prefixes of a Given String
// https://leetcode.com/problems/count-prefixes-of-a-given-string/

impl Solution {
    pub fn count_prefixes(words: Vec<String>, s: String) -> i32 {
        words.iter().filter(|w| s.starts_with(w.as_str())).count() as i32
    }
}
'''

FILES["2256_minimum_average_difference"] = r'''// LeetCode 2256 - Minimum Average Difference
// https://leetcode.com/problems/minimum-average-difference/

impl Solution {
    pub fn minimum_average_difference(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let total: i64 = nums.iter().map(|&v| v as i64).sum();
        let mut left = 0i64;
        let mut best_diff = i64::MAX;
        let mut best_idx = 0;
        for i in 0..n {
            left += nums[i] as i64;
            let left_avg = left / (i as i64 + 1);
            let right_avg = if i != n - 1 {
                (total - left) / (n as i64 - i as i64 - 1)
            } else {
                0
            };
            let diff = (left_avg - right_avg).abs();
            if diff < best_diff {
                best_diff = diff;
                best_idx = i;
            }
        }
        best_idx as i32
    }
}
'''

FILES["2257_count_unguarded_cells_in_the_grid"] = r'''// LeetCode 2257 - Count Unguarded Cells in the Grid
// https://leetcode.com/problems/count-unguarded-cells-in-the-grid/

impl Solution {
    pub fn count_unguarded(m: i32, n: i32, guards: Vec<Vec<i32>>, walls: Vec<Vec<i32>>) -> i32 {
        let m = m as usize;
        let n = n as usize;
        let mut grid = vec![vec![0i32; n]; m];
        for w in &walls {
            grid[w[0] as usize][w[1] as usize] = 2;
        }
        for g in &guards {
            grid[g[0] as usize][g[1] as usize] = 2;
        }
        let dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)];
        for g in &guards {
            for &(dr, dc) in &dirs {
                let mut r = g[0] + dr;
                let mut c = g[1] + dc;
                while r >= 0 && r < m as i32 && c >= 0 && c < n as i32 && grid[r as usize][c as usize] != 2 {
                    grid[r as usize][c as usize] = 1;
                    r += dr;
                    c += dc;
                }
            }
        }
        let mut ans = 0;
        for i in 0..m {
            for j in 0..n {
                if grid[i][j] == 0 {
                    ans += 1;
                }
            }
        }
        ans
    }
}
'''

FILES["2258_escape_the_spreading_fire"] = r'''// LeetCode 2258 - Escape the Spreading Fire
// https://leetcode.com/problems/escape-the-spreading-fire/

use std::collections::VecDeque;

impl Solution {
    pub fn maximum_minutes(grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        const INF: i32 = 1_000_000_000;
        let mut fire = vec![vec![INF; n]; m];
        let mut q = VecDeque::new();
        for i in 0..m {
            for j in 0..n {
                if grid[i][j] == 1 {
                    fire[i][j] = 0;
                    q.push_back((i, j));
                }
            }
        }
        let dirs = [(1isize, 0), (-1, 0), (0, 1), (0, -1)];
        while let Some((r, c)) = q.pop_front() {
            for &(dr, dc) in &dirs {
                let nr = r as isize + dr;
                let nc = c as isize + dc;
                if nr < 0 || nr >= m as isize || nc < 0 || nc >= n as isize {
                    continue;
                }
                let (nr, nc) = (nr as usize, nc as usize);
                if grid[nr][nc] == 2 || fire[nr][nc] != INF {
                    continue;
                }
                fire[nr][nc] = fire[r][c] + 1;
                q.push_back((nr, nc));
            }
        }
        let can = |wait: i32| -> bool {
            if wait >= fire[0][0] {
                return false;
            }
            let mut vis = vec![vec![false; n]; m];
            let mut qq = VecDeque::new();
            qq.push_back((0usize, 0usize, wait));
            vis[0][0] = true;
            while let Some((r, c, t)) = qq.pop_front() {
                for &(dr, dc) in &dirs {
                    let nr = r as isize + dr;
                    let nc = c as isize + dc;
                    let nt = t + 1;
                    if nr < 0 || nr >= m as isize || nc < 0 || nc >= n as isize {
                        continue;
                    }
                    let (nr, nc) = (nr as usize, nc as usize);
                    if grid[nr][nc] == 2 || vis[nr][nc] {
                        continue;
                    }
                    if nr == m - 1 && nc == n - 1 {
                        if nt <= fire[nr][nc] {
                            return true;
                        }
                        continue;
                    }
                    if nt >= fire[nr][nc] {
                        continue;
                    }
                    vis[nr][nc] = true;
                    qq.push_back((nr, nc, nt));
                }
            }
            false
        };
        let mut lo = 0;
        let mut hi = (m * n + 10) as i32;
        let mut ans = -1;
        while lo <= hi {
            let mid = (lo + hi) / 2;
            if can(mid) {
                ans = mid;
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        if ans >= (m * n) as i32 {
            INF
        } else {
            ans
        }
    }
}
'''

FILES["2259_remove_digit_from_number_to_maximize_result"] = r'''// LeetCode 2259 - Remove Digit From Number to Maximize Result
// https://leetcode.com/problems/remove-digit-from-number-to-maximize-result/

impl Solution {
    pub fn remove_digit(number: String, digit: char) -> String {
        let mut best = String::new();
        let bytes = number.as_bytes();
        for i in 0..bytes.len() {
            if bytes[i] as char == digit {
                let cand = format!("{}{}", &number[..i], &number[i + 1..]);
                if cand > best {
                    best = cand;
                }
            }
        }
        best
    }
}
'''

FILES["2260_minimum_consecutive_cards_to_pick_up"] = r'''// LeetCode 2260 - Minimum Consecutive Cards to Pick Up
// https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up/

use std::collections::HashMap;

impl Solution {
    pub fn minimum_card_pickup(cards: Vec<i32>) -> i32 {
        let mut last = HashMap::new();
        let mut ans = -1;
        for (i, &c) in cards.iter().enumerate() {
            if let Some(&prev) = last.get(&c) {
                let diff = i as i32 - prev + 1;
                if ans == -1 || diff < ans {
                    ans = diff;
                }
            }
            last.insert(c, i as i32);
        }
        ans
    }
}
'''

FILES["2261_k_divisible_elements_subarrays"] = r'''// LeetCode 2261 - K Divisible Elements Subarrays
// https://leetcode.com/problems/k-divisible-elements-subarrays/

use std::collections::HashSet;

impl Solution {
    pub fn count_distinct(nums: Vec<i32>, k: i32, p: i32) -> i32 {
        let n = nums.len();
        let mut seen = HashSet::new();
        for i in 0..n {
            let mut div = 0;
            let mut key = String::new();
            for j in i..n {
                if nums[j] % p == 0 {
                    div += 1;
                }
                if div > k {
                    break;
                }
                key.push_str(&(nums[j] + 1).to_string());
                key.push(',');
                seen.insert(key.clone());
            }
        }
        seen.len() as i32
    }
}
'''

FILES["2262_total_appeal_of_a_string"] = r'''// LeetCode 2262 - Total Appeal of A String
// https://leetcode.com/problems/total-appeal-of-a-string/

impl Solution {
    pub fn appeal_sum(s: String) -> i64 {
        let mut last = [-1i32; 26];
        let mut ans = 0i64;
        let mut cur = 0i64;
        for (i, c) in s.bytes().enumerate() {
            let idx = (c - b'a') as usize;
            cur += i as i64 - last[idx] as i64;
            last[idx] = i as i32;
            ans += cur;
        }
        ans
    }
}
'''

FILES["2263_make_array_non_decreasing_or_non_increasing"] = r'''// LeetCode 2263 - Make Array Non-decreasing or Non-increasing
// https://leetcode.com/problems/make-array-non-decreasing-or-non-increasing/

use std::collections::BinaryHeap;

impl Solution {
    pub fn convert_array(nums: Vec<i32>) -> i32 {
        fn cost(arr: &[i32]) -> i32 {
            let mut h = BinaryHeap::new();
            let mut ans = 0;
            for &x in arr {
                if let Some(&top) = h.peek() {
                    if top > x {
                        ans += top - x;
                        h.pop();
                        h.push(x);
                    }
                }
                h.push(x);
            }
            ans
        }
        let rev: Vec<i32> = nums.iter().copied().rev().collect();
        cost(&nums).min(cost(&rev))
    }
}
'''

FILES["2264_largest_3_same_digit_number_in_string"] = r'''// LeetCode 2264 - Largest 3-Same-Digit Number in String
// https://leetcode.com/problems/largest-3-same-digit-number-in-string/

impl Solution {
    pub fn largest_good_integer(num: String) -> String {
        let mut best = String::new();
        let bytes = num.as_bytes();
        for i in 0..bytes.len().saturating_sub(2) {
            if bytes[i] == bytes[i + 1] && bytes[i] == bytes[i + 2] {
                let cand = &num[i..i + 3];
                if cand > best.as_str() {
                    best = cand.to_string();
                }
            }
        }
        best
    }
}
'''

FILES["2265_count_nodes_equal_to_average_of_subtree"] = f'''// LeetCode 2265 - Count Nodes Equal to Average of Subtree
// https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

{TREE}
impl Solution {{
    pub fn average_of_subtree(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {{
        fn dfs(node: Option<Rc<RefCell<TreeNode>>>, ans: &mut i32) -> (i32, i32) {{
            let Some(node) = node else {{
                return (0, 0);
            }};
            let n = node.borrow();
            let (ls, lc) = dfs(n.left.clone(), ans);
            let (rs, rc) = dfs(n.right.clone(), ans);
            let sum = ls + rs + n.val;
            let cnt = lc + rc + 1;
            if sum / cnt == n.val {{
                *ans += 1;
            }}
            (sum, cnt)
        }}
        let mut ans = 0;
        dfs(root, &mut ans);
        ans
    }}
}}
'''

FILES["2266_count_number_of_texts"] = r'''// LeetCode 2266 - Count Number of Texts
// https://leetcode.com/problems/count-number-of-texts/

impl Solution {
    pub fn count_texts(pressed_keys: String) -> i32 {
        const MOD: i32 = 1_000_000_007;
        let s = pressed_keys.as_bytes();
        let n = s.len();
        let mut dp = vec![0i32; n + 1];
        dp[0] = 1;
        for i in 1..=n {
            dp[i] = dp[i - 1];
            let max_press = if s[i - 1] == b'7' || s[i - 1] == b'9' { 4 } else { 3 };
            for j in 2..=max_press {
                if j > i {
                    break;
                }
                if s[i - j] != s[i - 1] {
                    break;
                }
                dp[i] = (dp[i] + dp[i - j]) % MOD;
            }
        }
        dp[n]
    }
}
'''

FILES["2267_check_if_there_is_a_valid_parentheses_string_path"] = r'''// LeetCode 2267 - Check if There Is a Valid Parentheses String Path
// https://leetcode.com/problems/check-if-there-is-a-valid-parentheses-string-path/

use std::collections::HashSet;

impl Solution {
    pub fn has_valid_path(grid: Vec<Vec<char>>) -> bool {
        let m = grid.len();
        let n = grid[0].len();
        if (m + n - 1) % 2 == 1 || grid[0][0] == ')' || grid[m - 1][n - 1] == '(' {
            return false;
        }
        let mut vis = HashSet::new();
        fn dfs(
            r: usize,
            c: usize,
            mut bal: i32,
            grid: &[Vec<char>],
            vis: &mut HashSet<(usize, usize, i32)>,
        ) -> bool {
            let m = grid.len();
            let n = grid[0].len();
            if r >= m || c >= n {
                return false;
            }
            bal += if grid[r][c] == '(' { 1 } else { -1 };
            if bal < 0 {
                return false;
            }
            if r == m - 1 && c == n - 1 {
                return bal == 0;
            }
            if !vis.insert((r, c, bal)) {
                return false;
            }
            dfs(r + 1, c, bal, grid, vis) || dfs(r, c + 1, bal, grid, vis)
        }
        dfs(0, 0, 0, &grid, &mut vis)
    }
}
'''

FILES["2268_minimum_number_of_keypresses"] = r'''// LeetCode 2268 - Minimum Number of Keypresses
// https://leetcode.com/problems/minimum-number-of-keypresses/

impl Solution {
    pub fn minimum_keypresses(s: String) -> i32 {
        let mut freq = [0i32; 26];
        for c in s.bytes() {
            freq[(c - b'a') as usize] += 1;
        }
        freq.sort_unstable_by(|a, b| b.cmp(a));
        let mut ans = 0;
        for i in 0..26 {
            if freq[i] == 0 {
                break;
            }
            ans += freq[i] * (i as i32 / 9 + 1);
        }
        ans
    }
}
'''

FILES["2269_find_the_k_beauty_of_a_number"] = r'''// LeetCode 2269 - Find the K-Beauty of a Number
// https://leetcode.com/problems/find-the-k-beauty-of-a-number/

impl Solution {
    pub fn divisor_substrings(num: i32, k: i32) -> i32 {
        let s = num.to_string();
        let bytes = s.as_bytes();
        let k = k as usize;
        let mut ans = 0;
        for i in 0..=bytes.len().saturating_sub(k) {
            let mut sub = 0i32;
            for j in 0..k {
                sub = sub * 10 + (bytes[i + j] - b'0') as i32;
            }
            if sub != 0 && num % sub == 0 {
                ans += 1;
            }
        }
        ans
    }
}
'''

FILES["2270_number_of_ways_to_split_array"] = r'''// LeetCode 2270 - Number of Ways to Split Array
// https://leetcode.com/problems/number-of-ways-to-split-array/

impl Solution {
    pub fn ways_to_split_array(nums: Vec<i32>) -> i32 {
        let total: i64 = nums.iter().map(|&v| v as i64).sum();
        let mut left = 0i64;
        let mut ans = 0;
        for i in 0..nums.len() - 1 {
            left += nums[i] as i64;
            if left >= total - left {
                ans += 1;
            }
        }
        ans
    }
}
'''

written = 0
for folder, content in FILES.items():
    path = ROOT / folder / "solution.rs"
    path.write_text(content, encoding="utf-8", newline="\n")
    written += 1
print(f"wrote {written}")

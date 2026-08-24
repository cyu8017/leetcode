#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
FILES = {}

FILES["2271_maximum_white_tiles_covered_by_a_carpet"] = r'''// LeetCode 2271 - Maximum White Tiles Covered by a Carpet
// https://leetcode.com/problems/maximum-white-tiles-covered-by-a-carpet/

impl Solution {
    pub fn maximum_white_tiles(mut tiles: Vec<Vec<i32>>, carpet_len: i32) -> i32 {
        tiles.sort_unstable();
        let n = tiles.len();
        let mut pref = vec![0i32; n + 1];
        for i in 0..n {
            pref[i + 1] = pref[i] + (tiles[i][1] - tiles[i][0] + 1);
        }
        let mut ans = 0;
        let mut j = 0;
        for i in 0..n {
            let end = tiles[i][0] + carpet_len - 1;
            while j < n && tiles[j][0] <= end {
                j += 1;
            }
            let mut cover = pref[j] - pref[i];
            if j > 0 && tiles[j - 1][1] > end {
                cover -= tiles[j - 1][1] - end;
            }
            ans = ans.max(cover);
        }
        ans
    }
}
'''

FILES["2272_substring_with_largest_variance"] = r'''// LeetCode 2272 - Substring With Largest Variance
// https://leetcode.com/problems/substring-with-largest-variance/

impl Solution {
    pub fn largest_variance(s: String) -> i32 {
        let mut ans = 0;
        for a in b'a'..=b'z' {
            for b in b'a'..=b'z' {
                if a == b {
                    continue;
                }
                let mut bal = 0;
                let mut has_b = false;
                for c in s.bytes() {
                    if c == a {
                        bal += 1;
                    } else if c == b {
                        bal -= 1;
                        has_b = true;
                    }
                    if has_b {
                        ans = ans.max(bal);
                    }
                    if bal < 0 {
                        bal = 0;
                        has_b = false;
                    }
                }
            }
        }
        ans
    }
}
'''

FILES["2273_find_resultant_array_after_removing_anagrams"] = r'''// LeetCode 2273 - Find Resultant Array After Removing Anagrams
// https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/

impl Solution {
    pub fn remove_anagrams(words: Vec<String>) -> Vec<String> {
        fn sig(w: &str) -> [i32; 26] {
            let mut c = [0; 26];
            for ch in w.bytes() {
                c[(ch - b'a') as usize] += 1;
            }
            c
        }
        let mut ans = vec![words[0].clone()];
        let mut prev = sig(&words[0]);
        for w in words.iter().skip(1) {
            let cur = sig(w);
            if cur != prev {
                ans.push(w.clone());
                prev = cur;
            }
        }
        ans
    }
}
'''

FILES["2274_maximum_consecutive_floors_without_special_floors"] = r'''// LeetCode 2274 - Maximum Consecutive Floors Without Special Floors
// https://leetcode.com/problems/maximum-consecutive-floors-without-special-floors/

impl Solution {
    pub fn max_consecutive(bottom: i32, top: i32, mut special: Vec<i32>) -> i32 {
        special.sort_unstable();
        let mut ans = special[0] - bottom;
        for i in 1..special.len() {
            ans = ans.max(special[i] - special[i - 1] - 1);
        }
        ans.max(top - *special.last().unwrap())
    }
}
'''

FILES["2275_largest_combination_with_bitwise_and_greater_than_zero"] = r'''// LeetCode 2275 - Largest Combination With Bitwise AND Greater Than Zero
// https://leetcode.com/problems/largest-combination-with-bitwise-and-greater-than-zero/

impl Solution {
    pub fn largest_combination(candidates: Vec<i32>) -> i32 {
        let mut ans = 0;
        for bit in 0..24 {
            let mut cnt = 0;
            for &x in &candidates {
                if (x >> bit) & 1 == 1 {
                    cnt += 1;
                }
            }
            ans = ans.max(cnt);
        }
        ans
    }
}
'''

FILES["2276_count_integers_in_intervals"] = r'''// LeetCode 2276 - Count Integers in Intervals
// https://leetcode.com/problems/count-integers-in-intervals/

struct SegNode {
    left: Option<Box<SegNode>>,
    right: Option<Box<SegNode>>,
    covered: bool,
}

impl SegNode {
    fn new() -> Self {
        Self {
            left: None,
            right: None,
            covered: false,
        }
    }
}

pub struct CountIntervals {
    root: Option<Box<SegNode>>,
    cnt: i32,
}

impl CountIntervals {
    pub fn new() -> Self {
        Self { root: None, cnt: 0 }
    }

    fn add_seg(l_bound: i32, r_bound: i32, l: i32, r: i32, node: &mut Option<Box<SegNode>>) -> i32 {
        if node.is_none() {
            *node = Some(Box::new(SegNode::new()));
        }
        let n = node.as_mut().unwrap();
        if n.covered {
            return 0;
        }
        if l <= l_bound && r_bound <= r {
            n.covered = true;
            n.left = None;
            n.right = None;
            return r_bound - l_bound + 1;
        }
        let mid = l_bound + (r_bound - l_bound) / 2;
        let mut added = 0;
        if l <= mid {
            added += Self::add_seg(l_bound, mid, l, r, &mut n.left);
        }
        if r > mid {
            added += Self::add_seg(mid + 1, r_bound, l, r, &mut n.right);
        }
        if n.left.as_ref().map(|x| x.covered).unwrap_or(false)
            && n.right.as_ref().map(|x| x.covered).unwrap_or(false)
        {
            n.covered = true;
            n.left = None;
            n.right = None;
        }
        added
    }

    pub fn add(&mut self, left: i32, right: i32) {
        self.cnt += Self::add_seg(1, 1_000_000_000, left, right, &mut self.root);
    }

    pub fn count(&self) -> i32 {
        self.cnt
    }
}
'''

FILES["2277_closest_node_to_path_in_tree"] = r'''// LeetCode 2277 - Closest Node to Path in Tree
// https://leetcode.com/problems/closest-node-to-path-in-tree/

impl Solution {
    pub fn closest_node(n: i32, edges: Vec<Vec<i32>>, query: Vec<Vec<i32>>) -> Vec<i32> {
        let n = n as usize;
        let mut g = vec![Vec::new(); n];
        for e in edges {
            g[e[0] as usize].push(e[1] as usize);
            g[e[1] as usize].push(e[0] as usize);
        }
        const LOG: usize = 17;
        let mut up = vec![vec![0usize; n]; LOG];
        let mut depth = vec![0i32; n];
        fn dfs(u: usize, p: usize, g: &[Vec<usize>], up: &mut [Vec<usize>], depth: &mut [i32]) {
            up[0][u] = p;
            for &v in &g[u] {
                if v != p {
                    depth[v] = depth[u] + 1;
                    dfs(v, u, g, up, depth);
                }
            }
        }
        dfs(0, 0, &g, &mut up, &mut depth);
        for k in 1..LOG {
            for v in 0..n {
                up[k][v] = up[k - 1][up[k - 1][v]];
            }
        }
        let lift = |mut v: usize, d: i32, up: &[Vec<usize>]| {
            for k in 0..LOG {
                if (d >> k) & 1 == 1 {
                    v = up[k][v];
                }
            }
            v
        };
        let lca = |mut a: usize, mut b: usize, up: &[Vec<usize>], depth: &[i32]| {
            if depth[a] < depth[b] {
                std::mem::swap(&mut a, &mut b);
            }
            a = lift(a, depth[a] - depth[b], up);
            if a == b {
                return a;
            }
            for k in (0..LOG).rev() {
                if up[k][a] != up[k][b] {
                    a = up[k][a];
                    b = up[k][b];
                }
            }
            up[0][a]
        };
        let dist = |a: usize, b: usize, up: &[Vec<usize>], depth: &[i32]| {
            let c = lca(a, b, up, depth);
            depth[a] + depth[b] - 2 * depth[c]
        };
        let mut ans = vec![0; query.len()];
        for (i, q) in query.iter().enumerate() {
            let a = q[0] as usize;
            let b = q[1] as usize;
            let x = q[2] as usize;
            let cands = [lca(a, b, &up, &depth), lca(a, x, &up, &depth), lca(b, x, &up, &depth)];
            let mut best = cands[0];
            let mut best_d = dist(cands[0], x, &up, &depth);
            for &t in &cands[1..] {
                let d = dist(t, x, &up, &depth);
                if d < best_d {
                    best_d = d;
                    best = t;
                }
            }
            ans[i] = best as i32;
        }
        ans
    }
}
'''

FILES["2278_percentage_of_letter_in_string"] = r'''// LeetCode 2278 - Percentage of Letter in String
// https://leetcode.com/problems/percentage-of-letter-in-string/

impl Solution {
    pub fn percentage_letter(s: String, letter: char) -> i32 {
        let cnt = s.chars().filter(|&c| c == letter).count() as i32;
        cnt * 100 / s.len() as i32
    }
}
'''

FILES["2279_maximum_bags_with_full_capacity_of_rocks"] = r'''// LeetCode 2279 - Maximum Bags With Full Capacity of Rocks
// https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/

impl Solution {
    pub fn maximum_bags(capacity: Vec<i32>, rocks: Vec<i32>, mut additional_rocks: i32) -> i32 {
        let mut need: Vec<i32> = capacity.iter().zip(rocks.iter()).map(|(c, r)| c - r).collect();
        need.sort_unstable();
        let mut ans = 0;
        for n in need {
            if additional_rocks < n {
                break;
            }
            additional_rocks -= n;
            ans += 1;
        }
        ans
    }
}
'''

FILES["2280_minimum_lines_to_represent_a_line_chart"] = r'''// LeetCode 2280 - Minimum Lines to Represent a Line Chart
// https://leetcode.com/problems/minimum-lines-to-represent-a-line-chart/

impl Solution {
    pub fn minimum_lines(mut stock_prices: Vec<Vec<i32>>) -> i32 {
        if stock_prices.len() <= 1 {
            return 0;
        }
        stock_prices.sort_unstable();
        let mut ans = 1;
        for i in 2..stock_prices.len() {
            let x0 = stock_prices[i - 2][0] as i64;
            let y0 = stock_prices[i - 2][1] as i64;
            let x1 = stock_prices[i - 1][0] as i64;
            let y1 = stock_prices[i - 1][1] as i64;
            let x2 = stock_prices[i][0] as i64;
            let y2 = stock_prices[i][1] as i64;
            if (y1 - y0) * (x2 - x1) != (y2 - y1) * (x1 - x0) {
                ans += 1;
            }
        }
        ans
    }
}
'''

FILES["2281_sum_of_total_strength_of_wizards"] = r'''// LeetCode 2281 - Sum of Total Strength of Wizards
// https://leetcode.com/problems/sum-of-total-strength-of-wizards/

impl Solution {
    pub fn total_strength(strength: Vec<i32>) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let n = strength.len();
        let mut left = vec![0i32; n];
        let mut right = vec![0i32; n];
        let mut stack: Vec<usize> = Vec::new();
        for i in 0..n {
            while !stack.is_empty() && strength[*stack.last().unwrap()] >= strength[i] {
                stack.pop();
            }
            left[i] = if stack.is_empty() { -1 } else { *stack.last().unwrap() as i32 };
            stack.push(i);
        }
        stack.clear();
        for i in (0..n).rev() {
            while !stack.is_empty() && strength[*stack.last().unwrap()] > strength[i] {
                stack.pop();
            }
            right[i] = if stack.is_empty() { n as i32 } else { *stack.last().unwrap() as i32 };
            stack.push(i);
        }
        let mut pref = vec![0i64; n + 1];
        for i in 0..n {
            pref[i + 1] = (pref[i] + strength[i] as i64) % MOD;
        }
        let mut pref_pref = vec![0i64; n + 2];
        for i in 0..=n {
            pref_pref[i + 1] = (pref_pref[i] + pref[i]) % MOD;
        }
        let mut ans = 0i64;
        for i in 0..n {
            let l = left[i] + 1;
            let r = right[i] - 1;
            let left_sum = (pref_pref[i + 1] - pref_pref[l as usize] + MOD) % MOD;
            let right_sum = (pref_pref[r as usize + 2] - pref_pref[i + 1] + MOD) % MOD;
            let left_cnt = i as i64 - l as i64 + 1;
            let right_cnt = r as i64 - i as i64 + 1;
            let contrib = (right_cnt * left_sum % MOD - left_cnt * right_sum % MOD + MOD) % MOD;
            ans = (ans + contrib * strength[i] as i64 % MOD) % MOD;
        }
        ans as i32
    }
}
'''

FILES["2282_number_of_people_that_can_be_seen_in_a_grid"] = r'''// LeetCode 2282 - Number of People That Can Be Seen in a Grid
// https://leetcode.com/problems/number-of-people-that-can-be-seen-in-a-grid/

impl Solution {
    pub fn see_people(heights: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let m = heights.len();
        let n = heights[0].len();
        let mut ans = vec![vec![0; n]; m];
        for i in 0..m {
            let mut stack: Vec<usize> = Vec::new();
            for j in (0..n).rev() {
                let mut cnt = 0;
                while !stack.is_empty() && heights[i][*stack.last().unwrap()] < heights[i][j] {
                    stack.pop();
                    cnt += 1;
                }
                if !stack.is_empty() {
                    cnt += 1;
                }
                ans[i][j] += cnt;
                while !stack.is_empty() && heights[i][*stack.last().unwrap()] == heights[i][j] {
                    stack.pop();
                }
                stack.push(j);
            }
        }
        for j in 0..n {
            let mut stack: Vec<usize> = Vec::new();
            for i in (0..m).rev() {
                let mut cnt = 0;
                while !stack.is_empty() && heights[*stack.last().unwrap()][j] < heights[i][j] {
                    stack.pop();
                    cnt += 1;
                }
                if !stack.is_empty() {
                    cnt += 1;
                }
                ans[i][j] += cnt;
                while !stack.is_empty() && heights[*stack.last().unwrap()][j] == heights[i][j] {
                    stack.pop();
                }
                stack.push(i);
            }
        }
        ans
    }
}
'''

FILES["2283_check_if_number_has_equal_digit_count_and_digit_value"] = r'''// LeetCode 2283 - Check if Number Has Equal Digit Count and Digit Value
// https://leetcode.com/problems/check-if-number-has-equal-digit-count-and-digit-value/

impl Solution {
    pub fn digit_count(num: String) -> bool {
        let bytes = num.as_bytes();
        let mut cnt = [0i32; 10];
        for &c in bytes {
            cnt[(c - b'0') as usize] += 1;
        }
        for (i, &c) in bytes.iter().enumerate() {
            if cnt[i] != (c - b'0') as i32 {
                return false;
            }
        }
        true
    }
}
'''

FILES["2284_sender_with_largest_word_count"] = r'''// LeetCode 2284 - Sender With Largest Word Count
// https://leetcode.com/problems/sender-with-largest-word-count/

use std::collections::HashMap;

impl Solution {
    pub fn largest_word_count(messages: Vec<String>, senders: Vec<String>) -> String {
        let mut count = HashMap::new();
        let mut best = String::new();
        let mut best_cnt = -1;
        for i in 0..messages.len() {
            let words = 1 + messages[i].bytes().filter(|&c| c == b' ').count() as i32;
            let c = count.entry(senders[i].clone()).or_insert(0);
            *c += words;
            let c = *c;
            if c > best_cnt || (c == best_cnt && senders[i] > best) {
                best_cnt = c;
                best = senders[i].clone();
            }
        }
        best
    }
}
'''

FILES["2285_maximum_total_importance_of_roads"] = r'''// LeetCode 2285 - Maximum Total Importance of Roads
// https://leetcode.com/problems/maximum-total-importance-of-roads/

impl Solution {
    pub fn maximum_importance(n: i32, roads: Vec<Vec<i32>>) -> i64 {
        let mut deg = vec![0i32; n as usize];
        for r in roads {
            deg[r[0] as usize] += 1;
            deg[r[1] as usize] += 1;
        }
        deg.sort_unstable();
        let mut ans = 0i64;
        for i in 0..n as usize {
            ans += deg[i] as i64 * (i as i64 + 1);
        }
        ans
    }
}
'''

FILES["2286_booking_concert_tickets_in_groups"] = r'''// LeetCode 2286 - Booking Concert Tickets in Groups
// https://leetcode.com/problems/booking-concert-tickets-in-groups/

#[derive(Clone, Copy, Default)]
struct Node {
    sum: i64,
    mx: i64,
}

pub struct BookMyShow {
    n: i32,
    m: i32,
    tree: Vec<Node>,
}

impl BookMyShow {
    fn pull(&mut self, idx: usize) {
        self.tree[idx].sum = self.tree[idx * 2].sum + self.tree[idx * 2 + 1].sum;
        self.tree[idx].mx = self.tree[idx * 2].mx.max(self.tree[idx * 2 + 1].mx);
    }

    fn build(&mut self, idx: usize, l: i32, r: i32) {
        if l == r {
            self.tree[idx] = Node {
                sum: self.m as i64,
                mx: self.m as i64,
            };
            return;
        }
        let mid = (l + r) / 2;
        self.build(idx * 2, l, mid);
        self.build(idx * 2 + 1, mid + 1, r);
        self.pull(idx);
    }

    fn update(&mut self, idx: usize, l: i32, r: i32, pos: i32, val: i64) {
        if l == r {
            self.tree[idx].sum = val;
            self.tree[idx].mx = val;
            return;
        }
        let mid = (l + r) / 2;
        if pos <= mid {
            self.update(idx * 2, l, mid, pos, val);
        } else {
            self.update(idx * 2 + 1, mid + 1, r, pos, val);
        }
        self.pull(idx);
    }

    fn query_sum(&self, idx: usize, l: i32, r: i32, ql: i32, qr: i32) -> i64 {
        if qr < l || r < ql {
            return 0;
        }
        if ql <= l && r <= qr {
            return self.tree[idx].sum;
        }
        let mid = (l + r) / 2;
        self.query_sum(idx * 2, l, mid, ql, qr) + self.query_sum(idx * 2 + 1, mid + 1, r, ql, qr)
    }

    fn find_first(&self, idx: usize, l: i32, r: i32, max_row: i32, k: i64) -> i32 {
        if l > max_row || self.tree[idx].mx < k {
            return -1;
        }
        if l == r {
            return l;
        }
        let mid = (l + r) / 2;
        let left = self.find_first(idx * 2, l, mid, max_row, k);
        if left != -1 {
            return left;
        }
        self.find_first(idx * 2 + 1, mid + 1, r, max_row, k)
    }

    pub fn new(n: i32, m: i32) -> Self {
        let mut this = Self {
            n,
            m,
            tree: vec![Node::default(); 4 * n as usize],
        };
        this.build(1, 0, n - 1);
        this
    }

    pub fn gather(&mut self, k: i32, max_row: i32) -> Vec<i32> {
        let row = self.find_first(1, 0, self.n - 1, max_row, k as i64);
        if row == -1 {
            return vec![];
        }
        let remain = self.query_sum(1, 0, self.n - 1, row, row);
        let seat = self.m as i64 - remain;
        self.update(1, 0, self.n - 1, row, remain - k as i64);
        vec![row, seat as i32]
    }

    pub fn scatter(&mut self, k: i32, max_row: i32) -> bool {
        if self.query_sum(1, 0, self.n - 1, 0, max_row) < k as i64 {
            return false;
        }
        let mut need = k as i64;
        let mut row = 0;
        while row <= max_row && need > 0 {
            let remain = self.query_sum(1, 0, self.n - 1, row, row);
            if remain != 0 {
                let take = remain.min(need);
                self.update(1, 0, self.n - 1, row, remain - take);
                need -= take;
            }
            row += 1;
        }
        true
    }
}
'''

FILES["2287_rearrange_characters_to_make_target_string"] = r'''// LeetCode 2287 - Rearrange Characters to Make Target String
// https://leetcode.com/problems/rearrange-characters-to-make-target-string/

impl Solution {
    pub fn rearrange_characters(s: String, target: String) -> i32 {
        let mut sc = [0i32; 26];
        let mut tc = [0i32; 26];
        for c in s.bytes() {
            sc[(c - b'a') as usize] += 1;
        }
        for c in target.bytes() {
            tc[(c - b'a') as usize] += 1;
        }
        let mut ans = i32::MAX;
        for i in 0..26 {
            if tc[i] == 0 {
                continue;
            }
            ans = ans.min(sc[i] / tc[i]);
        }
        ans
    }
}
'''

FILES["2288_apply_discount_to_prices"] = r'''// LeetCode 2288 - Apply Discount to Prices
// https://leetcode.com/problems/apply-discount-to-prices/

impl Solution {
    pub fn discount_prices(sentence: String, discount: i32) -> String {
        let mut parts: Vec<String> = sentence.split_whitespace().map(|s| s.to_string()).collect();
        for part in parts.iter_mut() {
            if part.len() >= 2 && part.starts_with('$') {
                let rest = &part[1..];
                if !rest.is_empty() && rest.bytes().all(|c| c.is_ascii_digit()) {
                    let val: i64 = rest.parse().unwrap();
                    let price = val as f64 * (100.0 - discount as f64) / 100.0;
                    *part = format!("${price:.2}");
                }
            }
        }
        parts.join(" ")
    }
}
'''

FILES["2289_steps_to_make_array_non_decreasing"] = r'''// LeetCode 2289 - Steps to Make Array Non-decreasing
// https://leetcode.com/problems/steps-to-make-array-non-decreasing/

impl Solution {
    pub fn total_steps(nums: Vec<i32>) -> i32 {
        let mut stack: Vec<(i32, i32)> = Vec::new();
        let mut ans = 0;
        for i in (0..nums.len()).rev() {
            let mut steps = 0;
            while !stack.is_empty() && nums[i] > stack.last().unwrap().0 {
                steps = steps.max(stack.last().unwrap().1);
                stack.pop();
                steps += 1;
            }
            ans = ans.max(steps);
            stack.push((nums[i], steps));
        }
        ans
    }
}
'''

FILES["2290_minimum_obstacle_removal_to_reach_corner"] = r'''// LeetCode 2290 - Minimum Obstacle Removal to Reach Corner
// https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/

use std::collections::VecDeque;

impl Solution {
    pub fn minimum_obstacles(grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        let mut dist = vec![vec![i32::MAX / 2; n]; m];
        dist[0][0] = 0;
        let mut dq = VecDeque::new();
        dq.push_back((0usize, 0usize));
        let dirs = [(1isize, 0), (-1, 0), (0, 1), (0, -1)];
        while let Some((r, c)) = dq.pop_front() {
            for &(dr, dc) in &dirs {
                let nr = r as isize + dr;
                let nc = c as isize + dc;
                if nr < 0 || nr >= m as isize || nc < 0 || nc >= n as isize {
                    continue;
                }
                let (nr, nc) = (nr as usize, nc as usize);
                let nd = dist[r][c] + grid[nr][nc];
                if nd < dist[nr][nc] {
                    dist[nr][nc] = nd;
                    if grid[nr][nc] == 0 {
                        dq.push_front((nr, nc));
                    } else {
                        dq.push_back((nr, nc));
                    }
                }
            }
        }
        dist[m - 1][n - 1]
    }
}
'''

FILES["2291_maximum_profit_from_trading_stocks"] = r'''// LeetCode 2291 - Maximum Profit From Trading Stocks
// https://leetcode.com/problems/maximum-profit-from-trading-stocks/

impl Solution {
    pub fn maximum_profit(present: Vec<i32>, future: Vec<i32>, budget: i32) -> i32 {
        let n = present.len();
        let budget = budget as usize;
        let mut dp = vec![0; budget + 1];
        for i in 0..n {
            let profit = future[i] - present[i];
            if profit <= 0 {
                continue;
            }
            let cost = present[i] as usize;
            for b in (cost..=budget).rev() {
                dp[b] = dp[b].max(dp[b - cost] + profit);
            }
        }
        dp[budget]
    }
}
'''

FILES["2293_min_max_game"] = r'''// LeetCode 2293 - Min Max Game
// https://leetcode.com/problems/min-max-game/

impl Solution {
    pub fn min_max_game(mut nums: Vec<i32>) -> i32 {
        while nums.len() > 1 {
            let next: Vec<i32> = (0..nums.len() / 2)
                .map(|i| {
                    if i % 2 == 0 {
                        nums[2 * i].min(nums[2 * i + 1])
                    } else {
                        nums[2 * i].max(nums[2 * i + 1])
                    }
                })
                .collect();
            nums = next;
        }
        nums[0]
    }
}
'''

FILES["2294_partition_array_such_that_maximum_difference_is_k"] = r'''// LeetCode 2294 - Partition Array Such That Maximum Difference Is K
// https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/

impl Solution {
    pub fn partition_array(mut nums: Vec<i32>, k: i32) -> i32 {
        nums.sort_unstable();
        let mut ans = 1;
        let mut start = nums[0];
        for &x in nums.iter().skip(1) {
            if x - start > k {
                ans += 1;
                start = x;
            }
        }
        ans
    }
}
'''

FILES["2295_replace_elements_in_an_array"] = r'''// LeetCode 2295 - Replace Elements in an Array
// https://leetcode.com/problems/replace-elements-in-an-array/

use std::collections::HashMap;

impl Solution {
    pub fn array_change(mut nums: Vec<i32>, operations: Vec<Vec<i32>>) -> Vec<i32> {
        let mut pos = HashMap::new();
        for (i, &x) in nums.iter().enumerate() {
            pos.insert(x, i);
        }
        for op in operations {
            let i = pos[&op[0]];
            nums[i] = op[1];
            pos.remove(&op[0]);
            pos.insert(op[1], i);
        }
        nums
    }
}
'''

FILES["2296_design_a_text_editor"] = r'''// LeetCode 2296 - Design a Text Editor
// https://leetcode.com/problems/design-a-text-editor/

pub struct TextEditor {
    left: Vec<char>,
    right: Vec<char>,
}

impl TextEditor {
    pub fn new() -> Self {
        Self {
            left: Vec::new(),
            right: Vec::new(),
        }
    }

    fn suffix(&self) -> String {
        let start = self.left.len().saturating_sub(10);
        self.left[start..].iter().collect()
    }

    pub fn add_text(&mut self, text: String) {
        self.left.extend(text.chars());
    }

    pub fn delete_text(&mut self, mut k: i32) -> i32 {
        let mut deleted = 0;
        while k > 0 && !self.left.is_empty() {
            self.left.pop();
            k -= 1;
            deleted += 1;
        }
        deleted
    }

    pub fn cursor_left(&mut self, mut k: i32) -> String {
        while k > 0 && !self.left.is_empty() {
            let c = self.left.pop().unwrap();
            self.right.push(c);
            k -= 1;
        }
        self.suffix()
    }

    pub fn cursor_right(&mut self, mut k: i32) -> String {
        while k > 0 && !self.right.is_empty() {
            let c = self.right.pop().unwrap();
            self.left.push(c);
            k -= 1;
        }
        self.suffix()
    }
}
'''

FILES["2297_jump_game_viii"] = r'''// LeetCode 2297 - Jump Game VIII
// https://leetcode.com/problems/jump-game-viii/

impl Solution {
    pub fn min_cost(nums: Vec<i32>, costs: Vec<i32>) -> i64 {
        let n = nums.len();
        let mut dp = vec![i64::MAX / 4; n];
        dp[0] = 0;
        let mut stack1: Vec<usize> = Vec::new();
        let mut stack2: Vec<usize> = Vec::new();
        for i in 0..n {
            while !stack1.is_empty() && nums[*stack1.last().unwrap()] <= nums[i] {
                let j = stack1.pop().unwrap();
                dp[i] = dp[i].min(dp[j] + costs[i] as i64);
            }
            while !stack2.is_empty() && nums[*stack2.last().unwrap()] > nums[i] {
                let j = stack2.pop().unwrap();
                dp[i] = dp[i].min(dp[j] + costs[i] as i64);
            }
            if let Some(&j) = stack1.last() {
                dp[i] = dp[i].min(dp[j] + costs[i] as i64);
            }
            if let Some(&j) = stack2.last() {
                dp[i] = dp[i].min(dp[j] + costs[i] as i64);
            }
            stack1.push(i);
            stack2.push(i);
        }
        dp[n - 1]
    }
}
'''

FILES["2299_strong_password_checker_ii"] = r'''// LeetCode 2299 - Strong Password Checker II
// https://leetcode.com/problems/strong-password-checker-ii/

impl Solution {
    pub fn strong_password_checker_ii(password: String) -> bool {
        if password.len() < 8 {
            return false;
        }
        let special = "!@#$%^&*()-+";
        let mut has_lower = false;
        let mut has_upper = false;
        let mut has_digit = false;
        let mut has_special = false;
        let bytes = password.as_bytes();
        for i in 0..bytes.len() {
            let c = bytes[i] as char;
            if i > 0 && c == bytes[i - 1] as char {
                return false;
            }
            if c.is_ascii_lowercase() {
                has_lower = true;
            } else if c.is_ascii_uppercase() {
                has_upper = true;
            } else if c.is_ascii_digit() {
                has_digit = true;
            } else if special.contains(c) {
                has_special = true;
            }
        }
        has_lower && has_upper && has_digit && has_special
    }
}
'''

FILES["2300_successful_pairs_of_spells_and_potions"] = r'''// LeetCode 2300 - Successful Pairs of Spells and Potions
// https://leetcode.com/problems/successful-pairs-of-spells-and-potions/

impl Solution {
    pub fn successful_pairs(spells: Vec<i32>, mut potions: Vec<i32>, success: i64) -> Vec<i32> {
        potions.sort_unstable();
        let m = potions.len();
        let mut ans = vec![0; spells.len()];
        for (i, &spell) in spells.iter().enumerate() {
            let mut lo = 0;
            let mut hi = m;
            while lo < hi {
                let mid = (lo + hi) / 2;
                if spell as i64 * potions[mid] as i64 >= success {
                    hi = mid;
                } else {
                    lo = mid + 1;
                }
            }
            ans[i] = (m - lo) as i32;
        }
        ans
    }
}
'''

FILES["2301_match_substring_after_replacement"] = r'''// LeetCode 2301 - Match Substring After Replacement
// https://leetcode.com/problems/match-substring-after-replacement/

use std::collections::HashSet;

impl Solution {
    pub fn match_replacement(s: String, sub: String, mappings: Vec<Vec<char>>) -> bool {
        let mut allow = HashSet::new();
        for m in mappings {
            allow.insert(((m[0] as u32) << 8) | (m[1] as u32));
        }
        let s = s.as_bytes();
        let sub = sub.as_bytes();
        let n = s.len();
        let mlen = sub.len();
        for i in 0..=n.saturating_sub(mlen) {
            let mut ok = true;
            for j in 0..mlen {
                let a = s[i + j] as char;
                let b = sub[j] as char;
                if a == b || allow.contains(&(((b as u32) << 8) | (a as u32))) {
                    continue;
                }
                ok = false;
                break;
            }
            if ok {
                return true;
            }
        }
        false
    }
}
'''

written = 0
for folder, content in FILES.items():
    path = ROOT / folder / "solution.rs"
    path.write_text(content, encoding="utf-8", newline="\n")
    written += 1
print(f"wrote {written}")

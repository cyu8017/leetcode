#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
FILES = {}

FILES["3227_vowels_game_in_a_string"] = r'''// LeetCode 3227 - Vowels Game in a String
// https://leetcode.com/problems/vowels-game-in-a-string/

impl Solution {
    pub fn does_alice_win(s: String) -> bool {
        s.chars().any(|c| matches!(c, 'a' | 'e' | 'i' | 'o' | 'u'))
    }
}
'''

FILES["3228_maximum_number_of_operations_to_move_ones_to_the_end"] = r'''// LeetCode 3228 - Maximum Number of Operations to Move Ones to the End
// https://leetcode.com/problems/maximum-number-of-operations-to-move-ones-to-the-end/

impl Solution {
    pub fn max_operations(s: String) -> i32 {
        let b = s.as_bytes();
        let mut ans = 0;
        let mut cnt = 0;
        for i in 0..b.len() {
            if b[i] == b'1' {
                cnt += 1;
            } else if i > 0 && b[i - 1] == b'1' {
                ans += cnt;
            }
        }
        ans
    }
}
'''

FILES["3229_minimum_operations_to_make_array_equal_to_target"] = r'''// LeetCode 3229 - Minimum Operations to Make Array Equal to Target
// https://leetcode.com/problems/minimum-operations-to-make-array-equal-to-target/

impl Solution {
    pub fn minimum_operations(nums: Vec<i32>, target: Vec<i32>) -> i64 {
        let absv = |x: i32| if x < 0 { -x } else { x };
        let mut f = absv(target[0] - nums[0]) as i64;
        for i in 1..target.len() {
            let x = target[i] - nums[i];
            let y = target[i - 1] - nums[i - 1];
            if x as i64 * y as i64 > 0 {
                let d = absv(x) - absv(y);
                if d > 0 {
                    f += d as i64;
                }
            } else {
                f += absv(x) as i64;
            }
        }
        f
    }
}
'''

FILES["3231_minimum_number_of_increasing_subsequence_to_be_removed"] = r'''// LeetCode 3231 - Minimum Number of Increasing Subsequence to Be Removed
// https://leetcode.com/problems/minimum-number-of-increasing-subsequence-to-be-removed/

impl Solution {
    pub fn min_operations(nums: Vec<i32>) -> i32 {
        let mut g = Vec::new();
        for x in nums {
            let mut l = 0;
            let mut r = g.len();
            while l < r {
                let mid = (l + r) >> 1;
                if g[mid] < x {
                    r = mid;
                } else {
                    l = mid + 1;
                }
            }
            if l == g.len() {
                g.push(x);
            } else {
                g[l] = x;
            }
        }
        g.len() as i32
    }
}
'''

FILES["3232_find_if_digit_game_can_be_won"] = r'''// LeetCode 3232 - Find if Digit Game Can Be Won
// https://leetcode.com/problems/find-if-digit-game-can-be-won/

impl Solution {
    pub fn can_alice_win(nums: Vec<i32>) -> bool {
        let mut a = 0;
        let mut b = 0;
        for x in nums {
            if x < 10 {
                a += x;
            } else {
                b += x;
            }
        }
        a != b
    }
}
'''

FILES["3233_find_the_count_of_numbers_which_are_not_special"] = r'''// LeetCode 3233 - Find the Count of Numbers Which Are Not Special
// https://leetcode.com/problems/find-the-count-of-numbers-which-are-not-special/

impl Solution {
    pub fn non_special_count(l: i32, r: i32) -> i32 {
        const M: usize = 31623;
        let mut primes = vec![true; M + 1];
        primes[0] = false;
        primes[1] = false;
        for i in 2..=M {
            if primes[i] {
                let mut j = i * 2;
                while j <= M {
                    primes[j] = false;
                    j += i;
                }
            }
        }
        let lo = (l as f64).sqrt().ceil() as i32;
        let hi = (r as f64).sqrt().floor() as i32;
        let mut cnt = 0;
        for i in lo..=hi {
            if primes[i as usize] {
                cnt += 1;
            }
        }
        r - l + 1 - cnt
    }
}
'''

FILES["3234_count_the_number_of_substrings_with_dominant_ones"] = r'''// LeetCode 3234 - Count the Number of Substrings With Dominant Ones
// https://leetcode.com/problems/count-the-number-of-substrings-with-dominant-ones/

impl Solution {
    pub fn number_of_substrings(s: String) -> i32 {
        let b = s.as_bytes();
        let n = b.len();
        let mut nxt = vec![0; n + 1];
        nxt[n] = n;
        for i in (0..n).rev() {
            nxt[i] = nxt[i + 1];
            if b[i] == b'0' {
                nxt[i] = i;
            }
        }
        let mut ans = 0;
        for i in 0..n {
            let mut cnt0 = if b[i] == b'0' { 1 } else { 0 };
            let mut j = i;
            while j < n && (cnt0 as i64) * (cnt0 as i64) <= n as i64 {
                let cnt1 = nxt[j + 1] as i32 - i as i32 - cnt0;
                if cnt1 >= cnt0 * cnt0 {
                    ans += (nxt[j + 1] as i32 - j as i32).min(cnt1 - cnt0 * cnt0 + 1);
                }
                j = nxt[j + 1];
                cnt0 += 1;
            }
        }
        ans
    }
}
'''

FILES["3235_check_if_the_rectangle_corner_is_reachable"] = r'''// LeetCode 3235 - Check if the Rectangle Corner Is Reachable
// https://leetcode.com/problems/check-if-the-rectangle-corner-is-reachable/

impl Solution {
    pub fn can_reach_corner(x_corner: i32, y_corner: i32, circles: Vec<Vec<i32>>) -> bool {
        let in_circle = |x: i32, y: i32, cx: i32, cy: i32, r: i32| {
            let dx = x as i64 - cx as i64;
            let dy = y as i64 - cy as i64;
            dx * dx + dy * dy <= r as i64 * r as i64
        };
        let cross_left_top = |cx: i32, cy: i32, r: i32| {
            let a = cx.abs() <= r && cy >= 0 && cy <= y_corner;
            let b = (cy - y_corner).abs() <= r && cx >= 0 && cx <= x_corner;
            a || b
        };
        let cross_right_bottom = |cx: i32, cy: i32, r: i32| {
            let a = (cx - x_corner).abs() <= r && cy >= 0 && cy <= y_corner;
            let b = cy.abs() <= r && cx >= 0 && cx <= x_corner;
            a || b
        };
        let n = circles.len();
        let mut vis = vec![false; n];
        fn dfs(
            i: usize,
            circles: &[Vec<i32>],
            vis: &mut [bool],
            x_corner: i32,
            y_corner: i32,
            cross_right_bottom: &dyn Fn(i32, i32, i32) -> bool,
        ) -> bool {
            let x1 = circles[i][0];
            let y1 = circles[i][1];
            let r1 = circles[i][2];
            if cross_right_bottom(x1, y1, r1) {
                return true;
            }
            vis[i] = true;
            for j in 0..circles.len() {
                if vis[j] {
                    continue;
                }
                let x2 = circles[j][0];
                let y2 = circles[j][1];
                let r2 = circles[j][2];
                if (x1 as i64 - x2 as i64) * (x1 as i64 - x2 as i64)
                    + (y1 as i64 - y2 as i64) * (y1 as i64 - y2 as i64)
                    > (r1 as i64 + r2 as i64) * (r1 as i64 + r2 as i64)
                {
                    continue;
                }
                if x1 as i64 * r2 as i64 + x2 as i64 * r1 as i64 < (r1 as i64 + r2 as i64) * x_corner as i64
                    && y1 as i64 * r2 as i64 + y2 as i64 * r1 as i64
                        < (r1 as i64 + r2 as i64) * y_corner as i64
                    && dfs(j, circles, vis, x_corner, y_corner, cross_right_bottom)
                {
                    return true;
                }
            }
            false
        }
        for i in 0..n {
            let x = circles[i][0];
            let y = circles[i][1];
            let r = circles[i][2];
            if in_circle(0, 0, x, y, r) || in_circle(x_corner, y_corner, x, y, r) {
                return false;
            }
            if !vis[i] && cross_left_top(x, y, r)
                && dfs(i, &circles, &mut vis, x_corner, y_corner, &cross_right_bottom)
            {
                return false;
            }
        }
        true
    }
}
'''

FILES["3237_alt_and_tab_simulation"] = r'''// LeetCode 3237 - Alt and Tab Simulation
// https://leetcode.com/problems/alt-and-tab-simulation/

impl Solution {
    pub fn simulation_result(windows: Vec<i32>, queries: Vec<i32>) -> Vec<i32> {
        let n = windows.len();
        let mut s = vec![false; n + 1];
        let mut ans = Vec::new();
        for &q in queries.iter().rev() {
            if !s[q as usize] {
                s[q as usize] = true;
                ans.push(q);
            }
        }
        for w in windows {
            if !s[w as usize] {
                ans.push(w);
            }
        }
        ans
    }
}
'''

FILES["3238_find_the_number_of_winning_players"] = r'''// LeetCode 3238 - Find the Number of Winning Players
// https://leetcode.com/problems/find-the-number-of-winning-players/

use std::collections::HashSet;

impl Solution {
    pub fn winning_player_count(n: i32, pick: Vec<Vec<i32>>) -> i32 {
        let mut cnt = vec![[0; 11]; n as usize];
        let mut s = HashSet::new();
        for p in pick {
            let x = p[0] as usize;
            let y = p[1] as usize;
            cnt[x][y] += 1;
            if cnt[x][y] > x as i32 {
                s.insert(x);
            }
        }
        s.len() as i32
    }
}
'''

FILES["3239_minimum_number_of_flips_to_make_binary_grid_palindromic_i"] = r'''// LeetCode 3239 - Minimum Number of Flips to Make Binary Grid Palindromic I
// https://leetcode.com/problems/minimum-number-of-flips-to-make-binary-grid-palindromic-i/

impl Solution {
    pub fn min_flips(grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        let mut cnt1 = 0;
        let mut cnt2 = 0;
        for row in &grid {
            for j in 0..n / 2 {
                if row[j] != row[n - j - 1] {
                    cnt1 += 1;
                }
            }
        }
        for j in 0..n {
            for i in 0..m / 2 {
                if grid[i][j] != grid[m - i - 1][j] {
                    cnt2 += 1;
                }
            }
        }
        cnt1.min(cnt2)
    }
}
'''

FILES["3240_minimum_number_of_flips_to_make_binary_grid_palindromic_ii"] = r'''// LeetCode 3240 - Minimum Number of Flips to Make Binary Grid Palindromic II
// https://leetcode.com/problems/minimum-number-of-flips-to-make-binary-grid-palindromic-ii/

impl Solution {
    pub fn min_flips(grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        let mut ans = 0;
        for i in 0..m / 2 {
            for j in 0..n / 2 {
                let x = m - i - 1;
                let y = n - j - 1;
                let cnt1 = grid[i][j] + grid[x][j] + grid[i][y] + grid[x][y];
                ans += cnt1.min(4 - cnt1);
            }
        }
        if m % 2 == 1 && n % 2 == 1 {
            ans += grid[m / 2][n / 2];
        }
        let mut diff = 0;
        let mut cnt1 = 0;
        if m % 2 == 1 {
            for j in 0..n / 2 {
                if grid[m / 2][j] == grid[m / 2][n - j - 1] {
                    cnt1 += grid[m / 2][j] * 2;
                } else {
                    diff += 1;
                }
            }
        }
        if n % 2 == 1 {
            for i in 0..m / 2 {
                if grid[i][n / 2] == grid[m - i - 1][n / 2] {
                    cnt1 += grid[i][n / 2] * 2;
                } else {
                    diff += 1;
                }
            }
        }
        if cnt1 % 4 == 0 || diff > 0 {
            ans += diff;
        } else {
            ans += 2;
        }
        ans
    }
}
'''

FILES["3241_time_taken_to_mark_all_nodes"] = r'''// LeetCode 3241 - Time Taken to Mark All Nodes
// https://leetcode.com/problems/time-taken-to-mark-all-nodes/

impl Solution {
    pub fn time_taken(edges: Vec<Vec<i32>>) -> Vec<i32> {
        let n = edges.len() + 1;
        let mut ans = vec![0; n];
        let mut tree = vec![Vec::new(); n];
        let mut dp = vec![[(0, 0), (0, 0)]; n];
        for e in &edges {
            tree[e[0] as usize].push(e[1] as usize);
            tree[e[1] as usize].push(e[0] as usize);
        }
        let get_time = |u: usize| if u % 2 == 0 { 2 } else { 1 };
        fn dfs(u: usize, prev: i32, tree: &[Vec<usize>], dp: &mut [([(i32, i32); 2])]) -> i32 {
            let mut t1 = (0, 0);
            let mut t2 = (0, 0);
            for &v in &tree[u] {
                if v as i32 == prev {
                    continue;
                }
                let t = dfs(v, u as i32, tree, dp) + if v % 2 == 0 { 2 } else { 1 };
                if t >= t1.1 {
                    t2 = t1;
                    t1 = (v as i32, t);
                } else if t > t2.1 {
                    t2 = (v as i32, t);
                }
            }
            dp[u] = [t1, t2];
            t1.1
        }
        fn reroot(
            u: usize,
            prev: i32,
            max_time: i32,
            tree: &[Vec<usize>],
            dp: &[[(i32, i32); 2]],
            ans: &mut [i32],
        ) {
            ans[u] = max_time.max(dp[u][0].1);
            for &v in &tree[u] {
                if v as i32 == prev {
                    continue;
                }
                let side = if dp[u][0].0 == v as i32 { dp[u][1].1 } else { dp[u][0].1 };
                let new_max = max_time.max(side);
                let gt = if u % 2 == 0 { 2 } else { 1 };
                reroot(v, u as i32, gt + new_max, tree, dp, ans);
            }
        }
        dfs(0, -1, &tree, &mut dp);
        reroot(0, -1, 0, &tree, &dp, &mut ans);
        let _ = get_time;
        ans
    }
}
'''

FILES["3242_design_neighbor_sum_service"] = r'''// LeetCode 3242 - Design Neighbor Sum Service
// https://leetcode.com/problems/design-neighbor-sum-service/

use std::collections::HashMap;

pub struct NeighborSum {
    grid: Vec<Vec<i32>>,
    d: HashMap<i32, (i32, i32)>,
}

impl NeighborSum {
    pub fn new(grid: Vec<Vec<i32>>) -> Self {
        let mut d = HashMap::new();
        for i in 0..grid.len() {
            for j in 0..grid[i].len() {
                d.insert(grid[i][j], (i as i32, j as i32));
            }
        }
        Self { grid, d }
    }

    fn cal(&self, value: i32, k: usize) -> i32 {
        let dirs = [[-1, 0, 1, 0, -1], [-1, 1, 1, -1, -1]];
        let p = self.d[&value];
        let mut s = 0;
        for q in 0..4 {
            let x = p.0 + dirs[k][q];
            let y = p.1 + dirs[k][q + 1];
            if x >= 0 && x < self.grid.len() as i32 && y >= 0 && y < self.grid[0].len() as i32 {
                s += self.grid[x as usize][y as usize];
            }
        }
        s
    }

    pub fn adjacent_sum(&self, value: i32) -> i32 {
        self.cal(value, 0)
    }

    pub fn diagonal_sum(&self, value: i32) -> i32 {
        self.cal(value, 1)
    }
}
'''

FILES["3243_shortest_distance_after_road_addition_queries_i"] = r'''// LeetCode 3243 - Shortest Distance After Road Addition Queries I
// https://leetcode.com/problems/shortest-distance-after-road-addition-queries-i/

use std::collections::VecDeque;

impl Solution {
    pub fn shortest_distance_after_queries(n: i32, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let n = n as usize;
        let mut g = vec![Vec::new(); n];
        for i in 0..n - 1 {
            g[i].push(i + 1);
        }
        let bfs = |g: &[Vec<usize>]| -> i32 {
            let mut q = VecDeque::new();
            q.push_back(0);
            let mut vis = vec![false; n];
            vis[0] = true;
            let mut d = 0;
            loop {
                let k = q.len();
                for _ in 0..k {
                    let u = q.pop_front().unwrap();
                    if u == n - 1 {
                        return d;
                    }
                    for &v in &g[u] {
                        if !vis[v] {
                            vis[v] = true;
                            q.push_back(v);
                        }
                    }
                }
                d += 1;
            }
        };
        let mut ans = vec![0; queries.len()];
        for (i, q) in queries.iter().enumerate() {
            g[q[0] as usize].push(q[1] as usize);
            ans[i] = bfs(&g);
        }
        ans
    }
}
'''

FILES["3244_shortest_distance_after_road_addition_queries_ii"] = r'''// LeetCode 3244 - Shortest Distance After Road Addition Queries II
// https://leetcode.com/problems/shortest-distance-after-road-addition-queries-ii/

impl Solution {
    pub fn shortest_distance_after_queries(n: i32, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let n = n as usize;
        let mut nxt: Vec<i32> = (1..n as i32).collect();
        let mut cnt = n as i32 - 1;
        let mut ans = Vec::new();
        for q in queries {
            let u = q[0] as usize;
            let v = q[1];
            if nxt[u] > 0 && nxt[u] < v {
                let mut i = nxt[u];
                while i < v {
                    cnt -= 1;
                    let ni = nxt[i as usize];
                    nxt[i as usize] = 0;
                    i = ni;
                }
                nxt[u] = v;
            }
            ans.push(cnt);
        }
        ans
    }
}
'''

FILES["3245_alternating_groups_iii"] = r'''// LeetCode 3245 - Alternating Groups III
// https://leetcode.com/problems/alternating-groups-iii/

use std::collections::BTreeSet;

struct SegTree {
    n: usize,
    tree_interval_counts: Vec<i32>,
    tree_interval_lengths: Vec<i32>,
}

impl SegTree {
    fn new(n: usize) -> Self {
        Self {
            n,
            tree_interval_counts: vec![0; 4 * n],
            tree_interval_lengths: vec![0; 4 * n],
        }
    }
    fn add(&mut self, i: i32, val: i32) {
        self.add_rec(0, 0, self.n as i32 - 1, i, val);
    }
    fn add_rec(&mut self, tree_index: usize, lo: i32, hi: i32, i: i32, val: i32) {
        if lo == hi {
            self.tree_interval_counts[tree_index] += val;
            self.tree_interval_lengths[tree_index] = self.tree_interval_counts[tree_index] * i;
            return;
        }
        let mid = (lo + hi) / 2;
        if i <= mid {
            self.add_rec(2 * tree_index + 1, lo, mid, i, val);
        } else {
            self.add_rec(2 * tree_index + 2, mid + 1, hi, i, val);
        }
        self.tree_interval_counts[tree_index] =
            self.tree_interval_counts[2 * tree_index + 1] + self.tree_interval_counts[2 * tree_index + 2];
        self.tree_interval_lengths[tree_index] =
            self.tree_interval_lengths[2 * tree_index + 1] + self.tree_interval_lengths[2 * tree_index + 2];
    }
    fn query_interval_counts(&self, i: i32) -> i32 {
        self.query(&self.tree_interval_counts, 0, 0, self.n as i32 - 1, i, self.n as i32 - 1)
    }
    fn query_interval_lengths(&self, i: i32) -> i32 {
        self.query(&self.tree_interval_lengths, 0, 0, self.n as i32 - 1, i, self.n as i32 - 1)
    }
    fn query(&self, tree: &[i32], tree_index: usize, lo: i32, hi: i32, i: i32, j: i32) -> i32 {
        if i <= lo && hi <= j {
            return tree[tree_index];
        }
        if j < lo || hi < i {
            return 0;
        }
        let mid = (lo + hi) / 2;
        self.query(tree, tree_index * 2 + 1, lo, mid, i, j)
            + self.query(tree, tree_index * 2 + 2, mid + 1, hi, i, j)
    }
}

impl Solution {
    pub fn number_of_alternating_groups(colors: Vec<i32>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let n = colors.len();
        let mut ans = Vec::new();
        let mut arr = colors.clone();
        arr.extend_from_slice(&colors[..n - 1]);
        let mut tree = SegTree::new(2 * n - 1);
        let mut intervals: BTreeSet<(i32, i32)> = BTreeSet::new();

        let insert = |intervals: &mut BTreeSet<(i32, i32)>, tree: &mut SegTree, l: i32, r: i32, n: usize| {
            intervals.insert((l, r));
            if l < n as i32 {
                tree.add(r - l + 1, 1);
            }
        };
        let remove = |intervals: &mut BTreeSet<(i32, i32)>, tree: &mut SegTree, l: i32, r: i32, n: usize| {
            intervals.remove(&(l, r));
            if l < n as i32 {
                tree.add(r - l + 1, -1);
            }
        };
        let find_interval = |intervals: &BTreeSet<(i32, i32)>, target: i32| -> (i32, i32) {
            let mut best_l = -1;
            let mut best_r = -1;
            for &(l, r) in intervals {
                if l <= target && target <= r && l > best_l {
                    best_l = l;
                    best_r = r;
                }
            }
            (best_l, best_r)
        };

        let mut start = 0i32;
        for i in 1..(2 * n - 1) as i32 {
            if arr[i as usize] == arr[(i - 1) as usize] {
                insert(&mut intervals, &mut tree, start, i - 1, n);
                start = i;
            }
        }
        insert(&mut intervals, &mut tree, start, (2 * n - 2) as i32, n);

        for query in queries {
            if query[0] == 1 {
                let sz = query[1];
                let num_intervals = tree.query_interval_counts(sz);
                let sum_intervals = tree.query_interval_lengths(sz);
                let mut num_alternating_groups = sum_intervals - num_intervals * sz + num_intervals;
                let (l, r) = find_interval(&intervals, n as i32);
                if !(l < 0 || l >= n as i32 || r - l + 1 < sz) && r >= n as i32 {
                    let non_duplicate_groups = n as i32 - l;
                    let num_groups = (r - l + 1) - sz + 1;
                    let extra = num_groups - non_duplicate_groups;
                    if extra > 0 {
                        num_alternating_groups -= extra;
                    }
                }
                ans.push(num_alternating_groups);
            } else {
                let index = query[1];
                let color = query[2];
                if arr[index as usize] != color {
                    for &idx in &[index, if index < n as i32 - 1 { index + n as i32 } else { -1 }] {
                        if idx < 0 {
                            continue;
                        }
                        if arr[idx as usize] == color {
                            continue;
                        }
                        arr[idx as usize] = color;
                        let (start, end) = find_interval(&intervals, idx);
                        remove(&mut intervals, &mut tree, start, end, n);
                        if start < idx && idx < end {
                            insert(&mut intervals, &mut tree, start, idx - 1, n);
                            insert(&mut intervals, &mut tree, idx, idx, n);
                            insert(&mut intervals, &mut tree, idx + 1, end, n);
                            continue;
                        }
                        if start == idx && idx < end {
                            insert(&mut intervals, &mut tree, start + 1, end, n);
                        }
                        if start < idx && idx == end {
                            insert(&mut intervals, &mut tree, start, end - 1, n);
                        }
                        let mut ns = idx;
                        let mut ne = idx;
                        loop {
                            let mut merged = false;
                            let keys: Vec<(i32, i32)> = intervals.iter().copied().collect();
                            for (a, b) in keys {
                                if b + 1 == ns && arr[b as usize] != arr[ns as usize] {
                                    remove(&mut intervals, &mut tree, a, b, n);
                                    ns = a;
                                    merged = true;
                                    break;
                                }
                            }
                            if !merged {
                                break;
                            }
                        }
                        loop {
                            let mut merged = false;
                            let keys: Vec<(i32, i32)> = intervals.iter().copied().collect();
                            for (a, b) in keys {
                                if a == ne + 1 && arr[a as usize] != arr[ne as usize] {
                                    remove(&mut intervals, &mut tree, a, b, n);
                                    ne = b;
                                    merged = true;
                                    break;
                                }
                            }
                            if !merged {
                                break;
                            }
                        }
                        insert(&mut intervals, &mut tree, ns, ne, n);
                    }
                }
            }
        }
        ans
    }
}
'''

FILES["3247_number_of_subsequences_with_odd_sum"] = r'''// LeetCode 3247 - Number of Subsequences with Odd Sum
// https://leetcode.com/problems/number-of-subsequences-with-odd-sum/

impl Solution {
    pub fn subsequence_count(nums: Vec<i32>) -> i32 {
        const MOD: i32 = 1_000_000_007;
        let mut f = [0, 0];
        for x in nums {
            let mut g = [0, 0];
            if x % 2 == 1 {
                g[0] = (f[0] + f[1]) % MOD;
                g[1] = (f[0] + f[1] + 1) % MOD;
            } else {
                g[0] = (f[0] + f[0] + 1) % MOD;
                g[1] = (f[1] + f[1]) % MOD;
            }
            f = g;
        }
        f[1]
    }
}
'''

FILES["3248_snake_in_matrix"] = r'''// LeetCode 3248 - Snake in Matrix
// https://leetcode.com/problems/snake-in-matrix/

impl Solution {
    pub fn final_position_of_snake(n: i32, commands: Vec<String>) -> i32 {
        let mut x = 0;
        let mut y = 0;
        for c in commands {
            match c.as_bytes()[0] {
                b'U' => x -= 1,
                b'D' => x += 1,
                b'L' => y -= 1,
                b'R' => y += 1,
                _ => {}
            }
        }
        x * n + y
    }
}
'''

FILES["3249_count_the_number_of_good_nodes"] = r'''// LeetCode 3249 - Count the Number of Good Nodes
// https://leetcode.com/problems/count-the-number-of-good-nodes/

impl Solution {
    pub fn count_good_nodes(edges: Vec<Vec<i32>>) -> i32 {
        let n = edges.len() + 1;
        let mut g = vec![Vec::new(); n];
        for e in &edges {
            g[e[0] as usize].push(e[1] as usize);
            g[e[1] as usize].push(e[0] as usize);
        }
        let mut ans = 0;
        fn dfs(a: usize, fa: i32, g: &[Vec<usize>], ans: &mut i32) -> i32 {
            let mut pre = -1;
            let mut cnt = 1;
            let mut ok = 1;
            for &b in &g[a] {
                if b as i32 != fa {
                    let cur = dfs(b, a as i32, g, ans);
                    cnt += cur;
                    if pre < 0 {
                        pre = cur;
                    } else if pre != cur {
                        ok = 0;
                    }
                }
            }
            *ans += ok;
            cnt
        }
        dfs(0, -1, &g, &mut ans);
        ans
    }
}
'''

FILES["3250_find_the_count_of_monotonic_pairs_i"] = r'''// LeetCode 3250 - Find the Count of Monotonic Pairs I
// https://leetcode.com/problems/find-the-count-of-monotonic-pairs-i/

impl Solution {
    pub fn count_of_pairs(nums: Vec<i32>) -> i32 {
        const MOD: i32 = 1_000_000_007;
        let n = nums.len();
        let mut dp = vec![0; 51];
        for a in 0..=nums[0] as usize {
            dp[a] = 1;
        }
        for i in 1..n {
            let mut ndp = vec![0; 51];
            let mut pref = vec![0; 52];
            for a in 0..=50 {
                pref[a + 1] = (pref[a] + dp[a]) % MOD;
            }
            for a2 in 0..=nums[i] as usize {
                let b2 = nums[i] - a2 as i32;
                let mut max_a1 = a2 as i32;
                let lim = nums[i - 1] - b2;
                if lim < max_a1 {
                    max_a1 = lim;
                }
                if max_a1 < 0 {
                    continue;
                }
                if max_a1 > 50 {
                    max_a1 = 50;
                }
                ndp[a2] = pref[(max_a1 + 1) as usize];
            }
            dp = ndp;
        }
        let mut ans = 0;
        for v in dp {
            ans = (ans + v) % MOD;
        }
        ans
    }
}
'''

FILES["3251_find_the_count_of_monotonic_pairs_ii"] = r'''// LeetCode 3251 - Find the Count of Monotonic Pairs II
// https://leetcode.com/problems/find-the-count-of-monotonic-pairs-ii/

impl Solution {
    pub fn count_of_pairs(nums: Vec<i32>) -> i32 {
        const MOD: i32 = 1_000_000_007;
        let n = nums.len();
        let max_v = *nums.iter().max().unwrap() as usize;
        let mut dp = vec![0; max_v + 1];
        for a in 0..=nums[0] as usize {
            dp[a] = 1;
        }
        for i in 1..n {
            let mut ndp = vec![0; max_v + 1];
            let mut pref = vec![0; max_v + 2];
            for a in 0..=max_v {
                pref[a + 1] = (pref[a] + dp[a]) % MOD;
            }
            for a2 in 0..=nums[i] as usize {
                let b2 = nums[i] - a2 as i32;
                let mut max_a1 = a2 as i32;
                let lim = nums[i - 1] - b2;
                if lim < max_a1 {
                    max_a1 = lim;
                }
                if max_a1 < 0 {
                    continue;
                }
                if max_a1 > max_v as i32 {
                    max_a1 = max_v as i32;
                }
                ndp[a2] = pref[(max_a1 + 1) as usize];
            }
            dp = ndp;
        }
        let mut ans = 0;
        for v in dp {
            ans = (ans + v) % MOD;
        }
        ans
    }
}
'''

FILES["3253_construct_string_with_minimum_cost_easy"] = r'''// LeetCode 3253 - Construct String with Minimum Cost (Easy)
// https://leetcode.com/problems/construct-string-with-minimum-cost-easy/

use std::collections::HashMap;

impl Solution {
    pub fn minimum_cost(target: String, words: Vec<String>, costs: Vec<i32>) -> i32 {
        const INF: i64 = 1_000_000_000_000_000_000;
        let n = target.len();
        let tb = target.as_bytes();
        let mut dp = vec![INF; n + 1];
        dp[0] = 0;
        let mut best: HashMap<String, i32> = HashMap::new();
        for (i, w) in words.iter().enumerate() {
            let e = best.entry(w.clone()).or_insert(i32::MAX);
            if costs[i] < *e {
                *e = costs[i];
            }
        }
        for i in 0..n {
            if dp[i] == INF {
                continue;
            }
            for (w, &c) in &best {
                let l = w.len();
                if i + l <= n && &tb[i..i + l] == w.as_bytes() && dp[i] + c as i64 < dp[i + l] {
                    dp[i + l] = dp[i] + c as i64;
                }
            }
        }
        if dp[n] == INF { -1 } else { dp[n] as i32 }
    }
}
'''

def main():
    n = 0
    for folder, src in FILES.items():
        path = ROOT / folder / "solution.rs"
        path.write_text(src, encoding="utf-8", newline="\n")
        n += 1
        print("wrote", folder)
    print("total", n)

if __name__ == "__main__":
    main()

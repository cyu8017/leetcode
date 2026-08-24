#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
FILES = {}

LIST = r'''#[derive(PartialEq, Eq)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl ListNode {
    #[inline]
    pub fn new(val: i32) -> Self {
        ListNode { val, next: None }
    }
}
'''

FILES["2653_sliding_subarray_beauty"] = r'''// LeetCode 2653 - Sliding Subarray Beauty
// https://leetcode.com/problems/sliding-subarray-beauty/

impl Solution {
    pub fn get_subarray_beauty(nums: Vec<i32>, k: i32, x: i32) -> Vec<i32> {
        let mut freq = [0i32; 101];
        let k = k as usize;
        let mut ans = vec![0; nums.len() - k + 1];
        for i in 0..nums.len() {
            freq[(nums[i] + 50) as usize] += 1;
            if i >= k {
                freq[(nums[i - k] + 50) as usize] -= 1;
            }
            if i >= k - 1 {
                let mut need = x;
                let mut val = 0;
                for j in 0..50 {
                    need -= freq[j];
                    if need <= 0 {
                        val = j as i32 - 50;
                        break;
                    }
                }
                ans[i - k + 1] = val;
            }
        }
        ans
    }
}
'''

FILES["2654_minimum_number_of_operations_to_make_all_array_elements_equal_to_1"] = r'''// LeetCode 2654 - Minimum Number of Operations to Make All Array Elements Equal to 1
// https://leetcode.com/problems/minimum-number-of-operations-to-make-all-array-elements-equal-to-1/

impl Solution {
    pub fn min_operations(nums: Vec<i32>) -> i32 {
        fn gcd(mut a: i32, mut b: i32) -> i32 {
            while b != 0 {
                let t = a % b;
                a = b;
                b = t;
            }
            a
        }
        let n = nums.len() as i32;
        let ones = nums.iter().filter(|&&x| x == 1).count() as i32;
        if ones > 0 {
            return n - ones;
        }
        let mut best = n + 1;
        for i in 0..nums.len() {
            let mut g = 0;
            for j in i..nums.len() {
                g = gcd(g, nums[j]);
                if g == 1 {
                    best = best.min((j - i) as i32);
                    break;
                }
            }
        }
        if best == n + 1 {
            -1
        } else {
            best + n - 1
        }
    }
}
'''

FILES["2655_find_maximal_uncovered_ranges"] = r'''// LeetCode 2655 - Find Maximal Uncovered Ranges
// https://leetcode.com/problems/find-maximal-uncovered-ranges/

impl Solution {
    pub fn find_maximal_uncovered_ranges(n: i32, mut ranges: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        ranges.sort_unstable();
        let mut ans = Vec::new();
        let mut cur = 0;
        for r in &ranges {
            if r[0] > cur {
                ans.push(vec![cur, r[0] - 1]);
            }
            if r[1] + 1 > cur {
                cur = r[1] + 1;
            }
        }
        if cur < n {
            ans.push(vec![cur, n - 1]);
        }
        ans
    }
}
'''

FILES["2656_maximum_sum_with_exactly_k_elements"] = r'''// LeetCode 2656 - Maximum Sum With Exactly K Elements
// https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/

impl Solution {
    pub fn maximize_sum(nums: Vec<i32>, k: i32) -> i32 {
        let mx = *nums.iter().max().unwrap();
        k * mx + k * (k - 1) / 2
    }
}
'''

FILES["2657_find_the_prefix_common_array_of_two_arrays"] = r'''// LeetCode 2657 - Find the Prefix Common Array of Two Arrays
// https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/

impl Solution {
    pub fn find_the_prefix_common_array(a: Vec<i32>, b: Vec<i32>) -> Vec<i32> {
        let n = a.len();
        let mut seen_a = vec![0u8; n + 1];
        let mut seen_b = vec![0u8; n + 1];
        let mut ans = vec![0; n];
        let mut common = 0;
        for i in 0..n {
            if seen_b[a[i] as usize] != 0 {
                common += 1;
            }
            seen_a[a[i] as usize] = 1;
            if seen_a[b[i] as usize] != 0 {
                common += 1;
            }
            seen_b[b[i] as usize] = 1;
            ans[i] = common;
        }
        ans
    }
}
'''

FILES["2658_maximum_number_of_fish_in_a_grid"] = r'''// LeetCode 2658 - Maximum Number of Fish in a Grid
// https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/

impl Solution {
    pub fn find_max_fish(mut grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        fn dfs(grid: &mut [Vec<i32>], r: i32, c: i32, m: i32, n: i32) -> i32 {
            if r < 0 || r >= m || c < 0 || c >= n || grid[r as usize][c as usize] == 0 {
                return 0;
            }
            let fish = grid[r as usize][c as usize];
            grid[r as usize][c as usize] = 0;
            fish + dfs(grid, r + 1, c, m, n)
                + dfs(grid, r - 1, c, m, n)
                + dfs(grid, r, c + 1, m, n)
                + dfs(grid, r, c - 1, m, n)
        }
        let mut best = 0;
        for i in 0..m {
            for j in 0..n {
                if grid[i][j] > 0 {
                    best = best.max(dfs(&mut grid, i as i32, j as i32, m as i32, n as i32));
                }
            }
        }
        best
    }
}
'''

FILES["2659_make_array_empty"] = r'''// LeetCode 2659 - Make Array Empty
// https://leetcode.com/problems/make-array-empty/

impl Solution {
    pub fn count_operations_to_empty_array(nums: Vec<i32>) -> i64 {
        let n = nums.len();
        let mut idx: Vec<usize> = (0..n).collect();
        idx.sort_by_key(|&i| nums[i]);
        let mut ans = n as i64;
        for i in 1..n {
            if idx[i] < idx[i - 1] {
                ans += (n - i) as i64;
            }
        }
        ans
    }
}
'''

FILES["2660_determine_the_winner_of_a_bowling_game"] = r'''// LeetCode 2660 - Determine the Winner of a Bowling Game
// https://leetcode.com/problems/determine-the-winner-of-a-bowling-game/

impl Solution {
    pub fn is_winner(player1: Vec<i32>, player2: Vec<i32>) -> i32 {
        fn score(p: &[i32]) -> i32 {
            let mut s = 0;
            for i in 0..p.len() {
                let mut mul = 1;
                if (i > 0 && p[i - 1] == 10) || (i > 1 && p[i - 2] == 10) {
                    mul = 2;
                }
                s += mul * p[i];
            }
            s
        }
        let a = score(&player1);
        let b = score(&player2);
        if a > b {
            1
        } else if b > a {
            2
        } else {
            0
        }
    }
}
'''

FILES["2661_first_completely_painted_row_or_column"] = r'''// LeetCode 2661 - First Completely Painted Row or Column
// https://leetcode.com/problems/first-completely-painted-row-or-column/

impl Solution {
    pub fn first_complete_index(arr: Vec<i32>, mat: Vec<Vec<i32>>) -> i32 {
        let m = mat.len();
        let n = mat[0].len();
        let mut pos = vec![(0usize, 0usize); m * n + 1];
        for i in 0..m {
            for j in 0..n {
                pos[mat[i][j] as usize] = (i, j);
            }
        }
        let mut row_cnt = vec![0; m];
        let mut col_cnt = vec![0; n];
        for (i, &v) in arr.iter().enumerate() {
            let (r, c) = pos[v as usize];
            row_cnt[r] += 1;
            col_cnt[c] += 1;
            if row_cnt[r] == n || col_cnt[c] == m {
                return i as i32;
            }
        }
        -1
    }
}
'''

FILES["2662_minimum_cost_of_a_path_with_special_roads"] = r'''// LeetCode 2662 - Minimum Cost of a Path With Special Roads
// https://leetcode.com/problems/minimum-cost-of-a-path-with-special-roads/

use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn minimum_cost(start: Vec<i32>, target: Vec<i32>, special_roads: Vec<Vec<i32>>) -> i32 {
        let mut points = vec![start.clone(), target.clone()];
        for r in &special_roads {
            points.push(vec![r[0], r[1]]);
            points.push(vec![r[2], r[3]]);
        }
        let n = points.len();
        let dist_man = |a: &[i32], b: &[i32]| (a[0] - b[0]).abs() + (a[1] - b[1]).abs();
        let mut g = vec![Vec::new(); n];
        for i in 0..n {
            for j in 0..n {
                if i != j {
                    g[i].push((j, dist_man(&points[i], &points[j])));
                }
            }
        }
        for r in &special_roads {
            let mut u = -1;
            let mut v = -1;
            for i in 0..n {
                if points[i][0] == r[0] && points[i][1] == r[1] {
                    u = i as i32;
                }
                if points[i][0] == r[2] && points[i][1] == r[3] {
                    v = i as i32;
                }
            }
            if u >= 0 && v >= 0 {
                g[u as usize].push((v as usize, r[4]));
            }
        }
        let mut dist = vec![i32::MAX / 4; n];
        dist[0] = 0;
        let mut pq = BinaryHeap::new();
        pq.push(Reverse((0, 0usize)));
        while let Some(Reverse((cost, id))) = pq.pop() {
            if cost > dist[id] {
                continue;
            }
            for &(to, w) in &g[id] {
                if cost + w < dist[to] {
                    dist[to] = cost + w;
                    pq.push(Reverse((dist[to], to)));
                }
            }
        }
        dist[1]
    }
}
'''

FILES["2663_lexicographically_smallest_beautiful_string"] = r'''// LeetCode 2663 - Lexicographically Smallest Beautiful String
// https://leetcode.com/problems/lexicographically-smallest-beautiful-string/

impl Solution {
    pub fn smallest_beautiful_string(s: String, k: i32) -> String {
        let n = s.len();
        let mut b: Vec<u8> = s.into_bytes();
        for i in (0..n).rev() {
            let mut c = b[i] + 1;
            while c < b'a' + k as u8 {
                if (i > 0 && c == b[i - 1]) || (i > 1 && c == b[i - 2]) {
                    c += 1;
                    continue;
                }
                b[i] = c;
                for j in i + 1..n {
                    let mut nc = b'a';
                    while nc < b'a' + k as u8 {
                        if (j > 0 && nc == b[j - 1]) || (j > 1 && nc == b[j - 2]) {
                            nc += 1;
                            continue;
                        }
                        b[j] = nc;
                        break;
                    }
                }
                return String::from_utf8(b).unwrap();
            }
        }
        String::new()
    }
}
'''

FILES["2664_the_knights_tour"] = r'''// LeetCode 2664 - The Knight's Tour
// https://leetcode.com/problems/the-knights-tour/

impl Solution {
    pub fn tour_of_knight(m: i32, n: i32, r: i32, c: i32) -> Vec<Vec<i32>> {
        let m = m as usize;
        let n = n as usize;
        let mut ans = vec![vec![-1; n]; m];
        const DIRS: [(i32, i32); 8] = [
            (1, 2),
            (1, -2),
            (-1, 2),
            (-1, -2),
            (2, 1),
            (2, -1),
            (-2, 1),
            (-2, -1),
        ];
        fn dfs(ans: &mut [Vec<i32>], x: i32, y: i32, step: i32, m: i32, n: i32) -> bool {
            ans[x as usize][y as usize] = step;
            if step == m * n - 1 {
                return true;
            }
            for &(dx, dy) in &DIRS {
                let nx = x + dx;
                let ny = y + dy;
                if nx >= 0
                    && nx < m
                    && ny >= 0
                    && ny < n
                    && ans[nx as usize][ny as usize] == -1
                    && dfs(ans, nx, ny, step + 1, m, n)
                {
                    return true;
                }
            }
            ans[x as usize][y as usize] = -1;
            false
        }
        dfs(&mut ans, r, c, 0, m as i32, n as i32);
        ans
    }
}
'''

FILES["2665_counter_ii"] = r'''// LeetCode 2665 - Counter II
// https://leetcode.com/problems/counter-ii/

pub struct CounterII {
    init: i32,
    cur: i32,
}

impl CounterII {
    pub fn new(init: i32) -> Self {
        Self { init, cur: init }
    }

    pub fn increment(&mut self) -> i32 {
        self.cur += 1;
        self.cur
    }

    pub fn decrement(&mut self) -> i32 {
        self.cur -= 1;
        self.cur
    }

    pub fn reset(&mut self) -> i32 {
        self.cur = self.init;
        self.cur
    }
}

impl Solution {
    pub fn create_counter(init: i32) -> CounterII {
        CounterII::new(init)
    }
}
'''

FILES["2666_allow_one_function_call"] = r'''// LeetCode 2666 - Allow One Function Call
// https://leetcode.com/problems/allow-one-function-call/

impl Solution {
    pub fn once(f: impl Fn(i32) -> i32) -> impl FnMut(i32) -> Option<i32> {
        let mut called = false;
        move |arg| {
            if called {
                return None;
            }
            called = true;
            Some(f(arg))
        }
    }
}
'''

FILES["2667_create_hello_world_function"] = r'''// LeetCode 2667 - Create Hello World Function
// https://leetcode.com/problems/create-hello-world-function/

impl Solution {
    pub fn create_hello_world() -> impl Fn() -> String {
        || "Hello World".to_string()
    }
}
'''

FILES["2670_find_the_distinct_difference_array"] = r'''// LeetCode 2670 - Find the Distinct Difference Array
// https://leetcode.com/problems/find-the-distinct-difference-array/

use std::collections::HashSet;

impl Solution {
    pub fn distinct_difference_array(nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len();
        let mut suf = vec![0; n + 1];
        let mut seen = HashSet::new();
        for i in (0..n).rev() {
            seen.insert(nums[i]);
            suf[i] = seen.len() as i32;
        }
        seen.clear();
        let mut ans = vec![0; n];
        for i in 0..n {
            seen.insert(nums[i]);
            ans[i] = seen.len() as i32 - suf[i + 1];
        }
        ans
    }
}
'''

FILES["2671_frequency_tracker"] = r'''// LeetCode 2671 - Frequency Tracker
// https://leetcode.com/problems/frequency-tracker/

use std::collections::HashMap;

pub struct FrequencyTracker {
    freq: HashMap<i32, i32>,
    count: HashMap<i32, i32>,
}

impl FrequencyTracker {
    pub fn new() -> Self {
        Self {
            freq: HashMap::new(),
            count: HashMap::new(),
        }
    }

    pub fn add(&mut self, number: i32) {
        let old = *self.freq.get(&number).unwrap_or(&0);
        if old > 0 {
            *self.count.entry(old).or_insert(0) -= 1;
        }
        self.freq.insert(number, old + 1);
        *self.count.entry(old + 1).or_insert(0) += 1;
    }

    pub fn delete_one(&mut self, number: i32) {
        let old = *self.freq.get(&number).unwrap_or(&0);
        if old == 0 {
            return;
        }
        *self.count.entry(old).or_insert(0) -= 1;
        self.freq.insert(number, old - 1);
        if old - 1 > 0 {
            *self.count.entry(old - 1).or_insert(0) += 1;
        }
    }

    pub fn has_frequency(&self, frequency: i32) -> bool {
        *self.count.get(&frequency).unwrap_or(&0) > 0
    }
}
'''

FILES["2672_number_of_adjacent_elements_with_the_same_color"] = r'''// LeetCode 2672 - Number of Adjacent Elements With the Same Color
// https://leetcode.com/problems/number-of-adjacent-elements-with-the-same-color/

impl Solution {
    pub fn color_the_array(n: i32, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let n = n as usize;
        let mut colors = vec![0; n];
        let mut ans = vec![0; queries.len()];
        let mut same = 0;
        for (i, q) in queries.iter().enumerate() {
            let idx = q[0] as usize;
            let color = q[1];
            if colors[idx] != 0 {
                if idx > 0 && colors[idx] == colors[idx - 1] {
                    same -= 1;
                }
                if idx + 1 < n && colors[idx] == colors[idx + 1] {
                    same -= 1;
                }
            }
            colors[idx] = color;
            if idx > 0 && colors[idx] == colors[idx - 1] {
                same += 1;
            }
            if idx + 1 < n && colors[idx] == colors[idx + 1] {
                same += 1;
            }
            ans[i] = same;
        }
        ans
    }
}
'''

FILES["2673_make_costs_of_paths_equal_in_a_binary_tree"] = r'''// LeetCode 2673 - Make Costs of Paths Equal in a Binary Tree
// https://leetcode.com/problems/make-costs-of-paths-equal-in-a-binary-tree/

impl Solution {
    pub fn min_increments(n: i32, mut cost: Vec<i32>) -> i32 {
        let mut ans = 0;
        let mut i = n / 2 - 1;
        while i >= 0 {
            let l = (2 * i + 1) as usize;
            let r = (2 * i + 2) as usize;
            ans += (cost[l] - cost[r]).abs();
            cost[i as usize] += cost[l].max(cost[r]);
            i -= 1;
        }
        ans
    }
}
'''

FILES["2674_split_a_circular_linked_list"] = f'''// LeetCode 2674 - Split a Circular Linked List
// https://leetcode.com/problems/split-a-circular-linked-list/

{LIST}
impl Solution {{
    pub fn split_circular_linked_list(
        list: Option<Box<ListNode>>,
    ) -> Vec<Option<Box<ListNode>>> {{
        let mut vals = Vec::new();
        let mut cur = list;
        while let Some(node) = cur {{
            vals.push(node.val);
            cur = node.next;
        }}
        if vals.is_empty() {{
            return vec![None, None];
        }}
        let mid = (vals.len() + 1) / 2;
        fn build(slice: &[i32]) -> Option<Box<ListNode>> {{
            let mut head = None;
            for &v in slice.iter().rev() {{
                head = Some(Box::new(ListNode {{ val: v, next: head }}));
            }}
            head
        }}
        vec![build(&vals[..mid]), build(&vals[mid..])]
    }}
}}
'''

FILES["2675_array_of_objects_to_matrix"] = r'''// LeetCode 2675 - Array of Objects to Matrix
// https://leetcode.com/problems/array-of-objects-to-matrix/

use std::collections::{BTreeMap, BTreeSet};

impl Solution {
    pub fn json_to_matrix(arr: Vec<BTreeMap<String, String>>) -> Vec<Vec<String>> {
        let mut keys = BTreeSet::new();
        for obj in &arr {
            for k in obj.keys() {
                keys.insert(k.clone());
            }
        }
        let mut mat = vec![keys.iter().cloned().collect::<Vec<_>>()];
        for obj in &arr {
            let mut row = Vec::new();
            for k in &keys {
                row.push(obj.get(k).cloned().unwrap_or_default());
            }
            mat.push(row);
        }
        mat
    }
}
'''

FILES["2676_throttle"] = r'''// LeetCode 2676 - Throttle
// https://leetcode.com/problems/throttle/

use std::time::{Duration, Instant};

impl Solution {
    pub fn throttle(f: impl Fn(), t: i32) -> impl FnMut() {
        let mut last = Instant::now() - Duration::from_secs(86400);
        move || {
            let now = Instant::now();
            if now.duration_since(last).as_millis() as i64 >= t as i64 {
                last = now;
                f();
            }
        }
    }
}
'''

FILES["2677_chunk_array"] = r'''// LeetCode 2677 - Chunk Array
// https://leetcode.com/problems/chunk-array/

impl Solution {
    pub fn chunk(arr: Vec<i32>, size: i32) -> Vec<Vec<i32>> {
        let size = size as usize;
        let mut ans = Vec::new();
        let mut i = 0;
        while i < arr.len() {
            let end = (i + size).min(arr.len());
            ans.push(arr[i..end].to_vec());
            i += size;
        }
        ans
    }
}
'''

FILES["2678_number_of_senior_citizens"] = r'''// LeetCode 2678 - Number of Senior Citizens
// https://leetcode.com/problems/number-of-senior-citizens/

impl Solution {
    pub fn count_seniors(details: Vec<String>) -> i32 {
        let mut ans = 0;
        for d in &details {
            let b = d.as_bytes();
            let age = (b[11] - b'0') as i32 * 10 + (b[12] - b'0') as i32;
            if age > 60 {
                ans += 1;
            }
        }
        ans
    }
}
'''

FILES["2679_sum_in_a_matrix"] = r'''// LeetCode 2679 - Sum in a Matrix
// https://leetcode.com/problems/sum-in-a-matrix/

impl Solution {
    pub fn matrix_sum(mut nums: Vec<Vec<i32>>) -> i32 {
        for row in &mut nums {
            row.sort_unstable();
        }
        let mut ans = 0;
        let n = nums[0].len();
        for j in 0..n {
            let mut mx = 0;
            for row in &nums {
                mx = mx.max(row[j]);
            }
            ans += mx;
        }
        ans
    }
}
'''

FILES["2680_maximum_or"] = r'''// LeetCode 2680 - Maximum OR
// https://leetcode.com/problems/maximum-or/

impl Solution {
    pub fn maximum_or(nums: Vec<i32>, k: i32) -> i64 {
        let n = nums.len();
        let mut pref = vec![0i64; n + 1];
        let mut suf = vec![0i64; n + 1];
        for i in 0..n {
            pref[i + 1] = pref[i] | nums[i] as i64;
        }
        for i in (0..n).rev() {
            suf[i] = suf[i + 1] | nums[i] as i64;
        }
        let mut ans = 0i64;
        for i in 0..n {
            let cur = pref[i] | ((nums[i] as i64) << k) | suf[i + 1];
            if cur > ans {
                ans = cur;
            }
        }
        ans
    }
}
'''

FILES["2681_power_of_heroes"] = r'''// LeetCode 2681 - Power of Heroes
// https://leetcode.com/problems/power-of-heroes/

impl Solution {
    pub fn sum_of_power(mut nums: Vec<i32>) -> i32 {
        const MOD: i64 = 1_000_000_007;
        nums.sort_unstable();
        let mut ans = 0i64;
        let mut s = 0i64;
        for x in nums {
            let x = x as i64;
            ans = (ans + (s + x) % MOD * x % MOD * x) % MOD;
            s = (s * 2 + x) % MOD;
        }
        ans as i32
    }
}
'''

FILES["2682_find_the_losers_of_the_circular_game"] = r'''// LeetCode 2682 - Find the Losers of the Circular Game
// https://leetcode.com/problems/find-the-losers-of-the-circular-game/

impl Solution {
    pub fn circular_game_losers(n: i32, k: i32) -> Vec<i32> {
        let mut seen = vec![0u8; (n + 1) as usize];
        let mut cur = 1;
        let mut step = 1;
        while seen[cur as usize] == 0 {
            seen[cur as usize] = 1;
            cur = (cur - 1 + step * k) % n + 1;
            step += 1;
        }
        let mut ans = Vec::new();
        for i in 1..=n {
            if seen[i as usize] == 0 {
                ans.push(i);
            }
        }
        ans
    }
}
'''

FILES["2683_neighboring_bitwise_xor"] = r'''// LeetCode 2683 - Neighboring Bitwise XOR
// https://leetcode.com/problems/neighboring-bitwise-xor/

impl Solution {
    pub fn does_valid_array_exist(derived: Vec<i32>) -> bool {
        let mut x = 0;
        for v in derived {
            x ^= v;
        }
        x == 0
    }
}
'''

FILES["2684_maximum_number_of_moves_in_a_grid"] = r'''// LeetCode 2684 - Maximum Number of Moves in a Grid
// https://leetcode.com/problems/maximum-number-of-moves-in-a-grid/

impl Solution {
    pub fn max_moves(grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        let mut dp = vec![0; m];
        for c in (0..n - 1).rev() {
            let mut ndp = vec![0; m];
            for r in 0..m {
                let mut best = 0;
                for dr in [-1i32, 0, 1] {
                    let nr = r as i32 + dr;
                    if nr >= 0
                        && (nr as usize) < m
                        && grid[nr as usize][c + 1] > grid[r][c]
                    {
                        best = best.max(1 + dp[nr as usize]);
                    }
                }
                ndp[r] = best;
            }
            dp = ndp;
        }
        *dp.iter().max().unwrap()
    }
}
'''

FILES["2685_count_the_number_of_complete_components"] = r'''// LeetCode 2685 - Count the Number of Complete Components
// https://leetcode.com/problems/count-the-number-of-complete-components/

impl Solution {
    pub fn count_complete_components(n: i32, edges: Vec<Vec<i32>>) -> i32 {
        let n = n as usize;
        let mut g = vec![Vec::new(); n];
        for e in &edges {
            g[e[0] as usize].push(e[1] as usize);
            g[e[1] as usize].push(e[0] as usize);
        }
        let mut vis = vec![false; n];
        let mut ans = 0;
        for i in 0..n {
            if vis[i] {
                continue;
            }
            let mut nodes = Vec::new();
            fn dfs(u: usize, g: &[Vec<usize>], vis: &mut [bool], nodes: &mut Vec<usize>) {
                vis[u] = true;
                nodes.push(u);
                for &v in &g[u] {
                    if !vis[v] {
                        dfs(v, g, vis, nodes);
                    }
                }
            }
            dfs(i, &g, &mut vis, &mut nodes);
            let mut ecount = 0;
            for &u in &nodes {
                ecount += g[u].len() as i32;
            }
            ecount /= 2;
            let sz = nodes.len() as i32;
            if ecount == sz * (sz - 1) / 2 {
                ans += 1;
            }
        }
        ans
    }
}
'''

def main():
    n = 0
    for folder, text in FILES.items():
        path = ROOT / folder / "solution.rs"
        path.write_text(text, encoding="utf-8", newline="\n")
        if path.read_bytes().startswith(b"\xef\xbb\xbf"):
            raise SystemExit(f"BOM in {folder}")
        n += 1
        print(f"wrote {folder}/solution.rs ({len(text)} bytes)")
    print(f"batch B written: {n}")

if __name__ == "__main__":
    main()

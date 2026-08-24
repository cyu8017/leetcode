#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")

FILES = {}

FILES["2491_divide_players_into_teams_of_equal_skill"] = r'''// LeetCode 2491 - Divide Players Into Teams of Equal Skill
// https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

impl Solution {
    pub fn divide_players(mut skill: Vec<i32>) -> i64 {
        skill.sort_unstable();
        let n = skill.len();
        let target = skill[0] + skill[n - 1];
        let mut chem = 0i64;
        for i in 0..n / 2 {
            if skill[i] + skill[n - 1 - i] != target {
                return -1;
            }
            chem += skill[i] as i64 * skill[n - 1 - i] as i64;
        }
        chem
    }
}
'''

FILES["2492_minimum_score_of_a_path_between_two_cities"] = r'''// LeetCode 2492 - Minimum Score of a Path Between Two Cities
// https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/

use std::collections::VecDeque;

impl Solution {
    pub fn min_score(n: i32, roads: Vec<Vec<i32>>) -> i32 {
        let n = n as usize;
        let mut g = vec![Vec::new(); n + 1];
        for r in &roads {
            let (a, b, w) = (r[0] as usize, r[1] as usize, r[2]);
            g[a].push((b, w));
            g[b].push((a, w));
        }
        let mut vis = vec![false; n + 1];
        let mut ans = 1 << 30;
        let mut q = VecDeque::new();
        q.push_back(1);
        vis[1] = true;
        while let Some(u) = q.pop_front() {
            for &(v, w) in &g[u] {
                if w < ans {
                    ans = w;
                }
                if !vis[v] {
                    vis[v] = true;
                    q.push_back(v);
                }
            }
        }
        ans
    }
}
'''

FILES["2493_divide_nodes_into_the_maximum_number_of_groups"] = r'''// LeetCode 2493 - Divide Nodes Into the Maximum Number of Groups
// https://leetcode.com/problems/divide-nodes-into-the-maximum-number-of-groups/

use std::collections::VecDeque;

impl Solution {
    pub fn magnificent_sets(n: i32, edges: Vec<Vec<i32>>) -> i32 {
        let n = n as usize;
        let mut g = vec![Vec::new(); n + 1];
        for e in &edges {
            let (a, b) = (e[0] as usize, e[1] as usize);
            g[a].push(b);
            g[b].push(a);
        }
        let mut color = vec![-1i32; n + 1];
        let mut components = Vec::new();
        for i in 1..=n {
            if color[i] != -1 {
                continue;
            }
            let mut comp = Vec::new();
            let mut q = VecDeque::new();
            q.push_back(i);
            color[i] = 0;
            let mut bipartite = true;
            while let Some(u) = q.pop_front() {
                comp.push(u);
                for &v in &g[u] {
                    if color[v] == -1 {
                        color[v] = color[u] ^ 1;
                        q.push_back(v);
                    } else if color[v] == color[u] {
                        bipartite = false;
                    }
                }
            }
            if !bipartite {
                return -1;
            }
            components.push(comp);
        }
        fn bfs_depth(start: usize, n: usize, g: &[Vec<usize>]) -> i32 {
            let mut dist = vec![-1; n + 1];
            let mut q = VecDeque::new();
            q.push_back(start);
            dist[start] = 1;
            let mut best = 1;
            while let Some(u) = q.pop_front() {
                if dist[u] > best {
                    best = dist[u];
                }
                for &v in &g[u] {
                    if dist[v] == -1 {
                        dist[v] = dist[u] + 1;
                        q.push_back(v);
                    }
                }
            }
            best
        }
        let mut ans = 0;
        for comp in &components {
            let mut best = 0;
            for &u in comp {
                let d = bfs_depth(u, n, &g);
                if d > best {
                    best = d;
                }
            }
            ans += best;
        }
        ans
    }
}
'''

FILES["2495_number_of_subarrays_having_even_product"] = r'''// LeetCode 2495 - Number of Subarrays Having Even Product
// https://leetcode.com/problems/number-of-subarrays-having-even-product/

impl Solution {
    pub fn even_product(nums: Vec<i32>) -> i64 {
        let n = nums.len() as i64;
        let total = n * (n + 1) / 2;
        let mut odd_len = 0i64;
        let mut odd = 0i64;
        for x in nums {
            if x % 2 == 1 {
                odd += 1;
                odd_len += odd;
            } else {
                odd = 0;
            }
        }
        total - odd_len
    }
}
'''

FILES["2496_maximum_value_of_a_string_in_an_array"] = r'''// LeetCode 2496 - Maximum Value of a String in an Array
// https://leetcode.com/problems/maximum-value-of-a-string-in-an-array/

impl Solution {
    pub fn maximum_value(strs: Vec<String>) -> i32 {
        let mut ans = 0;
        for s in strs {
            let mut all_digit = true;
            let mut val = 0;
            for c in s.bytes() {
                if c < b'0' || c > b'9' {
                    all_digit = false;
                    break;
                }
                val = val * 10 + (c - b'0') as i32;
            }
            if !all_digit {
                val = s.len() as i32;
            }
            if val > ans {
                ans = val;
            }
        }
        ans
    }
}
'''

FILES["2497_maximum_star_sum_of_a_graph"] = r'''// LeetCode 2497 - Maximum Star Sum of a Graph
// https://leetcode.com/problems/maximum-star-sum-of-a-graph/

impl Solution {
    pub fn max_star_sum(vals: Vec<i32>, edges: Vec<Vec<i32>>, k: i32) -> i32 {
        let n = vals.len();
        let mut g = vec![Vec::new(); n];
        for e in &edges {
            let (a, b) = (e[0] as usize, e[1] as usize);
            g[a].push(b);
            g[b].push(a);
        }
        let mut ans = vals[0];
        for i in 0..n {
            let mut neigh = Vec::new();
            for &v in &g[i] {
                if vals[v] > 0 {
                    neigh.push(vals[v]);
                }
            }
            neigh.sort_unstable_by(|a, b| b.cmp(a));
            let mut sum = vals[i];
            for j in 0..neigh.len().min(k as usize) {
                sum += neigh[j];
            }
            if sum > ans {
                ans = sum;
            }
        }
        ans
    }
}
'''

FILES["2498_frog_jump_ii"] = r'''// LeetCode 2498 - Frog Jump II
// https://leetcode.com/problems/frog-jump-ii/

impl Solution {
    pub fn max_jump(stones: Vec<i32>) -> i32 {
        let mut ans = stones[1] - stones[0];
        for i in 2..stones.len() {
            let diff = stones[i] - stones[i - 2];
            if diff > ans {
                ans = diff;
            }
        }
        ans
    }
}
'''

FILES["2499_minimum_total_cost_to_make_arrays_unequal"] = r'''// LeetCode 2499 - Minimum Total Cost to Make Arrays Unequal
// https://leetcode.com/problems/minimum-total-cost-to-make-arrays-unequal/

use std::collections::HashMap;

impl Solution {
    pub fn minimum_total_cost(nums1: Vec<i32>, nums2: Vec<i32>) -> i64 {
        let n = nums1.len();
        let mut freq: HashMap<i32, i32> = HashMap::new();
        let mut ans = 0i64;
        let mut same = 0;
        for i in 0..n {
            if nums1[i] == nums2[i] {
                same += 1;
                *freq.entry(nums1[i]).or_insert(0) += 1;
                ans += i as i64;
            }
        }
        let mut max_freq = 0;
        let mut max_val = 0;
        for (&v, &c) in &freq {
            if c > max_freq {
                max_freq = c;
                max_val = v;
            }
        }
        let mut need = max_freq * 2 - same;
        if need <= 0 {
            return ans;
        }
        for i in 0..n {
            if need <= 0 {
                break;
            }
            if nums1[i] != nums2[i] && nums1[i] != max_val && nums2[i] != max_val {
                ans += i as i64;
                need -= 1;
            }
        }
        if need > 0 {
            -1
        } else {
            ans
        }
    }
}
'''

FILES["2500_delete_greatest_value_in_each_row"] = r'''// LeetCode 2500 - Delete Greatest Value in Each Row
// https://leetcode.com/problems/delete-greatest-value-in-each-row/

impl Solution {
    pub fn delete_greatest_value(mut grid: Vec<Vec<i32>>) -> i32 {
        for row in &mut grid {
            row.sort_unstable();
        }
        let mut ans = 0;
        let n = grid[0].len();
        for c in 0..n {
            let mut mx = 0;
            for row in &grid {
                if row[c] > mx {
                    mx = row[c];
                }
            }
            ans += mx;
        }
        ans
    }
}
'''

FILES["2501_longest_square_streak_in_an_array"] = r'''// LeetCode 2501 - Longest Square Streak in an Array
// https://leetcode.com/problems/longest-square-streak-in-an-array/

use std::collections::HashSet;

impl Solution {
    pub fn longest_square_streak(nums: Vec<i32>) -> i32 {
        let mut set: HashSet<i64> = nums.iter().map(|&x| x as i64).collect();
        let mut best = -1;
        for x in nums {
            if !set.contains(&(x as i64)) {
                continue;
            }
            let mut length = 0;
            let mut cur = x as i64;
            while set.contains(&cur) {
                length += 1;
                set.remove(&cur);
                if cur > 100000 {
                    break;
                }
                cur = cur * cur;
            }
            if length >= 2 && length > best {
                best = length;
            }
        }
        best
    }
}
'''

FILES["2502_design_memory_allocator"] = r'''// LeetCode 2502 - Design Memory Allocator
// https://leetcode.com/problems/design-memory-allocator/

pub struct Allocator {
    mem: Vec<i32>,
}

impl Allocator {
    pub fn new(n: i32) -> Self {
        Self {
            mem: vec![0; n as usize],
        }
    }

    pub fn allocate(&mut self, size: i32, m_id: i32) -> i32 {
        let mut free_cnt = 0;
        for i in 0..self.mem.len() {
            if self.mem[i] == 0 {
                free_cnt += 1;
                if free_cnt == size {
                    let start = i as i32 - size + 1;
                    for j in start as usize..=i {
                        self.mem[j] = m_id;
                    }
                    return start;
                }
            } else {
                free_cnt = 0;
            }
        }
        -1
    }

    pub fn free_memory(&mut self, m_id: i32) -> i32 {
        let mut cnt = 0;
        for x in &mut self.mem {
            if *x == m_id {
                *x = 0;
                cnt += 1;
            }
        }
        cnt
    }
}
'''

FILES["2503_maximum_number_of_points_from_grid_queries"] = r'''// LeetCode 2503 - Maximum Number of Points From Grid Queries
// https://leetcode.com/problems/maximum-number-of-points-from-grid-queries/

use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn max_points(grid: Vec<Vec<i32>>, queries: Vec<i32>) -> Vec<i32> {
        let m = grid.len();
        let n = grid[0].len();
        let mut order: Vec<usize> = (0..queries.len()).collect();
        order.sort_by_key(|&i| queries[i]);
        let mut ans = vec![0; queries.len()];
        let mut visited = vec![vec![false; n]; m];
        let mut pq: BinaryHeap<Reverse<(i32, usize, usize)>> = BinaryHeap::new();
        pq.push(Reverse((grid[0][0], 0, 0)));
        visited[0][0] = true;
        let mut points = 0;
        let dirs = [(1isize, 0isize), (-1, 0), (0, 1), (0, -1)];
        for qi in order {
            let q = queries[qi];
            while let Some(Reverse((v, _, _))) = pq.peek() {
                if *v >= q {
                    break;
                }
                let Reverse((_, r, c)) = pq.pop().unwrap();
                points += 1;
                for (dr, dc) in dirs {
                    let nr = r as isize + dr;
                    let nc = c as isize + dc;
                    if nr >= 0 && nr < m as isize && nc >= 0 && nc < n as isize {
                        let (nr, nc) = (nr as usize, nc as usize);
                        if !visited[nr][nc] {
                            visited[nr][nc] = true;
                            pq.push(Reverse((grid[nr][nc], nr, nc)));
                        }
                    }
                }
            }
            ans[qi] = points;
        }
        ans
    }
}
'''

FILES["2505_bitwise_or_of_all_subsequence_sums"] = r'''// LeetCode 2505 - Bitwise OR of All Subsequence Sums
// https://leetcode.com/problems/bitwise-or-of-all-subsequence-sums/

impl Solution {
    pub fn subsequence_sum_or(nums: Vec<i32>) -> i64 {
        let mut ans = 0i64;
        let mut prefix = 0i64;
        for x in nums {
            prefix += x as i64;
            ans |= x as i64 | prefix;
        }
        ans
    }
}
'''

FILES["2506_count_pairs_of_similar_strings"] = r'''// LeetCode 2506 - Count Pairs Of Similar Strings
// https://leetcode.com/problems/count-pairs-of-similar-strings/

use std::collections::HashMap;

impl Solution {
    pub fn similar_pairs(words: Vec<String>) -> i32 {
        let mut freq: HashMap<u32, i32> = HashMap::new();
        let mut ans = 0;
        for w in words {
            let mut mask = 0u32;
            for c in w.bytes() {
                mask |= 1 << (c - b'a');
            }
            ans += *freq.get(&mask).unwrap_or(&0);
            *freq.entry(mask).or_insert(0) += 1;
        }
        ans
    }
}
'''

FILES["2507_smallest_value_after_replacing_with_sum_of_prime_factors"] = r'''// LeetCode 2507 - Smallest Value After Replacing With Sum of Prime Factors
// https://leetcode.com/problems/smallest-value-after-replacing-with-sum-of-prime-factors/

impl Solution {
    pub fn smallest_value(mut n: i32) -> i32 {
        fn sum_prime_factors(mut x: i32) -> i32 {
            let mut s = 0;
            let mut i = 2;
            while i * i <= x {
                while x % i == 0 {
                    s += i;
                    x /= i;
                }
                i += 1;
            }
            if x > 1 {
                s += x;
            }
            s
        }
        loop {
            let s = sum_prime_factors(n);
            if s == n {
                return n;
            }
            n = s;
        }
    }
}
'''

FILES["2508_add_edges_to_make_degrees_of_all_nodes_even"] = r'''// LeetCode 2508 - Add Edges to Make Degrees of All Nodes Even
// https://leetcode.com/problems/add-edges-to-make-degrees-of-all-nodes-even/

use std::collections::HashSet;

impl Solution {
    pub fn is_possible(n: i32, edges: Vec<Vec<i32>>) -> bool {
        let n = n as usize;
        let mut deg = vec![0; n + 1];
        let mut adj = vec![HashSet::new(); n + 1];
        for e in &edges {
            let (u, v) = (e[0] as usize, e[1] as usize);
            deg[u] += 1;
            deg[v] += 1;
            adj[u].insert(v);
            adj[v].insert(u);
        }
        let mut odd = Vec::new();
        for i in 1..=n {
            if deg[i] % 2 == 1 {
                odd.push(i);
            }
        }
        if odd.is_empty() {
            return true;
        }
        if odd.len() == 2 {
            let (a, b) = (odd[0], odd[1]);
            if !adj[a].contains(&b) {
                return true;
            }
            for i in 1..=n {
                if i != a && i != b && !adj[a].contains(&i) && !adj[b].contains(&i) {
                    return true;
                }
            }
            return false;
        }
        if odd.len() == 4 {
            let (a, b, c, d) = (odd[0], odd[1], odd[2], odd[3]);
            return (!adj[a].contains(&b) && !adj[c].contains(&d))
                || (!adj[a].contains(&c) && !adj[b].contains(&d))
                || (!adj[a].contains(&d) && !adj[b].contains(&c));
        }
        false
    }
}
'''

FILES["2509_cycle_length_queries_in_a_tree"] = r'''// LeetCode 2509 - Cycle Length Queries in a Tree
// https://leetcode.com/problems/cycle-length-queries-in-a-tree/

impl Solution {
    pub fn cycle_length_queries(_n: i32, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let mut ans = vec![0; queries.len()];
        for (i, q) in queries.iter().enumerate() {
            let mut a = q[0];
            let mut b = q[1];
            let mut steps = 0;
            while a != b {
                if a > b {
                    a /= 2;
                } else {
                    b /= 2;
                }
                steps += 1;
            }
            ans[i] = steps + 1;
        }
        ans
    }
}
'''

FILES["2510_check_if_there_is_a_path_with_equal_number_of_0s_and_1s"] = r'''// LeetCode 2510 - Check if There is a Path With Equal Number of 0's And 1's
// https://leetcode.com/problems/check-if-there-is-a-path-with-equal-number-of-0s-and-1s/

use std::collections::HashMap;

impl Solution {
    pub fn is_there_a_path(grid: Vec<Vec<i32>>) -> bool {
        let m = grid.len();
        let n = grid[0].len();
        if (m + n - 1) % 2 != 0 {
            return false;
        }
        let target = (m + n - 1) / 2;
        let mut memo: HashMap<(usize, usize, i32), bool> = HashMap::new();
        fn dfs(
            r: usize,
            c: usize,
            bal: i32,
            grid: &[Vec<i32>],
            target: i32,
            memo: &mut HashMap<(usize, usize, i32), bool>,
        ) -> bool {
            let m = grid.len();
            let n = grid[0].len();
            if r >= m || c >= n {
                return false;
            }
            let bal = bal + grid[r][c];
            if bal > target || bal + (m as i32 - 1 - r as i32) + (n as i32 - 1 - c as i32) < target {
                return false;
            }
            if r == m - 1 && c == n - 1 {
                return bal == target;
            }
            if let Some(&v) = memo.get(&(r, c, bal)) {
                return v;
            }
            let ok = dfs(r + 1, c, bal, grid, target, memo) || dfs(r, c + 1, bal, grid, target, memo);
            memo.insert((r, c, bal), ok);
            ok
        }
        dfs(0, 0, 0, &grid, target as i32, &mut memo)
    }
}
'''

FILES["2511_maximum_enemy_forts_that_can_be_captured"] = r'''// LeetCode 2511 - Maximum Enemy Forts That Can Be Captured
// https://leetcode.com/problems/maximum-enemy-forts-that-can-be-captured/

impl Solution {
    pub fn capture_forts(forts: Vec<i32>) -> i32 {
        let mut ans = 0;
        let mut prev = -1i32;
        for i in 0..forts.len() {
            if forts[i] != 0 {
                if prev >= 0 && forts[prev as usize] == -forts[i] {
                    let d = i as i32 - prev - 1;
                    if d > ans {
                        ans = d;
                    }
                }
                prev = i as i32;
            }
        }
        ans
    }
}
'''

FILES["2512_reward_top_k_students"] = r'''// LeetCode 2512 - Reward Top K Students
// https://leetcode.com/problems/reward-top-k-students/

use std::collections::HashSet;

impl Solution {
    pub fn top_students(
        positive_feedback: Vec<String>,
        negative_feedback: Vec<String>,
        report: Vec<String>,
        student_id: Vec<i32>,
        k: i32,
    ) -> Vec<i32> {
        let pos: HashSet<&str> = positive_feedback.iter().map(|s| s.as_str()).collect();
        let neg: HashSet<&str> = negative_feedback.iter().map(|s| s.as_str()).collect();
        let mut arr: Vec<(i32, i32)> = Vec::new();
        for i in 0..report.len() {
            let mut score = 0;
            for w in report[i].split_whitespace() {
                if pos.contains(w) {
                    score += 3;
                } else if neg.contains(w) {
                    score -= 1;
                }
            }
            arr.push((student_id[i], score));
        }
        arr.sort_by(|a, b| {
            if a.1 != b.1 {
                b.1.cmp(&a.1)
            } else {
                a.0.cmp(&b.0)
            }
        });
        arr.into_iter().take(k as usize).map(|(id, _)| id).collect()
    }
}
'''

FILES["2513_minimize_the_maximum_of_two_arrays"] = r'''// LeetCode 2513 - Minimize the Maximum of Two Arrays
// https://leetcode.com/problems/minimize-the-maximum-of-two-arrays/

impl Solution {
    pub fn minimize_set(divisor1: i32, divisor2: i32, unique_cnt1: i32, unique_cnt2: i32) -> i32 {
        fn gcd(mut x: i64, mut y: i64) -> i64 {
            while y != 0 {
                let t = x % y;
                x = y;
                y = t;
            }
            x
        }
        let lcm = divisor1 as i64 / gcd(divisor1 as i64, divisor2 as i64) * divisor2 as i64;
        let ok = |x: i64| {
            let a = x - x / divisor1 as i64;
            let b = x - x / divisor2 as i64;
            let both = x - x / lcm;
            a >= unique_cnt1 as i64 && b >= unique_cnt2 as i64 && both >= unique_cnt1 as i64 + unique_cnt2 as i64
        };
        let mut lo = 1i64;
        let mut hi = 1i64 << 62;
        while lo < hi {
            let mid = (lo + hi) / 2;
            if ok(mid) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        lo as i32
    }
}
'''

FILES["2514_count_anagrams"] = r'''// LeetCode 2514 - Count Anagrams
// https://leetcode.com/problems/count-anagrams/

impl Solution {
    pub fn count_anagrams(s: String) -> i32 {
        const MOD: i64 = 1_000_000_007;
        fn mod_pow(mut a: i64, mut e: i64) -> i64 {
            let mut res = 1;
            a %= MOD;
            while e > 0 {
                if e & 1 == 1 {
                    res = res * a % MOD;
                }
                a = a * a % MOD;
                e >>= 1;
            }
            res
        }
        let words: Vec<&str> = s.split_whitespace().collect();
        let max_n = words.iter().map(|w| w.len()).max().unwrap_or(0);
        let mut fact = vec![1i64; max_n + 1];
        let mut inv_fact = vec![1i64; max_n + 1];
        for i in 1..=max_n {
            fact[i] = fact[i - 1] * i as i64 % MOD;
        }
        inv_fact[max_n] = mod_pow(fact[max_n], MOD - 2);
        for i in (1..=max_n).rev() {
            inv_fact[i - 1] = inv_fact[i] * i as i64 % MOD;
        }
        let mut ans = 1i64;
        for word in words {
            let mut cnt = [0usize; 26];
            for c in word.bytes() {
                cnt[(c - b'a') as usize] += 1;
            }
            let mut cur = fact[word.len()];
            for c in cnt {
                cur = cur * inv_fact[c] % MOD;
            }
            ans = ans * cur % MOD;
        }
        ans as i32
    }
}
'''

FILES["2515_shortest_distance_to_target_string_in_a_circular_array"] = r'''// LeetCode 2515 - Shortest Distance to Target String in a Circular Array
// https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array/

impl Solution {
    pub fn closest_target(words: Vec<String>, target: String, start_index: i32) -> i32 {
        let n = words.len() as i32;
        let mut best = -1;
        for i in 0..n {
            if words[i as usize] == target {
                let mut d = i - start_index;
                if d < 0 {
                    d = -d;
                }
                if n - d < d {
                    d = n - d;
                }
                if best < 0 || d < best {
                    best = d;
                }
            }
        }
        best
    }
}
'''

FILES["2516_take_k_of_each_character_from_left_and_right"] = r'''// LeetCode 2516 - Take K of Each Character From Left and Right
// https://leetcode.com/problems/take-k-of-each-character-from-left-and-right/

impl Solution {
    pub fn take_characters(s: String, k: i32) -> i32 {
        let b = s.as_bytes();
        let n = b.len();
        let mut cnt = [0i32; 3];
        for &c in b {
            cnt[(c - b'a') as usize] += 1;
        }
        if cnt[0] < k || cnt[1] < k || cnt[2] < k {
            return -1;
        }
        let need = [cnt[0] - k, cnt[1] - k, cnt[2] - k];
        let mut window = [0i32; 3];
        let mut left = 0;
        let mut max_mid = 0;
        for right in 0..n {
            window[(b[right] - b'a') as usize] += 1;
            while window[0] > need[0] || window[1] > need[1] || window[2] > need[2] {
                window[(b[left] - b'a') as usize] -= 1;
                left += 1;
            }
            if right - left + 1 > max_mid {
                max_mid = right - left + 1;
            }
        }
        (n - max_mid) as i32
    }
}
'''

FILES["2517_maximum_tastiness_of_candy_basket"] = r'''// LeetCode 2517 - Maximum Tastiness of Candy Basket
// https://leetcode.com/problems/maximum-tastiness-of-candy-basket/

impl Solution {
    pub fn maximum_tastiness(mut price: Vec<i32>, k: i32) -> i32 {
        price.sort_unstable();
        let ok = |d: i32| {
            let mut cnt = 1;
            let mut last = price[0];
            for i in 1..price.len() {
                if price[i] - last >= d {
                    cnt += 1;
                    last = price[i];
                    if cnt >= k {
                        return true;
                    }
                }
            }
            false
        };
        let mut lo = 0;
        let mut hi = price[price.len() - 1] - price[0];
        while lo < hi {
            let mid = (lo + hi + 1) / 2;
            if ok(mid) {
                lo = mid;
            } else {
                hi = mid - 1;
            }
        }
        lo
    }
}
'''

def main():
    n = 0
    for folder, content in FILES.items():
        path = ROOT / folder / "solution.rs"
        path.write_text(content)
        n += 1
        print(f"wrote {folder}")
    print(f"total {n}")

if __name__ == "__main__":
    main()

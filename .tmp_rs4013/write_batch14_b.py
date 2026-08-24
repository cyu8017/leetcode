#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
FILES = {}

FILES["3098_find_the_sum_of_subsequence_powers"] = r'''// LeetCode 3098 - Find the Sum of Subsequence Powers
// https://leetcode.com/problems/find-the-sum-of-subsequence-powers/

use std::collections::HashMap;

impl Solution {
    pub fn sum_of_powers(mut nums: Vec<i32>, k: i32) -> i32 {
        const MOD: i32 = 1_000_000_007;
        nums.sort_unstable();
        let n = nums.len();
        let mut f = HashMap::new();
        fn dfs(
            nums: &[i32],
            n: usize,
            i: usize,
            j: usize,
            kk: i32,
            mi: i32,
            f: &mut HashMap<i64, i32>,
        ) -> i32 {
            if i >= n {
                return if kk == 0 { mi } else { 0 };
            }
            if (n - i) as i32 < kk {
                return 0;
            }
            let key = ((mi as i64) << 18) | ((i as i64) << 12) | ((j as i64) << 6) | kk as i64;
            if let Some(&v) = f.get(&key) {
                return v;
            }
            let mut ans = dfs(nums, n, i + 1, j, kk, mi, f);
            if j == n {
                ans = (ans + dfs(nums, n, i + 1, i, kk - 1, mi, f)) % MOD;
            } else {
                ans = (ans + dfs(nums, n, i + 1, i, kk - 1, mi.min(nums[i] - nums[j]), f)) % MOD;
            }
            f.insert(key, ans);
            ans
        }
        dfs(&nums, n, 0, n, k, i32::MAX, &mut f)
    }
}
'''

FILES["3099_harshad_number"] = r'''// LeetCode 3099 - Harshad Number
// https://leetcode.com/problems/harshad-number/

impl Solution {
    pub fn sum_of_the_digits_of_harshad_number(x: i32) -> i32 {
        let mut s = 0;
        let mut y = x;
        while y > 0 {
            s += y % 10;
            y /= 10;
        }
        if x % s == 0 { s } else { -1 }
    }
}
'''

FILES["3100_water_bottles_ii"] = r'''// LeetCode 3100 - Water Bottles II
// https://leetcode.com/problems/water-bottles-ii/

impl Solution {
    pub fn max_bottles_drunk(mut num_bottles: i32, mut num_exchange: i32) -> i32 {
        let mut ans = num_bottles;
        while num_bottles >= num_exchange {
            num_bottles -= num_exchange;
            num_exchange += 1;
            ans += 1;
            num_bottles += 1;
        }
        ans
    }
}
'''

FILES["3101_count_alternating_subarrays"] = r'''// LeetCode 3101 - Count Alternating Subarrays
// https://leetcode.com/problems/count-alternating-subarrays/

impl Solution {
    pub fn count_alternating_subarrays(nums: Vec<i32>) -> i64 {
        let mut ans = 1i64;
        let mut s = 1i64;
        for i in 1..nums.len() {
            if nums[i] != nums[i - 1] {
                s += 1;
            } else {
                s = 1;
            }
            ans += s;
        }
        ans
    }
}
'''

FILES["3102_minimize_manhattan_distances"] = r'''// LeetCode 3102 - Minimize Manhattan Distances
// https://leetcode.com/problems/minimize-manhattan-distances/

use std::collections::BTreeMap;

impl Solution {
    pub fn minimum_distance(points: Vec<Vec<i32>>) -> i32 {
        let mut st1: BTreeMap<i32, i32> = BTreeMap::new();
        let mut st2: BTreeMap<i32, i32> = BTreeMap::new();
        let merge = |st: &mut BTreeMap<i32, i32>, x: i32, v: i32| {
            let e = st.entry(x).or_insert(0);
            *e += v;
            if *e == 0 {
                st.remove(&x);
            }
        };
        for p in &points {
            merge(&mut st1, p[0] + p[1], 1);
            merge(&mut st2, p[0] - p[1], 1);
        }
        let mut ans = i32::MAX;
        for p in &points {
            let (x, y) = (p[0], p[1]);
            merge(&mut st1, x + y, -1);
            merge(&mut st2, x - y, -1);
            let d1 = st1.keys().next_back().copied().unwrap() - st1.keys().next().copied().unwrap();
            let d2 = st2.keys().next_back().copied().unwrap() - st2.keys().next().copied().unwrap();
            ans = ans.min(d1.max(d2));
            merge(&mut st1, x + y, 1);
            merge(&mut st2, x - y, 1);
        }
        ans
    }
}
'''

FILES["3104_find_longest_self_contained_substring"] = r'''// LeetCode 3104 - Find Longest Self-Contained Substring
// https://leetcode.com/problems/find-longest-self-contained-substring/

impl Solution {
    pub fn max_substring_length(s: String) -> i32 {
        let b = s.as_bytes();
        let n = b.len();
        let mut first = [-1i32; 26];
        let mut last = [0i32; 26];
        for i in 0..n {
            let j = (b[i] - b'a') as usize;
            if first[j] == -1 {
                first[j] = i as i32;
            }
            last[j] = i as i32;
        }
        let mut ans = -1i32;
        for k in 0..26 {
            let i = first[k];
            if i == -1 {
                continue;
            }
            let mut mx = last[k];
            for j in i as usize..n {
                let a = first[(b[j] - b'a') as usize];
                let bb = last[(b[j] - b'a') as usize];
                if a < i {
                    break;
                }
                mx = mx.max(bb);
                if mx == j as i32 && (j as i32 - i + 1) < n as i32 {
                    ans = ans.max(j as i32 - i + 1);
                }
            }
        }
        ans
    }
}
'''

FILES["3105_longest_strictly_increasing_or_strictly_decreasing_subarray"] = r'''// LeetCode 3105 - Longest Strictly Increasing or Strictly Decreasing Subarray
// https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/

impl Solution {
    pub fn longest_monotonic_subarray(nums: Vec<i32>) -> i32 {
        let mut ans = 1;
        let mut t = 1;
        for i in 1..nums.len() {
            if nums[i - 1] < nums[i] {
                t += 1;
                ans = ans.max(t);
            } else {
                t = 1;
            }
        }
        t = 1;
        for i in 1..nums.len() {
            if nums[i - 1] > nums[i] {
                t += 1;
                ans = ans.max(t);
            } else {
                t = 1;
            }
        }
        ans
    }
}
'''

FILES["3106_lexicographically_smallest_string_after_operations_with_constraint"] = r'''// LeetCode 3106 - Lexicographically Smallest String After Operations With Constraint
// https://leetcode.com/problems/lexicographically-smallest-string-after-operations-with-constraint/

impl Solution {
    pub fn get_smallest_string(s: String, mut k: i32) -> String {
        let mut s = s.into_bytes();
        for i in 0..s.len() {
            let c1 = s[i];
            for c2 in b'a'..c1 {
                let d = (c1 - c2).min(26 - (c1 - c2)) as i32;
                if d <= k {
                    s[i] = c2;
                    k -= d;
                    break;
                }
            }
        }
        String::from_utf8(s).unwrap()
    }
}
'''

FILES["3107_minimum_operations_to_make_median_of_array_equal_to_k"] = r'''// LeetCode 3107 - Minimum Operations to Make Median of Array Equal to K
// https://leetcode.com/problems/minimum-operations-to-make-median-of-array-equal-to-k/

impl Solution {
    pub fn min_operations_to_make_median_k(mut nums: Vec<i32>, k: i32) -> i64 {
        nums.sort_unstable();
        let n = nums.len();
        let m = n >> 1;
        let mut ans = (nums[m] - k).abs() as i64;
        if nums[m] > k {
            let mut i = m;
            while i > 0 && nums[i - 1] > k {
                i -= 1;
                ans += (nums[i] - k) as i64;
            }
        } else {
            for i in m + 1..n {
                if nums[i] >= k {
                    break;
                }
                ans += (k - nums[i]) as i64;
            }
        }
        ans
    }
}
'''

FILES["3108_minimum_cost_walk_in_weighted_graph"] = r'''// LeetCode 3108 - Minimum Cost Walk in Weighted Graph
// https://leetcode.com/problems/minimum-cost-walk-in-weighted-graph/

struct UnionFind {
    p: Vec<usize>,
    size: Vec<i32>,
}

impl UnionFind {
    fn new(n: usize) -> Self {
        Self { p: (0..n).collect(), size: vec![1; n] }
    }
    fn find(&mut self, x: usize) -> usize {
        if self.p[x] != x {
            self.p[x] = self.find(self.p[x]);
        }
        self.p[x]
    }
    fn unite(&mut self, a: usize, b: usize) {
        let mut pa = self.find(a);
        let mut pb = self.find(b);
        if pa == pb {
            return;
        }
        if self.size[pa] > self.size[pb] {
            self.p[pb] = pa;
            self.size[pa] += self.size[pb];
        } else {
            self.p[pa] = pb;
            self.size[pb] += self.size[pa];
        }
    }
}

impl Solution {
    pub fn minimum_cost(n: i32, edges: Vec<Vec<i32>>, query: Vec<Vec<i32>>) -> Vec<i32> {
        let n = n as usize;
        let mut uf = UnionFind::new(n);
        let mut g = vec![-1i32; n];
        for e in &edges {
            uf.unite(e[0] as usize, e[1] as usize);
        }
        for e in &edges {
            let root = uf.find(e[0] as usize);
            g[root] &= e[2];
        }
        let mut ans = Vec::with_capacity(query.len());
        for q in &query {
            let (u, v) = (q[0] as usize, q[1] as usize);
            if u == v {
                ans.push(0);
                continue;
            }
            let a = uf.find(u);
            let b = uf.find(v);
            ans.push(if a == b { g[a] } else { -1 });
        }
        ans
    }
}
'''

FILES["3109_find_the_index_of_permutation"] = r'''// LeetCode 3109 - Find the Index of Permutation
// https://leetcode.com/problems/find-the-index-of-permutation/

struct Bit {
    n: usize,
    c: Vec<i32>,
}

impl Bit {
    fn new(n: usize) -> Self {
        Self { n, c: vec![0; n + 1] }
    }
    fn update(&mut self, mut x: usize, delta: i32) {
        while x <= self.n {
            self.c[x] += delta;
            x += x & x.wrapping_neg();
        }
    }
    fn query(&self, mut x: usize) -> i32 {
        let mut s = 0;
        while x > 0 {
            s += self.c[x];
            x -= x & x.wrapping_neg();
        }
        s
    }
}

impl Solution {
    pub fn get_permutation_index(perm: Vec<i32>) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let n = perm.len();
        let mut tree = Bit::new(n + 1);
        let mut f = vec![0i64; n];
        f[0] = 1;
        for i in 1..n {
            f[i] = f[i - 1] * i as i64 % MOD;
        }
        let mut ans = 0i64;
        for i in 0..n {
            let x = perm[i] as usize;
            let cnt = x as i64 - 1 - tree.query(x) as i64;
            ans = (ans + cnt * f[n - 1 - i]) % MOD;
            tree.update(x, 1);
        }
        ans as i32
    }
}
'''

FILES["3110_score_of_a_string"] = r'''// LeetCode 3110 - Score of a String
// https://leetcode.com/problems/score-of-a-string/

impl Solution {
    pub fn score_of_string(s: String) -> i32 {
        let b = s.as_bytes();
        let mut ans = 0;
        for i in 1..b.len() {
            ans += (b[i - 1] as i32 - b[i] as i32).abs();
        }
        ans
    }
}
'''

FILES["3111_minimum_rectangles_to_cover_points"] = r'''// LeetCode 3111 - Minimum Rectangles to Cover Points
// https://leetcode.com/problems/minimum-rectangles-to-cover-points/

impl Solution {
    pub fn min_rectangles_to_cover_points(mut points: Vec<Vec<i32>>, w: i32) -> i32 {
        points.sort_unstable_by_key(|p| p[0]);
        let mut ans = 0;
        let mut x1 = -1;
        for p in points {
            if p[0] > x1 {
                ans += 1;
                x1 = p[0] + w;
            }
        }
        ans
    }
}
'''

FILES["3112_minimum_time_to_visit_disappearing_nodes"] = r'''// LeetCode 3112 - Minimum Time to Visit Disappearing Nodes
// https://leetcode.com/problems/minimum-time-to-visit-disappearing-nodes/

use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn minimum_time(n: i32, edges: Vec<Vec<i32>>, disappear: Vec<i32>) -> Vec<i32> {
        let n = n as usize;
        let mut g = vec![Vec::new(); n];
        for e in &edges {
            g[e[0] as usize].push((e[1] as usize, e[2]));
            g[e[1] as usize].push((e[0] as usize, e[2]));
        }
        const INF: i32 = 1 << 30;
        let mut dist = vec![INF; n];
        dist[0] = 0;
        let mut pq = BinaryHeap::new();
        pq.push(Reverse((0i32, 0usize)));
        while let Some(Reverse((du, u))) = pq.pop() {
            if du > dist[u] {
                continue;
            }
            for &(v, w) in &g[u] {
                if dist[v] > dist[u] + w && dist[u] + w < disappear[v] {
                    dist[v] = dist[u] + w;
                    pq.push(Reverse((dist[v], v)));
                }
            }
        }
        (0..n).map(|i| if dist[i] < disappear[i] { dist[i] } else { -1 }).collect()
    }
}
'''

FILES["3113_find_the_number_of_subarrays_where_boundary_elements_are_maximum"] = r'''// LeetCode 3113 - Find the Number of Subarrays Where Boundary Elements Are Maximum
// https://leetcode.com/problems/find-the-number-of-subarrays-where-boundary-elements-are-maximum/

impl Solution {
    pub fn number_of_subarrays(nums: Vec<i32>) -> i64 {
        let mut stk: Vec<(i32, i64)> = Vec::new();
        let mut ans = 0i64;
        for x in nums {
            while !stk.is_empty() && stk.last().unwrap().0 < x {
                stk.pop();
            }
            if stk.is_empty() || stk.last().unwrap().0 > x {
                stk.push((x, 1));
            } else {
                stk.last_mut().unwrap().1 += 1;
            }
            ans += stk.last().unwrap().1;
        }
        ans
    }
}
'''

FILES["3114_latest_time_you_can_obtain_after_replacing_characters"] = r'''// LeetCode 3114 - Latest Time You Can Obtain After Replacing Characters
// https://leetcode.com/problems/latest-time-you-can-obtain-after-replacing-characters/

impl Solution {
    pub fn find_latest_time(s: String) -> String {
        let sb = s.as_bytes();
        for h in (0..=11).rev() {
            for m in (0..=59).rev() {
                let t = format!("{:02}:{:02}", h, m);
                let tb = t.as_bytes();
                let mut ok = true;
                for i in 0..5 {
                    if sb[i] != b'?' && sb[i] != tb[i] {
                        ok = false;
                        break;
                    }
                }
                if ok {
                    return t;
                }
            }
        }
        String::new()
    }
}
'''

FILES["3115_maximum_prime_difference"] = r'''// LeetCode 3115 - Maximum Prime Difference
// https://leetcode.com/problems/maximum-prime-difference/

impl Solution {
    fn is_prime(n: i32) -> bool {
        if n < 2 {
            return false;
        }
        let mut i = 2;
        while i <= n / i {
            if n % i == 0 {
                return false;
            }
            i += 1;
        }
        true
    }

    pub fn maximum_prime_difference(nums: Vec<i32>) -> i32 {
        let mut i = 0;
        loop {
            if Self::is_prime(nums[i]) {
                let mut j = nums.len() - 1;
                loop {
                    if Self::is_prime(nums[j]) {
                        return (j - i) as i32;
                    }
                    j -= 1;
                }
            }
            i += 1;
        }
    }
}
'''

FILES["3116_kth_smallest_amount_with_single_denomination_combination"] = r'''// LeetCode 3116 - Kth Smallest Amount With Single Denomination Combination
// https://leetcode.com/problems/kth-smallest-amount-with-single-denomination-combination/

impl Solution {
    fn gcdll(mut a: i64, mut b: i64) -> i64 {
        while b != 0 {
            let t = a % b;
            a = b;
            b = t;
        }
        a
    }
    fn lcmll(a: i64, b: i64) -> i64 {
        a / Self::gcdll(a, b) * b
    }

    pub fn find_kth_smallest(coins: Vec<i32>, k: i32) -> i64 {
        let r = 100_000_000_000i64;
        let n = coins.len();
        let check = |mx: i64| -> bool {
            let mut cnt = 0i64;
            for i in 1..(1 << n) {
                let mut v = 1i64;
                for j in 0..n {
                    if (i >> j) & 1 == 1 {
                        v = Self::lcmll(v, coins[j] as i64);
                        if v > mx {
                            break;
                        }
                    }
                }
                let m = i.count_ones();
                if m % 2 == 1 {
                    cnt += mx / v;
                } else {
                    cnt -= mx / v;
                }
            }
            cnt >= k as i64
        };
        let mut lo = 1i64;
        let mut hi = r;
        while lo < hi {
            let mid = lo + (hi - lo) / 2;
            if check(mid) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        lo
    }
}
'''

FILES["3117_minimum_sum_of_values_by_dividing_array"] = r'''// LeetCode 3117 - Minimum Sum of Values by Dividing Array
// https://leetcode.com/problems/minimum-sum-of-values-by-dividing-array/

use std::collections::HashMap;

impl Solution {
    pub fn minimum_value_sum(nums: Vec<i32>, and_values: Vec<i32>) -> i32 {
        let n = nums.len();
        let m = and_values.len();
        const INF: i32 = 1 << 29;
        let mut f = HashMap::new();
        fn dfs(
            nums: &[i32],
            and_values: &[i32],
            n: usize,
            m: usize,
            i: usize,
            j: usize,
            mut a: i32,
            f: &mut HashMap<i64, i32>,
        ) -> i32 {
            if n - i < m - j {
                return 1 << 29;
            }
            if j == m {
                return if i == n { 0 } else { 1 << 29 };
            }
            a &= nums[i];
            if a < and_values[j] {
                return 1 << 29;
            }
            let key = ((i as i64) << 36) | ((j as i64) << 32) | (a as u32 as i64);
            if let Some(&v) = f.get(&key) {
                return v;
            }
            let mut ans = dfs(nums, and_values, n, m, i + 1, j, a, f);
            if a == and_values[j] {
                ans = ans.min(dfs(nums, and_values, n, m, i + 1, j + 1, -1, f) + nums[i]);
            }
            f.insert(key, ans);
            ans
        }
        let ans = dfs(&nums, &and_values, n, m, 0, 0, -1, &mut f);
        if ans < INF { ans } else { -1 }
    }
}
'''

FILES["3119_maximum_number_of_potholes_that_can_be_fixed"] = r'''// LeetCode 3119 - Maximum Number of Potholes That Can Be Fixed
// https://leetcode.com/problems/maximum-number-of-potholes-that-can-be-fixed/

impl Solution {
    pub fn max_potholes(road: String, mut budget: i32) -> i32 {
        let mut road = road.into_bytes();
        road.push(b'.');
        let n = road.len();
        let mut cnt = vec![0i32; n];
        let mut k = 0i32;
        let mut ans = 0i32;
        for &c in &road {
            if c == b'x' {
                k += 1;
            } else if k > 0 {
                cnt[k as usize] += 1;
                k = 0;
            }
        }
        k = n as i32 - 1;
        while k > 0 && budget > 0 {
            let t = (budget / (k + 1)).min(cnt[k as usize]);
            ans += t * k;
            budget -= t * (k + 1);
            cnt[(k - 1) as usize] += cnt[k as usize] - t;
            k -= 1;
        }
        ans
    }
}
'''

FILES["3120_count_the_number_of_special_characters_i"] = r'''// LeetCode 3120 - Count the Number of Special Characters I
// https://leetcode.com/problems/count-the-number-of-special-characters-i/

impl Solution {
    pub fn number_of_special_chars(word: String) -> i32 {
        let mut s = [false; 128];
        for c in word.bytes() {
            s[c as usize] = true;
        }
        let mut ans = 0;
        for i in 0..26 {
            if s[b'a' as usize + i] && s[b'A' as usize + i] {
                ans += 1;
            }
        }
        ans
    }
}
'''

FILES["3121_count_the_number_of_special_characters_ii"] = r'''// LeetCode 3121 - Count the Number of Special Characters II
// https://leetcode.com/problems/count-the-number-of-special-characters-ii/

impl Solution {
    pub fn number_of_special_chars(word: String) -> i32 {
        let mut first = [0i32; 128];
        let mut last = [0i32; 128];
        for (i, c) in word.bytes().enumerate() {
            if first[c as usize] == 0 {
                first[c as usize] = i as i32 + 1;
            }
            last[c as usize] = i as i32 + 1;
        }
        let mut ans = 0;
        for i in 0..26 {
            if last[b'a' as usize + i] > 0 && last[b'a' as usize + i] < first[b'A' as usize + i] {
                ans += 1;
            }
        }
        ans
    }
}
'''

FILES["3122_minimum_number_of_operations_to_satisfy_conditions"] = r'''// LeetCode 3122 - Minimum Number of Operations to Satisfy Conditions
// https://leetcode.com/problems/minimum-number-of-operations-to-satisfy-conditions/

impl Solution {
    pub fn minimum_operations(grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        const INF: i32 = 1 << 29;
        let mut f = vec![vec![INF; 10]; n];
        for i in 0..n {
            let mut cnt = [0i32; 10];
            for j in 0..m {
                cnt[grid[j][i] as usize] += 1;
            }
            if i == 0 {
                for j in 0..10 {
                    f[i][j] = m as i32 - cnt[j];
                }
            } else {
                for j in 0..10 {
                    for k in 0..10 {
                        if j != k {
                            f[i][j] = f[i][j].min(f[i - 1][k] + m as i32 - cnt[j]);
                        }
                    }
                }
            }
        }
        *f[n - 1].iter().min().unwrap()
    }
}
'''

FILES["3123_find_edges_in_shortest_paths"] = r'''// LeetCode 3123 - Find Edges in Shortest Paths
// https://leetcode.com/problems/find-edges-in-shortest-paths/

use std::cmp::Reverse;
use std::collections::{BinaryHeap, VecDeque};

impl Solution {
    pub fn find_answer(n: i32, edges: Vec<Vec<i32>>) -> Vec<bool> {
        let n = n as usize;
        let mut g = vec![Vec::new(); n];
        for (i, e) in edges.iter().enumerate() {
            let (a, b, w) = (e[0] as usize, e[1] as usize, e[2]);
            g[a].push((b, w, i));
            g[b].push((a, w, i));
        }
        const INF: i32 = 1 << 30;
        let mut dist = vec![INF; n];
        dist[0] = 0;
        let mut pq = BinaryHeap::new();
        pq.push(Reverse((0i32, 0usize)));
        while let Some(Reverse((da, a))) = pq.pop() {
            if da > dist[a] {
                continue;
            }
            for &(b, w, _) in &g[a] {
                if dist[b] > dist[a] + w {
                    dist[b] = dist[a] + w;
                    pq.push(Reverse((dist[b], b)));
                }
            }
        }
        let mut ans = vec![false; edges.len()];
        if dist[n - 1] == INF {
            return ans;
        }
        let mut q = VecDeque::new();
        q.push_back(n - 1);
        while let Some(a) = q.pop_front() {
            for &(b, w, i) in &g[a] {
                if dist[a] == dist[b] + w {
                    ans[i] = true;
                    q.push_back(b);
                }
            }
        }
        ans
    }
}
'''

FILES["3125_maximum_number_that_makes_result_of_bitwise_and_zero"] = r'''// LeetCode 3125 - Maximum Number That Makes Result of Bitwise AND Zero
// https://leetcode.com/problems/maximum-number-that-makes-result-of-bitwise-and-zero/

impl Solution {
    pub fn max_number(n: i64) -> i64 {
        let len = 64 - (n as u64).leading_zeros();
        (1i64 << (len - 1)) - 1
    }
}
'''

FILES["3127_make_a_square_with_the_same_color"] = r'''// LeetCode 3127 - Make a Square with the Same Color
// https://leetcode.com/problems/make-a-square-with-the-same-color/

impl Solution {
    pub fn can_make_square(grid: Vec<Vec<char>>) -> bool {
        let dirs = [0, 0, 1, 1, 0];
        for i in 0..2 {
            for j in 0..2 {
                let mut cnt1 = 0;
                let mut cnt2 = 0;
                for k in 0..4 {
                    let x = i + dirs[k];
                    let y = j + dirs[k + 1];
                    if grid[x][y] == 'W' {
                        cnt1 += 1;
                    } else {
                        cnt2 += 1;
                    }
                }
                if cnt1 != cnt2 {
                    return true;
                }
            }
        }
        false
    }
}
'''

FILES["3128_right_triangles"] = r'''// LeetCode 3128 - Right Triangles
// https://leetcode.com/problems/right-triangles/

impl Solution {
    pub fn number_of_right_triangles(grid: Vec<Vec<i32>>) -> i64 {
        let m = grid.len();
        let n = grid[0].len();
        let mut rows = vec![0i32; m];
        let mut cols = vec![0i32; n];
        for i in 0..m {
            for j in 0..n {
                rows[i] += grid[i][j];
                cols[j] += grid[i][j];
            }
        }
        let mut ans = 0i64;
        for i in 0..m {
            for j in 0..n {
                if grid[i][j] == 1 {
                    ans += (rows[i] - 1) as i64 * (cols[j] - 1) as i64;
                }
            }
        }
        ans
    }
}
'''

FILES["3129_find_all_possible_stable_binary_arrays_i"] = r'''// LeetCode 3129 - Find All Possible Stable Binary Arrays I
// https://leetcode.com/problems/find-all-possible-stable-binary-arrays-i/

impl Solution {
    pub fn number_of_stable_arrays(zero: i32, one: i32, limit: i32) -> i32 {
        const MOD: i32 = 1_000_000_007;
        let mut f = vec![vec![[-1i32, -1]; one as usize + 1]; zero as usize + 1];
        fn dfs(i: i32, j: i32, k: usize, limit: i32, f: &mut Vec<Vec<[i32; 2]>>) -> i32 {
            const MOD: i32 = 1_000_000_007;
            if i < 0 || j < 0 {
                return 0;
            }
            if i == 0 {
                return if k == 1 && j <= limit { 1 } else { 0 };
            }
            if j == 0 {
                return if k == 0 && i <= limit { 1 } else { 0 };
            }
            if f[i as usize][j as usize][k] != -1 {
                return f[i as usize][j as usize][k];
            }
            let res = if k == 0 {
                (dfs(i - 1, j, 0, limit, f) + dfs(i - 1, j, 1, limit, f)
                    - dfs(i - limit - 1, j, 1, limit, f) + MOD)
                    % MOD
            } else {
                (dfs(i, j - 1, 0, limit, f) + dfs(i, j - 1, 1, limit, f)
                    - dfs(i, j - limit - 1, 0, limit, f) + MOD)
                    % MOD
            };
            f[i as usize][j as usize][k] = res;
            res
        }
        (dfs(zero, one, 0, limit, &mut f) + dfs(zero, one, 1, limit, &mut f)) % MOD
    }
}
'''

FILES["3130_find_all_possible_stable_binary_arrays_ii"] = r'''// LeetCode 3130 - Find All Possible Stable Binary Arrays II
// https://leetcode.com/problems/find-all-possible-stable-binary-arrays-ii/

impl Solution {
    pub fn number_of_stable_arrays(zero: i32, one: i32, limit: i32) -> i32 {
        const MOD: i32 = 1_000_000_007;
        let mut f = vec![vec![[-1i32, -1]; one as usize + 1]; zero as usize + 1];
        fn dfs(i: i32, j: i32, k: usize, limit: i32, f: &mut Vec<Vec<[i32; 2]>>) -> i32 {
            const MOD: i32 = 1_000_000_007;
            if i < 0 || j < 0 {
                return 0;
            }
            if i == 0 {
                return if k == 1 && j <= limit { 1 } else { 0 };
            }
            if j == 0 {
                return if k == 0 && i <= limit { 1 } else { 0 };
            }
            if f[i as usize][j as usize][k] != -1 {
                return f[i as usize][j as usize][k];
            }
            let res = if k == 0 {
                (dfs(i - 1, j, 0, limit, f) + dfs(i - 1, j, 1, limit, f)
                    - dfs(i - limit - 1, j, 1, limit, f) + MOD)
                    % MOD
            } else {
                (dfs(i, j - 1, 0, limit, f) + dfs(i, j - 1, 1, limit, f)
                    - dfs(i, j - limit - 1, 0, limit, f) + MOD)
                    % MOD
            };
            f[i as usize][j as usize][k] = res;
            res
        }
        (dfs(zero, one, 0, limit, &mut f) + dfs(zero, one, 1, limit, &mut f)) % MOD
    }
}
'''

FILES["3131_find_the_integer_added_to_array_i"] = r'''// LeetCode 3131 - Find the Integer Added to Array I
// https://leetcode.com/problems/find-the-integer-added-to-array-i/

impl Solution {
    pub fn added_integer(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        nums2.iter().copied().min().unwrap() - nums1.iter().copied().min().unwrap()
    }
}
'''

FILES["3132_find_the_integer_added_to_array_ii"] = r'''// LeetCode 3132 - Find the Integer Added to Array II
// https://leetcode.com/problems/find-the-integer-added-to-array-ii/

impl Solution {
    pub fn minimum_added_integer(mut nums1: Vec<i32>, mut nums2: Vec<i32>) -> i32 {
        nums1.sort_unstable();
        nums2.sort_unstable();
        let mut ans = 1 << 30;
        let f = |x: i32| -> bool {
            let mut i = 0usize;
            let mut j = 0usize;
            let mut cnt = 0;
            while i < nums1.len() && j < nums2.len() {
                if nums2[j] - nums1[i] != x {
                    cnt += 1;
                } else {
                    j += 1;
                }
                i += 1;
            }
            cnt <= 2
        };
        for t in 0..3 {
            let x = nums2[0] - nums1[t];
            if f(x) {
                ans = ans.min(x);
            }
        }
        ans
    }
}
'''

FILES["3133_minimum_array_end"] = r'''// LeetCode 3133 - Minimum Array End
// https://leetcode.com/problems/minimum-array-end/

impl Solution {
    pub fn min_end(mut n: i32, x: i32) -> i64 {
        n -= 1;
        let mut ans = x as i64;
        for i in 0..31 {
            if ((x >> i) & 1) == 0 {
                ans |= ((n & 1) as i64) << i;
                n >>= 1;
            }
        }
        ans |= (n as i64) << 31;
        ans
    }
}
'''

def main():
    n = 0
    for folder, content in FILES.items():
        path = ROOT / folder / "solution.rs"
        path.write_text(content, encoding="utf-8", newline="\n")
        n += 1
        print("wrote", folder)
    print("total", n)

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
FILES = {}

FILES["2593_find_score_of_an_array_after_marking_all_elements"] = r'''// LeetCode 2593 - Find Score of an Array After Marking All Elements
// https://leetcode.com/problems/find-score-of-an-array-after-marking-all-elements/

impl Solution {
    pub fn find_score(nums: Vec<i32>) -> i64 {
        let n = nums.len();
        let mut idx: Vec<usize> = (0..n).collect();
        idx.sort_by(|&a, &b| nums[a].cmp(&nums[b]).then(a.cmp(&b)));
        let mut marked = vec![false; n];
        let mut ans = 0i64;
        for i in idx {
            if marked[i] {
                continue;
            }
            ans += nums[i] as i64;
            marked[i] = true;
            if i > 0 {
                marked[i - 1] = true;
            }
            if i + 1 < n {
                marked[i + 1] = true;
            }
        }
        ans
    }
}
'''

FILES["2594_minimum_time_to_repair_cars"] = r'''// LeetCode 2594 - Minimum Time to Repair Cars
// https://leetcode.com/problems/minimum-time-to-repair-cars/

impl Solution {
    pub fn repair_cars(ranks: Vec<i32>, cars: i32) -> i64 {
        let cars = cars as i64;
        let ok = |t: i64| {
            let mut done = 0i64;
            for &r in &ranks {
                let mut lo = 0i64;
                let mut hi = cars;
                while lo < hi {
                    let mid = (lo + hi + 1) / 2;
                    if r as i64 * mid * mid <= t {
                        lo = mid;
                    } else {
                        hi = mid - 1;
                    }
                }
                done += lo;
                if done >= cars {
                    return true;
                }
            }
            done >= cars
        };
        let mn = *ranks.iter().min().unwrap() as i64;
        let mut lo = 1i64;
        let mut hi = mn * cars * cars;
        while lo < hi {
            let mid = (lo + hi) / 2;
            if ok(mid) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        lo
    }
}
'''

FILES["2595_number_of_even_and_odd_bits"] = r'''// LeetCode 2595 - Number of Even and Odd Bits
// https://leetcode.com/problems/number-of-even-and-odd-bits/

impl Solution {
    pub fn even_odd_bit(mut n: i32) -> Vec<i32> {
        let mut even = 0;
        let mut odd = 0;
        let mut i = 0;
        while n > 0 {
            if n & 1 == 1 {
                if i % 2 == 0 {
                    even += 1;
                } else {
                    odd += 1;
                }
            }
            n >>= 1;
            i += 1;
        }
        vec![even, odd]
    }
}
'''

FILES["2596_check_knight_tour_configuration"] = r'''// LeetCode 2596 - Check Knight Tour Configuration
// https://leetcode.com/problems/check-knight-tour-configuration/

impl Solution {
    pub fn check_valid_grid(grid: Vec<Vec<i32>>) -> bool {
        let n = grid.len();
        if grid[0][0] != 0 {
            return false;
        }
        let mut pos = vec![(0, 0); n * n];
        for i in 0..n {
            for j in 0..n {
                pos[grid[i][j] as usize] = (i as i32, j as i32);
            }
        }
        let dirs = [
            (1, 2),
            (1, -2),
            (-1, 2),
            (-1, -2),
            (2, 1),
            (2, -1),
            (-2, 1),
            (-2, -1),
        ];
        for v in 0..n * n - 1 {
            let (r, c) = pos[v];
            let mut ok = false;
            for (dr, dc) in dirs {
                if r + dr == pos[v + 1].0 && c + dc == pos[v + 1].1 {
                    ok = true;
                    break;
                }
            }
            if !ok {
                return false;
            }
        }
        true
    }
}
'''

FILES["2597_the_number_of_beautiful_subsets"] = r'''// LeetCode 2597 - The Number of Beautiful Subsets
// https://leetcode.com/problems/the-number-of-beautiful-subsets/

use std::collections::HashMap;

impl Solution {
    pub fn beautiful_subsets(nums: Vec<i32>, k: i32) -> i32 {
        let mut freq = HashMap::new();
        for x in nums {
            *freq.entry(x).or_insert(0) += 1;
        }
        let mut groups: HashMap<i32, Vec<i32>> = HashMap::new();
        for &x in freq.keys() {
            groups.entry(x % k).or_default().push(x);
        }
        let mut ans = 1;
        for vals in groups.values_mut() {
            vals.sort_unstable();
            let mut prev_take = 0;
            let mut prev_skip = 1;
            let mut prev_val = i32::MIN / 2;
            for &v in vals.iter() {
                let mut ways = 1;
                for _ in 0..freq[&v] {
                    ways *= 2;
                }
                ways -= 1;
                let skip = prev_take + prev_skip;
                let mut take = ways * prev_skip;
                if prev_val + k != v {
                    take += ways * prev_take;
                }
                prev_take = take;
                prev_skip = skip;
                prev_val = v;
            }
            ans *= prev_take + prev_skip;
        }
        ans - 1
    }
}
'''

FILES["2598_smallest_missing_non_negative_integer_after_operations"] = r'''// LeetCode 2598 - Smallest Missing Non-negative Integer After Operations
// https://leetcode.com/problems/smallest-missing-non-negative-integer-after-operations/

impl Solution {
    pub fn find_smallest_integer(nums: Vec<i32>, value: i32) -> i32 {
        let value = value as usize;
        let mut cnt = vec![0; value];
        for x in nums {
            let mut r = x % value as i32;
            if r < 0 {
                r += value as i32;
            }
            cnt[r as usize] += 1;
        }
        let mut mex = 0;
        while cnt[mex % value] > 0 {
            cnt[mex % value] -= 1;
            mex += 1;
        }
        mex as i32
    }
}
'''

FILES["2599_make_the_prefix_sum_non_negative"] = r'''// LeetCode 2599 - Make the Prefix Sum Non-negative
// https://leetcode.com/problems/make-the-prefix-sum-non-negative/

use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn make_pref_sum_non_negative(nums: Vec<i32>) -> i32 {
        let mut h: BinaryHeap<Reverse<i32>> = BinaryHeap::new();
        let mut sum = 0i64;
        let mut ans = 0;
        for x in nums {
            sum += x as i64;
            if x < 0 {
                h.push(Reverse(x));
            }
            if sum < 0 {
                let worst = h.pop().unwrap().0;
                sum -= worst as i64;
                ans += 1;
            }
        }
        ans
    }
}
'''

FILES["2600_k_items_with_the_maximum_sum"] = r'''// LeetCode 2600 - K Items With the Maximum Sum
// https://leetcode.com/problems/k-items-with-the-maximum-sum/

impl Solution {
    pub fn k_items_with_maximum_sum(num_ones: i32, num_zeros: i32, num_neg_ones: i32, mut k: i32) -> i32 {
        let mut ans = 0;
        let take = num_ones.min(k);
        ans += take;
        k -= take;
        let take = num_zeros.min(k);
        k -= take;
        let take = num_neg_ones.min(k);
        ans -= take;
        ans
    }
}
'''

FILES["2601_prime_subtraction_operation"] = r'''// LeetCode 2601 - Prime Subtraction Operation
// https://leetcode.com/problems/prime-subtraction-operation/

impl Solution {
    pub fn prime_sub_operation(nums: Vec<i32>) -> bool {
        let max_v = *nums.iter().max().unwrap() as usize;
        let mut is_p = vec![true; max_v + 1];
        if max_v >= 0 {
            is_p[0] = false;
        }
        if max_v >= 1 {
            is_p[1] = false;
        }
        let mut i = 2;
        while i * i <= max_v {
            if is_p[i] {
                let mut j = i * i;
                while j <= max_v {
                    is_p[j] = false;
                    j += i;
                }
            }
            i += 1;
        }
        let primes: Vec<i32> = (2..=max_v).filter(|&i| is_p[i]).map(|i| i as i32).collect();
        let mut prev = 0;
        for x in nums {
            if x <= prev {
                return false;
            }
            let mut best = x;
            for &p in &primes {
                if p >= x {
                    break;
                }
                if x - p > prev {
                    best = x - p;
                }
            }
            prev = best;
        }
        true
    }
}
'''

FILES["2602_minimum_operations_to_make_all_array_elements_equal"] = r'''// LeetCode 2602 - Minimum Operations to Make All Array Elements Equal
// https://leetcode.com/problems/minimum-operations-to-make-all-array-elements-equal/

impl Solution {
    pub fn min_operations(mut nums: Vec<i32>, queries: Vec<i32>) -> Vec<i64> {
        nums.sort_unstable();
        let n = nums.len();
        let mut pref = vec![0i64; n + 1];
        for i in 0..n {
            pref[i + 1] = pref[i] + nums[i] as i64;
        }
        queries
            .into_iter()
            .map(|q| {
                let i = nums.partition_point(|&x| x < q);
                let left = q as i64 * i as i64 - pref[i];
                let right = pref[n] - pref[i] - q as i64 * (n - i) as i64;
                left + right
            })
            .collect()
    }
}
'''

FILES["2603_collect_coins_in_a_tree"] = r'''// LeetCode 2603 - Collect Coins in a Tree
// https://leetcode.com/problems/collect-coins-in-a-tree/

use std::collections::{HashSet, VecDeque};

impl Solution {
    pub fn collect_the_coins(coins: Vec<i32>, edges: Vec<Vec<i32>>) -> i32 {
        let n = coins.len();
        let mut g: Vec<HashSet<i32>> = vec![HashSet::new(); n];
        for e in edges {
            g[e[0] as usize].insert(e[1]);
            g[e[1] as usize].insert(e[0]);
        }
        let mut deg: Vec<i32> = g.iter().map(|s| s.len() as i32).collect();
        let mut q = VecDeque::new();
        for i in 0..n {
            if deg[i] == 1 && coins[i] == 0 {
                q.push_back(i);
            }
        }
        while let Some(u) = q.pop_front() {
            let neigh: Vec<i32> = g[u].iter().copied().collect();
            for v in neigh {
                g[v as usize].remove(&(u as i32));
                deg[v as usize] -= 1;
                if deg[v as usize] == 1 && coins[v as usize] == 0 {
                    q.push_back(v as usize);
                }
            }
            g[u].clear();
            deg[u] = 0;
        }
        for _ in 0..2 {
            let leaves: Vec<usize> = (0..n).filter(|&i| deg[i] == 1).collect();
            for u in leaves {
                let neigh: Vec<i32> = g[u].iter().copied().collect();
                for v in neigh {
                    g[v as usize].remove(&(u as i32));
                    deg[v as usize] -= 1;
                }
                g[u].clear();
                deg[u] = 0;
            }
        }
        let mut remain = 0;
        for s in g {
            remain += s.len() as i32;
        }
        remain
    }
}
'''

FILES["2604_minimum_time_to_eat_all_grains"] = r'''// LeetCode 2604 - Minimum Time to Eat All Grains
// https://leetcode.com/problems/minimum-time-to-eat-all-grains/

impl Solution {
    pub fn minimum_time(mut hens: Vec<i32>, mut grains: Vec<i32>) -> i32 {
        hens.sort_unstable();
        grains.sort_unstable();
        let ok = |t: i32| {
            let mut j = 0;
            for &h in &hens {
                if j >= grains.len() {
                    return true;
                }
                if grains[j] >= h {
                    while j < grains.len() && grains[j] - h <= t {
                        j += 1;
                    }
                } else {
                    if h - grains[j] > t {
                        return false;
                    }
                    let left = h - grains[j];
                    let max_right1 = t - 2 * left;
                    let max_right2 = (t - left) / 2;
                    let mut reach = h;
                    if max_right1 > max_right2 {
                        if max_right1 > 0 {
                            reach = h + max_right1;
                        }
                    } else if max_right2 > 0 {
                        reach = h + max_right2;
                    }
                    while j < grains.len() && grains[j] <= reach {
                        j += 1;
                    }
                }
            }
            j >= grains.len()
        };
        let mut lo = 0i32;
        let mut hi = 2_000_000_000i32;
        while lo < hi {
            let mid = lo + (hi - lo) / 2;
            if ok(mid) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        lo
    }
}
'''

FILES["2605_form_smallest_number_from_two_digit_arrays"] = r'''// LeetCode 2605 - Form Smallest Number From Two Digit Arrays
// https://leetcode.com/problems/form-smallest-number-from-two-digit-arrays/

use std::collections::HashSet;

impl Solution {
    pub fn min_number(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        let s1: HashSet<i32> = nums1.iter().copied().collect();
        let s2: HashSet<i32> = nums2.iter().copied().collect();
        let mut best_shared = 10;
        for d in 1..=9 {
            if s1.contains(&d) && s2.contains(&d) && d < best_shared {
                best_shared = d;
            }
        }
        if best_shared < 10 {
            return best_shared;
        }
        let m1 = *nums1.iter().min().unwrap();
        let m2 = *nums2.iter().min().unwrap();
        if m1 < m2 {
            m1 * 10 + m2
        } else {
            m2 * 10 + m1
        }
    }
}
'''

FILES["2606_find_the_substring_with_maximum_cost"] = r'''// LeetCode 2606 - Find the Substring With Maximum Cost
// https://leetcode.com/problems/find-the-substring-with-maximum-cost/

impl Solution {
    pub fn maximum_cost_substring(s: String, chars: String, vals: Vec<i32>) -> i32 {
        let mut val = [0i32; 26];
        for i in 0..26 {
            val[i] = i as i32 + 1;
        }
        for (i, c) in chars.bytes().enumerate() {
            val[(c - b'a') as usize] = vals[i];
        }
        let mut best = 0;
        let mut cur = 0;
        for c in s.bytes() {
            cur += val[(c - b'a') as usize];
            if cur < 0 {
                cur = 0;
            }
            if cur > best {
                best = cur;
            }
        }
        best
    }
}
'''

FILES["2607_make_k_subarray_sums_equal"] = r'''// LeetCode 2607 - Make K-Subarray Sums Equal
// https://leetcode.com/problems/make-k-subarray-sums-equal/

impl Solution {
    pub fn make_sub_k_sum_equal(arr: Vec<i32>, k: i32) -> i64 {
        fn gcd(mut a: usize, mut b: usize) -> usize {
            while b != 0 {
                let t = a % b;
                a = b;
                b = t;
            }
            a
        }
        let n = arr.len();
        let g = gcd(n, k as usize);
        let mut ans = 0i64;
        for r in 0..g {
            let mut group = Vec::new();
            let mut i = r;
            while i < n {
                group.push(arr[i]);
                i += g;
            }
            group.sort_unstable();
            let med = group[group.len() / 2];
            for x in group {
                ans += (x - med).abs() as i64;
            }
        }
        ans
    }
}
'''

FILES["2608_shortest_cycle_in_a_graph"] = r'''// LeetCode 2608 - Shortest Cycle in a Graph
// https://leetcode.com/problems/shortest-cycle-in-a-graph/

use std::collections::VecDeque;

impl Solution {
    pub fn find_shortest_cycle(n: i32, edges: Vec<Vec<i32>>) -> i32 {
        let n = n as usize;
        let mut g = vec![Vec::new(); n];
        for e in edges {
            g[e[0] as usize].push(e[1] as usize);
            g[e[1] as usize].push(e[0] as usize);
        }
        const INF: i32 = 1_000_000_000;
        let mut ans = INF;
        for start in 0..n {
            let mut dist = vec![-1; n];
            let mut parent = vec![-1i32; n];
            let mut q = VecDeque::new();
            q.push_back(start);
            dist[start] = 0;
            while let Some(u) = q.pop_front() {
                for &v in &g[u] {
                    if dist[v] < 0 {
                        dist[v] = dist[u] + 1;
                        parent[v] = u as i32;
                        q.push_back(v);
                    } else if parent[u] != v as i32 {
                        let c = dist[u] + dist[v] + 1;
                        if c < ans {
                            ans = c;
                        }
                    }
                }
            }
        }
        if ans == INF {
            -1
        } else {
            ans
        }
    }
}
'''

FILES["2609_find_the_longest_balanced_substring_of_a_binary_string"] = r'''// LeetCode 2609 - Find the Longest Balanced Substring of a Binary String
// https://leetcode.com/problems/find-the-longest-balanced-substring-of-a-binary-string/

impl Solution {
    pub fn find_the_longest_balanced_substring(s: String) -> i32 {
        let mut ans = 0;
        let mut zeros = 0;
        let mut ones = 0;
        for c in s.bytes() {
            if c == b'0' {
                if ones > 0 {
                    zeros = 0;
                    ones = 0;
                }
                zeros += 1;
            } else {
                ones += 1;
                let cur = ones.min(zeros);
                if 2 * cur > ans {
                    ans = 2 * cur;
                }
            }
        }
        ans
    }
}
'''

FILES["2610_convert_an_array_into_a_2d_array_with_conditions"] = r'''// LeetCode 2610 - Convert an Array Into a 2D Array With Conditions
// https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/

use std::collections::HashMap;

impl Solution {
    pub fn find_matrix(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut freq = HashMap::new();
        let mut ans: Vec<Vec<i32>> = Vec::new();
        for x in nums {
            let f = *freq.get(&x).unwrap_or(&0);
            if f == ans.len() {
                ans.push(Vec::new());
            }
            ans[f].push(x);
            *freq.entry(x).or_insert(0) += 1;
        }
        ans
    }
}
'''

FILES["2611_mice_and_cheese"] = r'''// LeetCode 2611 - Mice and Cheese
// https://leetcode.com/problems/mice-and-cheese/

impl Solution {
    pub fn mice_and_cheese(reward1: Vec<i32>, reward2: Vec<i32>, k: i32) -> i32 {
        let n = reward1.len();
        let mut diff = vec![0; n];
        let mut ans = 0;
        for i in 0..n {
            ans += reward2[i];
            diff[i] = reward1[i] - reward2[i];
        }
        diff.sort_by(|a, b| b.cmp(a));
        for i in 0..k as usize {
            ans += diff[i];
        }
        ans
    }
}
'''

FILES["2612_minimum_reverse_operations"] = r'''// LeetCode 2612 - Minimum Reverse Operations
// https://leetcode.com/problems/minimum-reverse-operations/

use std::collections::{HashSet, VecDeque};

impl Solution {
    pub fn min_reverse_operations(n: i32, p: i32, banned: Vec<i32>, k: i32) -> Vec<i32> {
        let n = n as usize;
        let k = k as usize;
        let ban: HashSet<i32> = banned.into_iter().collect();
        let mut ans = vec![-1; n];
        ans[p as usize] = 0;
        let mut q = VecDeque::new();
        q.push_back((p as usize, 0));
        while let Some((i, d)) = q.pop_front() {
            let mut lo = i as i32 - (k as i32 - 1);
            if lo < 0 {
                lo = 0;
            }
            let mut hi = i as i32;
            if hi > n as i32 - k as i32 {
                hi = n as i32 - k as i32;
            }
            for l in lo..=hi {
                let r = l + k as i32 - 1;
                let ni = l + r - i as i32;
                if ni < 0 || ni >= n as i32 || ban.contains(&ni) || ans[ni as usize] != -1 {
                    continue;
                }
                ans[ni as usize] = d + 1;
                q.push_back((ni as usize, d + 1));
            }
        }
        ans
    }
}
'''

FILES["2613_beautiful_pairs"] = r'''// LeetCode 2613 - Beautiful Pairs
// https://leetcode.com/problems/beautiful-pairs/

impl Solution {
    pub fn beautiful_pair(nums1: Vec<i32>, nums2: Vec<i32>) -> Vec<i32> {
        let n = nums1.len();
        let mut best_dist = i64::MAX;
        let mut ans = vec![0, 1];
        for i in 0..n {
            for j in i + 1..n {
                let d = (nums1[i] - nums1[j]).abs() as i64 + (nums2[i] - nums2[j]).abs() as i64;
                if d < best_dist
                    || (d == best_dist && (i < ans[0] as usize || (i == ans[0] as usize && j < ans[1] as usize)))
                {
                    best_dist = d;
                    ans = vec![i as i32, j as i32];
                }
            }
        }
        ans
    }
}
'''

FILES["2614_prime_in_diagonal"] = r'''// LeetCode 2614 - Prime In Diagonal
// https://leetcode.com/problems/prime-in-diagonal/

impl Solution {
    pub fn diagonal_prime(nums: Vec<Vec<i32>>) -> i32 {
        fn is_prime(x: i32) -> bool {
            if x < 2 {
                return false;
            }
            let mut i = 2;
            while i * i <= x {
                if x % i == 0 {
                    return false;
                }
                i += 1;
            }
            true
        }
        let n = nums.len();
        let mut best = 0;
        for i in 0..n {
            for v in [nums[i][i], nums[i][n - 1 - i]] {
                if is_prime(v) && v > best {
                    best = v;
                }
            }
        }
        best
    }
}
'''

FILES["2615_sum_of_distances"] = r'''// LeetCode 2615 - Sum of Distances
// https://leetcode.com/problems/sum-of-distances/

use std::collections::HashMap;

impl Solution {
    pub fn distance(nums: Vec<i32>) -> Vec<i64> {
        let n = nums.len();
        let mut ans = vec![0i64; n];
        let mut pos: HashMap<i32, Vec<usize>> = HashMap::new();
        for (i, &x) in nums.iter().enumerate() {
            pos.entry(x).or_default().push(i);
        }
        for idxs in pos.values() {
            let m = idxs.len();
            let mut pref = vec![0i64; m + 1];
            for i in 0..m {
                pref[i + 1] = pref[i] + idxs[i] as i64;
            }
            for j in 0..m {
                let idx = idxs[j] as i64;
                let left = j as i64 * idx - pref[j];
                let right = pref[m] - pref[j + 1] - (m as i64 - 1 - j as i64) * idx;
                ans[idxs[j]] = left + right;
            }
        }
        ans
    }
}
'''

FILES["2616_minimize_the_maximum_difference_of_pairs"] = r'''// LeetCode 2616 - Minimize the Maximum Difference of Pairs
// https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/

impl Solution {
    pub fn minimize_max(mut nums: Vec<i32>, p: i32) -> i32 {
        nums.sort_unstable();
        let ok = |d: i32| {
            let mut cnt = 0;
            let mut i = 0;
            while i + 1 < nums.len() {
                if nums[i + 1] - nums[i] <= d {
                    cnt += 1;
                    i += 2;
                } else {
                    i += 1;
                }
            }
            cnt >= p
        };
        let mut lo = 0;
        let mut hi = nums[nums.len() - 1] - nums[0];
        while lo < hi {
            let mid = (lo + hi) / 2;
            if ok(mid) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        lo
    }
}
'''

FILES["2617_minimum_number_of_visited_cells_in_a_grid"] = r'''// LeetCode 2617 - Minimum Number of Visited Cells in a Grid
// https://leetcode.com/problems/minimum-number-of-visited-cells-in-a-grid/

use std::collections::VecDeque;

impl Solution {
    pub fn minimum_visited_cells(grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        let mut dist = vec![vec![-1; n]; m];
        let mut q = VecDeque::new();
        q.push_back((0usize, 0usize));
        dist[0][0] = 1;
        while let Some((r, c)) = q.pop_front() {
            if r == m - 1 && c == n - 1 {
                return dist[r][c];
            }
            let max_c = (c + grid[r][c] as usize).min(n - 1);
            for nc in c + 1..=max_c {
                if dist[r][nc] == -1 {
                    dist[r][nc] = dist[r][c] + 1;
                    q.push_back((r, nc));
                }
            }
            let max_r = (r + grid[r][c] as usize).min(m - 1);
            for nr in r + 1..=max_r {
                if dist[nr][c] == -1 {
                    dist[nr][c] = dist[r][c] + 1;
                    q.push_back((nr, c));
                }
            }
        }
        -1
    }
}
'''

def main():
    n = 0
    for folder, text in FILES.items():
        path = ROOT / folder / "solution.rs"
        path.write_text(text, encoding="utf-8", newline="\n")
        n += 1
        print(f"wrote {folder}")
    print(f"total={n}")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
FILES = {}

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

LIST = """#[derive(PartialEq, Eq)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl ListNode {
    #[inline]
    pub fn new(val: i32) -> Self {
        ListNode { next: None, val }
    }
}
"""

FILES["2725_interval_cancellation"] = r'''// LeetCode 2725 - Interval Cancellation
// https://leetcode.com/problems/interval-cancellation/

impl Solution {
    pub fn cancellable<F: FnMut() -> i32>(mut f: F, _t: i32, times: i32) -> Vec<i32> {
        let mut results = Vec::new();
        for _ in 0..times {
            results.push(f());
        }
        results
    }
}
'''

FILES["2726_calculator_with_method_chaining"] = r'''// LeetCode 2726 - Calculator with Method Chaining
// https://leetcode.com/problems/calculator-with-method-chaining/

pub struct Calculator {
    val: f64,
}

impl Calculator {
    pub fn new(value: f64) -> Self {
        Self { val: value }
    }

    pub fn add(&mut self, value: f64) -> &mut Self {
        self.val += value;
        self
    }

    pub fn subtract(&mut self, value: f64) -> &mut Self {
        self.val -= value;
        self
    }

    pub fn multiply(&mut self, value: f64) -> &mut Self {
        self.val *= value;
        self
    }

    pub fn divide(&mut self, value: f64) -> &mut Self {
        if value != 0.0 {
            self.val /= value;
        }
        self
    }

    pub fn power(&mut self, value: f64) -> &mut Self {
        self.val = self.val.powf(value);
        self
    }

    pub fn get_result(&self) -> f64 {
        self.val
    }
}
'''

FILES["2727_is_object_empty"] = r'''// LeetCode 2727 - Is Object Empty
// https://leetcode.com/problems/is-object-empty/

use std::collections::HashMap;

impl Solution {
    pub fn is_empty(obj: HashMap<String, i32>) -> bool {
        obj.is_empty()
    }

    pub fn is_empty_vec(arr: Vec<i32>) -> bool {
        arr.is_empty()
    }
}
'''

FILES["2728_count_houses_in_a_circular_street"] = r'''// LeetCode 2728 - Count Houses in a Circular Street
// https://leetcode.com/problems/count-houses-in-a-circular-street/

pub trait Street {
    fn open_door(&mut self);
    fn close_door(&mut self);
    fn is_door_open(&self) -> bool;
    fn move_right(&mut self);
    fn move_left(&mut self);
}

impl Solution {
    pub fn count_houses<S: Street>(street: &mut S, k: i32) -> i32 {
        for _ in 0..k {
            street.close_door();
            street.move_right();
        }
        let mut ans = 0;
        loop {
            ans += 1;
            street.open_door();
            street.move_right();
            if street.is_door_open() {
                break;
            }
        }
        ans
    }
}
'''

FILES["2729_check_if_the_number_is_fascinating"] = r'''// LeetCode 2729 - Check if The Number is Fascinating
// https://leetcode.com/problems/check-if-the-number-is-fascinating/

impl Solution {
    pub fn is_fascinating(n: i32) -> bool {
        let s = format!("{}{}{}", n, 2 * n, 3 * n);
        if s.len() != 9 {
            return false;
        }
        let mut cnt = [0i32; 10];
        for c in s.bytes() {
            cnt[(c - b'0') as usize] += 1;
        }
        if cnt[0] != 0 {
            return false;
        }
        (1..=9).all(|i| cnt[i] == 1)
    }
}
'''

FILES["2730_find_the_longest_semi_repetitive_substring"] = r'''// LeetCode 2730 - Find the Longest Semi-Repetitive Substring
// https://leetcode.com/problems/find-the-longest-semi-repetitive-substring/

impl Solution {
    pub fn longest_semi_repetitive_substring(s: String) -> i32 {
        let b = s.as_bytes();
        let mut ans = 0;
        let mut left = 0;
        let mut last_pair = -1i32;
        for right in 0..b.len() {
            if right > 0 && b[right] == b[right - 1] {
                if last_pair >= left as i32 {
                    left = (last_pair + 1) as usize;
                }
                last_pair = right as i32 - 1;
            }
            ans = ans.max(right - left + 1);
        }
        ans as i32
    }
}
'''

FILES["2731_movement_of_robots"] = r'''// LeetCode 2731 - Movement of Robots
// https://leetcode.com/problems/movement-of-robots/

impl Solution {
    pub fn sum_distance(nums: Vec<i32>, s: String, d: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let bytes = s.as_bytes();
        let mut pos: Vec<i64> = nums
            .iter()
            .enumerate()
            .map(|(i, &x)| x as i64 + if bytes[i] == b'R' { d as i64 } else { -(d as i64) })
            .collect();
        pos.sort_unstable();
        let mut ans = 0i64;
        let mut pref = 0i64;
        for (i, &p) in pos.iter().enumerate() {
            ans = (ans + p * i as i64 - pref) % MOD;
            pref += p;
        }
        ((ans % MOD + MOD) % MOD) as i32
    }
}
'''

FILES["2732_find_a_good_subset_of_the_matrix"] = r'''// LeetCode 2732 - Find a Good Subset of the Matrix
// https://leetcode.com/problems/find-a-good-subset-of-the-matrix/

use std::collections::HashMap;

impl Solution {
    pub fn good_subsetof_binary_matrix(grid: Vec<Vec<i32>>) -> Vec<i32> {
        let n = grid[0].len();
        let mut first: HashMap<i32, i32> = HashMap::new();
        for (i, row) in grid.iter().enumerate() {
            let mut mask = 0i32;
            for j in 0..n {
                if row[j] == 1 {
                    mask |= 1 << j;
                }
            }
            if mask == 0 {
                return vec![i as i32];
            }
            for (&m, &idx) in &first {
                if (m & mask) == 0 {
                    return if idx < i as i32 {
                        vec![idx, i as i32]
                    } else {
                        vec![i as i32, idx]
                    };
                }
            }
            first.entry(mask).or_insert(i as i32);
        }
        vec![]
    }
}
'''

FILES["2733_neither_minimum_nor_maximum"] = r'''// LeetCode 2733 - Neither Minimum nor Maximum
// https://leetcode.com/problems/neither-minimum-nor-maximum/

impl Solution {
    pub fn find_non_min_or_max(nums: Vec<i32>) -> i32 {
        if nums.len() < 3 {
            return -1;
        }
        let (a, b, c) = (nums[0], nums[1], nums[2]);
        a + b + c - a.max(b).max(c) - a.min(b).min(c)
    }
}
'''

FILES["2734_lexicographically_smallest_string_after_substring_operation"] = r'''// LeetCode 2734 - Lexicographically Smallest String After Substring Operation
// https://leetcode.com/problems/lexicographically-smallest-string-after-substring-operation/

impl Solution {
    pub fn smallest_string(s: String) -> String {
        let mut b = s.into_bytes();
        let n = b.len();
        let mut i = 0;
        while i < n && b[i] == b'a' {
            i += 1;
        }
        if i == n {
            b[n - 1] = b'z';
            return String::from_utf8(b).unwrap();
        }
        while i < n && b[i] != b'a' {
            b[i] -= 1;
            i += 1;
        }
        String::from_utf8(b).unwrap()
    }
}
'''

FILES["2735_collecting_chocolates"] = r'''// LeetCode 2735 - Collecting Chocolates
// https://leetcode.com/problems/collecting-chocolates/

impl Solution {
    pub fn min_cost(nums: Vec<i32>, x: i32) -> i64 {
        let n = nums.len();
        let mut best = nums.clone();
        let mut ans: i64 = nums.iter().map(|&v| v as i64).sum();
        for rot in 1..n {
            let mut cur = rot as i64 * x as i64;
            for i in 0..n {
                best[i] = best[i].min(nums[(i + rot) % n]);
                cur += best[i] as i64;
            }
            ans = ans.min(cur);
        }
        ans
    }
}
'''

FILES["2736_maximum_sum_queries"] = r'''// LeetCode 2736 - Maximum Sum Queries
// https://leetcode.com/problems/maximum-sum-queries/

impl Solution {
    pub fn maximum_sum_queries(
        nums1: Vec<i32>,
        nums2: Vec<i32>,
        queries: Vec<Vec<i32>>,
    ) -> Vec<i32> {
        let n = nums1.len();
        let mut pts: Vec<(i32, i32, i32)> = (0..n)
            .map(|i| (nums1[i], nums2[i], nums1[i] + nums2[i]))
            .collect();
        pts.sort_unstable_by(|a, b| b.0.cmp(&a.0));
        let mut qs: Vec<(i32, i32, usize)> = queries
            .iter()
            .enumerate()
            .map(|(i, q)| (q[0], q[1], i))
            .collect();
        qs.sort_unstable_by(|a, b| b.0.cmp(&a.0));
        let mut ys = nums2.clone();
        for q in &queries {
            ys.push(q[1]);
        }
        ys.sort_unstable();
        ys.dedup();
        let rank = |y: i32, ys: &[i32]| ys.binary_search(&y).unwrap_or_else(|e| e) as i32 + 1;
        let m = ys.len() as i32;
        let mut bit = vec![-1i32; (m + 2) as usize];
        let update = |bit: &mut [i32], mut i: i32, v: i32| {
            while i <= m {
                bit[i as usize] = bit[i as usize].max(v);
                i += i & -i;
            }
        };
        let query = |bit: &[i32], mut i: i32| {
            let mut best = -1;
            while i > 0 {
                best = best.max(bit[i as usize]);
                i -= i & -i;
            }
            best
        };
        let mut ans = vec![0; queries.len()];
        let mut j = 0;
        for &(qx, qy, qi) in &qs {
            while j < n && pts[j].0 >= qx {
                update(&mut bit, m - rank(pts[j].1, &ys) + 1, pts[j].2);
                j += 1;
            }
            ans[qi] = query(&bit, m - rank(qy, &ys) + 1);
        }
        ans
    }
}
'''

FILES["2737_find_the_closest_marked_node"] = r'''// LeetCode 2737 - Find the Closest Marked Node
// https://leetcode.com/problems/find-the-closest-marked-node/

use std::cmp::Reverse;
use std::collections::{BinaryHeap, HashSet};

impl Solution {
    pub fn minimum_distance(n: i32, edges: Vec<Vec<i32>>, s: i32, marked: Vec<i32>) -> i32 {
        let n = n as usize;
        let mut g = vec![Vec::<(usize, i32)>::new(); n];
        for e in edges {
            g[e[0] as usize].push((e[1] as usize, e[2]));
        }
        let mark: HashSet<i32> = marked.into_iter().collect();
        let mut dist = vec![i32::MAX / 4; n];
        dist[s as usize] = 0;
        let mut pq = BinaryHeap::new();
        pq.push(Reverse((0, s as usize)));
        while let Some(Reverse((d, u))) = pq.pop() {
            if mark.contains(&(u as i32)) {
                return d;
            }
            if d > dist[u] {
                continue;
            }
            for &(v, w) in &g[u] {
                if d + w < dist[v] {
                    dist[v] = d + w;
                    pq.push(Reverse((dist[v], v)));
                }
            }
        }
        -1
    }
}
'''

FILES["2739_total_distance_traveled"] = r'''// LeetCode 2739 - Total Distance Traveled
// https://leetcode.com/problems/total-distance-traveled/

impl Solution {
    pub fn distance_traveled(mut main_tank: i32, mut additional_tank: i32) -> i32 {
        let mut ans = 0;
        while main_tank > 0 {
            if main_tank >= 5 {
                ans += 50;
                main_tank -= 5;
                if additional_tank > 0 {
                    additional_tank -= 1;
                    main_tank += 1;
                }
            } else {
                ans += main_tank * 10;
                main_tank = 0;
            }
        }
        ans
    }
}
'''

FILES["2740_find_the_value_of_the_partition"] = r'''// LeetCode 2740 - Find the Value of the Partition
// https://leetcode.com/problems/find-the-value-of-the-partition/

impl Solution {
    pub fn find_value_of_partition(mut nums: Vec<i32>) -> i32 {
        nums.sort_unstable();
        let mut ans = i32::MAX;
        for i in 1..nums.len() {
            ans = ans.min(nums[i] - nums[i - 1]);
        }
        ans
    }
}
'''

FILES["2741_special_permutations"] = r'''// LeetCode 2741 - Special Permutations
// https://leetcode.com/problems/special-permutations/

impl Solution {
    pub fn special_perm(nums: Vec<i32>) -> i32 {
        const MOD: i32 = 1_000_000_007;
        let n = nums.len();
        let mut memo = vec![vec![-1i32; n]; 1 << n];
        fn dfs(
            mask: usize,
            last: usize,
            nums: &[i32],
            memo: &mut [Vec<i32>],
            n: usize,
        ) -> i32 {
            if mask == (1 << n) - 1 {
                return 1;
            }
            if memo[mask][last] != -1 {
                return memo[mask][last];
            }
            let mut res = 0;
            for i in 0..n {
                if mask & (1 << i) != 0 {
                    continue;
                }
                if nums[i] % nums[last] == 0 || nums[last] % nums[i] == 0 {
                    res = (res + dfs(mask | (1 << i), i, nums, memo, n)) % MOD;
                }
            }
            memo[mask][last] = res;
            res
        }
        let mut ans = 0;
        for i in 0..n {
            ans = (ans + dfs(1 << i, i, &nums, &mut memo, n)) % MOD;
        }
        ans
    }
}
'''

FILES["2742_painting_the_walls"] = r'''// LeetCode 2742 - Painting the Walls
// https://leetcode.com/problems/painting-the-walls/

impl Solution {
    pub fn paint_walls(cost: Vec<i32>, time: Vec<i32>) -> i32 {
        let n = cost.len();
        let inf = 1i64 << 60;
        let mut dp = vec![inf; n + 1];
        dp[0] = 0;
        for i in 0..n {
            for j in (0..=n).rev() {
                let mut nj = j + time[i] as usize + 1;
                if nj > n {
                    nj = n;
                }
                if dp[j] + cost[i] as i64 < dp[nj] {
                    dp[nj] = dp[j] + cost[i] as i64;
                }
            }
        }
        dp[n] as i32
    }
}
'''

FILES["2743_count_substrings_without_repeating_character"] = r'''// LeetCode 2743 - Count Substrings Without Repeating Character
// https://leetcode.com/problems/count-substrings-without-repeating-character/

impl Solution {
    pub fn number_of_special_substrings(s: String) -> i32 {
        let b = s.as_bytes();
        let n = b.len();
        let mut ans = 0;
        let mut left = 0;
        let mut cnt = [0i32; 26];
        for i in 0..n {
            let c = (b[i] - b'a') as usize;
            cnt[c] += 1;
            while cnt[c] > 1 {
                cnt[(b[left] - b'a') as usize] -= 1;
                left += 1;
            }
            ans += (i - left + 1) as i32;
        }
        ans
    }
}
'''

FILES["2744_find_maximum_number_of_string_pairs"] = r'''// LeetCode 2744 - Find Maximum Number of String Pairs
// https://leetcode.com/problems/find-maximum-number-of-string-pairs/

use std::collections::HashMap;

impl Solution {
    pub fn maximum_number_of_string_pairs(words: Vec<String>) -> i32 {
        let mut freq: HashMap<String, i32> = HashMap::new();
        let mut ans = 0;
        for w in words {
            let rev: String = w.chars().rev().collect();
            if let Some(c) = freq.get_mut(&rev) {
                if *c > 0 {
                    *c -= 1;
                    ans += 1;
                    continue;
                }
            }
            *freq.entry(w).or_insert(0) += 1;
        }
        ans
    }
}
'''

FILES["2745_construct_the_longest_new_string"] = r'''// LeetCode 2745 - Construct the Longest New String
// https://leetcode.com/problems/construct-the-longest-new-string/

impl Solution {
    pub fn longest_string(x: i32, y: i32, z: i32) -> i32 {
        if x < y {
            (2 * x + 1 + z) * 2
        } else if y < x {
            (2 * y + 1 + z) * 2
        } else {
            (x + y + z) * 2
        }
    }
}
'''

FILES["2746_decremental_string_concatenation"] = r'''// LeetCode 2746 - Decremental String Concatenation
// https://leetcode.com/problems/decremental-string-concatenation/

use std::collections::HashMap;

impl Solution {
    pub fn minimize_concatenated_length(words: Vec<String>) -> i32 {
        let n = words.len();
        let mut memo: HashMap<(usize, u8, u8), i32> = HashMap::new();
        fn dfs(
            i: usize,
            first: u8,
            last: u8,
            words: &[String],
            memo: &mut HashMap<(usize, u8, u8), i32>,
        ) -> i32 {
            if i == words.len() {
                return 0;
            }
            if let Some(&v) = memo.get(&(i, first, last)) {
                return v;
            }
            let w = words[i].as_bytes();
            let wf = w[0];
            let wl = w[w.len() - 1];
            let add1 = w.len() as i32 - if last == wf { 1 } else { 0 };
            let add2 = w.len() as i32 - if wl == first { 1 } else { 0 };
            let a = add1 + dfs(i + 1, first, wl, words, memo);
            let b = add2 + dfs(i + 1, wf, last, words, memo);
            let res = a.min(b);
            memo.insert((i, first, last), res);
            res
        }
        let w0 = words[0].as_bytes();
        w0.len() as i32 + dfs(1, w0[0], w0[w0.len() - 1], &words, &mut memo)
    }
}
'''

FILES["2747_count_zero_request_servers"] = r'''// LeetCode 2747 - Count Zero Request Servers
// https://leetcode.com/problems/count-zero-request-servers/

use std::collections::HashMap;

impl Solution {
    pub fn count_servers(n: i32, mut logs: Vec<Vec<i32>>, x: i32, queries: Vec<i32>) -> Vec<i32> {
        logs.sort_unstable_by_key(|a| a[1]);
        let mut qs: Vec<(i32, usize)> = queries.iter().enumerate().map(|(i, &t)| (t, i)).collect();
        qs.sort_unstable_by_key(|a| a.0);
        let mut ans = vec![0; queries.len()];
        let mut cnt: HashMap<i32, i32> = HashMap::new();
        let mut active = 0;
        let mut l = 0;
        let mut r = 0;
        for &(t, qi) in &qs {
            while r < logs.len() && logs[r][1] <= t {
                let id = logs[r][0];
                let e = cnt.entry(id).or_insert(0);
                if *e == 0 {
                    active += 1;
                }
                *e += 1;
                r += 1;
            }
            while l < r && logs[l][1] < t - x {
                let id = logs[l][0];
                if let Some(e) = cnt.get_mut(&id) {
                    *e -= 1;
                    if *e == 0 {
                        active -= 1;
                    }
                }
                l += 1;
            }
            ans[qi] = n - active;
        }
        ans
    }
}
'''

FILES["2748_number_of_beautiful_pairs"] = r'''// LeetCode 2748 - Number of Beautiful Pairs
// https://leetcode.com/problems/number-of-beautiful-pairs/

impl Solution {
    pub fn count_beautiful_pairs(nums: Vec<i32>) -> i32 {
        fn gcd(mut a: i32, mut b: i32) -> i32 {
            while b != 0 {
                let t = a % b;
                a = b;
                b = t;
            }
            a
        }
        fn first_digit(mut x: i32) -> i32 {
            while x >= 10 {
                x /= 10;
            }
            x
        }
        let mut ans = 0;
        let mut freq = [0i32; 10];
        for x in nums {
            let last = x % 10;
            for d in 1..=9 {
                if freq[d as usize] > 0 && gcd(d, last) == 1 {
                    ans += freq[d as usize];
                }
            }
            freq[first_digit(x) as usize] += 1;
        }
        ans
    }
}
'''

FILES["2749_minimum_operations_to_make_the_integer_zero"] = r'''// LeetCode 2749 - Minimum Operations to Make the Integer Zero
// https://leetcode.com/problems/minimum-operations-to-make-the-integer-zero/

impl Solution {
    pub fn make_the_integer_zero(num1: i32, num2: i32) -> i32 {
        for k in 1..=60 {
            let rem = num1 as i64 - k as i64 * num2 as i64;
            if rem < k {
                continue;
            }
            if (rem as u64).count_ones() <= k as u32 {
                return k as i32;
            }
        }
        -1
    }
}
'''

FILES["2750_ways_to_split_array_into_good_subarrays"] = r'''// LeetCode 2750 - Ways to Split Array Into Good Subarrays
// https://leetcode.com/problems/ways-to-split-array-into-good-subarrays/

impl Solution {
    pub fn number_of_good_subarray_splits(nums: Vec<i32>) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let ones: Vec<usize> = nums
            .iter()
            .enumerate()
            .filter(|(_, &v)| v == 1)
            .map(|(i, _)| i)
            .collect();
        if ones.is_empty() {
            return 0;
        }
        let mut ans = 1i64;
        for i in 1..ones.len() {
            ans = ans * (ones[i] - ones[i - 1]) as i64 % MOD;
        }
        ans as i32
    }
}
'''

FILES["2751_robot_collisions"] = r'''// LeetCode 2751 - Robot Collisions
// https://leetcode.com/problems/robot-collisions/

use std::collections::HashMap;

impl Solution {
    pub fn survived_robots_healths(
        positions: Vec<i32>,
        healths: Vec<i32>,
        directions: String,
    ) -> Vec<i32> {
        let n = positions.len();
        let dir = directions.as_bytes();
        let mut idx: Vec<usize> = (0..n).collect();
        idx.sort_unstable_by_key(|&i| positions[i]);
        let mut stack: Vec<(usize, i32, u8)> = Vec::new();
        for i in idx {
            let mut cur = (i, healths[i], dir[i]);
            while !stack.is_empty() && stack.last().unwrap().2 == b'R' && cur.2 == b'L' {
                let back = stack.last().unwrap().1;
                if back == cur.1 {
                    stack.pop();
                    cur.1 = 0;
                    break;
                } else if back > cur.1 {
                    stack.last_mut().unwrap().1 -= 1;
                    cur.1 = 0;
                    break;
                } else {
                    cur.1 -= 1;
                    stack.pop();
                }
            }
            if cur.1 > 0 {
                stack.push(cur);
            }
        }
        let alive: HashMap<usize, i32> = stack.into_iter().map(|(i, h, _)| (i, h)).collect();
        (0..n).filter_map(|i| alive.get(&i).copied()).collect()
    }
}
'''

FILES["2753_count_houses_in_a_circular_street_ii"] = r'''// LeetCode 2753 - Count Houses in a Circular Street II
// https://leetcode.com/problems/count-houses-in-a-circular-street-ii/

impl Solution {
    pub fn house_count(street: Vec<i32>, k: i32) -> i32 {
        let n = street.len();
        if n == 0 {
            return 0;
        }
        let start = match street.iter().position(|&v| v == 1) {
            Some(i) => i,
            None => return 0,
        };
        let mut count = 1;
        let mut moves = 0;
        let mut i = start;
        while moves < k {
            i = (i + 1) % n;
            moves += 1;
            if i == start {
                break;
            }
            if street[i] == 1 {
                count += 1;
            }
        }
        count
    }
}
'''

FILES["2754_bind_function_to_context"] = r'''// LeetCode 2754 - Bind Function to Context
// https://leetcode.com/problems/bind-function-to-context/

impl Solution {
    pub fn bind_function(fn_val: i32, _args: Vec<i32>) -> i32 {
        fn_val
    }
}
'''

FILES["2755_deep_merge_of_two_objects"] = r'''// LeetCode 2755 - Deep Merge of Two Objects
// https://leetcode.com/problems/deep-merge-of-two-objects/

use std::collections::HashMap;

impl Solution {
    pub fn deep_merge(
        obj1: HashMap<String, String>,
        obj2: HashMap<String, String>,
    ) -> HashMap<String, String> {
        let mut out = obj1;
        for (k, v) in obj2 {
            out.insert(k, v);
        }
        out
    }
}
'''

FILES["2756_query_batching"] = r'''// LeetCode 2756 - Query Batching
// https://leetcode.com/problems/query-batching/

pub struct QueryBatcher {
    pending: Vec<i32>,
}

impl QueryBatcher {
    pub fn new(_query_multiple: fn(Vec<i32>) -> Vec<i32>, _t: i32) -> Self {
        Self {
            pending: Vec::new(),
        }
    }

    pub fn add_query(&mut self, query: i32) {
        self.pending.push(query);
    }
}
'''

FILES["2757_generate_circular_array_values"] = r'''// LeetCode 2757 - Generate Circular Array Values
// https://leetcode.com/problems/generate-circular-array-values/

impl Solution {
    pub fn cyclic_generator(arr: Vec<i32>, start_index: i32) -> Box<dyn FnMut() -> i32> {
        let n = arr.len();
        let mut i = start_index as usize;
        Box::new(move || {
            let v = arr[i];
            i = (i + 1) % n;
            v
        })
    }
}
'''

FILES["2758_next_day"] = r'''// LeetCode 2758 - Next Day
// https://leetcode.com/problems/next-day/

impl Solution {
    pub fn next_day(date: String) -> String {
        let parts: Vec<i32> = date.split('-').filter_map(|p| p.parse().ok()).collect();
        if parts.len() != 3 {
            return date;
        }
        let (mut y, mut m, mut d) = (parts[0], parts[1], parts[2]);
        let is_leap = |yy: i32| (yy % 4 == 0 && yy % 100 != 0) || yy % 400 == 0;
        let mut mdays = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
        if is_leap(y) {
            mdays[2] = 29;
        }
        d += 1;
        if d > mdays[m as usize] {
            d = 1;
            m += 1;
        }
        if m > 12 {
            m = 1;
            y += 1;
        }
        format!("{:04}-{:02}-{:02}", y, m, d)
    }
}
'''

FILES["2759_convert_json_string_to_object"] = r'''// LeetCode 2759 - Convert JSON String to Object
// https://leetcode.com/problems/convert-json-string-to-object/

impl Solution {
    pub fn json_parse(s: String) -> String {
        s
    }
}
'''

FILES["2760_longest_even_odd_subarray_with_threshold"] = r'''// LeetCode 2760 - Longest Even Odd Subarray With Threshold
// https://leetcode.com/problems/longest-even-odd-subarray-with-threshold/

impl Solution {
    pub fn longest_alternating_subarray(nums: Vec<i32>, threshold: i32) -> i32 {
        let n = nums.len();
        let mut ans = 0;
        for i in 0..n {
            if nums[i] % 2 != 0 || nums[i] > threshold {
                continue;
            }
            let mut j = i;
            while j + 1 < n && nums[j + 1] <= threshold && nums[j + 1] % 2 != nums[j] % 2 {
                j += 1;
            }
            ans = ans.max((j - i + 1) as i32);
        }
        ans
    }
}
'''

def main():
    written = 0
    for folder, content in FILES.items():
        path = ROOT / folder / "solution.rs"
        path.write_text(content, encoding="utf-8", newline="\n")
        written += 1
        print(f"wrote {folder}")
    print(f"part A written={written}")

if __name__ == "__main__":
    main()

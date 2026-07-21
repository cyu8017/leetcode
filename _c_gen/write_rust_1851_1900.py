#!/usr/bin/env python3
"""Write Rust solutions for LeetCode 1851-1900 (non-SQL)."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SOLUTIONS: dict[int, str] = {}

SOLUTIONS[1851] = r'''// LeetCode 1851 - Minimum Interval to Include Each Query
// https://leetcode.com/problems/minimum-interval-to-include-each-query/

use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn min_interval(mut intervals: Vec<Vec<i32>>, queries: Vec<i32>) -> Vec<i32> {
        intervals.sort_by_key(|iv| iv[0]);
        let mut indexed: Vec<(usize, i32)> = queries.iter().copied().enumerate().collect();
        indexed.sort_by_key(|&(_, q)| q);

        let mut heap: BinaryHeap<Reverse<(i32, i32)>> = BinaryHeap::new();
        let mut answer = vec![-1; queries.len()];
        let mut interval_idx = 0usize;

        for (query_idx, query) in indexed {
            while interval_idx < intervals.len() && intervals[interval_idx][0] <= query {
                let left = intervals[interval_idx][0];
                let right = intervals[interval_idx][1];
                heap.push(Reverse((right - left + 1, right)));
                interval_idx += 1;
            }
            while let Some(Reverse((_, right))) = heap.peek() {
                if *right < query {
                    heap.pop();
                } else {
                    break;
                }
            }
            if let Some(Reverse((size, _))) = heap.peek() {
                answer[query_idx] = *size;
            }
        }
        answer
    }
}
'''

SOLUTIONS[1852] = r'''// LeetCode 1852 - Distinct Numbers in Each Subarray
// https://leetcode.com/problems/distinct-numbers-in-each-subarray/

use std::collections::HashMap;

impl Solution {
    pub fn distinct_numbers(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let k = k as usize;
        let mut counts: HashMap<i32, i32> = HashMap::new();
        for &num in &nums[..k] {
            *counts.entry(num).or_insert(0) += 1;
        }
        let mut result = vec![counts.len() as i32];
        let mut left = 0usize;
        for right in k..nums.len() {
            *counts.entry(nums[right]).or_insert(0) += 1;
            let outgoing = nums[left];
            if let Some(c) = counts.get_mut(&outgoing) {
                *c -= 1;
                if *c == 0 {
                    counts.remove(&outgoing);
                }
            }
            left += 1;
            result.push(counts.len() as i32);
        }
        result
    }
}
'''

SOLUTIONS[1854] = r'''// LeetCode 1854 - Maximum Population Year
// https://leetcode.com/problems/maximum-population-year/

impl Solution {
    pub fn maximum_population(logs: Vec<Vec<i32>>) -> i32 {
        let mut diff = [0i32; 101];
        for log in &logs {
            diff[(log[0] - 1950) as usize] += 1;
            diff[(log[1] - 1950) as usize] -= 1;
        }
        let mut best_year = 1950;
        let mut best_population = 0;
        let mut population = 0;
        for offset in 0..101 {
            population += diff[offset];
            if population > best_population {
                best_population = population;
                best_year = 1950 + offset as i32;
            }
        }
        best_year
    }
}
'''

SOLUTIONS[1855] = r'''// LeetCode 1855 - Maximum Distance Between a Pair of Values
// https://leetcode.com/problems/maximum-distance-between-a-pair-of-values/

impl Solution {
    pub fn max_distance(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        let mut answer = 0i32;
        let mut j = 0usize;
        for (i, &value) in nums1.iter().enumerate() {
            while j < nums2.len() && value <= nums2[j] {
                j += 1;
            }
            answer = answer.max(j as i32 - i as i32 - 1);
        }
        answer
    }
}
'''

SOLUTIONS[1856] = r'''// LeetCode 1856 - Maximum Subarray Min-Product
// https://leetcode.com/problems/maximum-subarray-min-product/

impl Solution {
    pub fn max_sum_min_product(nums: Vec<i32>) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let n = nums.len();
        let mut prefix = vec![0i64; n + 1];
        for (i, &value) in nums.iter().enumerate() {
            prefix[i + 1] = prefix[i] + value as i64;
        }

        let mut left_bound = vec![-1isize; n];
        let mut stack: Vec<usize> = Vec::new();
        for (i, &value) in nums.iter().enumerate() {
            while stack.last().is_some_and(|&j| nums[j] >= value) {
                stack.pop();
            }
            left_bound[i] = stack.last().map(|&j| j as isize).unwrap_or(-1);
            stack.push(i);
        }

        let mut right_bound = vec![n; n];
        stack.clear();
        for i in (0..n).rev() {
            let value = nums[i];
            while stack.last().is_some_and(|&j| nums[j] >= value) {
                stack.pop();
            }
            right_bound[i] = stack.last().copied().unwrap_or(n);
            stack.push(i);
        }

        let mut best = 0i64;
        for (i, &value) in nums.iter().enumerate() {
            let total = prefix[right_bound[i]] - prefix[(left_bound[i] + 1) as usize];
            best = best.max(total * value as i64);
        }
        (best % MOD) as i32
    }
}
'''

SOLUTIONS[1857] = r'''// LeetCode 1857 - Largest Color Value in a Directed Graph
// https://leetcode.com/problems/largest-color-value-in-a-directed-graph/

use std::collections::VecDeque;

impl Solution {
    pub fn largest_path_value(colors: String, edges: Vec<Vec<i32>>) -> i32 {
        let n = colors.len();
        let bytes = colors.as_bytes();
        let mut indegree = vec![0i32; n];
        let mut adjacency = vec![Vec::new(); n];
        for edge in &edges {
            let from = edge[0] as usize;
            let to = edge[1] as usize;
            adjacency[from].push(to);
            indegree[to] += 1;
        }

        let mut queue: VecDeque<usize> = (0..n).filter(|&i| indegree[i] == 0).collect();
        let mut dp = vec![[0i32; 26]; n];
        for node in 0..n {
            dp[node][(bytes[node] - b'a') as usize] = 1;
        }

        let mut processed = 0;
        let mut answer = 0;
        while let Some(node) = queue.pop_front() {
            processed += 1;
            answer = answer.max(*dp[node].iter().max().unwrap_or(&0));
            let neighbor_color_base = bytes;
            for &neighbor in &adjacency[node] {
                let neighbor_color = (neighbor_color_base[neighbor] - b'a') as usize;
                for color_index in 0..26 {
                    let mut candidate = dp[node][color_index];
                    if color_index == neighbor_color {
                        candidate += 1;
                    }
                    if candidate > dp[neighbor][color_index] {
                        dp[neighbor][color_index] = candidate;
                    }
                }
                indegree[neighbor] -= 1;
                if indegree[neighbor] == 0 {
                    queue.push_back(neighbor);
                }
            }
        }
        if processed == n {
            answer
        } else {
            -1
        }
    }
}
'''

SOLUTIONS[1858] = r'''// LeetCode 1858 - Longest Word With All Prefixes
// https://leetcode.com/problems/longest-word-with-all-prefixes/

use std::collections::HashSet;

impl Solution {
    pub fn longest_word(words: Vec<String>) -> String {
        let word_set: HashSet<&str> = words.iter().map(|w| w.as_str()).collect();
        let mut best = String::new();
        for word in &words {
            let mut valid = true;
            for end in 1..=word.len() {
                if !word_set.contains(&word[..end]) {
                    valid = false;
                    break;
                }
            }
            if valid
                && (word.len() > best.len()
                    || (word.len() == best.len() && word.as_str() < best.as_str()))
            {
                best = word.clone();
            }
        }
        best
    }
}
'''

SOLUTIONS[1859] = r'''// LeetCode 1859 - Sorting the Sentence
// https://leetcode.com/problems/sorting-the-sentence/

impl Solution {
    pub fn sort_sentence(s: String) -> String {
        let tokens: Vec<&str> = s.split_whitespace().collect();
        let mut ordered = vec![String::new(); tokens.len()];
        for token in tokens {
            let position = token.as_bytes()[token.len() - 1] as usize - b'1' as usize;
            ordered[position] = token[..token.len() - 1].to_string();
        }
        ordered.join(" ")
    }
}
'''

SOLUTIONS[1860] = r'''// LeetCode 1860 - Incremental Memory Leak
// https://leetcode.com/problems/incremental-memory-leak/

impl Solution {
    pub fn mem_leak(mut memory1: i32, mut memory2: i32) -> Vec<i32> {
        let mut second = 1i32;
        while memory1 >= second || memory2 >= second {
            if memory1 >= memory2 {
                memory1 -= second;
            } else {
                memory2 -= second;
            }
            second += 1;
        }
        vec![second, memory1, memory2]
    }
}
'''

SOLUTIONS[1861] = r'''// LeetCode 1861 - Rotating the Box
// https://leetcode.com/problems/rotating-the-box/

impl Solution {
    pub fn rotate_the_box(box_grid: Vec<Vec<char>>) -> Vec<Vec<char>> {
        let m = box_grid.len();
        let n = box_grid[0].len();
        let mut rotated = vec![vec!['.'; m]; n];
        for i in 0..n {
            for j in 0..m {
                rotated[i][j] = box_grid[m - 1 - j][i];
            }
        }
        for col in 0..m {
            let mut row = n as i32 - 1;
            for i in (0..n).rev() {
                if rotated[i][col] == '*' {
                    row = i as i32 - 1;
                } else if rotated[i][col] == '#' {
                    rotated[i][col] = '.';
                    rotated[row as usize][col] = '#';
                    row -= 1;
                }
            }
        }
        rotated
    }
}
'''

SOLUTIONS[1862] = r'''// LeetCode 1862 - Sum of Floored Pairs
// https://leetcode.com/problems/sum-of-floored-pairs/

impl Solution {
    pub fn sum_of_floored_pairs(nums: Vec<i32>) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let max_val = *nums.iter().max().unwrap() as usize;
        let mut count = vec![0i64; max_val + 1];
        for &num in &nums {
            count[num as usize] += 1;
        }
        let mut prefix = vec![0i64; max_val + 1];
        prefix[0] = count[0];
        for value in 1..=max_val {
            prefix[value] = prefix[value - 1] + count[value];
        }
        let mut answer = 0i64;
        for divisor in 1..=max_val {
            if count[divisor] == 0 {
                continue;
            }
            let mut quotient = 1usize;
            while quotient * divisor <= max_val {
                let low = quotient * divisor;
                let high = ((quotient + 1) * divisor - 1).min(max_val);
                let matches = prefix[high] - if low > 0 { prefix[low - 1] } else { 0 };
                answer = (answer + count[divisor] * matches * quotient as i64) % MOD;
                quotient += 1;
            }
        }
        answer as i32
    }
}
'''

SOLUTIONS[1863] = r'''// LeetCode 1863 - Sum of All Subset XOR Totals
// https://leetcode.com/problems/sum-of-all-subset-xor-totals/

impl Solution {
    pub fn subset_xor_sum(nums: Vec<i32>) -> i32 {
        let mut bits = 0;
        for &num in &nums {
            bits |= num;
        }
        let mut total = 0;
        let mut bit = 1;
        while bit <= bits {
            if bits & bit != 0 {
                total += bit;
            }
            bit <<= 1;
        }
        total << (nums.len() - 1)
    }
}
'''

SOLUTIONS[1864] = r'''// LeetCode 1864 - Minimum Number of Swaps to Make the Binary String Alternating
// https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-binary-string-alternating/

impl Solution {
    pub fn min_swaps(s: String) -> i32 {
        let zeros = s.bytes().filter(|&b| b == b'0').count() as i32;
        let ones = s.len() as i32 - zeros;
        if (zeros - ones).abs() > 1 {
            return -1;
        }
        let mismatches = |pattern: &[u8; 2]| -> i32 {
            s.bytes()
                .enumerate()
                .filter(|(i, ch)| *ch != pattern[i % 2])
                .count() as i32
                / 2
        };
        if zeros == ones {
            mismatches(b"01").min(mismatches(b"10"))
        } else if zeros > ones {
            mismatches(b"01")
        } else {
            mismatches(b"10")
        }
    }
}
'''

SOLUTIONS[1865] = r'''// LeetCode 1865 - Finding Pairs With a Certain Sum
// https://leetcode.com/problems/finding-pairs-with-a-certain-sum/

use std::collections::HashMap;

pub struct FindSumPairs {
    nums1: Vec<i32>,
    nums2: Vec<i32>,
    counts: HashMap<i32, i32>,
}

impl FindSumPairs {
    pub fn new(nums1: Vec<i32>, nums2: Vec<i32>) -> Self {
        let mut counts = HashMap::new();
        for &num in &nums2 {
            *counts.entry(num).or_insert(0) += 1;
        }
        Self {
            nums1,
            nums2,
            counts,
        }
    }

    pub fn add(&mut self, index: i32, val: i32) {
        let index = index as usize;
        *self.counts.entry(self.nums2[index]).or_insert(0) -= 1;
        self.nums2[index] += val;
        *self.counts.entry(self.nums2[index]).or_insert(0) += 1;
    }

    pub fn count(&self, tot: i32) -> i32 {
        self.nums1
            .iter()
            .map(|&num| *self.counts.get(&(tot - num)).unwrap_or(&0))
            .sum()
    }
}
'''

SOLUTIONS[1866] = r'''// LeetCode 1866 - Number of Ways to Rearrange Sticks With K Sticks Visible
// https://leetcode.com/problems/number-of-ways-to-rearrange-sticks-with-k-sticks-visible/

impl Solution {
    pub fn rearrange_sticks(n: i32, k: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let n = n as usize;
        let k = k as usize;
        if k == 0 || k > n {
            return 0;
        }
        let mut dp = vec![vec![0i64; n + 1]; n + 1];
        dp[1][1] = 1;
        for sticks in 2..=n {
            dp[sticks][1] = ((sticks as i64 - 1) * dp[sticks - 1][1]) % MOD;
            for visible in 2..=sticks {
                dp[sticks][visible] = (dp[sticks - 1][visible - 1]
                    + (sticks as i64 - 1) * dp[sticks - 1][visible])
                    % MOD;
            }
        }
        dp[n][k] as i32
    }
}
'''

SOLUTIONS[1868] = r'''// LeetCode 1868 - Product of Two Run-Length Encoded Arrays
// https://leetcode.com/problems/product-of-two-run-length-encoded-arrays/

impl Solution {
    pub fn find_rle_array(encoded1: Vec<Vec<i32>>, encoded2: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let mut result: Vec<Vec<i32>> = Vec::new();
        let mut i = 0usize;
        let mut j = 0usize;
        let mut rem1 = encoded1[0][1];
        let mut rem2 = encoded2[0][1];
        while i < encoded1.len() {
            let take = rem1.min(rem2);
            let value = encoded1[i][0] * encoded2[j][0];
            if let Some(last) = result.last_mut() {
                if last[0] == value {
                    last[1] += take;
                } else {
                    result.push(vec![value, take]);
                }
            } else {
                result.push(vec![value, take]);
            }
            rem1 -= take;
            rem2 -= take;
            if rem1 == 0 {
                i += 1;
                if i < encoded1.len() {
                    rem1 = encoded1[i][1];
                }
            }
            if rem2 == 0 {
                j += 1;
                if j < encoded2.len() {
                    rem2 = encoded2[j][1];
                }
            }
        }
        result
    }
}
'''

SOLUTIONS[1869] = r'''// LeetCode 1869 - Longer Contiguous Segments of Ones than Zeros
// https://leetcode.com/problems/longer-contiguous-segments-of-ones-than-zeros/

impl Solution {
    pub fn check_zero_ones(s: String) -> bool {
        let mut max_zeros = 0i32;
        let mut max_ones = 0i32;
        let mut zeros = 0i32;
        let mut ones = 0i32;
        for ch in s.bytes() {
            if ch == b'0' {
                zeros += 1;
                ones = 0;
                max_zeros = max_zeros.max(zeros);
            } else {
                ones += 1;
                zeros = 0;
                max_ones = max_ones.max(ones);
            }
        }
        max_ones > max_zeros
    }
}
'''

SOLUTIONS[1870] = r'''// LeetCode 1870 - Minimum Speed to Arrive on Time
// https://leetcode.com/problems/minimum-speed-to-arrive-on-time/

impl Solution {
    pub fn min_speed_on_time(dist: Vec<i32>, hour: f64) -> i32 {
        let n = dist.len();
        if (n as f64 - 1.0) >= hour {
            return -1;
        }
        let can_arrive = |speed: i32| -> bool {
            let mut time = 0.0f64;
            for i in 0..n - 1 {
                time += ((dist[i] + speed - 1) / speed) as f64;
            }
            time += dist[n - 1] as f64 / speed as f64;
            time <= hour
        };
        if !can_arrive(10_000_000) {
            return -1;
        }
        let mut lo = 1;
        let mut hi = 10_000_000;
        while lo < hi {
            let mid = (lo + hi) / 2;
            if can_arrive(mid) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        lo
    }
}
'''

SOLUTIONS[1871] = r'''// LeetCode 1871 - Jump Game VII
// https://leetcode.com/problems/jump-game-vii/

impl Solution {
    pub fn can_reach(s: String, min_jump: i32, max_jump: i32) -> bool {
        let n = s.len();
        let bytes = s.as_bytes();
        let min_jump = min_jump as usize;
        let max_jump = max_jump as usize;
        let mut reachable = vec![false; n];
        reachable[0] = true;
        let mut prefix = vec![0i32; n + 1];
        for i in 0..n {
            if i > 0 && bytes[i] == b'0' {
                let left = i.saturating_sub(max_jump);
                if i >= min_jump {
                    let right = i - min_jump;
                    if right >= left && prefix[right + 1] - prefix[left] > 0 {
                        reachable[i] = true;
                    }
                }
            }
            prefix[i + 1] = prefix[i] + if reachable[i] { 1 } else { 0 };
        }
        reachable[n - 1]
    }
}
'''

SOLUTIONS[1872] = r'''// LeetCode 1872 - Stone Game VIII
// https://leetcode.com/problems/stone-game-viii/

impl Solution {
    pub fn stone_game_viii(mut stones: Vec<i32>) -> i32 {
        let n = stones.len();
        for i in 1..n {
            stones[i] += stones[i - 1];
        }
        let mut score = stones[n - 1];
        for i in (1..n - 1).rev() {
            score = score.max(stones[i] - score);
        }
        score
    }
}
'''

SOLUTIONS[1874] = r'''// LeetCode 1874 - Minimize Product Sum of Two Arrays
// https://leetcode.com/problems/minimize-product-sum-of-two-arrays/

impl Solution {
    pub fn min_product_sum(mut nums1: Vec<i32>, mut nums2: Vec<i32>) -> i32 {
        nums1.sort_unstable();
        nums2.sort_unstable_by(|a, b| b.cmp(a));
        nums1.iter().zip(nums2.iter()).map(|(a, b)| a * b).sum()
    }
}
'''

SOLUTIONS[1876] = r'''// LeetCode 1876 - Substrings of Size Three with Distinct Characters
// https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/

impl Solution {
    pub fn count_good_substrings(s: String) -> i32 {
        if s.len() < 3 {
            return 0;
        }
        let bytes = s.as_bytes();
        let mut count = 0;
        for i in 0..bytes.len() - 2 {
            let a = bytes[i];
            let b = bytes[i + 1];
            let c = bytes[i + 2];
            if a != b && b != c && a != c {
                count += 1;
            }
        }
        count
    }
}
'''

SOLUTIONS[1877] = r'''// LeetCode 1877 - Minimize Maximum Pair Sum in Array
// https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/

impl Solution {
    pub fn min_pair_sum(mut nums: Vec<i32>) -> i32 {
        nums.sort_unstable();
        let n = nums.len();
        (0..n / 2)
            .map(|i| nums[i] + nums[n - 1 - i])
            .max()
            .unwrap_or(0)
    }
}
'''

SOLUTIONS[1878] = r'''// LeetCode 1878 - Get Biggest Three Rhombus Sums in a Grid
// https://leetcode.com/problems/get-biggest-three-rhombus-sums-in-a-grid/

use std::collections::BTreeSet;

impl Solution {
    pub fn get_biggest_three(grid: Vec<Vec<i32>>) -> Vec<i32> {
        let m = grid.len();
        let n = grid[0].len();
        let mut s1 = vec![vec![0i32; n + 2]; m + 1];
        let mut s2 = vec![vec![0i32; n + 2]; m + 1];
        for i in 1..=m {
            for j in 1..=n {
                let value = grid[i - 1][j - 1];
                s1[i][j] = s1[i - 1][j - 1] + value;
                s2[i][j] = s2[i - 1][j + 1] + value;
            }
        }
        let mut rhombus_sums = BTreeSet::new();
        for i in 1..=m {
            for j in 1..=n {
                let value = grid[i - 1][j - 1];
                let limit = (i - 1).min(m - i).min(j - 1).min(n - j);
                rhombus_sums.insert(value);
                for k in 1..=limit {
                    let a = s1[i + k][j] - s1[i][j - k];
                    let b = s1[i][j + k] - s1[i - k][j];
                    let c = s2[i][j - k] - s2[i - k][j];
                    let d = s2[i + k][j] - s2[i][j + k];
                    rhombus_sums.insert(
                        a + b + c + d - grid[i + k - 1][j - 1] + grid[i - k - 1][j - 1],
                    );
                }
            }
        }
        rhombus_sums.into_iter().rev().take(3).collect()
    }
}
'''

SOLUTIONS[1879] = r'''// LeetCode 1879 - Minimum XOR Sum of Two Arrays
// https://leetcode.com/problems/minimum-xor-sum-of-two-arrays/

impl Solution {
    pub fn minimum_xor_sum(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        let n = nums1.len();
        let mut dp = vec![i32::MAX; 1 << n];
        dp[0] = 0;
        for mask in 0usize..(1 << n) {
            let i = mask.count_ones() as usize;
            if i >= n {
                continue;
            }
            for j in 0..n {
                if mask & (1 << j) != 0 {
                    continue;
                }
                let next_mask = mask | (1 << j);
                let cost = dp[mask].saturating_add(nums1[i] ^ nums2[j]);
                if cost < dp[next_mask] {
                    dp[next_mask] = cost;
                }
            }
        }
        dp[(1 << n) - 1]
    }
}
'''

SOLUTIONS[1880] = r'''// LeetCode 1880 - Check if Word Equals Summation of Two Words
// https://leetcode.com/problems/check-if-word-equals-summation-of-two-words/

impl Solution {
    pub fn is_sum_equal(first_word: String, second_word: String, target_word: String) -> bool {
        fn value(word: &str) -> i32 {
            word.bytes()
                .fold(0, |acc, ch| acc * 10 + (ch - b'a') as i32)
        }
        value(&first_word) + value(&second_word) == value(&target_word)
    }
}
'''

SOLUTIONS[1881] = r'''// LeetCode 1881 - Maximum Value after Insertion
// https://leetcode.com/problems/maximum-value-after-insertion/

impl Solution {
    pub fn max_value(n: String, x: i32) -> String {
        let neg = n.as_bytes()[0] == b'-';
        let start = if neg { 1 } else { 0 };
        let xch = (b'0' + x as u8) as char;
        for i in start..n.len() {
            let d = (n.as_bytes()[i] - b'0') as i32;
            if neg {
                if d > x {
                    return format!("{}{}{}", &n[..i], xch, &n[i..]);
                }
            } else if d < x {
                return format!("{}{}{}", &n[..i], xch, &n[i..]);
            }
        }
        format!("{}{}", n, xch)
    }
}
'''

SOLUTIONS[1882] = r'''// LeetCode 1882 - Process Tasks Using Servers
// https://leetcode.com/problems/process-tasks-using-servers/

use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn assign_tasks(servers: Vec<i32>, tasks: Vec<i32>) -> Vec<i32> {
        let mut available: BinaryHeap<Reverse<(i32, usize)>> = servers
            .iter()
            .enumerate()
            .map(|(index, &weight)| Reverse((weight, index)))
            .collect();
        let mut busy: BinaryHeap<Reverse<(i64, i32, usize)>> = BinaryHeap::new();
        let mut answer = Vec::with_capacity(tasks.len());
        let mut time: i64 = 0;

        for (moment, &task) in tasks.iter().enumerate() {
            time = time.max(moment as i64);
            while let Some(Reverse((finish, weight, index))) = busy.peek().copied() {
                if finish <= time {
                    busy.pop();
                    available.push(Reverse((weight, index)));
                } else {
                    break;
                }
            }
            while available.is_empty() {
                if let Some(Reverse((finish, _, _))) = busy.peek().copied() {
                    time = finish;
                }
                while let Some(Reverse((finish, weight, index))) = busy.peek().copied() {
                    if finish <= time {
                        busy.pop();
                        available.push(Reverse((weight, index)));
                    } else {
                        break;
                    }
                }
            }
            let Reverse((weight, index)) = available.pop().unwrap();
            busy.push(Reverse((time + task as i64, weight, index)));
            answer.push(index as i32);
        }
        answer
    }
}
'''

SOLUTIONS[1883] = r'''// LeetCode 1883 - Minimum Skips to Arrive at Meeting On Time
// https://leetcode.com/problems/minimum-skips-to-arrive-at-meeting-on-time/

impl Solution {
    pub fn min_skips(dist: Vec<i32>, speed: i32, hours_before: i32) -> i32 {
        let limit = hours_before as i64 * speed as i64;
        let n = dist.len();
        const INF: i64 = i64::MAX / 4;
        let mut dp = vec![INF; n + 1];
        dp[0] = 0;
        for &road in &dist {
            let mut nxt = vec![INF; n + 1];
            for skips in 0..n {
                if dp[skips] == INF {
                    continue;
                }
                let ceiled = ((dp[skips] + road as i64 + speed as i64 - 1) / speed as i64)
                    * speed as i64;
                nxt[skips] = nxt[skips].min(ceiled);
                nxt[skips + 1] = nxt[skips + 1].min(dp[skips] + road as i64);
            }
            dp = nxt;
        }
        for (skips, total) in dp.iter().enumerate() {
            if *total <= limit {
                return skips as i32;
            }
        }
        -1
    }
}
'''

SOLUTIONS[1884] = r'''// LeetCode 1884 - Egg Drop With 2 Eggs and N Floors
// https://leetcode.com/problems/egg-drop-with-2-eggs-and-n-floors/

impl Solution {
    pub fn two_egg_drop(n: i32) -> i32 {
        let mut moves = 0;
        let mut covered = 0;
        while covered < n {
            moves += 1;
            covered += moves;
        }
        moves
    }
}
'''

SOLUTIONS[1885] = r'''// LeetCode 1885 - Count Pairs in Two Arrays
// https://leetcode.com/problems/count-pairs-in-two-arrays/

impl Solution {
    pub fn count_pairs(nums1: Vec<i32>, nums2: Vec<i32>) -> i64 {
        let mut diff: Vec<i32> = nums1
            .iter()
            .zip(nums2.iter())
            .map(|(a, b)| a - b)
            .collect();
        diff.sort_unstable();
        let mut answer = 0i64;
        let n = diff.len();
        for i in 0..n {
            let target = -diff[i];
            let mut lo = i + 1;
            let mut hi = n;
            while lo < hi {
                let mid = (lo + hi) / 2;
                if diff[mid] > target {
                    hi = mid;
                } else {
                    lo = mid + 1;
                }
            }
            answer += (n - lo) as i64;
        }
        answer
    }
}
'''

SOLUTIONS[1886] = r'''// LeetCode 1886 - Determine Whether Matrix Can Be Obtained By Rotation
// https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/

impl Solution {
    pub fn find_rotation(mat: Vec<Vec<i32>>, target: Vec<Vec<i32>>) -> bool {
        let mut current = mat;
        for _ in 0..4 {
            if current == target {
                return true;
            }
            let n = current.len();
            current = (0..n)
                .map(|col| (0..n).map(|row| current[n - 1 - row][col]).collect())
                .collect();
        }
        false
    }
}
'''

SOLUTIONS[1887] = r'''// LeetCode 1887 - Reduction Operations to Make the Array Elements Equal
// https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/

impl Solution {
    pub fn reduction_operations(mut nums: Vec<i32>) -> i32 {
        nums.sort_unstable();
        let mut answer = 0;
        let mut rank = 0;
        for i in 1..nums.len() {
            if nums[i] != nums[i - 1] {
                rank += 1;
            }
            answer += rank;
        }
        answer
    }
}
'''

SOLUTIONS[1888] = r'''// LeetCode 1888 - Minimum Number of Flips to Make the Binary String Alternating
// https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/

impl Solution {
    pub fn min_flips(s: String) -> i32 {
        let n = s.len();
        let doubled = format!("{}{}", s, s);
        let bytes = doubled.as_bytes();
        let mut alt0 = 0i32;
        let mut alt1 = 0i32;
        for i in 0..n {
            let expect0 = if i % 2 == 0 { b'0' } else { b'1' };
            let expect1 = if i % 2 == 0 { b'1' } else { b'0' };
            if bytes[i] != expect0 {
                alt0 += 1;
            }
            if bytes[i] != expect1 {
                alt1 += 1;
            }
        }
        let mut answer = alt0.min(alt1);
        for i in 0..n {
            let expect0 = if i % 2 == 0 { b'0' } else { b'1' };
            let expect1 = if i % 2 == 0 { b'1' } else { b'0' };
            if bytes[i] != expect0 {
                alt0 -= 1;
            }
            let j = i + n;
            let expect0n = if j % 2 == 0 { b'0' } else { b'1' };
            let expect1n = if j % 2 == 0 { b'1' } else { b'0' };
            if bytes[j] != expect0n {
                alt0 += 1;
            }
            if bytes[i] != expect1 {
                alt1 -= 1;
            }
            if bytes[j] != expect1n {
                alt1 += 1;
            }
            answer = answer.min(alt0).min(alt1);
        }
        answer
    }
}
'''

SOLUTIONS[1889] = r'''// LeetCode 1889 - Minimum Space Wasted From Packaging
// https://leetcode.com/problems/minimum-space-wasted-from-packaging/

impl Solution {
    pub fn min_wasted_space(mut packages: Vec<i32>, boxes: Vec<Vec<i32>>) -> i32 {
        packages.sort_unstable();
        let mut prefix = vec![0i64; packages.len()];
        prefix[0] = packages[0] as i64;
        for i in 1..packages.len() {
            prefix[i] = prefix[i - 1] + packages[i] as i64;
        }
        let mut answer = i64::MAX;
        for mut supplier in boxes {
            supplier.sort_unstable();
            let mut start = 0usize;
            let mut wasted = 0i64;
            for &box_size in &supplier {
                let mut lo = start;
                let mut hi = packages.len();
                while lo < hi {
                    let mid = (lo + hi) / 2;
                    if packages[mid] <= box_size {
                        lo = mid + 1;
                    } else {
                        hi = mid;
                    }
                }
                let end = lo;
                if end == start {
                    continue;
                }
                let package_sum = prefix[end - 1] - if start > 0 { prefix[start - 1] } else { 0 };
                wasted += box_size as i64 * (end - start) as i64 - package_sum;
                start = end;
            }
            if start == packages.len() {
                answer = answer.min(wasted);
            }
        }
        if answer == i64::MAX {
            -1
        } else {
            (answer % 1_000_000_007) as i32
        }
    }
}
'''

SOLUTIONS[1891] = r'''// LeetCode 1891 - Cutting Ribbons
// https://leetcode.com/problems/cutting-ribbons/

impl Solution {
    pub fn max_length(ribbons: Vec<i32>, k: i32) -> i32 {
        let can = |length: i32| -> bool {
            ribbons.iter().map(|&r| (r / length) as i64).sum::<i64>() >= k as i64
        };
        let mut lo = 1;
        let mut hi = *ribbons.iter().max().unwrap_or(&0);
        if hi == 0 {
            return 0;
        }
        while lo < hi {
            let mid = (lo + hi + 1) / 2;
            if can(mid) {
                lo = mid;
            } else {
                hi = mid - 1;
            }
        }
        if can(lo) {
            lo
        } else {
            0
        }
    }
}
'''

SOLUTIONS[1893] = r'''// LeetCode 1893 - Check if All the Integers in a Range Are Covered
// https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/

impl Solution {
    pub fn is_covered(ranges: Vec<Vec<i32>>, left: i32, right: i32) -> bool {
        let mut covered = [false; 51];
        for r in &ranges {
            for value in r[0]..=r[1] {
                covered[value as usize] = true;
            }
        }
        (left..=right).all(|value| covered[value as usize])
    }
}
'''

SOLUTIONS[1894] = r'''// LeetCode 1894 - Find the Student that Will Replace the Chalk
// https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/

impl Solution {
    pub fn chalk_replacer(chalk: Vec<i32>, k: i32) -> i32 {
        let total: i64 = chalk.iter().map(|&c| c as i64).sum();
        let mut k = (k as i64) % total;
        for (index, &need) in chalk.iter().enumerate() {
            if k < need as i64 {
                return index as i32;
            }
            k -= need as i64;
        }
        0
    }
}
'''

SOLUTIONS[1895] = r'''// LeetCode 1895 - Largest Magic Square
// https://leetcode.com/problems/largest-magic-square/

impl Solution {
    pub fn largest_magic_square(grid: Vec<Vec<i32>>) -> i32 {
        let rows = grid.len();
        let cols = grid[0].len();
        let mut row_prefix = vec![vec![0i32; cols + 1]; rows];
        let mut col_prefix = vec![vec![0i32; rows + 1]; cols];
        for i in 0..rows {
            for j in 0..cols {
                row_prefix[i][j + 1] = row_prefix[i][j] + grid[i][j];
                col_prefix[j][i + 1] = col_prefix[j][i] + grid[i][j];
            }
        }
        let row_sum = |row: usize, col_start: usize, col_end: usize| -> i32 {
            row_prefix[row][col_end + 1] - row_prefix[row][col_start]
        };
        let col_sum = |col: usize, row_start: usize, row_end: usize| -> i32 {
            col_prefix[col][row_end + 1] - col_prefix[col][row_start]
        };
        let is_magic = |row_start: usize, col_start: usize, size: usize| -> bool {
            let target = row_sum(row_start, col_start, col_start + size - 1);
            for row in row_start..row_start + size {
                if row_sum(row, col_start, col_start + size - 1) != target {
                    return false;
                }
            }
            for col in col_start..col_start + size {
                if col_sum(col, row_start, row_start + size - 1) != target {
                    return false;
                }
            }
            let mut diag1 = 0;
            let mut diag2 = 0;
            for offset in 0..size {
                diag1 += grid[row_start + offset][col_start + offset];
                diag2 += grid[row_start + offset][col_start + size - 1 - offset];
            }
            diag1 == target && diag2 == target
        };
        for size in (1..=rows.min(cols)).rev() {
            for row_start in 0..=rows - size {
                for col_start in 0..=cols - size {
                    if is_magic(row_start, col_start, size) {
                        return size as i32;
                    }
                }
            }
        }
        1
    }
}
'''

SOLUTIONS[1896] = r'''// LeetCode 1896 - Minimum Cost to Change the Final Value of Expression
// https://leetcode.com/problems/minimum-cost-to-change-the-final-value-of-expression/

impl Solution {
    pub fn min_operations_to_flip(expression: String) -> i32 {
        let bytes = expression.as_bytes();
        let mut index = 0usize;

        fn combine(left: [i32; 3], op: u8, right: [i32; 3]) -> [i32; 3] {
            let [left_val, left_to_zero, left_to_one] = left;
            let [right_val, right_to_zero, right_to_one] = right;
            if op == b'&' {
                let and_val = left_val & right_val;
                let and_to_zero = left_to_zero.min(left_to_one + right_to_zero);
                let and_to_one = left_to_one + right_to_one;
                let or_to_zero = left_to_zero + right_to_zero;
                let or_to_one = left_to_one
                    .min(left_to_zero + right_to_one)
                    .min(right_to_zero + left_to_one);
                [
                    and_val,
                    and_to_zero.min(1 + or_to_zero),
                    and_to_one.min(1 + or_to_one),
                ]
            } else {
                let or_val = left_val | right_val;
                let or_to_zero = left_to_zero + right_to_zero;
                let or_to_one = left_to_one
                    .min(left_to_zero + right_to_one)
                    .min(right_to_zero + left_to_one);
                let and_to_zero = left_to_zero.min(left_to_one + right_to_zero);
                let and_to_one = left_to_one + right_to_one;
                [
                    or_val,
                    or_to_zero.min(1 + and_to_zero),
                    or_to_one.min(1 + and_to_one),
                ]
            }
        }

        fn parse_factor(bytes: &[u8], index: &mut usize) -> [i32; 3] {
            if bytes[*index] == b'0' || bytes[*index] == b'1' {
                let value = (bytes[*index] - b'0') as i32;
                *index += 1;
                return [
                    value,
                    if value == 0 { 0 } else { 1 },
                    if value == 0 { 1 } else { 0 },
                ];
            }
            *index += 1;
            let node = parse_expr(bytes, index);
            *index += 1;
            node
        }

        fn parse_expr(bytes: &[u8], index: &mut usize) -> [i32; 3] {
            let mut node = parse_factor(bytes, index);
            while *index < bytes.len() && (bytes[*index] == b'&' || bytes[*index] == b'|') {
                let op = bytes[*index];
                *index += 1;
                node = combine(node, op, parse_factor(bytes, index));
            }
            node
        }

        let [value, to_zero, to_one] = parse_expr(bytes, &mut index);
        if value != 0 {
            to_zero
        } else {
            to_one
        }
    }
}
'''

SOLUTIONS[1897] = r'''// LeetCode 1897 - Redistribute Characters to Make All Strings Equal
// https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/

impl Solution {
    pub fn make_equal(words: Vec<String>) -> bool {
        let n = words.len();
        let mut counts = [0i32; 26];
        for word in &words {
            for b in word.bytes() {
                counts[(b - b'a') as usize] += 1;
            }
        }
        counts.iter().all(|&c| c as usize % n == 0)
    }
}
'''

SOLUTIONS[1898] = r'''// LeetCode 1898 - Maximum Number of Removable Characters
// https://leetcode.com/problems/maximum-number-of-removable-characters/

impl Solution {
    pub fn maximum_removals(s: String, p: String, removable: Vec<i32>) -> i32 {
        let s_bytes = s.as_bytes();
        let p_bytes = p.as_bytes();
        let still_subsequence = |k: usize| -> bool {
            let mut removed = vec![false; s_bytes.len()];
            for &idx in &removable[..k] {
                removed[idx as usize] = true;
            }
            let mut index = 0usize;
            for (position, &ch) in s_bytes.iter().enumerate() {
                if removed[position] {
                    continue;
                }
                if index < p_bytes.len() && ch == p_bytes[index] {
                    index += 1;
                }
            }
            index == p_bytes.len()
        };
        let mut lo = 0usize;
        let mut hi = removable.len();
        while lo < hi {
            let mid = (lo + hi + 1) / 2;
            if still_subsequence(mid) {
                lo = mid;
            } else {
                hi = mid - 1;
            }
        }
        lo as i32
    }
}
'''

SOLUTIONS[1899] = r'''// LeetCode 1899 - Merge Triplets to Form Target Triplet
// https://leetcode.com/problems/merge-triplets-to-form-target-triplet/

impl Solution {
    pub fn merge_triplets(triplets: Vec<Vec<i32>>, target: Vec<i32>) -> bool {
        let mut merged = [0, 0, 0];
        for t in &triplets {
            if t[0] <= target[0] && t[1] <= target[1] && t[2] <= target[2] {
                merged[0] = merged[0].max(t[0]);
                merged[1] = merged[1].max(t[1]);
                merged[2] = merged[2].max(t[2]);
            }
        }
        merged[0] == target[0] && merged[1] == target[1] && merged[2] == target[2]
    }
}
'''

SOLUTIONS[1900] = r'''// LeetCode 1900 - The Earliest and Latest Rounds Where Players Compete
// https://leetcode.com/problems/the-earliest-and-latest-rounds-where-players-compete/

use std::collections::HashMap;

impl Solution {
    pub fn earliest_and_latest(n: i32, first_player: i32, second_player: i32) -> Vec<i32> {
        let first = first_player;
        let second = second_player;
        let mut memo: HashMap<Vec<i32>, (i32, i32)> = HashMap::new();

        fn dfs(
            players: Vec<i32>,
            first: i32,
            second: i32,
            memo: &mut HashMap<Vec<i32>, (i32, i32)>,
        ) -> (i32, i32) {
            if let Some(&cached) = memo.get(&players) {
                return cached;
            }
            let count = players.len();
            let first_index = players.iter().position(|&p| p == first).unwrap();
            let second_index = players.iter().position(|&p| p == second).unwrap();
            if first_index + second_index == count - 1 {
                memo.insert(players, (1, 1));
                return (1, 1);
            }

            let mut choices: Vec<Vec<i32>> = Vec::new();
            for index in 0..count / 2 {
                let left = players[index];
                let right = players[count - 1 - index];
                if left == first || left == second {
                    choices.push(vec![left]);
                } else if right == first || right == second {
                    choices.push(vec![right]);
                } else {
                    choices.push(vec![left, right]);
                }
            }
            if count % 2 == 1 {
                choices.push(vec![players[count / 2]]);
            }

            let mut earliest = i32::MAX;
            let mut latest = 0;
            let mut picks = Vec::new();
            enumerate(
                &choices,
                0,
                &mut picks,
                &mut earliest,
                &mut latest,
                first,
                second,
                memo,
            );
            memo.insert(players, (earliest, latest));
            (earliest, latest)
        }

        fn enumerate(
            choices: &[Vec<i32>],
            idx: usize,
            picks: &mut Vec<i32>,
            earliest: &mut i32,
            latest: &mut i32,
            first: i32,
            second: i32,
            memo: &mut HashMap<Vec<i32>, (i32, i32)>,
        ) {
            if idx == choices.len() {
                let mut winners = picks.clone();
                winners.sort_unstable();
                let (early, late) = dfs(winners, first, second, memo);
                *earliest = (*earliest).min(early + 1);
                *latest = (*latest).max(late + 1);
                return;
            }
            for &player in &choices[idx] {
                picks.push(player);
                enumerate(choices, idx + 1, picks, earliest, latest, first, second, memo);
                picks.pop();
            }
        }

        let players: Vec<i32> = (1..=n).collect();
        let (early, late) = dfs(players, first, second, &mut memo);
        vec![early, late]
    }
}
'''

SKIP_SQL = {1853, 1867, 1873, 1875, 1890, 1892}


def folder_for(num: int) -> Path | None:
    prefix = f"{num:04d}_"
    for path in ROOT.iterdir():
        if path.is_dir() and path.name.startswith(prefix):
            return path
    return None


def main() -> None:
    written = []
    missing = []
    for num, content in sorted(SOLUTIONS.items()):
        folder = folder_for(num)
        if folder is None:
            missing.append(num)
            continue
        path = folder / "solution.rs"
        path.write_text(content.lstrip("\n") if False else content, encoding="utf-8")
        # ensure trailing newline
        if not content.endswith("\n"):
            path.write_text(content + "\n", encoding="utf-8")
        written.append(folder.name)

    print(f"written={len(written)}")
    for name in written:
        print(f"  {name}")
    if missing:
        print(f"missing folders: {missing}")

    # stub check
    stubs = []
    for num in range(1851, 1901):
        if num in SKIP_SQL:
            continue
        folder = folder_for(num)
        if folder is None:
            continue
        text = (folder / "solution.rs").read_text(encoding="utf-8")
        if "fn solve" in text:
            stubs.append(folder.name)
    print(f"remaining_stubs={len(stubs)}")
    for name in stubs:
        print(f"  STUB {name}")


if __name__ == "__main__":
    main()

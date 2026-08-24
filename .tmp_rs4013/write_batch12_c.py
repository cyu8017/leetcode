#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
FILES = {}

def add(folder, body):
    FILES[folder] = body.strip() + "\n"

add("2892_minimizing_array_after_replacing_pairs_with_their_product", r'''
// LeetCode 2892 - Minimizing Array After Replacing Pairs With Their Product
// https://leetcode.com/problems/minimizing-array-after-replacing-pairs-with-their-product/

impl Solution {
    pub fn min_array_length(nums: Vec<i32>, k: i32) -> i32 {
        if nums.is_empty() {
            return 0;
        }
        let mut ans = 1;
        let mut prod = nums[0] as i64;
        let k = k as i64;
        for &v in nums.iter().skip(1) {
            let v = v as i64;
            if prod <= k && v <= k && (v == 0 || prod <= k / v) {
                prod *= v;
            } else {
                ans += 1;
                prod = v;
            }
        }
        ans
    }
}
''')

add("2894_divisible_and_non_divisible_sums_difference", r'''
// LeetCode 2894 - Divisible and Non-divisible Sums Difference
// https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/

impl Solution {
    pub fn difference_of_sums(n: i32, m: i32) -> i32 {
        let mut num1 = 0;
        let mut num2 = 0;
        for i in 1..=n {
            if i % m == 0 {
                num2 += i;
            } else {
                num1 += i;
            }
        }
        num1 - num2
    }
}
''')

add("2895_minimum_processing_time", r'''
// LeetCode 2895 - Minimum Processing Time
// https://leetcode.com/problems/minimum-processing-time/

impl Solution {
    pub fn min_processing_time(mut processor_time: Vec<i32>, mut tasks: Vec<i32>) -> i32 {
        processor_time.sort_unstable();
        tasks.sort_unstable_by(|a, b| b.cmp(a));
        let mut ans = 0;
        for i in 0..processor_time.len() {
            ans = ans.max(processor_time[i] + tasks[i * 4]);
        }
        ans
    }
}
''')

add("2896_apply_operations_to_make_two_strings_equal", r'''
// LeetCode 2896 - Apply Operations to Make Two Strings Equal
// https://leetcode.com/problems/apply-operations-to-make-two-strings-equal/

impl Solution {
    pub fn min_operations(s1: String, s2: String, x: i32) -> i32 {
        let a = s1.as_bytes();
        let b = s2.as_bytes();
        let mut diff = Vec::new();
        for i in 0..a.len() {
            if a[i] != b[i] {
                diff.push(i as i32);
            }
        }
        let m = diff.len();
        if m % 2 == 1 {
            return -1;
        }
        if m == 0 {
            return 0;
        }
        let inf = 1 << 30;
        let mut dp2 = vec![inf; m + 1];
        dp2[0] = 0;
        for i in 0..m {
            if dp2[i] >= inf {
                continue;
            }
            if i + 1 < m {
                let mut cand = diff[i + 1] - diff[i];
                if cand > x {
                    cand = x;
                }
                if dp2[i] + cand < dp2[i + 2] {
                    dp2[i + 2] = dp2[i] + cand;
                }
            }
        }
        if dp2[m] >= inf { -1 } else { dp2[m] }
    }
}
''')

add("2897_apply_operations_on_array_to_maximize_sum_of_squares", r'''
// LeetCode 2897 - Apply Operations on Array to Maximize Sum of Squares
// https://leetcode.com/problems/apply-operations-on-array-to-maximize-sum-of-squares/

impl Solution {
    pub fn max_sum(nums: Vec<i32>, k: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let mut cnt = [0i32; 32];
        for v in nums {
            for b in 0..32 {
                if (v & (1 << b)) != 0 {
                    cnt[b] += 1;
                }
            }
        }
        let mut ans = 0i64;
        for _ in 0..k {
            let mut cur = 0i32;
            for b in 0..32 {
                if cnt[b] > 0 {
                    cur |= 1 << b;
                    cnt[b] -= 1;
                }
            }
            let c = (cur as i64) % MOD;
            ans = (ans + c * c % MOD) % MOD;
        }
        ans as i32
    }
}
''')

add("2898_maximum_linear_stock_score", r'''
// LeetCode 2898 - Maximum Linear Stock Score
// https://leetcode.com/problems/maximum-linear-stock-score/

use std::collections::HashMap;

impl Solution {
    pub fn max_score(prices: Vec<i32>) -> i64 {
        let mut best: HashMap<i32, i64> = HashMap::new();
        let mut ans = 0i64;
        for (i, &p) in prices.iter().enumerate() {
            let key = p - (i as i32 + 1);
            let cand = *best.get(&key).unwrap_or(&0) + p as i64;
            let e = best.entry(key).or_insert(0);
            if cand > *e {
                *e = cand;
            }
            if *e > ans {
                ans = *e;
            }
        }
        ans
    }
}
''')

add("2899_last_visited_integers", r'''
// LeetCode 2899 - Last Visited Integers
// https://leetcode.com/problems/last-visited-integers/

impl Solution {
    pub fn last_visited_integers(nums: Vec<i32>) -> Vec<i32> {
        let mut seen = Vec::new();
        let mut ans = Vec::new();
        let mut k = 0usize;
        for v in nums {
            if v != -1 {
                seen.push(v);
                k = 0;
            } else {
                k += 1;
                if k > seen.len() {
                    ans.push(-1);
                } else {
                    ans.push(seen[seen.len() - k]);
                }
            }
        }
        ans
    }
}
''')

add("2900_longest_unequal_adjacent_groups_subsequence_i", r'''
// LeetCode 2900 - Longest Unequal Adjacent Groups Subsequence I
// https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i/

impl Solution {
    pub fn get_longest_subsequence(words: Vec<String>, groups: Vec<i32>) -> Vec<String> {
        let mut ans = vec![words[0].clone()];
        let mut last = groups[0];
        for i in 1..words.len() {
            if groups[i] != last {
                ans.push(words[i].clone());
                last = groups[i];
            }
        }
        ans
    }
}
''')

add("2901_longest_unequal_adjacent_groups_subsequence_ii", r'''
// LeetCode 2901 - Longest Unequal Adjacent Groups Subsequence II
// https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-ii/

impl Solution {
    pub fn get_words_in_longest_subsequence(words: Vec<String>, groups: Vec<i32>) -> Vec<String> {
        let n = words.len();
        let mut dp = vec![1i32; n];
        let mut prev = vec![-1i32; n];
        let hamming = |a: &str, b: &str| -> i32 {
            if a.len() != b.len() {
                return 100;
            }
            a.bytes().zip(b.bytes()).filter(|(x, y)| x != y).count() as i32
        };
        let mut best = 1;
        let mut best_i = 0usize;
        for i in 0..n {
            for j in 0..i {
                if groups[i] != groups[j] && hamming(&words[i], &words[j]) == 1 && dp[j] + 1 > dp[i] {
                    dp[i] = dp[j] + 1;
                    prev[i] = j as i32;
                }
            }
            if dp[i] > best {
                best = dp[i];
                best_i = i;
            }
        }
        let mut path = Vec::new();
        let mut i = best_i as i32;
        while i != -1 {
            path.push(words[i as usize].clone());
            i = prev[i as usize];
        }
        path.reverse();
        path
    }
}
''')

add("2902_count_of_sub_multisets_with_bounded_sum", r'''
// LeetCode 2902 - Count of Sub-Multisets With Bounded Sum
// https://leetcode.com/problems/count-of-sub-multisets-with-bounded-sum/

use std::collections::HashMap;

impl Solution {
    pub fn count_sub_multisets(nums: Vec<i32>, l: i32, mut r: i32) -> i32 {
        const MOD: i32 = 1_000_000_007;
        let mut freq: HashMap<i32, i32> = HashMap::new();
        let mut total = 0i32;
        for v in nums {
            *freq.entry(v).or_insert(0) += 1;
            total += v;
        }
        if total < l {
            return 0;
        }
        if r > total {
            r = total;
        }
        let mut dp = vec![0i32; r as usize + 1];
        dp[0] = 1;
        let zeros = *freq.get(&0).unwrap_or(&0);
        freq.remove(&0);
        for (v, c) in freq {
            let mut ndp = vec![0i32; r as usize + 1];
            for sum in 0..=r as usize {
                if dp[sum] == 0 {
                    continue;
                }
                let mut k = 0i32;
                while k <= c && sum + (k * v) as usize <= r as usize {
                    let idx = sum + (k * v) as usize;
                    ndp[idx] = (ndp[idx] + dp[sum]) % MOD;
                    k += 1;
                }
            }
            dp = ndp;
        }
        let mut ans = 0i32;
        for s in l..=r {
            ans = (ans + dp[s as usize]) % MOD;
        }
        ((ans as i64) * (zeros as i64 + 1) % MOD as i64) as i32
    }
}
''')

add("2903_find_indices_with_index_and_value_difference_i", r'''
// LeetCode 2903 - Find Indices With Index and Value Difference I
// https://leetcode.com/problems/find-indices-with-index-and-value-difference-i/

impl Solution {
    pub fn find_indices(nums: Vec<i32>, index_difference: i32, value_difference: i32) -> Vec<i32> {
        let n = nums.len();
        for i in 0..n {
            for j in i..n {
                let di = (j as i32 - i as i32).abs();
                let dv = (nums[i] - nums[j]).abs();
                if di >= index_difference && dv >= value_difference {
                    return vec![i as i32, j as i32];
                }
            }
        }
        vec![-1, -1]
    }
}
''')

add("2904_shortest_and_lexicographically_smallest_beautiful_string", r'''
// LeetCode 2904 - Shortest and Lexicographically Smallest Beautiful String
// https://leetcode.com/problems/shortest-and-lexicographically-smallest-beautiful-string/

impl Solution {
    pub fn shortest_beautiful_substring(s: String, k: i32) -> String {
        let bytes = s.as_bytes();
        let n = bytes.len();
        let mut ans = String::new();
        for i in 0..n {
            let mut ones = 0;
            for j in i..n {
                if bytes[j] == b'1' {
                    ones += 1;
                }
                if ones == k {
                    let cand = s[i..=j].to_string();
                    if ans.is_empty()
                        || cand.len() < ans.len()
                        || (cand.len() == ans.len() && cand < ans)
                    {
                        ans = cand;
                    }
                    break;
                }
                if ones > k {
                    break;
                }
            }
        }
        ans
    }
}
''')

add("2905_find_indices_with_index_and_value_difference_ii", r'''
// LeetCode 2905 - Find Indices With Index and Value Difference II
// https://leetcode.com/problems/find-indices-with-index-and-value-difference-ii/

impl Solution {
    pub fn find_indices(nums: Vec<i32>, index_difference: i32, value_difference: i32) -> Vec<i32> {
        let n = nums.len();
        let mut min_idx = 0usize;
        let mut max_idx = 0usize;
        let start = index_difference as usize;
        for j in start..n {
            let i = j - start;
            if nums[i] < nums[min_idx] {
                min_idx = i;
            }
            if nums[i] > nums[max_idx] {
                max_idx = i;
            }
            if nums[j] - nums[min_idx] >= value_difference {
                return vec![min_idx as i32, j as i32];
            }
            if nums[max_idx] - nums[j] >= value_difference {
                return vec![max_idx as i32, j as i32];
            }
        }
        vec![-1, -1]
    }
}
''')

add("2906_construct_product_matrix", r'''
// LeetCode 2906 - Construct Product Matrix
// https://leetcode.com/problems/construct-product-matrix/

impl Solution {
    pub fn construct_product_matrix(grid: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        const MOD: i64 = 12345;
        let m = grid.len();
        let n = grid[0].len();
        let mut ans = vec![vec![0i32; n]; m];
        let mut pref = 1i64;
        for i in 0..m {
            for j in 0..n {
                ans[i][j] = pref as i32;
                pref = pref * (grid[i][j] as i64 % MOD) % MOD;
            }
        }
        let mut suf = 1i64;
        for i in (0..m).rev() {
            for j in (0..n).rev() {
                ans[i][j] = (ans[i][j] as i64 * suf % MOD) as i32;
                suf = suf * (grid[i][j] as i64 % MOD) % MOD;
            }
        }
        ans
    }
}
''')

add("2907_maximum_profitable_triplets_with_increasing_prices_i", r'''
// LeetCode 2907 - Maximum Profitable Triplets With Increasing Prices I
// https://leetcode.com/problems/maximum-profitable-triplets-with-increasing-prices-i/

impl Solution {
    pub fn max_profit(prices: Vec<i32>, profits: Vec<i32>) -> i32 {
        let n = prices.len();
        let mut ans = -1;
        for j in 0..n {
            let mut best_l = -1;
            let mut best_r = -1;
            for i in 0..j {
                if prices[i] < prices[j] && profits[i] > best_l {
                    best_l = profits[i];
                }
            }
            for k in j + 1..n {
                if prices[k] > prices[j] && profits[k] > best_r {
                    best_r = profits[k];
                }
            }
            if best_l >= 0 && best_r >= 0 {
                ans = ans.max(best_l + profits[j] + best_r);
            }
        }
        ans
    }
}
''')

add("2908_minimum_sum_of_mountain_triplets_i", r'''
// LeetCode 2908 - Minimum Sum of Mountain Triplets I
// https://leetcode.com/problems/minimum-sum-of-mountain-triplets-i/

impl Solution {
    pub fn minimum_sum(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut ans = 1 << 30;
        for j in 1..n - 1 {
            let mut left = 1 << 30;
            let mut right = 1 << 30;
            for i in 0..j {
                if nums[i] < nums[j] && nums[i] < left {
                    left = nums[i];
                }
            }
            for k in j + 1..n {
                if nums[k] < nums[j] && nums[k] < right {
                    right = nums[k];
                }
            }
            if left < (1 << 30) && right < (1 << 30) {
                ans = ans.min(left + nums[j] + right);
            }
        }
        if ans == (1 << 30) { -1 } else { ans }
    }
}
''')

add("2909_minimum_sum_of_mountain_triplets_ii", r'''
// LeetCode 2909 - Minimum Sum of Mountain Triplets II
// https://leetcode.com/problems/minimum-sum-of-mountain-triplets-ii/

impl Solution {
    pub fn minimum_sum(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut left = vec![0i32; n];
        let mut right = vec![0i32; n];
        let mut mn = 1 << 30;
        for i in 0..n {
            left[i] = mn;
            if nums[i] < mn {
                mn = nums[i];
            }
        }
        mn = 1 << 30;
        for i in (0..n).rev() {
            right[i] = mn;
            if nums[i] < mn {
                mn = nums[i];
            }
        }
        let mut ans = 1 << 30;
        for j in 1..n - 1 {
            if left[j] < nums[j] && right[j] < nums[j] {
                ans = ans.min(left[j] + nums[j] + right[j]);
            }
        }
        if ans == (1 << 30) { -1 } else { ans }
    }
}
''')

add("2910_minimum_number_of_groups_to_create_a_valid_assignment", r'''
// LeetCode 2910 - Minimum Number of Groups to Create a Valid Assignment
// https://leetcode.com/problems/minimum-number-of-groups-to-create-a-valid-assignment/

use std::collections::HashMap;

impl Solution {
    pub fn min_groups_for_valid_assignment(balls: Vec<i32>) -> i32 {
        let mut freq: HashMap<i32, i32> = HashMap::new();
        for b in &balls {
            *freq.entry(*b).or_insert(0) += 1;
        }
        let counts: Vec<i32> = freq.values().copied().collect();
        let min_f = *counts.iter().min().unwrap_or(&1);
        for size in (1..=min_f).rev() {
            let mut ok = true;
            let mut groups = 0;
            for &c in &counts {
                let rem = c % (size + 1);
                let g2 = c / (size + 1);
                if rem == 0 {
                    groups += g2;
                } else if size - rem <= g2 {
                    groups += g2 + 1;
                } else {
                    ok = false;
                    break;
                }
            }
            if ok {
                return groups;
            }
        }
        balls.len() as i32
    }
}
''')

add("2911_minimum_changes_to_make_k_semi_palindromes", r'''
// LeetCode 2911 - Minimum Changes to Make K Semi-palindromes
// https://leetcode.com/problems/minimum-changes-to-make-k-semi-palindromes/

impl Solution {
    pub fn minimum_changes(s: String, k: i32) -> i32 {
        let bytes = s.as_bytes();
        let n = bytes.len();
        let mut cost = vec![vec![1 << 20; n]; n];
        let semi_cost = |l: usize, r: usize| -> i32 {
            let length = r - l + 1;
            let mut best = 1 << 20;
            for d in 1..length {
                if length % d != 0 {
                    continue;
                }
                let mut chg = 0;
                for start in 0..d {
                    let mut chars = Vec::new();
                    let mut i = l + start;
                    while i <= r {
                        chars.push(bytes[i]);
                        i += d;
                    }
                    let mut a = 0;
                    let mut b = chars.len() - 1;
                    while a < b {
                        if chars[a] != chars[b] {
                            chg += 1;
                        }
                        a += 1;
                        b -= 1;
                    }
                }
                best = best.min(chg);
            }
            best
        };
        for i in 0..n {
            for j in i + 1..n {
                cost[i][j] = semi_cost(i, j);
            }
        }
        let k = k as usize;
        let mut dp = vec![vec![1 << 20; n + 1]; k + 1];
        dp[0][0] = 0;
        for p in 1..=k {
            for i in 1..=n {
                for t in 0..i.saturating_sub(1) {
                    let cand = dp[p - 1][t] + cost[t][i - 1];
                    if cand < dp[p][i] {
                        dp[p][i] = cand;
                    }
                }
            }
        }
        dp[k][n]
    }
}
''')

add("2912_number_of_ways_to_reach_destination_in_the_grid", r'''
// LeetCode 2912 - Number of Ways to Reach Destination in the Grid
// https://leetcode.com/problems/number-of-ways-to-reach-destination-in-the-grid/

impl Solution {
    pub fn number_of_ways(n: i32, m: i32, k: i32, source: Vec<i32>, dest: Vec<i32>) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let sx = source[0];
        let sy = source[1];
        let tx = dest[0];
        let ty = dest[1];
        let mut same = 0i64;
        let mut row = 0i64;
        let mut col = 0i64;
        let mut other = 0i64;
        if sx == tx && sy == ty {
            same = 1;
        } else if sx == tx {
            row = 1;
        } else if sy == ty {
            col = 1;
        } else {
            other = 1;
        }
        let n = n as i64;
        let m = m as i64;
        for _ in 0..k {
            let ns = (row * (m - 1) + col * (n - 1)) % MOD;
            let nr = (same + row * (m - 2) % MOD + other * (n - 1) % MOD) % MOD;
            let nc = (same + col * (n - 2) % MOD + other * (m - 1) % MOD) % MOD;
            let no = (row * (n - 1) + col * (m - 1) + other * (n + m - 4) % MOD) % MOD;
            same = ns;
            row = nr;
            col = nc;
            other = no;
        }
        if sx == tx && sy == ty {
            same as i32
        } else if sx == tx {
            row as i32
        } else if sy == ty {
            col as i32
        } else {
            other as i32
        }
    }
}
''')

add("2913_subarrays_distinct_element_sum_of_squares_i", r'''
// LeetCode 2913 - Subarrays Distinct Element Sum of Squares I
// https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-i/

use std::collections::HashSet;

impl Solution {
    pub fn sum_counts(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut ans = 0;
        for i in 0..n {
            let mut seen = HashSet::new();
            for j in i..n {
                seen.insert(nums[j]);
                let d = seen.len() as i32;
                ans += d * d;
            }
        }
        ans
    }
}
''')

add("2914_minimum_number_of_changes_to_make_binary_string_beautiful", r'''
// LeetCode 2914 - Minimum Number of Changes to Make Binary String Beautiful
// https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful/

impl Solution {
    pub fn min_changes(s: String) -> i32 {
        let b = s.as_bytes();
        let mut ans = 0;
        let mut i = 0;
        while i < b.len() {
            if b[i] != b[i + 1] {
                ans += 1;
            }
            i += 2;
        }
        ans
    }
}
''')

add("2915_length_of_the_longest_subsequence_that_sums_to_target", r'''
// LeetCode 2915 - Length of the Longest Subsequence That Sums to Target
// https://leetcode.com/problems/length-of-the-longest-subsequence-that-sums-to-target/

impl Solution {
    pub fn length_of_longest_subsequence(nums: Vec<i32>, target: i32) -> i32 {
        let target = target as usize;
        let mut dp = vec![-1i32; target + 1];
        dp[0] = 0;
        for v in nums {
            let v = v as usize;
            for s in (v..=target).rev() {
                if dp[s - v] >= 0 && dp[s - v] + 1 > dp[s] {
                    dp[s] = dp[s - v] + 1;
                }
            }
        }
        dp[target]
    }
}
''')

add("2916_subarrays_distinct_element_sum_of_squares_ii", r'''
// LeetCode 2916 - Subarrays Distinct Element Sum of Squares II
// https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-ii/

use std::collections::HashMap;

impl Solution {
    pub fn sum_counts(nums: Vec<i32>) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let n = nums.len();
        let mut last: HashMap<i32, usize> = HashMap::new();
        #[derive(Clone, Copy, Default)]
        struct Node {
            sum: i32,
            sum_sq: i32,
            lazy: i32,
        }
        let mut tree = vec![Node::default(); 4 * (n + 2)];
        fn apply(tree: &mut [Node], idx: usize, l: usize, r: usize, val: i32) {
            let length = (r - l + 1) as i64;
            let val = val as i64;
            tree[idx].sum_sq = ((tree[idx].sum_sq as i64
                + 2 * val % MOD * tree[idx].sum as i64 % MOD
                + val % MOD * val % MOD * length % MOD)
                % MOD) as i32;
            tree[idx].sum = ((tree[idx].sum as i64 + val % MOD * length % MOD) % MOD) as i32;
            tree[idx].lazy = ((tree[idx].lazy as i64 + val) % MOD) as i32;
        }
        fn update(tree: &mut [Node], idx: usize, l: usize, r: usize, ql: usize, qr: usize, val: i32) {
            if ql > r || qr < l {
                return;
            }
            if ql <= l && r <= qr {
                apply(tree, idx, l, r, val);
                return;
            }
            if tree[idx].lazy != 0 && l != r {
                let mid = (l + r) / 2;
                apply(tree, idx * 2, l, mid, tree[idx].lazy);
                apply(tree, idx * 2 + 1, mid + 1, r, tree[idx].lazy);
                tree[idx].lazy = 0;
            }
            let mid = (l + r) / 2;
            update(tree, idx * 2, l, mid, ql, qr, val);
            update(tree, idx * 2 + 1, mid + 1, r, ql, qr, val);
            tree[idx].sum = (tree[idx * 2].sum + tree[idx * 2 + 1].sum) % MOD as i32;
            tree[idx].sum_sq = (tree[idx * 2].sum_sq + tree[idx * 2 + 1].sum_sq) % MOD as i32;
        }
        let mut ans = 0i32;
        for i in 1..=n {
            let v = nums[i - 1];
            let prev = *last.get(&v).unwrap_or(&0);
            update(&mut tree, 1, 1, n, prev + 1, i, 1);
            ans = (ans + tree[1].sum_sq) % MOD as i32;
            last.insert(v, i);
        }
        ans
    }
}
''')

def main():
    n = 0
    for folder, body in FILES.items():
        path = ROOT / folder / "solution.rs"
        path.write_text(body, encoding="utf-8", newline="\n")
        n += 1
        print("wrote", folder)
    print("batch_c", n)

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
FILES = {}

FILES["2963_count_the_number_of_good_partitions"] = r'''// LeetCode 2963 - Count the Number of Good Partitions
// https://leetcode.com/problems/count-the-number-of-good-partitions/

use std::collections::HashMap;

impl Solution {
    pub fn number_of_good_partitions(nums: Vec<i32>) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let mut last = HashMap::new();
        for (i, &v) in nums.iter().enumerate() {
            last.insert(v, i);
        }
        let mut ans = 1i64;
        let mut end = 0;
        for i in 0..nums.len() {
            if last[&nums[i]] > end {
                end = last[&nums[i]];
            }
            if i == end && i != nums.len() - 1 {
                ans = ans * 2 % MOD;
            }
        }
        ans as i32
    }
}
'''

FILES["2964_number_of_divisible_triplet_sums"] = r'''// LeetCode 2964 - Number of Divisible Triplet Sums
// https://leetcode.com/problems/number-of-divisible-triplet-sums/

use std::collections::HashMap;

impl Solution {
    pub fn divisible_triplet_count(nums: Vec<i32>, d: i32) -> i32 {
        let n = nums.len();
        let mut ans = 0;
        for i in 0..n {
            let mut freq: HashMap<i32, i32> = HashMap::new();
            for j in (i + 1)..n {
                let need = (d - (nums[i] + nums[j]) % d) % d;
                ans += *freq.get(&need).unwrap_or(&0);
                *freq.entry(nums[j] % d).or_insert(0) += 1;
            }
        }
        ans
    }
}
'''

FILES["2965_find_missing_and_repeated_values"] = r'''// LeetCode 2965 - Find Missing and Repeated Values
// https://leetcode.com/problems/find-missing-and-repeated-values/

impl Solution {
    pub fn find_missing_and_repeated_values(grid: Vec<Vec<i32>>) -> Vec<i32> {
        let n = grid.len();
        let mut freq = vec![0; n * n + 1];
        for row in &grid {
            for &v in row {
                freq[v as usize] += 1;
            }
        }
        let mut rep = 0;
        let mut miss = 0;
        for i in 1..=n * n {
            if freq[i] == 2 {
                rep = i as i32;
            }
            if freq[i] == 0 {
                miss = i as i32;
            }
        }
        vec![rep, miss]
    }
}
'''

FILES["2966_divide_array_into_arrays_with_max_difference"] = r'''// LeetCode 2966 - Divide Array Into Arrays With Max Difference
// https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/

impl Solution {
    pub fn divide_array(mut nums: Vec<i32>, k: i32) -> Vec<Vec<i32>> {
        nums.sort_unstable();
        let mut ans = Vec::new();
        let mut i = 0;
        while i < nums.len() {
            if nums[i + 2] - nums[i] > k {
                return vec![];
            }
            ans.push(vec![nums[i], nums[i + 1], nums[i + 2]]);
            i += 3;
        }
        ans
    }
}
'''

FILES["2967_minimum_cost_to_make_array_equalindromic"] = r'''// LeetCode 2967 - Minimum Cost to Make Array Equalindromic
// https://leetcode.com/problems/minimum-cost-to-make-array-equalindromic/

impl Solution {
    pub fn minimum_cost(mut nums: Vec<i32>) -> i64 {
        nums.sort_unstable();
        let n = nums.len();
        let median = nums[n / 2];
        fn make_pal(x: i32) -> i32 {
            let mut s: Vec<u8> = x.to_string().into_bytes();
            let mut i = 0;
            let mut j = s.len() - 1;
            while i < j {
                s[j] = s[i];
                i += 1;
                j -= 1;
            }
            String::from_utf8(s).unwrap().parse().unwrap_or(0)
        }
        let mut candidates = Vec::new();
        candidates.push(make_pal(median));
        let s = median.to_string();
        let half: i32 = s[..(s.len() + 1) / 2].parse().unwrap();
        for d in -2..=2 {
            let h = half + d;
            if h <= 0 {
                continue;
            }
            let hs = h.to_string();
            let pal = if s.len() % 2 == 0 {
                let mut rb = hs.clone();
                let rev: String = rb.chars().rev().collect();
                hs + &rev
            } else {
                let prefix: String = hs.chars().take(hs.len() - 1).collect();
                let rev: String = prefix.chars().rev().collect();
                hs + &rev
            };
            if let Ok(v) = pal.parse::<i32>() {
                candidates.push(v);
            }
        }
        for v in [1, 9, 11, 99, 101] {
            candidates.push(v);
        }
        let cost = |p: i32| -> i64 {
            nums.iter().map(|&v| (v as i64 - p as i64).abs()).sum()
        };
        let mut ans = 1i64 << 62;
        for p in candidates {
            if p <= 0 {
                continue;
            }
            ans = ans.min(cost(p));
        }
        ans
    }
}
'''

FILES["2968_apply_operations_to_maximize_frequency_score"] = r'''// LeetCode 2968 - Apply Operations to Maximize Frequency Score
// https://leetcode.com/problems/apply-operations-to-maximize-frequency-score/

impl Solution {
    pub fn max_frequency_score(mut nums: Vec<i32>, k: i64) -> i32 {
        nums.sort_unstable();
        let n = nums.len();
        let mut pref = vec![0i64; n + 1];
        for i in 0..n {
            pref[i + 1] = pref[i] + nums[i] as i64;
        }
        let cost = |l: usize, r: usize| -> i64 {
            let mid = (l + r) / 2;
            let left = nums[mid] as i64 * (mid - l) as i64 - (pref[mid] - pref[l]);
            let right = (pref[r + 1] - pref[mid + 1]) - nums[mid] as i64 * (r - mid) as i64;
            left + right
        };
        let mut ans = 1;
        let mut left = 0;
        for right in 0..n {
            while cost(left, right) > k {
                left += 1;
            }
            ans = ans.max((right - left + 1) as i32);
        }
        ans
    }
}
'''

FILES["2969_minimum_number_of_coins_for_fruits_ii"] = r'''// LeetCode 2969 - Minimum Number of Coins for Fruits II
// https://leetcode.com/problems/minimum-number-of-coins-for-fruits-ii/

impl Solution {
    pub fn minimum_coins(prices: Vec<i32>) -> i32 {
        let n = prices.len();
        let mut dp = vec![1 << 30; n + 1];
        dp[0] = 0;
        for i in 1..=n {
            let mut j = i;
            while j <= n && j <= 2 * i {
                dp[j] = dp[j].min(dp[i - 1] + prices[i - 1]);
                j += 1;
            }
        }
        dp[n]
    }
}
'''

FILES["2970_count_the_number_of_incremovable_subarrays_i"] = r'''// LeetCode 2970 - Count the Number of Incremovable Subarrays I
// https://leetcode.com/problems/count-the-number-of-incremovable-subarrays-i/

impl Solution {
    pub fn incremovable_subarray_count(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut ans = 0;
        for i in 0..n {
            for j in i..n {
                let mut prev = -1;
                let mut ok = true;
                for t in 0..n {
                    if t >= i && t <= j {
                        continue;
                    }
                    if nums[t] <= prev {
                        ok = false;
                        break;
                    }
                    prev = nums[t];
                }
                if ok {
                    ans += 1;
                }
            }
        }
        ans
    }
}
'''

FILES["2971_find_polygon_with_the_largest_perimeter"] = r'''// LeetCode 2971 - Find Polygon With the Largest Perimeter
// https://leetcode.com/problems/find-polygon-with-the-largest-perimeter/

impl Solution {
    pub fn largest_perimeter(mut nums: Vec<i32>) -> i64 {
        nums.sort_unstable();
        let mut sum: i64 = nums.iter().map(|&v| v as i64).sum();
        for i in (2..nums.len()).rev() {
            sum -= nums[i] as i64;
            if sum > nums[i] as i64 {
                return sum + nums[i] as i64;
            }
        }
        -1
    }
}
'''

FILES["2972_count_the_number_of_incremovable_subarrays_ii"] = r'''// LeetCode 2972 - Count the Number of Incremovable Subarrays II
// https://leetcode.com/problems/count-the-number-of-incremovable-subarrays-ii/

impl Solution {
    pub fn incremovable_subarray_count(nums: Vec<i32>) -> i64 {
        let n = nums.len();
        let mut left: i32 = 0;
        while (left as usize) + 1 < n && nums[left as usize] < nums[left as usize + 1] {
            left += 1;
        }
        if left as usize == n - 1 {
            return n as i64 * (n as i64 + 1) / 2;
        }
        let mut ans = left as i64 + 2;
        let mut right = n as i32 - 1;
        while right > 0 && (right as usize == n - 1 || nums[right as usize] < nums[right as usize + 1]) {
            while left >= 0 && nums[left as usize] >= nums[right as usize] {
                left -= 1;
            }
            ans += left as i64 + 2;
            right -= 1;
            if right > 0 && nums[right as usize] >= nums[right as usize + 1] {
                break;
            }
        }
        ans
    }
}
'''

FILES["2973_find_number_of_coins_to_place_in_tree_nodes"] = r'''// LeetCode 2973 - Find Number of Coins to Place in Tree Nodes
// https://leetcode.com/problems/find-number-of-coins-to-place-in-tree-nodes/

impl Solution {
    pub fn placed_coins(edges: Vec<Vec<i32>>, cost: Vec<i32>) -> Vec<i64> {
        let n = cost.len();
        let mut g = vec![Vec::new(); n];
        for e in &edges {
            g[e[0] as usize].push(e[1] as usize);
            g[e[1] as usize].push(e[0] as usize);
        }
        let mut ans = vec![0i64; n];
        fn dfs(u: usize, p: i32, g: &[Vec<usize>], cost: &[i32], ans: &mut [i64]) -> Vec<i32> {
            let mut vals = vec![cost[u]];
            for &v in &g[u] {
                if v as i32 == p {
                    continue;
                }
                let mut child = dfs(v, u as i32, g, cost, ans);
                vals.append(&mut child);
            }
            vals.sort_unstable();
            if vals.len() < 3 {
                ans[u] = 1;
            } else {
                let m = vals.len();
                let cand1 = vals[m - 1] as i64 * vals[m - 2] as i64 * vals[m - 3] as i64;
                let cand2 = vals[0] as i64 * vals[1] as i64 * vals[m - 1] as i64;
                let mut best = cand1.max(cand2);
                if best < 0 {
                    best = 0;
                }
                ans[u] = best;
            }
            if vals.len() <= 5 {
                return vals;
            }
            vec![
                vals[0],
                vals[1],
                vals[vals.len() - 3],
                vals[vals.len() - 2],
                vals[vals.len() - 1],
            ]
        }
        dfs(0, -1, &g, &cost, &mut ans);
        ans
    }
}
'''

FILES["2974_minimum_number_game"] = r'''// LeetCode 2974 - Minimum Number Game
// https://leetcode.com/problems/minimum-number-game/

impl Solution {
    pub fn number_game(mut nums: Vec<i32>) -> Vec<i32> {
        nums.sort_unstable();
        let mut i = 0;
        while i + 1 < nums.len() {
            nums.swap(i, i + 1);
            i += 2;
        }
        nums
    }
}
'''

FILES["2975_maximum_square_area_by_removing_fences_from_a_field"] = r'''// LeetCode 2975 - Maximum Square Area by Removing Fences From a Field
// https://leetcode.com/problems/maximum-square-area-by-removing-fences-from-a-field/

use std::collections::HashSet;

impl Solution {
    pub fn maximize_square_area(m: i32, n: i32, h_fences: Vec<i32>, v_fences: Vec<i32>) -> i32 {
        const MOD: i64 = 1_000_000_007;
        fn gaps(mut fences: Vec<i32>, bound: i32) -> HashSet<i32> {
            fences.push(1);
            fences.push(bound);
            fences.sort_unstable();
            let mut g = HashSet::new();
            for i in 0..fences.len() {
                for j in (i + 1)..fences.len() {
                    g.insert(fences[j] - fences[i]);
                }
            }
            g
        }
        let hg = gaps(h_fences, m);
        let vg = gaps(v_fences, n);
        let mut best = -1i64;
        for &g in &hg {
            if vg.contains(&g) && g as i64 > best {
                best = g as i64;
            }
        }
        if best < 0 {
            return -1;
        }
        (best * best % MOD) as i32
    }
}
'''

FILES["2976_minimum_cost_to_convert_string_i"] = r'''// LeetCode 2976 - Minimum Cost to Convert String I
// https://leetcode.com/problems/minimum-cost-to-convert-string-i/

impl Solution {
    pub fn minimum_cost(
        source: String,
        target: String,
        original: Vec<char>,
        changed: Vec<char>,
        cost: Vec<i32>,
    ) -> i64 {
        const INF: i64 = 1i64 << 60;
        let mut dist = vec![vec![INF; 26]; 26];
        for i in 0..26 {
            dist[i][i] = 0;
        }
        for i in 0..original.len() {
            let u = (original[i] as u8 - b'a') as usize;
            let v = (changed[i] as u8 - b'a') as usize;
            let ww = cost[i] as i64;
            if ww < dist[u][v] {
                dist[u][v] = ww;
            }
        }
        for k in 0..26 {
            for i in 0..26 {
                for j in 0..26 {
                    if dist[i][k] + dist[k][j] < dist[i][j] {
                        dist[i][j] = dist[i][k] + dist[k][j];
                    }
                }
            }
        }
        let src = source.as_bytes();
        let tgt = target.as_bytes();
        let mut ans = 0i64;
        for i in 0..src.len() {
            let a = (src[i] - b'a') as usize;
            let b = (tgt[i] - b'a') as usize;
            if dist[a][b] >= INF / 2 {
                return -1;
            }
            ans += dist[a][b];
        }
        ans
    }
}
'''

FILES["2977_minimum_cost_to_convert_string_ii"] = r'''// LeetCode 2977 - Minimum Cost to Convert String II
// https://leetcode.com/problems/minimum-cost-to-convert-string-ii/

use std::collections::{HashMap, HashSet};

impl Solution {
    pub fn minimum_cost(
        source: String,
        target: String,
        original: Vec<String>,
        changed: Vec<String>,
        cost: Vec<i32>,
    ) -> i64 {
        const INF: i64 = 1i64 << 60;
        let mut ids: HashMap<String, usize> = HashMap::new();
        let mut next_id = 0usize;
        let mut get_id = |s: &str, ids: &mut HashMap<String, usize>, next_id: &mut usize| -> usize {
            if let Some(&v) = ids.get(s) {
                return v;
            }
            let v = *next_id;
            ids.insert(s.to_string(), v);
            *next_id += 1;
            v
        };
        for i in 0..original.len() {
            get_id(&original[i], &mut ids, &mut next_id);
            get_id(&changed[i], &mut ids, &mut next_id);
        }
        let m = ids.len();
        let mut dist = vec![vec![INF; m]; m];
        for i in 0..m {
            dist[i][i] = 0;
        }
        for i in 0..original.len() {
            let u = *ids.get(&original[i]).unwrap();
            let v = *ids.get(&changed[i]).unwrap();
            let ww = cost[i] as i64;
            if ww < dist[u][v] {
                dist[u][v] = ww;
            }
        }
        for k in 0..m {
            for i in 0..m {
                for j in 0..m {
                    if dist[i][k] + dist[k][j] < dist[i][j] {
                        dist[i][j] = dist[i][k] + dist[k][j];
                    }
                }
            }
        }
        let n = source.len();
        let mut dp = vec![INF; n + 1];
        dp[0] = 0;
        let lens: HashSet<usize> = ids.keys().map(|s| s.len()).collect();
        let src = source.as_bytes();
        let tgt = target.as_bytes();
        for i in 0..n {
            if dp[i] >= INF / 2 {
                continue;
            }
            if src[i] == tgt[i] && dp[i] < dp[i + 1] {
                dp[i + 1] = dp[i];
            }
            for &l in &lens {
                if i + l > n {
                    continue;
                }
                let ss = &source[i..i + l];
                let tt = &target[i..i + l];
                if let (Some(&iu), Some(&iv)) = (ids.get(ss), ids.get(tt)) {
                    if dist[iu][iv] < INF / 2 {
                        let cand = dp[i] + dist[iu][iv];
                        if cand < dp[i + l] {
                            dp[i + l] = cand;
                        }
                    }
                }
            }
        }
        if dp[n] >= INF / 2 {
            -1
        } else {
            dp[n]
        }
    }
}
'''

FILES["2979_most_expensive_item_that_can_not_be_bought"] = r'''// LeetCode 2979 - Most Expensive Item That Can Not Be Bought
// https://leetcode.com/problems/most-expensive-item-that-can-not-be-bought/

impl Solution {
    pub fn most_expensive_item(prime_one: i32, prime_two: i32) -> i32 {
        prime_one * prime_two - prime_one - prime_two
    }
}
'''

FILES["2980_check_if_bitwise_or_has_trailing_zeros"] = r'''// LeetCode 2980 - Check if Bitwise OR Has Trailing Zeros
// https://leetcode.com/problems/check-if-bitwise-or-has-trailing-zeros/

impl Solution {
    pub fn has_trailing_zeros(nums: Vec<i32>) -> bool {
        let mut even = 0;
        for v in nums {
            if v % 2 == 0 {
                even += 1;
                if even >= 2 {
                    return true;
                }
            }
        }
        false
    }
}
'''

FILES["2981_find_longest_special_substring_that_occurs_thrice_i"] = r'''// LeetCode 2981 - Find Longest Special Substring That Occurs Thrice I
// https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-i/

impl Solution {
    pub fn maximum_length(s: String) -> i32 {
        let b = s.as_bytes();
        let n = b.len();
        let mut ans = -1;
        for i in 0..n {
            for j in i..n {
                if b[j] != b[i] {
                    break;
                }
                let len = j - i + 1;
                let mut cnt = 0;
                for k in 0..=n.saturating_sub(len) {
                    if &b[k..k + len] == &b[i..i + len] {
                        cnt += 1;
                    }
                }
                if cnt >= 3 && len as i32 > ans {
                    ans = len as i32;
                }
            }
        }
        ans
    }
}
'''

FILES["2982_find_longest_special_substring_that_occurs_thrice_ii"] = r'''// LeetCode 2982 - Find Longest Special Substring That Occurs Thrice II
// https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-ii/

impl Solution {
    pub fn maximum_length(s: String) -> i32 {
        let b = s.as_bytes();
        let n = b.len();
        let mut groups: [Vec<i32>; 26] = Default::default();
        let mut i = 0;
        while i < n {
            let mut j = i;
            while j < n && b[j] == b[i] {
                j += 1;
            }
            groups[(b[i] - b'a') as usize].push((j - i) as i32);
            i = j;
        }
        let mut ans = -1;
        for arr in groups.iter_mut() {
            if arr.is_empty() {
                continue;
            }
            arr.sort_unstable_by(|a, b| b.cmp(a));
            for l in (1..=arr[0]).rev() {
                let mut cnt = 0;
                for &g in arr.iter() {
                    if g >= l {
                        cnt += g - l + 1;
                    }
                }
                if cnt >= 3 {
                    if l > ans {
                        ans = l;
                    }
                    break;
                }
            }
        }
        ans
    }
}
'''

FILES["2983_palindrome_rearrangement_queries"] = r'''// LeetCode 2983 - Palindrome Rearrangement Queries
// https://leetcode.com/problems/palindrome-rearrangement-queries/

impl Solution {
    pub fn can_make_palindrome_queries(s: String, queries: Vec<Vec<i32>>) -> Vec<bool> {
        let n = s.len();
        let m = n / 2;
        let bytes = s.as_bytes();
        let mut t: Vec<u8> = bytes[m..].to_vec();
        t.reverse();
        let s = bytes[..m].to_vec();

        let mut pre1 = vec![vec![0i32; 26]; m + 1];
        let mut pre2 = vec![vec![0i32; 26]; m + 1];
        let mut diff = vec![0i32; m + 1];
        for i in 1..=m {
            pre1[i] = pre1[i - 1].clone();
            pre2[i] = pre2[i - 1].clone();
            pre1[i][(s[i - 1] - b'a') as usize] += 1;
            pre2[i][(t[i - 1] - b'a') as usize] += 1;
            diff[i] = diff[i - 1] + if s[i - 1] == t[i - 1] { 0 } else { 1 };
        }

        fn count(pre: &[Vec<i32>], i: usize, j: usize) -> Vec<i32> {
            let mut cnt = vec![0; 26];
            for k in 0..26 {
                cnt[k] = pre[j + 1][k] - pre[i][k];
            }
            cnt
        }
        fn sub(cnt1: &[i32], cnt2: &[i32]) -> Option<Vec<i32>> {
            let mut cnt = vec![0; 26];
            for i in 0..26 {
                cnt[i] = cnt1[i] - cnt2[i];
                if cnt[i] < 0 {
                    return None;
                }
            }
            Some(cnt)
        }
        fn check(
            pre1: &[Vec<i32>],
            pre2: &[Vec<i32>],
            diff: &[i32],
            a: usize,
            b: usize,
            c: usize,
            d: usize,
        ) -> bool {
            if diff[a] > 0 || diff[diff.len() - 1] - diff[(b.max(d) + 1).min(diff.len() - 1)] > 0 {
                return false;
            }
            if d <= b {
                return count(pre1, a, b) == count(pre2, a, b);
            }
            if b < c {
                return diff[c] - diff[b + 1] == 0
                    && count(pre1, a, b) == count(pre2, a, b)
                    && count(pre1, c, d) == count(pre2, c, d);
            }
            match (sub(&count(pre1, a, b), &count(pre2, a, c - 1)), sub(&count(pre2, c, d), &count(pre1, b + 1, d))) {
                (Some(c1), Some(c2)) => c1 == c2,
                _ => false,
            }
        }

        let mut ans = vec![false; queries.len()];
        for (i, q) in queries.iter().enumerate() {
            let a = q[0] as usize;
            let b = q[1] as usize;
            let c = n - 1 - q[3] as usize;
            let d = n - 1 - q[2] as usize;
            ans[i] = if a <= c {
                check(&pre1, &pre2, &diff, a, b, c, d)
            } else {
                check(&pre2, &pre1, &diff, c, d, a, b)
            };
        }
        ans
    }
}
'''

FILES["2992_number_of_self_divisible_permutations"] = r'''// LeetCode 2992 - Number of Self-Divisible Permutations
// https://leetcode.com/problems/number-of-self-divisible-permutations/

fn gcd(mut a: i32, mut b: i32) -> i32 {
    while b != 0 {
        let t = a % b;
        a = b;
        b = t;
    }
    a
}

impl Solution {
    pub fn self_divisible_permutation_count(n: i32) -> i32 {
        let mut ans = 0;
        let mut used = vec![false; (n + 1) as usize];
        fn dfs(pos: i32, n: i32, used: &mut [bool], ans: &mut i32) {
            if pos > n {
                *ans += 1;
                return;
            }
            for v in 1..=n {
                if used[v as usize] {
                    continue;
                }
                if gcd(v, pos) != 1 {
                    continue;
                }
                used[v as usize] = true;
                dfs(pos + 1, n, used, ans);
                used[v as usize] = false;
            }
        }
        dfs(1, n, &mut used, &mut ans);
        ans
    }
}
'''

FILES["2996_smallest_missing_integer_greater_than_sequential_prefix_sum"] = r'''// LeetCode 2996 - Smallest Missing Integer Greater Than Sequential Prefix Sum
// https://leetcode.com/problems/smallest-missing-integer-greater-than-sequential-prefix-sum/

use std::collections::HashSet;

impl Solution {
    pub fn missing_integer(nums: Vec<i32>) -> i32 {
        let mut sum = nums[0];
        let mut i = 1;
        while i < nums.len() && nums[i] == nums[i - 1] + 1 {
            sum += nums[i];
            i += 1;
        }
        let seen: HashSet<i32> = nums.into_iter().collect();
        while seen.contains(&sum) {
            sum += 1;
        }
        sum
    }
}
'''

FILES["2997_minimum_number_of_operations_to_make_array_xor_equal_to_k"] = r'''// LeetCode 2997 - Minimum Number of Operations to Make Array XOR Equal to K
// https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/

impl Solution {
    pub fn min_operations(nums: Vec<i32>, k: i32) -> i32 {
        let mut xorr = 0;
        for v in nums {
            xorr ^= v;
        }
        (xorr ^ k).count_ones() as i32
    }
}
'''

FILES["2998_minimum_number_of_operations_to_make_x_and_y_equal"] = r'''// LeetCode 2998 - Minimum Number of Operations to Make X and Y Equal
// https://leetcode.com/problems/minimum-number-of-operations-to-make-x-and-y-equal/

use std::collections::{HashSet, VecDeque};

impl Solution {
    pub fn minimum_operations_to_make_equal(x: i32, y: i32) -> i32 {
        if x <= y {
            return y - x;
        }
        let mut q = VecDeque::new();
        q.push_back((x, 0));
        let mut seen = HashSet::new();
        seen.insert(x);
        while let Some((v, d)) = q.pop_front() {
            if v == y {
                return d;
            }
            let mut cands = vec![v + 1, v - 1];
            if v % 11 == 0 {
                cands.push(v / 11);
            }
            if v % 5 == 0 {
                cands.push(v / 5);
            }
            for nxt in cands {
                if nxt > 0 && nxt < 2 * x + 20 && seen.insert(nxt) {
                    q.push_back((nxt, d + 1));
                }
            }
        }
        -1
    }
}
'''

FILES["2999_count_the_number_of_powerful_integers"] = r'''// LeetCode 2999 - Count the Number of Powerful Integers
// https://leetcode.com/problems/count-the-number-of-powerful-integers/

use std::collections::HashMap;

impl Solution {
    pub fn number_of_powerful_int(start: i64, finish: i64, limit: i32, s: String) -> i64 {
        fn count(num: i64, limit: i32, s: &str) -> i64 {
            if num < 0 {
                return 0;
            }
            for c in s.bytes() {
                if (c - b'0') as i32 > limit {
                    return 0;
                }
            }
            let t = num.to_string();
            let n = t.len();
            let sn = s.len();
            if n < sn {
                return 0;
            }
            let mut ans = 0i64;
            for length in sn..n {
                let pre_len = length - sn;
                if pre_len == 0 {
                    ans += 1;
                } else {
                    let mut ways = limit as i64;
                    for _ in 1..pre_len {
                        ways *= (limit + 1) as i64;
                    }
                    ans += ways;
                }
            }
            let pref = n - sn;
            let tb = t.as_bytes();
            fn dfs(
                i: usize,
                tight: bool,
                pref: usize,
                tb: &[u8],
                s: &str,
                limit: i32,
                memo: &mut HashMap<(usize, i32), i64>,
            ) -> i64 {
                if i == pref {
                    if tight {
                        return if &tb[pref..] >= s.as_bytes() { 1 } else { 0 };
                    }
                    return 1;
                }
                let key = (i, if tight { 1 } else { 0 });
                if let Some(&v) = memo.get(&key) {
                    return v;
                }
                let mut up = if tight { (tb[i] - b'0') as i32 } else { limit };
                if up > limit {
                    up = limit;
                }
                let mut res = 0i64;
                for d in 0..=up {
                    if i == 0 && d == 0 {
                        continue;
                    }
                    res += dfs(i + 1, tight && d == (tb[i] - b'0') as i32, pref, tb, s, limit, memo);
                }
                memo.insert(key, res);
                res
            }
            let mut memo = HashMap::new();
            ans += dfs(0, true, pref, tb, s, limit, &mut memo);
            ans
        }
        count(finish, limit, &s) - count(start - 1, limit, &s)
    }
}
'''

FILES["3000_maximum_area_of_longest_diagonal_rectangle"] = r'''// LeetCode 3000 - Maximum Area of Longest Diagonal Rectangle
// https://leetcode.com/problems/maximum-area-of-longest-diagonal-rectangle/

impl Solution {
    pub fn area_of_max_diagonal(dimensions: Vec<Vec<i32>>) -> i32 {
        let mut ans = 0;
        let mut mx = 0;
        for d in &dimensions {
            let l = d[0];
            let w = d[1];
            let t = l * l + w * w;
            if mx < t {
                mx = t;
                ans = l * w;
            } else if mx == t {
                ans = ans.max(l * w);
            }
        }
        ans
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

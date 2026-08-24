#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
FILES = {}

FILES["2935_maximum_strong_pair_xor_ii"] = r'''// LeetCode 2935 - Maximum Strong Pair XOR II
// https://leetcode.com/problems/maximum-strong-pair-xor-ii/

impl Solution {
    pub fn maximum_strong_pair_xor(mut nums: Vec<i32>) -> i32 {
        nums.sort_unstable();
        let mut ans = 0;
        for i in 0..nums.len() {
            let x = nums[i];
            let mut j = i;
            while j < nums.len() && nums[j] <= 2 * x {
                let xorr = x ^ nums[j];
                if xorr > ans {
                    ans = xorr;
                }
                j += 1;
            }
        }
        ans
    }
}
'''

FILES["2936_number_of_equal_numbers_blocks"] = r'''// LeetCode 2936 - Number of Equal Numbers Blocks
// https://leetcode.com/problems/number-of-equal-numbers-blocks/

impl Solution {
    pub fn block_count(nums: Vec<i32>) -> i32 {
        if nums.is_empty() {
            return 0;
        }
        let mut ans = 1;
        for i in 1..nums.len() {
            if nums[i] != nums[i - 1] {
                ans += 1;
            }
        }
        ans
    }
}
'''

FILES["2937_make_three_strings_equal"] = r'''// LeetCode 2937 - Make Three Strings Equal
// https://leetcode.com/problems/make-three-strings-equal/

impl Solution {
    pub fn find_minimum_operations(s1: String, s2: String, s3: String) -> i32 {
        let b1 = s1.as_bytes();
        let b2 = s2.as_bytes();
        let b3 = s3.as_bytes();
        let n = b1.len().min(b2.len()).min(b3.len());
        let mut i = 0;
        while i < n && b1[i] == b2[i] && b2[i] == b3[i] {
            i += 1;
        }
        if i == 0 {
            return -1;
        }
        (b1.len() + b2.len() + b3.len() - 3 * i) as i32
    }
}
'''

FILES["2938_separate_black_and_white_balls"] = r'''// LeetCode 2938 - Separate Black and White Balls
// https://leetcode.com/problems/separate-black-and-white-balls/

impl Solution {
    pub fn minimum_steps(s: String) -> i64 {
        let mut ans = 0i64;
        let mut zeros = 0i64;
        for &c in s.as_bytes().iter().rev() {
            if c == b'0' {
                zeros += 1;
            } else {
                ans += zeros;
            }
        }
        ans
    }
}
'''

FILES["2939_maximum_xor_product"] = r'''// LeetCode 2939 - Maximum Xor Product
// https://leetcode.com/problems/maximum-xor-product/

impl Solution {
    pub fn maximum_xor_product(mut a: i64, mut b: i64, n: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        for i in (0..n).rev() {
            let bit = 1i64 << i;
            let abit = a & bit;
            let bbit = b & bit;
            if abit == bbit {
                a |= bit;
                b |= bit;
            } else if a > b {
                b |= bit;
                a &= !bit;
            } else {
                a |= bit;
                b &= !bit;
            }
        }
        ((a % MOD) * (b % MOD) % MOD) as i32
    }
}
'''

FILES["2940_find_building_where_alice_and_bob_can_meet"] = r'''// LeetCode 2940 - Find Building Where Alice and Bob Can Meet
// https://leetcode.com/problems/find-building-where-alice-and-bob-can-meet/

impl Solution {
    pub fn leftmost_building_queries(heights: Vec<i32>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let qn = queries.len();
        let mut ans = vec![-1; qn];
        let mut buckets = vec![Vec::<(i32, usize)>::new(); heights.len()];
        for (qi, q) in queries.iter().enumerate() {
            let mut a = q[0] as usize;
            let mut b = q[1] as usize;
            if a > b {
                std::mem::swap(&mut a, &mut b);
            }
            if a == b || heights[a] < heights[b] {
                ans[qi] = b as i32;
                continue;
            }
            buckets[b].push((heights[a], qi));
        }
        let mut st: Vec<(i32, i32)> = Vec::new();
        for i in (0..heights.len()).rev() {
            for &(h, qi) in &buckets[i] {
                let mut lo = 0i32;
                let mut hi = st.len() as i32 - 1;
                let mut pos = -1;
                while lo <= hi {
                    let mid = (lo + hi) / 2;
                    if st[mid as usize].0 > h {
                        pos = st[mid as usize].1;
                        lo = mid + 1;
                    } else {
                        hi = mid - 1;
                    }
                }
                ans[qi] = pos;
            }
            while !st.is_empty() && st.last().unwrap().0 <= heights[i] {
                st.pop();
            }
            st.push((heights[i], i as i32));
        }
        ans
    }
}
'''

FILES["2941_maximum_gcd_sum_of_a_subarray"] = r'''// LeetCode 2941 - Maximum GCD-Sum of a Subarray
// https://leetcode.com/problems/maximum-gcd-sum-of-a-subarray/

fn gcd(mut a: i32, mut b: i32) -> i32 {
    while b != 0 {
        let t = a % b;
        a = b;
        b = t;
    }
    a
}

impl Solution {
    pub fn max_gcd_sum(nums: Vec<i32>, k: i32) -> i64 {
        let n = nums.len();
        let mut pref = vec![0i64; n + 1];
        for i in 0..n {
            pref[i + 1] = pref[i] + nums[i] as i64;
        }
        let mut ans = 0i64;
        let mut st: Vec<(i32, usize)> = Vec::new();
        for i in 0..n {
            let mut nst = vec![(nums[i], i)];
            for &(g0, idx) in &st {
                let g = gcd(g0, nums[i]);
                if nst.last().unwrap().0 == g {
                    continue;
                }
                nst.push((g, idx));
            }
            st = nst;
            for &(g, idx) in &st {
                if (i - idx + 1) as i32 >= k {
                    let cand = (pref[i + 1] - pref[idx]) * g as i64;
                    if cand > ans {
                        ans = cand;
                    }
                }
            }
        }
        ans
    }
}
'''

FILES["2942_find_words_containing_character"] = r'''// LeetCode 2942 - Find Words Containing Character
// https://leetcode.com/problems/find-words-containing-character/

impl Solution {
    pub fn find_words_containing(words: Vec<String>, x: char) -> Vec<i32> {
        let mut ans = Vec::new();
        for (i, w) in words.iter().enumerate() {
            if w.contains(x) {
                ans.push(i as i32);
            }
        }
        ans
    }
}
'''

FILES["2943_maximize_area_of_square_hole_in_grid"] = r'''// LeetCode 2943 - Maximize Area of Square Hole in Grid
// https://leetcode.com/problems/maximize-area-of-square-hole-in-grid/

impl Solution {
    pub fn maximize_square_hole_area(_n: i32, _m: i32, h_bars: Vec<i32>, v_bars: Vec<i32>) -> i32 {
        fn max_gap(mut bars: Vec<i32>) -> i32 {
            if bars.is_empty() {
                return 1;
            }
            bars.sort_unstable();
            let mut best = 1;
            let mut cur = 1;
            for i in 1..bars.len() {
                if bars[i] == bars[i - 1] + 1 {
                    cur += 1;
                } else {
                    cur = 1;
                }
                if cur > best {
                    best = cur;
                }
            }
            best + 1
        }
        let mut side = max_gap(h_bars);
        let vs = max_gap(v_bars);
        if vs < side {
            side = vs;
        }
        side * side
    }
}
'''

FILES["2944_minimum_number_of_coins_for_fruits"] = r'''// LeetCode 2944 - Minimum Number of Coins for Fruits
// https://leetcode.com/problems/minimum-number-of-coins-for-fruits/

impl Solution {
    pub fn minimum_coins(prices: Vec<i32>) -> i32 {
        let n = prices.len();
        let mut dp = vec![1 << 30; n + 1];
        dp[0] = 0;
        for i in 1..=n {
            let mut j = i;
            while j <= n && j <= i + i {
                let cand = dp[i - 1] + prices[i - 1];
                if cand < dp[j] {
                    dp[j] = cand;
                }
                j += 1;
            }
        }
        dp[n]
    }
}
'''

FILES["2945_find_maximum_non_decreasing_array_length"] = r'''// LeetCode 2945 - Find Maximum Non-decreasing Array Length
// https://leetcode.com/problems/find-maximum-non-decreasing-array-length/

use std::collections::VecDeque;

impl Solution {
    pub fn find_maximum_length(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut pref = vec![0i64; n + 1];
        let mut last = vec![0i64; n + 1];
        for i in 0..n {
            pref[i + 1] = pref[i] + nums[i] as i64;
        }
        let mut dp = vec![0; n + 1];
        let mut dq: VecDeque<(usize, i64)> = VecDeque::new();
        dq.push_back((0, 0));
        for i in 1..=n {
            while dq.len() > 1 && dq[1].1 <= pref[i] {
                dq.pop_front();
            }
            let j = dq[0].0;
            dp[i] = dp[j] + 1;
            last[i] = pref[i] - pref[j];
            let val = pref[i] + last[i];
            while !dq.is_empty() && dq.back().unwrap().1 >= val {
                dq.pop_back();
            }
            dq.push_back((i, val));
        }
        dp[n]
    }
}
'''

FILES["2946_matrix_similarity_after_cyclic_shifts"] = r'''// LeetCode 2946 - Matrix Similarity After Cyclic Shifts
// https://leetcode.com/problems/matrix-similarity-after-cyclic-shifts/

impl Solution {
    pub fn are_similar(mat: Vec<Vec<i32>>, k: i32) -> bool {
        let m = mat.len();
        let n = mat[0].len();
        for i in 0..m {
            let shift = if i % 2 == 0 {
                let mut s = n - (k as usize % n);
                if s == n {
                    s = 0;
                }
                s
            } else {
                k as usize % n
            };
            for j in 0..n {
                if mat[i][j] != mat[i][(j + shift) % n] {
                    return false;
                }
            }
        }
        true
    }
}
'''

FILES["2947_count_beautiful_substrings_i"] = r'''// LeetCode 2947 - Count Beautiful Substrings I
// https://leetcode.com/problems/count-beautiful-substrings-i/

impl Solution {
    pub fn beautiful_substrings(s: String, k: i32) -> i32 {
        fn is_vowel(c: u8) -> bool {
            matches!(c, b'a' | b'e' | b'i' | b'o' | b'u')
        }
        let s = s.as_bytes();
        let n = s.len();
        let mut ans = 0;
        for i in 0..n {
            let mut v = 0;
            let mut c = 0;
            for j in i..n {
                if is_vowel(s[j]) {
                    v += 1;
                } else {
                    c += 1;
                }
                if v == c && (v * c) % k == 0 {
                    ans += 1;
                }
            }
        }
        ans
    }
}
'''

FILES["2948_make_lexicographically_smallest_array_by_swapping_elements"] = r'''// LeetCode 2948 - Make Lexicographically Smallest Array by Swapping Elements
// https://leetcode.com/problems/make-lexicographically-smallest-array-by-swapping-elements/

impl Solution {
    pub fn lexicographically_smallest_array(nums: Vec<i32>, limit: i32) -> Vec<i32> {
        let n = nums.len();
        let mut idx: Vec<usize> = (0..n).collect();
        idx.sort_by_key(|&i| nums[i]);
        let mut ans = vec![0; n];
        let mut i = 0;
        while i < n {
            let mut j = i + 1;
            while j < n && nums[idx[j]] - nums[idx[j - 1]] <= limit {
                j += 1;
            }
            let mut group_idx = idx[i..j].to_vec();
            group_idx.sort_unstable();
            for t in 0..(j - i) {
                ans[group_idx[t]] = nums[idx[i + t]];
            }
            i = j;
        }
        ans
    }
}
'''

FILES["2949_count_beautiful_substrings_ii"] = r'''// LeetCode 2949 - Count Beautiful Substrings II
// https://leetcode.com/problems/count-beautiful-substrings-ii/

use std::collections::HashMap;

impl Solution {
    pub fn beautiful_substrings(s: String, k: i32) -> i64 {
        fn is_vowel(c: u8) -> bool {
            matches!(c, b'a' | b'e' | b'i' | b'o' | b'u')
        }
        let mut x = 1;
        while (x * x) % k != 0 {
            x += 1;
        }
        let mut freq: HashMap<(i32, i32), i64> = HashMap::new();
        freq.insert((0, 0), 1);
        let mut bal = 0i32;
        let mut vowels = 0i32;
        let mut ans = 0i64;
        for &ch in s.as_bytes() {
            if is_vowel(ch) {
                bal += 1;
                vowels += 1;
            } else {
                bal -= 1;
            }
            let kk = (bal, vowels % x);
            ans += *freq.get(&kk).unwrap_or(&0);
            *freq.entry(kk).or_insert(0) += 1;
        }
        ans
    }
}
'''

FILES["2950_number_of_divisible_substrings"] = r'''// LeetCode 2950 - Number of Divisible Substrings
// https://leetcode.com/problems/number-of-divisible-substrings/

impl Solution {
    pub fn count_divisible_substrings(word: String) -> i32 {
        let vals = [
            1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9,
        ];
        let word = word.as_bytes();
        let n = word.len();
        let mut ans = 0;
        for i in 0..n {
            let mut sum = 0;
            for j in i..n {
                sum += vals[(word[j] - b'a') as usize];
                if sum % (j - i + 1) as i32 == 0 {
                    ans += 1;
                }
            }
        }
        ans
    }
}
'''

FILES["2951_find_the_peaks"] = r'''// LeetCode 2951 - Find the Peaks
// https://leetcode.com/problems/find-the-peaks/

impl Solution {
    pub fn find_peaks(mountain: Vec<i32>) -> Vec<i32> {
        let mut ans = Vec::new();
        for i in 1..mountain.len().saturating_sub(1) {
            if mountain[i] > mountain[i - 1] && mountain[i] > mountain[i + 1] {
                ans.push(i as i32);
            }
        }
        ans
    }
}
'''

FILES["2952_minimum_number_of_coins_to_be_added"] = r'''// LeetCode 2952 - Minimum Number of Coins to be Added
// https://leetcode.com/problems/minimum-number-of-coins-to-be-added/

impl Solution {
    pub fn minimum_added_coins(mut coins: Vec<i32>, target: i32) -> i32 {
        coins.sort_unstable();
        let mut ans = 0;
        let mut reach = 0;
        let mut i = 0;
        while reach < target {
            if i < coins.len() && coins[i] <= reach + 1 {
                reach += coins[i];
                i += 1;
            } else {
                reach += reach + 1;
                ans += 1;
            }
        }
        ans
    }
}
'''

FILES["2953_count_complete_substrings"] = r'''// LeetCode 2953 - Count Complete Substrings
// https://leetcode.com/problems/count-complete-substrings/

impl Solution {
    pub fn count_complete_substrings(word: String, k: i32) -> i32 {
        let word = word.as_bytes();
        let n = word.len();
        let mut ans = 0;
        let mut i = 0;
        while i < n {
            let mut j = i;
            while j + 1 < n && (word[j + 1] as i32 - word[j] as i32).abs() <= 2 {
                j += 1;
            }
            let seg = &word[i..=j];
            let m = seg.len();
            for chars in 1..=26 {
                let length = chars * k as usize;
                if length > m {
                    break;
                }
                let mut freq = [0i32; 26];
                let mut unique = 0;
                for r in 0..m {
                    let c = (seg[r] - b'a') as usize;
                    freq[c] += 1;
                    if freq[c] == 1 {
                        unique += 1;
                    }
                    if r >= length {
                        let c2 = (seg[r - length] - b'a') as usize;
                        freq[c2] -= 1;
                        if freq[c2] == 0 {
                            unique -= 1;
                        }
                    }
                    if r >= length - 1 && unique == chars {
                        let ok = freq.iter().all(|&f| f == 0 || f == k);
                        if ok {
                            ans += 1;
                        }
                    }
                }
            }
            i = j + 1;
        }
        ans
    }
}
'''

FILES["2954_count_the_number_of_infection_sequences"] = r'''// LeetCode 2954 - Count the Number of Infection Sequences
// https://leetcode.com/problems/count-the-number-of-infection-sequences/

impl Solution {
    pub fn number_of_sequence(n: i32, sick: Vec<i32>) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let n = n as usize;
        let mut fact = vec![0i64; n + 1];
        let mut inv_fact = vec![0i64; n + 1];
        fact[0] = 1;
        for i in 1..=n {
            fact[i] = fact[i - 1] * i as i64 % MOD;
        }
        fn mod_pow(mut a: i64, mut b: i32) -> i64 {
            const MOD: i64 = 1_000_000_007;
            let mut res = 1i64;
            while b > 0 {
                if b & 1 == 1 {
                    res = res * a % MOD;
                }
                a = a * a % MOD;
                b >>= 1;
            }
            res
        }
        inv_fact[n] = mod_pow(fact[n], 1_000_000_005);
        for i in (1..=n).rev() {
            inv_fact[i - 1] = inv_fact[i] * i as i64 % MOD;
        }
        let m = sick.len();
        let total_empty = n - m;
        let mut ans = fact[total_empty];
        let mut prev = -1i32;
        for &s in &sick {
            let gap = (s - prev - 1) as usize;
            if prev == -1 {
                ans = ans * inv_fact[gap] % MOD;
            } else if gap > 0 {
                ans = ans * inv_fact[gap] % MOD * mod_pow(2, gap as i32 - 1) % MOD;
            }
            prev = s;
        }
        let gap = (n as i32 - prev - 1) as usize;
        ans = ans * inv_fact[gap] % MOD;
        ans as i32
    }
}
'''

FILES["2955_number_of_same_end_substrings"] = r'''// LeetCode 2955 - Number of Same-End Substrings
// https://leetcode.com/problems/number-of-same-end-substrings/

impl Solution {
    pub fn same_end_substring_count(s: String, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let s = s.as_bytes();
        let n = s.len();
        let mut pref = vec![[0i32; 26]; n + 1];
        for i in 0..n {
            pref[i + 1] = pref[i];
            pref[i + 1][(s[i] - b'a') as usize] += 1;
        }
        let mut ans = vec![0; queries.len()];
        for (qi, q) in queries.iter().enumerate() {
            let l = q[0] as usize;
            let r = q[1] as usize;
            let mut total = 0;
            for c in 0..26 {
                let cnt = pref[r + 1][c] - pref[l][c];
                total += cnt * (cnt + 1) / 2;
            }
            ans[qi] = total;
        }
        ans
    }
}
'''

FILES["2956_find_common_elements_between_two_arrays"] = r'''// LeetCode 2956 - Find Common Elements Between Two Arrays
// https://leetcode.com/problems/find-common-elements-between-two-arrays/

use std::collections::HashSet;

impl Solution {
    pub fn find_intersection_values(nums1: Vec<i32>, nums2: Vec<i32>) -> Vec<i32> {
        let s1: HashSet<i32> = nums1.iter().copied().collect();
        let s2: HashSet<i32> = nums2.iter().copied().collect();
        let a = nums1.iter().filter(|v| s2.contains(v)).count() as i32;
        let b = nums2.iter().filter(|v| s1.contains(v)).count() as i32;
        vec![a, b]
    }
}
'''

FILES["2957_remove_adjacent_almost_equal_characters"] = r'''// LeetCode 2957 - Remove Adjacent Almost-Equal Characters
// https://leetcode.com/problems/remove-adjacent-almost-equal-characters/

impl Solution {
    pub fn remove_almost_equal_characters(word: String) -> i32 {
        let w = word.as_bytes();
        let n = w.len();
        let mut ans = 0;
        let mut i = 1;
        while i < n {
            if (w[i] as i32 - w[i - 1] as i32).abs() <= 1 {
                ans += 1;
                i += 2;
            } else {
                i += 1;
            }
        }
        ans
    }
}
'''

FILES["2958_length_of_longest_subarray_with_at_most_k_frequency"] = r'''// LeetCode 2958 - Length of Longest Subarray With at Most K Frequency
// https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/

use std::collections::HashMap;

impl Solution {
    pub fn max_subarray_length(nums: Vec<i32>, k: i32) -> i32 {
        let mut freq: HashMap<i32, i32> = HashMap::new();
        let mut ans = 0;
        let mut left = 0;
        for right in 0..nums.len() {
            *freq.entry(nums[right]).or_insert(0) += 1;
            while *freq.get(&nums[right]).unwrap() > k {
                *freq.get_mut(&nums[left]).unwrap() -= 1;
                left += 1;
            }
            let len = (right - left + 1) as i32;
            if len > ans {
                ans = len;
            }
        }
        ans
    }
}
'''

FILES["2959_number_of_possible_sets_of_closing_branches"] = r'''// LeetCode 2959 - Number of Possible Sets of Closing Branches
// https://leetcode.com/problems/number-of-possible-sets-of-closing-branches/

impl Solution {
    pub fn number_of_sets(n: i32, max_distance: i32, roads: Vec<Vec<i32>>) -> i32 {
        let n = n as usize;
        let mut ans = 0;
        for mask in 0..(1 << n) {
            let mut dist = vec![vec![1 << 29; n]; n];
            for i in 0..n {
                dist[i][i] = 0;
            }
            for r in &roads {
                let u = r[0] as usize;
                let v = r[1] as usize;
                let w = r[2];
                if (mask & (1 << u)) != 0 && (mask & (1 << v)) != 0 && w < dist[u][v] {
                    dist[u][v] = w;
                    dist[v][u] = w;
                }
            }
            for k in 0..n {
                if (mask & (1 << k)) == 0 {
                    continue;
                }
                for i in 0..n {
                    if (mask & (1 << i)) == 0 {
                        continue;
                    }
                    for j in 0..n {
                        if (mask & (1 << j)) == 0 {
                            continue;
                        }
                        if dist[i][k] + dist[k][j] < dist[i][j] {
                            dist[i][j] = dist[i][k] + dist[k][j];
                        }
                    }
                }
            }
            let mut ok = true;
            for i in 0..n {
                if (mask & (1 << i)) == 0 {
                    continue;
                }
                for j in 0..n {
                    if (mask & (1 << j)) == 0 {
                        continue;
                    }
                    if dist[i][j] > max_distance {
                        ok = false;
                        break;
                    }
                }
                if !ok {
                    break;
                }
            }
            if ok {
                ans += 1;
            }
        }
        ans
    }
}
'''

FILES["2960_count_tested_devices_after_test_operations"] = r'''// LeetCode 2960 - Count Tested Devices After Test Operations
// https://leetcode.com/problems/count-tested-devices-after-test-operations/

impl Solution {
    pub fn count_tested_devices(battery_percentages: Vec<i32>) -> i32 {
        let mut ans = 0;
        for b in battery_percentages {
            if b > ans {
                ans += 1;
            }
        }
        ans
    }
}
'''

FILES["2961_double_modular_exponentiation"] = r'''// LeetCode 2961 - Double Modular Exponentiation
// https://leetcode.com/problems/double-modular-exponentiation/

impl Solution {
    pub fn get_good_indices(variables: Vec<Vec<i32>>, target: i32) -> Vec<i32> {
        fn mod_pow(mut a: i64, mut b: i64, m: i64) -> i64 {
            let mut res = 1 % m;
            a %= m;
            while b > 0 {
                if b & 1 == 1 {
                    res = res * a % m;
                }
                a = a * a % m;
                b >>= 1;
            }
            res
        }
        let mut ans = Vec::new();
        for (i, v) in variables.iter().enumerate() {
            let a = v[0] as i64;
            let b = v[1] as i64;
            let c = v[2] as i64;
            let m = v[3] as i64;
            if mod_pow(mod_pow(a, b, 10), c, m) == target as i64 {
                ans.push(i as i32);
            }
        }
        ans
    }
}
'''

FILES["2962_count_subarrays_where_max_element_appears_at_least_k_times"] = r'''// LeetCode 2962 - Count Subarrays Where Max Element Appears at Least K Times
// https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/

impl Solution {
    pub fn count_subarrays(nums: Vec<i32>, k: i32) -> i64 {
        let mx = *nums.iter().max().unwrap();
        let mut ans = 0i64;
        let mut cnt = 0;
        let mut left = 0;
        for right in 0..nums.len() {
            if nums[right] == mx {
                cnt += 1;
            }
            while cnt >= k {
                if nums[left] == mx {
                    cnt -= 1;
                }
                left += 1;
            }
            ans += left as i64;
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

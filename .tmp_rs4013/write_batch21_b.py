#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
FILES = {}

FILES["3845_maximum_subarray_xor_with_bounded_range"] = r'''// LeetCode 3845 - Maximum Subarray XOR with Bounded Range
// https://leetcode.com/problems/maximum-subarray-xor-with-bounded-range/

struct Node {
    next: [usize; 2],
    count: i32,
}

impl Solution {
    pub fn max_subarray_xor(nums: Vec<i32>, k: i32) -> i32 {
        let mut nodes = vec![Node { next: [0, 0], count: 0 }];
        fn add(nodes: &mut Vec<Node>, x: i32, delta: i32) {
            let mut u = 0;
            nodes[u].count += delta;
            for b in (0..16).rev() {
                let bit = ((x >> b) & 1) as usize;
                if nodes[u].next[bit] == 0 {
                    nodes[u].next[bit] = nodes.len();
                    nodes.push(Node { next: [0, 0], count: 0 });
                }
                u = nodes[u].next[bit];
                nodes[u].count += delta;
            }
        }
        fn query(nodes: &[Node], x: i32) -> i32 {
            let mut u = 0;
            let mut res = 0;
            for b in (0..16).rev() {
                let bit = ((x >> b) & 1) as usize;
                let want = bit ^ 1;
                let v = nodes[u].next[want];
                if v != 0 && nodes[v].count > 0 {
                    res |= 1 << b;
                    u = v;
                } else {
                    u = nodes[u].next[bit];
                }
            }
            res
        }
        let n = nums.len();
        let mut pref = vec![0; n + 1];
        for i in 0..n {
            pref[i + 1] = pref[i] ^ nums[i];
        }
        let mut max_q = Vec::new();
        let mut min_q = Vec::new();
        let mut left = 0;
        let mut trie_left = 0;
        let mut ans = 0;
        for r in 0..n {
            let x = nums[r];
            while max_q.last().map(|&i| nums[i] <= x).unwrap_or(false) {
                max_q.pop();
            }
            max_q.push(r);
            while min_q.last().map(|&i| nums[i] >= x).unwrap_or(false) {
                min_q.pop();
            }
            min_q.push(r);
            while nums[max_q[0]] - nums[min_q[0]] > k {
                if max_q[0] == left {
                    max_q.remove(0);
                }
                if min_q[0] == left {
                    min_q.remove(0);
                }
                left += 1;
            }
            add(&mut nodes, pref[r], 1);
            while trie_left < left {
                add(&mut nodes, pref[trie_left], -1);
                trie_left += 1;
            }
            let cur = query(&nodes, pref[r + 1]);
            if cur > ans {
                ans = cur;
            }
        }
        ans
    }
}
'''

FILES["3846_total_distance_to_type_a_string_using_one_finger"] = r'''// LeetCode 3846 - Total Distance to Type a String Using One Finger
// https://leetcode.com/problems/total-distance-to-type-a-string-using-one-finger/

use std::collections::HashMap;

impl Solution {
    pub fn total_distance(s: String) -> i32 {
        let keys = ["qwertyuiop", "asdfghjkl", "zxcvbnm"];
        let mut pos = HashMap::new();
        for (i, row) in keys.iter().enumerate() {
            for (j, c) in row.chars().enumerate() {
                pos.insert(c, (i as i32, j as i32));
            }
        }
        let mut pre = 'a';
        let mut ans = 0;
        for cur in s.chars() {
            let p1 = pos[&pre];
            let p2 = pos[&cur];
            ans += (p1.0 - p2.0).abs() + (p1.1 - p2.1).abs();
            pre = cur;
        }
        ans
    }
}
'''

FILES["3847_find_the_score_difference_in_a_game"] = r'''// LeetCode 3847 - Find the Score Difference in a Game
// https://leetcode.com/problems/find-the-score-difference-in-a-game/

impl Solution {
    pub fn score_difference(nums: Vec<i32>) -> i32 {
        let mut ans = 0;
        let mut k = 1;
        for (i, &x) in nums.iter().enumerate() {
            if x % 2 != 0 {
                k = -k;
            }
            if i % 6 == 5 {
                k = -k;
            }
            ans += k * x;
        }
        ans
    }
}
'''

FILES["3848_check_digitorial_permutation"] = r'''// LeetCode 3848 - Check Digitorial Permutation
// https://leetcode.com/problems/check-digitorial-permutation/

impl Solution {
    pub fn is_digitorial_permutation(n: i32) -> bool {
        let mut f = [0i32; 10];
        f[0] = 1;
        for i in 1..10 {
            f[i] = f[i - 1] * i as i32;
        }
        let mut x = 0;
        let mut y = n;
        while y > 0 {
            x += f[(y % 10) as usize];
            y /= 10;
        }
        let mut a: Vec<u8> = x.to_string().into_bytes();
        let mut b: Vec<u8> = n.to_string().into_bytes();
        a.sort_unstable();
        b.sort_unstable();
        a == b
    }
}
'''

FILES["3849_maximum_bitwise_xor_after_rearrangement"] = r'''// LeetCode 3849 - Maximum Bitwise XOR After Rearrangement
// https://leetcode.com/problems/maximum-bitwise-xor-after-rearrangement/

impl Solution {
    pub fn maximum_xor(s: String, t: String) -> String {
        let mut cnt = [0; 2];
        for c in t.bytes() {
            cnt[(c - b'0') as usize] += 1;
        }
        let sb = s.as_bytes();
        let mut ans = vec![b'0'; sb.len()];
        for i in 0..sb.len() {
            let x = (sb[i] - b'0') as usize;
            if cnt[x ^ 1] > 0 {
                cnt[x ^ 1] -= 1;
                ans[i] = b'1';
            } else {
                cnt[x] -= 1;
                ans[i] = b'0';
            }
        }
        String::from_utf8(ans).unwrap()
    }
}
'''

FILES["3850_count_sequences_to_k"] = r'''// LeetCode 3850 - Count Sequences to K
// https://leetcode.com/problems/count-sequences-to-k/

use std::collections::HashMap;

impl Solution {
    pub fn count_sequences(nums: Vec<i32>, k: i64) -> i32 {
        fn gcd(mut a: i64, mut b: i64) -> i64 {
            while b != 0 {
                let t = a % b;
                a = b;
                b = t;
            }
            a
        }
        fn dfs(
            i: usize,
            p: i64,
            q: i64,
            nums: &[i32],
            k: i64,
            memo: &mut HashMap<(usize, i64, i64), i32>,
        ) -> i32 {
            if i == nums.len() {
                return if p == k && q == 1 { 1 } else { 0 };
            }
            if let Some(&v) = memo.get(&(i, p, q)) {
                return v;
            }
            let mut res = dfs(i + 1, p, q, nums, k, memo);
            let x = nums[i] as i64;
            let g1 = gcd(p * x, q);
            res += dfs(i + 1, (p * x) / g1, q / g1, nums, k, memo);
            let g2 = gcd(p, q * x);
            res += dfs(i + 1, p / g2, (q * x) / g2, nums, k, memo);
            memo.insert((i, p, q), res);
            res
        }
        dfs(0, 1, 1, &nums, k, &mut HashMap::new())
    }
}
'''

FILES["3851_maximum_requests_without_violating_the_limit"] = r'''// LeetCode 3851 - Maximum Requests Without Violating the Limit
// https://leetcode.com/problems/maximum-requests-without-violating-the-limit/

use std::collections::HashMap;

impl Solution {
    pub fn max_requests(requests: Vec<Vec<i32>>, k: i32, window: i32) -> i32 {
        let mut g: HashMap<i32, Vec<i32>> = HashMap::new();
        for r in &requests {
            g.entry(r[0]).or_default().push(r[1]);
        }
        let mut ans = requests.len() as i32;
        for ts in g.values_mut() {
            ts.sort_unstable();
            let mut kept = Vec::new();
            for &t in ts.iter() {
                while !kept.is_empty() && t - kept[0] > window {
                    kept.remove(0);
                }
                if (kept.len() as i32) < k {
                    kept.push(t);
                } else {
                    ans -= 1;
                }
            }
        }
        ans
    }
}
'''

FILES["3852_smallest_pair_with_different_frequencies"] = r'''// LeetCode 3852 - Smallest Pair With Different Frequencies
// https://leetcode.com/problems/smallest-pair-with-different-frequencies/

use std::collections::HashMap;

impl Solution {
    pub fn min_distinct_freq_pair(nums: Vec<i32>) -> Vec<i32> {
        let mut cnt = HashMap::new();
        for &v in &nums {
            *cnt.entry(v).or_insert(0) += 1;
        }
        let x = *nums.iter().min().unwrap();
        let mut min_y = i32::MAX;
        for (&y, _) in &cnt {
            if y < min_y && cnt[&x] != cnt[&y] {
                min_y = y;
            }
        }
        if min_y == i32::MAX {
            return vec![-1, -1];
        }
        vec![x, min_y]
    }
}
'''

FILES["3853_merge_close_characters"] = r'''// LeetCode 3853 - Merge Close Characters
// https://leetcode.com/problems/merge-close-characters/

use std::collections::HashMap;

impl Solution {
    pub fn merge_characters(s: String, k: i32) -> String {
        let mut last = HashMap::new();
        let mut ans = String::new();
        for c in s.chars() {
            let cur = ans.len() as i32;
            if let Some(&prev) = last.get(&c) {
                if cur - prev <= k {
                    continue;
                }
            }
            ans.push(c);
            last.insert(c, cur);
        }
        ans
    }
}
'''

FILES["3854_minimum_operations_to_make_array_parity_alternating"] = r'''// LeetCode 3854 - Minimum Operations to Make Array Parity Alternating
// https://leetcode.com/problems/minimum-operations-to-make-array-parity-alternating/

impl Solution {
    pub fn make_parity_alternating(nums: Vec<i32>) -> Vec<i32> {
        if nums.len() == 1 {
            return vec![0, 0];
        }
        let mn = *nums.iter().min().unwrap();
        let mx = *nums.iter().max().unwrap();
        let f = |k: i32| {
            let mut cnt = 0;
            let mut a = i32::MAX;
            let mut b = i32::MIN;
            for (i, &orig) in nums.iter().enumerate() {
                let mut x = orig;
                if ((x - i as i32) & 1) != k {
                    cnt += 1;
                    if x == mn {
                        x += 1;
                    } else if x == mx {
                        x -= 1;
                    }
                }
                a = a.min(x);
                b = b.max(x);
            }
            vec![cnt, 1.max(b - a)]
        };
        let r0 = f(0);
        let r1 = f(1);
        if r0[0] != r1[0] {
            if r0[0] < r1[0] {
                r0
            } else {
                r1
            }
        } else if r0[1] <= r1[1] {
            r0
        } else {
            r1
        }
    }
}
'''

FILES["3855_sum_of_k_digit_numbers_in_a_range"] = r'''// LeetCode 3855 - Sum of K Digit Numbers in a Range
// https://leetcode.com/problems/sum-of-k-digit-numbers-in-a-range/

impl Solution {
    pub fn sum_of_numbers(l: i32, r: i32, k: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        fn qpow(mut a: i64, mut n: i64, m: i64) -> i64 {
            a %= m;
            let mut ans = 1;
            while n > 0 {
                if n & 1 == 1 {
                    ans = ans * a % m;
                }
                a = a * a % m;
                n >>= 1;
            }
            ans
        }
        let n = (r - l + 1) as i64;
        let sum = (l as i64 + r as i64) * n / 2 % MOD;
        let part1 = qpow(n % MOD, (k - 1) as i64, MOD);
        let part2 = (qpow(10, k as i64, MOD) - 1 + MOD) % MOD;
        let inv9 = qpow(9, MOD - 2, MOD);
        let mut ans = sum;
        ans = ans * part1 % MOD;
        ans = ans * part2 % MOD;
        ans = ans * inv9 % MOD;
        ans as i32
    }
}
'''

FILES["3856_trim_trailing_vowels"] = r'''// LeetCode 3856 - Trim Trailing Vowels
// https://leetcode.com/problems/trim-trailing-vowels/

impl Solution {
    pub fn trim_trailing_vowels(s: String) -> String {
        let bytes = s.as_bytes();
        let mut i = bytes.len() as i32 - 1;
        let is_vowel = |c: u8| matches!(c, b'a' | b'e' | b'i' | b'o' | b'u');
        while i >= 0 && is_vowel(bytes[i as usize]) {
            i -= 1;
        }
        s[..(i + 1) as usize].to_string()
    }
}
'''

FILES["3857_minimum_cost_to_split_into_ones"] = r'''// LeetCode 3857 - Minimum Cost to Split Into Ones
// https://leetcode.com/problems/minimum-cost-to-split-into-ones/

impl Solution {
    pub fn min_cost(n: i32) -> i32 {
        n * (n - 1) / 2
    }
}
'''

FILES["3858_minimum_bitwise_or_from_grid"] = r'''// LeetCode 3858 - Minimum Bitwise OR From Grid
// https://leetcode.com/problems/minimum-bitwise-or-from-grid/

impl Solution {
    pub fn minimum_or(grid: Vec<Vec<i32>>) -> i32 {
        let mx = grid.iter().flat_map(|row| row.iter()).copied().max().unwrap_or(0);
        let m = if mx == 0 { 0 } else { 32 - (mx as u32).leading_zeros() as i32 };
        let mut ans = 0;
        for i in (0..m).rev() {
            let mask = ans | ((1 << i) - 1);
            let mut found_all = true;
            for row in &grid {
                let found = row.iter().any(|&x| (x | mask) == mask);
                if !found {
                    ans |= 1 << i;
                    found_all = false;
                    break;
                }
            }
            let _ = found_all;
        }
        ans
    }
}
'''

FILES["3859_count_subarrays_with_k_distinct_integers"] = r'''// LeetCode 3859 - Count Subarrays With K Distinct Integers
// https://leetcode.com/problems/count-subarrays-with-k-distinct-integers/

use std::collections::HashMap;

impl Solution {
    pub fn count_subarrays(nums: Vec<i32>, k: i32, m: i32) -> i64 {
        let f = |lim: i32| {
            let mut cnt = HashMap::new();
            let mut ans = 0i64;
            let mut l = 0usize;
            let mut t = 0;
            for &x in &nums {
                let e = cnt.entry(x).or_insert(0);
                *e += 1;
                if *e == m {
                    t += 1;
                }
                while cnt.len() as i32 >= lim && t >= k {
                    let y = nums[l];
                    l += 1;
                    let e = cnt.get_mut(&y).unwrap();
                    *e -= 1;
                    if *e == m - 1 {
                        t -= 1;
                    }
                    if *e == 0 {
                        cnt.remove(&y);
                    }
                }
                ans += l as i64;
            }
            ans
        };
        f(k) - f(k + 1)
    }
}
'''

FILES["3860_unique_email_groups"] = r'''// LeetCode 3860 - Unique Email Groups
// https://leetcode.com/problems/unique-email-groups/

use std::collections::HashSet;

impl Solution {
    pub fn unique_email_groups(emails: Vec<String>) -> i32 {
        let mut st = HashSet::new();
        for email in emails {
            let at = email.find('@').unwrap();
            let mut local = email[..at].to_string();
            let domain = email[at + 1..].to_ascii_lowercase();
            if let Some(plus) = local.find('+') {
                local.truncate(plus);
            }
            let cleaned: String = local
                .chars()
                .filter(|&c| c != '.')
                .map(|c| c.to_ascii_lowercase())
                .collect();
            st.insert(cleaned + &domain);
        }
        st.len() as i32
    }
}
'''

FILES["3861_minimum_capacity_box"] = r'''// LeetCode 3861 - Minimum Capacity Box
// https://leetcode.com/problems/minimum-capacity-box/

impl Solution {
    pub fn minimum_index(capacity: Vec<i32>, item_size: i32) -> i32 {
        let mut ans = -1;
        for (i, &c) in capacity.iter().enumerate() {
            if c >= item_size && (ans == -1 || c < capacity[ans as usize]) {
                ans = i as i32;
            }
        }
        ans
    }
}
'''

FILES["3862_find_the_smallest_balanced_index"] = r'''// LeetCode 3862 - Find the Smallest Balanced Index
// https://leetcode.com/problems/find-the-smallest-balanced-index/

impl Solution {
    pub fn smallest_balanced_index(nums: Vec<i32>) -> i32 {
        let mut s: i64 = nums.iter().map(|&x| x as i64).sum();
        let mut p = 1i64;
        for i in (0..nums.len()).rev() {
            s -= nums[i] as i64;
            if s == p {
                return i as i32;
            }
            p *= nums[i] as i64;
            if p >= s {
                break;
            }
        }
        -1
    }
}
'''

FILES["3863_minimum_operations_to_sort_a_string"] = r'''// LeetCode 3863 - Minimum Operations to Sort a String
// https://leetcode.com/problems/minimum-operations-to-sort-a-string/

impl Solution {
    pub fn min_operations(s: String) -> i32 {
        let b = s.as_bytes();
        let n = b.len();
        let sorted = b.windows(2).all(|w| w[1] >= w[0]);
        if sorted {
            return 0;
        }
        if n == 2 {
            return -1;
        }
        let mn = *b.iter().min().unwrap();
        let mx = *b.iter().max().unwrap();
        if b[0] == mn || b[n - 1] == mx {
            return 1;
        }
        for i in 1..n - 1 {
            if b[i] == mn || b[i] == mx {
                return 2;
            }
        }
        3
    }
}
'''

FILES["3864_minimum_cost_to_partition_a_binary_string"] = r'''// LeetCode 3864 - Minimum Cost to Partition a Binary String
// https://leetcode.com/problems/minimum-cost-to-partition-a-binary-string/

impl Solution {
    pub fn min_cost(s: String, enc_cost: i32, flat_cost: i32) -> i64 {
        let n = s.len();
        let b = s.as_bytes();
        let mut pre = vec![0; n + 1];
        for i in 1..=n {
            pre[i] = pre[i - 1] + (b[i - 1] - b'0') as i32;
        }
        fn dfs(l: usize, r: usize, pre: &[i32], enc_cost: i32, flat_cost: i32) -> i64 {
            let x = pre[r] - pre[l];
            let mut res = if x != 0 {
                (r - l) as i64 * x as i64 * enc_cost as i64
            } else {
                flat_cost as i64
            };
            if (r - l) % 2 == 0 {
                let m = (l + r) / 2;
                res = res.min(dfs(l, m, pre, enc_cost, flat_cost) + dfs(m, r, pre, enc_cost, flat_cost));
            }
            res
        }
        dfs(0, n, &pre, enc_cost, flat_cost)
    }
}
'''

FILES["3865_reverse_k_subarrays"] = r'''// LeetCode 3865 - Reverse K Subarrays
// https://leetcode.com/problems/reverse-k-subarrays/

impl Solution {
    pub fn reverse_subarrays(mut nums: Vec<i32>, k: i32) -> Vec<i32> {
        let n = nums.len();
        let m = n / k as usize;
        let mut i = 0;
        while i < n {
            nums[i..i + m].reverse();
            i += m;
        }
        nums
    }
}
'''

FILES["3866_first_unique_even_element"] = r'''// LeetCode 3866 - First Unique Even Element
// https://leetcode.com/problems/first-unique-even-element/

impl Solution {
    pub fn first_unique_even(nums: Vec<i32>) -> i32 {
        let mut cnt = [0; 101];
        for &x in &nums {
            cnt[x as usize] += 1;
        }
        for x in nums {
            if x % 2 == 0 && cnt[x as usize] == 1 {
                return x;
            }
        }
        -1
    }
}
'''

FILES["3867_sum_of_gcd_of_formed_pairs"] = r'''// LeetCode 3867 - Sum of GCD of Formed Pairs
// https://leetcode.com/problems/sum-of-gcd-of-formed-pairs/

impl Solution {
    pub fn gcd_sum(nums: Vec<i32>) -> i64 {
        fn gcd(mut a: i32, mut b: i32) -> i32 {
            while b != 0 {
                let t = a % b;
                a = b;
                b = t;
            }
            a
        }
        let n = nums.len();
        let mut prefix_gcd = vec![0; n];
        let mut mx = 0;
        for i in 0..n {
            mx = mx.max(nums[i]);
            prefix_gcd[i] = gcd(nums[i], mx);
        }
        prefix_gcd.sort_unstable();
        let mut ans = 0i64;
        for i in 0..n / 2 {
            ans += gcd(prefix_gcd[i], prefix_gcd[n - i - 1]) as i64;
        }
        ans
    }
}
'''

FILES["3868_minimum_cost_to_equalize_arrays_using_swaps"] = r'''// LeetCode 3868 - Minimum Cost to Equalize Arrays Using Swaps
// https://leetcode.com/problems/minimum-cost-to-equalize-arrays-using-swaps/

use std::collections::HashMap;

impl Solution {
    pub fn min_cost(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        let mut cnt2 = HashMap::new();
        for x in nums2 {
            *cnt2.entry(x).or_insert(0) += 1;
        }
        let mut cnt1 = HashMap::new();
        for x in nums1 {
            if let Some(v) = cnt2.get_mut(&x) {
                if *v > 0 {
                    *v -= 1;
                    continue;
                }
            }
            *cnt1.entry(x).or_insert(0) += 1;
        }
        let mut ans = 0;
        for &v in cnt1.values() {
            if v % 2 == 1 {
                return -1;
            }
            ans += v / 2;
        }
        for &v in cnt2.values() {
            if v % 2 == 1 {
                return -1;
            }
        }
        ans
    }
}
'''

FILES["3869_count_fancy_numbers_in_a_range"] = r'''// LeetCode 3869 - Count Fancy Numbers in a Range
// https://leetcode.com/problems/count-fancy-numbers-in-a-range/

impl Solution {
    pub fn count_fancy(l: i64, r: i64) -> i64 {
        fn check(s: i32) -> bool {
            if s < 100 {
                return s % 11 != 0;
            }
            let mid = (s / 10) % 10;
            let last = s % 10;
            mid > 1 && mid < last
        }
        fn calc(x: i64) -> i64 {
            let num: Vec<u8> = x.to_string().into_bytes();
            let n = num.len();
            let mut f = vec![vec![vec![vec![-1i64; 4]; 10]; 9 * n + 1]; n];
            fn dfs(
                pos: usize,
                s: usize,
                prev: usize,
                st: usize,
                lim: bool,
                num: &[u8],
                f: &mut [Vec<Vec<Vec<i64>>>],
            ) -> i64 {
                if pos >= num.len() {
                    return if st != 3 {
                        1
                    } else if check(s as i32) {
                        1
                    } else {
                        0
                    };
                }
                if !lim && f[pos][s][prev][st] != -1 {
                    return f[pos][s][prev][st];
                }
                let up = if lim { (num[pos] - b'0') as usize } else { 9 };
                let mut res = 0i64;
                for i in 0..=up {
                    let nxt_st = if st == 0 {
                        if prev == 0 {
                            0
                        } else if i > prev {
                            1
                        } else if i < prev {
                            2
                        } else {
                            3
                        }
                    } else if st == 1 {
                        if i > prev { 1 } else { 3 }
                    } else if st == 2 {
                        if i < prev { 2 } else { 3 }
                    } else {
                        3
                    };
                    res += dfs(pos + 1, s + i, i, nxt_st, lim && i == up, num, f);
                }
                if !lim {
                    f[pos][s][prev][st] = res;
                }
                res
            }
            dfs(0, 0, 0, 0, true, &num, &mut f)
        }
        calc(r) - calc(l - 1)
    }
}
'''

FILES["3870_count_commas_in_range"] = r'''// LeetCode 3870 - Count Commas in Range
// https://leetcode.com/problems/count-commas-in-range/

impl Solution {
    pub fn count_commas(n: i32) -> i32 {
        0.max(n - 999)
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

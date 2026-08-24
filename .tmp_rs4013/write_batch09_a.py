#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
FILES = {}

FILES["2518_number_of_great_partitions"] = r'''// LeetCode 2518 - Number of Great Partitions
// https://leetcode.com/problems/number-of-great-partitions/

impl Solution {
    pub fn count_partitions(nums: Vec<i32>, k: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let k = k as usize;
        let sum: i64 = nums.iter().map(|&x| x as i64).sum();
        if sum < 2 * k as i64 {
            return 0;
        }
        let mut dp = vec![0i64; k];
        dp[0] = 1;
        for &x in &nums {
            let x = x as usize;
            for s in (x..k).rev() {
                dp[s] = (dp[s] + dp[s - x]) % MOD;
            }
        }
        let bad: i64 = dp.iter().sum::<i64>() % MOD;
        let mut total = 1i64;
        for _ in 0..nums.len() {
            total = total * 2 % MOD;
        }
        ((total - 2 * bad % MOD + MOD) % MOD) as i32
    }
}
'''

FILES["2519_count_the_number_of_k_big_indices"] = r'''// LeetCode 2519 - Count the Number of K-Big Indices
// https://leetcode.com/problems/count-the-number-of-k-big-indices/

use std::collections::HashMap;

struct Fenwick {
    bit: Vec<i32>,
}

impl Fenwick {
    fn new(n: usize) -> Self {
        Self { bit: vec![0; n + 2] }
    }
    fn add(&mut self, mut i: usize, v: i32) {
        while i < self.bit.len() {
            self.bit[i] += v;
            i += i & i.wrapping_neg();
        }
    }
    fn sum(&self, mut i: usize) -> i32 {
        let mut s = 0;
        while i > 0 {
            s += self.bit[i];
            i -= i & i.wrapping_neg();
        }
        s
    }
}

impl Solution {
    pub fn k_big_indices(nums: Vec<i32>, k: i32) -> i32 {
        let n = nums.len();
        let mut uniq = nums.clone();
        uniq.sort_unstable();
        uniq.dedup();
        let mut rank = HashMap::new();
        for (i, &v) in uniq.iter().enumerate() {
            rank.insert(v, i + 1);
        }
        let m = uniq.len();
        let mut left = vec![0; n];
        let mut right = vec![0; n];
        let mut ft = Fenwick::new(m);
        for i in 0..n {
            let r = rank[&nums[i]];
            left[i] = ft.sum(r - 1);
            ft.add(r, 1);
        }
        let mut ft = Fenwick::new(m);
        for i in (0..n).rev() {
            let r = rank[&nums[i]];
            right[i] = ft.sum(r - 1);
            ft.add(r, 1);
        }
        let mut ans = 0;
        for i in 0..n {
            if left[i] >= k && right[i] >= k {
                ans += 1;
            }
        }
        ans
    }
}
'''

FILES["2520_count_the_digits_that_divide_a_number"] = r'''// LeetCode 2520 - Count the Digits That Divide a Number
// https://leetcode.com/problems/count-the-digits-that-divide-a-number/

impl Solution {
    pub fn count_digits(num: i32) -> i32 {
        let mut ans = 0;
        let mut x = num;
        while x > 0 {
            let d = x % 10;
            if d != 0 && num % d == 0 {
                ans += 1;
            }
            x /= 10;
        }
        ans
    }
}
'''

FILES["2521_distinct_prime_factors_of_product_of_array"] = r'''// LeetCode 2521 - Distinct Prime Factors of Product of Array
// https://leetcode.com/problems/distinct-prime-factors-of-product-of-array/

use std::collections::HashSet;

impl Solution {
    pub fn distinct_prime_factors(nums: Vec<i32>) -> i32 {
        let mut set = HashSet::new();
        for mut x in nums {
            let mut p = 2;
            while p * p <= x {
                if x % p == 0 {
                    set.insert(p);
                    while x % p == 0 {
                        x /= p;
                    }
                }
                p += 1;
            }
            if x > 1 {
                set.insert(x);
            }
        }
        set.len() as i32
    }
}
'''

FILES["2522_partition_string_into_substrings_with_values_at_most_k"] = r'''// LeetCode 2522 - Partition String Into Substrings With Values At Most K
// https://leetcode.com/problems/partition-string-into-substrings-with-values-at-most-k/

impl Solution {
    pub fn minimum_partition(s: String, k: i32) -> i32 {
        let k = k as i64;
        let mut ans = 1;
        let mut cur = 0i64;
        for ch in s.bytes() {
            let d = (ch - b'0') as i64;
            if d > k {
                return -1;
            }
            let nxt = cur * 10 + d;
            if nxt > k {
                ans += 1;
                cur = d;
            } else {
                cur = nxt;
            }
        }
        ans
    }
}
'''

FILES["2523_closest_prime_numbers_in_range"] = r'''// LeetCode 2523 - Closest Prime Numbers in Range
// https://leetcode.com/problems/closest-prime-numbers-in-range/

impl Solution {
    pub fn closest_primes(left: i32, right: i32) -> Vec<i32> {
        let right = right as usize;
        let left = left as usize;
        let mut is_prime = vec![true; right + 1];
        if right >= 0 {
            is_prime[0] = false;
        }
        if right >= 1 {
            is_prime[1] = false;
        }
        let mut i = 2;
        while i * i <= right {
            if is_prime[i] {
                let mut j = i * i;
                while j <= right {
                    is_prime[j] = false;
                    j += i;
                }
            }
            i += 1;
        }
        let primes: Vec<i32> = (left..=right)
            .filter(|&i| is_prime[i])
            .map(|i| i as i32)
            .collect();
        if primes.len() < 2 {
            return vec![-1, -1];
        }
        let mut best = vec![primes[0], primes[1]];
        let mut diff = primes[1] - primes[0];
        for i in 1..primes.len() - 1 {
            let d = primes[i + 1] - primes[i];
            if d < diff {
                diff = d;
                best = vec![primes[i], primes[i + 1]];
            }
        }
        best
    }
}
'''

FILES["2524_maximum_frequency_score_of_a_subarray"] = r'''// LeetCode 2524 - Maximum Frequency Score of a Subarray
// https://leetcode.com/problems/maximum-frequency-score-of-a-subarray/

use std::collections::HashMap;

impl Solution {
    pub fn max_frequency_score(nums: Vec<i32>, k: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        fn mod_pow(mut a: i64, mut e: i64) -> i64 {
            let mut res = 1i64;
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
        let k = k as usize;
        let mut freq: HashMap<i32, i32> = HashMap::new();
        let mut score = 0i64;
        let mut add = |freq: &mut HashMap<i32, i32>, score: &mut i64, x: i32| {
            let c = *freq.get(&x).unwrap_or(&0);
            if c > 0 {
                *score = (*score - mod_pow(x as i64, c as i64) + MOD) % MOD;
            }
            freq.insert(x, c + 1);
            *score = (*score + mod_pow(x as i64, (c + 1) as i64)) % MOD;
        };
        let mut remove = |freq: &mut HashMap<i32, i32>, score: &mut i64, x: i32| {
            let c = freq[&x];
            *score = (*score - mod_pow(x as i64, c as i64) + MOD) % MOD;
            if c == 1 {
                freq.remove(&x);
            } else {
                freq.insert(x, c - 1);
                *score = (*score + mod_pow(x as i64, (c - 1) as i64)) % MOD;
            }
        };
        let mut best = 0i64;
        for i in 0..nums.len() {
            add(&mut freq, &mut score, nums[i]);
            if i >= k {
                remove(&mut freq, &mut score, nums[i - k]);
            }
            if i + 1 >= k && score > best {
                best = score;
            }
        }
        best as i32
    }
}
'''

FILES["2525_categorize_box_according_to_criteria"] = r'''// LeetCode 2525 - Categorize Box According to Criteria
// https://leetcode.com/problems/categorize-box-according-to-criteria/

impl Solution {
    pub fn categorize_box(length: i32, width: i32, height: i32, mass: i32) -> String {
        let bulky = length >= 10000
            || width >= 10000
            || height >= 10000
            || (length as i64) * (width as i64) * (height as i64) >= 1_000_000_000;
        let heavy = mass >= 100;
        if bulky && heavy {
            "Both".to_string()
        } else if bulky {
            "Bulky".to_string()
        } else if heavy {
            "Heavy".to_string()
        } else {
            "Neither".to_string()
        }
    }
}
'''

FILES["2526_find_consecutive_integers_from_a_data_stream"] = r'''// LeetCode 2526 - Find Consecutive Integers from a Data Stream
// https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/

pub struct DataStream {
    value: i32,
    k: i32,
    streak: i32,
}

impl DataStream {
    pub fn new(value: i32, k: i32) -> Self {
        Self {
            value,
            k,
            streak: 0,
        }
    }

    pub fn consec(&mut self, num: i32) -> bool {
        if num == self.value {
            self.streak += 1;
        } else {
            self.streak = 0;
        }
        self.streak >= self.k
    }
}
'''

FILES["2527_find_xor_beauty_of_array"] = r'''// LeetCode 2527 - Find Xor-Beauty of Array
// https://leetcode.com/problems/find-xor-beauty-of-array/

impl Solution {
    pub fn xor_beauty(nums: Vec<i32>) -> i32 {
        let mut ans = 0;
        for x in nums {
            ans ^= x;
        }
        ans
    }
}
'''

FILES["2528_maximize_the_minimum_powered_city"] = r'''// LeetCode 2528 - Maximize the Minimum Powered City
// https://leetcode.com/problems/maximize-the-minimum-powered-city/

impl Solution {
    pub fn max_power(stations: Vec<i32>, r: i32, k: i32) -> i64 {
        let n = stations.len();
        let r = r as usize;
        let k = k as i64;
        let mut diff = vec![0i64; n + 1];
        for i in 0..n {
            let l = i.saturating_sub(r);
            let rr = (i + r).min(n - 1);
            diff[l] += stations[i] as i64;
            diff[rr + 1] -= stations[i] as i64;
        }
        let mut power = vec![0i64; n];
        let mut cur = 0i64;
        for i in 0..n {
            cur += diff[i];
            power[i] = cur;
        }
        let ok = |x: i64| -> bool {
            let mut extra = vec![0i64; n + 1];
            let mut have = 0i64;
            let mut used = 0i64;
            for i in 0..n {
                have += extra[i];
                let need = x - (power[i] + have);
                if need > 0 {
                    used += need;
                    if used > k {
                        return false;
                    }
                    have += need;
                    let end = i + 2 * r;
                    if end + 1 <= n {
                        extra[end + 1] -= need;
                    }
                }
            }
            true
        };
        let mut lo = 0i64;
        let mut hi = k;
        for &p in &power {
            if p > hi {
                hi = p;
            }
        }
        hi += k;
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

FILES["2529_maximum_count_of_positive_integer_and_negative_integer"] = r'''// LeetCode 2529 - Maximum Count of Positive Integer and Negative Integer
// https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/

impl Solution {
    pub fn maximum_count(nums: Vec<i32>) -> i32 {
        let mut pos = 0;
        let mut neg = 0;
        for x in nums {
            if x > 0 {
                pos += 1;
            } else if x < 0 {
                neg += 1;
            }
        }
        pos.max(neg)
    }
}
'''

FILES["2530_maximal_score_after_applying_k_operations"] = r'''// LeetCode 2530 - Maximal Score After Applying K Operations
// https://leetcode.com/problems/maximal-score-after-applying-k-operations/

use std::collections::BinaryHeap;

impl Solution {
    pub fn max_kelements(nums: Vec<i32>, k: i32) -> i64 {
        let mut pq = BinaryHeap::from(nums);
        let mut ans = 0i64;
        for _ in 0..k {
            let x = pq.pop().unwrap();
            ans += x as i64;
            pq.push((x + 2) / 3);
        }
        ans
    }
}
'''

FILES["2531_make_number_of_distinct_characters_equal"] = r'''// LeetCode 2531 - Make Number of Distinct Characters Equal
// https://leetcode.com/problems/make-number-of-distinct-characters-equal/

impl Solution {
    pub fn is_it_possible(word1: String, word2: String) -> bool {
        let mut c1 = [0i32; 26];
        let mut c2 = [0i32; 26];
        for c in word1.bytes() {
            c1[(c - b'a') as usize] += 1;
        }
        for c in word2.bytes() {
            c2[(c - b'a') as usize] += 1;
        }
        let mut d1 = 0;
        let mut d2 = 0;
        for i in 0..26 {
            if c1[i] > 0 {
                d1 += 1;
            }
            if c2[i] > 0 {
                d2 += 1;
            }
        }
        for a in 0..26 {
            if c1[a] == 0 {
                continue;
            }
            for b in 0..26 {
                if c2[b] == 0 {
                    continue;
                }
                let mut nd1 = d1;
                let mut nd2 = d2;
                if a == b {
                    if nd1 == nd2 {
                        return true;
                    }
                    continue;
                }
                if c1[a] == 1 {
                    nd1 -= 1;
                }
                if c1[b] == 0 {
                    nd1 += 1;
                }
                if c2[b] == 1 {
                    nd2 -= 1;
                }
                if c2[a] == 0 {
                    nd2 += 1;
                }
                if nd1 == nd2 {
                    return true;
                }
            }
        }
        false
    }
}
'''

FILES["2532_time_to_cross_a_bridge"] = r'''// LeetCode 2532 - Time to Cross a Bridge
// https://leetcode.com/problems/time-to-cross-a-bridge/

use std::cmp::Reverse;
use std::collections::BinaryHeap;

#[derive(Clone, Copy, Eq, PartialEq)]
struct Worker {
    idx: i32,
    efficiency: i32,
    left_to_right: i32,
    pick_old: i32,
    right_to_left: i32,
    put_new: i32,
}

impl Ord for Worker {
    fn cmp(&self, other: &Self) -> std::cmp::Ordering {
        self.efficiency
            .cmp(&other.efficiency)
            .then(self.idx.cmp(&other.idx))
    }
}

impl PartialOrd for Worker {
    fn partial_cmp(&self, other: &Self) -> Option<std::cmp::Ordering> {
        Some(self.cmp(other))
    }
}

impl Solution {
    pub fn find_crossing_time(n: i32, k: i32, time: Vec<Vec<i32>>) -> i32 {
        let mut left: BinaryHeap<Worker> = BinaryHeap::new();
        let mut right: BinaryHeap<Worker> = BinaryHeap::new();
        for i in 0..k {
            left.push(Worker {
                idx: i,
                efficiency: time[i as usize][0] + time[i as usize][2],
                left_to_right: time[i as usize][0],
                pick_old: time[i as usize][1],
                right_to_left: time[i as usize][2],
                put_new: time[i as usize][3],
            });
        }
        let mut events: BinaryHeap<Reverse<(i32, i32, Worker)>> = BinaryHeap::new();
        let mut cur = 0;
        let mut remain = n;
        let mut done = 0;
        let mut bridge_free = 0;
        while done < n {
            while let Some(Reverse((t, side, w))) = events.peek().copied() {
                if t > cur {
                    break;
                }
                events.pop();
                if side == 0 {
                    left.push(w);
                } else {
                    right.push(w);
                }
            }
            if cur < bridge_free {
                cur = bridge_free;
                continue;
            }
            if let Some(w) = right.pop() {
                cur += w.right_to_left;
                bridge_free = cur;
                events.push(Reverse((cur + w.put_new, 0, w)));
                done += 1;
                continue;
            }
            if remain > 0 {
                if let Some(w) = left.pop() {
                    cur += w.left_to_right;
                    bridge_free = cur;
                    remain -= 1;
                    events.push(Reverse((cur + w.pick_old, 1, w)));
                    continue;
                }
            }
            if let Some(Reverse((t, _, _))) = events.peek() {
                cur = *t;
            } else {
                break;
            }
        }
        cur
    }
}
'''

FILES["2533_number_of_good_binary_strings"] = r'''// LeetCode 2533 - Number of Good Binary Strings
// https://leetcode.com/problems/number-of-good-binary-strings/

impl Solution {
    pub fn good_binary_strings(min_length: i32, max_length: i32, one_group: i32, zero_group: i32) -> i32 {
        const MOD: i32 = 1_000_000_007;
        let max_length = max_length as usize;
        let min_length = min_length as usize;
        let one_group = one_group as usize;
        let zero_group = zero_group as usize;
        let mut dp = vec![0i32; max_length + 1];
        dp[0] = 1;
        for i in 0..=max_length {
            if dp[i] == 0 {
                continue;
            }
            if i + one_group <= max_length {
                dp[i + one_group] = (dp[i + one_group] + dp[i]) % MOD;
            }
            if i + zero_group <= max_length {
                dp[i + zero_group] = (dp[i + zero_group] + dp[i]) % MOD;
            }
        }
        let mut ans = 0i32;
        for i in min_length..=max_length {
            ans = (ans + dp[i]) % MOD;
        }
        ans
    }
}
'''

FILES["2534_time_taken_to_cross_the_door"] = r'''// LeetCode 2534 - Time Taken to Cross the Door
// https://leetcode.com/problems/time-taken-to-cross-the-door/

use std::collections::VecDeque;

impl Solution {
    pub fn time_taken(arrival: Vec<i32>, state: Vec<i32>) -> Vec<i32> {
        let n = arrival.len();
        let mut ans = vec![0; n];
        let mut enter = VecDeque::new();
        let mut exitq = VecDeque::new();
        let mut i = 0;
        let mut t = 0;
        let mut prev = 1;
        while i < n || !enter.is_empty() || !exitq.is_empty() {
            while i < n && arrival[i] <= t {
                if state[i] == 0 {
                    enter.push_back(i);
                } else {
                    exitq.push_back(i);
                }
                i += 1;
            }
            if enter.is_empty() && exitq.is_empty() {
                if i < n {
                    t = arrival[i];
                    prev = 1;
                }
                continue;
            }
            if prev == 1 {
                if let Some(idx) = exitq.pop_front() {
                    ans[idx] = t;
                    prev = 1;
                } else if let Some(idx) = enter.pop_front() {
                    ans[idx] = t;
                    prev = 0;
                }
            } else if let Some(idx) = enter.pop_front() {
                ans[idx] = t;
                prev = 0;
            } else if let Some(idx) = exitq.pop_front() {
                ans[idx] = t;
                prev = 1;
            }
            t += 1;
        }
        ans
    }
}
'''

FILES["2535_difference_between_element_sum_and_digit_sum_of_an_array"] = r'''// LeetCode 2535 - Difference Between Element Sum and Digit Sum of an Array
// https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/

impl Solution {
    pub fn difference_of_sum(nums: Vec<i32>) -> i32 {
        let mut elem = 0;
        let mut digit = 0;
        for mut x in nums {
            elem += x;
            while x > 0 {
                digit += x % 10;
                x /= 10;
            }
        }
        (elem - digit).abs()
    }
}
'''

FILES["2536_increment_submatrices_by_one"] = r'''// LeetCode 2536 - Increment Submatrices by One
// https://leetcode.com/problems/increment-submatrices-by-one/

impl Solution {
    pub fn range_add_queries(n: i32, queries: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let n = n as usize;
        let mut diff = vec![vec![0; n + 1]; n + 1];
        for q in queries {
            let r1 = q[0] as usize;
            let c1 = q[1] as usize;
            let r2 = q[2] as usize;
            let c2 = q[3] as usize;
            diff[r1][c1] += 1;
            diff[r1][c2 + 1] -= 1;
            diff[r2 + 1][c1] -= 1;
            diff[r2 + 1][c2 + 1] += 1;
        }
        let mut mat = vec![vec![0; n]; n];
        for i in 0..n {
            for j in 0..n {
                let mut v = diff[i][j];
                if i > 0 {
                    v += mat[i - 1][j];
                }
                if j > 0 {
                    v += mat[i][j - 1];
                }
                if i > 0 && j > 0 {
                    v -= mat[i - 1][j - 1];
                }
                mat[i][j] = v;
            }
        }
        mat
    }
}
'''

FILES["2537_count_the_number_of_good_subarrays"] = r'''// LeetCode 2537 - Count the Number of Good Subarrays
// https://leetcode.com/problems/count-the-number-of-good-subarrays/

use std::collections::HashMap;

impl Solution {
    pub fn count_good(nums: Vec<i32>, k: i32) -> i64 {
        let mut freq = HashMap::new();
        let mut pairs = 0i64;
        let mut ans = 0i64;
        let mut left = 0;
        let n = nums.len();
        for right in 0..n {
            pairs += *freq.get(&nums[right]).unwrap_or(&0);
            *freq.entry(nums[right]).or_insert(0) += 1;
            while pairs >= k as i64 {
                ans += (n - right) as i64;
                *freq.get_mut(&nums[left]).unwrap() -= 1;
                pairs -= freq[&nums[left]];
                left += 1;
            }
        }
        ans
    }
}
'''

FILES["2538_difference_between_maximum_and_minimum_price_sum"] = r'''// LeetCode 2538 - Difference Between Maximum and Minimum Price Sum
// https://leetcode.com/problems/difference-between-maximum-and-minimum-price-sum/

impl Solution {
    pub fn max_output(n: i32, edges: Vec<Vec<i32>>, price: Vec<i32>) -> i64 {
        let n = n as usize;
        let mut g = vec![Vec::new(); n];
        for e in edges {
            g[e[0] as usize].push(e[1] as usize);
            g[e[1] as usize].push(e[0] as usize);
        }
        let mut ans = 0i64;
        fn dfs(u: usize, p: i32, g: &[Vec<usize>], price: &[i32], ans: &mut i64) -> i64 {
            let mut max_child = 0i64;
            for &v in &g[u] {
                if v as i32 == p {
                    continue;
                }
                let child = dfs(v, u as i32, g, price, ans);
                if child > max_child {
                    max_child = child;
                }
                if child > *ans {
                    *ans = child;
                }
            }
            price[u] as i64 + max_child
        }
        dfs(0, -1, &g, &price, &mut ans);
        ans
    }
}
'''

FILES["2539_count_the_number_of_good_subsequences"] = r'''// LeetCode 2539 - Count the Number of Good Subsequences
// https://leetcode.com/problems/count-the-number-of-good-subsequences/

impl Solution {
    pub fn count_good_subsequences(s: String) -> i32 {
        const MOD: i64 = 1_000_000_007;
        fn mod_pow(mut a: i64, mut e: i64) -> i64 {
            let mut res = 1i64;
            while e > 0 {
                if e & 1 == 1 {
                    res = res * a % MOD;
                }
                a = a * a % MOD;
                e >>= 1;
            }
            res
        }
        let mut cnt = [0i32; 26];
        let mut maxf = 0;
        for c in s.bytes() {
            let i = (c - b'a') as usize;
            cnt[i] += 1;
            if cnt[i] > maxf {
                maxf = cnt[i];
            }
        }
        let maxf = maxf as usize;
        let mut fact = vec![0i64; maxf + 1];
        let mut inv_fact = vec![0i64; maxf + 1];
        fact[0] = 1;
        for i in 1..=maxf {
            fact[i] = fact[i - 1] * i as i64 % MOD;
        }
        inv_fact[maxf] = mod_pow(fact[maxf], MOD - 2);
        for i in (1..=maxf).rev() {
            inv_fact[i - 1] = inv_fact[i] * i as i64 % MOD;
        }
        let comb = |n: i32, k: i32| -> i64 {
            if k < 0 || k > n {
                return 0;
            }
            let n = n as usize;
            let k = k as usize;
            fact[n] * inv_fact[k] % MOD * inv_fact[n - k] % MOD
        };
        let mut ans = 0i64;
        for k in 1..=maxf as i32 {
            let mut ways = 1i64;
            for i in 0..26 {
                if cnt[i] >= k {
                    ways = ways * (1 + comb(cnt[i], k)) % MOD;
                }
            }
            ans = (ans + ways - 1 + MOD) % MOD;
        }
        ans as i32
    }
}
'''

FILES["2540_minimum_common_value"] = r'''// LeetCode 2540 - Minimum Common Value
// https://leetcode.com/problems/minimum-common-value/

impl Solution {
    pub fn get_common(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        let mut i = 0;
        let mut j = 0;
        while i < nums1.len() && j < nums2.len() {
            if nums1[i] == nums2[j] {
                return nums1[i];
            }
            if nums1[i] < nums2[j] {
                i += 1;
            } else {
                j += 1;
            }
        }
        -1
    }
}
'''

FILES["2541_minimum_operations_to_make_array_equal_ii"] = r'''// LeetCode 2541 - Minimum Operations to Make Array Equal II
// https://leetcode.com/problems/minimum-operations-to-make-array-equal-ii/

impl Solution {
    pub fn min_operations(nums1: Vec<i32>, nums2: Vec<i32>, k: i32) -> i64 {
        if k == 0 {
            for i in 0..nums1.len() {
                if nums1[i] != nums2[i] {
                    return -1;
                }
            }
            return 0;
        }
        let mut pos = 0i64;
        let mut neg = 0i64;
        for i in 0..nums1.len() {
            let d = nums1[i] - nums2[i];
            if d % k != 0 {
                return -1;
            }
            if d > 0 {
                pos += (d / k) as i64;
            } else {
                neg += ((-d) / k) as i64;
            }
        }
        if pos != neg {
            -1
        } else {
            pos
        }
    }
}
'''

FILES["2542_maximum_subsequence_score"] = r'''// LeetCode 2542 - Maximum Subsequence Score
// https://leetcode.com/problems/maximum-subsequence-score/

use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn max_score(nums1: Vec<i32>, nums2: Vec<i32>, k: i32) -> i64 {
        let n = nums1.len();
        let k = k as usize;
        let mut idx: Vec<usize> = (0..n).collect();
        idx.sort_by_key(|&i| Reverse(nums2[i]));
        let mut pq: BinaryHeap<Reverse<i32>> = BinaryHeap::new();
        let mut sum = 0i64;
        let mut ans = 0i64;
        for i in idx {
            pq.push(Reverse(nums1[i]));
            sum += nums1[i] as i64;
            if pq.len() > k {
                sum -= pq.pop().unwrap().0 as i64;
            }
            if pq.len() == k {
                let cand = sum * nums2[i] as i64;
                if cand > ans {
                    ans = cand;
                }
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
        if text.startswith("\ufeff"):
            raise SystemExit(f"BOM in {folder}")
        n += 1
        print(f"wrote {folder}")
    print(f"total={n}")

if __name__ == "__main__":
    main()

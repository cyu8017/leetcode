#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
FILES = {}

FILES["2543_check_if_point_is_reachable"] = r'''// LeetCode 2543 - Check if Point Is Reachable
// https://leetcode.com/problems/check-if-point-is-reachable/

impl Solution {
    pub fn is_reachable(target_x: i32, target_y: i32) -> bool {
        fn gcd(mut a: i32, mut b: i32) -> i32 {
            while b != 0 {
                let t = a % b;
                a = b;
                b = t;
            }
            a
        }
        let mut g = gcd(target_x, target_y);
        while g % 2 == 0 {
            g /= 2;
        }
        g == 1
    }
}
'''

FILES["2544_alternating_digit_sum"] = r'''// LeetCode 2544 - Alternating Digit Sum
// https://leetcode.com/problems/alternating-digit-sum/

impl Solution {
    pub fn alternate_digit_sum(mut n: i32) -> i32 {
        let mut s = Vec::new();
        while n > 0 {
            s.push(n % 10);
            n /= 10;
        }
        let mut ans = 0;
        let mut sign = 1;
        for i in (0..s.len()).rev() {
            ans += sign * s[i];
            sign = -sign;
        }
        ans
    }
}
'''

FILES["2545_sort_the_students_by_their_kth_score"] = r'''// LeetCode 2545 - Sort the Students by Their Kth Score
// https://leetcode.com/problems/sort-the-students-by-their-kth-score/

impl Solution {
    pub fn sort_the_students(mut score: Vec<Vec<i32>>, k: i32) -> Vec<Vec<i32>> {
        let k = k as usize;
        score.sort_by(|a, b| b[k].cmp(&a[k]));
        score
    }
}
'''

FILES["2546_apply_bitwise_operations_to_make_strings_equal"] = r'''// LeetCode 2546 - Apply Bitwise Operations to Make Strings Equal
// https://leetcode.com/problems/apply-bitwise-operations-to-make-strings-equal/

impl Solution {
    pub fn make_strings_equal(s: String, target: String) -> bool {
        let has1s = s.bytes().any(|c| c == b'1');
        let has1t = target.bytes().any(|c| c == b'1');
        has1s == has1t
    }
}
'''

FILES["2547_minimum_cost_to_split_an_array"] = r'''// LeetCode 2547 - Minimum Cost to Split an Array
// https://leetcode.com/problems/minimum-cost-to-split-an-array/

use std::collections::HashMap;

impl Solution {
    pub fn min_cost(nums: Vec<i32>, k: i32) -> i32 {
        let n = nums.len();
        let inf = i64::MAX / 4;
        let mut dp = vec![inf; n + 1];
        dp[0] = 0;
        for i in 0..n {
            let mut freq = HashMap::new();
            let mut trimmed = 0i64;
            for j in i..n {
                let c = freq.entry(nums[j]).or_insert(0);
                *c += 1;
                if *c == 2 {
                    trimmed += 2;
                } else if *c > 2 {
                    trimmed += 1;
                }
                let cost = dp[i] + k as i64 + trimmed;
                if cost < dp[j + 1] {
                    dp[j + 1] = cost;
                }
            }
        }
        dp[n] as i32
    }
}
'''

FILES["2548_maximum_price_to_fill_a_bag"] = r'''// LeetCode 2548 - Maximum Price to Fill a Bag
// https://leetcode.com/problems/maximum-price-to-fill-a-bag/

impl Solution {
    pub fn max_price(mut items: Vec<Vec<i32>>, capacity: i32) -> f64 {
        items.sort_by(|a, b| {
            let ra = a[0] as f64 / a[1] as f64;
            let rb = b[0] as f64 / b[1] as f64;
            rb.partial_cmp(&ra).unwrap()
        });
        let mut ans = 0.0;
        let mut remain = capacity;
        for it in items {
            let price = it[0];
            let weight = it[1];
            if remain >= weight {
                ans += price as f64;
                remain -= weight;
            } else {
                ans += price as f64 * remain as f64 / weight as f64;
                remain = 0;
                break;
            }
        }
        if remain > 0 {
            -1.0
        } else {
            ans
        }
    }
}
'''

FILES["2549_count_distinct_numbers_on_board"] = r'''// LeetCode 2549 - Count Distinct Numbers on Board
// https://leetcode.com/problems/count-distinct-numbers-on-board/

impl Solution {
    pub fn distinct_integers(n: i32) -> i32 {
        if n == 1 {
            1
        } else {
            n - 1
        }
    }
}
'''

FILES["2550_count_collisions_of_monkeys_on_a_polygon"] = r'''// LeetCode 2550 - Count Collisions of Monkeys on a Polygon
// https://leetcode.com/problems/count-collisions-of-monkeys-on-a-polygon/

impl Solution {
    pub fn monkey_move(n: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        fn powmod(mut a: i64, mut e: i32) -> i32 {
            let mut res = 1i64;
            while e > 0 {
                if e & 1 == 1 {
                    res = res * a % MOD;
                }
                a = a * a % MOD;
                e >>= 1;
            }
            res as i32
        }
        (powmod(2, n) as i64 - 2 + MOD) as i32 % MOD as i32
    }
}
'''

FILES["2551_put_marbles_in_bags"] = r'''// LeetCode 2551 - Put Marbles in Bags
// https://leetcode.com/problems/put-marbles-in-bags/

impl Solution {
    pub fn put_marbles(weights: Vec<i32>, k: i32) -> i64 {
        let n = weights.len();
        if k == 1 || k as usize == n {
            return 0;
        }
        let mut pair: Vec<i32> = (0..n - 1).map(|i| weights[i] + weights[i + 1]).collect();
        pair.sort_unstable();
        let mut mn = 0i64;
        let mut mx = 0i64;
        for i in 0..(k as usize - 1) {
            mn += pair[i] as i64;
            mx += pair[n - 2 - i] as i64;
        }
        mx - mn
    }
}
'''

FILES["2552_count_increasing_quadruplets"] = r'''// LeetCode 2552 - Count Increasing Quadruplets
// https://leetcode.com/problems/count-increasing-quadruplets/

impl Solution {
    pub fn count_quadruplets(nums: Vec<i32>) -> i64 {
        let n = nums.len();
        let mut ans = 0i64;
        let mut great = vec![0i32; n];
        for j in 0..n {
            for i in 0..j {
                if nums[i] < nums[j] {
                    ans += great[i] as i64;
                } else if nums[i] > nums[j] {
                    great[i] += 1;
                }
            }
        }
        ans
    }
}
'''

FILES["2553_separate_the_digits_in_an_array"] = r'''// LeetCode 2553 - Separate the Digits in an Array
// https://leetcode.com/problems/separate-the-digits-in-an-array/

impl Solution {
    pub fn separate_digits(nums: Vec<i32>) -> Vec<i32> {
        let mut ans = Vec::new();
        for mut x in nums {
            let mut digits = Vec::new();
            while x > 0 {
                digits.push(x % 10);
                x /= 10;
            }
            for d in digits.into_iter().rev() {
                ans.push(d);
            }
        }
        ans
    }
}
'''

FILES["2554_maximum_number_of_integers_to_choose_from_a_range_i"] = r'''// LeetCode 2554 - Maximum Number of Integers to Choose From a Range I
// https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-i/

use std::collections::HashSet;

impl Solution {
    pub fn max_count(banned: Vec<i32>, n: i32, max_sum: i32) -> i32 {
        let ban: HashSet<i32> = banned.into_iter().collect();
        let mut ans = 0;
        let mut sum = 0;
        for i in 1..=n {
            if ban.contains(&i) {
                continue;
            }
            if sum + i > max_sum {
                break;
            }
            sum += i;
            ans += 1;
        }
        ans
    }
}
'''

FILES["2555_maximize_win_from_two_segments"] = r'''// LeetCode 2555 - Maximize Win From Two Segments
// https://leetcode.com/problems/maximize-win-from-two-segments/

impl Solution {
    pub fn maximize_win(prize_positions: Vec<i32>, k: i32) -> i32 {
        let n = prize_positions.len();
        let mut dp = vec![0; n + 1];
        let mut ans = 0;
        let mut left = 0;
        for right in 0..n {
            while prize_positions[right] - prize_positions[left] > k {
                left += 1;
            }
            let cur = (right - left + 1) as i32;
            if dp[left] + cur > ans {
                ans = dp[left] + cur;
            }
            let mut best = cur;
            if dp[right] > best {
                best = dp[right];
            }
            dp[right + 1] = best;
        }
        ans
    }
}
'''

FILES["2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip"] = r'''// LeetCode 2556 - Disconnect Path in a Binary Matrix by at Most One Flip
// https://leetcode.com/problems/disconnect-path-in-a-binary-matrix-by-at-most-one-flip/

impl Solution {
    pub fn is_possible_to_cut_path(mut grid: Vec<Vec<i32>>) -> bool {
        let m = grid.len();
        let n = grid[0].len();
        fn dfs(r: usize, c: usize, grid: &mut [Vec<i32>], m: usize, n: usize) -> bool {
            if r == m - 1 && c == n - 1 {
                return true;
            }
            if r >= m || c >= n || grid[r][c] == 0 {
                return false;
            }
            if !(r == 0 && c == 0) {
                grid[r][c] = 0;
            }
            dfs(r + 1, c, grid, m, n) || dfs(r, c + 1, grid, m, n)
        }
        if !dfs(0, 0, &mut grid, m, n) {
            return true;
        }
        grid[0][0] = 1;
        !dfs(0, 0, &mut grid, m, n)
    }
}
'''

FILES["2557_maximum_number_of_integers_to_choose_from_a_range_ii"] = r'''// LeetCode 2557 - Maximum Number of Integers to Choose From a Range II
// https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-ii/

impl Solution {
    pub fn max_count(mut banned: Vec<i32>, n: i32, max_sum: i64) -> i32 {
        banned.sort_unstable();
        let mut uniq = Vec::new();
        for x in banned {
            if x >= 1 && x <= n && (uniq.is_empty() || *uniq.last().unwrap() != x) {
                uniq.push(x);
            }
        }
        let mut ans = 0i32;
        let mut prev = 0i32;
        let mut remain = max_sum;
        let mut check = |l: i64, r: i64, remain: &mut i64, ans: &mut i32| {
            if l > r || *remain <= 0 {
                return;
            }
            let mut lo = l;
            let mut hi = r;
            let mut best = l - 1;
            while lo <= hi {
                let mid = (lo + hi) / 2;
                let cnt = mid - l + 1;
                let sum = (l + mid) * cnt / 2;
                if sum <= *remain {
                    best = mid;
                    lo = mid + 1;
                } else {
                    hi = mid - 1;
                }
            }
            if best >= l {
                let cnt = (best - l + 1) as i32;
                *ans += cnt;
                *remain -= (l + best) * cnt as i64 / 2;
            }
        };
        for b in uniq {
            check(prev as i64 + 1, b as i64 - 1, &mut remain, &mut ans);
            prev = b;
        }
        check(prev as i64 + 1, n as i64, &mut remain, &mut ans);
        ans
    }
}
'''

FILES["2558_take_gifts_from_the_richest_pile"] = r'''// LeetCode 2558 - Take Gifts From the Richest Pile
// https://leetcode.com/problems/take-gifts-from-the-richest-pile/

use std::collections::BinaryHeap;

impl Solution {
    pub fn pick_gifts(gifts: Vec<i32>, k: i32) -> i64 {
        let mut h = BinaryHeap::from(gifts);
        for _ in 0..k {
            let x = h.pop().unwrap();
            h.push((x as f64).sqrt() as i32);
        }
        h.into_iter().map(|x| x as i64).sum()
    }
}
'''

FILES["2559_count_vowel_strings_in_ranges"] = r'''// LeetCode 2559 - Count Vowel Strings in Ranges
// https://leetcode.com/problems/count-vowel-strings-in-ranges/

impl Solution {
    pub fn vowel_strings(words: Vec<String>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        fn is_v(c: u8) -> bool {
            matches!(c, b'a' | b'e' | b'i' | b'o' | b'u')
        }
        let n = words.len();
        let mut pref = vec![0; n + 1];
        for i in 0..n {
            pref[i + 1] = pref[i];
            let w = words[i].as_bytes();
            if !w.is_empty() && is_v(w[0]) && is_v(w[w.len() - 1]) {
                pref[i + 1] += 1;
            }
        }
        queries
            .into_iter()
            .map(|q| pref[q[1] as usize + 1] - pref[q[0] as usize])
            .collect()
    }
}
'''

FILES["2560_house_robber_iv"] = r'''// LeetCode 2560 - House Robber IV
// https://leetcode.com/problems/house-robber-iv/

impl Solution {
    pub fn min_capability(nums: Vec<i32>, k: i32) -> i32 {
        let mut lo = *nums.iter().min().unwrap();
        let mut hi = *nums.iter().max().unwrap();
        let ok = |cap: i32| {
            let mut cnt = 0;
            let mut i = 0;
            while i < nums.len() {
                if nums[i] <= cap {
                    cnt += 1;
                    i += 2;
                } else {
                    i += 1;
                }
            }
            cnt >= k
        };
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

FILES["2561_rearranging_fruits"] = r'''// LeetCode 2561 - Rearranging Fruits
// https://leetcode.com/problems/rearranging-fruits/

use std::collections::HashMap;

impl Solution {
    pub fn min_cost(basket1: Vec<i32>, basket2: Vec<i32>) -> i64 {
        let mut freq = HashMap::new();
        let mut mn = i32::MAX;
        for x in basket1 {
            *freq.entry(x).or_insert(0) += 1;
            mn = mn.min(x);
        }
        for x in basket2 {
            *freq.entry(x).or_insert(0) -= 1;
            mn = mn.min(x);
        }
        let mut extra = Vec::new();
        for (&v, &c) in &freq {
            if c % 2 != 0 {
                return -1;
            }
            for _ in 0..c.abs() / 2 {
                extra.push(v);
            }
        }
        extra.sort_unstable();
        let mut ans = 0i64;
        for i in 0..extra.len() / 2 {
            let a = extra[i] as i64;
            let b = 2 * mn as i64;
            ans += a.min(b);
        }
        ans
    }
}
'''

FILES["2562_find_the_array_concatenation_value"] = r'''// LeetCode 2562 - Find the Array Concatenation Value
// https://leetcode.com/problems/find-the-array-concatenation-value/

impl Solution {
    pub fn find_the_array_conc_val(nums: Vec<i32>) -> i64 {
        let mut ans = 0i64;
        let mut l = 0;
        let mut r = nums.len() as i32 - 1;
        while l <= r {
            if l == r {
                ans += nums[l as usize] as i64;
                break;
            }
            let left = nums[l as usize];
            let right = nums[r as usize];
            let mut pow = 1i64;
            let mut t = right;
            while t > 0 {
                pow *= 10;
                t /= 10;
            }
            ans += left as i64 * pow + right as i64;
            l += 1;
            r -= 1;
        }
        ans
    }
}
'''

FILES["2563_count_the_number_of_fair_pairs"] = r'''// LeetCode 2563 - Count the Number of Fair Pairs
// https://leetcode.com/problems/count-the-number-of-fair-pairs/

impl Solution {
    pub fn count_fair_pairs(mut nums: Vec<i32>, lower: i32, upper: i32) -> i64 {
        nums.sort_unstable();
        let count = |x: i32| {
            let mut ans = 0i64;
            let mut l = 0;
            let mut r = nums.len() as i32 - 1;
            while l < r {
                if nums[l as usize] + nums[r as usize] <= x {
                    ans += (r - l) as i64;
                    l += 1;
                } else {
                    r -= 1;
                }
            }
            ans
        };
        count(upper) - count(lower - 1)
    }
}
'''

FILES["2564_substring_xor_queries"] = r'''// LeetCode 2564 - Substring XOR Queries
// https://leetcode.com/problems/substring-xor-queries/

use std::collections::HashMap;

impl Solution {
    pub fn substring_xor_queries(s: String, queries: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let s = s.as_bytes();
        let n = s.len();
        let mut pos: HashMap<i32, (i32, i32)> = HashMap::new();
        for i in 0..n {
            if s[i] == b'0' {
                pos.entry(0).or_insert((i as i32, i as i32));
                continue;
            }
            let mut val = 0i32;
            for j in i..n.min(i + 30) {
                val = val * 2 + (s[j] - b'0') as i32;
                pos.entry(val).or_insert((i as i32, j as i32));
            }
        }
        queries
            .into_iter()
            .map(|q| {
                let need = q[0] ^ q[1];
                if let Some(&(a, b)) = pos.get(&need) {
                    vec![a, b]
                } else {
                    vec![-1, -1]
                }
            })
            .collect()
    }
}
'''

FILES["2565_subsequence_with_the_minimum_score"] = r'''// LeetCode 2565 - Subsequence With the Minimum Score
// https://leetcode.com/problems/subsequence-with-the-minimum-score/

impl Solution {
    pub fn minimum_score(s: String, t: String) -> i32 {
        let s = s.as_bytes();
        let t = t.as_bytes();
        let n = s.len();
        let m = t.len();
        let mut left = vec![-1i32; m];
        let mut right = vec![-1i32; m];
        let mut j = 0;
        for i in 0..n {
            if j < m && s[i] == t[j] {
                left[j] = i as i32;
                j += 1;
            }
        }
        j = m;
        for i in (0..n).rev() {
            if j > 0 && s[i] == t[j - 1] {
                right[j - 1] = i as i32;
                j -= 1;
            }
        }
        if m > 0 && left[m - 1] != -1 {
            return 0;
        }
        let mut ans = m as i32;
        for i in 0..m {
            if right[i] != -1 {
                if i as i32 + 0 < ans {
                    ans = i as i32;
                }
                break;
            }
        }
        for i in (0..m).rev() {
            if left[i] != -1 {
                let rem = (m - 1 - i) as i32;
                if rem < ans {
                    ans = rem;
                }
                break;
            }
        }
        let mut j = 0;
        for i in 0..m {
            if left[i] == -1 {
                break;
            }
            while j < m && (right[j] == -1 || right[j] <= left[i]) {
                j += 1;
            }
            if j < m {
                let rem = j as i32 - i as i32 - 1;
                if rem < ans {
                    ans = rem;
                }
            }
        }
        ans
    }
}
'''

FILES["2566_maximum_difference_by_remapping_a_digit"] = r'''// LeetCode 2566 - Maximum Difference by Remapping a Digit
// https://leetcode.com/problems/maximum-difference-by-remapping-a-digit/

impl Solution {
    pub fn min_max_difference(num: i32) -> i32 {
        let s: Vec<u8> = num.to_string().into_bytes();
        let remap = |from: u8, to: u8| {
            let mut v = 0i32;
            for &c in &s {
                let d = if c == from { to } else { c };
                v = v * 10 + (d - b'0') as i32;
            }
            v
        };
        let mut max_v = num;
        for &c in &s {
            if c != b'9' {
                max_v = remap(c, b'9');
                break;
            }
        }
        let min_v = remap(s[0], b'0');
        max_v - min_v
    }
}
'''

FILES["2567_minimum_score_by_changing_two_elements"] = r'''// LeetCode 2567 - Minimum Score by Changing Two Elements
// https://leetcode.com/problems/minimum-score-by-changing-two-elements/

impl Solution {
    pub fn minimize_sum(mut nums: Vec<i32>) -> i32 {
        nums.sort_unstable();
        let n = nums.len();
        let a = nums[n - 1] - nums[2];
        let b = nums[n - 3] - nums[0];
        let c = nums[n - 2] - nums[1];
        a.min(b).min(c)
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

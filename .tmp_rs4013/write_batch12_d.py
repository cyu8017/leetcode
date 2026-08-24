#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
FILES = {}

def add(folder, body):
    FILES[folder] = body.strip() + "\n"

add("2917_find_the_k_or_of_an_array", r'''
// LeetCode 2917 - Find the K-or of an Array
// https://leetcode.com/problems/find-the-k-or-of-an-array/

impl Solution {
    pub fn find_k_or(nums: Vec<i32>, k: i32) -> i32 {
        let mut ans = 0;
        for b in 0..31 {
            let mut cnt = 0;
            for &v in &nums {
                if (v & (1 << b)) != 0 {
                    cnt += 1;
                }
            }
            if cnt >= k {
                ans |= 1 << b;
            }
        }
        ans
    }
}
''')

add("2918_minimum_equal_sum_of_two_arrays_after_replacing_zeros", r'''
// LeetCode 2918 - Minimum Equal Sum of Two Arrays After Replacing Zeros
// https://leetcode.com/problems/minimum-equal-sum-of-two-arrays-after-replacing-zeros/

impl Solution {
    pub fn min_sum(nums1: Vec<i32>, nums2: Vec<i32>) -> i64 {
        let mut s1 = 0i64;
        let mut s2 = 0i64;
        let mut z1 = 0i32;
        let mut z2 = 0i32;
        for v in nums1 {
            if v == 0 {
                z1 += 1;
                s1 += 1;
            } else {
                s1 += v as i64;
            }
        }
        for v in nums2 {
            if v == 0 {
                z2 += 1;
                s2 += 1;
            } else {
                s2 += v as i64;
            }
        }
        if z1 == 0 && s1 < s2 {
            return -1;
        }
        if z2 == 0 && s2 < s1 {
            return -1;
        }
        s1.max(s2)
    }
}
''')

add("2919_minimum_increment_operations_to_make_array_beautiful", r'''
// LeetCode 2919 - Minimum Increment Operations to Make Array Beautiful
// https://leetcode.com/problems/minimum-increment-operations-to-make-array-beautiful/

impl Solution {
    pub fn min_increment_operations(nums: Vec<i32>, k: i32) -> i64 {
        let mut dp0 = 0i64;
        let mut dp1 = 0i64;
        let mut dp2 = 0i64;
        for v in nums {
            let cost = if v < k { (k - v) as i64 } else { 0 };
            let nd0 = cost + dp0.min(dp1).min(dp2);
            dp0 = dp1;
            dp1 = dp2;
            dp2 = nd0;
        }
        dp0.min(dp1).min(dp2)
    }
}
''')

add("2920_maximum_points_after_collecting_coins_from_all_nodes", r'''
// LeetCode 2920 - Maximum Points After Collecting Coins From All Nodes
// https://leetcode.com/problems/maximum-points-after-collecting-coins-from-all-nodes/

use std::collections::HashMap;

impl Solution {
    pub fn maximum_points(edges: Vec<Vec<i32>>, coins: Vec<i32>, k: i32) -> i32 {
        let n = coins.len();
        let mut g = vec![Vec::new(); n];
        for e in edges {
            g[e[0] as usize].push(e[1] as usize);
            g[e[1] as usize].push(e[0] as usize);
        }
        fn dfs(
            u: usize,
            p: i32,
            mut shifts: i32,
            g: &[Vec<usize>],
            coins: &[i32],
            k: i32,
            memo: &mut HashMap<(usize, i32), i32>,
        ) -> i32 {
            if shifts > 14 {
                shifts = 14;
            }
            if let Some(&v) = memo.get(&(u, shifts)) {
                return v;
            }
            let c = coins[u] >> shifts;
            let mut opt1 = c - k;
            let mut opt2 = c / 2;
            for &v in &g[u] {
                if v as i32 == p {
                    continue;
                }
                opt1 += dfs(v, u as i32, shifts, g, coins, k, memo);
                opt2 += dfs(v, u as i32, shifts + 1, g, coins, k, memo);
            }
            let best = opt1.max(opt2);
            memo.insert((u, shifts), best);
            best
        }
        let mut memo = HashMap::new();
        dfs(0, -1, 0, &g, &coins, k, &mut memo)
    }
}
''')

add("2921_maximum_profitable_triplets_with_increasing_prices_ii", r'''
// LeetCode 2921 - Maximum Profitable Triplets With Increasing Prices II
// https://leetcode.com/problems/maximum-profitable-triplets-with-increasing-prices-ii/

impl Solution {
    pub fn max_profit(prices: Vec<i32>, profits: Vec<i32>) -> i32 {
        let n = prices.len();
        let mut ans = -1;
        let mut max_left = vec![-1i32; n];
        let mut bit = vec![0i32; 5002];
        let update = |bit: &mut [i32], mut i: usize, val: i32| {
            while i < bit.len() {
                if val > bit[i] {
                    bit[i] = val;
                }
                i += i & i.wrapping_neg();
            }
        };
        let query = |bit: &[i32], mut i: usize| -> i32 {
            let mut best = -1;
            while i > 0 {
                if bit[i] > best {
                    best = bit[i];
                }
                i -= i & i.wrapping_neg();
            }
            best
        };
        for j in 0..n {
            max_left[j] = query(&bit, (prices[j] - 1) as usize);
            update(&mut bit, prices[j] as usize, profits[j]);
        }
        for j in 0..n {
            let mut best_r = -1;
            for k in j + 1..n {
                if prices[k] > prices[j] && profits[k] > best_r {
                    best_r = profits[k];
                }
            }
            if max_left[j] >= 0 && best_r >= 0 {
                ans = ans.max(max_left[j] + profits[j] + best_r);
            }
        }
        ans
    }
}
''')

add("2923_find_champion_i", r'''
// LeetCode 2923 - Find Champion I
// https://leetcode.com/problems/find-champion-i/

impl Solution {
    pub fn find_champion(grid: Vec<Vec<i32>>) -> i32 {
        let n = grid.len();
        for i in 0..n {
            let mut win = true;
            for j in 0..n {
                if i != j && grid[i][j] == 0 {
                    win = false;
                    break;
                }
            }
            if win {
                return i as i32;
            }
        }
        -1
    }
}
''')

add("2924_find_champion_ii", r'''
// LeetCode 2924 - Find Champion II
// https://leetcode.com/problems/find-champion-ii/

impl Solution {
    pub fn find_champion(n: i32, edges: Vec<Vec<i32>>) -> i32 {
        let mut indeg = vec![0i32; n as usize];
        for e in edges {
            indeg[e[1] as usize] += 1;
        }
        let mut ans = -1;
        for i in 0..n {
            if indeg[i as usize] == 0 {
                if ans != -1 {
                    return -1;
                }
                ans = i;
            }
        }
        ans
    }
}
''')

add("2925_maximum_score_after_applying_operations_on_a_tree", r'''
// LeetCode 2925 - Maximum Score After Applying Operations on a Tree
// https://leetcode.com/problems/maximum-score-after-applying-operations-on-a-tree/

impl Solution {
    pub fn maximum_score_after_operations(edges: Vec<Vec<i32>>, values: Vec<i32>) -> i64 {
        let n = values.len();
        let mut g = vec![Vec::new(); n];
        for e in edges {
            g[e[0] as usize].push(e[1] as usize);
            g[e[1] as usize].push(e[0] as usize);
        }
        let total: i64 = values.iter().map(|&v| v as i64).sum();
        fn dfs(u: usize, p: i32, g: &[Vec<usize>], values: &[i32]) -> i64 {
            let mut sum_kids = 0i64;
            let mut is_leaf = true;
            for &v in &g[u] {
                if v as i32 == p {
                    continue;
                }
                is_leaf = false;
                sum_kids += dfs(v, u as i32, g, values);
            }
            if is_leaf {
                return values[u] as i64;
            }
            (values[u] as i64).min(sum_kids)
        }
        total - dfs(0, -1, &g, &values)
    }
}
''')

add("2926_maximum_balanced_subsequence_sum", r'''
// LeetCode 2926 - Maximum Balanced Subsequence Sum
// https://leetcode.com/problems/maximum-balanced-subsequence-sum/

impl Solution {
    pub fn max_balanced_subsequence_sum(nums: Vec<i32>) -> i64 {
        let n = nums.len();
        let mut keys: Vec<i32> = (0..n).map(|i| nums[i] - i as i32).collect();
        let mut uniq = keys.clone();
        uniq.sort_unstable();
        uniq.dedup();
        let idx_of = |v: i32, uniq: &[i32]| -> usize {
            uniq.binary_search(&v).unwrap_or_else(|e| e) + 1
        };
        const NEG_INF: i64 = -(1i64 << 60);
        let mut bit = vec![NEG_INF; uniq.len() + 2];
        let update = |bit: &mut [i64], mut i: usize, val: i64| {
            while i < bit.len() {
                if val > bit[i] {
                    bit[i] = val;
                }
                i += i & i.wrapping_neg();
            }
        };
        let query = |bit: &[i64], mut i: usize| -> i64 {
            let mut best = NEG_INF;
            while i > 0 {
                if bit[i] > best {
                    best = bit[i];
                }
                i -= i & i.wrapping_neg();
            }
            best
        };
        let mut ans = NEG_INF;
        for i in 0..n {
            let id = idx_of(keys[i], &uniq);
            let best = query(&bit, id);
            let mut cur = nums[i] as i64;
            if best > NEG_INF / 2 {
                cur = cur.max(best + nums[i] as i64);
            }
            update(&mut bit, id, cur);
            if cur > ans {
                ans = cur;
            }
        }
        ans
    }
}
''')

add("2927_distribute_candies_among_children_iii", r'''
// LeetCode 2927 - Distribute Candies Among Children III
// https://leetcode.com/problems/distribute-candies-among-children-iii/

impl Solution {
    pub fn distribute_candies(n: i32, limit: i32) -> i64 {
        let comb = |x: i64| -> i64 {
            if x < 2 {
                0
            } else {
                x * (x - 1) / 2
            }
        };
        let n = n as i64;
        let limit = limit as i64;
        let mut ans = comb(n + 2);
        ans -= 3 * comb(n - limit + 1);
        ans += 3 * comb(n - 2 * (limit + 1) + 2);
        ans -= comb(n - 3 * (limit + 1) + 2);
        if ans < 0 {
            ans = 0;
        }
        ans
    }
}
''')

add("2928_distribute_candies_among_children_i", r'''
// LeetCode 2928 - Distribute Candies Among Children I
// https://leetcode.com/problems/distribute-candies-among-children-i/

impl Solution {
    pub fn distribute_candies(n: i32, limit: i32) -> i32 {
        let mut ans = 0;
        for i in 0..=limit {
            for j in 0..=limit {
                let k = n - i - j;
                if k >= 0 && k <= limit {
                    ans += 1;
                }
            }
        }
        ans
    }
}
''')

add("2929_distribute_candies_among_children_ii", r'''
// LeetCode 2929 - Distribute Candies Among Children II
// https://leetcode.com/problems/distribute-candies-among-children-ii/

impl Solution {
    pub fn distribute_candies(n: i32, limit: i32) -> i64 {
        let comb2 = |x: i64| -> i64 {
            if x < 0 {
                0
            } else {
                (x + 1) * (x + 2) / 2
            }
        };
        let n = n as i64;
        let limit = limit as i64;
        let mut ans = comb2(n);
        ans -= 3 * comb2(n - (limit + 1));
        ans += 3 * comb2(n - 2 * (limit + 1));
        ans -= comb2(n - 3 * (limit + 1));
        ans
    }
}
''')

add("2930_number_of_strings_which_can_be_rearranged_to_contain_substring", r'''
// LeetCode 2930 - Number of Strings Which Can Be Rearranged to Contain Substring
// https://leetcode.com/problems/number-of-strings-which-can-be-rearranged-to-contain-substring/

impl Solution {
    pub fn string_count(n: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        fn mod_pow(mut a: i64, mut b: i32) -> i64 {
            const MOD: i64 = 1_000_000_007;
            let mut res = 1i64;
            a %= MOD;
            while b > 0 {
                if b & 1 == 1 {
                    res = res * a % MOD;
                }
                a = a * a % MOD;
                b >>= 1;
            }
            res
        }
        if n < 4 {
            return 0;
        }
        let mut ans = mod_pow(26, n);
        ans = (ans - 3 * mod_pow(25, n) % MOD + MOD) % MOD;
        ans = (ans + 3 * mod_pow(24, n) % MOD) % MOD;
        ans = (ans - mod_pow(23, n) + MOD) % MOD;
        ans = (ans + (n as i64 % MOD) * mod_pow(25, n - 1) % MOD) % MOD;
        ans = (ans - 2 * (n as i64 % MOD) % MOD * mod_pow(24, n - 1) % MOD + MOD) % MOD;
        ans = (ans + (n as i64 % MOD) * mod_pow(23, n - 1) % MOD) % MOD;
        ans = (ans
            - (n as i64 % MOD) * ((n - 1 + MOD as i32) as i64 % MOD) % MOD * mod_pow(24, n - 2) % MOD
                % MOD
            + MOD)
            % MOD;
        ans = (ans
            + (n as i64 % MOD) * ((n - 1 + MOD as i32) as i64 % MOD) % MOD * mod_pow(23, n - 2) % MOD)
            % MOD;
        ans as i32
    }
}
''')

add("2931_maximum_spending_after_buying_items", r'''
// LeetCode 2931 - Maximum Spending After Buying Items
// https://leetcode.com/problems/maximum-spending-after-buying-items/

impl Solution {
    pub fn max_spending(values: Vec<Vec<i32>>) -> i64 {
        let m = values.len();
        let n = values[0].len();
        let mut idx = vec![n as i32 - 1; m];
        let mut ans = 0i64;
        let mut day = 1i64;
        let total = m * n;
        for _ in 0..total {
            let mut best_i = 0usize;
            let mut best_v = 1i64 << 60;
            for i in 0..m {
                if idx[i] >= 0 && (values[i][idx[i] as usize] as i64) < best_v {
                    best_v = values[i][idx[i] as usize] as i64;
                    best_i = i;
                }
            }
            ans += best_v * day;
            idx[best_i] -= 1;
            day += 1;
        }
        ans
    }
}
''')

add("2932_maximum_strong_pair_xor_i", r'''
// LeetCode 2932 - Maximum Strong Pair XOR I
// https://leetcode.com/problems/maximum-strong-pair-xor-i/

impl Solution {
    pub fn maximum_strong_pair_xor(nums: Vec<i32>) -> i32 {
        let mut ans = 0;
        for i in 0..nums.len() {
            for j in i..nums.len() {
                let x = nums[i];
                let y = nums[j];
                if (x - y).abs() <= x.min(y) {
                    ans = ans.max(x ^ y);
                }
            }
        }
        ans
    }
}
''')

add("2933_high_access_employees", r'''
// LeetCode 2933 - High-Access Employees
// https://leetcode.com/problems/high-access-employees/

use std::collections::HashMap;

impl Solution {
    pub fn find_high_access_employees(access_times: Vec<Vec<String>>) -> Vec<String> {
        let mut m: HashMap<String, Vec<i32>> = HashMap::new();
        for a in access_times {
            let name = a[0].clone();
            let t = a[1].as_bytes();
            let hh = (t[0] - b'0') as i32 * 10 + (t[1] - b'0') as i32;
            let mm = (t[2] - b'0') as i32 * 10 + (t[3] - b'0') as i32;
            m.entry(name).or_default().push(hh * 60 + mm);
        }
        let mut ans = Vec::new();
        for (name, times) in m.iter_mut() {
            times.sort_unstable();
            for i in 0..times.len().saturating_sub(2) {
                if times[i + 2] - times[i] < 60 {
                    ans.push(name.clone());
                    break;
                }
            }
        }
        ans.sort();
        ans
    }
}
''')

add("2934_minimum_operations_to_maximize_last_elements_in_arrays", r'''
// LeetCode 2934 - Minimum Operations to Maximize Last Elements in Arrays
// https://leetcode.com/problems/minimum-operations-to-maximize-last-elements-in-arrays/

impl Solution {
    pub fn min_operations(mut nums1: Vec<i32>, mut nums2: Vec<i32>) -> i32 {
        let n = nums1.len();
        let calc = |a1: &[i32], a2: &[i32]| -> i32 {
            let mut ops = 0;
            let last1 = a1[n - 1];
            let last2 = a2[n - 1];
            for i in 0..n - 1 {
                let x = a1[i];
                let y = a2[i];
                if x <= last1 && y <= last2 {
                    continue;
                }
                if y <= last1 && x <= last2 {
                    ops += 1;
                    continue;
                }
                return 1 << 30;
            }
            ops
        };
        let mut ans = calc(&nums1, &nums2);
        let tmp = nums1[n - 1];
        nums1[n - 1] = nums2[n - 1];
        nums2[n - 1] = tmp;
        let cand = calc(&nums1, &nums2) + 1;
        if cand < ans {
            ans = cand;
        }
        if ans >= (1 << 30) { -1 } else { ans }
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
    print("batch_d", n)

if __name__ == "__main__":
    main()

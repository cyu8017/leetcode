#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
FILES = {}

FILES["3199_count_triplets_with_even_xor_set_bits_i"] = r'''// LeetCode 3199 - Count Triplets with Even XOR Set Bits I
// https://leetcode.com/problems/count-triplets-with-even-xor-set-bits-i/

impl Solution {
    pub fn triplet_count(a: Vec<i32>, b: Vec<i32>, c: Vec<i32>) -> i32 {
        let mut cnt1 = [0; 2];
        let mut cnt2 = [0; 2];
        let mut cnt3 = [0; 2];
        for x in a {
            cnt1[(x.count_ones() % 2) as usize] += 1;
        }
        for x in b {
            cnt2[(x.count_ones() % 2) as usize] += 1;
        }
        for x in c {
            cnt3[(x.count_ones() % 2) as usize] += 1;
        }
        let mut ans = 0;
        for i in 0..2 {
            for j in 0..2 {
                for k in 0..2 {
                    if (i + j + k) % 2 == 0 {
                        ans += cnt1[i] * cnt2[j] * cnt3[k];
                    }
                }
            }
        }
        ans
    }
}
'''

FILES["3200_maximum_height_of_a_triangle"] = r'''// LeetCode 3200 - Maximum Height of a Triangle
// https://leetcode.com/problems/maximum-height-of-a-triangle/

impl Solution {
    pub fn max_height_of_triangle(red: i32, blue: i32) -> i32 {
        let mut ans = 0;
        for k in 0..2 {
            let mut c = [red, blue];
            let mut j = k;
            let mut i = 1;
            while i <= c[j] {
                c[j] -= i;
                ans = ans.max(i);
                i += 1;
                j ^= 1;
            }
        }
        ans
    }
}
'''

FILES["3201_find_the_maximum_length_of_valid_subsequence_i"] = r'''// LeetCode 3201 - Find the Maximum Length of Valid Subsequence I
// https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-i/

impl Solution {
    pub fn maximum_length(nums: Vec<i32>) -> i32 {
        let k = 2;
        let mut f = vec![vec![0; k]; k];
        let mut ans = 0;
        for mut x in nums {
            x %= k as i32;
            let x = x as usize;
            for j in 0..k {
                let y = (j + k - x) % k;
                f[x][y] = f[y][x] + 1;
                ans = ans.max(f[x][y]);
            }
        }
        ans
    }
}
'''

FILES["3202_find_the_maximum_length_of_valid_subsequence_ii"] = r'''// LeetCode 3202 - Find the Maximum Length of Valid Subsequence II
// https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-ii/

impl Solution {
    pub fn maximum_length(nums: Vec<i32>, k: i32) -> i32 {
        let k = k as usize;
        let mut f = vec![vec![0; k]; k];
        let mut ans = 0;
        for mut x in nums {
            x %= k as i32;
            let x = x as usize;
            for j in 0..k {
                let y = (j + k - x) % k;
                f[x][y] = f[y][x] + 1;
                ans = ans.max(f[x][y]);
            }
        }
        ans
    }
}
'''

FILES["3203_find_minimum_diameter_after_merging_two_trees"] = r'''// LeetCode 3203 - Find Minimum Diameter After Merging Two Trees
// https://leetcode.com/problems/find-minimum-diameter-after-merging-two-trees/

impl Solution {
    fn tree_diameter(edges: &[Vec<i32>]) -> i32 {
        let n = edges.len() + 1;
        let mut g = vec![Vec::new(); n];
        for e in edges {
            g[e[0] as usize].push(e[1] as usize);
            g[e[1] as usize].push(e[0] as usize);
        }
        let mut ans = 0;
        let mut a = 0;
        fn dfs(i: usize, fa: i32, t: i32, g: &[Vec<usize>], ans: &mut i32, a: &mut usize) {
            for &j in &g[i] {
                if j as i32 != fa {
                    dfs(j, i as i32, t + 1, g, ans, a);
                }
            }
            if *ans < t {
                *ans = t;
                *a = i;
            }
        }
        dfs(0, -1, 0, &g, &mut ans, &mut a);
        dfs(a, -1, 0, &g, &mut ans, &mut a);
        ans
    }

    pub fn minimum_diameter_after_merge(edges1: Vec<Vec<i32>>, edges2: Vec<Vec<i32>>) -> i32 {
        let d1 = Self::tree_diameter(&edges1);
        let d2 = Self::tree_diameter(&edges2);
        d1.max(d2).max((d1 + 1) / 2 + (d2 + 1) / 2 + 1)
    }
}
'''

FILES["3205_maximum_array_hopping_score_i"] = r'''// LeetCode 3205 - Maximum Array Hopping Score I
// https://leetcode.com/problems/maximum-array-hopping-score-i/

impl Solution {
    pub fn max_score(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut f = vec![0; n];
        fn dfs(i: usize, nums: &[i32], f: &mut [i32]) -> i32 {
            if f[i] > 0 {
                return f[i];
            }
            for j in i + 1..nums.len() {
                f[i] = f[i].max((j - i) as i32 * nums[j] + dfs(j, nums, f));
            }
            f[i]
        }
        dfs(0, &nums, &mut f)
    }
}
'''

FILES["3206_alternating_groups_i"] = r'''// LeetCode 3206 - Alternating Groups I
// https://leetcode.com/problems/alternating-groups-i/

impl Solution {
    pub fn number_of_alternating_groups(colors: Vec<i32>) -> i32 {
        let k = 3;
        let n = colors.len();
        let mut cnt = 0;
        let mut ans = 0;
        for i in 0..n * 2 {
            if i > 0 && colors[i % n] == colors[(i - 1) % n] {
                cnt = 1;
            } else {
                cnt += 1;
            }
            if i >= n && cnt >= k {
                ans += 1;
            }
        }
        ans
    }
}
'''

FILES["3207_maximum_points_after_enemy_battles"] = r'''// LeetCode 3207 - Maximum Points After Enemy Battles
// https://leetcode.com/problems/maximum-points-after-enemy-battles/

impl Solution {
    pub fn maximum_points(mut enemy_energies: Vec<i32>, mut current_energy: i32) -> i64 {
        enemy_energies.sort_unstable();
        if current_energy < enemy_energies[0] {
            return 0;
        }
        let mut ans = 0i64;
        for i in (0..enemy_energies.len()).rev() {
            ans += (current_energy / enemy_energies[0]) as i64;
            current_energy %= enemy_energies[0];
            current_energy += enemy_energies[i];
        }
        ans
    }
}
'''

FILES["3208_alternating_groups_ii"] = r'''// LeetCode 3208 - Alternating Groups II
// https://leetcode.com/problems/alternating-groups-ii/

impl Solution {
    pub fn number_of_alternating_groups(colors: Vec<i32>, k: i32) -> i32 {
        let n = colors.len();
        let mut cnt = 0;
        let mut ans = 0;
        for i in 0..n * 2 {
            if i > 0 && colors[i % n] == colors[(i - 1) % n] {
                cnt = 1;
            } else {
                cnt += 1;
            }
            if i >= n && cnt >= k {
                ans += 1;
            }
        }
        ans
    }
}
'''

FILES["3209_number_of_subarrays_with_and_value_of_k"] = r'''// LeetCode 3209 - Number of Subarrays With AND Value of K
// https://leetcode.com/problems/number-of-subarrays-with-and-value-of-k/

use std::collections::HashMap;

impl Solution {
    pub fn count_subarrays(nums: Vec<i32>, k: i32) -> i64 {
        let mut pre: HashMap<i32, i64> = HashMap::new();
        let mut ans = 0i64;
        for x in nums {
            let mut cur: HashMap<i32, i64> = HashMap::new();
            for (&y, &v) in &pre {
                *cur.entry(x & y).or_insert(0) += v;
            }
            *cur.entry(x).or_insert(0) += 1;
            ans += *cur.get(&k).unwrap_or(&0);
            pre = cur;
        }
        ans
    }
}
'''

FILES["3210_find_the_encrypted_string"] = r'''// LeetCode 3210 - Find the Encrypted String
// https://leetcode.com/problems/find-the-encrypted-string/

impl Solution {
    pub fn get_encrypted_string(s: String, k: i32) -> String {
        let n = s.len();
        let b = s.as_bytes();
        let mut cs = vec![0u8; n];
        for i in 0..n {
            cs[i] = b[(i + k as usize) % n];
        }
        String::from_utf8(cs).unwrap()
    }
}
'''

FILES["3211_generate_binary_strings_without_adjacent_zeros"] = r'''// LeetCode 3211 - Generate Binary Strings Without Adjacent Zeros
// https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/

impl Solution {
    pub fn valid_strings(n: i32) -> Vec<String> {
        let n = n as usize;
        let mut ans = Vec::new();
        let mut t = String::new();
        fn dfs(i: usize, n: usize, t: &mut String, ans: &mut Vec<String>) {
            if i >= n {
                ans.push(t.clone());
                return;
            }
            for j in 0..2 {
                if (j == 0 && (i == 0 || t.as_bytes()[i - 1] == b'1')) || j == 1 {
                    t.push(char::from(b'0' + j as u8));
                    dfs(i + 1, n, t, ans);
                    t.pop();
                }
            }
        }
        dfs(0, n, &mut t, &mut ans);
        ans
    }
}
'''

FILES["3212_count_submatrices_with_equal_frequency_of_x_and_y"] = r'''// LeetCode 3212 - Count Submatrices With Equal Frequency of X and Y
// https://leetcode.com/problems/count-submatrices-with-equal-frequency-of-x-and-y/

impl Solution {
    pub fn number_of_submatrices(grid: Vec<Vec<char>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        let mut s = vec![vec![[0; 2]; n + 1]; m + 1];
        let mut ans = 0;
        for i in 1..=m {
            for j in 1..=n {
                s[i][j][0] = s[i - 1][j][0] + s[i][j - 1][0] - s[i - 1][j - 1][0];
                if grid[i - 1][j - 1] == 'X' {
                    s[i][j][0] += 1;
                }
                s[i][j][1] = s[i - 1][j][1] + s[i][j - 1][1] - s[i - 1][j - 1][1];
                if grid[i - 1][j - 1] == 'Y' {
                    s[i][j][1] += 1;
                }
                if s[i][j][0] > 0 && s[i][j][0] == s[i][j][1] {
                    ans += 1;
                }
            }
        }
        ans
    }
}
'''

FILES["3213_construct_string_with_minimum_cost"] = r'''// LeetCode 3213 - Construct String with Minimum Cost
// https://leetcode.com/problems/construct-string-with-minimum-cost/

use std::collections::{HashMap, HashSet};

impl Solution {
    pub fn minimum_cost(target: String, words: Vec<String>, costs: Vec<i32>) -> i32 {
        const BASE: i64 = 13331;
        const MOD: i64 = 998244353;
        const INF: i32 = i32::MAX / 2;
        let n = target.len();
        let tb = target.as_bytes();
        let mut p = vec![0i64; n + 1];
        let mut h = vec![0i64; n + 1];
        p[0] = 1;
        for i in 1..=n {
            p[i] = p[i - 1] * BASE % MOD;
            h[i] = (h[i - 1] * BASE + tb[i - 1] as i64) % MOD;
        }
        let query = |l: usize, r: usize| -> i64 {
            (h[r] - h[l - 1] * p[r - l + 1] % MOD + MOD) % MOD
        };
        let mut f = vec![INF; n + 1];
        f[0] = 0;
        let mut ss: HashSet<usize> = HashSet::new();
        for w in &words {
            ss.insert(w.len());
        }
        let mut lengths: Vec<usize> = ss.into_iter().collect();
        lengths.sort_unstable();
        let mut d: HashMap<i64, i32> = HashMap::new();
        for (i, w) in words.iter().enumerate() {
            let mut x = 0i64;
            for &c in w.as_bytes() {
                x = (x * BASE + c as i64) % MOD;
            }
            let e = d.entry(x).or_insert(INF);
            if costs[i] < *e {
                *e = costs[i];
            }
        }
        for i in 1..=n {
            for &j in &lengths {
                if j > i {
                    break;
                }
                let x = query(i - j + 1, i);
                if let Some(&c) = d.get(&x) {
                    f[i] = f[i].min(f[i - j] + c);
                }
            }
        }
        if f[n] >= INF { -1 } else { f[n] }
    }
}
'''

FILES["3215_count_triplets_with_even_xor_set_bits_ii"] = r'''// LeetCode 3215 - Count Triplets with Even XOR Set Bits II
// https://leetcode.com/problems/count-triplets-with-even-xor-set-bits-ii/

impl Solution {
    pub fn triplet_count(a: Vec<i32>, b: Vec<i32>, c: Vec<i32>) -> i64 {
        let mut cnt1 = [0i64; 2];
        let mut cnt2 = [0i64; 2];
        let mut cnt3 = [0i64; 2];
        for x in a {
            cnt1[(x.count_ones() % 2) as usize] += 1;
        }
        for x in b {
            cnt2[(x.count_ones() % 2) as usize] += 1;
        }
        for x in c {
            cnt3[(x.count_ones() % 2) as usize] += 1;
        }
        let mut ans = 0i64;
        for i in 0..2 {
            for j in 0..2 {
                for k in 0..2 {
                    if (i + j + k) % 2 == 0 {
                        ans += cnt1[i] * cnt2[j] * cnt3[k];
                    }
                }
            }
        }
        ans
    }
}
'''

FILES["3216_lexicographically_smallest_string_after_a_swap"] = r'''// LeetCode 3216 - Lexicographically Smallest String After a Swap
// https://leetcode.com/problems/lexicographically-smallest-string-after-a-swap/

impl Solution {
    pub fn get_smallest_string(s: String) -> String {
        let mut b = s.into_bytes();
        let n = b.len();
        for i in 1..n {
            let a = b[i - 1];
            let c = b[i];
            if a > c && a % 2 == c % 2 {
                b.swap(i - 1, i);
                return String::from_utf8(b).unwrap();
            }
        }
        String::from_utf8(b).unwrap()
    }
}
'''

FILES["3217_delete_nodes_from_linked_list_present_in_array"] = r'''// LeetCode 3217 - Delete Nodes From Linked List Present in Array
// https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/

use std::collections::HashSet;

#[derive(PartialEq, Eq, Clone, Debug)]
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

impl Solution {
    pub fn modified_list(nums: Vec<i32>, mut head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let s: HashSet<i32> = nums.into_iter().collect();
        let mut dummy = ListNode { val: 0, next: None };
        let mut tail = &mut dummy;
        while let Some(mut node) = head {
            head = node.next.take();
            if !s.contains(&node.val) {
                tail.next = Some(node);
                tail = tail.next.as_mut().unwrap();
            }
        }
        dummy.next
    }
}
'''

FILES["3218_minimum_cost_for_cutting_cake_i"] = r'''// LeetCode 3218 - Minimum Cost for Cutting Cake I
// https://leetcode.com/problems/minimum-cost-for-cutting-cake-i/

impl Solution {
    pub fn minimum_cost(m: i32, n: i32, mut horizontal_cut: Vec<i32>, mut vertical_cut: Vec<i32>) -> i32 {
        horizontal_cut.sort_unstable_by(|a, b| b.cmp(a));
        vertical_cut.sort_unstable_by(|a, b| b.cmp(a));
        let mut i = 0;
        let mut j = 0;
        let mut h = 1;
        let mut v = 1;
        let mut ans = 0;
        while i < m - 1 || j < n - 1 {
            if j == n - 1 || (i < m - 1 && horizontal_cut[i as usize] > vertical_cut[j as usize]) {
                ans += horizontal_cut[i as usize] * v;
                h += 1;
                i += 1;
            } else {
                ans += vertical_cut[j as usize] * h;
                v += 1;
                j += 1;
            }
        }
        ans
    }
}
'''

FILES["3219_minimum_cost_for_cutting_cake_ii"] = r'''// LeetCode 3219 - Minimum Cost for Cutting Cake II
// https://leetcode.com/problems/minimum-cost-for-cutting-cake-ii/

impl Solution {
    pub fn minimum_cost(m: i32, n: i32, mut horizontal_cut: Vec<i32>, mut vertical_cut: Vec<i32>) -> i64 {
        horizontal_cut.sort_unstable_by(|a, b| b.cmp(a));
        vertical_cut.sort_unstable_by(|a, b| b.cmp(a));
        let mut i = 0;
        let mut j = 0;
        let mut h = 1i64;
        let mut v = 1i64;
        let mut ans = 0i64;
        while i < m - 1 || j < n - 1 {
            if j == n - 1 || (i < m - 1 && horizontal_cut[i as usize] > vertical_cut[j as usize]) {
                ans += horizontal_cut[i as usize] as i64 * v;
                h += 1;
                i += 1;
            } else {
                ans += vertical_cut[j as usize] as i64 * h;
                v += 1;
                j += 1;
            }
        }
        ans
    }
}
'''

FILES["3221_maximum_array_hopping_score_ii"] = r'''// LeetCode 3221 - Maximum Array Hopping Score II
// https://leetcode.com/problems/maximum-array-hopping-score-ii/

impl Solution {
    pub fn max_score(nums: Vec<i32>) -> i64 {
        let mut stk = Vec::new();
        for i in 0..nums.len() {
            while !stk.is_empty() && nums[*stk.last().unwrap()] <= nums[i] {
                stk.pop();
            }
            stk.push(i);
        }
        let mut ans = 0i64;
        let mut i = 0;
        for j in stk {
            ans += (j - i) as i64 * nums[j] as i64;
            i = j;
        }
        ans
    }
}
'''

FILES["3222_find_the_winning_player_in_coin_game"] = r'''// LeetCode 3222 - Find the Winning Player in Coin Game
// https://leetcode.com/problems/find-the-winning-player-in-coin-game/

impl Solution {
    pub fn winning_player(x: i32, y: i32) -> String {
        let k = (x / 2).min(y / 8);
        let x = x - 2 * k;
        let y = y - 8 * k;
        if x > 0 && y >= 4 {
            "Alice".to_string()
        } else {
            "Bob".to_string()
        }
    }
}
'''

FILES["3223_minimum_length_of_string_after_operations"] = r'''// LeetCode 3223 - Minimum Length of String After Operations
// https://leetcode.com/problems/minimum-length-of-string-after-operations/

impl Solution {
    pub fn minimum_length(s: String) -> i32 {
        let mut cnt = [0; 26];
        for c in s.bytes() {
            cnt[(c - b'a') as usize] += 1;
        }
        let mut ans = 0;
        for x in cnt {
            if x > 0 {
                ans += if x & 1 == 1 { 1 } else { 2 };
            }
        }
        ans
    }
}
'''

FILES["3224_minimum_array_changes_to_make_differences_equal"] = r'''// LeetCode 3224 - Minimum Array Changes to Make Differences Equal
// https://leetcode.com/problems/minimum-array-changes-to-make-differences-equal/

impl Solution {
    pub fn min_changes(nums: Vec<i32>, k: i32) -> i32 {
        let mut d = vec![0; (k + 2) as usize];
        let n = nums.len();
        for i in 0..n / 2 {
            let mut x = nums[i];
            let mut y = nums[n - 1 - i];
            if x > y {
                std::mem::swap(&mut x, &mut y);
            }
            d[0] += 1;
            d[(y - x) as usize] -= 1;
            d[(y - x + 1) as usize] += 1;
            let mx = y.max(k - x);
            d[(mx + 1) as usize] -= 1;
            d[(mx + 1) as usize] += 2;
        }
        let mut ans = n as i32;
        let mut s = 0;
        for x in d {
            s += x;
            ans = ans.min(s);
        }
        ans
    }
}
'''

FILES["3225_maximum_score_from_grid_operations"] = r'''// LeetCode 3225 - Maximum Score From Grid Operations
// https://leetcode.com/problems/maximum-score-from-grid-operations/

impl Solution {
    pub fn maximum_score(grid: Vec<Vec<i32>>) -> i64 {
        let n = grid.len();
        let mut prefix = vec![vec![0i64; n + 1]; n];
        for j in 0..n {
            for i in 0..n {
                prefix[j][i + 1] = prefix[j][i] + grid[i][j] as i64;
            }
        }
        let mut prev_pick = vec![0i64; n + 1];
        let mut prev_skip = vec![0i64; n + 1];
        for j in 1..n {
            let mut curr_pick = vec![0i64; n + 1];
            let mut curr_skip = vec![0i64; n + 1];
            for curr in 0..=n {
                for prev in 0..=n {
                    if curr > prev {
                        let score = prefix[j - 1][curr] - prefix[j - 1][prev];
                        curr_pick[curr] = curr_pick[curr].max(prev_skip[prev] + score);
                        curr_skip[curr] = curr_skip[curr].max(prev_skip[prev] + score);
                    } else {
                        let score = prefix[j][prev] - prefix[j][curr];
                        curr_pick[curr] = curr_pick[curr].max(prev_pick[prev] + score);
                        curr_skip[curr] = curr_skip[curr].max(prev_pick[prev]);
                    }
                }
            }
            prev_pick = curr_pick;
            prev_skip = curr_skip;
        }
        *prev_pick.iter().max().unwrap()
    }
}
'''

FILES["3226_number_of_bit_changes_to_make_two_integers_equal"] = r'''// LeetCode 3226 - Number of Bit Changes to Make Two Integers Equal
// https://leetcode.com/problems/number-of-bit-changes-to-make-two-integers-equal/

impl Solution {
    pub fn min_changes(n: i32, k: i32) -> i32 {
        if (n & k) != k {
            return -1;
        }
        (n ^ k).count_ones() as i32
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

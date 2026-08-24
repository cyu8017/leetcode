#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")

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

FILES = {}

FILES["2195_append_k_integers_with_minimal_sum"] = r'''// LeetCode 2195 - Append K Integers With Minimal Sum
// https://leetcode.com/problems/append-k-integers-with-minimal-sum/

impl Solution {
    pub fn minimal_k_sum(mut nums: Vec<i32>, mut k: i32) -> i64 {
        nums.sort_unstable();
        let mut ans: i64 = 0;
        let mut prev = 0i32;
        for x in nums {
            if x <= prev {
                continue;
            }
            let start = prev + 1;
            let mut end = x - 1;
            if start <= end {
                let mut cnt = end - start + 1;
                if cnt > k {
                    end = start + k - 1;
                    cnt = k;
                }
                ans += (start as i64 + end as i64) * cnt as i64 / 2;
                k -= cnt;
                if k == 0 {
                    return ans;
                }
            }
            prev = x;
        }
        let start = prev as i64 + 1;
        let end = start + k as i64 - 1;
        ans += (start + end) * k as i64 / 2;
        ans
    }
}
'''

FILES["2196_create_binary_tree_from_descriptions"] = f'''// LeetCode 2196 - Create Binary Tree From Descriptions
// https://leetcode.com/problems/create-binary-tree-from-descriptions/

use std::collections::{{HashMap, HashSet}};
{TREE}
impl Solution {{
    pub fn create_binary_tree(descriptions: Vec<Vec<i32>>) -> Option<Rc<RefCell<TreeNode>>> {{
        let mut nodes: HashMap<i32, Rc<RefCell<TreeNode>>> = HashMap::new();
        let mut child = HashSet::new();
        for d in descriptions {{
            let (p, c, is_left) = (d[0], d[1], d[2]);
            nodes.entry(p).or_insert_with(|| Rc::new(RefCell::new(TreeNode::new(p))));
            nodes.entry(c).or_insert_with(|| Rc::new(RefCell::new(TreeNode::new(c))));
            let parent = nodes.get(&p).unwrap().clone();
            let ch = nodes.get(&c).unwrap().clone();
            if is_left == 1 {{
                parent.borrow_mut().left = Some(ch);
            }} else {{
                parent.borrow_mut().right = Some(ch);
            }}
            child.insert(c);
        }}
        for (v, node) in nodes {{
            if !child.contains(&v) {{
                return Some(node);
            }}
        }}
        None
    }}
}}
'''

FILES["2197_replace_non_coprime_numbers_in_array"] = r'''// LeetCode 2197 - Replace Non-Coprime Numbers in Array
// https://leetcode.com/problems/replace-non-coprime-numbers-in-array/

impl Solution {
    pub fn replace_non_coprimes(nums: Vec<i32>) -> Vec<i32> {
        fn gcd(mut a: i64, mut b: i64) -> i64 {
            while b != 0 {
                let t = a % b;
                a = b;
                b = t;
            }
            a
        }
        let mut stack: Vec<i64> = Vec::new();
        for x0 in nums {
            let mut x = x0 as i64;
            while let Some(&last) = stack.last() {
                let g = gcd(last, x);
                if g == 1 {
                    break;
                }
                x = last / g * x;
                stack.pop();
            }
            stack.push(x);
        }
        stack.into_iter().map(|x| x as i32).collect()
    }
}
'''

FILES["2198_number_of_single_divisor_triplets"] = r'''// LeetCode 2198 - Number of Single Divisor Triplets
// https://leetcode.com/problems/number-of-single-divisor-triplets/

impl Solution {
    pub fn single_divisor_triplet(nums: Vec<i32>) -> i64 {
        let mut freq = [0i64; 101];
        for x in nums {
            freq[x as usize] += 1;
        }
        let mut ans = 0i64;
        for a in 1..=100 {
            if freq[a] == 0 {
                continue;
            }
            for b in a..=100 {
                if freq[b] == 0 {
                    continue;
                }
                for c in b..=100 {
                    if freq[c] == 0 {
                        continue;
                    }
                    let s = a + b + c;
                    let mut cnt = 0;
                    if s % a == 0 {
                        cnt += 1;
                    }
                    if s % b == 0 {
                        cnt += 1;
                    }
                    if s % c == 0 {
                        cnt += 1;
                    }
                    if cnt != 1 {
                        continue;
                    }
                    if a == b && b == c {
                        ans += freq[a] * (freq[a] - 1) * (freq[a] - 2);
                    } else if a == b {
                        ans += freq[a] * (freq[a] - 1) * freq[c] * 3;
                    } else if b == c {
                        ans += freq[b] * (freq[b] - 1) * freq[a] * 3;
                    } else if a == c {
                        ans += freq[a] * (freq[a] - 1) * freq[b] * 3;
                    } else {
                        ans += freq[a] * freq[b] * freq[c] * 6;
                    }
                }
            }
        }
        ans
    }
}
'''

FILES["2200_find_all_k_distant_indices_in_an_array"] = r'''// LeetCode 2200 - Find All K-Distant Indices in an Array
// https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/

impl Solution {
    pub fn find_k_distant_indices(nums: Vec<i32>, key: i32, k: i32) -> Vec<i32> {
        let n = nums.len() as i32;
        let mut mark = vec![false; n as usize];
        for i in 0..n {
            if nums[i as usize] == key {
                let l = 0.max(i - k);
                let r = (n - 1).min(i + k);
                for j in l..=r {
                    mark[j as usize] = true;
                }
            }
        }
        (0..n).filter(|&i| mark[i as usize]).collect()
    }
}
'''

FILES["2201_count_artifacts_that_can_be_extracted"] = r'''// LeetCode 2201 - Count Artifacts That Can Be Extracted
// https://leetcode.com/problems/count-artifacts-that-can-be-extracted/

use std::collections::HashSet;

impl Solution {
    pub fn dig_artifacts(n: i32, artifacts: Vec<Vec<i32>>, dig: Vec<Vec<i32>>) -> i32 {
        let _ = n;
        let dug: HashSet<(i32, i32)> = dig.into_iter().map(|d| (d[0], d[1])).collect();
        let mut ans = 0;
        for a in artifacts {
            let mut ok = true;
            for r in a[0]..=a[2] {
                for c in a[1]..=a[3] {
                    if !dug.contains(&(r, c)) {
                        ok = false;
                    }
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

FILES["2202_maximize_the_topmost_element_after_k_moves"] = r'''// LeetCode 2202 - Maximize the Topmost Element After K Moves
// https://leetcode.com/problems/maximize-the-topmost-element-after-k-moves/

impl Solution {
    pub fn maximum_top(nums: Vec<i32>, k: i32) -> i32 {
        let n = nums.len() as i32;
        if n == 1 {
            return if k % 2 == 1 { -1 } else { nums[0] };
        }
        if k == 0 {
            return nums[0];
        }
        let mut ans = -1;
        let limit = (k - 1).min(n);
        for i in 0..limit {
            ans = ans.max(nums[i as usize]);
        }
        if k < n {
            ans = ans.max(nums[k as usize]);
        }
        ans
    }
}
'''

FILES["2203_minimum_weighted_subgraph_with_the_required_paths"] = r'''// LeetCode 2203 - Minimum Weighted Subgraph With the Required Paths
// https://leetcode.com/problems/minimum-weighted-subgraph-with-the-required-paths/

use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    fn dijkstra(n: usize, g: &[Vec<(usize, i32)>], src: usize) -> Vec<i64> {
        const INF: i64 = 1i64 << 62;
        let mut dist = vec![INF; n];
        dist[src] = 0;
        let mut pq = BinaryHeap::new();
        pq.push(Reverse((0i64, src)));
        while let Some(Reverse((d, u))) = pq.pop() {
            if d != dist[u] {
                continue;
            }
            for &(v, w) in &g[u] {
                if d + w as i64 < dist[v] {
                    dist[v] = d + w as i64;
                    pq.push(Reverse((dist[v], v)));
                }
            }
        }
        dist
    }

    pub fn minimum_weight(n: i32, edges: Vec<Vec<i32>>, src1: i32, src2: i32, dest: i32) -> i64 {
        let n = n as usize;
        let mut g = vec![Vec::new(); n];
        let mut rg = vec![Vec::new(); n];
        for e in edges {
            g[e[0] as usize].push((e[1] as usize, e[2]));
            rg[e[1] as usize].push((e[0] as usize, e[2]));
        }
        let d1 = Self::dijkstra(n, &g, src1 as usize);
        let d2 = Self::dijkstra(n, &g, src2 as usize);
        let dd = Self::dijkstra(n, &rg, dest as usize);
        const INF: i64 = 1i64 << 62;
        let mut ans = INF;
        for i in 0..n {
            if d1[i] >= INF || d2[i] >= INF || dd[i] >= INF {
                continue;
            }
            ans = ans.min(d1[i] + d2[i] + dd[i]);
        }
        if ans >= INF { -1 } else { ans }
    }
}
'''

FILES["2204_distance_to_a_cycle_in_undirected_graph"] = r'''// LeetCode 2204 - Distance to a Cycle in Undirected Graph
// https://leetcode.com/problems/distance-to-a-cycle-in-undirected-graph/

use std::collections::VecDeque;

impl Solution {
    pub fn distance_to_cycle(n: i32, edges: Vec<Vec<i32>>) -> Vec<i32> {
        let n = n as usize;
        let mut g = vec![Vec::new(); n];
        let mut deg = vec![0; n];
        for e in edges {
            let (a, b) = (e[0] as usize, e[1] as usize);
            g[a].push(b);
            g[b].push(a);
            deg[a] += 1;
            deg[b] += 1;
        }
        let mut q = VecDeque::new();
        for i in 0..n {
            if deg[i] == 1 {
                q.push_back(i);
            }
        }
        let mut on_cycle = vec![true; n];
        while let Some(u) = q.pop_front() {
            on_cycle[u] = false;
            for &v in &g[u] {
                deg[v] -= 1;
                if deg[v] == 1 {
                    q.push_back(v);
                }
            }
        }
        let mut ans = vec![-1; n];
        let mut qq = VecDeque::new();
        for i in 0..n {
            if on_cycle[i] {
                ans[i] = 0;
                qq.push_back(i);
            }
        }
        while let Some(u) = qq.pop_front() {
            for &v in &g[u] {
                if ans[v] == -1 {
                    ans[v] = ans[u] + 1;
                    qq.push_back(v);
                }
            }
        }
        ans
    }
}
'''

FILES["2205_the_number_of_users_that_are_eligible_for_discount"] = r'''// LeetCode 2205 - The Number of Users That Are Eligible for Discount
// https://leetcode.com/problems/the-number-of-users-that-are-eligible-for-discount/

const QUERY: &str = r#"
CREATE FUNCTION getUserIDs(startDate DATE, endDate DATE, minAmount INT) RETURNS INT
READS SQL DATA
BEGIN
  RETURN (
    SELECT COUNT(DISTINCT user_id) AS user_cnt
    FROM Purchases
    WHERE time_stamp BETWEEN startDate AND endDate
      AND amount >= minAmount
  );
END
"#;
'''

FILES["2206_divide_array_into_equal_pairs"] = r'''// LeetCode 2206 - Divide Array Into Equal Pairs
// https://leetcode.com/problems/divide-array-into-equal-pairs/

use std::collections::HashMap;

impl Solution {
    pub fn divide_array(nums: Vec<i32>) -> bool {
        let mut freq = HashMap::new();
        for x in nums {
            *freq.entry(x).or_insert(0) += 1;
        }
        freq.values().all(|&c| c % 2 == 0)
    }
}
'''

FILES["2207_maximize_number_of_subsequences_in_a_string"] = r'''// LeetCode 2207 - Maximize Number of Subsequences in a String
// https://leetcode.com/problems/maximize-number-of-subsequences-in-a-string/

impl Solution {
    pub fn maximum_subsequence_count(text: String, pattern: String) -> i64 {
        let pb: Vec<u8> = pattern.bytes().collect();
        let a = pb[0];
        let b = pb[1];
        let count = |s: &[u8]| {
            let mut ca = 0i64;
            let mut ans = 0i64;
            for &c in s {
                if c == b {
                    ans += ca;
                }
                if c == a {
                    ca += 1;
                }
            }
            ans
        };
        let mut s1 = vec![a];
        s1.extend(text.bytes());
        let mut s2 = text.into_bytes();
        s2.push(b);
        count(&s1).max(count(&s2))
    }
}
'''

FILES["2208_minimum_operations_to_halve_array_sum"] = r'''// LeetCode 2208 - Minimum Operations to Halve Array Sum
// https://leetcode.com/problems/minimum-operations-to-halve-array-sum/

use std::collections::BinaryHeap;

impl Solution {
    pub fn halve_array(nums: Vec<i32>) -> i32 {
        let mut h = BinaryHeap::new();
        let mut sum = 0.0f64;
        for x in nums {
            h.push(ordered_float(x as f64));
            sum += x as f64;
        }
        let target = sum / 2.0;
        let mut ans = 0;
        while sum > target {
            let x = h.pop().unwrap().0 / 2.0;
            sum -= x;
            h.push(ordered_float(x));
            ans += 1;
        }
        ans
    }
}

#[derive(Copy, Clone, PartialEq, PartialOrd)]
struct F64(f64);

impl Eq for F64 {}
impl Ord for F64 {
    fn cmp(&self, other: &Self) -> std::cmp::Ordering {
        self.0.partial_cmp(&other.0).unwrap_or(std::cmp::Ordering::Equal)
    }
}

fn ordered_float(x: f64) -> F64 {
    F64(x)
}
'''

FILES["2209_minimum_white_tiles_after_covering_with_carpets"] = r'''// LeetCode 2209 - Minimum White Tiles After Covering With Carpets
// https://leetcode.com/problems/minimum-white-tiles-after-covering-with-carpets/

impl Solution {
    pub fn minimum_white_tiles(floor: String, num_carpets: i32, carpet_len: i32) -> i32 {
        let floor = floor.into_bytes();
        let n = floor.len();
        let num_carpets = num_carpets as usize;
        let carpet_len = carpet_len as usize;
        let inf = 1 << 30;
        let mut dp = vec![vec![inf; n + 1]; num_carpets + 1];
        dp[0][0] = 0;
        for j in 1..=n {
            dp[0][j] = dp[0][j - 1] + i32::from(floor[j - 1] == b'1');
        }
        for c in 1..=num_carpets {
            dp[c][0] = 0;
            for j in 1..=n {
                dp[c][j] = dp[c][j - 1] + i32::from(floor[j - 1] == b'1');
                let start = j.saturating_sub(carpet_len);
                dp[c][j] = dp[c][j].min(dp[c - 1][start]);
            }
        }
        dp[num_carpets][n]
    }
}
'''

FILES["2210_count_hills_and_valleys_in_an_array"] = r'''// LeetCode 2210 - Count Hills and Valleys in an Array
// https://leetcode.com/problems/count-hills-and-valleys-in-an-array/

impl Solution {
    pub fn count_hill_valley(nums: Vec<i32>) -> i32 {
        let mut compact = vec![nums[0]];
        for &x in nums.iter().skip(1) {
            if x != *compact.last().unwrap() {
                compact.push(x);
            }
        }
        let mut ans = 0;
        for i in 1..compact.len().saturating_sub(1) {
            if (compact[i] > compact[i - 1] && compact[i] > compact[i + 1])
                || (compact[i] < compact[i - 1] && compact[i] < compact[i + 1])
            {
                ans += 1;
            }
        }
        ans
    }
}
'''

FILES["2211_count_collisions_on_a_road"] = r'''// LeetCode 2211 - Count Collisions on a Road
// https://leetcode.com/problems/count-collisions-on-a-road/

impl Solution {
    pub fn count_collisions(directions: String) -> i32 {
        let d = directions.as_bytes();
        let mut i = 0;
        let mut j = d.len() as i32 - 1;
        while i < d.len() && d[i] == b'L' {
            i += 1;
        }
        while j >= 0 && d[j as usize] == b'R' {
            j -= 1;
        }
        let mut ans = 0;
        if j >= i as i32 {
            for k in i..=j as usize {
                if d[k] != b'S' {
                    ans += 1;
                }
            }
        }
        ans
    }
}
'''

FILES["2212_maximum_points_in_an_archery_competition"] = r'''// LeetCode 2212 - Maximum Points in an Archery Competition
// https://leetcode.com/problems/maximum-points-in-an-archery-competition/

impl Solution {
    pub fn maximum_bob_points(num_arrows: i32, alice_arrows: Vec<i32>) -> Vec<i32> {
        let mut best_score = -1;
        let mut best = vec![0; 12];
        fn dfs(
            i: usize,
            remain: i32,
            score: i32,
            bob: &mut [i32],
            alice: &[i32],
            best_score: &mut i32,
            best: &mut [i32],
        ) {
            if i == 12 {
                if score > *best_score {
                    *best_score = score;
                    best.copy_from_slice(bob);
                    if remain > 0 {
                        best[0] += remain;
                    }
                }
                return;
            }
            dfs(i + 1, remain, score, bob, alice, best_score, best);
            let need = alice[i] + 1;
            if remain >= need {
                bob[i] = need;
                dfs(i + 1, remain - need, score + i as i32, bob, alice, best_score, best);
                bob[i] = 0;
            }
        }
        let mut bob = vec![0; 12];
        dfs(0, num_arrows, 0, &mut bob, &alice_arrows, &mut best_score, &mut best);
        best
    }
}
'''

FILES["2213_longest_substring_of_one_repeating_character"] = r'''// LeetCode 2213 - Longest Substring of One Repeating Character
// https://leetcode.com/problems/longest-substring-of-one-repeating-character/

#[derive(Clone, Copy)]
struct Seg {
    l_char: u8,
    r_char: u8,
    l_len: i32,
    r_len: i32,
    best: i32,
    size: i32,
}

impl Default for Seg {
    fn default() -> Self {
        Self {
            l_char: 0,
            r_char: 0,
            l_len: 0,
            r_len: 0,
            best: 0,
            size: 0,
        }
    }
}

impl Solution {
    fn merge(a: Seg, b: Seg) -> Seg {
        if a.size == 0 {
            return b;
        }
        if b.size == 0 {
            return a;
        }
        let mut res = Seg {
            l_char: a.l_char,
            r_char: b.r_char,
            size: a.size + b.size,
            best: a.best.max(b.best),
            l_len: a.l_len,
            r_len: b.r_len,
        };
        if a.r_char == b.l_char {
            let mid = a.r_len + b.l_len;
            res.best = res.best.max(mid);
            if a.l_len == a.size {
                res.l_len = a.size + b.l_len;
            }
            if b.r_len == b.size {
                res.r_len = b.size + a.r_len;
            }
        }
        res
    }

    fn build(tree: &mut [Seg], s: &[u8], idx: usize, l: usize, r: usize) {
        if l == r {
            tree[idx] = Seg {
                l_char: s[l],
                r_char: s[l],
                l_len: 1,
                r_len: 1,
                best: 1,
                size: 1,
            };
            return;
        }
        let mid = (l + r) / 2;
        Self::build(tree, s, idx * 2, l, mid);
        Self::build(tree, s, idx * 2 + 1, mid + 1, r);
        tree[idx] = Self::merge(tree[idx * 2], tree[idx * 2 + 1]);
    }

    fn update(tree: &mut [Seg], s: &mut [u8], idx: usize, l: usize, r: usize, pos: usize, ch: u8) {
        if l == r {
            s[pos] = ch;
            tree[idx] = Seg {
                l_char: ch,
                r_char: ch,
                l_len: 1,
                r_len: 1,
                best: 1,
                size: 1,
            };
            return;
        }
        let mid = (l + r) / 2;
        if pos <= mid {
            Self::update(tree, s, idx * 2, l, mid, pos, ch);
        } else {
            Self::update(tree, s, idx * 2 + 1, mid + 1, r, pos, ch);
        }
        tree[idx] = Self::merge(tree[idx * 2], tree[idx * 2 + 1]);
    }

    pub fn longest_repeating(s: String, query_characters: String, query_indices: Vec<i32>) -> Vec<i32> {
        let mut s = s.into_bytes();
        let n = s.len();
        let mut tree = vec![Seg::default(); 4 * n + 5];
        Self::build(&mut tree, &s, 1, 0, n - 1);
        let qc = query_characters.into_bytes();
        let mut ans = vec![0; query_indices.len()];
        for i in 0..query_indices.len() {
            Self::update(&mut tree, &mut s, 1, 0, n - 1, query_indices[i] as usize, qc[i]);
            ans[i] = tree[1].best;
        }
        ans
    }
}
'''

FILES["2214_minimum_health_to_beat_game"] = r'''// LeetCode 2214 - Minimum Health to Beat Game
// https://leetcode.com/problems/minimum-health-to-beat-game/

impl Solution {
    pub fn minimum_health(damage: Vec<i32>, armor: i32) -> i64 {
        let mut sum = 0i64;
        let mut mx = 0i32;
        for d in damage {
            sum += d as i64;
            mx = mx.max(d);
        }
        sum - armor.min(mx) as i64 + 1
    }
}
'''

FILES["2215_find_the_difference_of_two_arrays"] = r'''// LeetCode 2215 - Find the Difference of Two Arrays
// https://leetcode.com/problems/find-the-difference-of-two-arrays/

use std::collections::HashSet;

impl Solution {
    pub fn find_difference(nums1: Vec<i32>, nums2: Vec<i32>) -> Vec<Vec<i32>> {
        let s1: HashSet<i32> = nums1.into_iter().collect();
        let s2: HashSet<i32> = nums2.into_iter().collect();
        let a: Vec<i32> = s1.iter().copied().filter(|x| !s2.contains(x)).collect();
        let b: Vec<i32> = s2.iter().copied().filter(|x| !s1.contains(x)).collect();
        vec![a, b]
    }
}
'''

FILES["2216_minimum_deletions_to_make_array_beautiful"] = r'''// LeetCode 2216 - Minimum Deletions to Make Array Beautiful
// https://leetcode.com/problems/minimum-deletions-to-make-array-beautiful/

impl Solution {
    pub fn min_deletion(nums: Vec<i32>) -> i32 {
        let mut ans = 0;
        let mut i = 0;
        let n = nums.len();
        while i + 1 < n {
            if nums[i] == nums[i + 1] {
                ans += 1;
                i += 1;
            } else {
                i += 2;
            }
        }
        if (n as i32 - ans) % 2 == 1 {
            ans += 1;
        }
        ans
    }
}
'''

FILES["2217_find_palindrome_with_fixed_length"] = r'''// LeetCode 2217 - Find Palindrome With Fixed Length
// https://leetcode.com/problems/find-palindrome-with-fixed-length/

impl Solution {
    pub fn kth_palindrome(queries: Vec<i32>, int_length: i32) -> Vec<i64> {
        let half = (int_length + 1) / 2;
        let mut start = 1i32;
        for _ in 1..half {
            start *= 10;
        }
        let total = start * 9;
        let mut ans = vec![0i64; queries.len()];
        for (i, &q) in queries.iter().enumerate() {
            if q > total {
                ans[i] = -1;
                continue;
            }
            let left = start + q - 1;
            let mut pal = left as i64;
            let mut x = left;
            if int_length % 2 == 1 {
                x /= 10;
            }
            while x > 0 {
                pal = pal * 10 + (x % 10) as i64;
                x /= 10;
            }
            ans[i] = pal;
        }
        ans
    }
}
'''

FILES["2218_maximum_value_of_k_coins_from_piles"] = r'''// LeetCode 2218 - Maximum Value of K Coins From Piles
// https://leetcode.com/problems/maximum-value-of-k-coins-from-piles/

impl Solution {
    pub fn max_value_of_coins(piles: Vec<Vec<i32>>, k: i32) -> i32 {
        let k = k as usize;
        let mut dp = vec![0; k + 1];
        for pile in piles {
            let mut ndp = dp.clone();
            let mut sum = 0;
            for take in 1..=pile.len().min(k) {
                sum += pile[take - 1];
                for j in take..=k {
                    ndp[j] = ndp[j].max(dp[j - take] + sum);
                }
            }
            dp = ndp;
        }
        dp[k]
    }
}
'''

FILES["2219_maximum_sum_score_of_array"] = r'''// LeetCode 2219 - Maximum Sum Score of Array
// https://leetcode.com/problems/maximum-sum-score-of-array/

impl Solution {
    pub fn maximum_sum_score(nums: Vec<i32>) -> i64 {
        let total: i64 = nums.iter().map(|&x| x as i64).sum();
        let mut pref = 0i64;
        let mut ans = i64::MIN;
        for x in nums {
            pref += x as i64;
            ans = ans.max(pref.max(total - pref + x as i64));
        }
        ans
    }
}
'''

FILES["2220_minimum_bit_flips_to_convert_number"] = r'''// LeetCode 2220 - Minimum Bit Flips to Convert Number
// https://leetcode.com/problems/minimum-bit-flips-to-convert-number/

impl Solution {
    pub fn min_bit_flips(start: i32, goal: i32) -> i32 {
        let mut x = start ^ goal;
        let mut ans = 0;
        while x > 0 {
            ans += x & 1;
            x >>= 1;
        }
        ans
    }
}
'''

FILES["2221_find_triangular_sum_of_an_array"] = r'''// LeetCode 2221 - Find Triangular Sum of an Array
// https://leetcode.com/problems/find-triangular-sum-of-an-array/

impl Solution {
    pub fn triangular_sum(mut nums: Vec<i32>) -> i32 {
        while nums.len() > 1 {
            let next: Vec<i32> = nums.windows(2).map(|w| (w[0] + w[1]) % 10).collect();
            nums = next;
        }
        nums[0]
    }
}
'''

FILES["2222_number_of_ways_to_select_buildings"] = r'''// LeetCode 2222 - Number of Ways to Select Buildings
// https://leetcode.com/problems/number-of-ways-to-select-buildings/

impl Solution {
    pub fn number_of_ways(s: String) -> i64 {
        let bytes = s.as_bytes();
        let mut total0 = 0i32;
        let mut total1 = 0i32;
        for &c in bytes {
            if c == b'0' {
                total0 += 1;
            } else {
                total1 += 1;
            }
        }
        let mut left0 = 0i32;
        let mut left1 = 0i32;
        let mut ans = 0i64;
        for &c in bytes {
            if c == b'0' {
                ans += left1 as i64 * (total1 - left1) as i64;
                left0 += 1;
            } else {
                ans += left0 as i64 * (total0 - left0) as i64;
                left1 += 1;
            }
        }
        ans
    }
}
'''

FILES["2223_sum_of_scores_of_built_strings"] = r'''// LeetCode 2223 - Sum of Scores of Built Strings
// https://leetcode.com/problems/sum-of-scores-of-built-strings/

impl Solution {
    pub fn sum_scores(s: String) -> i64 {
        let s = s.as_bytes();
        let n = s.len();
        let mut z = vec![0; n];
        let mut l = 0;
        let mut r = 0;
        for i in 1..n {
            if i <= r {
                z[i] = z[i - l].min(r - i + 1);
            }
            while i + z[i] < n && s[z[i]] == s[i + z[i]] {
                z[i] += 1;
            }
            if i + z[i] - 1 > r {
                l = i;
                r = i + z[i] - 1;
            }
        }
        let mut ans = n as i64;
        for i in 1..n {
            ans += z[i] as i64;
        }
        ans
    }
}
'''

FILES["2224_minimum_number_of_operations_to_convert_time"] = r'''// LeetCode 2224 - Minimum Number of Operations to Convert Time
// https://leetcode.com/problems/minimum-number-of-operations-to-convert-time/

impl Solution {
    pub fn convert_time(current: String, correct: String) -> i32 {
        fn to_min(t: &str) -> i32 {
            let b = t.as_bytes();
            (b[0] - b'0') as i32 * 600
                + (b[1] - b'0') as i32 * 60
                + (b[3] - b'0') as i32 * 10
                + (b[4] - b'0') as i32
        }
        let mut diff = to_min(&correct) - to_min(&current);
        let mut ans = 0;
        for step in [60, 15, 5, 1] {
            ans += diff / step;
            diff %= step;
        }
        ans
    }
}
'''

FILES["2225_find_players_with_zero_or_one_losses"] = r'''// LeetCode 2225 - Find Players With Zero or One Losses
// https://leetcode.com/problems/find-players-with-zero-or-one-losses/

use std::collections::{HashMap, HashSet};

impl Solution {
    pub fn find_winners(matches: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let mut lose = HashMap::new();
        let mut seen = HashSet::new();
        for m in matches {
            seen.insert(m[0]);
            seen.insert(m[1]);
            *lose.entry(m[1]).or_insert(0) += 1;
        }
        let mut zero = Vec::new();
        let mut one = Vec::new();
        for p in seen {
            let l = *lose.get(&p).unwrap_or(&0);
            if l == 0 {
                zero.push(p);
            } else if l == 1 {
                one.push(p);
            }
        }
        zero.sort_unstable();
        one.sort_unstable();
        vec![zero, one]
    }
}
'''

FILES["2226_maximum_candies_allocated_to_k_children"] = r'''// LeetCode 2226 - Maximum Candies Allocated to K Children
// https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

impl Solution {
    pub fn maximum_candies(candies: Vec<i32>, k: i64) -> i32 {
        let mx = *candies.iter().max().unwrap_or(&0);
        let mut lo = 0;
        let mut hi = mx;
        let can = |mid: i32| {
            if mid == 0 {
                return true;
            }
            let mut cnt = 0i64;
            for &c in &candies {
                cnt += (c / mid) as i64;
                if cnt >= k {
                    return true;
                }
            }
            false
        };
        while lo < hi {
            let mid = (lo + hi + 1) / 2;
            if can(mid) {
                lo = mid;
            } else {
                hi = mid - 1;
            }
        }
        lo
    }
}
'''

FILES["2227_encrypt_and_decrypt_strings"] = r'''// LeetCode 2227 - Encrypt and Decrypt Strings
// https://leetcode.com/problems/encrypt-and-decrypt-strings/

use std::collections::HashMap;

pub struct Encrypter {
    enc: HashMap<char, String>,
    cnt: HashMap<String, i32>,
}

impl Encrypter {
    pub fn new(keys: Vec<char>, values: Vec<String>, dictionary: Vec<String>) -> Self {
        let mut enc = HashMap::new();
        for i in 0..keys.len() {
            enc.insert(keys[i], values[i].clone());
        }
        let mut this = Self {
            enc,
            cnt: HashMap::new(),
        };
        for w in dictionary {
            let e = this.encrypt(w);
            *this.cnt.entry(e).or_insert(0) += 1;
        }
        this
    }

    pub fn encrypt(&self, word1: String) -> String {
        let mut b = String::new();
        for c in word1.chars() {
            match self.enc.get(&c) {
                Some(v) => b.push_str(v),
                None => return String::new(),
            }
        }
        b
    }

    pub fn decrypt(&self, word2: String) -> i32 {
        *self.cnt.get(&word2).unwrap_or(&0)
    }
}
'''

FILES["2229_check_if_an_array_is_consecutive"] = r'''// LeetCode 2229 - Check if an Array Is Consecutive
// https://leetcode.com/problems/check-if-an-array-is-consecutive/

use std::collections::HashSet;

impl Solution {
    pub fn is_consecutive(nums: Vec<i32>) -> bool {
        let mut mn = nums[0];
        let mut mx = nums[0];
        let mut seen = HashSet::new();
        for x in &nums {
            if !seen.insert(*x) {
                return false;
            }
            mn = mn.min(*x);
            mx = mx.max(*x);
        }
        mx - mn + 1 == nums.len() as i32
    }
}
'''

FILES["2230_the_users_that_are_eligible_for_discount"] = r'''// LeetCode 2230 - The Users That Are Eligible for Discount
// https://leetcode.com/problems/the-users-that-are-eligible-for-discount/

const QUERY: &str = r#"
CREATE PROCEDURE getUserIDs(startDate DATE, endDate DATE, minAmount INT)
BEGIN
  SELECT DISTINCT user_id
  FROM Purchases
  WHERE time_stamp BETWEEN startDate AND endDate
    AND amount >= minAmount
  ORDER BY user_id;
END
"#;
'''

FILES["2231_largest_number_after_digit_swaps_by_parity"] = r'''// LeetCode 2231 - Largest Number After Digit Swaps by Parity
// https://leetcode.com/problems/largest-number-after-digit-swaps-by-parity/

impl Solution {
    pub fn largest_integer(num: i32) -> i32 {
        let mut digits = Vec::new();
        let mut x = num;
        if x == 0 {
            digits.push(0);
        }
        while x > 0 {
            digits.insert(0, x % 10);
            x /= 10;
        }
        let mut even: Vec<i32> = digits.iter().copied().filter(|d| d % 2 == 0).collect();
        let mut odd: Vec<i32> = digits.iter().copied().filter(|d| d % 2 != 0).collect();
        even.sort_unstable_by(|a, b| b.cmp(a));
        odd.sort_unstable_by(|a, b| b.cmp(a));
        let mut ei = 0;
        let mut oi = 0;
        let mut ans = 0;
        for d in digits {
            if d % 2 == 0 {
                ans = ans * 10 + even[ei];
                ei += 1;
            } else {
                ans = ans * 10 + odd[oi];
                oi += 1;
            }
        }
        ans
    }
}
'''

FILES["2232_minimize_result_by_adding_parentheses_to_expression"] = r'''// LeetCode 2232 - Minimize Result by Adding Parentheses to Expression
// https://leetcode.com/problems/minimize-result-by-adding-parentheses-to-expression/

impl Solution {
    pub fn minimize_result(expression: String) -> String {
        let plus = expression.find('+').unwrap();
        let left = &expression[..plus];
        let right = &expression[plus + 1..];
        let mut best_val = i32::MAX;
        let mut best = String::new();
        for i in 0..left.len() {
            for j in 1..=right.len() {
                let a = &left[..i];
                let b = &left[i..];
                let c = &right[..j];
                let d = &right[j..];
                let mut val = b.parse::<i32>().unwrap() + c.parse::<i32>().unwrap();
                if !a.is_empty() {
                    val *= a.parse::<i32>().unwrap();
                }
                if !d.is_empty() {
                    val *= d.parse::<i32>().unwrap();
                }
                if val < best_val {
                    best_val = val;
                    best = format!("{a}({b}+{c}){d}");
                }
            }
        }
        best
    }
}
'''

FILES["2233_maximum_product_after_k_increments"] = r'''// LeetCode 2233 - Maximum Product After K Increments
// https://leetcode.com/problems/maximum-product-after-k-increments/

use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn maximum_product(nums: Vec<i32>, k: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let mut h: BinaryHeap<Reverse<i32>> = nums.into_iter().map(Reverse).collect();
        for _ in 0..k {
            let x = h.pop().unwrap().0 + 1;
            h.push(Reverse(x));
        }
        let mut ans = 1i64;
        while let Some(Reverse(x)) = h.pop() {
            ans = ans * x as i64 % MOD;
        }
        ans as i32
    }
}
'''

FILES["2234_maximum_total_beauty_of_the_gardens"] = r'''// LeetCode 2234 - Maximum Total Beauty of the Gardens
// https://leetcode.com/problems/maximum-total-beauty-of-the-gardens/

impl Solution {
    pub fn maximum_beauty(mut flowers: Vec<i32>, new_flowers: i64, target: i32, full: i32, partial: i32) -> i64 {
        let n = flowers.len();
        for f in flowers.iter_mut() {
            if *f > target {
                *f = target;
            }
        }
        flowers.sort_unstable();
        let sum: i64 = flowers.iter().map(|&f| f as i64).sum();
        if target as i64 * n as i64 - sum <= new_flowers {
            return n as i64 * full as i64;
        }
        let mut pref = vec![0i64; n + 1];
        for i in 0..n {
            pref[i + 1] = pref[i] + flowers[i] as i64;
        }
        let mut ans = 0i64;
        let mut j = n as i32 - 1;
        let mut remain = new_flowers;
        for complete in 0..=n {
            if complete > 0 {
                let need = target as i64 - flowers[n - complete] as i64;
                if remain < need {
                    break;
                }
                remain -= need;
            }
            while j >= n as i32 - complete as i32
                || (j >= 0 && flowers[j as usize] as i64 * (j as i64 + 1) - pref[j as usize + 1] > remain)
            {
                j -= 1;
            }
            let mut partial_val = 0i64;
            if j >= 0 {
                let extra = (remain - (flowers[j as usize] as i64 * (j as i64 + 1) - pref[j as usize + 1]))
                    / (j as i64 + 1);
                partial_val = flowers[j as usize] as i64 + extra;
                if partial_val >= target as i64 {
                    partial_val = target as i64 - 1;
                }
            }
            ans = ans.max(complete as i64 * full as i64 + partial_val * partial as i64);
        }
        ans
    }
}
'''

FILES["2235_add_two_integers"] = r'''// LeetCode 2235 - Add Two Integers
// https://leetcode.com/problems/add-two-integers/

impl Solution {
    pub fn sum(num1: i32, num2: i32) -> i32 {
        num1 + num2
    }
}
'''

written = 0
for folder, content in FILES.items():
    path = ROOT / folder / "solution.rs"
    path.write_text(content, encoding="utf-8", newline="\n")
    if content.startswith("\ufeff"):
        raise SystemExit(f"BOM in {folder}")
    written += 1
print(f"wrote {written}")

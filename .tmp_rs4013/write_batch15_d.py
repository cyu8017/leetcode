#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
FILES = {}

FILES["3254_find_the_power_of_k_size_subarrays_i"] = r'''// LeetCode 3254 - Find the Power of K-Size Subarrays I
// https://leetcode.com/problems/find-the-power-of-k-size-subarrays-i/

impl Solution {
    pub fn results_array(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let n = nums.len();
        let k = k as usize;
        let mut ans = vec![0; n - k + 1];
        for i in 0..=n - k {
            let mut ok = true;
            for j in i + 1..i + k {
                if nums[j] != nums[j - 1] + 1 {
                    ok = false;
                    break;
                }
            }
            ans[i] = if ok { nums[i + k - 1] } else { -1 };
        }
        ans
    }
}
'''

FILES["3255_find_the_power_of_k_size_subarrays_ii"] = r'''// LeetCode 3255 - Find the Power of K-Size Subarrays II
// https://leetcode.com/problems/find-the-power-of-k-size-subarrays-ii/

impl Solution {
    pub fn results_array(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let n = nums.len();
        let k = k as usize;
        if k == 1 {
            return nums;
        }
        let mut ans = vec![0; n - k + 1];
        let mut streak = 1;
        for i in 1..n {
            if nums[i] == nums[i - 1] + 1 {
                streak += 1;
            } else {
                streak = 1;
            }
            if i >= k - 1 {
                ans[i - k + 1] = if streak >= k { nums[i] } else { -1 };
            }
        }
        ans
    }
}
'''

FILES["3256_maximum_value_sum_by_placing_three_rooks_i"] = r'''// LeetCode 3256 - Maximum Value Sum by Placing Three Rooks I
// https://leetcode.com/problems/maximum-value-sum-by-placing-three-rooks-i/

impl Solution {
    pub fn maximum_value_sum(board: Vec<Vec<i32>>) -> i64 {
        let m = board.len();
        let n = board[0].len();
        let mut tops: Vec<Vec<(i32, usize)>> = Vec::new();
        for i in 0..m {
            let mut row: Vec<(i32, usize)> = Vec::new();
            for j in 0..n {
                let cur = (board[i][j], j);
                let mut placed = false;
                for t in 0..row.len() {
                    if cur.0 > row[t].0 {
                        row.insert(t, cur);
                        placed = true;
                        break;
                    }
                }
                if !placed {
                    row.push(cur);
                }
                if row.len() > 3 {
                    row.truncate(3);
                }
            }
            tops.push(row);
        }
        let mut ans = i64::MIN / 2;
        for i in 0..m {
            for &(av, ac) in &tops[i] {
                for j in i + 1..m {
                    for &(bv, bc) in &tops[j] {
                        if ac == bc {
                            continue;
                        }
                        for k in j + 1..m {
                            for &(cv, cc) in &tops[k] {
                                if cc == ac || cc == bc {
                                    continue;
                                }
                                let s = av as i64 + bv as i64 + cv as i64;
                                if s > ans {
                                    ans = s;
                                }
                            }
                        }
                    }
                }
            }
        }
        ans
    }
}
'''

FILES["3257_maximum_value_sum_by_placing_three_rooks_ii"] = r'''// LeetCode 3257 - Maximum Value Sum by Placing Three Rooks II
// https://leetcode.com/problems/maximum-value-sum-by-placing-three-rooks-ii/

impl Solution {
    pub fn maximum_value_sum(board: Vec<Vec<i32>>) -> i64 {
        let m = board.len();
        let n = board[0].len();
        let mut tops: Vec<Vec<(i32, usize)>> = Vec::new();
        for i in 0..m {
            let mut row: Vec<(i32, usize)> = Vec::new();
            for j in 0..n {
                let cur = (board[i][j], j);
                let mut placed = false;
                for t in 0..row.len() {
                    if cur.0 > row[t].0 {
                        row.insert(t, cur);
                        placed = true;
                        break;
                    }
                }
                if !placed {
                    row.push(cur);
                }
                if row.len() > 3 {
                    row.truncate(3);
                }
            }
            tops.push(row);
        }
        let mut ans = i64::MIN / 2;
        for i in 0..m {
            for &(av, ac) in &tops[i] {
                for j in i + 1..m {
                    for &(bv, bc) in &tops[j] {
                        if ac == bc {
                            continue;
                        }
                        for k in j + 1..m {
                            for &(cv, cc) in &tops[k] {
                                if cc == ac || cc == bc {
                                    continue;
                                }
                                let s = av as i64 + bv as i64 + cv as i64;
                                if s > ans {
                                    ans = s;
                                }
                            }
                        }
                    }
                }
            }
        }
        ans
    }
}
'''

FILES["3258_count_substrings_that_satisfy_k_constraint_i"] = r'''// LeetCode 3258 - Count Substrings That Satisfy K-Constraint I
// https://leetcode.com/problems/count-substrings-that-satisfy-k-constraint-i/

impl Solution {
    pub fn count_k_constraint_substrings(s: String, k: i32) -> i32 {
        let b = s.as_bytes();
        let n = b.len();
        let mut ans = 0;
        for i in 0..n {
            let mut z = 0;
            let mut o = 0;
            for j in i..n {
                if b[j] == b'0' {
                    z += 1;
                } else {
                    o += 1;
                }
                if z <= k || o <= k {
                    ans += 1;
                } else {
                    break;
                }
            }
        }
        ans
    }
}
'''

FILES["3259_maximum_energy_boost_from_two_drinks"] = r'''// LeetCode 3259 - Maximum Energy Boost From Two Drinks
// https://leetcode.com/problems/maximum-energy-boost-from-two-drinks/

impl Solution {
    pub fn max_energy_boost(energy_drink_a: Vec<i32>, energy_drink_b: Vec<i32>) -> i64 {
        let n = energy_drink_a.len();
        let mut dp_a = vec![0i64; n];
        let mut dp_b = vec![0i64; n];
        dp_a[0] = energy_drink_a[0] as i64;
        dp_b[0] = energy_drink_b[0] as i64;
        if n == 1 {
            return dp_a[0].max(dp_b[0]);
        }
        dp_a[1] = energy_drink_a[1] as i64 + dp_a[0];
        dp_b[1] = energy_drink_b[1] as i64 + dp_b[0];
        for i in 2..n {
            dp_a[i] = energy_drink_a[i] as i64 + dp_a[i - 1].max(dp_b[i - 2]);
            dp_b[i] = energy_drink_b[i] as i64 + dp_b[i - 1].max(dp_a[i - 2]);
        }
        dp_a[n - 1].max(dp_b[n - 1])
    }
}
'''

FILES["3260_find_the_largest_palindrome_divisible_by_k"] = r'''// LeetCode 3260 - Find the Largest Palindrome Divisible by K
// https://leetcode.com/problems/find-the-largest-palindrome-divisible-by-k/

impl Solution {
    fn strings_repeat8(n: i32) -> String {
        "8".repeat(n as usize)
    }

    fn mod7(s: &str) -> i32 {
        let mut r = 0;
        for c in s.bytes() {
            r = (r * 10 + (c - b'0') as i32) % 7;
        }
        r
    }

    fn largest_pal7(n: i32) -> String {
        let half_len = ((n + 1) / 2) as usize;
        let mut half = vec![b'9'; half_len];
        loop {
            let mut pal = vec![b'0'; n as usize];
            for i in 0..half_len {
                pal[i] = half[i];
            }
            for i in 0..(n as usize / 2) {
                pal[n as usize - 1 - i] = pal[i];
            }
            let pal_s = String::from_utf8(pal).unwrap();
            if Self::mod7(&pal_s) == 0 {
                return pal_s;
            }
            let mut i = half_len as i32 - 1;
            while i >= 0 && half[i as usize] == b'0' {
                half[i as usize] = b'9';
                i -= 1;
            }
            if i < 0 {
                break;
            }
            half[i as usize] -= 1;
        }
        String::new()
    }

    pub fn largest_palindrome(n: i32, k: i32) -> String {
        let mut digits = vec![b'9'; n as usize];
        let half = ((n + 1) / 2) as usize;
        match k {
            1 | 3 | 9 => String::from_utf8(digits).unwrap(),
            2 => {
                digits[0] = b'8';
                digits[n as usize - 1] = b'8';
                String::from_utf8(digits).unwrap()
            }
            4 => {
                if n == 1 {
                    return "8".to_string();
                }
                digits[0] = b'8';
                digits[1] = b'8';
                digits[n as usize - 1] = b'8';
                digits[n as usize - 2] = b'8';
                String::from_utf8(digits).unwrap()
            }
            5 => {
                digits[0] = b'5';
                digits[n as usize - 1] = b'5';
                String::from_utf8(digits).unwrap()
            }
            8 => {
                if n <= 2 {
                    return Self::strings_repeat8(n);
                }
                digits[0] = b'8';
                digits[1] = b'8';
                digits[2] = b'8';
                digits[n as usize - 1] = b'8';
                digits[n as usize - 2] = b'8';
                digits[n as usize - 3] = b'8';
                String::from_utf8(digits).unwrap()
            }
            6 => {
                if n == 1 {
                    return "6".to_string();
                }
                digits[0] = b'8';
                digits[n as usize - 1] = b'8';
                let sum = 16 + 9 * (n - 2);
                let need = sum % 3;
                if need != 0 {
                    let pos = half - 1;
                    digits[pos] = (digits[pos] - need as u8) as u8;
                    if n % 2 == 0 || pos != n as usize - 1 - pos {
                        digits[n as usize - 1 - pos] = digits[pos];
                    }
                }
                String::from_utf8(digits).unwrap()
            }
            7 => Self::largest_pal7(n),
            _ => String::from_utf8(digits).unwrap(),
        }
    }
}
'''

FILES["3261_count_substrings_that_satisfy_k_constraint_ii"] = r'''// LeetCode 3261 - Count Substrings That Satisfy K-Constraint II
// https://leetcode.com/problems/count-substrings-that-satisfy-k-constraint-ii/

impl Solution {
    pub fn count_k_constraint_substrings(s: String, k: i32, queries: Vec<Vec<i32>>) -> Vec<i64> {
        let b = s.as_bytes();
        let n = b.len();
        let mut left_most = vec![0; n];
        let mut z = 0;
        let mut o = 0;
        let mut l = 0;
        for r in 0..n {
            if b[r] == b'0' {
                z += 1;
            } else {
                o += 1;
            }
            while z > k && o > k {
                if b[l] == b'0' {
                    z -= 1;
                } else {
                    o -= 1;
                }
                l += 1;
            }
            left_most[r] = l;
        }
        let mut pref = vec![0i64; n + 1];
        for i in 0..n {
            pref[i + 1] = pref[i] + (i - left_most[i] + 1) as i64;
        }
        let mut ans = vec![0i64; queries.len()];
        for (qi, q) in queries.iter().enumerate() {
            let lq = q[0] as usize;
            let rq = q[1] as usize;
            let mut lo = lq;
            let mut hi = rq + 1;
            while lo < hi {
                let mid = (lo + hi) / 2;
                if left_most[mid] < lq {
                    lo = mid + 1;
                } else {
                    hi = mid;
                }
            }
            let mut res = 0i64;
            if lo > lq {
                let m = (lo - lq) as i64;
                res += m * (m + 1) / 2;
            }
            if lo <= rq {
                res += pref[rq + 1] - pref[lo];
            }
            ans[qi] = res;
        }
        ans
    }
}
'''

FILES["3263_convert_doubly_linked_list_to_array_i"] = r'''// LeetCode 3263 - Convert Doubly Linked List to Array I
// https://leetcode.com/problems/convert-doubly-linked-list-to-array-i/

use std::cell::RefCell;
use std::rc::Rc;

pub struct Node {
    pub val: i32,
    pub prev: Option<Rc<RefCell<Node>>>,
    pub next: Option<Rc<RefCell<Node>>>,
}

impl Node {
    pub fn new(val: i32) -> Self {
        Node {
            val,
            prev: None,
            next: None,
        }
    }
}

impl Solution {
    pub fn to_array(head: Option<Rc<RefCell<Node>>>) -> Vec<i32> {
        let mut ans = Vec::new();
        let mut cur = head;
        while let Some(node) = cur {
            ans.push(node.borrow().val);
            cur = node.borrow().next.clone();
        }
        ans
    }
}
'''

FILES["3264_final_array_state_after_k_multiplication_operations_i"] = r'''// LeetCode 3264 - Final Array State After K Multiplication Operations I
// https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-i/

use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn get_final_state(mut nums: Vec<i32>, k: i32, multiplier: i32) -> Vec<i32> {
        let mut h: BinaryHeap<Reverse<(i32, usize)>> = BinaryHeap::new();
        for (i, &v) in nums.iter().enumerate() {
            h.push(Reverse((v, i)));
        }
        for _ in 0..k {
            if let Some(Reverse((v, i))) = h.pop() {
                let nv = v * multiplier;
                nums[i] = nv;
                h.push(Reverse((nv, i)));
            }
        }
        nums
    }
}
'''

FILES["3265_count_almost_equal_pairs_i"] = r'''// LeetCode 3265 - Count Almost Equal Pairs I
// https://leetcode.com/problems/count-almost-equal-pairs-i/

impl Solution {
    fn sprintf_num(mut x: i32) -> String {
        if x == 0 {
            return "0".to_string();
        }
        let mut b = String::new();
        while x > 0 {
            b.insert(0, char::from(b'0' + (x % 10) as u8));
            x /= 10;
        }
        b
    }

    fn almost_equal(a: i32, b: i32) -> bool {
        let mut sa = Self::sprintf_num(a);
        let mut sb = Self::sprintf_num(b);
        while sa.len() < sb.len() {
            sa.insert(0, '0');
        }
        while sb.len() < sa.len() {
            sb.insert(0, '0');
        }
        let mut diff = Vec::new();
        for i in 0..sa.len() {
            if sa.as_bytes()[i] != sb.as_bytes()[i] {
                diff.push(i);
            }
        }
        if diff.is_empty() {
            return true;
        }
        if diff.len() != 2 {
            return false;
        }
        let i = diff[0];
        let j = diff[1];
        sa.as_bytes()[i] == sb.as_bytes()[j] && sa.as_bytes()[j] == sb.as_bytes()[i]
    }

    pub fn count_pairs(nums: Vec<i32>) -> i32 {
        let mut ans = 0;
        for i in 0..nums.len() {
            for j in i + 1..nums.len() {
                if Self::almost_equal(nums[i], nums[j]) {
                    ans += 1;
                }
            }
        }
        ans
    }
}
'''

FILES["3266_final_array_state_after_k_multiplication_operations_ii"] = r'''// LeetCode 3266 - Final Array State After K Multiplication Operations II
// https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-ii/

use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    fn mod_pow(mut a: i64, mut e: i64, m: i64) -> i64 {
        let mut r = 1;
        a %= m;
        while e > 0 {
            if e & 1 == 1 {
                r = r * a % m;
            }
            a = a * a % m;
            e >>= 1;
        }
        r
    }

    pub fn get_final_state(mut nums: Vec<i32>, mut k: i32, multiplier: i32) -> Vec<i32> {
        const MOD: i64 = 1_000_000_007;
        if multiplier == 1 {
            return nums;
        }
        let mut h: BinaryHeap<Reverse<(i32, usize)>> = BinaryHeap::new();
        let mut max_v = 0;
        for (i, &v) in nums.iter().enumerate() {
            h.push(Reverse((v, i)));
            if v > max_v {
                max_v = v;
            }
        }
        while k > 0 && !h.is_empty() {
            let Reverse((v, i)) = h.pop().unwrap();
            if v as i64 * multiplier as i64 > max_v as i64 && k >= nums.len() as i32 {
                h.push(Reverse((v, i)));
                break;
            }
            let nv = v * multiplier;
            nums[i] = nv;
            if nv > max_v {
                max_v = nv;
            }
            h.push(Reverse((nv, i)));
            k -= 1;
        }
        if k > 0 {
            let n = nums.len() as i32;
            let full = k / n;
            let rem = k % n;
            let pow_full = Self::mod_pow(multiplier as i64, full as i64, MOD);
            for x in &mut nums {
                *x = ((*x as i64) * pow_full % MOD) as i32;
            }
            let mut hh: BinaryHeap<Reverse<(i32, usize)>> = BinaryHeap::new();
            for (i, &v) in nums.iter().enumerate() {
                hh.push(Reverse((v, i)));
            }
            for _ in 0..rem {
                let Reverse((v, i)) = hh.pop().unwrap();
                let nv = ((v as i64) * multiplier as i64 % MOD) as i32;
                nums[i] = nv;
                hh.push(Reverse((nv, i)));
            }
            for x in &mut nums {
                *x %= MOD as i32;
            }
        } else {
            for x in &mut nums {
                *x %= MOD as i32;
            }
        }
        nums
    }
}
'''

FILES["3267_count_almost_equal_pairs_ii"] = r'''// LeetCode 3267 - Count Almost Equal Pairs II
// https://leetcode.com/problems/count-almost-equal-pairs-ii/

impl Solution {
    fn pad_num(mut x: i32) -> String {
        if x == 0 {
            return "0".to_string();
        }
        let mut b = String::new();
        while x > 0 {
            b.insert(0, char::from(b'0' + (x % 10) as u8));
            x /= 10;
        }
        b
    }

    fn can_with_swaps(sa: &mut Vec<u8>, sb: &[u8], start: usize, left: i32) -> bool {
        if sa.as_slice() == sb {
            return true;
        }
        if left == 0 {
            return false;
        }
        for i in start..sa.len() {
            if sa[i] == sb[i] {
                continue;
            }
            for j in i + 1..sa.len() {
                if sa[j] == sb[i] {
                    sa.swap(i, j);
                    if Self::can_with_swaps(sa, sb, i + 1, left - 1) {
                        return true;
                    }
                    sa.swap(i, j);
                }
            }
            return false;
        }
        sa.as_slice() == sb
    }

    fn almost_equal(a: i32, b: i32) -> bool {
        let mut sa = Self::pad_num(a);
        let mut sb = Self::pad_num(b);
        while sa.len() < sb.len() {
            sa.insert(0, '0');
        }
        while sb.len() < sa.len() {
            sb.insert(0, '0');
        }
        if sa == sb {
            return true;
        }
        let mut sa_b = sa.into_bytes();
        let sb_b = sb.into_bytes();
        Self::can_with_swaps(&mut sa_b, &sb_b, 0, 2)
    }

    pub fn count_pairs(nums: Vec<i32>) -> i32 {
        let mut ans = 0;
        for i in 0..nums.len() {
            for j in i + 1..nums.len() {
                if Self::almost_equal(nums[i], nums[j]) {
                    ans += 1;
                }
            }
        }
        ans
    }
}
'''

FILES["3269_constructing_two_increasing_arrays"] = r'''// LeetCode 3269 - Constructing Two Increasing Arrays
// https://leetcode.com/problems/constructing-two-increasing-arrays/

impl Solution {
    pub fn min_largest(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        let n = nums1.len();
        let m = nums2.len();
        const INF: i32 = 1_000_000_000;
        let mut dp = vec![vec![INF; m + 1]; n + 1];
        dp[0][0] = 0;
        for i in 0..=n {
            for j in 0..=m {
                if dp[i][j] == INF {
                    continue;
                }
                let prev = dp[i][j];
                if i < n {
                    let mut need = prev + 1;
                    if nums1[i] == 0 {
                        if need % 2 != 0 {
                            need += 1;
                        }
                    } else if need % 2 == 0 {
                        need += 1;
                    }
                    if need < dp[i + 1][j] {
                        dp[i + 1][j] = need;
                    }
                }
                if j < m {
                    let mut need = prev + 1;
                    if nums2[j] == 0 {
                        if need % 2 != 0 {
                            need += 1;
                        }
                    } else if need % 2 == 0 {
                        need += 1;
                    }
                    if need < dp[i][j + 1] {
                        dp[i][j + 1] = need;
                    }
                }
            }
        }
        dp[n][m]
    }
}
'''

FILES["3270_find_the_key_of_the_numbers"] = r'''// LeetCode 3270 - Find the Key of the Numbers
// https://leetcode.com/problems/find-the-key-of-the-numbers/

impl Solution {
    pub fn generate_key(mut num1: i32, mut num2: i32, mut num3: i32) -> i32 {
        let mut ans = 0;
        let mut mul = 1;
        for _ in 0..4 {
            let d = num1 % 10;
            let d = d.min(num2 % 10).min(num3 % 10);
            ans += d * mul;
            mul *= 10;
            num1 /= 10;
            num2 /= 10;
            num3 /= 10;
        }
        ans
    }
}
'''

FILES["3271_hash_divided_string"] = r'''// LeetCode 3271 - Hash Divided String
// https://leetcode.com/problems/hash-divided-string/

impl Solution {
    pub fn string_hash(s: String, k: i32) -> String {
        let b = s.as_bytes();
        let k = k as usize;
        let mut out = String::new();
        let mut i = 0;
        while i < b.len() {
            let mut sum = 0;
            for j in i..i + k {
                sum += (b[j] - b'a') as i32;
            }
            out.push(char::from(b'a' + (sum % 26) as u8));
            i += k;
        }
        out
    }
}
'''

FILES["3272_find_the_count_of_good_integers"] = r'''// LeetCode 3272 - Find the Count of Good Integers
// https://leetcode.com/problems/find-the-count-of-good-integers/

use std::collections::HashSet;

impl Solution {
    fn itoa(mut x: i32) -> String {
        if x == 0 {
            return "0".to_string();
        }
        let mut b = String::new();
        while x > 0 {
            b.insert(0, char::from(b'0' + (x % 10) as u8));
            x /= 10;
        }
        b
    }

    fn atoi_str(s: &str) -> i64 {
        let mut v = 0i64;
        for c in s.bytes() {
            v = v * 10 + (c - b'0') as i64;
        }
        v
    }

    pub fn count_good_integers(n: i32, k: i32) -> i64 {
        let half = (n + 1) / 2;
        let mut start = 1;
        for _ in 1..half {
            start *= 10;
        }
        let end = start * 10;
        let mut seen = HashSet::new();
        let mut ans = 0i64;
        let mut fact = vec![1i64; (n + 1) as usize];
        for i in 1..=n as usize {
            fact[i] = fact[i - 1] * i as i64;
        }
        for h in start..end {
            let s = Self::itoa(h);
            let mut pal = s.clone();
            let mut rev_start = s.len() as i32 - 1;
            if n % 2 == 1 {
                rev_start -= 1;
            }
            let sb = s.as_bytes();
            let mut i = rev_start;
            while i >= 0 {
                pal.push(sb[i as usize] as char);
                i -= 1;
            }
            if Self::atoi_str(&pal) % k as i64 != 0 {
                continue;
            }
            let mut chars: Vec<u8> = pal.into_bytes();
            chars.sort_unstable();
            if seen.contains(&chars) {
                continue;
            }
            seen.insert(chars.clone());
            let mut cnt = [0i32; 10];
            for c in &chars {
                cnt[(c - b'0') as usize] += 1;
            }
            let mut total = fact[n as usize];
            for &c in &cnt {
                total /= fact[c as usize];
            }
            if cnt[0] > 0 {
                let mut bad = fact[n as usize - 1];
                cnt[0] -= 1;
                for &c in &cnt {
                    bad /= fact[c as usize];
                }
                cnt[0] += 1;
                total -= bad;
            }
            ans += total;
        }
        ans
    }
}
'''

FILES["3273_minimum_amount_of_damage_dealt_to_bob"] = r'''// LeetCode 3273 - Minimum Amount of Damage Dealt to Bob
// https://leetcode.com/problems/minimum-amount-of-damage-dealt-to-bob/

impl Solution {
    pub fn min_damage(power: i32, damage: Vec<i32>, health: Vec<i32>) -> i64 {
        let n = damage.len();
        let mut arr = Vec::with_capacity(n);
        let mut total_dmg = 0i64;
        for i in 0..n {
            let hits = (health[i] + power - 1) / power;
            arr.push((damage[i], hits));
            total_dmg += damage[i] as i64;
        }
        arr.sort_by(|a, b| (a.1 as i64 * b.0 as i64).cmp(&(b.1 as i64 * a.0 as i64)));
        let mut ans = 0i64;
        let mut cur = total_dmg;
        for (dmg, hits) in arr {
            ans += cur * hits as i64;
            cur -= dmg as i64;
        }
        ans
    }
}
'''

FILES["3274_check_if_two_chessboard_squares_have_the_same_color"] = r'''// LeetCode 3274 - Check if Two Chessboard Squares Have the Same Color
// https://leetcode.com/problems/check-if-two-chessboard-squares-have-the-same-color/

impl Solution {
    pub fn check_two_chessboards(coordinate1: String, coordinate2: String) -> bool {
        let b1 = coordinate1.as_bytes();
        let b2 = coordinate2.as_bytes();
        let c1 = (b1[0] - b'a') as i32 + (b1[1] - b'1') as i32;
        let c2 = (b2[0] - b'a') as i32 + (b2[1] - b'1') as i32;
        c1 % 2 == c2 % 2
    }
}
'''

FILES["3275_k_th_nearest_obstacle_queries"] = r'''// LeetCode 3275 - K-th Nearest Obstacle Queries
// https://leetcode.com/problems/k-th-nearest-obstacle-queries/

use std::collections::BinaryHeap;

impl Solution {
    pub fn results_array(queries: Vec<Vec<i32>>, k: i32) -> Vec<i32> {
        let mut h = BinaryHeap::new();
        let mut ans = vec![0; queries.len()];
        for (i, q) in queries.iter().enumerate() {
            let d = q[0].abs() + q[1].abs();
            h.push(d);
            if h.len() as i32 > k {
                h.pop();
            }
            ans[i] = if (h.len() as i32) < k { -1 } else { *h.peek().unwrap() };
        }
        ans
    }
}
'''

FILES["3276_select_cells_in_grid_with_maximum_score"] = r'''// LeetCode 3276 - Select Cells in Grid With Maximum Score
// https://leetcode.com/problems/select-cells-in-grid-with-maximum-score/

use std::collections::{HashMap, HashSet};

impl Solution {
    pub fn max_score(grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        let mut vals: HashMap<i32, Vec<usize>> = HashMap::new();
        for (i, row) in grid.iter().enumerate() {
            let mut seen = HashSet::new();
            for &v in row {
                if seen.insert(v) {
                    vals.entry(v).or_default().push(i);
                }
            }
        }
        let mut arr: Vec<i32> = vals.keys().copied().collect();
        arr.sort_unstable_by(|a, b| b.cmp(a));
        let nmask = 1 << m;
        let mut dp = vec![0; nmask];
        for v in arr {
            let mut ndp = dp.clone();
            for &r in &vals[&v] {
                let bit = 1 << r;
                for mask in 0..nmask {
                    if mask & bit != 0 {
                        continue;
                    }
                    let cand = dp[mask] + v;
                    let nm = mask | bit;
                    if cand > ndp[nm] {
                        ndp[nm] = cand;
                    }
                }
            }
            dp = ndp;
        }
        *dp.iter().max().unwrap()
    }
}
'''

FILES["3277_maximum_xor_score_subarray_queries"] = r'''// LeetCode 3277 - Maximum XOR Score Subarray Queries
// https://leetcode.com/problems/maximum-xor-score-subarray-queries/

impl Solution {
    pub fn maximum_subarray_xor(nums: Vec<i32>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let n = nums.len();
        let mut f = vec![vec![0; n]; n];
        for i in 0..n {
            f[i][i] = nums[i];
        }
        for length in 2..=n {
            for i in 0..=n - length {
                let j = i + length - 1;
                f[i][j] = f[i][j - 1] ^ f[i + 1][j];
            }
        }
        let mut best = vec![vec![0; n]; n];
        for i in 0..n {
            best[i][i] = f[i][i];
        }
        for length in 2..=n {
            for i in 0..=n - length {
                let j = i + length - 1;
                best[i][j] = f[i][j].max(best[i][j - 1]).max(best[i + 1][j]);
            }
        }
        queries.iter().map(|q| best[q[0] as usize][q[1] as usize]).collect()
    }
}
'''

FILES["3279_maximum_total_area_occupied_by_pistons"] = r'''// LeetCode 3279 - Maximum Total Area Occupied by Pistons
// https://leetcode.com/problems/maximum-total-area-occupied-by-pistons/

impl Solution {
    pub fn max_area(height: i32, positions: Vec<i32>, directions: String) -> i64 {
        let n = positions.len();
        let mut pos = positions;
        let mut dir = directions.into_bytes();
        let mut best = 0i64;
        for _ in 0..=2 * height {
            let mut sum = 0i64;
            for &p in &pos {
                sum += p as i64;
            }
            if sum > best {
                best = sum;
            }
            for i in 0..n {
                if dir[i] == b'U' {
                    if pos[i] == height {
                        dir[i] = b'D';
                        pos[i] -= 1;
                    } else {
                        pos[i] += 1;
                    }
                } else if pos[i] == 0 {
                    dir[i] = b'U';
                    pos[i] += 1;
                } else {
                    pos[i] -= 1;
                }
            }
        }
        best
    }
}
'''

FILES["3280_convert_date_to_binary"] = r'''// LeetCode 3280 - Convert Date to Binary
// https://leetcode.com/problems/convert-date-to-binary/

impl Solution {
    fn to_binary(mut v: i32) -> String {
        if v == 0 {
            return "0".to_string();
        }
        let mut s = String::new();
        while v > 0 {
            s.insert(0, char::from(b'0' + (v & 1) as u8));
            v >>= 1;
        }
        s
    }

    pub fn convert_date_to_binary(date: String) -> String {
        let parts: Vec<i32> = date.split('-').map(|p| p.parse().unwrap()).collect();
        format!(
            "{}-{}-{}",
            Self::to_binary(parts[0]),
            Self::to_binary(parts[1]),
            Self::to_binary(parts[2])
        )
    }
}
'''

FILES["3281_maximize_score_of_numbers_in_ranges"] = r'''// LeetCode 3281 - Maximize Score of Numbers in Ranges
// https://leetcode.com/problems/maximize-score-of-numbers-in-ranges/

impl Solution {
    pub fn max_possible_score(mut start: Vec<i32>, d: i32) -> i32 {
        start.sort_unstable();
        let n = start.len();
        let ok = |mid: i32| -> bool {
            let mut prev = start[0] as i64;
            for i in 1..n {
                let need = prev + mid as i64;
                let cur = start[i] as i64;
                if need > cur + d as i64 {
                    return false;
                }
                prev = if need > cur { need } else { cur };
            }
            true
        };
        let mut lo = 0;
        let mut hi = start[n - 1] + d - start[0] + 1;
        while lo < hi {
            let mid = (lo as i64 + hi as i64 + 1) / 2;
            let mid = mid as i32;
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

FILES["3282_reach_end_of_array_with_max_score"] = r'''// LeetCode 3282 - Reach End of Array With Max Score
// https://leetcode.com/problems/reach-end-of-array-with-max-score/

impl Solution {
    pub fn find_maximum_score(nums: Vec<i32>) -> i64 {
        let mut ans = 0i64;
        let mut max_v = 0;
        for i in 0..nums.len() - 1 {
            if nums[i] > max_v {
                max_v = nums[i];
            }
            ans += max_v as i64;
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

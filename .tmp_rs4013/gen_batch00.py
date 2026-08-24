#!/usr/bin/env python3
"""Generate Rust solutions for batch_00."""
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

LIST = """#[derive(PartialEq, Eq)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}
"""

NARY = """use std::cell::RefCell;
use std::rc::Rc;

#[derive(Debug, PartialEq, Eq)]
pub struct Node {
    pub val: i32,
    pub children: Vec<Rc<RefCell<Node>>>,
}
"""

QUAD = """#[derive(Debug, PartialEq, Eq)]
pub struct Node {
    pub val: bool,
    pub is_leaf: bool,
    pub top_left: Option<Box<Node>>,
    pub top_right: Option<Box<Node>>,
    pub bottom_left: Option<Box<Node>>,
    pub bottom_right: Option<Box<Node>>,
}
"""


def header(num: str, title: str, slug: str) -> str:
    return f"// LeetCode {num} - {title}\n// https://leetcode.com/problems/{slug}/\n\n"


FILES: dict[str, str] = {}

FILES["0141_linked_list_cycle"] = header("0141", "Linked List Cycle", "linked-list-cycle") + LIST + """
impl Solution {
    pub fn has_cycle(head: Option<Box<ListNode>>) -> bool {
        let mut slow = head.as_deref();
        let mut fast = head.as_deref();
        while let Some(fast_node) = fast {
            let Some(next_fast) = fast_node.next.as_deref() else {
                return false;
            };
            slow = slow.and_then(|node| node.next.as_deref());
            fast = next_fast.next.as_deref();
            if let (Some(slow_node), Some(fast_node)) = (slow, fast) {
                if std::ptr::eq(slow_node, fast_node) {
                    return true;
                }
            }
        }
        false
    }
}
"""

FILES["0142_linked_list_cycle_ii"] = header("0142", "Linked List Cycle II", "linked-list-cycle-ii") + LIST + """
impl Solution {
    pub fn detect_cycle(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut slow = head.as_deref();
        let mut fast = head.as_deref();
        let mut met = false;
        while let Some(fast_node) = fast {
            let Some(next_fast) = fast_node.next.as_deref() else {
                break;
            };
            slow = slow.and_then(|node| node.next.as_deref());
            fast = next_fast.next.as_deref();
            if let (Some(s), Some(f)) = (slow, fast) {
                if std::ptr::eq(s, f) {
                    met = true;
                    break;
                }
            }
        }
        if !met {
            return None;
        }
        let mut p1 = head.as_deref();
        let mut p2 = slow;
        while let (Some(a), Some(b)) = (p1, p2) {
            if std::ptr::eq(a, b) {
                return Some(Box::new(ListNode { val: a.val, next: None }));
            }
            p1 = a.next.as_deref();
            p2 = b.next.as_deref();
        }
        None
    }
}
"""

FILES["0551_student_attendance_record_i"] = header(
    "0551", "Student Attendance Record I", "student-attendance-record-i"
) + """impl Solution {
    pub fn check_record(s: String) -> bool {
        let mut absents = 0;
        let mut late_streak = 0;
        for ch in s.chars() {
            if ch == 'A' {
                absents += 1;
                if absents >= 2 {
                    return false;
                }
                late_streak = 0;
            } else if ch == 'L' {
                late_streak += 1;
                if late_streak >= 3 {
                    return false;
                }
            } else {
                late_streak = 0;
            }
        }
        true
    }
}
"""

FILES["0552_student_attendance_record_ii"] = header(
    "0552", "Student Attendance Record II", "student-attendance-record-ii"
) + """impl Solution {
    pub fn check_record(n: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let mut dp = [[0i64; 3]; 2];
        dp[0][0] = 1;
        for _ in 0..n {
            let mut nxt = [[0i64; 3]; 2];
            for absences in 0..2 {
                for lates in 0..3 {
                    let ways = dp[absences][lates];
                    if ways == 0 {
                        continue;
                    }
                    nxt[absences][0] = (nxt[absences][0] + ways) % MOD;
                    if absences == 0 {
                        nxt[1][0] = (nxt[1][0] + ways) % MOD;
                    }
                    if lates < 2 {
                        nxt[absences][lates + 1] = (nxt[absences][lates + 1] + ways) % MOD;
                    }
                }
            }
            dp = nxt;
        }
        let mut total = 0;
        for absences in 0..2 {
            for lates in 0..3 {
                total = (total + dp[absences][lates]) % MOD;
            }
        }
        total as i32
    }
}
"""

FILES["0553_optimal_division"] = header("0553", "Optimal Division", "optimal-division") + """impl Solution {
    pub fn optimal_division(nums: Vec<i32>) -> String {
        if nums.len() == 1 {
            return nums[0].to_string();
        }
        if nums.len() == 2 {
            return format!("{}/{}", nums[0], nums[1]);
        }
        let mut result = format!("{}/(", nums[0]);
        for (i, num) in nums.iter().enumerate().skip(1) {
            if i > 1 {
                result.push('/');
            }
            result.push_str(&num.to_string());
        }
        result.push(')');
        result
    }
}
"""

FILES["0554_brick_wall"] = header("0554", "Brick Wall", "brick-wall") + """use std::collections::HashMap;

impl Solution {
    pub fn least_bricks(wall: Vec<Vec<i32>>) -> i32 {
        let mut edges = HashMap::new();
        let mut best = 0;
        for row in &wall {
            let mut width = 0;
            for &brick in &row[..row.len().saturating_sub(1)] {
                width += brick;
                let count = edges.entry(width).or_insert(0);
                *count += 1;
                best = best.max(*count);
            }
        }
        wall.len() as i32 - best
    }
}
"""

FILES["0555_split_concatenated_strings"] = header(
    "0555", "Split Concatenated Strings", "split-concatenated-strings"
) + """impl Solution {
    pub fn split_looped_string(strs: Vec<String>) -> String {
        let best_forms: Vec<String> = strs
            .iter()
            .map(|s| {
                let rev: String = s.chars().rev().collect();
                if s.as_str() > rev.as_str() {
                    s.clone()
                } else {
                    rev
                }
            })
            .collect();

        let mut answer = String::new();
        for i in 0..strs.len() {
            let mut mid = String::new();
            for j in i + 1..strs.len() {
                mid.push_str(&best_forms[j]);
            }
            for j in 0..i {
                mid.push_str(&best_forms[j]);
            }
            let original = &strs[i];
            let reversed: String = original.chars().rev().collect();
            for candidate in [original.as_str(), reversed.as_str()] {
                let chars: Vec<char> = candidate.chars().collect();
                for cut in 0..chars.len() {
                    let formed: String = chars[cut..]
                        .iter()
                        .chain(mid.chars().collect::<Vec<_>>().iter())
                        .chain(chars[..cut].iter())
                        .collect();
                    if formed > answer {
                        answer = formed;
                    }
                }
            }
        }
        answer
    }
}
"""

FILES["0556_next_greater_element_iii"] = header(
    "0556", "Next Greater Element III", "next-greater-element-iii"
) + """impl Solution {
    pub fn next_greater_element(n: i32) -> i32 {
        let mut digits: Vec<char> = n.to_string().chars().collect();
        let mut i = digits.len() as i32 - 2;
        while i >= 0 && digits[i as usize] >= digits[i as usize + 1] {
            i -= 1;
        }
        if i < 0 {
            return -1;
        }
        let mut j = digits.len() as i32 - 1;
        while digits[j as usize] <= digits[i as usize] {
            j -= 1;
        }
        digits.swap(i as usize, j as usize);
        digits[(i as usize + 1)..].reverse();
        let mut value: i64 = 0;
        for ch in digits {
            value = value * 10 + (ch as i64 - '0' as i64);
        }
        if value > i32::MAX as i64 {
            -1
        } else {
            value as i32
        }
    }
}
"""

FILES["0557_reverse_words_in_a_string_iii"] = header(
    "0557", "Reverse Words in a String III", "reverse-words-in-a-string-iii"
) + """impl Solution {
    pub fn reverse_words(s: String) -> String {
        let mut chars: Vec<char> = s.chars().collect();
        let n = chars.len();
        let mut start = 0;
        for i in 0..=n {
            if i == n || chars[i] == ' ' {
                chars[start..i].reverse();
                start = i + 1;
            }
        }
        chars.into_iter().collect()
    }
}
"""

FILES["0558_logical_or_of_two_binary_grids_represented_as_quad_trees"] = header(
    "0558",
    "Logical OR of Two Binary Grids Represented as Quad-Trees",
    "logical-or-of-two-binary-grids-represented-as-quad-trees",
) + QUAD + """
impl Solution {
    pub fn intersect(quad_tree1: Option<Box<Node>>, quad_tree2: Option<Box<Node>>) -> Option<Box<Node>> {
        let a = quad_tree1?;
        let b = quad_tree2?;
        if a.is_leaf {
            return if a.val { Some(a) } else { Some(b) };
        }
        if b.is_leaf {
            return if b.val { Some(b) } else { Some(a) };
        }
        let top_left = Self::intersect(a.top_left, b.top_left);
        let top_right = Self::intersect(a.top_right, b.top_right);
        let bottom_left = Self::intersect(a.bottom_left, b.bottom_left);
        let bottom_right = Self::intersect(a.bottom_right, b.bottom_right);
        if let (Some(tl), Some(tr), Some(bl), Some(br)) = (
            top_left.as_ref(),
            top_right.as_ref(),
            bottom_left.as_ref(),
            bottom_right.as_ref(),
        ) {
            if tl.is_leaf
                && tr.is_leaf
                && bl.is_leaf
                && br.is_leaf
                && tl.val == tr.val
                && tr.val == bl.val
                && bl.val == br.val
            {
                return Some(Box::new(Node {
                    val: tl.val,
                    is_leaf: true,
                    top_left: None,
                    top_right: None,
                    bottom_left: None,
                    bottom_right: None,
                }));
            }
        }
        Some(Box::new(Node {
            val: false,
            is_leaf: false,
            top_left,
            top_right,
            bottom_left,
            bottom_right,
        }))
    }
}
"""

FILES["0559_maximum_depth_of_n_ary_tree"] = header(
    "0559", "Maximum Depth of N-ary Tree", "maximum-depth-of-n-ary-tree"
) + NARY + """
impl Solution {
    pub fn max_depth(root: Option<Rc<RefCell<Node>>>) -> i32 {
        let Some(root) = root else {
            return 0;
        };
        let node = root.borrow();
        if node.children.is_empty() {
            return 1;
        }
        let mut best = 0;
        for child in &node.children {
            best = best.max(Self::max_depth(Some(child.clone())));
        }
        best + 1
    }
}
"""

FILES["0560_subarray_sum_equals_k"] = header(
    "0560", "Subarray Sum Equals K", "subarray-sum-equals-k"
) + """use std::collections::HashMap;

impl Solution {
    pub fn subarray_sum(nums: Vec<i32>, k: i32) -> i32 {
        let mut counts = HashMap::new();
        counts.insert(0, 1);
        let mut prefix = 0;
        let mut answer = 0;
        for num in nums {
            prefix += num;
            if let Some(&count) = counts.get(&(prefix - k)) {
                answer += count;
            }
            *counts.entry(prefix).or_insert(0) += 1;
        }
        answer
    }
}
"""

FILES["0561_array_partition"] = header("0561", "Array Partition", "array-partition") + """impl Solution {
    pub fn array_pair_sum(mut nums: Vec<i32>) -> i32 {
        nums.sort_unstable();
        nums.iter().step_by(2).sum()
    }
}
"""

FILES["0562_longest_line_of_consecutive_one_in_matrix"] = header(
    "0562",
    "Longest Line of Consecutive One in Matrix",
    "longest-line-of-consecutive-one-in-matrix",
) + """impl Solution {
    pub fn longest_line(mat: Vec<Vec<i32>>) -> i32 {
        if mat.is_empty() || mat[0].is_empty() {
            return 0;
        }
        let rows = mat.len();
        let cols = mat[0].len();
        let mut dp = vec![vec![[0i32; 4]; cols]; rows];
        let mut best = 0;
        for r in 0..rows {
            for c in 0..cols {
                if mat[r][c] == 0 {
                    continue;
                }
                dp[r][c][0] = if c > 0 { dp[r][c - 1][0] } else { 0 } + 1;
                dp[r][c][1] = if r > 0 { dp[r - 1][c][1] } else { 0 } + 1;
                dp[r][c][2] = if r > 0 && c > 0 { dp[r - 1][c - 1][2] } else { 0 } + 1;
                dp[r][c][3] = if r > 0 && c + 1 < cols { dp[r - 1][c + 1][3] } else { 0 } + 1;
                best = best.max(*dp[r][c].iter().max().unwrap());
            }
        }
        best
    }
}
"""

FILES["0563_binary_tree_tilt"] = header("0563", "Binary Tree Tilt", "binary-tree-tilt") + TREE + """
impl Solution {
    fn subtree_sum(node: &Option<Rc<RefCell<TreeNode>>>, total: &mut i32) -> i32 {
        let Some(node) = node else {
            return 0;
        };
        let node = node.borrow();
        let left = Self::subtree_sum(&node.left, total);
        let right = Self::subtree_sum(&node.right, total);
        *total += (left - right).abs();
        node.val + left + right
    }

    pub fn find_tilt(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let mut total = 0;
        Self::subtree_sum(&root, &mut total);
        total
    }
}
"""

FILES["0564_find_the_closest_palindrome"] = header(
    "0564", "Find the Closest Palindrome", "find-the-closest-palindrome"
) + """impl Solution {
    fn make_palindrome(half: i64, length: usize) -> i64 {
        let text = half.to_string();
        let chars: Vec<char> = text.chars().collect();
        let mut pal = text.clone();
        if length % 2 == 0 {
            for i in (0..chars.len()).rev() {
                pal.push(chars[i]);
            }
        } else {
            for i in (0..chars.len().saturating_sub(1)).rev() {
                pal.push(chars[i]);
            }
        }
        pal.parse().unwrap_or(0)
    }

    fn pow10ll(exp: usize) -> i64 {
        let mut value = 1i64;
        for _ in 0..exp {
            value *= 10;
        }
        value
    }

    pub fn nearest_palindromic(n: String) -> String {
        let length = n.len();
        let number: i64 = n.parse().unwrap();
        let mut candidates = vec![Self::pow10ll(length - 1) - 1, Self::pow10ll(length) + 1];
        let prefix: i64 = n[..(length + 1) / 2].parse().unwrap();
        for half in prefix - 1..=prefix + 1 {
            candidates.push(Self::make_palindrome(half, length));
        }
        let mut best = -1i64;
        let mut best_diff = i64::MAX;
        for candidate in candidates {
            if candidate == number {
                continue;
            }
            let diff = (candidate - number).abs();
            if diff < best_diff || (diff == best_diff && candidate < best) {
                best = candidate;
                best_diff = diff;
            }
        }
        best.to_string()
    }
}
"""

FILES["0565_array_nesting"] = header("0565", "Array Nesting", "array-nesting") + """impl Solution {
    pub fn array_nesting(mut nums: Vec<i32>) -> i32 {
        let mut best = 0;
        for i in 0..nums.len() {
            if nums[i] < 0 {
                continue;
            }
            let mut length = 0;
            let mut j = i as i32;
            while nums[j as usize] >= 0 {
                let nxt = nums[j as usize];
                nums[j as usize] = -1;
                j = nxt;
                length += 1;
            }
            best = best.max(length);
        }
        best
    }
}
"""

FILES["0566_reshape_the_matrix"] = header("0566", "Reshape the Matrix", "reshape-the-matrix") + """impl Solution {
    pub fn matrix_reshape(mat: Vec<Vec<i32>>, r: i32, c: i32) -> Vec<Vec<i32>> {
        let rows = mat.len() as i32;
        let cols = mat[0].len() as i32;
        if rows * cols != r * c {
            return mat;
        }
        let mut result = vec![vec![0; c as usize]; r as usize];
        let mut index = 0;
        for i in 0..r as usize {
            for j in 0..c as usize {
                result[i][j] = mat[index / cols as usize][index % cols as usize];
                index += 1;
            }
        }
        result
    }
}
"""

FILES["0567_permutation_in_string"] = header(
    "0567", "Permutation in String", "permutation-in-string"
) + """impl Solution {
    pub fn check_inclusion(s1: String, s2: String) -> bool {
        let s1: Vec<u8> = s1.into_bytes();
        let s2: Vec<u8> = s2.into_bytes();
        let n1 = s1.len();
        let n2 = s2.len();
        if n1 > n2 {
            return false;
        }
        let mut need = [0i32; 26];
        let mut window = [0i32; 26];
        for i in 0..n1 {
            need[(s1[i] - b'a') as usize] += 1;
            window[(s2[i] - b'a') as usize] += 1;
        }
        let mut matches = 0;
        for i in 0..26 {
            if need[i] == window[i] {
                matches += 1;
            }
        }
        if matches == 26 {
            return true;
        }
        for right in n1..n2 {
            let add = (s2[right] - b'a') as usize;
            let remove = (s2[right - n1] - b'a') as usize;
            if window[add] == need[add] {
                matches -= 1;
            }
            window[add] += 1;
            if window[add] == need[add] {
                matches += 1;
            }
            if window[remove] == need[remove] {
                matches -= 1;
            }
            window[remove] -= 1;
            if window[remove] == need[remove] {
                matches += 1;
            }
            if matches == 26 {
                return true;
            }
        }
        false
    }
}
"""

FILES["0568_maximum_vacation_days"] = header(
    "0568", "Maximum Vacation Days", "maximum-vacation-days"
) + """impl Solution {
    pub fn max_vacation_days(flights: Vec<Vec<i32>>, days: Vec<Vec<i32>>) -> i32 {
        let cities = flights.len();
        let weeks = days[0].len();
        const NEG: i32 = -1_000_000_000;
        let mut dp = vec![NEG; cities];
        dp[0] = 0;
        for week in 0..weeks {
            let mut nxt = vec![NEG; cities];
            for city in 0..cities {
                if dp[city] == NEG {
                    continue;
                }
                for dest in 0..cities {
                    if dest == city || flights[city][dest] == 1 {
                        nxt[dest] = nxt[dest].max(dp[city] + days[dest][week]);
                    }
                }
            }
            dp = nxt;
        }
        *dp.iter().max().unwrap()
    }
}
"""

FILES["0572_subtree_of_another_tree"] = header(
    "0572", "Subtree of Another Tree", "subtree-of-another-tree"
) + TREE + """
impl Solution {
    fn same(a: &Option<Rc<RefCell<TreeNode>>>, b: &Option<Rc<RefCell<TreeNode>>>) -> bool {
        match (a, b) {
            (None, None) => true,
            (Some(a), Some(b)) => {
                let a = a.borrow();
                let b = b.borrow();
                a.val == b.val && Self::same(&a.left, &b.left) && Self::same(&a.right, &b.right)
            }
            _ => false,
        }
    }

    pub fn is_subtree(
        root: Option<Rc<RefCell<TreeNode>>>,
        sub_root: Option<Rc<RefCell<TreeNode>>>,
    ) -> bool {
        let Some(root) = root else {
            return false;
        };
        let node = root.borrow();
        Self::same(&Some(root.clone()), &sub_root)
            || Self::is_subtree(node.left.clone(), sub_root.clone())
            || Self::is_subtree(node.right.clone(), sub_root)
    }
}
"""

FILES["0573_squirrel_simulation"] = header("0573", "Squirrel Simulation", "squirrel-simulation") + """impl Solution {
    fn dist(a: &[i32], b: &[i32]) -> i32 {
        (a[0] - b[0]).abs() + (a[1] - b[1]).abs()
    }

    pub fn min_distance(
        _height: i32,
        _width: i32,
        tree: Vec<i32>,
        squirrel: Vec<i32>,
        nuts: Vec<Vec<i32>>,
    ) -> i32 {
        let mut total = 0;
        let mut best_save = i32::MIN;
        for nut in &nuts {
            let tree_dist = Self::dist(&tree, nut);
            let squirrel_dist = Self::dist(&squirrel, nut);
            total += 2 * tree_dist;
            best_save = best_save.max(tree_dist - squirrel_dist);
        }
        total - best_save
    }
}
"""

FILES["0575_distribute_candies"] = header("0575", "Distribute Candies", "distribute-candies") + """use std::collections::HashSet;

impl Solution {
    pub fn distribute_candies(candy_type: Vec<i32>) -> i32 {
        let unique: HashSet<i32> = candy_type.iter().copied().collect();
        unique.len().min(candy_type.len() / 2) as i32
    }
}
"""

FILES["0576_out_of_boundary_paths"] = header(
    "0576", "Out of Boundary Paths", "out-of-boundary-paths"
) + """impl Solution {
    pub fn find_paths(m: i32, n: i32, max_move: i32, start_row: i32, start_column: i32) -> i32 {
        const MOD: i32 = 1_000_000_007;
        let m = m as usize;
        let n = n as usize;
        let mut dp = vec![vec![0i32; n]; m];
        dp[start_row as usize][start_column as usize] = 1;
        let mut result = 0;
        let dirs = [(0isize, 1isize), (0, -1), (1, 0), (-1, 0)];
        for _ in 0..max_move {
            let mut nxt = vec![vec![0i32; n]; m];
            for row in 0..m {
                for col in 0..n {
                    let ways = dp[row][col];
                    if ways == 0 {
                        continue;
                    }
                    for (dr, dc) in dirs {
                        let nr = row as isize + dr;
                        let nc = col as isize + dc;
                        if nr >= 0 && nr < m as isize && nc >= 0 && nc < n as isize {
                            nxt[nr as usize][nc as usize] = (nxt[nr as usize][nc as usize] + ways) % MOD;
                        } else {
                            result = (result + ways) % MOD;
                        }
                    }
                }
            }
            dp = nxt;
        }
        result
    }
}
"""

FILES["0581_shortest_unsorted_continuous_subarray"] = header(
    "0581",
    "Shortest Unsorted Continuous Subarray",
    "shortest-unsorted-continuous-subarray",
) + """impl Solution {
    pub fn find_unsorted_subarray(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut left: i32 = -1;
        let mut right: i32 = -2;
        let mut max_seen = nums[0];
        let mut min_seen = nums[n - 1];
        for i in 0..n {
            max_seen = max_seen.max(nums[i]);
            if nums[i] < max_seen {
                right = i as i32;
            }
            let j = n - 1 - i;
            min_seen = min_seen.min(nums[j]);
            if nums[j] > min_seen {
                left = j as i32;
            }
        }
        right - left + 1
    }
}
"""

FILES["0582_kill_process"] = header("0582", "Kill Process", "kill-process") + """use std::collections::{HashMap, VecDeque};

impl Solution {
    pub fn kill_process(pid: Vec<i32>, ppid: Vec<i32>, kill: i32) -> Vec<i32> {
        let mut children: HashMap<i32, Vec<i32>> = HashMap::new();
        for i in 0..pid.len() {
            children.entry(ppid[i]).or_default().push(pid[i]);
        }
        let mut result = Vec::new();
        let mut queue = VecDeque::new();
        queue.push_back(kill);
        while let Some(process) = queue.pop_front() {
            result.push(process);
            if let Some(kids) = children.get(&process) {
                for &child in kids {
                    queue.push_back(child);
                }
            }
        }
        result
    }
}
"""

FILES["0583_delete_operation_for_two_strings"] = header(
    "0583", "Delete Operation for Two Strings", "delete-operation-for-two-strings"
) + """impl Solution {
    pub fn min_distance(word1: String, word2: String) -> i32 {
        let w1 = word1.as_bytes();
        let w2 = word2.as_bytes();
        let m = w1.len();
        let n = w2.len();
        let mut prev = vec![0i32; n + 1];
        let mut curr = vec![0i32; n + 1];
        for i in 1..=m {
            for j in 1..=n {
                if w1[i - 1] == w2[j - 1] {
                    curr[j] = prev[j - 1] + 1;
                } else {
                    curr[j] = prev[j].max(curr[j - 1]);
                }
            }
            std::mem::swap(&mut prev, &mut curr);
            curr.fill(0);
        }
        (m + n) as i32 - 2 * prev[n]
    }
}
"""

FILES["0587_erect_the_fence"] = header("0587", "Erect the Fence", "erect-the-fence") + """impl Solution {
    fn cross(o: &[i32], a: &[i32], b: &[i32]) -> i64 {
        (a[0] as i64 - o[0] as i64) * (b[1] as i64 - o[1] as i64)
            - (a[1] as i64 - o[1] as i64) * (b[0] as i64 - o[0] as i64)
    }

    pub fn outer_trees(trees: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let mut points = trees;
        points.sort();
        if points.len() <= 1 {
            return points;
        }
        let build = |ordered: &[Vec<i32>]| {
            let mut hull: Vec<Vec<i32>> = Vec::new();
            for point in ordered {
                while hull.len() >= 2
                    && Self::cross(&hull[hull.len() - 2], &hull[hull.len() - 1], point) < 0
                {
                    hull.pop();
                }
                hull.push(point.clone());
            }
            hull
        };
        let lower = build(&points);
        let mut reversed = points.clone();
        reversed.reverse();
        let upper = build(&reversed);
        let mut unique = std::collections::BTreeSet::new();
        for i in 0..lower.len().saturating_sub(1) {
            unique.insert(lower[i].clone());
        }
        for i in 0..upper.len().saturating_sub(1) {
            unique.insert(upper[i].clone());
        }
        unique.into_iter().collect()
    }
}
"""

FILES["0588_design_in_memory_file_system"] = header(
    "0588", "Design In-Memory File System", "design-in-memory-file-system"
) + """use std::collections::BTreeMap;

struct FsNode {
    is_file: bool,
    content: String,
    children: BTreeMap<String, FsNode>,
}

impl FsNode {
    fn new() -> Self {
        Self {
            is_file: false,
            content: String::new(),
            children: BTreeMap::new(),
        }
    }
}

pub struct FileSystem {
    root: FsNode,
}

impl FileSystem {
    pub fn new() -> Self {
        Self { root: FsNode::new() }
    }

    fn split(path: &str) -> Vec<String> {
        path.split('/')
            .filter(|part| !part.is_empty())
            .map(|part| part.to_string())
            .collect()
    }

    pub fn ls(&self, path: String) -> Vec<String> {
        if path == "/" {
            return self.root.children.keys().cloned().collect();
        }
        let parts = Self::split(&path);
        let mut node = &self.root;
        for part in &parts {
            node = node.children.get(part).unwrap();
        }
        if node.is_file {
            return vec![parts.last().unwrap().clone()];
        }
        node.children.keys().cloned().collect()
    }

    pub fn mkdir(&mut self, path: String) {
        let mut node = &mut self.root;
        for part in Self::split(&path) {
            node = node.children.entry(part).or_insert_with(FsNode::new);
        }
    }

    pub fn add_content_to_file(&mut self, file_path: String, content: String) {
        let parts = Self::split(&file_path);
        let mut node = &mut self.root;
        for part in &parts[..parts.len() - 1] {
            node = node.children.entry(part.clone()).or_insert_with(FsNode::new);
        }
        let name = parts.last().unwrap();
        let file = node.children.entry(name.clone()).or_insert_with(FsNode::new);
        file.is_file = true;
        file.content.push_str(&content);
    }

    pub fn read_content_from_file(&self, file_path: String) -> String {
        let mut node = &self.root;
        for part in Self::split(&file_path) {
            node = node.children.get(&part).unwrap();
        }
        node.content.clone()
    }
}
"""

FILES["0589_n_ary_tree_preorder_traversal"] = header(
    "0589", "N-ary Tree Preorder Traversal", "n-ary-tree-preorder-traversal"
) + NARY + """
impl Solution {
    fn dfs(node: Option<Rc<RefCell<Node>>>, result: &mut Vec<i32>) {
        let Some(node) = node else {
            return;
        };
        let node = node.borrow();
        result.push(node.val);
        for child in &node.children {
            Self::dfs(Some(child.clone()), result);
        }
    }

    pub fn preorder(root: Option<Rc<RefCell<Node>>>) -> Vec<i32> {
        let mut result = Vec::new();
        Self::dfs(root, &mut result);
        result
    }
}
"""

FILES["0590_n_ary_tree_postorder_traversal"] = header(
    "0590", "N-ary Tree Postorder Traversal", "n-ary-tree-postorder-traversal"
) + NARY + """
impl Solution {
    fn dfs(node: Option<Rc<RefCell<Node>>>, result: &mut Vec<i32>) {
        let Some(node) = node else {
            return;
        };
        let node = node.borrow();
        for child in &node.children {
            Self::dfs(Some(child.clone()), result);
        }
        result.push(node.val);
    }

    pub fn postorder(root: Option<Rc<RefCell<Node>>>) -> Vec<i32> {
        let mut result = Vec::new();
        Self::dfs(root, &mut result);
        result
    }
}
"""

FILES["0591_tag_validator"] = header("0591", "Tag Validator", "tag-validator") + """impl Solution {
    pub fn is_valid(code: String) -> bool {
        let chars: Vec<char> = code.chars().collect();
        let n = chars.len();
        let mut stack = Vec::new();
        let mut i = 0;
        while i < n {
            let rest: String = chars[i..].iter().collect();
            if rest.starts_with("<![CDATA[") {
                if stack.is_empty() {
                    return false;
                }
                if let Some(j) = rest.find("]]>") {
                    i += j + 3;
                } else {
                    return false;
                }
            } else if rest.starts_with("</") {
                if let Some(j) = rest[2..].find('>') {
                    let tag: String = rest[2..2 + j].to_string();
                    if stack.last() != Some(&tag) {
                        return false;
                    }
                    stack.pop();
                    i += 2 + j + 1;
                    if stack.is_empty() && i < n {
                        return false;
                    }
                } else {
                    return false;
                }
            } else if chars[i] == '<' {
                if let Some(j) = rest[1..].find('>') {
                    let tag: String = rest[1..1 + j].to_string();
                    if tag.is_empty() || tag.len() > 9 {
                        return false;
                    }
                    if !tag.chars().all(|ch| ch.is_ascii_uppercase()) {
                        return false;
                    }
                    stack.push(tag);
                    i += 1 + j + 1;
                } else {
                    return false;
                }
            } else {
                if stack.is_empty() {
                    return false;
                }
                i += 1;
            }
        }
        stack.is_empty()
    }
}
"""

FILES["0592_fraction_addition_and_subtraction"] = header(
    "0592", "Fraction Addition and Subtraction", "fraction-addition-and-subtraction"
) + """impl Solution {
    fn gcd(mut a: i64, mut b: i64) -> i64 {
        a = a.abs();
        b = b.abs();
        while b != 0 {
            let t = a % b;
            a = b;
            b = t;
        }
        a
    }

    pub fn fraction_addition(expression: String) -> String {
        let chars: Vec<char> = expression.chars().collect();
        let mut numerator = 0i64;
        let mut denominator = 1i64;
        let mut i = 0;
        while i < chars.len() {
            let mut sign = 1i64;
            if chars[i] == '+' || chars[i] == '-' {
                if chars[i] == '-' {
                    sign = -1;
                }
                i += 1;
            }
            let mut a = 0i64;
            while i < chars.len() && chars[i].is_ascii_digit() {
                a = a * 10 + (chars[i] as i64 - '0' as i64);
                i += 1;
            }
            a *= sign;
            i += 1;
            let mut b = 0i64;
            while i < chars.len() && chars[i].is_ascii_digit() {
                b = b * 10 + (chars[i] as i64 - '0' as i64);
                i += 1;
            }
            numerator = numerator * b + a * denominator;
            denominator *= b;
            let g = Self::gcd(numerator, denominator);
            numerator /= g;
            denominator /= g;
        }
        format!("{}/{}", numerator, denominator)
    }
}
"""

FILES["0593_valid_square"] = header("0593", "Valid Square", "valid-square") + """impl Solution {
    fn dist_sq(a: &[i32], b: &[i32]) -> i64 {
        let dx = a[0] as i64 - b[0] as i64;
        let dy = a[1] as i64 - b[1] as i64;
        dx * dx + dy * dy
    }

    pub fn valid_square(p1: Vec<i32>, p2: Vec<i32>, p3: Vec<i32>, p4: Vec<i32>) -> bool {
        let points = [p1, p2, p3, p4];
        let mut distances = Vec::new();
        for i in 0..4 {
            for j in i + 1..4 {
                distances.push(Self::dist_sq(&points[i], &points[j]));
            }
        }
        distances.sort_unstable();
        distances[0] > 0
            && distances[0] == distances[1]
            && distances[1] == distances[2]
            && distances[2] == distances[3]
            && distances[4] == distances[5]
            && distances[4] == 2 * distances[0]
    }
}
"""

FILES["0594_longest_harmonious_subsequence"] = header(
    "0594", "Longest Harmonious Subsequence", "longest-harmonious-subsequence"
) + """use std::collections::HashMap;

impl Solution {
    pub fn find_lhs(nums: Vec<i32>) -> i32 {
        let mut counts = HashMap::new();
        for num in nums {
            *counts.entry(num).or_insert(0) += 1;
        }
        let mut best = 0;
        for (&value, &count) in &counts {
            if let Some(&next) = counts.get(&(value + 1)) {
                best = best.max(count + next);
            }
        }
        best
    }
}
"""

FILES["0598_range_addition_ii"] = header("0598", "Range Addition II", "range-addition-ii") + """impl Solution {
    pub fn max_count(mut m: i32, mut n: i32, ops: Vec<Vec<i32>>) -> i32 {
        for op in ops {
            m = m.min(op[0]);
            n = n.min(op[1]);
        }
        m * n
    }
}
"""

FILES["0599_minimum_index_sum_of_two_lists"] = header(
    "0599", "Minimum Index Sum of Two Lists", "minimum-index-sum-of-two-lists"
) + """use std::collections::HashMap;

impl Solution {
    pub fn find_restaurant(list1: Vec<String>, list2: Vec<String>) -> Vec<String> {
        let mut index1 = HashMap::new();
        for (i, s) in list1.iter().enumerate() {
            index1.insert(s.clone(), i as i32);
        }
        let mut best = i32::MAX;
        let mut answer = Vec::new();
        for (j, s) in list2.iter().enumerate() {
            if let Some(&i) = index1.get(s) {
                let total = i + j as i32;
                if total < best {
                    best = total;
                    answer = vec![s.clone()];
                } else if total == best {
                    answer.push(s.clone());
                }
            }
        }
        answer
    }
}
"""

FILES["0600_non_negative_integers_without_consecutive_ones"] = header(
    "0600",
    "Non-negative Integers without Consecutive Ones",
    "non-negative-integers-without-consecutive-ones",
) + """impl Solution {
    pub fn find_integers(n: i32) -> i32 {
        let mut fib = [0i32; 32];
        fib[0] = 1;
        fib[1] = 2;
        for i in 2..32 {
            fib[i] = fib[i - 1] + fib[i - 2];
        }
        let mut answer = 0;
        let mut prev_bit = 0;
        for bit in (0..=30).rev() {
            if n & (1 << bit) != 0 {
                answer += fib[bit as usize];
                if prev_bit == 1 {
                    return answer;
                }
                prev_bit = 1;
            } else {
                prev_bit = 0;
            }
        }
        answer + 1
    }
}
"""

FILES["0604_design_compressed_string_iterator"] = header(
    "0604", "Design Compressed String Iterator", "design-compressed-string-iterator"
) + """pub struct StringIterator {
    chars: Vec<char>,
    counts: Vec<i32>,
    index: usize,
}

impl StringIterator {
    pub fn new(compressed_string: String) -> Self {
        let chars_in: Vec<char> = compressed_string.chars().collect();
        let mut chars = Vec::new();
        let mut counts = Vec::new();
        let mut i = 0;
        while i < chars_in.len() {
            let ch = chars_in[i];
            i += 1;
            let j_start = i;
            while i < chars_in.len() && chars_in[i].is_ascii_digit() {
                i += 1;
            }
            let num: i32 = chars_in[j_start..i].iter().collect::<String>().parse().unwrap();
            chars.push(ch);
            counts.push(num);
        }
        Self {
            chars,
            counts,
            index: 0,
        }
    }

    pub fn next(&mut self) -> char {
        if !self.has_next() {
            return ' ';
        }
        let ch = self.chars[self.index];
        self.counts[self.index] -= 1;
        if self.counts[self.index] == 0 {
            self.index += 1;
        }
        ch
    }

    pub fn has_next(&self) -> bool {
        self.index < self.chars.len()
    }
}
"""

FILES["0605_can_place_flowers"] = header("0605", "Can Place Flowers", "can-place-flowers") + """impl Solution {
    pub fn can_place_flowers(mut flowerbed: Vec<i32>, mut n: i32) -> bool {
        if n == 0 {
            return true;
        }
        let len = flowerbed.len();
        for i in 0..len {
            if flowerbed[i] == 1 {
                continue;
            }
            let left_empty = i == 0 || flowerbed[i - 1] == 0;
            let right_empty = i == len - 1 || flowerbed[i + 1] == 0;
            if left_empty && right_empty {
                flowerbed[i] = 1;
                n -= 1;
                if n == 0 {
                    return true;
                }
            }
        }
        false
    }
}
"""

FILES["0606_construct_string_from_binary_tree"] = header(
    "0606", "Construct String from Binary Tree", "construct-string-from-binary-tree"
) + TREE + """
impl Solution {
    pub fn tree2str(root: Option<Rc<RefCell<TreeNode>>>) -> String {
        let Some(root) = root else {
            return String::new();
        };
        let node = root.borrow();
        let mut result = node.val.to_string();
        if node.left.is_some() || node.right.is_some() {
            result.push('(');
            result.push_str(&Self::tree2str(node.left.clone()));
            result.push(')');
        }
        if node.right.is_some() {
            result.push('(');
            result.push_str(&Self::tree2str(node.right.clone()));
            result.push(')');
        }
        result
    }
}
"""

FILES["0609_find_duplicate_file_in_system"] = header(
    "0609", "Find Duplicate File in System", "find-duplicate-file-in-system"
) + """use std::collections::HashMap;

impl Solution {
    pub fn find_duplicate(paths: Vec<String>) -> Vec<Vec<String>> {
        let mut content_to_paths: HashMap<String, Vec<String>> = HashMap::new();
        for entry in paths {
            let mut parts = entry.split_whitespace();
            let directory = parts.next().unwrap();
            for file_info in parts {
                let open = file_info.find('(').unwrap();
                let name = &file_info[..open];
                let content = &file_info[open + 1..file_info.len() - 1];
                content_to_paths
                    .entry(content.to_string())
                    .or_default()
                    .push(format!("{}/{}", directory, name));
            }
        }
        content_to_paths
            .into_values()
            .filter(|group| group.len() > 1)
            .collect()
    }
}
"""

FILES["0611_valid_triangle_number"] = header(
    "0611", "Valid Triangle Number", "valid-triangle-number"
) + """impl Solution {
    pub fn triangle_number(mut nums: Vec<i32>) -> i32 {
        nums.sort_unstable();
        let n = nums.len();
        let mut count = 0;
        for k in (2..n).rev() {
            let mut left = 0;
            let mut right = k - 1;
            while left < right {
                if nums[left] + nums[right] > nums[k] {
                    count += (right - left) as i32;
                    right -= 1;
                } else {
                    left += 1;
                }
            }
        }
        count
    }
}
"""

FILES["0616_add_bold_tag_in_string"] = header(
    "0616", "Add Bold Tag in String", "add-bold-tag-in-string"
) + """impl Solution {
    pub fn add_bold_tag(s: String, words: Vec<String>) -> String {
        let n = s.len();
        let mut bold = vec![false; n];
        for word in &words {
            let mut start = 0;
            while let Some(pos) = s[start..].find(word) {
                let abs = start + pos;
                for i in abs..abs + word.len() {
                    bold[i] = true;
                }
                start = abs + 1;
            }
        }
        let bytes = s.as_bytes();
        let mut parts = String::new();
        let mut i = 0;
        while i < n {
            if bold[i] {
                parts.push_str("<b>");
                while i < n && bold[i] {
                    parts.push(bytes[i] as char);
                    i += 1;
                }
                parts.push_str("</b>");
            } else {
                parts.push(bytes[i] as char);
                i += 1;
            }
        }
        parts
    }
}
"""

FILES["0617_merge_two_binary_trees"] = header(
    "0617", "Merge Two Binary Trees", "merge-two-binary-trees"
) + TREE + """
impl Solution {
    pub fn merge_trees(
        root1: Option<Rc<RefCell<TreeNode>>>,
        root2: Option<Rc<RefCell<TreeNode>>>,
    ) -> Option<Rc<RefCell<TreeNode>>> {
        match (root1, root2) {
            (None, r) | (r, None) => r,
            (Some(a), Some(b)) => {
                let mut a_ref = a.borrow_mut();
                let b_ref = b.borrow();
                a_ref.val += b_ref.val;
                let left = Self::merge_trees(a_ref.left.clone(), b_ref.left.clone());
                let right = Self::merge_trees(a_ref.right.clone(), b_ref.right.clone());
                a_ref.left = left;
                a_ref.right = right;
                drop(a_ref);
                Some(a)
            }
        }
    }
}
"""

FILES["0621_task_scheduler"] = header("0621", "Task Scheduler", "task-scheduler") + """impl Solution {
    pub fn least_interval(tasks: Vec<char>, n: i32) -> i32 {
        let mut counts = [0i32; 26];
        for task in &tasks {
            counts[(*task as u8 - b'A') as usize] += 1;
        }
        let max_freq = *counts.iter().max().unwrap();
        let max_count = counts.iter().filter(|&&c| c == max_freq).count() as i32;
        (tasks.len() as i32).max((max_freq - 1) * (n + 1) + max_count)
    }
}
"""

FILES["0622_design_circular_queue"] = header(
    "0622", "Design Circular Queue", "design-circular-queue"
) + """pub struct MyCircularQueue {
    data: Vec<i32>,
    capacity: usize,
    head: usize,
    size: usize,
}

impl MyCircularQueue {
    pub fn new(k: i32) -> Self {
        Self {
            data: vec![0; k as usize],
            capacity: k as usize,
            head: 0,
            size: 0,
        }
    }

    pub fn en_queue(&mut self, value: i32) -> bool {
        if self.is_full() {
            return false;
        }
        self.data[(self.head + self.size) % self.capacity] = value;
        self.size += 1;
        true
    }

    pub fn de_queue(&mut self) -> bool {
        if self.is_empty() {
            return false;
        }
        self.head = (self.head + 1) % self.capacity;
        self.size -= 1;
        true
    }

    pub fn front(&self) -> i32 {
        if self.is_empty() {
            -1
        } else {
            self.data[self.head]
        }
    }

    pub fn rear(&self) -> i32 {
        if self.is_empty() {
            -1
        } else {
            self.data[(self.head + self.size - 1) % self.capacity]
        }
    }

    pub fn is_empty(&self) -> bool {
        self.size == 0
    }

    pub fn is_full(&self) -> bool {
        self.size == self.capacity
    }
}
"""

FILES["0623_add_one_row_to_tree"] = header("0623", "Add One Row to Tree", "add-one-row-to-tree") + TREE + """
impl Solution {
    fn dfs(node: &Option<Rc<RefCell<TreeNode>>>, current: i32, val: i32, depth: i32) {
        let Some(node) = node else {
            return;
        };
        let mut node = node.borrow_mut();
        if current == depth - 1 {
            node.left = Some(Rc::new(RefCell::new(TreeNode {
                val,
                left: node.left.clone(),
                right: None,
            })));
            node.right = Some(Rc::new(RefCell::new(TreeNode {
                val,
                left: None,
                right: node.right.clone(),
            })));
            return;
        }
        Self::dfs(&node.left, current + 1, val, depth);
        Self::dfs(&node.right, current + 1, val, depth);
    }

    pub fn add_one_row(
        root: Option<Rc<RefCell<TreeNode>>>,
        val: i32,
        depth: i32,
    ) -> Option<Rc<RefCell<TreeNode>>> {
        if depth == 1 {
            return Some(Rc::new(RefCell::new(TreeNode {
                val,
                left: root,
                right: None,
            })));
        }
        Self::dfs(&root, 1, val, depth);
        root
    }
}
"""

FILES["0624_maximum_distance_in_arrays"] = header(
    "0624", "Maximum Distance in Arrays", "maximum-distance-in-arrays"
) + """impl Solution {
    pub fn max_distance(arrays: Vec<Vec<i32>>) -> i32 {
        let mut min_val = arrays[0][0];
        let mut max_val = *arrays[0].last().unwrap();
        let mut best = 0;
        for arr in arrays.iter().skip(1) {
            let first = arr[0];
            let last = *arr.last().unwrap();
            best = best.max((last - min_val).abs()).max((max_val - first).abs());
            min_val = min_val.min(first);
            max_val = max_val.max(last);
        }
        best
    }
}
"""

FILES["0625_minimum_factorization"] = header(
    "0625", "Minimum Factorization", "minimum-factorization"
) + """impl Solution {
    pub fn smallest_factorization(mut num: i32) -> i32 {
        if num < 10 {
            return num;
        }
        let mut digits = Vec::new();
        for digit in (2..=9).rev() {
            while num % digit == 0 {
                digits.push(digit);
                num /= digit;
            }
        }
        if num != 1 {
            return 0;
        }
        let mut result = 0i64;
        for &d in digits.iter().rev() {
            result = result * 10 + d as i64;
            if result > i32::MAX as i64 {
                return 0;
            }
        }
        result as i32
    }
}
"""

FILES["0628_maximum_product_of_three_numbers"] = header(
    "0628", "Maximum Product of Three Numbers", "maximum-product-of-three-numbers"
) + """impl Solution {
    pub fn maximum_product(mut nums: Vec<i32>) -> i32 {
        nums.sort_unstable();
        let n = nums.len();
        (nums[n - 1] * nums[n - 2] * nums[n - 3]).max(nums[0] * nums[1] * nums[n - 1])
    }
}
"""

FILES["0629_k_inverse_pairs_array"] = header(
    "0629", "K Inverse Pairs Array", "k-inverse-pairs-array"
) + """impl Solution {
    pub fn k_inverse_pairs(n: i32, k: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let k = k as usize;
        let mut dp = vec![0i64; k + 1];
        dp[0] = 1;
        for size in 1..=n {
            let mut nxt = vec![0i64; k + 1];
            let mut prefix = 0i64;
            for pairs in 0..=k {
                prefix = (prefix + dp[pairs]) % MOD;
                if pairs as i32 >= size {
                    prefix = (prefix - dp[pairs - size as usize] + MOD) % MOD;
                }
                nxt[pairs] = prefix;
            }
            dp = nxt;
        }
        dp[k] as i32
    }
}
"""

FILES["0630_course_schedule_iii"] = header("0630", "Course Schedule III", "course-schedule-iii") + """use std::collections::BinaryHeap;

impl Solution {
    pub fn schedule_course(mut courses: Vec<Vec<i32>>) -> i32 {
        courses.sort_by_key(|c| c[1]);
        let mut heap = BinaryHeap::new();
        let mut time = 0;
        for course in courses {
            let duration = course[0];
            let last_day = course[1];
            if time + duration <= last_day {
                heap.push(duration);
                time += duration;
            } else if let Some(&top) = heap.peek() {
                if top > duration {
                    time += duration - top;
                    heap.pop();
                    heap.push(duration);
                }
            }
        }
        heap.len() as i32
    }
}
"""

FILES["0631_design_excel_sum_formula"] = header(
    "0631", "Design Excel Sum Formula", "design-excel-sum-formula"
) + """use std::collections::HashMap;

pub struct Excel {
    values: Vec<Vec<i32>>,
    formulas: HashMap<(i32, usize), Vec<(i32, usize)>>,
}

impl Excel {
    pub fn new(height: i32, width: char) -> Self {
        let width = (width as u8 - b'A' + 1) as usize;
        Self {
            values: vec![vec![0; width]; (height + 1) as usize],
            formulas: HashMap::new(),
        }
    }

    fn parse(cell: &str) -> (i32, usize) {
        let col = (cell.as_bytes()[0] - b'A') as usize;
        let row: i32 = cell[1..].parse().unwrap();
        (row, col)
    }

    fn eval(&self, row: i32, col: usize) -> i32 {
        if let Some(cells) = self.formulas.get(&(row, col)) {
            return cells.iter().map(|&(r, c)| self.eval(r, c)).sum();
        }
        self.values[row as usize][col]
    }

    pub fn set(&mut self, row: i32, column: char, val: i32) {
        let col = (column as u8 - b'A') as usize;
        self.formulas.remove(&(row, col));
        self.values[row as usize][col] = val;
    }

    pub fn get(&self, row: i32, column: char) -> i32 {
        self.eval(row, (column as u8 - b'A') as usize)
    }

    pub fn sum(&mut self, row: i32, column: char, numbers: Vec<String>) -> i32 {
        let col = (column as u8 - b'A') as usize;
        let mut cells = Vec::new();
        for token in numbers {
            if let Some(pos) = token.find(':') {
                let (r1, c1) = Self::parse(&token[..pos]);
                let (r2, c2) = Self::parse(&token[pos + 1..]);
                for r in r1..=r2 {
                    for c in c1..=c2 {
                        cells.push((r, c));
                    }
                }
            } else {
                cells.push(Self::parse(&token));
            }
        }
        self.formulas.insert((row, col), cells);
        self.eval(row, col)
    }
}
"""

FILES["0632_smallest_range_covering_elements_from_k_lists"] = header(
    "0632",
    "Smallest Range Covering Elements from K Lists",
    "smallest-range-covering-elements-from-k-lists",
) + """use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn smallest_range(nums: Vec<Vec<i32>>) -> Vec<i32> {
        let mut heap: BinaryHeap<Reverse<(i32, usize, usize)>> = BinaryHeap::new();
        let mut current_max = i32::MIN;
        for (i, list) in nums.iter().enumerate() {
            heap.push(Reverse((list[0], i, 0)));
            current_max = current_max.max(list[0]);
        }
        let Reverse((first, _, _)) = *heap.peek().unwrap();
        let mut best_left = first;
        let mut best_right = current_max;
        loop {
            let Reverse((value, list_index, index)) = heap.pop().unwrap();
            if current_max - value < best_right - best_left {
                best_left = value;
                best_right = current_max;
            }
            if index + 1 == nums[list_index].len() {
                break;
            }
            let nxt = nums[list_index][index + 1];
            heap.push(Reverse((nxt, list_index, index + 1)));
            current_max = current_max.max(nxt);
        }
        vec![best_left, best_right]
    }
}
"""

FILES["0633_sum_of_square_numbers"] = header(
    "0633", "Sum of Square Numbers", "sum-of-square-numbers"
) + """impl Solution {
    pub fn judge_square_sum(c: i32) -> bool {
        let mut left: i64 = 0;
        let mut right = (c as f64).sqrt() as i64;
        while left <= right {
            let total = left * left + right * right;
            if total == c as i64 {
                return true;
            }
            if total < c as i64 {
                left += 1;
            } else {
                right -= 1;
            }
        }
        false
    }
}
"""

FILES["0634_find_the_derangement_of_an_array"] = header(
    "0634", "Find the Derangement of An Array", "find-the-derangement-of-an-array"
) + """impl Solution {
    pub fn find_derangement(n: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        if n == 1 {
            return 0;
        }
        let mut prev2 = 0i64;
        let mut prev1 = 1i64;
        for size in 3..=n {
            let next = (size as i64 - 1) * (prev1 + prev2) % MOD;
            prev2 = prev1;
            prev1 = next;
        }
        prev1 as i32
    }
}
"""

FILES["0635_design_log_storage_system"] = header(
    "0635", "Design Log Storage System", "design-log-storage-system"
) + """use std::collections::HashMap;

pub struct LogSystem {
    logs: Vec<(i32, String)>,
    granularity_index: HashMap<String, usize>,
}

impl LogSystem {
    pub fn new() -> Self {
        let mut granularity_index = HashMap::new();
        granularity_index.insert("Year".to_string(), 4);
        granularity_index.insert("Month".to_string(), 7);
        granularity_index.insert("Day".to_string(), 10);
        granularity_index.insert("Hour".to_string(), 13);
        granularity_index.insert("Minute".to_string(), 16);
        granularity_index.insert("Second".to_string(), 19);
        Self {
            logs: Vec::new(),
            granularity_index,
        }
    }

    pub fn put(&mut self, id: i32, timestamp: String) {
        self.logs.push((id, timestamp));
    }

    pub fn retrieve(&self, start: String, end: String, granularity: String) -> Vec<i32> {
        let index = self.granularity_index[&granularity];
        let start_key = &start[..index];
        let end_key = &end[..index];
        let mut matched = Vec::new();
        for (log_id, timestamp) in &self.logs {
            let key = &timestamp[..index];
            if start_key <= key && key <= end_key {
                matched.push((timestamp.clone(), *log_id));
            }
        }
        matched.sort();
        matched.into_iter().map(|(_, id)| id).collect()
    }
}
"""

FILES["0636_exclusive_time_of_functions"] = header(
    "0636", "Exclusive Time of Functions", "exclusive-time-of-functions"
) + """impl Solution {
    pub fn exclusive_time(n: i32, logs: Vec<String>) -> Vec<i32> {
        let mut result = vec![0; n as usize];
        let mut stack = Vec::new();
        let mut prev_time = 0;
        for log in logs {
            let mut parts = log.split(':');
            let func_id: usize = parts.next().unwrap().parse().unwrap();
            let event = parts.next().unwrap();
            let time: i32 = parts.next().unwrap().parse().unwrap();
            if event == "start" {
                if let Some(&top) = stack.last() {
                    result[top] += time - prev_time;
                }
                stack.push(func_id);
                prev_time = time;
            } else {
                let top = stack.pop().unwrap();
                result[top] += time - prev_time + 1;
                prev_time = time + 1;
            }
        }
        result
    }
}
"""

FILES["0637_average_of_levels_in_binary_tree"] = header(
    "0637", "Average of Levels in Binary Tree", "average-of-levels-in-binary-tree"
) + TREE + """use std::collections::VecDeque;

impl Solution {
    pub fn average_of_levels(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<f64> {
        let mut result = Vec::new();
        let Some(root) = root else {
            return result;
        };
        let mut queue = VecDeque::new();
        queue.push_back(root);
        while !queue.is_empty() {
            let count = queue.len();
            let mut total = 0i64;
            for _ in 0..count {
                let node = queue.pop_front().unwrap();
                let node = node.borrow();
                total += node.val as i64;
                if let Some(left) = node.left.clone() {
                    queue.push_back(left);
                }
                if let Some(right) = node.right.clone() {
                    queue.push_back(right);
                }
            }
            result.push(total as f64 / count as f64);
        }
        result
    }
}
"""

FILES["0638_shopping_offers"] = header("0638", "Shopping Offers", "shopping-offers") + """use std::collections::HashMap;

impl Solution {
    fn dfs(
        state: Vec<i32>,
        price: &[i32],
        special: &[Vec<i32>],
        memo: &mut HashMap<Vec<i32>, i32>,
    ) -> i32 {
        if let Some(&cached) = memo.get(&state) {
            return cached;
        }
        let mut cost = 0;
        for i in 0..price.len() {
            cost += state[i] * price[i];
        }
        for offer in special {
            let mut nxt = state.clone();
            let mut valid = true;
            for i in 0..price.len() {
                if nxt[i] < offer[i] {
                    valid = false;
                    break;
                }
                nxt[i] -= offer[i];
            }
            if valid {
                cost = cost.min(offer[price.len()] + Self::dfs(nxt, price, special, memo));
            }
        }
        memo.insert(state, cost);
        cost
    }

    pub fn shopping_offers(price: Vec<i32>, special: Vec<Vec<i32>>, needs: Vec<i32>) -> i32 {
        let mut memo = HashMap::new();
        Self::dfs(needs, &price, &special, &mut memo)
    }
}
"""

FILES["0639_decode_ways_ii"] = header("0639", "Decode Ways II", "decode-ways-ii") + """impl Solution {
    fn one(ch: u8) -> i64 {
        match ch {
            b'*' => 9,
            b'0' => 0,
            _ => 1,
        }
    }

    fn two(a: u8, b: u8) -> i64 {
        if a == b'*' && b == b'*' {
            return 15;
        }
        if a == b'*' {
            return if b <= b'6' { 2 } else { 1 };
        }
        if b == b'*' {
            return match a {
                b'1' => 9,
                b'2' => 6,
                _ => 0,
            };
        }
        let value = (a - b'0') as i32 * 10 + (b - b'0') as i32;
        if (10..=26).contains(&value) { 1 } else { 0 }
    }

    pub fn num_decodings(s: String) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let s = s.as_bytes();
        let mut prev2 = 1i64;
        let mut prev1 = Self::one(s[0]);
        for i in 1..s.len() {
            let cur = (Self::one(s[i]) * prev1 + Self::two(s[i - 1], s[i]) * prev2) % MOD;
            prev2 = prev1;
            prev1 = cur;
        }
        prev1 as i32
    }
}
"""

FILES["0640_solve_the_equation"] = header("0640", "Solve the Equation", "solve-the-equation") + """impl Solution {
    fn parse(expr: &str) -> (i32, i32) {
        let chars: Vec<char> = expr.chars().collect();
        let mut coef = 0;
        let mut constant = 0;
        let mut i = 0;
        while i < chars.len() {
            let mut sign = 1;
            if chars[i] == '+' || chars[i] == '-' {
                sign = if chars[i] == '-' { -1 } else { 1 };
                i += 1;
            }
            let mut value = 0;
            let mut has_digit = false;
            while i < chars.len() && chars[i].is_ascii_digit() {
                has_digit = true;
                value = value * 10 + (chars[i] as i32 - '0' as i32);
                i += 1;
            }
            if i < chars.len() && chars[i] == 'x' {
                coef += sign * if has_digit { value } else { 1 };
                i += 1;
            } else {
                constant += sign * value;
            }
        }
        (coef, constant)
    }

    pub fn solve_equation(equation: String) -> String {
        let eq = equation.find('=').unwrap();
        let (left_coef, left_const) = Self::parse(&equation[..eq]);
        let (right_coef, right_const) = Self::parse(&equation[eq + 1..]);
        let coef = left_coef - right_coef;
        let constant = right_const - left_const;
        if coef == 0 {
            return if constant == 0 {
                "Infinite solutions".to_string()
            } else {
                "No solution".to_string()
            };
        }
        format!("x={}", constant / coef)
    }
}
"""

FILES["0641_design_circular_deque"] = header(
    "0641", "Design Circular Deque", "design-circular-deque"
) + """pub struct MyCircularDeque {
    data: Vec<i32>,
    capacity: usize,
    front: usize,
    size: usize,
}

impl MyCircularDeque {
    pub fn new(k: i32) -> Self {
        Self {
            data: vec![0; k as usize],
            capacity: k as usize,
            front: 0,
            size: 0,
        }
    }

    pub fn insert_front(&mut self, value: i32) -> bool {
        if self.is_full() {
            return false;
        }
        self.front = (self.front + self.capacity - 1) % self.capacity;
        self.data[self.front] = value;
        self.size += 1;
        true
    }

    pub fn insert_last(&mut self, value: i32) -> bool {
        if self.is_full() {
            return false;
        }
        self.data[(self.front + self.size) % self.capacity] = value;
        self.size += 1;
        true
    }

    pub fn delete_front(&mut self) -> bool {
        if self.is_empty() {
            return false;
        }
        self.front = (self.front + 1) % self.capacity;
        self.size -= 1;
        true
    }

    pub fn delete_last(&mut self) -> bool {
        if self.is_empty() {
            return false;
        }
        self.size -= 1;
        true
    }

    pub fn get_front(&self) -> i32 {
        if self.is_empty() { -1 } else { self.data[self.front] }
    }

    pub fn get_rear(&self) -> i32 {
        if self.is_empty() {
            -1
        } else {
            self.data[(self.front + self.size - 1) % self.capacity]
        }
    }

    pub fn is_empty(&self) -> bool {
        self.size == 0
    }

    pub fn is_full(&self) -> bool {
        self.size == self.capacity
    }
}
"""

FILES["0642_design_search_autocomplete_system"] = header(
    "0642", "Design Search Autocomplete System", "design-search-autocomplete-system"
) + """use std::collections::HashMap;

pub struct AutocompleteSystem {
    counts: HashMap<String, i32>,
    current: String,
}

impl AutocompleteSystem {
    pub fn new(sentences: Vec<String>, times: Vec<i32>) -> Self {
        let mut counts = HashMap::new();
        for (sentence, time) in sentences.into_iter().zip(times) {
            *counts.entry(sentence).or_insert(0) += time;
        }
        Self {
            counts,
            current: String::new(),
        }
    }

    pub fn input(&mut self, c: char) -> Vec<String> {
        if c == '#' {
            *self.counts.entry(self.current.clone()).or_insert(0) += 1;
            self.current.clear();
            return Vec::new();
        }
        self.current.push(c);
        let mut matches: Vec<String> = self
            .counts
            .keys()
            .filter(|s| s.starts_with(&self.current))
            .cloned()
            .collect();
        matches.sort_by(|a, b| {
            let ca = self.counts[a];
            let cb = self.counts[b];
            if ca != cb {
                cb.cmp(&ca)
            } else {
                a.cmp(b)
            }
        });
        matches.truncate(3);
        matches
    }
}
"""

FILES["0643_maximum_average_subarray_i"] = header(
    "0643", "Maximum Average Subarray I", "maximum-average-subarray-i"
) + """impl Solution {
    pub fn find_max_average(nums: Vec<i32>, k: i32) -> f64 {
        let k = k as usize;
        let mut window: i64 = nums[..k].iter().map(|&x| x as i64).sum();
        let mut best = window;
        for i in k..nums.len() {
            window += nums[i] as i64 - nums[i - k] as i64;
            best = best.max(window);
        }
        best as f64 / k as f64
    }
}
"""

FILES["0644_maximum_average_subarray_ii"] = header(
    "0644", "Maximum Average Subarray II", "maximum-average-subarray-ii"
) + """impl Solution {
    fn can_reach(nums: &[i32], k: usize, mid: f64) -> bool {
        let mut prefix = 0.0;
        for i in 0..k {
            prefix += nums[i] as f64 - mid;
        }
        if prefix >= 0.0 {
            return true;
        }
        let mut prev = 0.0;
        let mut min_prev = 0.0;
        for i in k..nums.len() {
            prefix += nums[i] as f64 - mid;
            prev += nums[i - k] as f64 - mid;
            min_prev = min_prev.min(prev);
            if prefix - min_prev >= 0.0 {
                return true;
            }
        }
        false
    }

    pub fn find_max_average(nums: Vec<i32>, k: i32) -> f64 {
        let mut left = *nums.iter().min().unwrap() as f64;
        let mut right = *nums.iter().max().unwrap() as f64;
        for _ in 0..80 {
            let mid = (left + right) / 2.0;
            if Self::can_reach(&nums, k as usize, mid) {
                left = mid;
            } else {
                right = mid;
            }
        }
        left
    }
}
"""

FILES["0645_set_mismatch"] = header("0645", "Set Mismatch", "set-mismatch") + """impl Solution {
    pub fn find_error_nums(nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len();
        let mut seen = vec![0; n + 1];
        let mut duplicate = -1;
        let mut missing = -1;
        for value in nums {
            seen[value as usize] += 1;
        }
        for value in 1..=n {
            if seen[value] == 2 {
                duplicate = value as i32;
            } else if seen[value] == 0 {
                missing = value as i32;
            }
        }
        vec![duplicate, missing]
    }
}
"""

FILES["0646_maximum_length_of_pair_chain"] = header(
    "0646", "Maximum Length of Pair Chain", "maximum-length-of-pair-chain"
) + """impl Solution {
    pub fn find_longest_chain(mut pairs: Vec<Vec<i32>>) -> i32 {
        pairs.sort_by_key(|p| p[1]);
        let mut length = 0;
        let mut current_end = i32::MIN;
        for pair in pairs {
            if pair[0] > current_end {
                length += 1;
                current_end = pair[1];
            }
        }
        length
    }
}
"""

FILES["0647_palindromic_substrings"] = header(
    "0647", "Palindromic Substrings", "palindromic-substrings"
) + """impl Solution {
    fn expand(s: &[u8], mut left: i32, mut right: i32) -> i32 {
        let mut count = 0;
        while left >= 0 && right < s.len() as i32 && s[left as usize] == s[right as usize] {
            count += 1;
            left -= 1;
            right += 1;
        }
        count
    }

    pub fn count_substrings(s: String) -> i32 {
        let s = s.as_bytes();
        let mut total = 0;
        for i in 0..s.len() {
            total += Self::expand(s, i as i32, i as i32);
            total += Self::expand(s, i as i32, i as i32 + 1);
        }
        total
    }
}
"""

FILES["0648_replace_words"] = header("0648", "Replace Words", "replace-words") + """use std::collections::HashSet;

impl Solution {
    pub fn replace_words(dictionary: Vec<String>, sentence: String) -> String {
        let roots: HashSet<String> = dictionary.into_iter().collect();
        sentence
            .split_whitespace()
            .map(|word| {
                for i in 1..=word.len() {
                    if roots.contains(&word[..i]) {
                        return word[..i].to_string();
                    }
                }
                word.to_string()
            })
            .collect::<Vec<_>>()
            .join(" ")
    }
}
"""

FILES["0649_dota2_senate"] = header("0649", "Dota2 Senate", "dota2-senate") + """use std::collections::VecDeque;

impl Solution {
    pub fn predict_party_victory(senate: String) -> String {
        let mut radiant = VecDeque::new();
        let mut dire = VecDeque::new();
        let n = senate.len() as i32;
        for (i, ch) in senate.chars().enumerate() {
            if ch == 'R' {
                radiant.push_back(i as i32);
            } else {
                dire.push_back(i as i32);
            }
        }
        while !radiant.is_empty() && !dire.is_empty() {
            let r = radiant.pop_front().unwrap();
            let d = dire.pop_front().unwrap();
            if r < d {
                radiant.push_back(r + n);
            } else {
                dire.push_back(d + n);
            }
        }
        if radiant.is_empty() {
            "Dire".to_string()
        } else {
            "Radiant".to_string()
        }
    }
}
"""

FILES["0650_2_keys_keyboard"] = header("0650", "2 Keys Keyboard", "2-keys-keyboard") + """impl Solution {
    pub fn min_steps(mut n: i32) -> i32 {
        let mut steps = 0;
        let mut factor = 2;
        while factor * factor <= n {
            while n % factor == 0 {
                steps += factor;
                n /= factor;
            }
            factor += 1;
        }
        if n > 1 {
            steps += n;
        }
        steps
    }
}
"""

FILES["0651_4_keys_keyboard"] = header("0651", "4 Keys Keyboard", "4-keys-keyboard") + """impl Solution {
    pub fn max_a(n: i32) -> i32 {
        let n = n as usize;
        let mut dp: Vec<i32> = (0..=n as i32).collect();
        for i in 1..=n {
            for j in 0..i.saturating_sub(2) {
                dp[i] = dp[i].max(dp[j] * (i - j - 1) as i32);
            }
        }
        dp[n]
    }
}
"""

FILES["0652_find_duplicate_subtrees"] = header(
    "0652", "Find Duplicate Subtrees", "find-duplicate-subtrees"
) + TREE + """use std::collections::HashMap;

impl Solution {
    fn serialize(
        node: &Option<Rc<RefCell<TreeNode>>>,
        counts: &mut HashMap<String, i32>,
        result: &mut Vec<Option<Rc<RefCell<TreeNode>>>>,
    ) -> String {
        let Some(node_rc) = node else {
            return "#".to_string();
        };
        let node = node_rc.borrow();
        let key = format!(
            "{},{},{}",
            node.val,
            Self::serialize(&node.left, counts, result),
            Self::serialize(&node.right, counts, result)
        );
        let count = counts.entry(key.clone()).or_insert(0);
        *count += 1;
        if *count == 2 {
            result.push(Some(node_rc.clone()));
        }
        key
    }

    pub fn find_duplicate_subtrees(
        root: Option<Rc<RefCell<TreeNode>>>,
    ) -> Vec<Option<Rc<RefCell<TreeNode>>>> {
        let mut counts = HashMap::new();
        let mut result = Vec::new();
        Self::serialize(&root, &mut counts, &mut result);
        result
    }
}
"""

FILES["0653_two_sum_iv_input_is_a_bst"] = header(
    "0653", "Two Sum IV - Input is a BST", "two-sum-iv-input-is-a-bst"
) + TREE + """use std::collections::HashSet;

impl Solution {
    fn dfs(node: &Option<Rc<RefCell<TreeNode>>>, k: i32, seen: &mut HashSet<i32>) -> bool {
        let Some(node) = node else {
            return false;
        };
        let node = node.borrow();
        if seen.contains(&(k - node.val)) {
            return true;
        }
        seen.insert(node.val);
        Self::dfs(&node.left, k, seen) || Self::dfs(&node.right, k, seen)
    }

    pub fn find_target(root: Option<Rc<RefCell<TreeNode>>>, k: i32) -> bool {
        let mut seen = HashSet::new();
        Self::dfs(&root, k, &mut seen)
    }
}
"""

FILES["0654_maximum_binary_tree"] = header("0654", "Maximum Binary Tree", "maximum-binary-tree") + TREE + """
impl Solution {
    fn build(nums: &[i32], left: i32, right: i32) -> Option<Rc<RefCell<TreeNode>>> {
        if left > right {
            return None;
        }
        let mut mid = left;
        for i in left..=right {
            if nums[i as usize] > nums[mid as usize] {
                mid = i;
            }
        }
        Some(Rc::new(RefCell::new(TreeNode {
            val: nums[mid as usize],
            left: Self::build(nums, left, mid - 1),
            right: Self::build(nums, mid + 1, right),
        })))
    }

    pub fn construct_maximum_binary_tree(nums: Vec<i32>) -> Option<Rc<RefCell<TreeNode>>> {
        Self::build(&nums, 0, nums.len() as i32 - 1)
    }
}
"""

FILES["0655_print_binary_tree"] = header("0655", "Print Binary Tree", "print-binary-tree") + TREE + """
impl Solution {
    fn height(node: &Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let Some(node) = node else {
            return -1;
        };
        let node = node.borrow();
        1 + Self::height(&node.left).max(Self::height(&node.right))
    }

    fn place(
        node: &Option<Rc<RefCell<TreeNode>>>,
        r: usize,
        c: usize,
        h: i32,
        res: &mut Vec<Vec<String>>,
    ) {
        let Some(node) = node else {
            return;
        };
        let node = node.borrow();
        res[r][c] = node.val.to_string();
        if r as i32 == h {
            return;
        }
        let offset = 1 << (h - r as i32 - 1);
        Self::place(&node.left, r + 1, c - offset as usize, h, res);
        Self::place(&node.right, r + 1, c + offset as usize, h, res);
    }

    pub fn print_tree(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<Vec<String>> {
        let h = Self::height(&root);
        let rows = (h + 1) as usize;
        let cols = (1 << (h + 1)) - 1;
        let mut res = vec![vec![String::new(); cols as usize]; rows];
        Self::place(&root, 0, (cols as usize - 1) / 2, h, &mut res);
        res
    }
}
"""

FILES["0656_coin_path"] = header("0656", "Coin Path", "coin-path") + """impl Solution {
    pub fn cheapest_jump(coins: Vec<i32>, max_jump: i32) -> Vec<i32> {
        let n = coins.len();
        if coins[n - 1] == -1 {
            return Vec::new();
        }
        let inf = i64::MAX / 4;
        let mut cost = vec![inf; n];
        let mut nxt = vec![-1i32; n];
        cost[n - 1] = coins[n - 1] as i64;
        for i in (0..n - 1).rev() {
            if coins[i] == -1 {
                continue;
            }
            for jump in 1..=max_jump {
                let j = i + jump as usize;
                if j >= n {
                    break;
                }
                if cost[j] == inf {
                    continue;
                }
                let candidate = coins[i] as i64 + cost[j];
                if candidate < cost[i] || (candidate == cost[i] && (nxt[i] == -1 || j as i32 < nxt[i])) {
                    cost[i] = candidate;
                    nxt[i] = j as i32;
                }
            }
        }
        if cost[0] == inf {
            return Vec::new();
        }
        let mut path = vec![1];
        let mut i = 0;
        while i != n - 1 {
            i = nxt[i] as usize;
            path.push(i as i32 + 1);
        }
        path
    }
}
"""

FILES["0657_robot_return_to_origin"] = header(
    "0657", "Robot Return to Origin", "robot-return-to-origin"
) + """impl Solution {
    pub fn judge_circle(moves: String) -> bool {
        let mut x = 0;
        let mut y = 0;
        for mv in moves.chars() {
            match mv {
                'U' => y += 1,
                'D' => y -= 1,
                'L' => x -= 1,
                'R' => x += 1,
                _ => {}
            }
        }
        x == 0 && y == 0
    }
}
"""

FILES["0658_find_k_closest_elements"] = header(
    "0658", "Find K Closest Elements", "find-k-closest-elements"
) + """impl Solution {
    pub fn find_closest_elements(arr: Vec<i32>, k: i32, x: i32) -> Vec<i32> {
        let k = k as usize;
        let mut left = 0;
        let mut right = arr.len() - k;
        while left < right {
            let mid = left + (right - left) / 2;
            if x - arr[mid] > arr[mid + k] - x {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        arr[left..left + k].to_vec()
    }
}
"""

FILES["0659_split_array_into_consecutive_subsequences"] = header(
    "0659",
    "Split Array into Consecutive Subsequences",
    "split-array-into-consecutive-subsequences",
) + """use std::collections::HashMap;

impl Solution {
    pub fn is_possible(nums: Vec<i32>) -> bool {
        let mut freq = HashMap::new();
        let mut tails = HashMap::new();
        for &num in &nums {
            *freq.entry(num).or_insert(0) += 1;
        }
        for &num in &nums {
            if freq[&num] == 0 {
                continue;
            }
            *freq.get_mut(&num).unwrap() -= 1;
            if *tails.get(&(num - 1)).unwrap_or(&0) > 0 {
                *tails.get_mut(&(num - 1)).unwrap() -= 1;
                *tails.entry(num).or_insert(0) += 1;
            } else if *freq.get(&(num + 1)).unwrap_or(&0) > 0 && *freq.get(&(num + 2)).unwrap_or(&0) > 0 {
                *freq.get_mut(&(num + 1)).unwrap() -= 1;
                *freq.get_mut(&(num + 2)).unwrap() -= 1;
                *tails.entry(num + 2).or_insert(0) += 1;
            } else {
                return false;
            }
        }
        true
    }
}
"""

FILES["0660_remove_9"] = header("0660", "Remove 9", "remove-9") + """impl Solution {
    pub fn new_integer(mut n: i32) -> i32 {
        let mut result = 0;
        let mut base = 1;
        while n > 0 {
            result += (n % 9) * base;
            n /= 9;
            base *= 10;
        }
        result
    }
}
"""

FILES["0661_image_smoother"] = header("0661", "Image Smoother", "image-smoother") + """impl Solution {
    pub fn image_smoother(img: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let m = img.len();
        let n = img[0].len();
        let mut out = vec![vec![0; n]; m];
        for i in 0..m {
            for j in 0..n {
                let mut total = 0;
                let mut count = 0;
                for di in -1i32..=1 {
                    for dj in -1i32..=1 {
                        let ni = i as i32 + di;
                        let nj = j as i32 + dj;
                        if ni >= 0 && ni < m as i32 && nj >= 0 && nj < n as i32 {
                            total += img[ni as usize][nj as usize];
                            count += 1;
                        }
                    }
                }
                out[i][j] = total / count;
            }
        }
        out
    }
}
"""

FILES["0662_maximum_width_of_binary_tree"] = header(
    "0662", "Maximum Width of Binary Tree", "maximum-width-of-binary-tree"
) + TREE + """use std::collections::VecDeque;

impl Solution {
    pub fn width_of_binary_tree(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let Some(root) = root else {
            return 0;
        };
        let mut queue = VecDeque::new();
        queue.push_back((root, 0u64));
        let mut best = 0i32;
        while !queue.is_empty() {
            let left = queue.front().unwrap().1;
            let size = queue.len();
            for _ in 0..size {
                let (node, idx) = queue.pop_front().unwrap();
                best = best.max((idx - left + 1) as i32);
                let node = node.borrow();
                if let Some(left_child) = node.left.clone() {
                    queue.push_back((left_child, idx * 2));
                }
                if let Some(right_child) = node.right.clone() {
                    queue.push_back((right_child, idx * 2 + 1));
                }
            }
        }
        best
    }
}
"""

FILES["0663_equal_tree_partition"] = header("0663", "Equal Tree Partition", "equal-tree-partition") + TREE + """
impl Solution {
    fn dfs(node: &Option<Rc<RefCell<TreeNode>>>, sums: &mut Vec<i32>) -> i32 {
        let Some(node) = node else {
            return 0;
        };
        let node = node.borrow();
        let total = node.val + Self::dfs(&node.left, sums) + Self::dfs(&node.right, sums);
        sums.push(total);
        total
    }

    pub fn check_equal_tree(root: Option<Rc<RefCell<TreeNode>>>) -> bool {
        let mut subtree_sums = Vec::new();
        let total = Self::dfs(&root, &mut subtree_sums);
        if !subtree_sums.is_empty() {
            subtree_sums.pop();
        }
        if total % 2 != 0 {
            return false;
        }
        let half = total / 2;
        subtree_sums.iter().any(|&s| s == half)
    }
}
"""

FILES["0664_strange_printer"] = header("0664", "Strange Printer", "strange-printer") + """impl Solution {
    pub fn strange_printer(s: String) -> i32 {
        let s = s.as_bytes();
        let n = s.len();
        if n == 0 {
            return 0;
        }
        let mut dp = vec![vec![0i32; n]; n];
        for i in (0..n).rev() {
            dp[i][i] = 1;
            for j in i + 1..n {
                dp[i][j] = dp[i + 1][j] + 1;
                for k in i + 1..=j {
                    if s[k] == s[i] {
                        let extra = if k + 1 <= j { dp[k + 1][j] } else { 0 };
                        dp[i][j] = dp[i][j].min(dp[i][k - 1] + extra);
                    }
                }
            }
        }
        dp[0][n - 1]
    }
}
"""

FILES["0665_non_decreasing_array"] = header(
    "0665", "Non-decreasing Array", "non-decreasing-array"
) + """impl Solution {
    pub fn check_possibility(mut nums: Vec<i32>) -> bool {
        let mut changed = false;
        for i in 1..nums.len() {
            if nums[i] >= nums[i - 1] {
                continue;
            }
            if changed {
                return false;
            }
            changed = true;
            if i >= 2 && nums[i] < nums[i - 2] {
                nums[i] = nums[i - 1];
            } else {
                nums[i - 1] = nums[i];
            }
        }
        true
    }
}
"""

FILES["0666_path_sum_iv"] = header("0666", "Path Sum IV", "path-sum-iv") + """use std::collections::HashMap;

impl Solution {
    fn dfs(tree: &HashMap<(i32, i32), i32>, depth: i32, pos: i32, path: i32, total: &mut i32) {
        if !tree.contains_key(&(depth, pos)) {
            return;
        }
        let path = path + tree[&(depth, pos)];
        let left = (depth + 1, pos * 2 - 1);
        let right = (depth + 1, pos * 2);
        if !tree.contains_key(&left) && !tree.contains_key(&right) {
            *total += path;
            return;
        }
        Self::dfs(tree, depth + 1, pos * 2 - 1, path, total);
        Self::dfs(tree, depth + 1, pos * 2, path, total);
    }

    pub fn path_sum(nums: Vec<i32>) -> i32 {
        let mut tree = HashMap::new();
        for num in nums {
            tree.insert((num / 100, (num / 10) % 10), num % 10);
        }
        let mut total = 0;
        Self::dfs(&tree, 1, 1, 0, &mut total);
        total
    }
}
"""

FILES["0667_beautiful_arrangement_ii"] = header(
    "0667", "Beautiful Arrangement II", "beautiful-arrangement-ii"
) + """impl Solution {
    pub fn construct_array(n: i32, k: i32) -> Vec<i32> {
        let mut res = Vec::new();
        for i in 1..=n - k {
            res.push(i);
        }
        let mut left = n - k + 1;
        let mut right = n;
        let mut take_high = true;
        while left <= right {
            if take_high {
                res.push(right);
                right -= 1;
            } else {
                res.push(left);
                left += 1;
            }
            take_high = !take_high;
        }
        res
    }
}
"""

FILES["0668_kth_smallest_number_in_multiplication_table"] = header(
    "0668",
    "Kth Smallest Number in Multiplication Table",
    "kth-smallest-number-in-multiplication-table",
) + """impl Solution {
    fn count_le(m: i32, n: i32, x: i32) -> i32 {
        let mut count = 0;
        for row in 1..=m {
            count += (x / row).min(n);
        }
        count
    }

    pub fn find_kth_number(m: i32, n: i32, k: i32) -> i32 {
        let mut lo = 1;
        let mut hi = m * n;
        while lo < hi {
            let mid = lo + (hi - lo) / 2;
            if Self::count_le(m, n, mid) >= k {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        lo
    }
}
"""

FILES["0669_trim_a_binary_search_tree"] = header(
    "0669", "Trim a Binary Search Tree", "trim-a-binary-search-tree"
) + TREE + """
impl Solution {
    pub fn trim_bst(
        root: Option<Rc<RefCell<TreeNode>>>,
        low: i32,
        high: i32,
    ) -> Option<Rc<RefCell<TreeNode>>> {
        let root = root?;
        let val = root.borrow().val;
        if val < low {
            return Self::trim_bst(root.borrow().right.clone(), low, high);
        }
        if val > high {
            return Self::trim_bst(root.borrow().left.clone(), low, high);
        }
        {
            let mut node = root.borrow_mut();
            node.left = Self::trim_bst(node.left.clone(), low, high);
            node.right = Self::trim_bst(node.right.clone(), low, high);
        }
        Some(root)
    }
}
"""

FILES["0670_maximum_swap"] = header("0670", "Maximum Swap", "maximum-swap") + """impl Solution {
    pub fn maximum_swap(num: i32) -> i32 {
        let mut digits: Vec<u8> = num.to_string().into_bytes();
        let mut last = [-1i32; 10];
        for (i, &d) in digits.iter().enumerate() {
            last[(d - b'0') as usize] = i as i32;
        }
        for i in 0..digits.len() {
            let cur = (digits[i] - b'0') as i32;
            for candidate in (cur + 1..=9).rev() {
                if last[candidate as usize] > i as i32 {
                    let j = last[candidate as usize] as usize;
                    digits.swap(i, j);
                    return String::from_utf8(digits).unwrap().parse().unwrap();
                }
            }
        }
        num
    }
}
"""

FILES["0671_second_minimum_node_in_a_binary_tree"] = header(
    "0671",
    "Second Minimum Node In a Binary Tree",
    "second-minimum-node-in-a-binary-tree",
) + TREE + """
impl Solution {
    fn dfs(node: &Option<Rc<RefCell<TreeNode>>>, root_val: i32, ans: &mut i32) {
        let Some(node) = node else {
            return;
        };
        let node = node.borrow();
        if node.val > root_val {
            if *ans == -1 || node.val < *ans {
                *ans = node.val;
            }
            return;
        }
        Self::dfs(&node.left, root_val, ans);
        Self::dfs(&node.right, root_val, ans);
    }

    pub fn find_second_minimum_value(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let Some(root_rc) = root else {
            return -1;
        };
        let root_val = root_rc.borrow().val;
        let mut ans = -1;
        Self::dfs(&Some(root_rc), root_val, &mut ans);
        ans
    }
}
"""

FILES["0672_bulb_switcher_ii"] = header("0672", "Bulb Switcher II", "bulb-switcher-ii") + """impl Solution {
    pub fn flip_lights(n: i32, presses: i32) -> i32 {
        let n = n.min(3) as usize;
        if presses == 0 {
            return 1;
        }
        let one_press = [2, 3, 4];
        let two_press = [2, 4, 7];
        let many_press = [2, 4, 8];
        if presses == 1 {
            return one_press[n - 1];
        }
        if presses == 2 {
            return two_press[n - 1];
        }
        many_press[n - 1]
    }
}
"""

FILES["0673_number_of_longest_increasing_subsequence"] = header(
    "0673",
    "Number of Longest Increasing Subsequence",
    "number-of-longest-increasing-subsequence",
) + """impl Solution {
    pub fn find_number_of_lis(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut lengths = vec![1; n];
        let mut counts = vec![1; n];
        for i in 0..n {
            for j in 0..i {
                if nums[j] >= nums[i] {
                    continue;
                }
                if lengths[j] + 1 > lengths[i] {
                    lengths[i] = lengths[j] + 1;
                    counts[i] = counts[j];
                } else if lengths[j] + 1 == lengths[i] {
                    counts[i] += counts[j];
                }
            }
        }
        let longest = *lengths.iter().max().unwrap();
        counts
            .iter()
            .zip(lengths.iter())
            .filter(|(_, &len)| len == longest)
            .map(|(c, _)| *c)
            .sum()
    }
}
"""

FILES["0674_longest_continuous_increasing_subsequence"] = header(
    "0674",
    "Longest Continuous Increasing Subsequence",
    "longest-continuous-increasing-subsequence",
) + """impl Solution {
    pub fn find_length_of_lcis(nums: Vec<i32>) -> i32 {
        let mut best = 1;
        let mut cur = 1;
        for i in 1..nums.len() {
            if nums[i] > nums[i - 1] {
                cur += 1;
                best = best.max(cur);
            } else {
                cur = 1;
            }
        }
        best
    }
}
"""

FILES["0675_cut_off_trees_for_golf_event"] = header(
    "0675", "Cut Off Trees for Golf Event", "cut-off-trees-for-golf-event"
) + """use std::collections::VecDeque;

impl Solution {
    fn bfs(forest: &[Vec<i32>], sr: usize, sc: usize, tr: usize, tc: usize) -> i32 {
        if sr == tr && sc == tc {
            return 0;
        }
        let m = forest.len();
        let n = forest[0].len();
        let mut seen = vec![vec![false; n]; m];
        let mut queue = VecDeque::new();
        queue.push_back((sr, sc, 0));
        seen[sr][sc] = true;
        let dirs = [(-1isize, 0isize), (1, 0), (0, -1), (0, 1)];
        while let Some((r, c, dist)) = queue.pop_front() {
            for (dr, dc) in dirs {
                let nr = r as isize + dr;
                let nc = c as isize + dc;
                if nr < 0 || nr >= m as isize || nc < 0 || nc >= n as isize {
                    continue;
                }
                let (nr, nc) = (nr as usize, nc as usize);
                if seen[nr][nc] || forest[nr][nc] == 0 {
                    continue;
                }
                if nr == tr && nc == tc {
                    return dist + 1;
                }
                seen[nr][nc] = true;
                queue.push_back((nr, nc, dist + 1));
            }
        }
        -1
    }

    pub fn cut_off_tree(forest: Vec<Vec<i32>>) -> i32 {
        let mut trees = Vec::new();
        for i in 0..forest.len() {
            for j in 0..forest[0].len() {
                if forest[i][j] > 1 {
                    trees.push((forest[i][j], i, j));
                }
            }
        }
        trees.sort_unstable();
        let mut sr = 0;
        let mut sc = 0;
        let mut steps = 0;
        for (_, tr, tc) in trees {
            let dist = Self::bfs(&forest, sr, sc, tr, tc);
            if dist < 0 {
                return -1;
            }
            steps += dist;
            sr = tr;
            sc = tc;
        }
        steps
    }
}
"""

FILES["0676_implement_magic_dictionary"] = header(
    "0676", "Implement Magic Dictionary", "implement-magic-dictionary"
) + """pub struct MagicDictionary {
    words: Vec<String>,
}

impl MagicDictionary {
    pub fn new() -> Self {
        Self { words: Vec::new() }
    }

    pub fn build_dict(&mut self, dictionary: Vec<String>) {
        self.words = dictionary;
    }

    pub fn search(&self, search_word: String) -> bool {
        for word in &self.words {
            if word.len() != search_word.len() {
                continue;
            }
            let diff = word
                .bytes()
                .zip(search_word.bytes())
                .filter(|(a, b)| a != b)
                .count();
            if diff == 1 {
                return true;
            }
        }
        false
    }
}
"""

FILES["0677_map_sum_pairs"] = header("0677", "Map Sum Pairs", "map-sum-pairs") + """use std::collections::HashMap;

pub struct MapSum {
    values: HashMap<String, i32>,
    prefix_sums: HashMap<String, i32>,
}

impl MapSum {
    pub fn new() -> Self {
        Self {
            values: HashMap::new(),
            prefix_sums: HashMap::new(),
        }
    }

    pub fn insert(&mut self, key: String, val: i32) {
        let delta = val - self.values.get(&key).copied().unwrap_or(0);
        self.values.insert(key.clone(), val);
        for i in 1..=key.len() {
            *self.prefix_sums.entry(key[..i].to_string()).or_insert(0) += delta;
        }
    }

    pub fn sum(&self, prefix: String) -> i32 {
        self.prefix_sums.get(&prefix).copied().unwrap_or(0)
    }
}
"""


def main() -> None:
    folders = (ROOT / ".tmp_rs4013/batch_00.txt").read_text().strip().splitlines()
    missing = [f for f in folders if f not in FILES]
    extra = [f for f in FILES if f not in folders]
    if missing:
        raise SystemExit(f"missing implementations: {missing}")
    if extra:
        raise SystemExit(f"extra implementations: {extra}")
    written = 0
    for folder, content in FILES.items():
        path = ROOT / folder / "solution.rs"
        text = content.lstrip("\n")
        if text.startswith("\ufeff"):
            raise SystemExit(f"BOM in {folder}")
        if "pub fn solve()" in text:
            raise SystemExit(f"stub solve() in {folder}")
        path.write_text(text, encoding="utf-8", newline="\n")
        written += 1
        print(f"wrote {folder}/solution.rs ({len(text)} bytes)")
    print(f"DONE written={written}")


if __name__ == "__main__":
    main()

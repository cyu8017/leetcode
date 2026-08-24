#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
SOLUTIONS: dict[str, str] = {}


def add(name: str, content: str) -> None:
    SOLUTIONS[name] = content.strip() + "\n"


TREE = """class TreeNode {
    public $val = 0;
    public $left = null;
    public $right = null;
    function __construct($val = 0, $left = null, $right = null) {
        $this->val = $val;
        $this->left = $left;
        $this->right = $right;
    }
}
"""

LISTN = """class ListNode {
    public $val = 0;
    public $next = null;
    function __construct($val = 0, $next = null) {
        $this->val = $val;
        $this->next = $next;
    }
}
"""

add("0680_valid_palindrome_ii", r"""<?php
// LeetCode 0680 - Valid Palindrome II
// https://leetcode.com/problems/valid-palindrome-ii/

class Solution {
    function validPalindrome($s) {
        $isPalindrome = function ($left, $right) use ($s) {
            while ($left < $right) {
                if ($s[$left] !== $s[$right]) return false;
                $left++;
                $right--;
            }
            return true;
        };
        $left = 0;
        $right = strlen($s) - 1;
        while ($left < $right) {
            if ($s[$left] !== $s[$right]) {
                return $isPalindrome($left + 1, $right) || $isPalindrome($left, $right - 1);
            }
            $left++;
            $right--;
        }
        return true;
    }
}
""")

add("0681_next_closest_time", r"""<?php
// LeetCode 0681 - Next Closest Time
// https://leetcode.com/problems/next-closest-time/

class Solution {
    function nextClosestTime($time) {
        $digits = [$time[0] => true, $time[1] => true, $time[3] => true, $time[4] => true];
        $start = intval(substr($time, 0, 2), 10) * 60 + intval(substr($time, 3, 2), 10);
        for ($delta = 1; $delta <= 24 * 60; $delta++) {
            $mins = ($start + $delta) % (24 * 60);
            $hh = intdiv($mins, 60);
            $mm = $mins % 60;
            $c0 = (string)intdiv($hh, 10);
            $c1 = (string)($hh % 10);
            $c2 = (string)intdiv($mm, 10);
            $c3 = (string)($mm % 10);
            if (isset($digits[$c0]) && isset($digits[$c1]) && isset($digits[$c2]) && isset($digits[$c3])) {
                return $c0 . $c1 . ':' . $c2 . $c3;
            }
        }
        return $time;
    }
}
""")

add("0682_baseball_game", r"""<?php
// LeetCode 0682 - Baseball Game
// https://leetcode.com/problems/baseball-game/

class Solution {
    function calPoints($operations) {
        $stack = [];
        foreach ($operations as $op) {
            if ($op === 'C') array_pop($stack);
            else if ($op === 'D') $stack[] = $stack[count($stack) - 1] * 2;
            else if ($op === '+') $stack[] = $stack[count($stack) - 1] + $stack[count($stack) - 2];
            else $stack[] = intval($op, 10);
        }
        $total = 0;
        foreach ($stack as $value) $total += $value;
        return $total;
    }
}
""")

add("0683_k_empty_slots", r"""<?php
// LeetCode 0683 - K Empty Slots
// https://leetcode.com/problems/k-empty-slots/

class Solution {
    function kEmptySlots($bulbs, $k) {
        $n = count($bulbs);
        $days = array_fill(0, $n, 0);
        for ($day = 1; $day <= $n; $day++) $days[$bulbs[$day - 1] - 1] = $day;
        $ans = PHP_INT_MAX;
        $i = 0;
        while ($i < $n - $k - 1) {
            $left = $i;
            $right = $i + $k + 1;
            $j = $left + 1;
            while ($j < $right && $days[$j] > $days[$left] && $days[$j] > $days[$right]) $j++;
            if ($j === $right) {
                $ans = min($ans, max($days[$left], $days[$right]));
                $i++;
            } else $i = $j;
        }
        return $ans === PHP_INT_MAX ? -1 : $ans;
    }
}
""")

add("0684_redundant_connection", r"""<?php
// LeetCode 0684 - Redundant Connection
// https://leetcode.com/problems/redundant-connection/

class Solution {
    function findRedundantConnection($edges) {
        $find = function (&$parent, $x) {
            while ($parent[$x] !== $x) {
                $parent[$x] = $parent[$parent[$x]];
                $x = $parent[$x];
            }
            return $x;
        };
        $parent = [];
        for ($i = 0; $i <= count($edges); $i++) $parent[$i] = $i;
        foreach ($edges as $edge) {
            $u = $edge[0];
            $v = $edge[1];
            $pu = $find($parent, $u);
            $pv = $find($parent, $v);
            if ($pu === $pv) return [$u, $v];
            $parent[$pu] = $pv;
        }
        return [];
    }
}
""")

add("0685_redundant_connection_ii", r"""<?php
// LeetCode 0685 - Redundant Connection II
// https://leetcode.com/problems/redundant-connection-ii/

class Solution {
    function findRedundantDirectedConnection($edges) {
        $find = function (&$uf, $x) {
            while ($uf[$x] !== $x) {
                $uf[$x] = $uf[$uf[$x]];
                $x = $uf[$x];
            }
            return $x;
        };
        $n = count($edges);
        $parent = array_fill(0, $n + 1, 0);
        $cand1 = null;
        $cand2 = null;
        for ($i = 0; $i < $n; $i++) {
            $u = $edges[$i][0];
            $v = $edges[$i][1];
            if ($parent[$v] === 0) $parent[$v] = $u;
            else {
                $cand1 = [$parent[$v], $v];
                $cand2 = [$u, $v];
                $edges[$i] = [-1, -1];
                break;
            }
        }
        $uf = [];
        for ($i = 0; $i <= $n; $i++) $uf[$i] = $i;
        foreach ($edges as $edge) {
            if ($edge[0] < 0) continue;
            $pu = $find($uf, $edge[0]);
            $pv = $find($uf, $edge[1]);
            if ($pu === $pv) return $cand1 !== null ? $cand1 : [$edge[0], $edge[1]];
            $uf[$pu] = $pv;
        }
        return $cand2;
    }
}
""")

add("0686_repeated_string_match", r"""<?php
// LeetCode 0686 - Repeated String Match
// https://leetcode.com/problems/repeated-string-match/

class Solution {
    function repeatedStringMatch($a, $b) {
        $repeats = intdiv(strlen($b) + strlen($a) - 1, strlen($a));
        $built = '';
        for ($i = 0; $i < $repeats; $i++) $built .= $a;
        if (strpos($built, $b) !== false) return $repeats;
        $built .= $a;
        if (strpos($built, $b) !== false) return $repeats + 1;
        return -1;
    }
}
""")

add("0687_longest_univalue_path", """<?php
// LeetCode 0687 - Longest Univalue Path
// https://leetcode.com/problems/longest-univalue-path/

""" + TREE + r"""
class Solution {
    function longestUnivaluePath($root) {
        $best = 0;
        $dfs = function ($node) use (&$dfs, &$best) {
            if ($node === null) return 0;
            $left = $dfs($node->left);
            $right = $dfs($node->right);
            $leftPath = $node->left !== null && $node->left->val === $node->val ? $left + 1 : 0;
            $rightPath = $node->right !== null && $node->right->val === $node->val ? $right + 1 : 0;
            $best = max($best, $leftPath + $rightPath);
            return max($leftPath, $rightPath);
        };
        $dfs($root);
        return $best;
    }
}
""")

add("0688_knight_probability_in_chessboard", r"""<?php
// LeetCode 0688 - Knight Probability in Chessboard
// https://leetcode.com/problems/knight-probability-in-chessboard/

class Solution {
    function knightProbability($n, $k, $row, $column) {
        $moves = [[-2,-1],[-2,1],[-1,-2],[-1,2],[1,-2],[1,2],[2,-1],[2,1]];
        $dp = array_fill(0, $n, array_fill(0, $n, 0.0));
        $dp[$row][$column] = 1.0;
        for ($step = 0; $step < $k; $step++) {
            $nxt = array_fill(0, $n, array_fill(0, $n, 0.0));
            for ($r = 0; $r < $n; $r++) {
                for ($c = 0; $c < $n; $c++) {
                    if ($dp[$r][$c] === 0.0) continue;
                    foreach ($moves as $move) {
                        $nr = $r + $move[0];
                        $nc = $c + $move[1];
                        if ($nr >= 0 && $nr < $n && $nc >= 0 && $nc < $n) $nxt[$nr][$nc] += $dp[$r][$c] / 8.0;
                    }
                }
            }
            $dp = $nxt;
        }
        $total = 0.0;
        for ($r = 0; $r < $n; $r++)
            for ($c = 0; $c < $n; $c++)
                $total += $dp[$r][$c];
        return $total;
    }
}
""")

add("0689_maximum_sum_of_3_non_overlapping_subarrays", r"""<?php
// LeetCode 0689 - Maximum Sum of 3 Non-Overlapping Subarrays
// https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/

class Solution {
    function maxSumOfThreeSubarrays($nums, $k) {
        $n = count($nums);
        $windows = $n - $k + 1;
        $sums = array_fill(0, $windows, 0);
        $total = 0;
        for ($i = 0; $i < $k; $i++) $total += $nums[$i];
        $sums[0] = $total;
        for ($i = 1; $i < $windows; $i++) {
            $total += $nums[$i + $k - 1] - $nums[$i - 1];
            $sums[$i] = $total;
        }
        $left = array_fill(0, $windows, 0);
        $best = 0;
        for ($i = 0; $i < $windows; $i++) {
            if ($sums[$i] > $sums[$best]) $best = $i;
            $left[$i] = $best;
        }
        $right = array_fill(0, $windows, 0);
        $best = $windows - 1;
        for ($i = $windows - 1; $i >= 0; $i--) {
            if ($sums[$i] >= $sums[$best]) $best = $i;
            $right[$i] = $best;
        }
        $answer = [0, 0, 0];
        $bestTotal = -1;
        for ($mid = $k; $mid < $windows - $k; $mid++) {
            $l = $left[$mid - $k];
            $r = $right[$mid + $k];
            $cur = $sums[$l] + $sums[$mid] + $sums[$r];
            if ($cur > $bestTotal) {
                $bestTotal = $cur;
                $answer = [$l, $mid, $r];
            }
        }
        return $answer;
    }
}
""")

add("0690_employee_importance", r"""<?php
// LeetCode 0690 - Employee Importance
// https://leetcode.com/problems/employee-importance/

class Employee {
    public $id;
    public $importance;
    public $subordinates;
    function __construct($id = 0, $importance = 0, $subordinates = []) {
        $this->id = $id;
        $this->importance = $importance;
        $this->subordinates = $subordinates;
    }
}

class Solution {
    function getImportance($employees, $id) {
        $table = [];
        foreach ($employees as $emp) {
            if (is_array($emp)) {
                $eid = $emp[0];
                $imp = $emp[1];
                $subs = $emp[2];
            } else {
                $eid = $emp->id;
                $imp = $emp->importance;
                $subs = $emp->subordinates;
            }
            $table[$eid] = [$imp, $subs];
        }
        $dfs = function ($eid) use (&$dfs, &$table) {
            [$imp, $subs] = $table[$eid];
            $total = $imp;
            foreach ($subs as $sub) $total += $dfs($sub);
            return $total;
        };
        return $dfs($id);
    }
}
""")

add("0691_stickers_to_spell_word", r"""<?php
// LeetCode 0691 - Stickers to Spell Word
// https://leetcode.com/problems/stickers-to-spell-word/

class Solution {
    function minStickers($stickers, $target) {
        $need = array_fill(0, 26, 0);
        $len = strlen($target);
        for ($i = 0; $i < $len; $i++) $need[ord($target[$i]) - 97]++;
        $chars = [];
        for ($i = 0; $i < 26; $i++) if ($need[$i] > 0) $chars[] = chr(97 + $i);
        $sticks = [];
        foreach ($stickers as $sticker) {
            $counts = array_fill(0, 26, 0);
            $slen = strlen($sticker);
            for ($i = 0; $i < $slen; $i++) $counts[ord($sticker[$i]) - 97]++;
            $useful = false;
            foreach ($chars as $ch) if ($counts[ord($ch) - 97] > 0) { $useful = true; break; }
            if ($useful) $sticks[] = $counts;
        }
        $memo = [];
        $dfs = function ($state) use (&$dfs, &$memo, &$chars, &$sticks) {
            $k = implode(',', $state);
            if (isset($memo[$k])) return $memo[$k];
            $i = 0;
            while ($i < count($state) && $state[$i] === 0) $i++;
            if ($i === count($state)) {
                $memo[$k] = 0;
                return 0;
            }
            $first = $chars[$i];
            $best = 1000000000;
            foreach ($sticks as $stick) {
                if ($stick[ord($first) - 97] === 0) continue;
                $nxt = $state;
                for ($j = 0; $j < count($chars); $j++) {
                    $nxt[$j] = max(0, $nxt[$j] - $stick[ord($chars[$j]) - 97]);
                }
                $best = min($best, 1 + $dfs($nxt));
            }
            $memo[$k] = $best;
            return $best;
        };
        $state = [];
        foreach ($chars as $ch) $state[] = $need[ord($ch) - 97];
        $result = $dfs($state);
        return $result >= 1000000000 ? -1 : $result;
    }
}
""")

add("0692_top_k_frequent_words", r"""<?php
// LeetCode 0692 - Top K Frequent Words
// https://leetcode.com/problems/top-k-frequent-words/

class Solution {
    function topKFrequent($words, $k) {
        $counts = [];
        foreach ($words as $word) $counts[$word] = ($counts[$word] ?? 0) + 1;
        $ordered = array_keys($counts);
        usort($ordered, function ($a, $b) use ($counts) {
            $ca = $counts[$a];
            $cb = $counts[$b];
            if ($ca !== $cb) return $cb - $ca;
            return $a < $b ? -1 : ($a > $b ? 1 : 0);
        });
        return array_slice($ordered, 0, $k);
    }
}
""")

add("0693_binary_number_with_alternating_bits", r"""<?php
// LeetCode 0693 - Binary Number with Alternating Bits
// https://leetcode.com/problems/binary-number-with-alternating-bits/

class Solution {
    function hasAlternatingBits($n) {
        $x = $n ^ ($n >> 1);
        return ($x & ($x + 1)) === 0;
    }
}
""")

add("0694_number_of_distinct_islands", r"""<?php
// LeetCode 0694 - Number of Distinct Islands
// https://leetcode.com/problems/number-of-distinct-islands/

class Solution {
    function numDistinctIslands($grid) {
        if ($grid === null || count($grid) === 0) return 0;
        $dfs = function ($r, $c, $br, $bc, &$path) use (&$dfs, &$grid) {
            if ($r < 0 || $r >= count($grid) || $c < 0 || $c >= count($grid[0]) || $grid[$r][$c] === 0) return;
            $grid[$r][$c] = 0;
            $path[] = ($r - $br) . ',' . ($c - $bc);
            $dfs($r + 1, $c, $br, $bc, $path);
            $dfs($r - 1, $c, $br, $bc, $path);
            $dfs($r, $c + 1, $br, $bc, $path);
            $dfs($r, $c - 1, $br, $bc, $path);
        };
        $shapes = [];
        for ($i = 0; $i < count($grid); $i++) {
            for ($j = 0; $j < count($grid[0]); $j++) {
                if ($grid[$i][$j] === 1) {
                    $path = [];
                    $dfs($i, $j, $i, $j, $path);
                    $shapes[implode(';', $path)] = true;
                }
            }
        }
        return count($shapes);
    }
}
""")

add("0695_max_area_of_island", r"""<?php
// LeetCode 0695 - Max Area of Island
// https://leetcode.com/problems/max-area-of-island/

class Solution {
    function maxAreaOfIsland($grid) {
        $dfs = function ($r, $c) use (&$dfs, &$grid) {
            if ($r < 0 || $r >= count($grid) || $c < 0 || $c >= count($grid[0]) || $grid[$r][$c] === 0) return 0;
            $grid[$r][$c] = 0;
            return 1 + $dfs($r + 1, $c) + $dfs($r - 1, $c) + $dfs($r, $c + 1) + $dfs($r, $c - 1);
        };
        $best = 0;
        for ($i = 0; $i < count($grid); $i++)
            for ($j = 0; $j < count($grid[0]); $j++)
                $best = max($best, $dfs($i, $j));
        return $best;
    }
}
""")

add("0696_count_binary_substrings", r"""<?php
// LeetCode 0696 - Count Binary Substrings
// https://leetcode.com/problems/count-binary-substrings/

class Solution {
    function countBinarySubstrings($s) {
        $prev = 0;
        $cur = 1;
        $ans = 0;
        $n = strlen($s);
        for ($i = 1; $i < $n; $i++) {
            if ($s[$i] === $s[$i - 1]) $cur++;
            else {
                $ans += min($prev, $cur);
                $prev = $cur;
                $cur = 1;
            }
        }
        return $ans + min($prev, $cur);
    }
}
""")

add("0697_degree_of_an_array", r"""<?php
// LeetCode 0697 - Degree of an Array
// https://leetcode.com/problems/degree-of-an-array/

class Solution {
    function findShortestSubArray($nums) {
        $first = [];
        $last = [];
        $count = [];
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            if (!array_key_exists($nums[$i], $first)) $first[$nums[$i]] = $i;
            $last[$nums[$i]] = $i;
            $count[$nums[$i]] = ($count[$nums[$i]] ?? 0) + 1;
        }
        $degree = 0;
        foreach ($count as $freq) $degree = max($degree, $freq);
        $best = PHP_INT_MAX;
        foreach ($count as $key => $value) {
            if ($value === $degree) $best = min($best, $last[$key] - $first[$key] + 1);
        }
        return $best;
    }
}
""")

add("0698_partition_to_k_equal_sum_subsets", r"""<?php
// LeetCode 0698 - Partition to K Equal Sum Subsets
// https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

class Solution {
    function canPartitionKSubsets($nums, $k) {
        $total = 0;
        foreach ($nums as $x) $total += $x;
        if ($total % $k !== 0) return false;
        $target = intdiv($total, $k);
        $arr = $nums;
        rsort($arr);
        if ($arr[0] > $target) return false;
        $buckets = array_fill(0, $k, 0);
        $dfs = function ($index) use (&$dfs, &$arr, &$buckets, $target) {
            if ($index === count($arr)) return true;
            for ($i = 0; $i < count($buckets); $i++) {
                if ($buckets[$i] + $arr[$index] > $target) continue;
                $buckets[$i] += $arr[$index];
                if ($dfs($index + 1)) return true;
                $buckets[$i] -= $arr[$index];
                if ($buckets[$i] === 0) break;
            }
            return false;
        };
        return $dfs(0);
    }
}
""")

add("0699_falling_squares", r"""<?php
// LeetCode 0699 - Falling Squares
// https://leetcode.com/problems/falling-squares/

class Solution {
    function fallingSquares($positions) {
        $intervals = [];
        $answer = [];
        $maxHeight = 0;
        foreach ($positions as $pos) {
            $left = $pos[0];
            $side = $pos[1];
            $right = $left + $side;
            $bas = 0;
            foreach ($intervals as $it) {
                if ($it[1] > $left && $it[0] < $right) $bas = max($bas, $it[2]);
            }
            $height = $bas + $side;
            $intervals[] = [$left, $right, $height];
            $maxHeight = max($maxHeight, $height);
            $answer[] = $maxHeight;
        }
        return $answer;
    }
}
""")

add("0700_search_in_a_binary_search_tree", """<?php
// LeetCode 0700 - Search in a Binary Search Tree
// https://leetcode.com/problems/search-in-a-binary-search-tree/

""" + TREE + r"""
class Solution {
    function searchBST($root, $val) {
        while ($root !== null && $root->val !== $val) {
            $root = $val < $root->val ? $root->left : $root->right;
        }
        return $root;
    }
}
""")

add("0701_insert_into_a_binary_search_tree", """<?php
// LeetCode 0701 - Insert into a Binary Search Tree
// https://leetcode.com/problems/insert-into-a-binary-search-tree/

""" + TREE + r"""
class Solution {
    function insertIntoBST($root, $val) {
        if ($root === null) return new TreeNode($val);
        $node = $root;
        while (true) {
            if ($val < $node->val) {
                if ($node->left === null) { $node->left = new TreeNode($val); break; }
                $node = $node->left;
            } else {
                if ($node->right === null) { $node->right = new TreeNode($val); break; }
                $node = $node->right;
            }
        }
        return $root;
    }
}
""")

add("0702_search_in_a_sorted_array_of_unknown_size", r"""<?php
// LeetCode 0702 - Search in a Sorted Array of Unknown Size
// https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size/

class Solution {
    function search($reader, $target) {
        if (is_array($reader)) {
            $secret = $reader;
            $reader = new class($secret) {
                private $secret;
                function __construct($secret) { $this->secret = $secret; }
                function get($index) {
                    if ($index < 0 || $index >= count($this->secret)) return 2147483647;
                    return $this->secret[$index];
                }
            };
        }
        $right = 1;
        while ($reader->get($right) < $target) $right <<= 1;
        $left = $right >> 1;
        while ($left <= $right) {
            $mid = $left + intdiv($right - $left, 2);
            $value = $reader->get($mid);
            if ($value === $target) return $mid;
            if ($value > $target) $right = $mid - 1;
            else $left = $mid + 1;
        }
        return -1;
    }
}
""")

add("0703_kth_largest_element_in_a_stream", r"""<?php
// LeetCode 0703 - Kth Largest Element in a Stream
// https://leetcode.com/problems/kth-largest-element-in-a-stream/

class KthLargest {
    private $k;
    private $heap = [];

    function __construct($k, $nums) {
        $this->k = $k;
        foreach ($nums as $num) $this->add($num);
    }

    function add($val) {
        $this->heap[] = $val;
        sort($this->heap);
        if (count($this->heap) > $this->k) array_shift($this->heap);
        return $this->heap[0];
    }
}
""")

add("0704_binary_search", r"""<?php
// LeetCode 0704 - Binary Search
// https://leetcode.com/problems/binary-search/

class Solution {
    function search($nums, $target) {
        $left = 0;
        $right = count($nums) - 1;
        while ($left <= $right) {
            $mid = $left + intdiv($right - $left, 2);
            if ($nums[$mid] === $target) return $mid;
            if ($nums[$mid] < $target) $left = $mid + 1;
            else $right = $mid - 1;
        }
        return -1;
    }
}
""")

add("0705_design_hashset", r"""<?php
// LeetCode 0705 - Design HashSet
// https://leetcode.com/problems/design-hashset/

class MyHashSet {
    private $data = [];

    function __construct() {
        $this->data = [];
    }

    function add($key) {
        $this->data[$key] = true;
    }

    function remove($key) {
        unset($this->data[$key]);
    }

    function contains($key) {
        return isset($this->data[$key]);
    }
}
""")

add("0706_design_hashmap", r"""<?php
// LeetCode 0706 - Design HashMap
// https://leetcode.com/problems/design-hashmap/

class MyHashMap {
    private $data = [];

    function __construct() {
        $this->data = [];
    }

    function put($key, $value) {
        $this->data[$key] = $value;
    }

    function get($key) {
        return array_key_exists($key, $this->data) ? $this->data[$key] : -1;
    }

    function remove($key) {
        unset($this->data[$key]);
    }
}
""")

add("0707_design_linked_list", r"""<?php
// LeetCode 0707 - Design Linked List
// https://leetcode.com/problems/design-linked-list/

class MyLinkedList {
    private $dummy;
    private $size;

    function __construct() {
        $this->dummy = (object)['val' => 0, 'next' => null];
        $this->size = 0;
    }

    function get($index) {
        if ($index < 0 || $index >= $this->size) return -1;
        $node = $this->dummy->next;
        for ($i = 0; $i < $index; $i++) $node = $node->next;
        return $node->val;
    }

    function addAtHead($val) { $this->addAtIndex(0, $val); }

    function addAtTail($val) { $this->addAtIndex($this->size, $val); }

    function addAtIndex($index, $val) {
        if ($index < 0 || $index > $this->size) return;
        $prev = $this->dummy;
        for ($i = 0; $i < $index; $i++) $prev = $prev->next;
        $node = (object)['val' => $val, 'next' => $prev->next];
        $prev->next = $node;
        $this->size++;
    }

    function deleteAtIndex($index) {
        if ($index < 0 || $index >= $this->size) return;
        $prev = $this->dummy;
        for ($i = 0; $i < $index; $i++) $prev = $prev->next;
        $prev->next = $prev->next->next;
        $this->size--;
    }
}
""")

add("0708_insert_into_a_sorted_circular_linked_list", r"""<?php
// LeetCode 0708 - Insert into a Sorted Circular Linked List
// https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/

class Node {
    public $val = 0;
    public $next = null;
    function __construct($val = 0, $next = null) {
        $this->val = $val;
        $this->next = $next;
    }
}

class Solution {
    function insert($head, $insertVal) {
        $node = new Node($insertVal);
        if ($head === null) {
            $node->next = $node;
            return $node;
        }
        $cur = $head;
        while ($cur->next !== null && $cur->next !== $head) $cur = $cur->next;
        $cur->next = $head;
        $prev = $head;
        $curr = $head->next;
        while (true) {
            if ($prev->val <= $insertVal && $insertVal <= $curr->val) break;
            if ($prev->val > $curr->val && ($insertVal >= $prev->val || $insertVal <= $curr->val)) break;
            $prev = $curr;
            $curr = $curr->next;
            if ($prev === $head) break;
        }
        $prev->next = $node;
        $node->next = $curr;
        return $head;
    }
}
""")

add("0709_to_lower_case", r"""<?php
// LeetCode 0709 - To Lower Case
// https://leetcode.com/problems/to-lower-case/

class Solution {
    function toLowerCase($s) {
        $chars = str_split($s);
        $n = count($chars);
        for ($i = 0; $i < $n; $i++) {
            $code = ord($chars[$i]);
            if ($code >= 65 && $code <= 90) $chars[$i] = chr($code + 32);
        }
        return implode('', $chars);
    }
}
""")

add("0710_random_pick_with_blacklist", r"""<?php
// LeetCode 0710 - Random Pick with Blacklist
// https://leetcode.com/problems/random-pick-with-blacklist/

class Solution {
    private $size;
    private $mapping;

    function __construct($n, $blacklist) {
        $this->size = $n - count($blacklist);
        $this->mapping = [];
        $black = [];
        foreach ($blacklist as $b) $black[$b] = true;
        $white = $this->size;
        foreach ($blacklist as $b) {
            if ($b < $this->size) {
                while (isset($black[$white])) $white++;
                $this->mapping[$b] = $white++;
            }
        }
    }

    function pick() {
        $index = $this->size > 0 ? mt_rand(0, $this->size - 1) : 0;
        return array_key_exists($index, $this->mapping) ? $this->mapping[$index] : $index;
    }
}
""")

add("0711_number_of_distinct_islands_ii", r"""<?php
// LeetCode 0711 - Number of Distinct Islands II
// https://leetcode.com/problems/number-of-distinct-islands-ii/

class Solution {
    function numDistinctIslands2($grid) {
        if ($grid === null || count($grid) === 0) return 0;
        $m = count($grid);
        $n = count($grid[0]);
        $dfs = function ($r, $c, &$cells) use (&$dfs, &$grid, $m, $n) {
            if ($r < 0 || $r >= $m || $c < 0 || $c >= $n || $grid[$r][$c] === 0) return;
            $grid[$r][$c] = 0;
            $cells[] = [$r, $c];
            $dfs($r + 1, $c, $cells);
            $dfs($r - 1, $c, $cells);
            $dfs($r, $c + 1, $cells);
            $dfs($r, $c - 1, $cells);
        };
        $canonical = function ($cells) {
            $signs = [
                [1, 1, 0], [1, -1, 0], [-1, 1, 0], [-1, -1, 0],
                [1, 1, 1], [1, -1, 1], [-1, 1, 1], [-1, -1, 1]
            ];
            $best = null;
            foreach ($signs as $s) {
                $pts = [];
                foreach ($cells as $p) {
                    $x = $p[0];
                    $y = $p[1];
                    if ($s[2] === 0) { $nx = $s[0] * $x; $ny = $s[1] * $y; }
                    else { $nx = $s[0] * $y; $ny = $s[1] * $x; }
                    $pts[] = [$nx, $ny];
                }
                $minX = PHP_INT_MAX;
                $minY = PHP_INT_MAX;
                foreach ($pts as $p) {
                    $minX = min($minX, $p[0]);
                    $minY = min($minY, $p[1]);
                }
                for ($i = 0; $i < count($pts); $i++) {
                    $pts[$i][0] -= $minX;
                    $pts[$i][1] -= $minY;
                }
                usort($pts, function ($a, $b) {
                    return $a[0] !== $b[0] ? $a[0] - $b[0] : $a[1] - $b[1];
                });
                $parts = [];
                foreach ($pts as $p) $parts[] = $p[0] . ',' . $p[1];
                $key = implode(';', $parts);
                if ($best === null || $key < $best) $best = $key;
            }
            return $best;
        };
        $shapes = [];
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if ($grid[$i][$j] === 1) {
                    $cells = [];
                    $dfs($i, $j, $cells);
                    $shapes[$canonical($cells)] = true;
                }
            }
        }
        return count($shapes);
    }
}
""")

add("0712_minimum_ascii_delete_sum_for_two_strings", r"""<?php
// LeetCode 0712 - Minimum ASCII Delete Sum for Two Strings
// https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/

class Solution {
    function minimumDeleteSum($s1, $s2) {
        $m = strlen($s1);
        $n = strlen($s2);
        $dp = array_fill(0, $m + 1, array_fill(0, $n + 1, 0));
        for ($i = 1; $i <= $m; $i++) $dp[$i][0] = $dp[$i - 1][0] + ord($s1[$i - 1]);
        for ($j = 1; $j <= $n; $j++) $dp[0][$j] = $dp[0][$j - 1] + ord($s2[$j - 1]);
        for ($i = 1; $i <= $m; $i++) {
            for ($j = 1; $j <= $n; $j++) {
                if ($s1[$i - 1] === $s2[$j - 1]) $dp[$i][$j] = $dp[$i - 1][$j - 1];
                else $dp[$i][$j] = min($dp[$i - 1][$j] + ord($s1[$i - 1]), $dp[$i][$j - 1] + ord($s2[$j - 1]));
            }
        }
        return $dp[$m][$n];
    }
}
""")

add("0713_subarray_product_less_than_k", r"""<?php
// LeetCode 0713 - Subarray Product Less Than K
// https://leetcode.com/problems/subarray-product-less-than-k/

class Solution {
    function numSubarrayProductLessThanK($nums, $k) {
        if ($k <= 1) return 0;
        $product = 1;
        $left = 0;
        $ans = 0;
        $n = count($nums);
        for ($right = 0; $right < $n; $right++) {
            $product *= $nums[$right];
            while ($product >= $k) $product = intdiv($product, $nums[$left++]);
            $ans += $right - $left + 1;
        }
        return $ans;
    }
}
""")

add("0714_best_time_to_buy_and_sell_stock_with_transaction_fee", r"""<?php
// LeetCode 0714 - Best Time to Buy and Sell Stock with Transaction Fee
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

class Solution {
    function maxProfit($prices, $fee) {
        $hold = -$prices[0];
        $cash = 0;
        $n = count($prices);
        for ($i = 1; $i < $n; $i++) {
            $price = $prices[$i];
            $hold = max($hold, $cash - $price);
            $cash = max($cash, $hold + $price - $fee);
        }
        return $cash;
    }
}
""")

add("0715_range_module", r"""<?php
// LeetCode 0715 - Range Module
// https://leetcode.com/problems/range-module/

class RangeModule {
    private $intervals = [];

    function __construct() {
        $this->intervals = [];
    }

    function addRange($left, $right) {
        $next = [];
        $placed = false;
        foreach ($this->intervals as $iv) {
            $start = $iv[0];
            $end = $iv[1];
            if ($end < $left) $next[] = [$start, $end];
            else if ($right < $start) {
                if (!$placed) { $next[] = [$left, $right]; $placed = true; }
                $next[] = [$start, $end];
            } else {
                $left = min($left, $start);
                $right = max($right, $end);
            }
        }
        if (!$placed) $next[] = [$left, $right];
        $this->intervals = $next;
    }

    function queryRange($left, $right) {
        foreach ($this->intervals as $iv) {
            if ($iv[0] <= $left && $right <= $iv[1]) return true;
            if ($iv[1] >= $right) break;
        }
        return false;
    }

    function removeRange($left, $right) {
        $next = [];
        foreach ($this->intervals as $iv) {
            $start = $iv[0];
            $end = $iv[1];
            if ($end <= $left || $right <= $start) $next[] = [$start, $end];
            else {
                if ($start < $left) $next[] = [$start, $left];
                if ($right < $end) $next[] = [$right, $end];
            }
        }
        $this->intervals = $next;
    }
}
""")

add("0716_max_stack", r"""<?php
// LeetCode 0716 - Max Stack
// https://leetcode.com/problems/max-stack/

class MaxStack {
    private $stack = [];
    private $maxes = [];

    function __construct() {
        $this->stack = [];
        $this->maxes = [];
    }

    function push($x) {
        $this->stack[] = $x;
        $this->maxes[] = count($this->maxes) === 0 ? $x : max($x, $this->maxes[count($this->maxes) - 1]);
    }

    function pop() {
        array_pop($this->maxes);
        return array_pop($this->stack);
    }

    function top() { return $this->stack[count($this->stack) - 1]; }

    function peekMax() { return $this->maxes[count($this->maxes) - 1]; }

    function popMax() {
        $maxVal = $this->peekMax();
        $buffer = [];
        while ($this->top() !== $maxVal) $buffer[] = $this->pop();
        $this->pop();
        for ($i = count($buffer) - 1; $i >= 0; $i--) $this->push($buffer[$i]);
        return $maxVal;
    }
}
""")

add("0717_1_bit_and_2_bit_characters", r"""<?php
// LeetCode 0717 - 1-bit and 2-bit Characters
// https://leetcode.com/problems/1-bit-and-2-bit-characters/

class Solution {
    function isOneBitCharacter($bits) {
        $i = 0;
        $n = count($bits);
        while ($i < $n - 1) $i += $bits[$i] === 1 ? 2 : 1;
        return $i === $n - 1;
    }
}
""")

add("0718_maximum_length_of_repeated_subarray", r"""<?php
// LeetCode 0718 - Maximum Length of Repeated Subarray
// https://leetcode.com/problems/maximum-length-of-repeated-subarray/

class Solution {
    function findLength($nums1, $nums2) {
        $m = count($nums1);
        $n = count($nums2);
        $best = 0;
        $dp = array_fill(0, $n + 1, 0);
        for ($i = 1; $i <= $m; $i++) {
            $next = array_fill(0, $n + 1, 0);
            for ($j = 1; $j <= $n; $j++) {
                if ($nums1[$i - 1] === $nums2[$j - 1]) {
                    $next[$j] = $dp[$j - 1] + 1;
                    $best = max($best, $next[$j]);
                }
            }
            $dp = $next;
        }
        return $best;
    }
}
""")

add("0719_find_k_th_smallest_pair_distance", r"""<?php
// LeetCode 0719 - Find K-th Smallest Pair Distance
// https://leetcode.com/problems/find-k-th-smallest-pair-distance/

class Solution {
    function smallestDistancePair($nums, $k) {
        sort($nums);
        $countPairs = function ($distance) use ($nums) {
            $count = 0;
            $left = 0;
            $n = count($nums);
            for ($right = 0; $right < $n; $right++) {
                while ($nums[$right] - $nums[$left] > $distance) $left++;
                $count += $right - $left;
            }
            return $count;
        };
        $lo = 0;
        $hi = $nums[count($nums) - 1] - $nums[0];
        while ($lo < $hi) {
            $mid = $lo + intdiv($hi - $lo, 2);
            if ($countPairs($mid) >= $k) $hi = $mid;
            else $lo = $mid + 1;
        }
        return $lo;
    }
}
""")

add("0720_longest_word_in_dictionary", r"""<?php
// LeetCode 0720 - Longest Word in Dictionary
// https://leetcode.com/problems/longest-word-in-dictionary/

class Solution {
    function longestWord($words) {
        sort($words);
        $built = ['' => true];
        $best = '';
        foreach ($words as $word) {
            $prefix = substr($word, 0, strlen($word) - 1);
            if (isset($built[$prefix])) {
                $built[$word] = true;
                if (strlen($word) > strlen($best)) $best = $word;
            }
        }
        return $best;
    }
}
""")

add("0721_accounts_merge", r"""<?php
// LeetCode 0721 - Accounts Merge
// https://leetcode.com/problems/accounts-merge/

class Solution {
    function accountsMerge($accounts) {
        $parent = [];
        $find = function ($x) use (&$find, &$parent) {
            if (!array_key_exists($x, $parent)) $parent[$x] = $x;
            while ($parent[$x] !== $x) {
                $parent[$x] = $parent[$parent[$x]];
                $x = $parent[$x];
            }
            return $x;
        };
        $unite = function ($a, $b) use (&$find, &$parent) {
            $parent[$find($a)] = $find($b);
        };
        $emailName = [];
        foreach ($accounts as $account) {
            $name = $account[0];
            $first = $account[1];
            for ($i = 1; $i < count($account); $i++) {
                $email = $account[$i];
                if (!array_key_exists($email, $parent)) $parent[$email] = $email;
                $emailName[$email] = $name;
                $unite($first, $email);
            }
        }
        $groups = [];
        foreach ($parent as $email => $_) {
            $root = $find($email);
            if (!isset($groups[$root])) $groups[$root] = [];
            $groups[$root][] = $email;
        }
        $result = [];
        foreach ($groups as $emails) {
            sort($emails);
            $result[] = array_merge([$emailName[$emails[0]]], $emails);
        }
        return $result;
    }
}
""")

add("0722_remove_comments", r"""<?php
// LeetCode 0722 - Remove Comments
// https://leetcode.com/problems/remove-comments/

class Solution {
    function removeComments($source) {
        $result = [];
        $buffer = '';
        $inBlock = false;
        foreach ($source as $line) {
            $i = 0;
            $len = strlen($line);
            while ($i < $len) {
                if ($inBlock) {
                    if ($i + 1 < $len && $line[$i] === '*' && $line[$i + 1] === '/') {
                        $inBlock = false;
                        $i += 2;
                    } else $i++;
                } else if ($i + 1 < $len && $line[$i] === '/' && $line[$i + 1] === '*') {
                    $inBlock = true;
                    $i += 2;
                } else if ($i + 1 < $len && $line[$i] === '/' && $line[$i + 1] === '/') break;
                else $buffer .= $line[$i++];
            }
            if (!$inBlock && strlen($buffer) > 0) {
                $result[] = $buffer;
                $buffer = '';
            }
        }
        return $result;
    }
}
""")

add("0723_candy_crush", r"""<?php
// LeetCode 0723 - Candy Crush
// https://leetcode.com/problems/candy-crush/

class Solution {
    function candyCrush($board) {
        $m = count($board);
        $n = count($board[0]);
        $stable = false;
        while (!$stable) {
            $stable = true;
            for ($i = 0; $i < $m; $i++) {
                for ($j = 0; $j < $n - 2; $j++) {
                    $value = abs($board[$i][$j]);
                    if ($value !== 0 && $value === abs($board[$i][$j + 1]) && $value === abs($board[$i][$j + 2])) {
                        $board[$i][$j] = $board[$i][$j + 1] = $board[$i][$j + 2] = -$value;
                        $stable = false;
                    }
                }
            }
            for ($j = 0; $j < $n; $j++) {
                for ($i = 0; $i < $m - 2; $i++) {
                    $value = abs($board[$i][$j]);
                    if ($value !== 0 && $value === abs($board[$i + 1][$j]) && $value === abs($board[$i + 2][$j])) {
                        $board[$i][$j] = $board[$i + 1][$j] = $board[$i + 2][$j] = -$value;
                        $stable = false;
                    }
                }
            }
            for ($j = 0; $j < $n; $j++) {
                $write = $m - 1;
                for ($i = $m - 1; $i >= 0; $i--) {
                    if ($board[$i][$j] > 0) $board[$write--][$j] = $board[$i][$j];
                }
                for ($i = $write; $i >= 0; $i--) $board[$i][$j] = 0;
            }
        }
        return $board;
    }
}
""")

add("0724_find_pivot_index", r"""<?php
// LeetCode 0724 - Find Pivot Index
// https://leetcode.com/problems/find-pivot-index/

class Solution {
    function pivotIndex($nums) {
        $total = 0;
        foreach ($nums as $x) $total += $x;
        $left = 0;
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            if ($left === $total - $left - $nums[$i]) return $i;
            $left += $nums[$i];
        }
        return -1;
    }
}
""")

add("0725_split_linked_list_in_parts", """<?php
// LeetCode 0725 - Split Linked List in Parts
// https://leetcode.com/problems/split-linked-list-in-parts/

""" + LISTN + r"""
class Solution {
    function splitListToParts($head, $k) {
        $length = 0;
        for ($node = $head; $node !== null; $node = $node->next) $length++;
        $partSize = intdiv($length, $k);
        $extra = $length % $k;
        $result = array_fill(0, $k, null);
        $current = $head;
        for ($i = 0; $i < $k; $i++) {
            $result[$i] = $current;
            $size = $partSize + ($i < $extra ? 1 : 0);
            for ($j = 0; $j < $size - 1 && $current !== null; $j++) $current = $current->next;
            if ($current !== null) {
                $nxt = $current->next;
                $current->next = null;
                $current = $nxt;
            }
        }
        return $result;
    }
}
""")

add("0726_number_of_atoms", r"""<?php
// LeetCode 0726 - Number of Atoms
// https://leetcode.com/problems/number-of-atoms/

class Solution {
    function countOfAtoms($formula) {
        $st = [[]];
        $i = 0;
        $n = strlen($formula);
        while ($i < $n) {
            if ($formula[$i] === '(') {
                $st[] = [];
                $i++;
            } else if ($formula[$i] === ')') {
                $i++;
                $start = $i;
                while ($i < $n && $formula[$i] >= '0' && $formula[$i] <= '9') $i++;
                $mult = $start < $i ? intval(substr($formula, $start, $i - $start), 10) : 1;
                $top = array_pop($st);
                $peekIdx = count($st) - 1;
                foreach ($top as $key => $value) {
                    $st[$peekIdx][$key] = ($st[$peekIdx][$key] ?? 0) + $value * $mult;
                }
            } else {
                $start = $i++;
                while ($i < $n && $formula[$i] >= 'a' && $formula[$i] <= 'z') $i++;
                $atom = substr($formula, $start, $i - $start);
                $start = $i;
                while ($i < $n && $formula[$i] >= '0' && $formula[$i] <= '9') $i++;
                $count = $start < $i ? intval(substr($formula, $start, $i - $start), 10) : 1;
                $peekIdx = count($st) - 1;
                $st[$peekIdx][$atom] = ($st[$peekIdx][$atom] ?? 0) + $count;
            }
        }
        $peek = $st[count($st) - 1];
        $keys = array_keys($peek);
        sort($keys);
        $result = '';
        foreach ($keys as $key) {
            $result .= $key;
            if ($peek[$key] > 1) $result .= $peek[$key];
        }
        return $result;
    }
}
""")

add("0727_minimum_window_subsequence", r"""<?php
// LeetCode 0727 - Minimum Window Subsequence
// https://leetcode.com/problems/minimum-window-subsequence/

class Solution {
    function minWindow($s1, $s2) {
        $m = strlen($s1);
        $n = strlen($s2);
        $best = '';
        $i = 0;
        while ($i < $m) {
            $j = 0;
            $k = $i;
            while ($k < $m && $j < $n) {
                if ($s1[$k] === $s2[$j]) $j++;
                $k++;
            }
            if ($j < $n) break;
            $end = $k - 1;
            $j = $n - 1;
            $k = $end;
            while ($j >= 0) {
                if ($s1[$k] === $s2[$j]) $j--;
                $k--;
            }
            $start = $k + 1;
            if (strlen($best) === 0 || $end - $start + 1 < strlen($best)) $best = substr($s1, $start, $end - $start + 1);
            $i = $start + 1;
        }
        return $best;
    }
}
""")

add("0728_self_dividing_numbers", r"""<?php
// LeetCode 0728 - Self Dividing Numbers
// https://leetcode.com/problems/self-dividing-numbers/

class Solution {
    function selfDividingNumbers($left, $right) {
        $isSelfDividing = function ($num) {
            $x = $num;
            while ($x > 0) {
                $digit = $x % 10;
                if ($digit === 0 || $num % $digit !== 0) return false;
                $x = intdiv($x, 10);
            }
            return true;
        };
        $result = [];
        for ($num = $left; $num <= $right; $num++) if ($isSelfDividing($num)) $result[] = $num;
        return $result;
    }
}
""")

add("0729_my_calendar_i", r"""<?php
// LeetCode 0729 - My Calendar I
// https://leetcode.com/problems/my-calendar-i/

class MyCalendar {
    private $bookings = [];

    function __construct() {
        $this->bookings = [];
    }

    function book($startTime, $endTime) {
        foreach ($this->bookings as $b) {
            if ($b[0] < $endTime && $startTime < $b[1]) return false;
        }
        $this->bookings[] = [$startTime, $endTime];
        return true;
    }
}
""")


def is_stub(path: Path) -> bool:
    return "function solve()" in path.read_text(encoding="utf-8")


def main() -> None:
    ported = 0
    for folder, content in SOLUTIONS.items():
        path = ROOT / folder / "solution.php"
        if not path.exists():
            print(f"MISSING {folder}")
            continue
        if not is_stub(path):
            print(f"skip done {folder}")
            continue
        path.write_text(content, encoding="utf-8", newline="\n")
        ported += 1
        print(f"ported {folder}")
    print(f"ported={ported} total={len(SOLUTIONS)}")


if __name__ == "__main__":
    main()

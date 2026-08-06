#!/usr/bin/env python3
"""Port stub solution.php files for problems 1143-1178 (non-SQL)."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOLUTIONS: dict[str, str] = {}


def add(name: str, content: str) -> None:
    SOLUTIONS[name] = content.strip() + "\n"


add("1143_longest_common_subsequence", r"""<?php
// LeetCode 1143 - Longest Common Subsequence
// https://leetcode.com/problems/longest-common-subsequence/

class Solution {
    /**
     * @param String $text1
     * @param String $text2
     * @return Integer
     */
    function longestCommonSubsequence($text1, $text2) {
        $m = strlen($text1);
        $n = strlen($text2);
        $dp = array_fill(0, $n + 1, 0);
        for ($i = 1; $i <= $m; $i++) {
            $prev = 0;
            for ($j = 1; $j <= $n; $j++) {
                $cur = $dp[$j];
                if ($text1[$i - 1] === $text2[$j - 1]) {
                    $dp[$j] = $prev + 1;
                } else {
                    $dp[$j] = max($dp[$j], $dp[$j - 1]);
                }
                $prev = $cur;
            }
        }
        return $dp[$n];
    }
}
""")

add("1144_decrease_elements_to_make_array_zigzag", r"""<?php
// LeetCode 1144 - Decrease Elements To Make Array Zigzag
// https://leetcode.com/problems/decrease-elements-to-make-array-zigzag/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function movesToMakeZigzag($nums) {
        $cost = function ($start) use ($nums) {
            $ans = 0;
            $n = count($nums);
            for ($i = $start; $i < $n; $i += 2) {
                $left = $i > 0 ? $nums[$i - 1] : PHP_INT_MAX;
                $right = $i + 1 < $n ? $nums[$i + 1] : PHP_INT_MAX;
                $ans += max(0, $nums[$i] - min($left, $right) + 1);
            }
            return $ans;
        };
        return min($cost(0), $cost(1));
    }
}
""")

add("1145_binary_tree_coloring_game", r"""<?php
// LeetCode 1145 - Binary Tree Coloring Game
// https://leetcode.com/problems/binary-tree-coloring-game/

class Solution {
    private $left = 0;
    private $right = 0;

    /**
     * @param TreeNode $root
     * @param Integer $n
     * @param Integer $x
     * @return Boolean
     */
    function btreeGameWinningMove($root, $n, $x) {
        $this->left = $this->right = 0;
        $this->dfs($root, $x);
        return max($this->left, $this->right, $n - $this->left - $this->right - 1) > intdiv($n, 2);
    }

    private function dfs($node, $x) {
        if ($node === null) return 0;
        $l = $this->dfs($node->left, $x);
        $r = $this->dfs($node->right, $x);
        if ($node->val === $x) {
            $this->left = $l;
            $this->right = $r;
        }
        return $l + $r + 1;
    }
}
""")

add("1146_snapshot_array", r"""<?php
// LeetCode 1146 - Snapshot Array
// https://leetcode.com/problems/snapshot-array/

class SnapshotArray {
    private $snapId = 0;
    private $data = [];

    /**
     * @param Integer $length
     */
    function __construct($length) {
        for ($i = 0; $i < $length; $i++) {
            $this->data[$i] = [[0, 0]];
        }
    }

    /**
     * @param Integer $index
     * @param Integer $val
     * @return NULL
     */
    function set($index, $val) {
        $hist = &$this->data[$index];
        $last = count($hist) - 1;
        if ($hist[$last][0] === $this->snapId) {
            $hist[$last][1] = $val;
        } else {
            $hist[] = [$this->snapId, $val];
        }
    }

    /**
     * @return Integer
     */
    function snap() {
        return $this->snapId++;
    }

    /**
     * @param Integer $index
     * @param Integer $snap_id
     * @return Integer
     */
    function get($index, $snap_id) {
        $hist = $this->data[$index];
        $lo = 0;
        $hi = count($hist) - 1;
        $ans = 0;
        while ($lo <= $hi) {
            $mid = ($lo + $hi) >> 1;
            if ($hist[$mid][0] <= $snap_id) {
                $ans = $mid;
                $lo = $mid + 1;
            } else {
                $hi = $mid - 1;
            }
        }
        return $hist[$ans][1];
    }
}
""")

add("1147_longest_chunked_palindrome_decomposition", r"""<?php
// LeetCode 1147 - Longest Chunked Palindrome Decomposition
// https://leetcode.com/problems/longest-chunked-palindrome-decomposition/

class Solution {
    /**
     * @param String $text
     * @return Integer
     */
    function longestDecomposition($text) {
        $n = strlen($text);
        $ans = 0;
        $i = 0;
        while ($i < $n - $i) {
            $found = false;
            $maxLen = intdiv($n - 2 * $i, 2);
            for ($length = 1; $length <= $maxLen; $length++) {
                if (substr($text, $i, $length) === substr($text, $n - $i - $length, $length)) {
                    $ans += 2;
                    $i += $length;
                    $found = true;
                    break;
                }
            }
            if (!$found) {
                $ans++;
                break;
            }
        }
        return $ans;
    }
}
""")

add("1150_check_if_a_number_is_majority_element_in_a_sorted_array", r"""<?php
// LeetCode 1150 - Check If a Number Is Majority Element in a Sorted Array
// https://leetcode.com/problems/check-if-a-number-is-majority-element-in-a-sorted-array/

class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $target
     * @return Boolean
     */
    function isMajorityElement($nums, $target) {
        $n = count($nums);
        $lo = 0; $hi = $n;
        while ($lo < $hi) {
            $mid = ($lo + $hi) >> 1;
            if ($nums[$mid] < $target) $lo = $mid + 1;
            else $hi = $mid;
        }
        $left = $lo;
        $lo = 0; $hi = $n;
        while ($lo < $hi) {
            $mid = ($lo + $hi) >> 1;
            if ($nums[$mid] <= $target) $lo = $mid + 1;
            else $hi = $mid;
        }
        return $lo - $left > intdiv($n, 2);
    }
}
""")

add("1151_minimum_swaps_to_group_all_1s_together", r"""<?php
// LeetCode 1151 - Minimum Swaps to Group All 1's Together
// https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together/

class Solution {
    /**
     * @param Integer[] $data
     * @return Integer
     */
    function minSwaps($data) {
        $ones = array_sum($data);
        if ($ones <= 1) return 0;
        $cur = array_sum(array_slice($data, 0, $ones));
        $best = $cur;
        $n = count($data);
        for ($i = $ones; $i < $n; $i++) {
            $cur += $data[$i] - $data[$i - $ones];
            $best = max($best, $cur);
        }
        return $ones - $best;
    }
}
""")

add("1152_analyze_user_website_visit_pattern", r"""<?php
// LeetCode 1152 - Analyze User Website Visit Pattern
// https://leetcode.com/problems/analyze-user-website-visit-pattern/

class Solution {
    /**
     * @param String[] $username
     * @param Integer[] $timestamp
     * @param String[] $website
     * @return String[]
     */
    function mostVisitedPattern($username, $timestamp, $website) {
        $visits = [];
        $n = count($username);
        for ($i = 0; $i < $n; $i++) {
            $visits[$username[$i]][] = [$timestamp[$i], $website[$i]];
        }
        $scores = [];
        foreach ($visits as $user => $list) {
            usort($list, fn($a, $b) => $a[0] <=> $b[0]);
            $sites = array_map(fn($x) => $x[1], $list);
            $patterns = [];
            $m = count($sites);
            for ($i = 0; $i < $m; $i++) {
                for ($j = $i + 1; $j < $m; $j++) {
                    for ($k = $j + 1; $k < $m; $k++) {
                        $key = $sites[$i] . "\0" . $sites[$j] . "\0" . $sites[$k];
                        $patterns[$key] = [$sites[$i], $sites[$j], $sites[$k]];
                    }
                }
            }
            foreach ($patterns as $key => $pattern) {
                $scores[$key] = ($scores[$key] ?? [0, $pattern]);
                $scores[$key][0]++;
            }
        }
        $bestCount = -1;
        $best = null;
        foreach ($scores as [$count, $pattern]) {
            if ($count > $bestCount || ($count === $bestCount && ($best === null || $pattern < $best))) {
                $bestCount = $count;
                $best = $pattern;
            }
        }
        return $best;
    }
}
""")

add("1153_string_transforms_into_another_string", r"""<?php
// LeetCode 1153 - String Transforms Into Another String
// https://leetcode.com/problems/string-transforms-into-another-string/

class Solution {
    /**
     * @param String $str1
     * @param String $str2
     * @return Boolean
     */
    function canConvert($str1, $str2) {
        if ($str1 === $str2) return true;
        $mapping = [];
        $n = strlen($str1);
        for ($i = 0; $i < $n; $i++) {
            $a = $str1[$i];
            $b = $str2[$i];
            if (isset($mapping[$a]) && $mapping[$a] !== $b) return false;
            $mapping[$a] = $b;
        }
        return count(array_unique(str_split($str2))) < 26;
    }
}
""")

add("1154_day_of_the_year", r"""<?php
// LeetCode 1154 - Day of the Year
// https://leetcode.com/problems/day-of-the-year/

class Solution {
    /**
     * @param String $date
     * @return Integer
     */
    function dayOfYear($date) {
        [$year, $month, $day] = array_map('intval', explode('-', $date));
        $leap = ($year % 4 === 0 && $year % 100 !== 0) || ($year % 400 === 0);
        $days = [31, $leap ? 29 : 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
        return array_sum(array_slice($days, 0, $month - 1)) + $day;
    }
}
""")

add("1155_number_of_dice_rolls_with_target_sum", r"""<?php
// LeetCode 1155 - Number of Dice Rolls With Target Sum
// https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/

class Solution {
    /**
     * @param Integer $n
     * @param Integer $k
     * @param Integer $target
     * @return Integer
     */
    function numRollsToTarget($n, $k, $target) {
        $mod = 1000000007;
        $dp = array_fill(0, $target + 1, 0);
        $dp[0] = 1;
        for ($dice = 0; $dice < $n; $dice++) {
            $new = array_fill(0, $target + 1, 0);
            for ($s = 0; $s <= $target; $s++) {
                if ($dp[$s] === 0) continue;
                for ($face = 1; $face <= $k; $face++) {
                    if ($s + $face <= $target) {
                        $new[$s + $face] = ($new[$s + $face] + $dp[$s]) % $mod;
                    }
                }
            }
            $dp = $new;
        }
        return $dp[$target];
    }
}
""")

add("1156_swap_for_longest_repeated_character_substring", r"""<?php
// LeetCode 1156 - Swap For Longest Repeated Character Substring
// https://leetcode.com/problems/swap-for-longest-repeated-character-substring/

class Solution {
    /**
     * @param String $text
     * @return Integer
     */
    function maxRepOpt1($text) {
        $count = array_count_values(str_split($text));
        $n = strlen($text);
        $ans = 0;
        $i = 0;
        while ($i < $n) {
            $j = $i;
            while ($j < $n && $text[$j] === $text[$i]) $j++;
            $length = $j - $i;
            $k = $j + 1;
            while ($k < $n && $text[$k] === $text[$i]) $k++;
            $length2 = $j < $n ? $k - $j - 1 : 0;
            $ans = max($ans, min($length + $length2 + 1, $count[$text[$i]]));
            $i = $j;
        }
        return $ans;
    }
}
""")

add("1157_online_majority_element_in_subarray", r"""<?php
// LeetCode 1157 - Online Majority Element In Subarray
// https://leetcode.com/problems/online-majority-element-in-subarray/

class MajorityChecker {
    private $arr;
    private $pos = [];

    /**
     * @param Integer[] $arr
     */
    function __construct($arr) {
        $this->arr = $arr;
        foreach ($arr as $i => $x) {
            $this->pos[$x][] = $i;
        }
    }

    /**
     * @param Integer $left
     * @param Integer $right
     * @param Integer $threshold
     * @return Integer
     */
    function query($left, $right, $threshold) {
        $candidate = 0;
        $count = 0;
        for ($i = $left; $i <= $right; $i++) {
            if ($count === 0) $candidate = $this->arr[$i];
            $count += $this->arr[$i] === $candidate ? 1 : -1;
        }
        $locs = $this->pos[$candidate] ?? [];
        $lo = 0; $hi = count($locs);
        while ($lo < $hi) {
            $mid = ($lo + $hi) >> 1;
            if ($locs[$mid] < $left) $lo = $mid + 1;
            else $hi = $mid;
        }
        $L = $lo;
        $lo = 0; $hi = count($locs);
        while ($lo < $hi) {
            $mid = ($lo + $hi) >> 1;
            if ($locs[$mid] <= $right) $lo = $mid + 1;
            else $hi = $mid;
        }
        return ($lo - $L) >= $threshold ? $candidate : -1;
    }
}
""")

add("1160_find_words_that_can_be_formed_by_characters", r"""<?php
// LeetCode 1160 - Find Words That Can Be Formed by Characters
// https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/

class Solution {
    /**
     * @param String[] $words
     * @param String $chars
     * @return Integer
     */
    function countCharacters($words, $chars) {
        $avail = array_count_values(str_split($chars));
        $ans = 0;
        foreach ($words as $word) {
            $need = array_count_values(str_split($word));
            $ok = true;
            foreach ($need as $c => $v) {
                if (($avail[$c] ?? 0) < $v) { $ok = false; break; }
            }
            if ($ok) $ans += strlen($word);
        }
        return $ans;
    }
}
""")

add("1161_maximum_level_sum_of_a_binary_tree", r"""<?php
// LeetCode 1161 - Maximum Level Sum of a Binary Tree
// https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/

class Solution {
    /**
     * @param TreeNode $root
     * @return Integer
     */
    function maxLevelSum($root) {
        $queue = [$root];
        $bestSum = PHP_INT_MIN;
        $bestLevel = $level = 1;
        $head = 0;
        while ($head < count($queue)) {
            $sz = count($queue) - $head;
            $total = 0;
            for ($i = 0; $i < $sz; $i++) {
                $node = $queue[$head++];
                $total += $node->val;
                if ($node->left !== null) $queue[] = $node->left;
                if ($node->right !== null) $queue[] = $node->right;
            }
            if ($total > $bestSum) {
                $bestSum = $total;
                $bestLevel = $level;
            }
            $level++;
        }
        return $bestLevel;
    }
}
""")

add("1162_as_far_from_land_as_possible", r"""<?php
// LeetCode 1162 - As Far from Land as Possible
// https://leetcode.com/problems/as-far-from-land-as-possible/

class Solution {
    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function maxDistance($grid) {
        $n = count($grid);
        $queue = [];
        for ($r = 0; $r < $n; $r++) {
            for ($c = 0; $c < $n; $c++) {
                if ($grid[$r][$c] === 1) $queue[] = [$r, $c];
            }
        }
        if (empty($queue) || count($queue) === $n * $n) return -1;
        $dist = -1;
        $head = 0;
        $dirs = [[1,0],[-1,0],[0,1],[0,-1]];
        while ($head < count($queue)) {
            $dist++;
            $sz = count($queue) - $head;
            for ($i = 0; $i < $sz; $i++) {
                [$r, $c] = $queue[$head++];
                foreach ($dirs as [$dr, $dc]) {
                    $nr = $r + $dr; $nc = $c + $dc;
                    if ($nr >= 0 && $nr < $n && $nc >= 0 && $nc < $n && $grid[$nr][$nc] === 0) {
                        $grid[$nr][$nc] = 1;
                        $queue[] = [$nr, $nc];
                    }
                }
            }
        }
        return $dist;
    }
}
""")

add("1163_last_substring_in_lexicographical_order", r"""<?php
// LeetCode 1163 - Last Substring in Lexicographical Order
// https://leetcode.com/problems/last-substring-in-lexicographical-order/

class Solution {
    /**
     * @param String $s
     * @return String
     */
    function lastSubstring($s) {
        $i = 0; $j = 1; $k = 0;
        $n = strlen($s);
        while ($j + $k < $n) {
            if ($s[$i + $k] === $s[$j + $k]) {
                $k++;
                continue;
            }
            if ($s[$i + $k] > $s[$j + $k]) {
                $j = $j + $k + 1;
            } else {
                $i = max($i + $k + 1, $j);
                $j = $i + 1;
            }
            $k = 0;
        }
        return substr($s, $i);
    }
}
""")

add("1165_single_row_keyboard", r"""<?php
// LeetCode 1165 - Single-Row Keyboard
// https://leetcode.com/problems/single-row-keyboard/

class Solution {
    /**
     * @param String $keyboard
     * @param String $word
     * @return Integer
     */
    function calculateTime($keyboard, $word) {
        $pos = [];
        for ($i = 0; $i < strlen($keyboard); $i++) $pos[$keyboard[$i]] = $i;
        $ans = 0; $prev = 0;
        for ($i = 0; $i < strlen($word); $i++) {
            $ans += abs($pos[$word[$i]] - $prev);
            $prev = $pos[$word[$i]];
        }
        return $ans;
    }
}
""")

add("1166_design_file_system", r"""<?php
// LeetCode 1166 - Design File System
// https://leetcode.com/problems/design-file-system/

class FileSystem {
    private $paths = ['' => -1];

    function __construct() {}

    /**
     * @param String $path
     * @param Integer $value
     * @return Boolean
     */
    function createPath($path, $value) {
        if (isset($this->paths[$path])) return false;
        $parent = substr($path, 0, strrpos($path, '/'));
        if (!isset($this->paths[$parent])) return false;
        $this->paths[$path] = $value;
        return true;
    }

    /**
     * @param String $path
     * @return Integer
     */
    function get($path) {
        return $this->paths[$path] ?? -1;
    }
}
""")

add("1167_minimum_cost_to_connect_sticks", r"""<?php
// LeetCode 1167 - Minimum Cost to Connect Sticks
// https://leetcode.com/problems/minimum-cost-to-connect-sticks/

class Solution {
    /**
     * @param Integer[] $sticks
     * @return Integer
     */
    function connectSticks($sticks) {
        if (count($sticks) <= 1) return 0;
        $heap = new SplMinHeap();
        foreach ($sticks as $s) $heap->insert($s);
        $ans = 0;
        while ($heap->count() > 1) {
            $cost = $heap->extract() + $heap->extract();
            $ans += $cost;
            $heap->insert($cost);
        }
        return $ans;
    }
}
""")

add("1168_optimize_water_distribution_in_a_village", r"""<?php
// LeetCode 1168 - Optimize Water Distribution in a Village
// https://leetcode.com/problems/optimize-water-distribution-in-a-village/

class Solution {
    /**
     * @param Integer $n
     * @param Integer[] $wells
     * @param Integer[][] $pipes
     * @return Integer
     */
    function minCostToSupplyWater($n, $wells, $pipes) {
        $parent = range(0, $n);
        $find = function ($x) use (&$parent, &$find) {
            while ($parent[$x] !== $x) {
                $parent[$x] = $parent[$parent[$x]];
                $x = $parent[$x];
            }
            return $x;
        };
        $edges = [];
        foreach ($wells as $i => $w) $edges[] = [0, $i + 1, $w];
        foreach ($pipes as $p) $edges[] = $p;
        usort($edges, fn($a, $b) => $a[2] <=> $b[2]);
        $ans = 0;
        foreach ($edges as [$a, $b, $cost]) {
            $ra = $find($a); $rb = $find($b);
            if ($ra === $rb) continue;
            $parent[$rb] = $ra;
            $ans += $cost;
        }
        return $ans;
    }
}
""")

add("1169_invalid_transactions", r"""<?php
// LeetCode 1169 - Invalid Transactions
// https://leetcode.com/problems/invalid-transactions/

class Solution {
    /**
     * @param String[] $transactions
     * @return String[]
     */
    function invalidTransactions($transactions) {
        $parsed = [];
        foreach ($transactions as $t) {
            [$name, $time, $amount, $city] = explode(',', $t);
            $parsed[] = [$name, (int)$time, (int)$amount, $city, $t];
        }
        $invalid = [];
        $m = count($parsed);
        for ($i = 0; $i < $m; $i++) {
            [$name, $time, $amount, $city, $raw] = $parsed[$i];
            if ($amount > 1000) $invalid[$raw] = true;
            for ($j = 0; $j < $m; $j++) {
                if ($i === $j) continue;
                [$name2, $time2, , $city2, $raw2] = $parsed[$j];
                if ($name === $name2 && $city !== $city2 && abs($time - $time2) <= 60) {
                    $invalid[$raw] = true;
                    $invalid[$raw2] = true;
                }
            }
        }
        return array_keys($invalid);
    }
}
""")

add("1170_compare_strings_by_frequency_of_the_smallest_character", r"""<?php
// LeetCode 1170 - Compare Strings by Frequency of the Smallest Character
// https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/

class Solution {
    /**
     * @param String[] $queries
     * @param String[] $words
     * @return Integer[]
     */
    function numSmallerByFrequency($queries, $words) {
        $f = function ($s) {
            $min = min(str_split($s));
            return substr_count($s, $min);
        };
        $freqs = array_map($f, $words);
        sort($freqs);
        $ans = [];
        foreach ($queries as $q) {
            $fq = $f($q);
            $lo = 0; $hi = count($freqs);
            while ($lo < $hi) {
                $mid = ($lo + $hi) >> 1;
                if ($freqs[$mid] <= $fq) $lo = $mid + 1;
                else $hi = $mid;
            }
            $ans[] = count($freqs) - $lo;
        }
        return $ans;
    }
}
""")

add("1171_remove_zero_sum_consecutive_nodes_from_linked_list", r"""<?php
// LeetCode 1171 - Remove Zero Sum Consecutive Nodes from Linked List
// https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/

class Solution {
    /**
     * @param ListNode $head
     * @return ListNode
     */
    function removeZeroSumSublists($head) {
        $dummy = (object)['val' => 0, 'next' => $head];
        $prefix = 0;
        $seen = [0 => $dummy];
        $node = $dummy;
        while ($node !== null) {
            $prefix += $node->val;
            $seen[$prefix] = $node;
            $node = $node->next;
        }
        $prefix = 0;
        $node = $dummy;
        while ($node !== null) {
            $prefix += $node->val;
            $node->next = $seen[$prefix]->next;
            $node = $node->next;
        }
        return $dummy->next;
    }
}
""")

add("1172_dinner_plate_stacks", r"""<?php
// LeetCode 1172 - Dinner Plate Stacks
// https://leetcode.com/problems/dinner-plate-stacks/

class DinnerPlates {
    private $capacity;
    private $stacks = [];
    private $available;

    /**
     * @param Integer $capacity
     */
    function __construct($capacity) {
        $this->capacity = $capacity;
        $this->available = new SplMinHeap();
    }

    /**
     * @param Integer $val
     * @return NULL
     */
    function push($val) {
        while (!$this->available->isEmpty()) {
            $top = $this->available->top();
            if ($top >= count($this->stacks) || count($this->stacks[$top]) === $this->capacity) {
                $this->available->extract();
            } else break;
        }
        if ($this->available->isEmpty()) {
            $this->stacks[] = [];
            $this->available->insert(count($this->stacks) - 1);
        }
        $idx = $this->available->top();
        $this->stacks[$idx][] = $val;
        if (count($this->stacks[$idx]) === $this->capacity) {
            $this->available->extract();
        }
    }

    /**
     * @return Integer
     */
    function pop() {
        while (!empty($this->stacks) && empty($this->stacks[count($this->stacks) - 1])) {
            array_pop($this->stacks);
        }
        return empty($this->stacks) ? -1 : $this->popAtStack(count($this->stacks) - 1);
    }

    /**
     * @param Integer $index
     * @return Integer
     */
    function popAtStack($index) {
        if ($index < 0 || $index >= count($this->stacks) || empty($this->stacks[$index])) return -1;
        if (count($this->stacks[$index]) === $this->capacity) {
            $this->available->insert($index);
        }
        return array_pop($this->stacks[$index]);
    }
}
""")

add("1175_prime_arrangements", r"""<?php
// LeetCode 1175 - Prime Arrangements
// https://leetcode.com/problems/prime-arrangements/

class Solution {
    /**
     * @param Integer $n
     * @return Integer
     */
    function numPrimeArrangements($n) {
        $mod = 1000000007;
        $isPrime = function ($x) {
            if ($x < 2) return false;
            for ($d = 2; $d * $d <= $x; $d++) {
                if ($x % $d === 0) return false;
            }
            return true;
        };
        $primes = 0;
        for ($i = 1; $i <= $n; $i++) if ($isPrime($i)) $primes++;
        $fact = function ($x) use ($mod) {
            $ans = 1;
            for ($i = 2; $i <= $x; $i++) $ans = $ans * $i % $mod;
            return $ans;
        };
        return $fact($primes) * $fact($n - $primes) % $mod;
    }
}
""")

add("1176_diet_plan_performance", r"""<?php
// LeetCode 1176 - Diet Plan Performance
// https://leetcode.com/problems/diet-plan-performance/

class Solution {
    /**
     * @param Integer[] $calories
     * @param Integer $k
     * @param Integer $lower
     * @param Integer $upper
     * @return Integer
     */
    function dietPlanPerformance($calories, $k, $lower, $upper) {
        $window = array_sum(array_slice($calories, 0, $k));
        $ans = 0;
        if ($window < $lower) $ans--;
        elseif ($window > $upper) $ans++;
        $n = count($calories);
        for ($i = $k; $i < $n; $i++) {
            $window += $calories[$i] - $calories[$i - $k];
            if ($window < $lower) $ans--;
            elseif ($window > $upper) $ans++;
        }
        return $ans;
    }
}
""")

add("1177_can_make_palindrome_from_substring", r"""<?php
// LeetCode 1177 - Can Make Palindrome from Substring
// https://leetcode.com/problems/can-make-palindrome-from-substring/

class Solution {
    /**
     * @param String $s
     * @param Integer[][] $queries
     * @return Boolean[]
     */
    function canMakePaliQueries($s, $queries) {
        $prefix = [0];
        $mask = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $mask ^= 1 << (ord($s[$i]) - 97);
            $prefix[] = $mask;
        }
        $ans = [];
        foreach ($queries as [$left, $right, $k]) {
            $bits = $prefix[$right + 1] ^ $prefix[$left];
            $ans[] = (substr_count(decbin($bits), '1') >> 1) <= $k;
        }
        return $ans;
    }
}
""")

add("1178_number_of_valid_words_for_each_puzzle", r"""<?php
// LeetCode 1178 - Number of Valid Words for Each Puzzle
// https://leetcode.com/problems/number-of-valid-words-for-each-puzzle/

class Solution {
    /**
     * @param String[] $words
     * @param String[] $puzzles
     * @return Integer[]
     */
    function findNumOfValidWords($words, $puzzles) {
        $maskOf = function ($s) {
            $mask = 0;
            $n = strlen($s);
            for ($i = 0; $i < $n; $i++) $mask |= 1 << (ord($s[$i]) - 97);
            return $mask;
        };
        $freq = [];
        foreach ($words as $w) {
            $m = $maskOf($w);
            $freq[$m] = ($freq[$m] ?? 0) + 1;
        }
        $ans = [];
        foreach ($puzzles as $puzzle) {
            $first = 1 << (ord($puzzle[0]) - 97);
            $full = $maskOf($puzzle);
            $sub = $full;
            $total = 0;
            while (true) {
                if ($sub & $first) $total += $freq[$sub] ?? 0;
                if ($sub === 0) break;
                $sub = ($sub - 1) & $full;
            }
            $ans[] = $total;
        }
        return $ans;
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

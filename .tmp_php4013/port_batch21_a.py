#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
SOLUTIONS = {}

def add(folder, body):
    SOLUTIONS[folder] = body


add("3823_reverse_letters_then_special_characters_in_a_string", r'''<?php
// LeetCode 3823 - Reverse Letters Then Special Characters in a String
// https://leetcode.com/problems/reverse-letters-then-special-characters-in-a-string/

class Solution {
    function reverseByType($s) {
        $a = [];
        $b = [];
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $c = $s[$i];
            if (($c >= 'A' && $c <= 'Z') || ($c >= 'a' && $c <= 'z')) $a[] = $c;
            else $b[] = $c;
        }
        $j = count($a);
        $k = count($b);
        $arr = [];
        for ($i = 0; $i < $n; $i++) $arr[] = $s[$i];
        for ($i = 0; $i < $n; $i++) {
            if (($arr[$i] >= 'A' && $arr[$i] <= 'Z') || ($arr[$i] >= 'a' && $arr[$i] <= 'z')) $arr[$i] = $a[--$j];
            else $arr[$i] = $b[--$k];
        }
        return implode('', $arr);
    }
}
''')

add("3824_minimum_k_to_reduce_array_within_limit", r'''<?php
// LeetCode 3824 - Minimum K to Reduce Array Within Limit
// https://leetcode.com/problems/minimum-k-to-reduce-array-within-limit/

class Solution {
    function check($nums, $k) {
        $t = 0;
        foreach ($nums as $x) $t += intdiv($x + $k - 1, $k);
        return $t <= $k * $k;
    }
    function minimumK($nums) {
        $lo = 1;
        $hi = 100000;
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi, 2);
            if ($this->check($nums, $mid)) $hi = $mid;
            else $lo = $mid + 1;
        }
        return $lo;
    }
}
''')

add("3825_longest_strictly_increasing_subsequence_with_non_zero_bitwise_and", r'''<?php
// LeetCode 3825 - Longest Strictly Increasing Subsequence With Non Zero Bitwise AND
// https://leetcode.com/problems/longest-strictly-increasing-subsequence-with-non-zero-bitwise-and/

class Solution {
    function bitLen($x) {
        if ($x === 0) return 0;
        $n = 0;
        while ($x > 0) { $n++; $x >>= 1; }
        return $n;
    }
    function lis($arr) {
        $g = [];
        foreach ($arr as $x) {
            $lo = 0;
            $hi = count($g);
            while ($lo < $hi) {
                $mid = ($lo + $hi) >> 1;
                if ($g[$mid] < $x) $lo = $mid + 1;
                else $hi = $mid;
            }
            if ($lo === count($g)) $g[] = $x;
            else $g[$lo] = $x;
        }
        return count($g);
    }
    function longestSubsequence($nums) {
        $ans = 0;
        $mx = 0;
        foreach ($nums as $x) $mx = max($mx, $x);
        $m = $this->bitLen($mx);
        for ($i = 0; $i < $m; $i++) {
            $arr = [];
            foreach ($nums as $x) {
                if ((($x >> $i) & 1) !== 0) $arr[] = $x;
            }
            $ans = max($ans, $this->lis($arr));
        }
        return $ans;
    }
}
''')

add("3826_minimum_partition_score", r'''<?php
// LeetCode 3826 - Minimum Partition Score
// https://leetcode.com/problems/minimum-partition-score/

class Solution {
    public $previous;
    public $current;
    public $prefix;
    public $INF;
    function value($left, $right) {
        $sum = $this->prefix[$right] - $this->prefix[$left];
        return $sum * ($sum + 1) / 2;
    }
    function compute($lo, $hi, $optLo, $optHi) {
        if ($lo > $hi) return;
        $mid = ($lo + $hi) >> 1;
        $bestIndex = -1;
        $end = min($optHi, $mid - 1);
        for ($split = $optLo; $split <= $end; $split++) {
            if ($this->previous[$split] === $this->INF) continue;
            $candidate = $this->previous[$split] + $this->value($split, $mid);
            if ($candidate < $this->current[$mid]) {
                $this->current[$mid] = $candidate;
                $bestIndex = $split;
            }
        }
        if ($bestIndex === -1) $bestIndex = $optLo;
        $this->compute($lo, $mid - 1, $optLo, $bestIndex);
        $this->compute($mid + 1, $hi, $bestIndex, $optHi);
    }
    function minPartitionScore($nums, $k) {
        $n = count($nums);
        $this->INF = PHP_INT_MAX / 4;
        $this->prefix = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; $i++) $this->prefix[$i + 1] = $this->prefix[$i] + $nums[$i];
        $this->previous = array_fill(0, $n + 1, $this->INF);
        $this->previous[0] = 0;
        for ($parts = 1; $parts <= $k; $parts++) {
            $this->current = array_fill(0, $n + 1, $this->INF);
            $this->compute($parts, $n, $parts - 1, $n - 1);
            $this->previous = $this->current;
        }
        return $this->previous[$n];
    }
}
''')

add("3827_count_monobit_integers", r'''<?php
// LeetCode 3827 - Count Monobit Integers
// https://leetcode.com/problems/count-monobit-integers/

class Solution {
    function countMonobit($n) {
        $ans = 1;
        for ($i = 1, $x = 1; $x <= $n; $i++) {
            $ans++;
            $x += (1 << $i);
        }
        return $ans;
    }
}
''')

add("3828_final_element_after_subarray_deletions", r'''<?php
// LeetCode 3828 - Final Element After Subarray Deletions
// https://leetcode.com/problems/final-element-after-subarray-deletions/

class Solution {
    function finalElement($nums) {
        return max($nums[0], $nums[count($nums) - 1]);
    }
}
''')

add("3829_design_ride_sharing_system", r'''<?php
// LeetCode 3829 - Design Ride Sharing System
// https://leetcode.com/problems/design-ride-sharing-system/

class RideSharingSystem {
    public $t = 0;
    public $riders = [];
    public $drivers = [];
    public $d = [];
    public $riderKeys = [];
    public $driverKeys = [];
    function __construct() {
        $this->t = 0;
        $this->riders = [];
        $this->drivers = [];
        $this->d = [];
        $this->riderKeys = [];
        $this->driverKeys = [];
    }
    function addRider($riderId) {
        $this->d[$riderId] = $this->t;
        $this->riders[$this->t] = $riderId;
        $this->riderKeys[] = $this->t;
        $this->t++;
    }
    function addDriver($driverId) {
        $this->drivers[$this->t] = $driverId;
        $this->driverKeys[] = $this->t;
        $this->t++;
    }
    function matchDriverWithRider() {
        while (count($this->riderKeys) && !isset($this->riders[$this->riderKeys[0]])) array_shift($this->riderKeys);
        while (count($this->driverKeys) && !isset($this->drivers[$this->driverKeys[0]])) array_shift($this->driverKeys);
        if (!count($this->riderKeys) || !count($this->driverKeys)) return [-1, -1];
        $dKey = array_shift($this->driverKeys);
        $rKey = array_shift($this->riderKeys);
        $driverId = $this->drivers[$dKey];
        $riderId = $this->riders[$rKey];
        unset($this->drivers[$dKey]);
        unset($this->riders[$rKey]);
        return [$driverId, $riderId];
    }
    function cancelRider($riderId) {
        if (!isset($this->d[$riderId])) return;
        unset($this->riders[$this->d[$riderId]]);
    }
}
''')

add("3830_longest_alternating_subarray_after_removing_at_most_one_element", r'''<?php
// LeetCode 3830 - Longest Alternating Subarray After Removing at Most One Element
// https://leetcode.com/problems/longest-alternating-subarray-after-removing-at-most-one-element/

class Solution {
    function longestAlternating($nums) {
        $n = count($nums);
        $l1 = array_fill(0, $n, 1);
        $l2 = array_fill(0, $n, 1);
        $r1 = array_fill(0, $n, 1);
        $r2 = array_fill(0, $n, 1);
        $ans = 0;
        for ($i = 1; $i < $n; $i++) {
            if ($nums[$i - 1] < $nums[$i]) $l1[$i] = $l2[$i - 1] + 1;
            else if ($nums[$i - 1] > $nums[$i]) $l2[$i] = $l1[$i - 1] + 1;
            $ans = max($ans, max($l1[$i], $l2[$i]));
        }
        for ($i = $n - 2; $i >= 0; $i--) {
            if ($nums[$i + 1] > $nums[$i]) $r1[$i] = $r2[$i + 1] + 1;
            else if ($nums[$i + 1] < $nums[$i]) $r2[$i] = $r1[$i + 1] + 1;
        }
        for ($i = 1; $i < $n - 1; $i++) {
            if ($nums[$i - 1] < $nums[$i + 1]) $ans = max($ans, $l2[$i - 1] + $r2[$i + 1]);
            else if ($nums[$i - 1] > $nums[$i + 1]) $ans = max($ans, $l1[$i - 1] + $r1[$i + 1]);
        }
        return $ans;
    }
}
''')

add("3831_median_of_a_binary_search_tree_level", r'''<?php
// LeetCode 3831 - Median of a Binary Search Tree Level
// https://leetcode.com/problems/median-of-a-binary-search-tree-level/

class TreeNode {
    public $val = null;
    public $left = null;
    public $right = null;
    function __construct($val = 0, $left = null, $right = null) {
        $this->val = $val;
        $this->left = $left;
        $this->right = $right;
    }
}

class Solution {
    public $nums;
    public $level;
    function dfs($node, $i) {
        if (!$node) return;
        $this->dfs($node->left, $i + 1);
        if ($i === $this->level) $this->nums[] = $node->val;
        $this->dfs($node->right, $i + 1);
    }
    function levelMedian($root, $level) {
        $this->nums = [];
        $this->level = $level;
        $this->dfs($root, 0);
        if (!count($this->nums)) return -1;
        return $this->nums[intdiv(count($this->nums), 2)];
    }
}
''')

add("3833_count_dominant_indices", r'''<?php
// LeetCode 3833 - Count Dominant Indices
// https://leetcode.com/problems/count-dominant-indices/

class Solution {
    function dominantIndices($nums) {
        $n = count($nums);
        $ans = 0;
        $suf = $nums[$n - 1];
        for ($i = $n - 2; $i >= 0; $i--) {
            if ($nums[$i] * ($n - $i - 1) > $suf) $ans++;
            $suf += $nums[$i];
        }
        return $ans;
    }
}
''')

add("3834_merge_adjacent_equal_elements", r'''<?php
// LeetCode 3834 - Merge Adjacent Equal Elements
// https://leetcode.com/problems/merge-adjacent-equal-elements/

class Solution {
    function mergeAdjacent($nums) {
        $stk = [];
        foreach ($nums as $x) {
            $stk[] = $x;
            while (count($stk) > 1 && $stk[count($stk) - 1] === $stk[count($stk) - 2]) {
                $a = array_pop($stk);
                $b = array_pop($stk);
                $stk[] = $a + $b;
            }
        }
        return $stk;
    }
}
''')

add("3835_count_subarrays_with_cost_less_than_or_equal_to_k", r'''<?php
// LeetCode 3835 - Count Subarrays With Cost Less Than or Equal to K
// https://leetcode.com/problems/count-subarrays-with-cost-less-than-or-equal-to-k/

class Solution {
    function countSubarrays($nums, $k) {
        $ans = 0;
        $q1 = [];
        $q2 = [];
        $l = 0;
        $n = count($nums);
        for ($r = 0; $r < $n; $r++) {
            $x = $nums[$r];
            while (count($q1) && $nums[$q1[count($q1) - 1]] <= $x) array_pop($q1);
            while (count($q2) && $nums[$q2[count($q2) - 1]] >= $x) array_pop($q2);
            $q1[] = $r;
            $q2[] = $r;
            while ($l < $r && ($nums[$q1[0]] - $nums[$q2[0]]) * ($r - $l + 1) > $k) {
                $l++;
                if ($q1[0] < $l) array_shift($q1);
                if ($q2[0] < $l) array_shift($q2);
            }
            $ans += $r - $l + 1;
        }
        return $ans;
    }
}
''')

add("3836_maximum_score_using_exactly_k_pairs", r'''<?php
// LeetCode 3836 - Maximum Score Using Exactly K Pairs
// https://leetcode.com/problems/maximum-score-using-exactly-k-pairs/

class Solution {
    function maxScore($nums1, $nums2, $K) {
        $n = count($nums1);
        $m = count($nums2);
        $NEG = PHP_INT_MIN / 4;
        $f = [];
        for ($i = 0; $i <= $n; $i++) {
            $f[$i] = [];
            for ($j = 0; $j <= $m; $j++) $f[$i][$j] = array_fill(0, $K + 1, $NEG);
        }
        $f[0][0][0] = 0;
        for ($i = 0; $i <= $n; $i++) {
            for ($j = 0; $j <= $m; $j++) {
                for ($k = 0; $k <= $K; $k++) {
                    if ($i > 0) $f[$i][$j][$k] = max($f[$i][$j][$k], $f[$i - 1][$j][$k]);
                    if ($j > 0) $f[$i][$j][$k] = max($f[$i][$j][$k], $f[$i][$j - 1][$k]);
                    if ($i > 0 && $j > 0 && $k > 0) {
                        $f[$i][$j][$k] = max($f[$i][$j][$k], $f[$i - 1][$j - 1][$k - 1] + $nums1[$i - 1] * $nums2[$j - 1]);
                    }
                }
            }
        }
        return $f[$n][$m][$K];
    }
}
''')

add("3837_delayed_count_of_equal_elements", r'''<?php
// LeetCode 3837 - Delayed Count of Equal Elements
// https://leetcode.com/problems/delayed-count-of-equal-elements/

class Solution {
    function delayedCount($nums, $k) {
        $n = count($nums);
        $cnt = [];
        $ans = array_fill(0, $n, 0);
        for ($i = $n - $k - 2; $i >= 0; $i--) {
            $key = $nums[$i + $k + 1];
            $cnt[$key] = ($cnt[$key] ?? 0) + 1;
            $ans[$i] = $cnt[$nums[$i]] ?? 0;
        }
        return $ans;
    }
}
''')

add("3838_weighted_word_mapping", r'''<?php
// LeetCode 3838 - Weighted Word Mapping
// https://leetcode.com/problems/weighted-word-mapping/

class Solution {
    function mapWordWeights($words, $weights) {
        $ans = '';
        foreach ($words as $w) {
            $s = 0;
            $len = strlen($w);
            for ($i = 0; $i < $len; $i++) $s = ($s + $weights[ord($w[$i]) - 97]) % 26;
            $ans .= chr(97 + (25 - $s));
        }
        return $ans;
    }
}
''')

add("3839_number_of_prefix_connected_groups", r'''<?php
// LeetCode 3839 - Number of Prefix Connected Groups
// https://leetcode.com/problems/number-of-prefix-connected-groups/

class Solution {
    function prefixConnected($words, $k) {
        $cnt = [];
        foreach ($words as $w) {
            if (strlen($w) >= $k) {
                $p = substr($w, 0, $k);
                $cnt[$p] = ($cnt[$p] ?? 0) + 1;
            }
        }
        $ans = 0;
        foreach ($cnt as $v) if ($v > 1) $ans++;
        return $ans;
    }
}
''')

add("3840_house_robber_v", r'''<?php
// LeetCode 3840 - House Robber V
// https://leetcode.com/problems/house-robber-v/

class Solution {
    function rob($nums, $colors) {
        $n = count($nums);
        $f = 0;
        $g = $nums[0];
        for ($i = 1; $i < $n; $i++) {
            if ($colors[$i - 1] === $colors[$i]) {
                $nf = max($f, $g);
                $g = $f + $nums[$i];
                $f = $nf;
            } else {
                $nf = max($f, $g);
                $g = $nf + $nums[$i];
                $f = $nf;
            }
        }
        return max($f, $g);
    }
}
''')

add("3841_palindromic_path_queries_in_a_tree", r'''<?php
// LeetCode 3841 - Palindromic Path Queries in a Tree
// https://leetcode.com/problems/palindromic-path-queries-in-a-tree/

class Solution {
    public $bit;
    public $n;
    public $parent;
    public $depth;
    public $head;
    public $position;
    function update($index, $value) {
        for ($index++; $index <= $this->n; $index += $index & -$index) $this->bit[$index] ^= $value;
    }
    function prefix($index) {
        $result = 0;
        for (; $index > 0; $index -= $index & -$index) $result ^= $this->bit[$index];
        return $result;
    }
    function pathMask($u, $v) {
        $result = 0;
        while ($this->head[$u] !== $this->head[$v]) {
            if ($this->depth[$this->head[$u]] < $this->depth[$this->head[$v]]) { $tmp = $u; $u = $v; $v = $tmp; }
            $result ^= $this->prefix($this->position[$u] + 1) ^ $this->prefix($this->position[$this->head[$u]]);
            $u = $this->parent[$this->head[$u]];
        }
        if ($this->position[$u] > $this->position[$v]) { $tmp = $u; $u = $v; $v = $tmp; }
        return $result ^ $this->prefix($this->position[$v] + 1) ^ $this->prefix($this->position[$u]);
    }
    function palindromicPathQueries($n, $edges, $s, $queries) {
        $this->n = $n;
        $graph = [];
        for ($i = 0; $i < $n; $i++) $graph[$i] = [];
        foreach ($edges as $edge) {
            $graph[$edge[0]][] = $edge[1];
            $graph[$edge[1]][] = $edge[0];
        }
        $parent = array_fill(0, $n, -2);
        $depth = array_fill(0, $n, 0);
        $parent[0] = -1;
        $order = [0];
        for ($i = 0; $i < count($order); $i++) {
            $u = $order[$i];
            foreach ($graph[$u] as $v) {
                if ($parent[$v] === -2) {
                    $parent[$v] = $u;
                    $depth[$v] = $depth[$u] + 1;
                    $order[] = $v;
                }
            }
        }
        $size = array_fill(0, $n, 0);
        $heavy = array_fill(0, $n, -1);
        for ($i = $n - 1; $i >= 0; $i--) {
            $u = $order[$i];
            $size[$u] = 1;
            foreach ($graph[$u] as $v) {
                if ($parent[$v] === $u) {
                    $size[$u] += $size[$v];
                    if ($heavy[$u] === -1 || $size[$v] > $size[$heavy[$u]]) $heavy[$u] = $v;
                }
            }
        }
        $head = array_fill(0, $n, 0);
        $position = array_fill(0, $n, 0);
        $stack = [[0, 0]];
        $nextPosition = 0;
        while (count($stack)) {
            $chain = array_pop($stack);
            for ($u = $chain[0]; $u !== -1; $u = $heavy[$u]) {
                $head[$u] = $chain[1];
                $position[$u] = $nextPosition++;
                foreach ($graph[$u] as $v) {
                    if ($parent[$v] === $u && $v !== $heavy[$u]) $stack[] = [$v, $v];
                }
            }
        }
        $this->parent = $parent;
        $this->depth = $depth;
        $this->head = $head;
        $this->position = $position;
        $this->bit = array_fill(0, $n + 1, 0);
        $current = [];
        for ($i = 0; $i < $n; $i++) $current[] = $s[$i];
        for ($node = 0; $node < $n; $node++) $this->update($position[$node], 1 << (ord($current[$node]) - 97));
        $answer = [];
        foreach ($queries as $query) {
            $parts = explode(' ', $query);
            $op = $parts[0];
            $node = intval($parts[1]);
            if ($op === 'update') {
                $newCharacter = $parts[2][0];
                $delta = (1 << (ord($current[$node]) - 97)) ^ (1 << (ord($newCharacter) - 97));
                $this->update($position[$node], $delta);
                $current[$node] = $newCharacter;
            } else {
                $other = intval($parts[2]);
                $mask = $this->pathMask($node, $other);
                $answer[] = (($mask & ($mask - 1)) === 0);
            }
        }
        return $answer;
    }
}
''')

add("3842_toggle_light_bulbs", r'''<?php
// LeetCode 3842 - Toggle Light Bulbs
// https://leetcode.com/problems/toggle-light-bulbs/

class Solution {
    function toggleLightBulbs($bulbs) {
        $st = array_fill(0, 101, 0);
        foreach ($bulbs as $x) $st[$x] ^= 1;
        $ans = [];
        for ($i = 0; $i < 101; $i++) if ($st[$i] === 1) $ans[] = $i;
        return $ans;
    }
}
''')

add("3843_first_element_with_unique_frequency", r'''<?php
// LeetCode 3843 - First Element With Unique Frequency
// https://leetcode.com/problems/first-element-with-unique-frequency/

class Solution {
    function firstUniqueFreq($nums) {
        $cnt = [];
        foreach ($nums as $x) $cnt[$x] = ($cnt[$x] ?? 0) + 1;
        $freq = [];
        foreach ($cnt as $v) $freq[$v] = ($freq[$v] ?? 0) + 1;
        foreach ($nums as $x) {
            if ($freq[$cnt[$x]] === 1) return $x;
        }
        return -1;
    }
}
''')

add("3844_longest_almost_palindromic_substring", r'''<?php
// LeetCode 3844 - Longest Almost Palindromic Substring
// https://leetcode.com/problems/longest-almost-palindromic-substring/

class Solution {
    function expand($s, $l, $r) {
        $n = strlen($s);
        while ($l >= 0 && $r < $n && $s[$l] === $s[$r]) { $l--; $r++; }
        $l1 = $l - 1;
        $r1 = $r;
        $l2 = $l;
        $r2 = $r + 1;
        while ($l1 >= 0 && $r1 < $n && $s[$l1] === $s[$r1]) { $l1--; $r1++; }
        while ($l2 >= 0 && $r2 < $n && $s[$l2] === $s[$r2]) { $l2--; $r2++; }
        return min($n, max($r1 - $l1 - 1, $r2 - $l2 - 1));
    }
    function almostPalindromic($s) {
        $n = strlen($s);
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            $ans = max($ans, max($this->expand($s, $i, $i), $this->expand($s, $i, $i + 1)));
        }
        return $ans;
    }
}
''')

add("3845_maximum_subarray_xor_with_bounded_range", r'''<?php
// LeetCode 3845 - Maximum Subarray XOR with Bounded Range
// https://leetcode.com/problems/maximum-subarray-xor-with-bounded-range/

class Solution {
    public $nodes;
    function add($x, $delta) {
        $u = 0;
        $this->nodes[$u]['count'] += $delta;
        for ($b = 15; $b >= 0; $b--) {
            $bit = ($x >> $b) & 1;
            if ($this->nodes[$u]['next'][$bit] === 0) {
                $this->nodes[$u]['next'][$bit] = count($this->nodes);
                $this->nodes[] = ['next' => [0, 0], 'count' => 0];
            }
            $u = $this->nodes[$u]['next'][$bit];
            $this->nodes[$u]['count'] += $delta;
        }
    }
    function query($x) {
        $u = 0;
        $res = 0;
        for ($b = 15; $b >= 0; $b--) {
            $bit = ($x >> $b) & 1;
            $want = $bit ^ 1;
            $v = $this->nodes[$u]['next'][$want];
            if ($v !== 0 && $this->nodes[$v]['count'] > 0) {
                $res |= 1 << $b;
                $u = $v;
            } else {
                $u = $this->nodes[$u]['next'][$bit];
            }
        }
        return $res;
    }
    function maxSubarrayXor($nums, $k) {
        $this->nodes = [['next' => [0, 0], 'count' => 0]];
        $n = count($nums);
        $pref = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; $i++) $pref[$i + 1] = $pref[$i] ^ $nums[$i];
        $maxQ = [];
        $minQ = [];
        $left = 0;
        $trieLeft = 0;
        $ans = 0;
        for ($r = 0; $r < $n; $r++) {
            $x = $nums[$r];
            while (count($maxQ) && $nums[$maxQ[count($maxQ) - 1]] <= $x) array_pop($maxQ);
            $maxQ[] = $r;
            while (count($minQ) && $nums[$minQ[count($minQ) - 1]] >= $x) array_pop($minQ);
            $minQ[] = $r;
            while ($nums[$maxQ[0]] - $nums[$minQ[0]] > $k) {
                if ($maxQ[0] === $left) array_shift($maxQ);
                if ($minQ[0] === $left) array_shift($minQ);
                $left++;
            }
            $this->add($pref[$r], 1);
            while ($trieLeft < $left) {
                $this->add($pref[$trieLeft], -1);
                $trieLeft++;
            }
            $cur = $this->query($pref[$r + 1]);
            if ($cur > $ans) $ans = $cur;
        }
        return $ans;
    }
}
''')

add("3846_total_distance_to_type_a_string_using_one_finger", r'''<?php
// LeetCode 3846 - Total Distance to Type a String Using One Finger
// https://leetcode.com/problems/total-distance-to-type-a-string-using-one-finger/

class Solution {
    function totalDistance($s) {
        $pos = [];
        $keys = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm'];
        for ($i = 0; $i < 3; $i++) {
            $len = strlen($keys[$i]);
            for ($j = 0; $j < $len; $j++) $pos[$keys[$i][$j]] = [$i, $j];
        }
        $pre = 'a';
        $ans = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $cur = $s[$i];
            $p1 = $pos[$pre];
            $p2 = $pos[$cur];
            $ans += abs($p1[0] - $p2[0]) + abs($p1[1] - $p2[1]);
            $pre = $cur;
        }
        return $ans;
    }
}
''')

add("3847_find_the_score_difference_in_a_game", r'''<?php
// LeetCode 3847 - Find the Score Difference in a Game
// https://leetcode.com/problems/find-the-score-difference-in-a-game/

class Solution {
    function scoreDifference($nums) {
        $ans = 0;
        $k = 1;
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            if ($nums[$i] % 2 !== 0) $k = -$k;
            if ($i % 6 === 5) $k = -$k;
            $ans += $k * $nums[$i];
        }
        return $ans;
    }
}
''')

add("3848_check_digitorial_permutation", r'''<?php
// LeetCode 3848 - Check Digitorial Permutation
// https://leetcode.com/problems/check-digitorial-permutation/

class Solution {
    function isDigitorialPermutation($n) {
        $f = array_fill(0, 10, 0);
        $f[0] = 1;
        for ($i = 1; $i < 10; $i++) $f[$i] = $f[$i - 1] * $i;
        $x = 0;
        $y = $n;
        while ($y > 0) {
            $x += $f[$y % 10];
            $y = intdiv($y, 10);
        }
        $a = str_split(strval($x));
        sort($a);
        $b = str_split(strval($n));
        sort($b);
        return implode('', $a) === implode('', $b);
    }
}
''')

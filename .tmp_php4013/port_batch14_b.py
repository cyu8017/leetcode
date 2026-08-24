#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
SOLUTIONS = {}

def add(folder, body):
    SOLUTIONS[folder] = body if body.endswith("\n") else body + "\n"

MINHEAP = r'''
class MinHeap {
    public $a = [];
    public $cmp;
    function __construct($cmp = null) {
        $this->cmp = $cmp;
    }
    function _up($i) {
        $a = &$this->a;
        $cmp = $this->cmp;
        while ($i > 0) {
            $p = ($i - 1) >> 1;
            $c = $cmp ? $cmp($a[$i], $a[$p]) : ($a[$i] <=> $a[$p]);
            if ($c >= 0) break;
            $t = $a[$i]; $a[$i] = $a[$p]; $a[$p] = $t;
            $i = $p;
        }
    }
    function _down($i) {
        $a = &$this->a;
        $cmp = $this->cmp;
        $n = count($a);
        while (true) {
            $s = $i; $l = $i * 2 + 1; $r = $l + 1;
            if ($l < $n) {
                $c = $cmp ? $cmp($a[$l], $a[$s]) : ($a[$l] <=> $a[$s]);
                if ($c < 0) $s = $l;
            }
            if ($r < $n) {
                $c = $cmp ? $cmp($a[$r], $a[$s]) : ($a[$r] <=> $a[$s]);
                if ($c < 0) $s = $r;
            }
            if ($s === $i) break;
            $t = $a[$i]; $a[$i] = $a[$s]; $a[$s] = $t;
            $i = $s;
        }
    }
    function push($x) { $this->a[] = $x; $this->_up(count($this->a) - 1); }
    function pop() {
        $a = &$this->a;
        if (!$a) return null;
        $top = $a[0];
        $last = array_pop($a);
        if ($a) { $a[0] = $last; $this->_down(0); }
        return $top;
    }
    function peek() { return $this->a[0]; }
    function size() { return count($this->a); }
}
'''

BIT = r'''
class BIT {
    public $n;
    public $c;
    function __construct($n) {
        $this->n = $n;
        $this->c = array_fill(0, $n + 1, 0);
    }
    function update($x, $delta) {
        for (; $x <= $this->n; $x += $x & -$x) $this->c[$x] += $delta;
    }
    function query($x) {
        $s = 0;
        for (; $x > 0; $x -= $x & -$x) $s += $this->c[$x];
        return $s;
    }
}
'''

add("3088_make_string_anti_palindrome", r'''<?php
// LeetCode 3088 - Make String Anti-palindrome
// https://leetcode.com/problems/make-string-anti-palindrome/

class Solution {
    function makeAntiPalindrome($s) {
        $arr = str_split($s);
        sort($arr);
        $n = count($arr);
        $m = intdiv($n, 2);
        if ($arr[$m] === $arr[$m - 1]) {
            $i = $m;
            while ($i < $n && $arr[$i] === $arr[$i - 1]) $i++;
            for ($j = $m; $j < $n && $arr[$j] === $arr[$n - $j - 1]; $i++, $j++) {
                if ($i >= $n) return "-1";
                $tmp = $arr[$i]; $arr[$i] = $arr[$j]; $arr[$j] = $tmp;
            }
        }
        return implode("", $arr);
    }
}
''')

add("3090_maximum_length_substring_with_two_occurrences", r'''<?php
// LeetCode 3090 - Maximum Length Substring With Two Occurrences
// https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/

class Solution {
    function maximumLengthSubstring($s) {
        $l = 0;
        $ans = 0;
        $cnt = array_fill(0, 26, 0);
        $n = strlen($s);
        for ($r = 0; $r < $n; $r++) {
            $idx = ord($s[$r]) - 97;
            $cnt[$idx]++;
            while ($cnt[$idx] > 2) {
                $cnt[ord($s[$l]) - 97]--;
                $l++;
            }
            $ans = max($ans, $r - $l + 1);
        }
        return $ans;
    }
}
''')

add("3091_apply_operations_to_make_sum_of_array_greater_than_or_equal_to_k", r'''<?php
// LeetCode 3091 - Apply Operations to Make Sum of Array Greater Than or Equal to k
// https://leetcode.com/problems/apply-operations-to-make-sum-of-array-greater-than-or-equal-to-k/

class Solution {
    function minOperations($k) {
        $ans = $k;
        for ($a = 0; $a < $k; $a++) {
            $x = $a + 1;
            $b = intdiv($k + $x - 1, $x) - 1;
            $ans = min($ans, $a + $b);
        }
        return $ans;
    }
}
''')

add("3092_most_frequent_ids", '''<?php
// LeetCode 3092 - Most Frequent IDs
// https://leetcode.com/problems/most-frequent-ids/
''' + MINHEAP + r'''
class Solution {
    function mostFrequentIDs($nums, $freq) {
        $n = count($nums);
        $cnt = [];
        $lazy = [];
        $ans = array_fill(0, $n, 0);
        $pq = new MinHeap(function ($a, $b) { return $b <=> $a; });
        for ($i = 0; $i < $n; $i++) {
            $x = $nums[$i];
            $f = $freq[$i];
            $old = $cnt[$x] ?? 0;
            $lazy[$old] = ($lazy[$old] ?? 0) + 1;
            $neu = $old + $f;
            $cnt[$x] = $neu;
            $pq->push($neu);
            while ($pq->size() && ($lazy[$pq->peek()] ?? 0) > 0) {
                $top = $pq->pop();
                $lazy[$top]--;
            }
            $ans[$i] = $pq->size() ? $pq->peek() : 0;
        }
        return $ans;
    }
}
''')

add("3093_longest_common_suffix_queries", r'''<?php
// LeetCode 3093 - Longest Common Suffix Queries
// https://leetcode.com/problems/longest-common-suffix-queries/

class Trie {
    public $children;
    public $length;
    public $idx;
    function __construct() {
        $this->children = array_fill(0, 26, null);
        $this->length = 1 << 30;
        $this->idx = 1 << 30;
    }
}

class Solution {
    function stringIndices($wordsContainer, $wordsQuery) {
        $trie = new Trie();
        for ($i = 0; $i < count($wordsContainer); $i++) $this->insert($trie, $wordsContainer[$i], $i);
        $ans = [];
        for ($i = 0; $i < count($wordsQuery); $i++) $ans[$i] = $this->query($trie, $wordsQuery[$i]);
        return $ans;
    }
    function insert($t, $w, $i) {
        $node = $t;
        $len = strlen($w);
        if ($node->length > $len) {
            $node->length = $len;
            $node->idx = $i;
        }
        for ($k = $len - 1; $k >= 0; $k--) {
            $id = ord($w[$k]) - 97;
            if ($node->children[$id] === null) $node->children[$id] = new Trie();
            $node = $node->children[$id];
            if ($node->length > $len) {
                $node->length = $len;
                $node->idx = $i;
            }
        }
    }
    function query($t, $w) {
        $node = $t;
        for ($k = strlen($w) - 1; $k >= 0; $k--) {
            $id = ord($w[$k]) - 97;
            if ($node->children[$id] === null) break;
            $node = $node->children[$id];
        }
        return $node->idx;
    }
}
''')

add("3094_guess_the_number_using_bitwise_questions_ii", r'''<?php
// LeetCode 3094 - Guess the Number Using Bitwise Questions II
// https://leetcode.com/problems/guess-the-number-using-bitwise-questions-ii/

function commonBits($num) {
    global $hiddenNumber;
    $hiddenNumber ^= $num;
    return substr_count(decbin($hiddenNumber), "1");
}

class Solution {
    function findNumber() {
        $n = 0;
        for ($i = 0; $i < 32; $i++) {
            $count1 = commonBits(1 << $i);
            $count2 = commonBits(1 << $i);
            if ($count1 > $count2) $n |= 1 << $i;
        }
        return $n;
    }
}
''')

add("3095_shortest_subarray_with_or_at_least_k_i", r'''<?php
// LeetCode 3095 - Shortest Subarray With OR at Least K I
// https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-i/

class Solution {
    function minimumSubarrayLength($nums, $k) {
        $n = count($nums);
        $cnt = array_fill(0, 32, 0);
        $ans = $n + 1;
        $s = 0;
        $i = 0;
        for ($j = 0; $j < $n; $j++) {
            $x = $nums[$j];
            $s |= $x;
            for ($h = 0; $h < 32; $h++)
                if ((($x >> $h) & 1) !== 0) $cnt[$h]++;
            for (; $s >= $k && $i <= $j; $i++) {
                $ans = min($ans, $j - $i + 1);
                for ($h = 0; $h < 32; $h++) {
                    if ((($nums[$i] >> $h) & 1) !== 0) {
                        $cnt[$h]--;
                        if ($cnt[$h] === 0) $s ^= 1 << $h;
                    }
                }
            }
        }
        return $ans === $n + 1 ? -1 : $ans;
    }
}
''')

add("3096_minimum_levels_to_gain_more_points", r'''<?php
// LeetCode 3096 - Minimum Levels to Gain More Points
// https://leetcode.com/problems/minimum-levels-to-gain-more-points/

class Solution {
    function minimumLevels($possible) {
        $s = 0;
        foreach ($possible as $x) $s += ($x === 0 ? -1 : $x);
        $t = 0;
        $n = count($possible);
        for ($i = 0; $i + 1 < $n; $i++) {
            $x = $possible[$i] === 0 ? -1 : $possible[$i];
            $t += $x;
            if ($t > $s - $t) return $i + 1;
        }
        return -1;
    }
}
''')

add("3097_shortest_subarray_with_or_at_least_k_ii", r'''<?php
// LeetCode 3097 - Shortest Subarray With OR at Least K II
// https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-ii/

class Solution {
    function minimumSubarrayLength($nums, $k) {
        $n = count($nums);
        $cnt = array_fill(0, 32, 0);
        $ans = $n + 1;
        $s = 0;
        $i = 0;
        for ($j = 0; $j < $n; $j++) {
            $x = $nums[$j];
            $s |= $x;
            for ($h = 0; $h < 32; $h++)
                if ((($x >> $h) & 1) !== 0) $cnt[$h]++;
            for (; $s >= $k && $i <= $j; $i++) {
                $ans = min($ans, $j - $i + 1);
                for ($h = 0; $h < 32; $h++) {
                    if ((($nums[$i] >> $h) & 1) !== 0) {
                        $cnt[$h]--;
                        if ($cnt[$h] === 0) $s ^= 1 << $h;
                    }
                }
            }
        }
        return $ans === $n + 1 ? -1 : $ans;
    }
}
''')

add("3098_find_the_sum_of_subsequence_powers", r'''<?php
// LeetCode 3098 - Find the Sum of Subsequence Powers
// https://leetcode.com/problems/find-the-sum-of-subsequence-powers/

class Solution {
    public $nums;
    public $n;
    public $f = [];
    function sumOfPowers($nums, $k) {
        sort($nums);
        $this->nums = $nums;
        $this->n = count($nums);
        $this->f = [];
        return $this->dfs(0, $this->n, $k, PHP_INT_MAX);
    }
    function dfs($i, $j, $kk, $mi) {
        $MOD = 1000000007;
        if ($i >= $this->n) return $kk === 0 ? $mi : 0;
        if ($this->n - $i < $kk) return 0;
        $key = $mi . "," . $i . "," . $j . "," . $kk;
        if (isset($this->f[$key])) return $this->f[$key];
        $ans = $this->dfs($i + 1, $j, $kk, $mi);
        if ($j === $this->n) $ans = ($ans + $this->dfs($i + 1, $i, $kk - 1, $mi)) % $MOD;
        else $ans = ($ans + $this->dfs($i + 1, $i, $kk - 1, min($mi, $this->nums[$i] - $this->nums[$j]))) % $MOD;
        $this->f[$key] = $ans;
        return $ans;
    }
}
''')

add("3099_harshad_number", r'''<?php
// LeetCode 3099 - Harshad Number
// https://leetcode.com/problems/harshad-number/

class Solution {
    function sumOfTheDigitsOfHarshadNumber($x) {
        $s = 0;
        for ($y = $x; $y > 0; $y = intdiv($y, 10)) $s += $y % 10;
        return $x % $s === 0 ? $s : -1;
    }
}
''')

add("3100_water_bottles_ii", r'''<?php
// LeetCode 3100 - Water Bottles II
// https://leetcode.com/problems/water-bottles-ii/

class Solution {
    function maxBottlesDrunk($numBottles, $numExchange) {
        $ans = $numBottles;
        while ($numBottles >= $numExchange) {
            $numBottles -= $numExchange;
            $numExchange++;
            $ans++;
            $numBottles++;
        }
        return $ans;
    }
}
''')

add("3101_count_alternating_subarrays", r'''<?php
// LeetCode 3101 - Count Alternating Subarrays
// https://leetcode.com/problems/count-alternating-subarrays/

class Solution {
    function countAlternatingSubarrays($nums) {
        $ans = 1;
        $s = 1;
        $n = count($nums);
        for ($i = 1; $i < $n; $i++) {
            if ($nums[$i] !== $nums[$i - 1]) $s++;
            else $s = 1;
            $ans += $s;
        }
        return $ans;
    }
}
''')

add("3102_minimize_manhattan_distances", r'''<?php
// LeetCode 3102 - Minimize Manhattan Distances
// https://leetcode.com/problems/minimize-manhattan-distances/

class MultiSet {
    public $m = [];
    public $keys = [];
    function merge($x, $v) {
        $nv = ($this->m[$x] ?? 0) + $v;
        if ($nv === 0) {
            unset($this->m[$x]);
            $i = array_search($x, $this->keys, true);
            if ($i !== false) array_splice($this->keys, $i, 1);
        } else {
            if (!isset($this->m[$x])) {
                $lo = 0;
                $hi = count($this->keys);
                while ($lo < $hi) {
                    $mid = ($lo + $hi) >> 1;
                    if ($this->keys[$mid] < $x) $lo = $mid + 1;
                    else $hi = $mid;
                }
                array_splice($this->keys, $lo, 0, [$x]);
            }
            $this->m[$x] = $nv;
        }
    }
    function first() { return $this->keys[0]; }
    function last() { return $this->keys[count($this->keys) - 1]; }
}

class Solution {
    function minimumDistance($points) {
        $st1 = new MultiSet();
        $st2 = new MultiSet();
        foreach ($points as $p) {
            $st1->merge($p[0] + $p[1], 1);
            $st2->merge($p[0] - $p[1], 1);
        }
        $ans = PHP_INT_MAX;
        foreach ($points as $p) {
            $x = $p[0];
            $y = $p[1];
            $st1->merge($x + $y, -1);
            $st2->merge($x - $y, -1);
            $ans = min($ans, max($st1->last() - $st1->first(), $st2->last() - $st2->first()));
            $st1->merge($x + $y, 1);
            $st2->merge($x - $y, 1);
        }
        return $ans;
    }
}
''')

add("3104_find_longest_self_contained_substring", r'''<?php
// LeetCode 3104 - Find Longest Self-Contained Substring
// https://leetcode.com/problems/find-longest-self-contained-substring/

class Solution {
    function maxSubstringLength($s) {
        $first = array_fill(0, 26, -1);
        $last = array_fill(0, 26, 0);
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $j = ord($s[$i]) - 97;
            if ($first[$j] === -1) $first[$j] = $i;
            $last[$j] = $i;
        }
        $ans = -1;
        for ($k = 0; $k < 26; $k++) {
            $i = $first[$k];
            if ($i === -1) continue;
            $mx = $last[$k];
            for ($j = $i; $j < $n; $j++) {
                $a = $first[ord($s[$j]) - 97];
                $b = $last[ord($s[$j]) - 97];
                if ($a < $i) break;
                $mx = max($mx, $b);
                if ($mx === $j && $j - $i + 1 < $n) $ans = max($ans, $j - $i + 1);
            }
        }
        return $ans;
    }
}
''')

add("3105_longest_strictly_increasing_or_strictly_decreasing_subarray", r'''<?php
// LeetCode 3105 - Longest Strictly Increasing or Strictly Decreasing Subarray
// https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/

class Solution {
    function longestMonotonicSubarray($nums) {
        $ans = 1;
        $t = 1;
        $n = count($nums);
        for ($i = 1; $i < $n; $i++) {
            if ($nums[$i - 1] < $nums[$i]) {
                $t++;
                $ans = max($ans, $t);
            } else $t = 1;
        }
        $t = 1;
        for ($i = 1; $i < $n; $i++) {
            if ($nums[$i - 1] > $nums[$i]) {
                $t++;
                $ans = max($ans, $t);
            } else $t = 1;
        }
        return $ans;
    }
}
''')

add("3106_lexicographically_smallest_string_after_operations_with_constraint", r'''<?php
// LeetCode 3106 - Lexicographically Smallest String After Operations With Constraint
// https://leetcode.com/problems/lexicographically-smallest-string-after-operations-with-constraint/

class Solution {
    function getSmallestString($s, $k) {
        $arr = str_split($s);
        $n = count($arr);
        for ($i = 0; $i < $n; $i++) {
            $c1 = ord($arr[$i]);
            for ($c2 = 97; $c2 < $c1; $c2++) {
                $d = min($c1 - $c2, 26 - ($c1 - $c2));
                if ($d <= $k) {
                    $arr[$i] = chr($c2);
                    $k -= $d;
                    break;
                }
            }
        }
        return implode("", $arr);
    }
}
''')

add("3107_minimum_operations_to_make_median_of_array_equal_to_k", r'''<?php
// LeetCode 3107 - Minimum Operations to Make Median of Array Equal to K
// https://leetcode.com/problems/minimum-operations-to-make-median-of-array-equal-to-k/

class Solution {
    function minOperationsToMakeMedianK($nums, $k) {
        sort($nums);
        $n = count($nums);
        $m = $n >> 1;
        $ans = abs($nums[$m] - $k);
        if ($nums[$m] > $k) {
            for ($i = $m - 1; $i >= 0 && $nums[$i] > $k; $i--) $ans += $nums[$i] - $k;
        } else {
            for ($i = $m + 1; $i < $n && $nums[$i] < $k; $i++) $ans += $k - $nums[$i];
        }
        return $ans;
    }
}
''')

add("3108_minimum_cost_walk_in_weighted_graph", r'''<?php
// LeetCode 3108 - Minimum Cost Walk in Weighted Graph
// https://leetcode.com/problems/minimum-cost-walk-in-weighted-graph/

class Solution {
    public $p;
    public $size;
    function minimumCost($n, $edges, $query) {
        $this->p = range(0, $n - 1);
        $this->size = array_fill(0, $n, 1);
        $g = array_fill(0, $n, -1);
        foreach ($edges as $e) $this->unite($e[0], $e[1]);
        foreach ($edges as $e) {
            $root = $this->find($e[0]);
            $g[$root] &= $e[2];
        }
        $ans = [];
        for ($i = 0; $i < count($query); $i++) {
            $u = $query[$i][0];
            $v = $query[$i][1];
            if ($u === $v) $ans[$i] = 0;
            else {
                $a = $this->find($u);
                $b = $this->find($v);
                $ans[$i] = $a === $b ? $g[$a] : -1;
            }
        }
        return $ans;
    }
    function find($x) {
        if ($this->p[$x] !== $x) $this->p[$x] = $this->find($this->p[$x]);
        return $this->p[$x];
    }
    function unite($a, $b) {
        $pa = $this->find($a);
        $pb = $this->find($b);
        if ($pa === $pb) return;
        if ($this->size[$pa] > $this->size[$pb]) {
            $this->p[$pb] = $pa;
            $this->size[$pa] += $this->size[$pb];
        } else {
            $this->p[$pa] = $pb;
            $this->size[$pb] += $this->size[$pa];
        }
    }
}
''')

add("3109_find_the_index_of_permutation", '''<?php
// LeetCode 3109 - Find the Index of Permutation
// https://leetcode.com/problems/find-the-index-of-permutation/
''' + BIT + r'''
class Solution {
    function getPermutationIndex($perm) {
        $MOD = 1000000007;
        $n = count($perm);
        $tree = new BIT($n + 1);
        $f = array_fill(0, $n, 0);
        $f[0] = 1;
        for ($i = 1; $i < $n; $i++) $f[$i] = $f[$i - 1] * $i % $MOD;
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            $x = $perm[$i];
            $cnt = $x - 1 - $tree->query($x);
            $ans = ($ans + $cnt * $f[$n - 1 - $i]) % $MOD;
            $tree->update($x, 1);
        }
        return $ans;
    }
}
''')

add("3110_score_of_a_string", r'''<?php
// LeetCode 3110 - Score of a String
// https://leetcode.com/problems/score-of-a-string/

class Solution {
    function scoreOfString($s) {
        $ans = 0;
        $n = strlen($s);
        for ($i = 1; $i < $n; $i++)
            $ans += abs(ord($s[$i - 1]) - ord($s[$i]));
        return $ans;
    }
}
''')

add("3111_minimum_rectangles_to_cover_points", r'''<?php
// LeetCode 3111 - Minimum Rectangles to Cover Points
// https://leetcode.com/problems/minimum-rectangles-to-cover-points/

class Solution {
    function minRectanglesToCoverPoints($points, $w) {
        usort($points, function ($a, $b) { return $a[0] <=> $b[0]; });
        $ans = 0;
        $x1 = -1;
        foreach ($points as $p) {
            if ($p[0] > $x1) {
                $ans++;
                $x1 = $p[0] + $w;
            }
        }
        return $ans;
    }
}
''')

add("3112_minimum_time_to_visit_disappearing_nodes", '''<?php
// LeetCode 3112 - Minimum Time to Visit Disappearing Nodes
// https://leetcode.com/problems/minimum-time-to-visit-disappearing-nodes/
''' + MINHEAP + r'''
class Solution {
    function minimumTime($n, $edges, $disappear) {
        $g = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $g[$e[0]][] = [$e[1], $e[2]];
            $g[$e[1]][] = [$e[0], $e[2]];
        }
        $INF = 1 << 30;
        $dist = array_fill(0, $n, $INF);
        $dist[0] = 0;
        $pq = new MinHeap(function ($a, $b) { return $a[0] <=> $b[0]; });
        $pq->push([0, 0]);
        while ($pq->size()) {
            $cur = $pq->pop();
            $du = $cur[0];
            $u = $cur[1];
            if ($du > $dist[$u]) continue;
            foreach ($g[$u] as $e) {
                $v = $e[0];
                $w = $e[1];
                if ($dist[$v] > $dist[$u] + $w && $dist[$u] + $w < $disappear[$v]) {
                    $dist[$v] = $dist[$u] + $w;
                    $pq->push([$dist[$v], $v]);
                }
            }
        }
        $ans = array_fill(0, $n, 0);
        for ($i = 0; $i < $n; $i++)
            $ans[$i] = $dist[$i] < $disappear[$i] ? $dist[$i] : -1;
        return $ans;
    }
}
''')

add("3113_find_the_number_of_subarrays_where_boundary_elements_are_maximum", r'''<?php
// LeetCode 3113 - Find the Number of Subarrays Where Boundary Elements Are Maximum
// https://leetcode.com/problems/find-the-number-of-subarrays-where-boundary-elements-are-maximum/

class Solution {
    function numberOfSubarrays($nums) {
        $stk = [];
        $ans = 0;
        foreach ($nums as $x) {
            while ($stk && $stk[count($stk) - 1][0] < $x) array_pop($stk);
            if (!$stk || $stk[count($stk) - 1][0] > $x) $stk[] = [$x, 1];
            else $stk[count($stk) - 1][1]++;
            $ans += $stk[count($stk) - 1][1];
        }
        return $ans;
    }
}
''')

add("3114_latest_time_you_can_obtain_after_replacing_characters", r'''<?php
// LeetCode 3114 - Latest Time You Can Obtain After Replacing Characters
// https://leetcode.com/problems/latest-time-you-can-obtain-after-replacing-characters/

class Solution {
    function findLatestTime($s) {
        for ($h = 11; ; $h--) {
            for ($m = 59; $m >= 0; $m--) {
                $t = str_pad((string)$h, 2, "0", STR_PAD_LEFT) . ":" . str_pad((string)$m, 2, "0", STR_PAD_LEFT);
                $ok = true;
                for ($i = 0; $i < 5; $i++) {
                    if ($s[$i] !== "?" && $s[$i] !== $t[$i]) { $ok = false; break; }
                }
                if ($ok) return $t;
            }
        }
    }
}
''')

add("3115_maximum_prime_difference", r'''<?php
// LeetCode 3115 - Maximum Prime Difference
// https://leetcode.com/problems/maximum-prime-difference/

class Solution {
    function maximumPrimeDifference($nums) {
        for ($i = 0; ; $i++) {
            if ($this->isPrime($nums[$i])) {
                for ($j = count($nums) - 1; ; $j--) {
                    if ($this->isPrime($nums[$j])) return $j - $i;
                }
            }
        }
    }
    function isPrime($n) {
        if ($n < 2) return false;
        for ($i = 2; $i * $i <= $n; $i++) if ($n % $i === 0) return false;
        return true;
    }
}
''')

add("3116_kth_smallest_amount_with_single_denomination_combination", r'''<?php
// LeetCode 3116 - Kth Smallest Amount With Single Denomination Combination
// https://leetcode.com/problems/kth-smallest-amount-with-single-denomination-combination/

class Solution {
    public $coins;
    public $k;
    public $n;
    function findKthSmallest($coins, $k) {
        $this->coins = $coins;
        $this->k = $k;
        $this->n = count($coins);
        $lo = 1;
        $hi = 100000000000;
        while ($lo < $hi) {
            $mid = $lo + intdiv($hi - $lo, 2);
            if ($this->check($mid)) $hi = $mid;
            else $lo = $mid + 1;
        }
        return $lo;
    }
    function gcdll($a, $b) {
        while ($b !== 0) { $t = $a % $b; $a = $b; $b = $t; }
        return $a;
    }
    function lcmll($a, $b) {
        return intdiv($a, $this->gcdll($a, $b)) * $b;
    }
    function bitCount($x) {
        $c = 0;
        while ($x !== 0) { $c += $x & 1; $x >>= 1; }
        return $c;
    }
    function check($mx) {
        $cnt = 0;
        $n = $this->n;
        for ($i = 1; $i < (1 << $n); $i++) {
            $v = 1;
            for ($j = 0; $j < $n; $j++) {
                if ((($i >> $j) & 1) !== 0) {
                    $v = $this->lcmll($v, $this->coins[$j]);
                    if ($v > $mx) break;
                }
            }
            $m = $this->bitCount($i);
            if ($m % 2 === 1) $cnt += intdiv($mx, $v);
            else $cnt -= intdiv($mx, $v);
        }
        return $cnt >= $this->k;
    }
}
''')

add("3117_minimum_sum_of_values_by_dividing_array", r'''<?php
// LeetCode 3117 - Minimum Sum of Values by Dividing Array
// https://leetcode.com/problems/minimum-sum-of-values-by-dividing-array/

class Solution {
    public $nums;
    public $andValues;
    public $n;
    public $m;
    public $f = [];
    function minimumValueSum($nums, $andValues) {
        $this->nums = $nums;
        $this->andValues = $andValues;
        $this->n = count($nums);
        $this->m = count($andValues);
        $this->f = [];
        $ans = $this->dfs(0, 0, -1);
        return $ans < (1 << 29) ? $ans : -1;
    }
    function dfs($i, $j, $a) {
        $INF = 1 << 29;
        if ($this->n - $i < $this->m - $j) return $INF;
        if ($j === $this->m) return $i === $this->n ? 0 : $INF;
        $a &= $this->nums[$i];
        if ($a < $this->andValues[$j]) return $INF;
        $key = $i . "," . $j . "," . $a;
        if (isset($this->f[$key])) return $this->f[$key];
        $ans = $this->dfs($i + 1, $j, $a);
        if ($a === $this->andValues[$j]) {
            $ans = min($ans, $this->dfs($i + 1, $j + 1, -1) + $this->nums[$i]);
        }
        $this->f[$key] = $ans;
        return $ans;
    }
}
''')

add("3119_maximum_number_of_potholes_that_can_be_fixed", r'''<?php
// LeetCode 3119 - Maximum Number of Potholes That Can Be Fixed
// https://leetcode.com/problems/maximum-number-of-potholes-that-can-be-fixed/

class Solution {
    function maxPotholes($road, $budget) {
        $road = $road . ".";
        $n = strlen($road);
        $cnt = array_fill(0, $n, 0);
        $k = 0;
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            $c = $road[$i];
            if ($c === "x") $k++;
            else if ($k > 0) { $cnt[$k]++; $k = 0; }
        }
        for ($k = $n - 1; $k > 0 && $budget > 0; $k--) {
            $t = min(intdiv($budget, $k + 1), $cnt[$k]);
            $ans += $t * $k;
            $budget -= $t * ($k + 1);
            $cnt[$k - 1] += $cnt[$k] - $t;
        }
        return $ans;
    }
}
''')

add("3120_count_the_number_of_special_characters_i", r'''<?php
// LeetCode 3120 - Count the Number of Special Characters I
// https://leetcode.com/problems/count-the-number-of-special-characters-i/

class Solution {
    function numberOfSpecialChars($word) {
        $s = array_fill(0, 128, false);
        $n = strlen($word);
        for ($i = 0; $i < $n; $i++) $s[ord($word[$i])] = true;
        $ans = 0;
        for ($i = 0; $i < 26; $i++) {
            if ($s[97 + $i] && $s[65 + $i]) $ans++;
        }
        return $ans;
    }
}
''')

add("3121_count_the_number_of_special_characters_ii", r'''<?php
// LeetCode 3121 - Count the Number of Special Characters II
// https://leetcode.com/problems/count-the-number-of-special-characters-ii/

class Solution {
    function numberOfSpecialChars($word) {
        $first = array_fill(0, 128, 0);
        $last = array_fill(0, 128, 0);
        $n = strlen($word);
        for ($i = 0; $i < $n; $i++) {
            $c = ord($word[$i]);
            if ($first[$c] === 0) $first[$c] = $i + 1;
            $last[$c] = $i + 1;
        }
        $ans = 0;
        for ($i = 0; $i < 26; $i++) {
            if ($last[97 + $i] > 0 && $last[97 + $i] < $first[65 + $i]) $ans++;
        }
        return $ans;
    }
}
''')

add("3122_minimum_number_of_operations_to_satisfy_conditions", r'''<?php
// LeetCode 3122 - Minimum Number of Operations to Satisfy Conditions
// https://leetcode.com/problems/minimum-number-of-operations-to-satisfy-conditions/

class Solution {
    function minimumOperations($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        $INF = 1 << 29;
        $f = [];
        for ($i = 0; $i < $n; $i++) $f[] = array_fill(0, 10, $INF);
        for ($i = 0; $i < $n; $i++) {
            $cnt = array_fill(0, 10, 0);
            for ($j = 0; $j < $m; $j++) $cnt[$grid[$j][$i]]++;
            if ($i === 0) {
                for ($j = 0; $j < 10; $j++) $f[$i][$j] = $m - $cnt[$j];
            } else {
                for ($j = 0; $j < 10; $j++) {
                    for ($k = 0; $k < 10; $k++) {
                        if ($j !== $k) $f[$i][$j] = min($f[$i][$j], $f[$i - 1][$k] + $m - $cnt[$j]);
                    }
                }
            }
        }
        $ans = $INF;
        for ($j = 0; $j < 10; $j++) $ans = min($ans, $f[$n - 1][$j]);
        return $ans;
    }
}
''')

add("3123_find_edges_in_shortest_paths", '''<?php
// LeetCode 3123 - Find Edges in Shortest Paths
// https://leetcode.com/problems/find-edges-in-shortest-paths/
''' + MINHEAP + r'''
class Solution {
    function findAnswer($n, $edges) {
        $g = array_fill(0, $n, []);
        for ($i = 0; $i < count($edges); $i++) {
            $a = $edges[$i][0];
            $b = $edges[$i][1];
            $w = $edges[$i][2];
            $g[$a][] = [$b, $w, $i];
            $g[$b][] = [$a, $w, $i];
        }
        $INF = 1 << 30;
        $dist = array_fill(0, $n, $INF);
        $dist[0] = 0;
        $pq = new MinHeap(function ($a, $b) { return $a[0] <=> $b[0]; });
        $pq->push([0, 0]);
        while ($pq->size()) {
            $cur = $pq->pop();
            $da = $cur[0];
            $a = $cur[1];
            if ($da > $dist[$a]) continue;
            foreach ($g[$a] as $e) {
                $b = $e[0];
                $w = $e[1];
                if ($dist[$b] > $dist[$a] + $w) {
                    $dist[$b] = $dist[$a] + $w;
                    $pq->push([$dist[$b], $b]);
                }
            }
        }
        $ans = array_fill(0, count($edges), false);
        if ($dist[$n - 1] === $INF) return $ans;
        $q = [$n - 1];
        while ($q) {
            $a = array_shift($q);
            foreach ($g[$a] as $e) {
                $b = $e[0];
                $w = $e[1];
                $i = $e[2];
                if ($dist[$a] === $dist[$b] + $w) {
                    $ans[$i] = true;
                    $q[] = $b;
                }
            }
        }
        return $ans;
    }
}
''')

if __name__ == "__main__":
    n = 0
    for folder, body in SOLUTIONS.items():
        (ROOT / folder / "solution.php").write_text(body, encoding="utf-8")
        n += 1
        print("wrote", folder)
    print("written", n)

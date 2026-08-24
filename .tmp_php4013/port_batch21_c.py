#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
SOLUTIONS = {}

def add(folder, body):
    SOLUTIONS[folder] = body


add("3874_valid_subarrays_with_exactly_one_peak", r'''<?php
// LeetCode 3874 - Valid Subarrays With Exactly One Peak
// https://leetcode.com/problems/valid-subarrays-with-exactly-one-peak/

class Solution {
    function validSubarrays($nums, $k) {
        $n = count($nums);
        $peaks = [];
        for ($i = 1; $i < $n - 1; $i++) {
            if ($nums[$i] > $nums[$i - 1] && $nums[$i] > $nums[$i + 1]) $peaks[] = $i;
        }
        $ans = 0;
        $pn = count($peaks);
        for ($j = 0; $j < $pn; $j++) {
            $p = $peaks[$j];
            $leftMin = max($p - $k, 0);
            if ($j > 0) $leftMin = max($leftMin, $peaks[$j - 1] + 1);
            $rightMax = min($p + $k, $n - 1);
            if ($j < $pn - 1) $rightMax = min($rightMax, $peaks[$j + 1] - 1);
            $ans += ($p - $leftMin + 1) * ($rightMax - $p + 1);
        }
        return $ans;
    }
}
''')

add("3875_construct_uniform_parity_array_i", r'''<?php
// LeetCode 3875 - Construct Uniform Parity Array I
// https://leetcode.com/problems/construct-uniform-parity-array-i/

class Solution {
    function uniformArray($nums1) {
        return true;
    }
}
''')

add("3876_construct_uniform_parity_array_ii", r'''<?php
// LeetCode 3876 - Construct Uniform Parity Array II
// https://leetcode.com/problems/construct-uniform-parity-array-ii/

class Solution {
    function uniformArray($nums1) {
        $mn = PHP_INT_MAX;
        foreach ($nums1 as $x) {
            if ($x % 2 === 1 && $x < $mn) $mn = $x;
        }
        foreach ($nums1 as $x) {
            if ($x % 2 === 0 && $mn !== PHP_INT_MAX && $x < $mn) return false;
        }
        return true;
    }
}
''')

add("3877_minimum_removals_to_achieve_target_xor", r'''<?php
// LeetCode 3877 - Minimum Removals to Achieve Target XOR
// https://leetcode.com/problems/minimum-removals-to-achieve-target-xor/

class Solution {
    function minRemovals($nums, $target) {
        $mx = 0;
        foreach ($nums as $x) $mx = max($mx, $x);
        $m = 0;
        if ($mx > 0) {
            $u = $mx;
            while ($u !== 0) { $m++; $u >>= 1; }
        }
        if ((1 << $m) <= $target) return -1;
        $n = count($nums);
        $N = 1 << $m;
        $NEG = PHP_INT_MIN / 4;
        $f = [];
        for ($i = 0; $i <= $n; $i++) $f[$i] = array_fill(0, $N, $NEG);
        $f[0][0] = 0;
        for ($i = 1; $i <= $n; $i++) {
            $x = $nums[$i - 1];
            for ($j = 0; $j < $N; $j++) {
                $f[$i][$j] = $f[$i - 1][$j];
                if ($f[$i - 1][$j ^ $x] !== $NEG) {
                    $f[$i][$j] = max($f[$i][$j], $f[$i - 1][$j ^ $x] + 1);
                }
            }
        }
        if ($f[$n][$target] < 0) return -1;
        return $n - $f[$n][$target];
    }
}
''')

add("3878_count_good_subarrays", r'''<?php
// LeetCode 3878 - Count Good Subarrays
// https://leetcode.com/problems/count-good-subarrays/

class Solution {
    function countGoodSubarrays($nums) {
        $n = count($nums);
        $l = array_fill(0, $n, -1);
        $stk = [];
        for ($i = 0; $i < $n; $i++) {
            $x = $nums[$i];
            while (count($stk) > 0 && $nums[$stk[count($stk) - 1]] < $x && ($nums[$stk[count($stk) - 1]] | $x) === $x) {
                array_pop($stk);
            }
            if (count($stk) > 0) $l[$i] = $stk[count($stk) - 1];
            $stk[] = $i;
        }
        $r = array_fill(0, $n, $n);
        $stk = [];
        for ($i = $n - 1; $i >= 0; $i--) {
            while (count($stk) > 0 && ($nums[$stk[count($stk) - 1]] | $nums[$i]) === $nums[$i]) {
                array_pop($stk);
            }
            if (count($stk) > 0) $r[$i] = $stk[count($stk) - 1];
            $stk[] = $i;
        }
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            $ans += ($i - $l[$i]) * ($r[$i] - $i);
        }
        return $ans;
    }
}
''')

add("3879_maximum_distinct_path_sum_in_a_binary_tree", r'''<?php
// LeetCode 3879 - Maximum Distinct Path Sum in a Binary Tree
// https://leetcode.com/problems/maximum-distinct-path-sum-in-a-binary-tree/

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
    public $g;
    public $vis;
    function dfs($node, $p) {
        if (!$node) return;
        $this->g[spl_object_id($node)] = [$p, $node->left, $node->right];
        $this->dfs($node->left, $node);
        $this->dfs($node->right, $node);
    }
    function dfs2($node) {
        if (!$node || ($this->vis[$node->val] ?? false) === true) return 0;
        $this->vis[$node->val] = true;
        $res = $node->val;
        $best = 0;
        foreach ($this->g[spl_object_id($node)] as $nxt) $best = max($best, $this->dfs2($nxt));
        $this->vis[$node->val] = false;
        return $res + $best;
    }
    function collect($node, &$nodes) {
        if (!$node) return;
        $nodes[] = $node;
        $this->collect($node->left, $nodes);
        $this->collect($node->right, $nodes);
    }
    function maxSum($root) {
        $this->g = [];
        $this->vis = [];
        $this->dfs($root, null);
        $nodes = [];
        $this->collect($root, $nodes);
        $ans = PHP_INT_MIN;
        foreach ($nodes as $node) {
            $ans = max($ans, $this->dfs2($node));
            $this->vis = [];
        }
        return $ans;
    }
}
''')

add("3880_minimum_absolute_difference_between_two_values", r'''<?php
// LeetCode 3880 - Minimum Absolute Difference Between Two Values
// https://leetcode.com/problems/minimum-absolute-difference-between-two-values/

class Solution {
    function minAbsoluteDifference($nums) {
        $n = count($nums);
        $ans = $n + 1;
        $last = [-$ans, -$ans, -$ans];
        for ($i = 0; $i < $n; $i++) {
            $x = $nums[$i];
            if ($x !== 0) {
                $ans = min($ans, $i - $last[3 - $x]);
                $last[$x] = $i;
            }
        }
        if ($ans > $n) return -1;
        return $ans;
    }
}
''')

add("3881_direction_assignments_with_exactly_k_visible_people", r'''<?php
// LeetCode 3881 - Direction Assignments With Exactly K Visible People
// https://leetcode.com/problems/direction-assignments-with-exactly-k-visible-people/

class Solution {
    public $fact;
    public $invFact;
    public $ready = false;
    const N = 100001;
    const MOD = 1000000007;
    function qmi($a, $k, $p) {
        $res = 1;
        while ($k !== 0) {
            if (($k & 1) !== 0) $res = $res * $a % $p;
            $k >>= 1;
            $a = $a * $a % $p;
        }
        return $res;
    }
    function init() {
        if ($this->ready) return;
        $this->fact = array_fill(0, self::N, 0);
        $this->invFact = array_fill(0, self::N, 0);
        $this->fact[0] = $this->invFact[0] = 1;
        for ($i = 1; $i < self::N; $i++) {
            $this->fact[$i] = $this->fact[$i - 1] * $i % self::MOD;
            $this->invFact[$i] = $this->qmi($this->fact[$i], self::MOD - 2, self::MOD);
        }
        $this->ready = true;
    }
    function comb($n, $k) {
        return $this->fact[$n] * $this->invFact[$k] % self::MOD * $this->invFact[$n - $k] % self::MOD;
    }
    function countVisiblePeople($n, $pos, $k) {
        $this->init();
        $l = $pos;
        $r = $n - $pos - 1;
        $ans = 0;
        $lim = min($k, $l);
        for ($a = 0; $a <= $lim; $a++) {
            $b = $k - $a;
            if ($b <= $r) {
                $ans = ($ans + 2 * $this->comb($l, $a) % self::MOD * $this->comb($r, $b) % self::MOD) % self::MOD;
            }
        }
        return $ans;
    }
}
''')

add("3882_minimum_xor_path_in_a_grid", r'''<?php
// LeetCode 3882 - Minimum XOR Path in a Grid
// https://leetcode.com/problems/minimum-xor-path-in-a-grid/

class Solution {
    function minXor($grid) {
        $rows = count($grid);
        $cols = count($grid[0]);
        $dp = [];
        for ($c = 0; $c < $cols; $c++) $dp[$c] = array_fill(0, 1024, false);
        for ($row = 0; $row < $rows; $row++) {
            $left = array_fill(0, 1024, false);
            for ($col = 0; $col < $cols; $col++) {
                $next = array_fill(0, 1024, false);
                $value = $grid[$row][$col];
                if ($row === 0 && $col === 0) {
                    $next[$value] = true;
                } else {
                    for ($xorv = 0; $xorv < 1024; $xorv++) {
                        if ($dp[$col][$xorv] || $left[$xorv]) $next[$xorv ^ $value] = true;
                    }
                }
                $dp[$col] = $next;
                $left = $next;
            }
        }
        for ($xorv = 0; $xorv < 1024; $xorv++) {
            if ($dp[$cols - 1][$xorv]) return $xorv;
        }
        return -1;
    }
}
''')

add("3883_count_non_decreasing_arrays_with_given_digit_sums", r'''<?php
// LeetCode 3883 - Count Non Decreasing Arrays With Given Digit Sums
// https://leetcode.com/problems/count-non-decreasing-arrays-with-given-digit-sums/

class Solution {
    function countNonDecreasingArrays($digitSum) {
        $mod = 1000000007;
        $groups = [];
        for ($i = 0; $i <= 50; $i++) $groups[$i] = [];
        for ($x = 0; $x <= 5000; $x++) {
            $s = 0;
            for ($y = $x; $y > 0; $y = intdiv($y, 10)) $s += $y % 10;
            $groups[$s][] = $x;
        }
        $prevVals = $groups[$digitSum[0]];
        $dp = array_fill(0, count($prevVals), 1);
        $len = count($digitSum);
        for ($pos = 1; $pos < $len; $pos++) {
            $curVals = $groups[$digitSum[$pos]];
            $next = array_fill(0, count($curVals), 0);
            $j = 0;
            $prefix = 0;
            $cn = count($curVals);
            $pn = count($prevVals);
            for ($i = 0; $i < $cn; $i++) {
                $x = $curVals[$i];
                while ($j < $pn && $prevVals[$j] <= $x) {
                    $prefix += $dp[$j];
                    if ($prefix >= $mod) $prefix -= $mod;
                    $j++;
                }
                $next[$i] = $prefix;
            }
            $prevVals = $curVals;
            $dp = $next;
        }
        $ans = 0;
        foreach ($dp as $x) {
            $ans += $x;
            if ($ans >= $mod) $ans -= $mod;
        }
        return $ans;
    }
}
''')

add("3884_first_matching_character_from_both_ends", r'''<?php
// LeetCode 3884 - First Matching Character From Both Ends
// https://leetcode.com/problems/first-matching-character-from-both-ends/

class Solution {
    function firstMatchingIndex($s) {
        $n = strlen($s);
        $lim = intdiv($n, 2) + 1;
        for ($i = 0; $i < $lim; $i++) {
            if ($s[$i] === $s[$n - $i - 1]) return $i;
        }
        return -1;
    }
}
''')

add("3885_design_event_manager", r'''<?php
// LeetCode 3885 - Design Event Manager
// https://leetcode.com/problems/design-event-manager/

class EventManager {
    public $sl = [];
    public $d = [];
    function __construct($events) {
        $this->sl = [];
        $this->d = [];
        foreach ($events as $e) {
            $eventId = $e[0];
            $priority = $e[1];
            $this->sl[] = [-$priority, $eventId];
            $this->d[$eventId] = $priority;
        }
        $this->_sort();
    }
    function _sort() {
        usort($this->sl, function($a, $b) {
            if ($a[0] !== $b[0]) return $a[0] <=> $b[0];
            return $a[1] <=> $b[1];
        });
    }
    function updatePriority($eventId, $newPriority) {
        $old = $this->d[$eventId];
        $this->sl = array_values(array_filter($this->sl, function($x) use ($old, $eventId) {
            return !($x[0] === -$old && $x[1] === $eventId);
        }));
        $this->sl[] = [-$newPriority, $eventId];
        $this->d[$eventId] = $newPriority;
        $this->_sort();
    }
    function pollHighest() {
        if (!count($this->sl)) return -1;
        $top = array_shift($this->sl);
        $eventId = $top[1];
        unset($this->d[$eventId]);
        return $eventId;
    }
}
''')

add("3886_sum_of_sortable_integers", r'''<?php
// LeetCode 3886 - Sum of Sortable Integers
// https://leetcode.com/problems/sum-of-sortable-integers/

class Solution {
    function rotationMatches($block, $target) {
        $k = count($block);
        $prefix = array_fill(0, $k, 0);
        for ($i = 1; $i < $k; $i++) {
            $j = $prefix[$i - 1];
            while ($j > 0 && $target[$i] !== $target[$j]) $j = $prefix[$j - 1];
            if ($target[$i] === $target[$j]) $j++;
            $prefix[$i] = $j;
        }
        $matched = 0;
        $lim = 2 * $k - 1;
        for ($i = 0; $i < $lim; $i++) {
            $x = $block[$i % $k];
            while ($matched > 0 && $x !== $target[$matched]) $matched = $prefix[$matched - 1];
            if ($x === $target[$matched]) $matched++;
            if ($matched === $k) return true;
        }
        return false;
    }
    function sumOfSortableIntegers($nums) {
        $n = count($nums);
        $sorted = $nums;
        sort($sorted);
        $divisors = [];
        for ($d = 1; $d * $d <= $n; $d++) {
            if ($n % $d === 0) {
                $divisors[] = $d;
                if ($d * $d !== $n) $divisors[] = intdiv($n, $d);
            }
        }
        $answer = 0;
        foreach ($divisors as $k) {
            $ok = true;
            for ($start = 0; $start < $n; $start += $k) {
                $block = array_slice($nums, $start, $k);
                $target = array_slice($sorted, $start, $k);
                if (!$this->rotationMatches($block, $target)) { $ok = false; break; }
            }
            if ($ok) $answer += $k;
        }
        return $answer;
    }
}
''')

add("3887_incremental_even_weighted_cycle_queries", r'''<?php
// LeetCode 3887 - Incremental Even-Weighted Cycle Queries
// https://leetcode.com/problems/incremental-even-weighted-cycle-queries/

class Solution {
    public $parent;
    public $parity;
    function find($x) {
        if ($this->parent[$x] === $x) return [$x, 0];
        $res = $this->find($this->parent[$x]);
        $root = $res[0];
        $p = $res[1];
        $this->parity[$x] ^= $p;
        $this->parent[$x] = $root;
        return [$root, $this->parity[$x]];
    }
    function countValidEdges($n, $edges) {
        $this->parent = [];
        $size = [];
        $this->parity = array_fill(0, $n, 0);
        for ($i = 0; $i < $n; $i++) { $this->parent[$i] = $i; $size[$i] = 1; }
        $ans = 0;
        foreach ($edges as $e) {
            $fu = $this->find($e[0]);
            $fv = $this->find($e[1]);
            $ru = $fu[0];
            $pu = $fu[1];
            $rv = $fv[0];
            $pv = $fv[1];
            if ($ru === $rv) {
                if (($pu ^ $pv) === $e[2]) $ans++;
                continue;
            }
            if ($size[$ru] < $size[$rv]) {
                $t = $ru; $ru = $rv; $rv = $t;
                $t = $pu; $pu = $pv; $pv = $t;
            }
            $this->parent[$rv] = $ru;
            $this->parity[$rv] = $pu ^ $pv ^ $e[2];
            $size[$ru] += $size[$rv];
            $ans++;
        }
        return $ans;
    }
}
''')

add("3888_minimum_operations_to_make_all_grid_elements_equal", r'''<?php
// LeetCode 3888 - Minimum Operations to Make All Grid Elements Equal
// https://leetcode.com/problems/minimum-operations-to-make-all-grid-elements-equal/

class Solution {
    public $grid;
    public $k;
    public $m;
    public $n;
    function check($target) {
        $diff = [];
        for ($i = 0; $i < $this->m + 2; $i++) $diff[$i] = array_fill(0, $this->n + 2, 0);
        $totalOps = 0;
        for ($i = 1; $i <= $this->m; $i++) {
            for ($j = 1; $j <= $this->n; $j++) {
                $diff[$i][$j] += $diff[$i - 1][$j] + $diff[$i][$j - 1] - $diff[$i - 1][$j - 1];
                $curVal = $this->grid[$i - 1][$j - 1] + $diff[$i][$j];
                if ($curVal > $target) return -1;
                if ($curVal < $target) {
                    if ($i + $this->k - 1 > $this->m || $j + $this->k - 1 > $this->n) return -1;
                    $needed = $target - $curVal;
                    $totalOps += $needed;
                    $diff[$i][$j] += $needed;
                    $diff[$i + $this->k][$j] -= $needed;
                    $diff[$i][$j + $this->k] -= $needed;
                    $diff[$i + $this->k][$j + $this->k] += $needed;
                }
            }
        }
        return $totalOps;
    }
    function minOperations($grid, $k) {
        $this->grid = $grid;
        $this->k = $k;
        $this->m = count($grid);
        $this->n = count($grid[0]);
        $maxVal = $grid[0][0];
        foreach ($grid as $row) foreach ($row as $x) $maxVal = max($maxVal, $x);
        for ($t = $maxVal; $t <= $maxVal + 1; $t++) {
            $res = $this->check($t);
            if ($res !== -1) return $res;
        }
        return -1;
    }
}
''')

add("3889_mirror_frequency_distance", r'''<?php
// LeetCode 3889 - Mirror Frequency Distance
// https://leetcode.com/problems/mirror-frequency-distance/

class Solution {
    function mirrorFrequency($s) {
        $freq = [];
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $c = $s[$i];
            $freq[$c] = ($freq[$c] ?? 0) + 1;
        }
        $ans = 0;
        $vis = [];
        foreach ($freq as $c => $v) {
            if ($c >= 'a' && $c <= 'z') $m = chr(97 + 25 - (ord($c) - 97));
            else $m = chr(48 + (9 - (ord($c) - 48)));
            if (($vis[$m] ?? false) === true) continue;
            $vis[$c] = true;
            $mv = $freq[$m] ?? 0;
            $ans += abs($v - $mv);
        }
        return $ans;
    }
}
''')

add("3890_integers_with_multiple_sum_of_two_cubes", r'''<?php
// LeetCode 3890 - Integers With Multiple Sum of Two Cubes
// https://leetcode.com/problems/integers-with-multiple-sum-of-two-cubes/

class Solution {
    static $GOOD = null;
    function init() {
        if (self::$GOOD !== null) return;
        $LIMIT = 1000000000;
        $cnt = [];
        $cubes = [];
        for ($i = 0; $i <= 1000; $i++) $cubes[$i] = $i * $i * $i;
        for ($a = 1; $a <= 1000; $a++) {
            for ($b = $a; $b <= 1000; $b++) {
                $x = $cubes[$a] + $cubes[$b];
                if ($x > $LIMIT) break;
                $cnt[$x] = ($cnt[$x] ?? 0) + 1;
            }
        }
        self::$GOOD = [];
        foreach ($cnt as $k => $v) {
            if ($v > 1) self::$GOOD[] = $k;
        }
        sort(self::$GOOD);
    }
    function findGoodIntegers($n) {
        $this->init();
        $lo = 0;
        $hi = count(self::$GOOD);
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi, 2);
            if (self::$GOOD[$mid] <= $n) $lo = $mid + 1;
            else $hi = $mid;
        }
        return array_slice(self::$GOOD, 0, $lo);
    }
}
''')

add("3891_minimum_increase_to_maximize_special_indices", r'''<?php
// LeetCode 3891 - Minimum Increase to Maximize Special Indices
// https://leetcode.com/problems/minimum-increase-to-maximize-special-indices/

class Solution {
    public $nums;
    public $n;
    public $f;
    function dfs($i, $j) {
        if ($i >= $this->n - 1) return 0;
        if ($this->f[$i][$j] !== -1) return $this->f[$i][$j];
        $cost = max(0, max($this->nums[$i - 1], $this->nums[$i + 1]) + 1 - $this->nums[$i]);
        $ans = $cost + $this->dfs($i + 2, $j);
        if ($j > 0) $ans = min($ans, $this->dfs($i + 1, 0));
        return $this->f[$i][$j] = $ans;
    }
    function minIncrease($nums) {
        $this->nums = $nums;
        $this->n = count($nums);
        $this->f = [];
        for ($i = 0; $i < $this->n; $i++) $this->f[$i] = [-1, -1];
        return $this->dfs(1, ($this->n & 1) ^ 1);
    }
}
''')

add("3892_minimum_operations_to_achieve_at_least_k_peaks", r'''<?php
// LeetCode 3892 - Minimum Operations to Achieve at Least K Peaks
// https://leetcode.com/problems/minimum-operations-to-achieve-at-least-k-peaks/

class Solution {
    public $cost;
    public $INF;
    function line($left, $right, $choose) {
        if ($choose === 0) return 0;
        if ($left > $right || $choose > intdiv($right - $left + 2, 2)) return $this->INF;
        $prev2 = array_fill(0, $choose + 1, $this->INF);
        $prev1 = array_fill(0, $choose + 1, $this->INF);
        $prev2[0] = $prev1[0] = 0;
        for ($i = $left; $i <= $right; $i++) {
            $current = $prev1;
            for ($j = 1; $j <= $choose; $j++) {
                if ($prev2[$j - 1] !== $this->INF && $prev2[$j - 1] + $this->cost[$i] < $current[$j]) {
                    $current[$j] = $prev2[$j - 1] + $this->cost[$i];
                }
            }
            $prev2 = $prev1;
            $prev1 = $current;
        }
        return $prev1[$choose];
    }
    function minOperations($nums, $k) {
        $this->INF = PHP_INT_MAX / 4;
        $n = count($nums);
        if ($k === 0) return 0;
        if ($k > intdiv($n, 2)) return -1;
        $this->cost = array_fill(0, $n, 0);
        for ($i = 0; $i < $n; $i++) {
            $left = $nums[($i + $n - 1) % $n];
            $right = $nums[($i + 1) % $n];
            $need = max($left, $right);
            if ($need >= $nums[$i]) $this->cost[$i] = $need - $nums[$i] + 1;
        }
        $answer = $this->line(1, $n - 1, $k);
        $withFirst = $this->line(2, $n - 2, $k - 1);
        if ($withFirst !== $this->INF) {
            $withFirst += $this->cost[0];
            $answer = min($answer, $withFirst);
        }
        if ($answer === $this->INF) return -1;
        return $answer;
    }
}
''')

add("3893_maximum_team_size_with_overlapping_intervals", r'''<?php
// LeetCode 3893 - Maximum Team Size With Overlapping Intervals
// https://leetcode.com/problems/maximum-team-size-with-overlapping-intervals/

class Solution {
    function UpperBound($a, $x) {
        $lo = 0;
        $hi = count($a);
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi, 2);
            if ($a[$mid] <= $x) $lo = $mid + 1;
            else $hi = $mid;
        }
        return $lo;
    }
    function maximumTeamSize($startTime, $endTime) {
        $n = count($startTime);
        $st = $startTime;
        $en = $endTime;
        sort($st);
        sort($en);
        $ans = 0;
        for ($t = 0; $t < $n; $t++) {
            $l = $startTime[$t];
            $r = $endTime[$t];
            $i = $this->UpperBound($en, $l - 1);
            $j = $this->UpperBound($st, $r);
            $ans = max($ans, $j - $i);
        }
        return $ans;
    }
}
''')

add("3894_traffic_signal_color", r'''<?php
// LeetCode 3894 - Traffic Signal Color
// https://leetcode.com/problems/traffic-signal-color/

class Solution {
    function trafficSignal($timer) {
        if ($timer === 0) return 'Green';
        if ($timer === 30) return 'Orange';
        if ($timer > 30 && $timer <= 90) return 'Red';
        return 'Invalid';
    }
}
''')

add("3895_count_digit_appearances", r'''<?php
// LeetCode 3895 - Count Digit Appearances
// https://leetcode.com/problems/count-digit-appearances/

class Solution {
    function countDigitOccurrences($nums, $digit) {
        $ans = 0;
        foreach ($nums as $num) {
            $x = $num;
            for (; $x > 0; $x = intdiv($x, 10)) {
                if ($x % 10 === $digit) $ans++;
            }
        }
        return $ans;
    }
}
''')

add("3896_minimum_operations_to_transform_array_into_alternating_prime", r'''<?php
// LeetCode 3896 - Minimum Operations to Transform Array Into Alternating Prime
// https://leetcode.com/problems/minimum-operations-to-transform-array-into-alternating-prime/

class Solution {
    static $isPrime = null;
    static $primes = null;
    const MX = 200000;
    function init() {
        if (self::$isPrime !== null) return;
        self::$isPrime = array_fill(0, self::MX + 1, true);
        self::$isPrime[0] = self::$isPrime[1] = false;
        for ($i = 2; $i * $i <= self::MX; $i++) {
            if (self::$isPrime[$i]) {
                for ($j = $i * $i; $j <= self::MX; $j += $i) self::$isPrime[$j] = false;
            }
        }
        self::$primes = [];
        for ($i = 2; $i <= self::MX; $i++) if (self::$isPrime[$i]) self::$primes[] = $i;
    }
    function minOperations($nums) {
        $this->init();
        $ans = 0;
        $n = count($nums);
        $pn = count(self::$primes);
        for ($i = 0; $i < $n; $i++) {
            $x = $nums[$i];
            if ($i % 2 === 0) {
                $lo = 0;
                $hi = $pn;
                while ($lo < $hi) {
                    $mid = ($lo + $hi) >> 1;
                    if (self::$primes[$mid] < $x) $lo = $mid + 1;
                    else $hi = $mid;
                }
                $ans += self::$primes[$lo] - $x;
            } else if (self::$isPrime[$x]) {
                $ans += ($x === 2) ? 2 : 1;
            }
        }
        return $ans;
    }
}
''')

add("3897_maximum_value_of_concatenated_binary_segments", r'''<?php
// LeetCode 3897 - Maximum Value of Concatenated Binary Segments
// https://leetcode.com/problems/maximum-value-of-concatenated-binary-segments/

class Solution {
    const MOD = 1000000007;
    function group($p) {
        if ($p[1] === 0) return 0;
        if ($p[0] > 0) return 1;
        return 2;
    }
    function maxValue($nums1, $nums0) {
        $n = count($nums1);
        $pairs = [];
        for ($i = 0; $i < $n; $i++) $pairs[] = [$nums1[$i], $nums0[$i]];
        $b = 0;
        for ($i = 0; $i < $n; $i++) $b += $nums1[$i] + $nums0[$i];
        usort($pairs, function($a, $c) {
            $g1 = $this->group($a);
            $g2 = $this->group($c);
            if ($g1 !== $g2) return $g1 <=> $g2;
            if ($g1 === 0) return $c[0] <=> $a[0];
            if ($g1 === 1) {
                if ($a[0] !== $c[0]) return $c[0] <=> $a[0];
                return $a[1] <=> $c[1];
            }
            return $a[1] <=> $c[1];
        });
        $p = [];
        $p[0] = 1;
        for ($i = 1; $i < $b; $i++) $p[$i] = 2 * $p[$i - 1] % self::MOD;
        $ans = 0;
        $b--;
        foreach ($pairs as $pr) {
            $cnt1 = $pr[0];
            $cnt0 = $pr[1];
            while ($cnt1 > 0) {
                $ans = ($ans + $p[$b]) % self::MOD;
                $b--;
                $cnt1--;
            }
            $b -= $cnt0;
        }
        return $ans;
    }
}
''')

add("3898_find_the_degree_of_each_vertex", r'''<?php
// LeetCode 3898 - Find the Degree of Each Vertex
// https://leetcode.com/problems/find-the-degree-of-each-vertex/

class Solution {
    function findDegrees($matrix) {
        $ans = array_fill(0, count($matrix), 0);
        $n = count($matrix);
        for ($i = 0; $i < $n; $i++) {
            foreach ($matrix[$i] as $x) $ans[$i] += $x;
        }
        return $ans;
    }
}
''')

add("3899_angles_of_a_triangle", r'''<?php
// LeetCode 3899 - Angles of a Triangle
// https://leetcode.com/problems/angles-of-a-triangle/

class Solution {
    function internalAngles($sides) {
        $sides = $sides;
        sort($sides);
        $a = $sides[0];
        $b = $sides[1];
        $c = $sides[2];
        if ($a + $b <= $c) return [];
        $PI = acos(-1.0);
        $A = acos(($b * $b + $c * $c - $a * $a) / (2.0 * $b * $c)) * 180.0 / $PI;
        $B = acos(($a * $a + $c * $c - $b * $b) / (2.0 * $a * $c)) * 180.0 / $PI;
        $C = 180.0 - $A - $B;
        return [$A, $B, $C];
    }
}
''')

add("3900_longest_balanced_substring_after_one_swap", r'''<?php
// LeetCode 3900 - Longest Balanced Substring After One Swap
// https://leetcode.com/problems/longest-balanced-substring-after-one-swap/

class Solution {
    function longestBalanced($s) {
        $cnt0 = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) if ($s[$i] === '0') $cnt0++;
        $cnt1 = $n - $cnt0;
        $pos = [];
        $pos[0] = [-1];
        $ans = 0;
        $pre = 0;
        for ($i = 0; $i < $n; $i++) {
            if ($s[$i] === '1') $pre++;
            else $pre--;
            if (!isset($pos[$pre])) $pos[$pre] = [];
            $pos[$pre][] = $i;
            $ans = max($ans, $i - $pos[$pre][0]);
            if (isset($pos[$pre - 2])) {
                $p = $pos[$pre - 2];
                if (intdiv($i - $p[0] - 2, 2) < $cnt0) $ans = max($ans, $i - $p[0]);
                else if (count($p) > 1) $ans = max($ans, $i - $p[1]);
            }
            if (isset($pos[$pre + 2])) {
                $p = $pos[$pre + 2];
                if (intdiv($i - $p[0] - 2, 2) < $cnt1) $ans = max($ans, $i - $p[0]);
                else if (count($p) > 1) $ans = max($ans, $i - $p[1]);
            }
        }
        return $ans;
    }
}
''')

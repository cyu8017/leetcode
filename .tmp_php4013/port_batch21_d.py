#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
SOLUTIONS = {}

def add(folder, body):
    SOLUTIONS[folder] = body


add("3901_good_subsequence_queries", r'''<?php
// LeetCode 3901 - Good Subsequence Queries
// https://leetcode.com/problems/good-subsequence-queries/

class SegmentTree3901 {
    public $tr;
    function gcd($a, $b) {
        while ($b !== 0) { $t = $a % $b; $a = $b; $b = $t; }
        return $a;
    }
    function __construct($n) {
        $this->tr = [];
        $sz = $n << 2;
        for ($i = 0; $i < $sz; $i++) $this->tr[$i] = ['l' => 0, 'r' => 0, 'g' => 0];
        $this->build(1, 1, $n);
    }
    function build($u, $l, $r) {
        $this->tr[$u]['l'] = $l;
        $this->tr[$u]['r'] = $r;
        $this->tr[$u]['g'] = 0;
        if ($l === $r) return;
        $mid = ($l + $r) >> 1;
        $this->build($u << 1, $l, $mid);
        $this->build($u << 1 | 1, $mid + 1, $r);
    }
    function pushup($u) {
        $this->tr[$u]['g'] = $this->gcd($this->tr[$u << 1]['g'], $this->tr[$u << 1 | 1]['g']);
    }
    function modify($u, $x, $v) {
        if ($this->tr[$u]['l'] === $this->tr[$u]['r']) { $this->tr[$u]['g'] = $v; return; }
        $mid = ($this->tr[$u]['l'] + $this->tr[$u]['r']) >> 1;
        if ($x <= $mid) $this->modify($u << 1, $x, $v);
        else $this->modify($u << 1 | 1, $x, $v);
        $this->pushup($u);
    }
    function query($u, $l, $r) {
        if ($l > $r) return 0;
        if ($this->tr[$u]['l'] >= $l && $this->tr[$u]['r'] <= $r) return $this->tr[$u]['g'];
        $mid = ($this->tr[$u]['l'] + $this->tr[$u]['r']) >> 1;
        if ($r <= $mid) return $this->query($u << 1, $l, $r);
        if ($l > $mid) return $this->query($u << 1 | 1, $l, $r);
        return $this->gcd($this->query($u << 1, $l, $mid), $this->query($u << 1 | 1, $mid + 1, $r));
    }
}

class Solution {
    function gcd($a, $b) {
        while ($b !== 0) { $t = $a % $b; $a = $b; $b = $t; }
        return $a;
    }
    function countGoodSubseq($nums, $p, $queries) {
        $n = count($nums);
        $tree = new SegmentTree3901($n);
        $cnt = 0;
        for ($i = 0; $i < $n; $i++) {
            if ($nums[$i] % $p === 0) {
                $tree->modify(1, $i + 1, $nums[$i]);
                $cnt++;
            }
        }
        $ans = 0;
        foreach ($queries as $q) {
            $idx = $q[0];
            $val = $q[1];
            if ($nums[$idx] % $p === 0) {
                $tree->modify(1, $idx + 1, 0);
                $cnt--;
            }
            if ($val % $p === 0) {
                $tree->modify(1, $idx + 1, $val);
                $cnt++;
            }
            $nums[$idx] = $val;
            if ($tree->tr[1]['g'] !== $p) continue;
            if ($cnt < $n || $n > 6) {
                $ans++;
                continue;
            }
            for ($i = 1; $i <= $n; $i++) {
                $leftG = $tree->query(1, 1, $i - 1);
                $rightG = $tree->query(1, $i + 1, $n);
                if ($this->gcd($leftG, $rightG) === $p) { $ans++; break; }
            }
        }
        return $ans;
    }
}
''')

add("3902_zigzag_level_sum_of_binary_tree", r'''<?php
// LeetCode 3902 - Zigzag Level Sum of Binary Tree
// https://leetcode.com/problems/zigzag-level-sum-of-binary-tree/

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
    function zigzagLevelSum($root) {
        $ans = [];
        $q = [$root];
        $left = true;
        while (count($q)) {
            $nq = [];
            foreach ($q as $node) {
                if ($node->left) $nq[] = $node->left;
                if ($node->right) $nq[] = $node->right;
            }
            $m = count($q);
            $s = 0;
            for ($i = 0; $i < $m; $i++) {
                $node = $left ? $q[$i] : $q[$m - $i - 1];
                $child = $left ? $node->left : $node->right;
                if (!$child) break;
                $s += $node->val;
            }
            $ans[] = $s;
            $left = !$left;
            $q = $nq;
        }
        return $ans;
    }
}
''')

add("3903_smallest_stable_index_i", r'''<?php
// LeetCode 3903 - Smallest Stable Index I
// https://leetcode.com/problems/smallest-stable-index-i/

class Solution {
    function firstStableIndex($nums, $k) {
        $n = count($nums);
        $right = [];
        $right[$n - 1] = $nums[$n - 1];
        for ($i = $n - 2; $i >= 0; $i--) $right[$i] = min($right[$i + 1], $nums[$i]);
        $left = 0;
        for ($i = 0; $i < $n; $i++) {
            $left = max($left, $nums[$i]);
            if ($left - $right[$i] <= $k) return $i;
        }
        return -1;
    }
}
''')

add("3904_smallest_stable_index_ii", r'''<?php
// LeetCode 3904 - Smallest Stable Index II
// https://leetcode.com/problems/smallest-stable-index-ii/

class Solution {
    function firstStableIndex($nums, $k) {
        $n = count($nums);
        $right = [];
        $right[$n - 1] = $nums[$n - 1];
        for ($i = $n - 2; $i >= 0; $i--) $right[$i] = min($right[$i + 1], $nums[$i]);
        $left = 0;
        for ($i = 0; $i < $n; $i++) {
            $left = max($left, $nums[$i]);
            if ($left - $right[$i] <= $k) return $i;
        }
        return -1;
    }
}
''')

add("3905_multi_source_flood_fill", r'''<?php
// LeetCode 3905 - Multi Source Flood Fill
// https://leetcode.com/problems/multi-source-flood-fill/

class Solution {
    function colorGrid($n, $m, $sources) {
        $ans = [];
        for ($i = 0; $i < $n; $i++) $ans[$i] = array_fill(0, $m, 0);
        $q = [];
        foreach ($sources as $s) $q[] = [$s[0], $s[1], $s[2]];
        $dirs = [-1, 0, 1, 0, -1];
        foreach ($q as $s) $ans[$s[0]][$s[1]] = $s[2];
        while (count($q)) {
            $vis = [];
            foreach ($q as $curr) {
                $r = $curr[0];
                $c = $curr[1];
                $color = $curr[2];
                for ($i = 0; $i < 4; $i++) {
                    $x = $r + $dirs[$i];
                    $y = $c + $dirs[$i + 1];
                    if ($x >= 0 && $x < $n && $y >= 0 && $y < $m && $ans[$x][$y] === 0) {
                        $key = $x . ',' . $y;
                        if (!isset($vis[$key]) || $color > $vis[$key]) $vis[$key] = $color;
                    }
                }
            }
            $q = [];
            foreach ($vis as $key => $color) {
                $parts = explode(',', $key);
                $x = intval($parts[0]);
                $y = intval($parts[1]);
                $ans[$x][$y] = $color;
                $q[] = [$x, $y, $color];
            }
        }
        return $ans;
    }
}
''')

add("3906_count_good_integers_on_a_grid_path", r'''<?php
// LeetCode 3906 - Count Good Integers on a Grid Path
// https://leetcode.com/problems/count-good-integers-on-a-grid-path/

class Solution {
    public $key;
    public $s;
    public $f;
    function dfs($pos, $last, $lim) {
        if ($pos === 16) return 1;
        if (!$lim && $this->f[$pos][$last] !== -1) return $this->f[$pos][$last];
        $res = 0;
        $start = $this->key[$pos] ? $last : 0;
        $end = $lim ? (ord($this->s[$pos]) - 48) : 9;
        for ($i = $start; $i <= $end; $i++) {
            $nextLast = $this->key[$pos] ? $i : $last;
            $res += $this->dfs($pos + 1, $nextLast, $lim && ($i === $end));
        }
        if (!$lim) $this->f[$pos][$last] = $res;
        return $res;
    }
    function calc($x) {
        if ($x < 0) return 0;
        $t = strval($x);
        $this->s = str_repeat('0', 16 - strlen($t)) . $t;
        $this->f = [];
        for ($i = 0; $i < 16; $i++) $this->f[$i] = array_fill(0, 10, -1);
        return $this->dfs(0, 0, true);
    }
    function countGoodIntegersOnPath($l, $r, $directions) {
        $this->key = array_fill(0, 16, false);
        $row = 0;
        $col = 0;
        $this->key[0] = true;
        $n = strlen($directions);
        for ($i = 0; $i < $n; $i++) {
            $c = $directions[$i];
            if ($c === 'D') $row++;
            else $col++;
            $this->key[$row * 4 + $col] = true;
        }
        return $this->calc($r) - $this->calc($l - 1);
    }
}
''')

add("3907_count_smaller_elements_with_opposite_parity", r'''<?php
// LeetCode 3907 - Count Smaller Elements With Opposite Parity
// https://leetcode.com/problems/count-smaller-elements-with-opposite-parity/

class BIT3907 {
    public $n;
    public $c;
    function __construct($n_) {
        $this->n = $n_;
        $this->c = array_fill(0, $n_ + 1, 0);
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

class Solution {
    function countSmallerOppositeParity($nums) {
        $n = count($nums);
        $sorted = $nums;
        sort($sorted);
        $m = 0;
        $uniq = [];
        for ($i = 0; $i < count($sorted); $i++) {
            if ($i === 0 || $sorted[$i] !== $sorted[$i - 1]) $uniq[$m++] = $sorted[$i];
        }
        $sorted = $uniq;
        $bits = [new BIT3907($m), new BIT3907($m)];
        $ans = array_fill(0, $n, 0);
        for ($i = $n - 1; $i >= 0; $i--) {
            $lo = 0;
            $hi = count($sorted);
            while ($lo < $hi) {
                $mid = ($lo + $hi) >> 1;
                if ($sorted[$mid] < $nums[$i]) $lo = $mid + 1;
                else $hi = $mid;
            }
            $x = $lo + 1;
            $ans[$i] = $bits[($nums[$i] & 1) ^ 1]->query($x - 1);
            $bits[$nums[$i] & 1]->update($x, 1);
        }
        return $ans;
    }
}
''')

add("3908_valid_digit_number", r'''<?php
// LeetCode 3908 - Valid Digit Number
// https://leetcode.com/problems/valid-digit-number/

class Solution {
    function validDigit($n, $x) {
        $hasX = false;
        while ($n > 9) {
            $hasX = $hasX || ($n % 10 === $x);
            $n = intdiv($n, 10);
        }
        return $hasX && ($n !== $x);
    }
}
''')

add("3909_compare_sums_of_bitonic_parts", r'''<?php
// LeetCode 3909 - Compare Sums of Bitonic Parts
// https://leetcode.com/problems/compare-sums-of-bitonic-parts/

class Solution {
    function compareBitonicSums($nums) {
        $l = $nums[0];
        $r = 0;
        foreach ($nums as $x) $r += $x;
        $n = count($nums);
        for ($i = 1; $i < $n; $i++) {
            if ($nums[$i - 1] > $nums[$i]) break;
            $l += $nums[$i];
            $r -= $nums[$i - 1];
        }
        if ($l === $r) return -1;
        if ($l > $r) return 0;
        return 1;
    }
}
''')

add("3910_count_connected_subgraphs_with_even_node_sum", r'''<?php
// LeetCode 3910 - Count Connected Subgraphs With Even Node Sum
// https://leetcode.com/problems/count-connected-subgraphs-with-even-node-sum/

class Solution {
    public $g;
    public $vis;
    function dfs($u) {
        $this->vis |= 1 << $u;
        foreach ($this->g[$u] as $v) {
            if ((($this->vis >> $v) & 1) === 0) $this->dfs($v);
        }
    }
    function evenSumSubgraphs($nums, $edges) {
        $n = count($nums);
        $this->g = [];
        for ($i = 0; $i < $n; $i++) $this->g[$i] = [];
        foreach ($edges as $e) {
            $this->g[$e[0]][] = $e[1];
            $this->g[$e[1]][] = $e[0];
        }
        $m = (1 << $n) - 1;
        $ans = 0;
        for ($sub = 1; $sub <= $m; $sub++) {
            $s = 0;
            for ($i = 0; $i < $n; $i++) {
                if ((($sub >> $i) & 1) !== 0) $s += $nums[$i];
            }
            if ($s % 2 !== 0) continue;
            $this->vis = $m ^ $sub;
            $start = 0;
            for ($b = 31; $b >= 0; $b--) {
                if (($sub >> $b) & 1) { $start = $b; break; }
            }
            $this->dfs($start);
            if ($this->vis === $m) $ans++;
        }
        return $ans;
    }
}
''')

add("3911_k_th_smallest_remaining_even_integer_in_subarray_queries", r'''<?php
// LeetCode 3911 - K-th Smallest Remaining Even Integer in Subarray Queries
// https://leetcode.com/problems/k-th-smallest-remaining-even-integer-in-subarray-queries/

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
    function kthSmallestEven($nums, $queries) {
        $n = count($nums);
        $evenPrefix = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; $i++) {
            $evenPrefix[$i + 1] = $evenPrefix[$i] + ($nums[$i] % 2 === 0 ? 1 : 0);
        }
        $ans = [];
        $qn = count($queries);
        for ($qi = 0; $qi < $qn; $qi++) {
            $l = $queries[$qi][0];
            $r = $queries[$qi][1];
            $k = $queries[$qi][2];
            $lo = 1;
            $hi = $k + ($r - $l + 1);
            while ($lo < $hi) {
                $mid = intdiv($lo + $hi, 2);
                $pos = $this->UpperBound($nums, 2 * $mid);
                if ($pos > $r + 1) $pos = $r + 1;
                $removed = 0;
                if ($pos > $l) $removed = $evenPrefix[$pos] - $evenPrefix[$l];
                if ($mid - $removed >= $k) $hi = $mid;
                else $lo = $mid + 1;
            }
            $ans[$qi] = 2 * $lo;
        }
        return $ans;
    }
}
''')

add("3912_valid_elements_in_an_array", r'''<?php
// LeetCode 3912 - Valid Elements in an Array
// https://leetcode.com/problems/valid-elements-in-an-array/

class Solution {
    function findValidElements($nums) {
        $n = count($nums);
        $right = [];
        $right[$n - 1] = $nums[$n - 1];
        for ($i = $n - 2; $i >= 0; $i--) $right[$i] = max($right[$i + 1], $nums[$i]);
        $left = 0;
        $ans = [];
        for ($i = 0; $i < $n; $i++) {
            $x = $nums[$i];
            if ($x > $left || $i === $n - 1 || $x > $right[$i + 1]) $ans[] = $x;
            $left = max($left, $x);
        }
        return $ans;
    }
}
''')

add("3913_sort_vowels_by_frequency", r'''<?php
// LeetCode 3913 - Sort Vowels by Frequency
// https://leetcode.com/problems/sort-vowels-by-frequency/

class Solution {
    function sortVowels($s) {
        $st = ['a' => true, 'e' => true, 'i' => true, 'o' => true, 'u' => true];
        $vowels = [];
        $cnt = [];
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $c = $s[$i];
            if (!isset($st[$c])) continue;
            if (!isset($cnt[$c])) { $vowels[] = $c; $cnt[$c] = 0; }
            $cnt[$c]++;
        }
        usort($vowels, function($a, $b) use (&$cnt) {
            return $cnt[$b] <=> $cnt[$a];
        });
        $ans = [];
        for ($i = 0; $i < $n; $i++) $ans[] = $s[$i];
        $i = 0;
        for ($k = 0; $k < $n; $k++) {
            if (!isset($st[$s[$k]])) continue;
            $ch = $vowels[$i];
            $ans[$k] = $ch;
            $cnt[$ch]--;
            if ($cnt[$ch] === 0) $i++;
        }
        return implode('', $ans);
    }
}
''')

add("3914_minimum_operations_to_make_array_non_decreasing", r'''<?php
// LeetCode 3914 - Minimum Operations to Make Array Non Decreasing
// https://leetcode.com/problems/minimum-operations-to-make-array-non-decreasing/

class Solution {
    function minOperations($nums) {
        $ans = 0;
        $n = count($nums);
        for ($i = 1; $i < $n; $i++) {
            $ans += max(0, $nums[$i - 1] - $nums[$i]);
        }
        return $ans;
    }
}
''')

add("3915_maximum_sum_of_alternating_subsequence_with_distance_at_least_k", r'''<?php
// LeetCode 3915 - Maximum Sum of Alternating Subsequence With Distance at Least K
// https://leetcode.com/problems/maximum-sum-of-alternating-subsequence-with-distance-at-least-k/

class Fenwick3915 {
    public $f;
    function __construct($n) {
        $this->f = array_fill(0, $n, 0);
    }
    function update($i, $val) {
        for (; $i < count($this->f); $i += $i & -$i) $this->f[$i] = max($this->f[$i], $val);
    }
    function preMax($i) {
        $res = 0;
        for (; $i > 0; $i &= $i - 1) $res = max($res, $this->f[$i]);
        return $res;
    }
}

class Solution {
    function maxAlternatingSum($nums, $k) {
        $sorted = $nums;
        sort($sorted);
        $m = 0;
        $uniq = [];
        for ($i = 0; $i < count($sorted); $i++) {
            if ($i === 0 || $sorted[$i] !== $sorted[$i - 1]) $uniq[$m++] = $sorted[$i];
        }
        $sorted = $uniq;
        $n = count($nums);
        $fInc = array_fill(0, $n, 0);
        $fDec = array_fill(0, $n, 0);
        $inc = new Fenwick3915($m + 1);
        $dec = new Fenwick3915($m + 1);
        $ans = 0;
        $ranks = array_fill(0, $n, 0);
        for ($i = 0; $i < $n; $i++) {
            $x = $nums[$i];
            if ($i >= $k) {
                $j = $ranks[$i - $k];
                $inc->update($m - $j, $fInc[$i - $k]);
                $dec->update($j + 1, $fDec[$i - $k]);
            }
            $lo = 0;
            $hi = count($sorted);
            while ($lo < $hi) {
                $mid = ($lo + $hi) >> 1;
                if ($sorted[$mid] < $x) $lo = $mid + 1;
                else $hi = $mid;
            }
            $ranks[$i] = $lo;
            $fInc[$i] = $dec->preMax($lo) + $x;
            $fDec[$i] = $inc->preMax($m - 1 - $lo) + $x;
            $ans = max($ans, max($fInc[$i], $fDec[$i]));
        }
        return $ans;
    }
}
''')

add("3916_number_of_zigzag_arrays_iii", r'''<?php
// LeetCode 3916 - Number of ZigZag Arrays III
// https://leetcode.com/problems/number-of-zigzag-arrays-iii/

class Solution {
    function powm($a, $e, $mod) {
        $res = 1;
        while ($e > 0) {
            if (($e & 1) !== 0) $res = $res * $a % $mod;
            $a = $a * $a % $mod;
            $e >>= 1;
        }
        return $res;
    }
    function zigZagArrays($n, $l, $r) {
        $mod = 1000000007;
        $points = $n + 1;
        $values = array_fill(0, $points + 1, 0);
        for ($m = 1; $m <= $points; $m++) {
            $up = [];
            $down = [];
            for ($value = 0; $value < $m; $value++) {
                $up[$value] = $value;
                $down[$value] = $m - 1 - $value;
            }
            for ($length = 3; $length <= $n; $length++) {
                $nextUp = array_fill(0, $m, 0);
                $nextDown = array_fill(0, $m, 0);
                $prefix = 0;
                for ($value = 0; $value < $m; $value++) {
                    $nextUp[$value] = $prefix;
                    $prefix = ($prefix + $down[$value]) % $mod;
                }
                $suffix = 0;
                for ($value = $m - 1; $value >= 0; $value--) {
                    $nextDown[$value] = $suffix;
                    $suffix = ($suffix + $up[$value]) % $mod;
                }
                $up = $nextUp;
                $down = $nextDown;
            }
            for ($value = 0; $value < $m; $value++) {
                $values[$m] = ($values[$m] + $up[$value] + $down[$value]) % $mod;
            }
        }
        $x = ($r - $l + 1) % $mod;
        if ($r - $l + 1 <= $points) return $values[$r - $l + 1];
        $prefixA = [];
        $suffixA = [];
        $prefixA[0] = 1;
        for ($i = 1; $i <= $points; $i++) {
            $prefixA[$i] = $prefixA[$i - 1] * (($x - $i + $mod) % $mod) % $mod;
        }
        $suffixA[$points + 1] = 1;
        for ($i = $points; $i >= 1; $i--) {
            $suffixA[$i] = $suffixA[$i + 1] * (($x - $i + $mod) % $mod) % $mod;
        }
        $factorial = [];
        $factorial[0] = 1;
        for ($i = 1; $i <= $points; $i++) $factorial[$i] = $factorial[$i - 1] * $i % $mod;
        $answer = 0;
        for ($i = 1; $i <= $points; $i++) {
            $numerator = $prefixA[$i - 1] * $suffixA[$i + 1] % $mod;
            $denominator = $factorial[$i - 1] * $factorial[$points - $i] % $mod;
            $term = $values[$i] * $numerator % $mod * $this->powm($denominator, $mod - 2, $mod) % $mod;
            if (($points - $i) % 2 === 1) $answer -= $term;
            else $answer += $term;
            $answer %= $mod;
        }
        if ($answer < 0) $answer += $mod;
        return $answer;
    }
}
''')

add("3917_count_indices_with_opposite_parity", r'''<?php
// LeetCode 3917 - Count Indices With Opposite Parity
// https://leetcode.com/problems/count-indices-with-opposite-parity/

class Solution {
    function countOppositeParity($nums) {
        $cnt = [0, 0];
        foreach ($nums as $x) $cnt[$x & 1]++;
        $n = count($nums);
        $ans = array_fill(0, $n, 0);
        for ($i = 0; $i < $n; $i++) {
            $x = $nums[$i];
            $cnt[$x & 1]--;
            $ans[$i] = $cnt[($x & 1) ^ 1];
        }
        return $ans;
    }
}
''')

add("3918_sum_of_primes_between_number_and_its_reverse", r'''<?php
// LeetCode 3918 - Sum of Primes Between Number and Its Reverse
// https://leetcode.com/problems/sum-of-primes-between-number-and-its-reverse/

class Solution {
    static $isPrime = null;
    function Init() {
        if (self::$isPrime !== null) return;
        self::$isPrime = array_fill(0, 1001, true);
        self::$isPrime[0] = self::$isPrime[1] = false;
        for ($i = 2; $i * $i <= 1000; $i++) {
            if (self::$isPrime[$i]) {
                for ($j = $i * $i; $j <= 1000; $j += $i) self::$isPrime[$j] = false;
            }
        }
    }
    function sumOfPrimesInRange($n) {
        $this->Init();
        $r = 0;
        for ($x = $n; $x > 0; $x = intdiv($x, 10)) $r = $r * 10 + $x % 10;
        $low = min($n, $r);
        $high = max($n, $r);
        $ans = 0;
        for ($x = $low; $x <= $high; $x++) {
            if (self::$isPrime[$x]) $ans += $x;
        }
        return $ans;
    }
}
''')

add("3919_minimum_cost_to_move_between_indices", r'''<?php
// LeetCode 3919 - Minimum Cost to Move Between Indices
// https://leetcode.com/problems/minimum-cost-to-move-between-indices/

class Solution {
    function minCost($nums, $queries) {
        $n = count($nums);
        $s1 = array_fill(0, $n, 0);
        $s2 = array_fill(0, $n, 0);
        for ($i = 1; $i < $n; $i++) {
            $c1 = 1;
            if ($i > 1 && $nums[$i - 1] - $nums[$i - 2] <= $nums[$i] - $nums[$i - 1]) $c1 = $nums[$i] - $nums[$i - 1];
            $c2 = 1;
            if ($i < $n - 1 && $nums[$i] - $nums[$i - 1] > $nums[$i + 1] - $nums[$i]) $c2 = $nums[$i] - $nums[$i - 1];
            $s1[$i] = $s1[$i - 1] + $c1;
            $s2[$i] = $s2[$i - 1] + $c2;
        }
        $ans = [];
        $qn = count($queries);
        for ($i = 0; $i < $qn; $i++) {
            $l = $queries[$i][0];
            $r = $queries[$i][1];
            $ans[$i] = ($l < $r) ? ($s1[$r] - $s1[$l]) : ($s2[$l] - $s2[$r]);
        }
        return $ans;
    }
}
''')

add("3920_maximize_fixed_points_after_deletions", r'''<?php
// LeetCode 3920 - Maximize Fixed Points After Deletions
// https://leetcode.com/problems/maximize-fixed-points-after-deletions/

class Solution {
    function maxFixedPoints($nums) {
        $tails = [];
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            if ($i < $nums[$i]) continue;
            $d = $i - $nums[$i];
            $lo = 0;
            $hi = count($tails);
            while ($lo < $hi) {
                $mid = ($lo + $hi) >> 1;
                if ($tails[$mid] < $d) $lo = $mid + 1;
                else $hi = $mid;
            }
            if ($lo === count($tails)) $tails[] = $d;
            else $tails[$lo] = $d;
        }
        return count($tails);
    }
}
''')

add("3921_score_validator", r'''<?php
// LeetCode 3921 - Score Validator
// https://leetcode.com/problems/score-validator/

class Solution {
    function scoreValidator($events) {
        $score = 0;
        $counter = 0;
        foreach ($events as $eventStr) {
            $isNum = strlen($eventStr) > 0;
            $num = 0;
            $start = 0;
            if ($isNum && $eventStr[0] === '-') $start = 1;
            $len = strlen($eventStr);
            for ($i = $start; $i < $len; $i++) {
                if ($eventStr[$i] < '0' || $eventStr[$i] > '9') {
                    $isNum = false;
                    break;
                }
                $num = $num * 10 + (ord($eventStr[$i]) - 48);
            }
            if ($isNum && !($start === 1 && $len === 1)) {
                if ($start === 1) $num = -$num;
                $score += $num;
            } else if ($eventStr === 'W') {
                $counter++;
                if ($counter === 10) break;
            } else {
                $score++;
            }
        }
        return [$score, $counter];
    }
}
''')

add("3922_minimum_flips_to_make_binary_string_coherent", r'''<?php
// LeetCode 3922 - Minimum Flips to Make Binary String Coherent
// https://leetcode.com/problems/minimum-flips-to-make-binary-string-coherent/

class Solution {
    function minFlips($s) {
        $ones = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) if ($s[$i] === '1') $ones++;
        $answer = $ones;
        if ($ones > 0) $answer = $ones - 1;
        $zeros = $n - $ones;
        $answer = min($answer, $zeros);
        if ($n >= 2) {
            $cost = 0;
            for ($i = 0; $i < $n; $i++) {
                $want = ($i === 0 || $i === $n - 1) ? '1' : '0';
                if ($s[$i] !== $want) $cost++;
            }
            $answer = min($answer, $cost);
        }
        return $answer;
    }
}
''')

add("3923_minimum_generations_to_target_point", r'''<?php
// LeetCode 3923 - Minimum Generations to Target Point
// https://leetcode.com/problems/minimum-generations-to-target-point/

class Solution {
    function key($a, $b, $c) {
        return $a . ',' . $b . ',' . $c;
    }
    function minGenerations($points, $target) {
        $targetKey = $this->key($target[0], $target[1], $target[2]);
        $generation = [];
        $all = [];
        foreach ($points as $values) {
            $k = $this->key($values[0], $values[1], $values[2]);
            $generation[$k] = 0;
            $all[] = [$values[0], $values[1], $values[2]];
        }
        if (isset($generation[$targetKey])) return $generation[$targetKey];
        for ($current = 1; ; $current++) {
            $limit = count($all);
            $added = [];
            for ($i = 0; $i < $limit; $i++) {
                for ($j = $i + 1; $j < $limit; $j++) {
                    $pi = $all[$i];
                    $pj = $all[$j];
                    if ($pi[0] === $pj[0] && $pi[1] === $pj[1] && $pi[2] === $pj[2]) continue;
                    $p = [intdiv($pi[0] + $pj[0], 2), intdiv($pi[1] + $pj[1], 2), intdiv($pi[2] + $pj[2], 2)];
                    $k = $this->key($p[0], $p[1], $p[2]);
                    if (!isset($generation[$k])) {
                        $generation[$k] = $current;
                        $added[] = $p;
                    }
                }
            }
            if (isset($generation[$targetKey])) return $generation[$targetKey];
            if (count($added) === 0) return -1;
            foreach ($added as $p) $all[] = $p;
        }
    }
}
''')

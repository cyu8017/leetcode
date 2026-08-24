#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
SOLUTIONS = {}

def add(folder, body):
    SOLUTIONS[folder] = body


add("3720_lexicographically_smallest_permutation_greater_than_target", r'''<?php
// LeetCode 3720 - Lexicographically Smallest Permutation Greater Than Target
// https://leetcode.com/problems/lexicographically-smallest-permutation-greater-than-target/

class Solution {
    function lexGreaterPermutation($s, $target) {
        $cnt = array_fill(0, 26, 0);
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) $cnt[ord($s[$i]) - 97]++;
        $ans = array_fill(0, $n, '');
        $dfs = function($pos, $greater) use (&$dfs, &$cnt, &$ans, $n, $target) {
            if ($pos === $n) return $greater;
            $start = $greater ? 0 : (ord($target[$pos]) - 97);
            for ($c = $start; $c < 26; $c++) {
                if ($cnt[$c] === 0) continue;
                $cnt[$c]--;
                $ans[$pos] = chr(97 + $c);
                $ng = $greater || $c > (ord($target[$pos]) - 97);
                if ($dfs($pos + 1, $ng)) return true;
                $cnt[$c]++;
            }
            return false;
        };
        if ($dfs(0, false)) return implode('', $ans);
        return "";
    }
}
''')

add("3721_longest_balanced_subarray_ii", r'''<?php
// LeetCode 3721 - Longest Balanced Subarray II
// https://leetcode.com/problems/longest-balanced-subarray-ii/

class _LBNode {
    public $l = 0;
    public $r = 0;
    public $mn = 0;
    public $mx = 0;
    public $lazy = 0;
}

class _LBSegTree {
    public $tr;
    function __construct($n) {
        $this->tr = [];
        $sz = $n << 2;
        for ($i = 0; $i <= $sz; $i++) $this->tr[$i] = new _LBNode();
        $this->build(1, 0, $n);
    }
    function build($u, $l, $r) {
        $tr = $this->tr;
        $tr[$u]->l = $l; $tr[$u]->r = $r; $tr[$u]->mn = 0; $tr[$u]->mx = 0; $tr[$u]->lazy = 0;
        if ($l === $r) return;
        $mid = ($l + $r) >> 1;
        $this->build($u << 1, $l, $mid);
        $this->build($u << 1 | 1, $mid + 1, $r);
    }
    function apply($u, $v) {
        $this->tr[$u]->mn += $v;
        $this->tr[$u]->mx += $v;
        $this->tr[$u]->lazy += $v;
    }
    function pushup($u) {
        $tr = $this->tr;
        $tr[$u]->mn = min($tr[$u << 1]->mn, $tr[$u << 1 | 1]->mn);
        $tr[$u]->mx = max($tr[$u << 1]->mx, $tr[$u << 1 | 1]->mx);
    }
    function pushdown($u) {
        if ($this->tr[$u]->lazy !== 0) {
            $v = $this->tr[$u]->lazy;
            $this->apply($u << 1, $v);
            $this->apply($u << 1 | 1, $v);
            $this->tr[$u]->lazy = 0;
        }
    }
    function modify($u, $l, $r, $v) {
        $tr = $this->tr;
        if ($tr[$u]->l >= $l && $tr[$u]->r <= $r) {
            $this->apply($u, $v);
            return;
        }
        $this->pushdown($u);
        $mid = ($tr[$u]->l + $tr[$u]->r) >> 1;
        if ($l <= $mid) $this->modify($u << 1, $l, $r, $v);
        if ($r > $mid) $this->modify($u << 1 | 1, $l, $r, $v);
        $this->pushup($u);
    }
    function query($u, $target) {
        $tr = $this->tr;
        if ($tr[$u]->l === $tr[$u]->r) return $tr[$u]->l;
        $this->pushdown($u);
        $left = $u << 1;
        $right = $u << 1 | 1;
        if ($tr[$left]->mn <= $target && $target <= $tr[$left]->mx) return $this->query($left, $target);
        return $this->query($right, $target);
    }
}

class Solution {
    function longestBalanced($nums) {
        $n = count($nums);
        $st = new _LBSegTree($n);
        $last = [];
        $now = 0;
        $ans = 0;
        for ($i = 1; $i <= $n; $i++) {
            $x = $nums[$i - 1];
            $det = ($x & 1) !== 0 ? 1 : -1;
            if (isset($last[$x])) {
                $st->modify(1, $last[$x], $n, -$det);
                $now -= $det;
            }
            $last[$x] = $i;
            $st->modify(1, $i, $n, $det);
            $now += $det;
            $pos = $st->query(1, $now);
            $ans = max($ans, $i - $pos);
        }
        return $ans;
    }
}
''')

add("3722_lexicographically_smallest_string_after_reverse", r'''<?php
// LeetCode 3722 - Lexicographically Smallest String After Reverse
// https://leetcode.com/problems/lexicographically-smallest-string-after-reverse/

class Solution {
    function lexSmallest($s) {
        $ans = $s;
        $n = strlen($s);
        $reverse = function(&$a, $l, $r) {
            for ($i = $l, $j = $r - 1; $i < $j; $i++, $j--) {
                $t = $a[$i]; $a[$i] = $a[$j]; $a[$j] = $t;
            }
        };
        for ($k = 1; $k <= $n; $k++) {
            $a1 = str_split($s);
            $reverse($a1, 0, $k);
            $t1 = implode('', $a1);
            $a2 = str_split($s);
            $reverse($a2, $n - $k, $n);
            $t2 = implode('', $a2);
            if ($t1 < $ans) $ans = $t1;
            if ($t2 < $ans) $ans = $t2;
        }
        return $ans;
    }
}
''')

add("3723_maximize_sum_of_squares_of_digits", r'''<?php
// LeetCode 3723 - Maximize Sum of Squares of Digits
// https://leetcode.com/problems/maximize-sum-of-squares-of-digits/

class Solution {
    function maxSumOfSquares($num, $sum) {
        if ($num * 9 < $sum) return "";
        $k = intdiv($sum, 9);
        $s = $sum % 9;
        $ans = str_repeat('9', $k);
        if ($s > 0) $ans .= chr(48 + $s);
        while (strlen($ans) < $num) $ans .= '0';
        return $ans;
    }
}
''')

add("3724_minimum_operations_to_transform_array", r'''<?php
// LeetCode 3724 - Minimum Operations to Transform Array
// https://leetcode.com/problems/minimum-operations-to-transform-array/

class Solution {
    function minOperations($nums1, $nums2) {
        $ans = 1;
        $n = count($nums1);
        $ok = false;
        $d = 1 << 30;
        for ($i = 0; $i < $n; $i++) {
            $x = max($nums1[$i], $nums2[$i]);
            $y = min($nums1[$i], $nums2[$i]);
            $ans += $x - $y;
            $d = min($d, min(abs($x - $nums2[$n]), abs($y - $nums2[$n])));
            if ($nums2[$n] >= $y && $nums2[$n] <= $x) $ok = true;
        }
        if (!$ok) $ans += $d;
        return $ans;
    }
}
''')

add("3725_count_ways_to_choose_coprime_integers_from_rows", r'''<?php
// LeetCode 3725 - Count Ways to Choose Coprime Integers from Rows
// https://leetcode.com/problems/count-ways-to-choose-coprime-integers-from-rows/

class Solution {
    function countCoprime($mat) {
        $MOD = 1000000007;
        $m = count($mat);
        $gcd = function($a, $b) {
            while ($b !== 0) {
                $t = $a % $b;
                $a = $b;
                $b = $t;
            }
            return $a;
        };
        $dp = [];
        foreach ($mat[0] as $v) {
            if (!isset($dp[$v])) $dp[$v] = 0;
            $dp[$v]++;
        }
        for ($i = 1; $i < $m; $i++) {
            $ndp = [];
            foreach ($mat[$i] as $v) {
                foreach ($dp as $key => $val) {
                    $ng = $gcd($key, $v);
                    if (!isset($ndp[$ng])) $ndp[$ng] = 0;
                    $ndp[$ng] = ($ndp[$ng] + $val) % $MOD;
                }
            }
            $dp = $ndp;
        }
        return isset($dp[1]) ? $dp[1] : 0;
    }
}
''')

add("3726_remove_zeros_in_decimal_representation", r'''<?php
// LeetCode 3726 - Remove Zeros in Decimal Representation
// https://leetcode.com/problems/remove-zeros-in-decimal-representation/

class Solution {
    function removeZeros($n) {
        $ans = 0;
        $k = 1;
        while ($n > 0) {
            $x = $n % 10;
            if ($x > 0) {
                $ans = $k * $x + $ans;
                $k *= 10;
            }
            $n = intdiv($n, 10);
        }
        return $ans;
    }
}
''')

add("3727_maximum_alternating_sum_of_squares", r'''<?php
// LeetCode 3727 - Maximum Alternating Sum of Squares
// https://leetcode.com/problems/maximum-alternating-sum-of-squares/

class Solution {
    function maxAlternatingSum($nums) {
        $a = [];
        foreach ($nums as $x) $a[] = $x * $x;
        sort($a);
        $m = intdiv(count($a), 2);
        $ans = 0;
        for ($i = 0; $i < $m; $i++) $ans -= $a[$i];
        for ($i = $m; $i < count($a); $i++) $ans += $a[$i];
        return $ans;
    }
}
''')

add("3728_stable_subarrays_with_equal_boundary_and_interior_sum", r'''<?php
// LeetCode 3728 - Stable Subarrays With Equal Boundary and Interior Sum
// https://leetcode.com/problems/stable-subarrays-with-equal-boundary-and-interior-sum/

class Solution {
    function countStableSubarrays($capacity) {
        $n = count($capacity);
        $s = array_fill(0, $n + 1, 0);
        for ($i = 1; $i <= $n; $i++) $s[$i] = $s[$i - 1] + $capacity[$i - 1];
        $cnt = [];
        $ans = 0;
        for ($r = 2; $r < $n; $r++) {
            $l = $r - 2;
            $keyL = $capacity[$l] . "#" . ($capacity[$l] + $s[$l + 1]);
            if (!isset($cnt[$keyL])) $cnt[$keyL] = 0;
            $cnt[$keyL]++;
            $keyR = $capacity[$r] . "#" . $s[$r];
            $ans += isset($cnt[$keyR]) ? $cnt[$keyR] : 0;
        }
        return $ans;
    }
}
''')

add("3729_count_distinct_subarrays_divisible_by_k_in_sorted_array", r'''<?php
// LeetCode 3729 - Count Distinct Subarrays Divisible by K in Sorted Array
// https://leetcode.com/problems/count-distinct-subarrays-divisible-by-k-in-sorted-array/

class Solution {
    function numGoodSubarrays($nums, $k) {
        $ans = 0;
        $s = 0;
        $cnt = [];
        $cnt[0] = 1;
        foreach ($nums as $x) {
            $s = ($s + $x) % $k;
            $ans += isset($cnt[$s]) ? $cnt[$s] : 0;
            if (!isset($cnt[$s])) $cnt[$s] = 0;
            $cnt[$s]++;
        }
        $n = count($nums);
        for ($i = 0; $i < $n; ) {
            $j = $i + 1;
            while ($j < $n && $nums[$j] === $nums[$i]) $j++;
            $m = $j - $i;
            for ($h = 1; $h <= $m; $h++) {
                if (($nums[$i] * $h) % $k === 0) $ans -= ($m - $h);
            }
            $i = $j;
        }
        return $ans;
    }
}
''')

add("3730_maximum_calories_burnt_from_jumps", r'''<?php
// LeetCode 3730 - Maximum Calories Burnt from Jumps
// https://leetcode.com/problems/maximum-calories-burnt-from-jumps/

class Solution {
    function maxCaloriesBurnt($heights) {
        sort($heights);
        $ans = 0;
        $pre = 0;
        $l = 0;
        $r = count($heights) - 1;
        while ($l < $r) {
            $d1 = $heights[$r] - $pre;
            $ans += $d1 * $d1;
            $d2 = $heights[$l] - $heights[$r];
            $ans += $d2 * $d2;
            $pre = $heights[$l];
            $l++;
            $r--;
        }
        $d = $heights[$r] - $pre;
        $ans += $d * $d;
        return $ans;
    }
}
''')

add("3731_find_missing_elements", r'''<?php
// LeetCode 3731 - Find Missing Elements
// https://leetcode.com/problems/find-missing-elements/

class Solution {
    function findMissingElements($nums) {
        $mn = 100;
        $mx = 0;
        $s = [];
        foreach ($nums as $x) {
            $mn = min($mn, $x);
            $mx = max($mx, $x);
            $s[$x] = true;
        }
        $ans = [];
        for ($x = $mn + 1; $x < $mx; $x++) {
            if (!isset($s[$x])) $ans[] = $x;
        }
        return $ans;
    }
}
''')

add("3732_maximum_product_of_three_elements_after_one_replacement", r'''<?php
// LeetCode 3732 - Maximum Product of Three Elements After One Replacement
// https://leetcode.com/problems/maximum-product-of-three-elements-after-one-replacement/

class Solution {
    function maxProduct($nums) {
        $a = $nums;
        sort($a);
        $n = count($a);
        $A = $a[0]; $B = $a[1]; $C = $a[$n - 2]; $D = $a[$n - 1];
        $x = 100000;
        return max(max($A * $B * $x, $C * $D * $x), -$A * $D * $x);
    }
}
''')

add("3733_minimum_time_to_complete_all_deliveries", r'''<?php
// LeetCode 3733 - Minimum Time to Complete All Deliveries
// https://leetcode.com/problems/minimum-time-to-complete-all-deliveries/

class Solution {
    function minimumTime($d, $r) {
        $ok = function($T) use ($d, $r) {
            $w0 = $T - intdiv($T, $r[0]);
            $w1 = $T - intdiv($T, $r[1]);
            return $w0 + $w1 >= $d[0] + $d[1];
        };
        $lo = 1;
        $hi = 9007199254740991;
        while ($lo < $hi) {
            $mid = $lo + intdiv($hi - $lo, 2);
            if ($ok($mid)) $hi = $mid;
            else $lo = $mid + 1;
        }
        return $lo;
    }
}
''')

add("3734_lexicographically_smallest_palindromic_permutation_greater_than_target", r'''<?php
// LeetCode 3734 - Lexicographically Smallest Palindromic Permutation Greater Than Target
// https://leetcode.com/problems/lexicographically-smallest-palindromic-permutation-greater-than-target/

class Solution {
    function lexPalindromicPermutation($s, $target) {
        $cnt = array_fill(0, 26, 0);
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) $cnt[ord($s[$i]) - 97]++;
        $odd = 0;
        $mid = -1;
        for ($i = 0; $i < 26; $i++) {
            if ($cnt[$i] % 2 === 1) { $odd++; $mid = $i; }
        }
        if ($odd > 1) return "";
        $half = array_fill(0, 26, 0);
        for ($i = 0; $i < 26; $i++) $half[$i] = intdiv($cnt[$i], 2);
        $halfLen = intdiv($n, 2);
        $left = array_fill(0, $halfLen, '');
        $dfs = function($pos, $greater) use (&$dfs, &$half, &$left, $halfLen, $mid, $target) {
            if ($pos === $halfLen) {
                if ($mid >= 0) {
                    if ($greater) return true;
                    return chr(97 + $mid) > $target[$halfLen];
                }
                return $greater;
            }
            $start = $greater ? 0 : (ord($target[$pos]) - 97);
            for ($c = $start; $c < 26; $c++) {
                if ($half[$c] === 0) continue;
                $half[$c]--;
                $left[$pos] = chr(97 + $c);
                if ($dfs($pos + 1, $greater || $c > (ord($target[$pos]) - 97))) return true;
                $half[$c]++;
            }
            return false;
        };
        if (!$dfs(0, false)) return "";
        $res = implode('', $left);
        if ($mid >= 0) $res .= chr(97 + $mid);
        for ($i = $halfLen - 1; $i >= 0; $i--) $res .= $left[$i];
        if ($res <= $target) return "";
        return $res;
    }
}
''')

add("3735_lexicographically_smallest_string_after_reverse_ii", r'''<?php
// LeetCode 3735 - Lexicographically Smallest String After Reverse II
// https://leetcode.com/problems/lexicographically-smallest-string-after-reverse-ii/

class Solution {
    function lexSmallest($s) {
        $n = strlen($s);
        $best = $s;
        $reverse = function(&$a, $l, $r) {
            for ($i = $l, $j = $r - 1; $i < $j; $i++, $j--) {
                $t = $a[$i]; $a[$i] = $a[$j]; $a[$j] = $t;
            }
        };
        for ($i = 1; $i <= $n; $i++) {
            $t = str_split($s);
            $reverse($t, 0, $i);
            $ts = implode('', $t);
            if ($ts < $best) $best = $ts;
        }
        for ($i = 0; $i < $n; $i++) {
            $t = str_split($s);
            $reverse($t, $i, $n);
            $ts = implode('', $t);
            if ($ts < $best) $best = $ts;
        }
        return $best;
    }
}
''')

add("3736_minimum_moves_to_equal_array_elements_iii", r'''<?php
// LeetCode 3736 - Minimum Moves to Equal Array Elements III
// https://leetcode.com/problems/minimum-moves-to-equal-array-elements-iii/

class Solution {
    function minMoves($nums) {
        $mx = 0;
        $s = 0;
        foreach ($nums as $x) {
            $mx = max($mx, $x);
            $s += $x;
        }
        return $mx * count($nums) - $s;
    }
}
''')

add("3737_count_subarrays_with_majority_element_i", r'''<?php
// LeetCode 3737 - Count Subarrays With Majority Element I
// https://leetcode.com/problems/count-subarrays-with-majority-element-i/

class Solution {
    function countMajoritySubarrays($nums, $target) {
        $n = count($nums);
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            $cnt = 0;
            for ($j = $i; $j < $n; $j++) {
                if ($nums[$j] === $target) $cnt++;
                if ($cnt * 2 > $j - $i + 1) $ans++;
            }
        }
        return $ans;
    }
}
''')

add("3738_longest_non_decreasing_subarray_after_replacing_at_most_one_element", r'''<?php
// LeetCode 3738 - Longest Non-Decreasing Subarray After Replacing at Most One Element
// https://leetcode.com/problems/longest-non-decreasing-subarray-after-replacing-at-most-one-element/

class Solution {
    function longestSubarray($nums) {
        $n = count($nums);
        $left = array_fill(0, $n, 1);
        $right = array_fill(0, $n, 1);
        for ($i = 1; $i < $n; $i++) {
            if ($nums[$i] >= $nums[$i - 1]) $left[$i] = $left[$i - 1] + 1;
        }
        for ($i = $n - 2; $i >= 0; $i--) {
            if ($nums[$i] <= $nums[$i + 1]) $right[$i] = $right[$i + 1] + 1;
        }
        $ans = 0;
        foreach ($left as $v) $ans = max($ans, $v);
        for ($i = 0; $i < $n; $i++) {
            $a = $i > 0 ? $left[$i - 1] : 0;
            $b = $i + 1 < $n ? $right[$i + 1] : 0;
            if ($i > 0 && $i + 1 < $n && $nums[$i - 1] > $nums[$i + 1]) {
                $ans = max($ans, max($a + 1, $b + 1));
            } else {
                $ans = max($ans, $a + $b + 1);
            }
        }
        return $ans;
    }
}
''')

add("3739_count_subarrays_with_majority_element_ii", r'''<?php
// LeetCode 3739 - Count Subarrays With Majority Element II
// https://leetcode.com/problems/count-subarrays-with-majority-element-ii/

class _CMBIT {
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
    function countMajoritySubarrays($nums, $target) {
        $n = count($nums);
        $tree = new _CMBIT(2 * $n + 1);
        $s = $n + 1;
        $tree->update($s, 1);
        $ans = 0;
        foreach ($nums as $x) {
            if ($x === $target) $s++;
            else $s--;
            $ans += $tree->query($s - 1);
            $tree->update($s, 1);
        }
        return $ans;
    }
}
''')

add("3740_minimum_distance_between_three_equal_elements_i", r'''<?php
// LeetCode 3740 - Minimum Distance Between Three Equal Elements I
// https://leetcode.com/problems/minimum-distance-between-three-equal-elements-i/

class Solution {
    function minimumDistance($nums) {
        $g = [];
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            if (!isset($g[$nums[$i]])) $g[$nums[$i]] = [];
            $g[$nums[$i]][] = $i;
        }
        $inf = 1 << 30;
        $ans = $inf;
        foreach ($g as $ls) {
            $m = count($ls);
            for ($h = 0; $h < $m - 2; $h++) {
                $ans = min($ans, ($ls[$h + 2] - $ls[$h]) * 2);
            }
        }
        return $ans === $inf ? -1 : $ans;
    }
}
''')

add("3741_minimum_distance_between_three_equal_elements_ii", r'''<?php
// LeetCode 3741 - Minimum Distance Between Three Equal Elements II
// https://leetcode.com/problems/minimum-distance-between-three-equal-elements-ii/

class Solution {
    function minimumDistance($nums) {
        $g = [];
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            if (!isset($g[$nums[$i]])) $g[$nums[$i]] = [];
            $g[$nums[$i]][] = $i;
        }
        $inf = 1 << 30;
        $ans = $inf;
        foreach ($g as $ls) {
            $m = count($ls);
            for ($h = 0; $h < $m - 2; $h++) {
                $ans = min($ans, ($ls[$h + 2] - $ls[$h]) * 2);
            }
        }
        return $ans === $inf ? -1 : $ans;
    }
}
''')

add("3742_maximum_path_score_in_a_grid", r'''<?php
// LeetCode 3742 - Maximum Path Score in a Grid
// https://leetcode.com/problems/maximum-path-score-in-a-grid/

class Solution {
    function maxPathScore($grid, $k) {
        $INF = 1 << 30;
        $m = count($grid);
        $n = count($grid[0]);
        $f = [];
        for ($i = 0; $i < $m; $i++) {
            $f[$i] = [];
            for ($j = 0; $j < $n; $j++) $f[$i][$j] = array_fill(0, $k + 1, -1);
        }
        $dfs = function($i, $j, $kk) use (&$dfs, &$f, $grid, $INF) {
            if ($i < 0 || $j < 0 || $kk < 0) return -$INF;
            if ($i === 0 && $j === 0) return 0;
            if ($f[$i][$j][$kk] !== -1) return $f[$i][$j][$kk];
            $res = $grid[$i][$j];
            $nk = $kk;
            if ($grid[$i][$j] !== 0) $nk--;
            $a = $dfs($i - 1, $j, $nk);
            $b = $dfs($i, $j - 1, $nk);
            $res += max($a, $b);
            return $f[$i][$j][$kk] = $res;
        };
        $ans = $dfs($m - 1, $n - 1, $k);
        return $ans < 0 ? -1 : $ans;
    }
}
''')

add("3743_maximize_cyclic_partition_score", r'''<?php
// LeetCode 3743 - Maximize Cyclic Partition Score
// https://leetcode.com/problems/maximize-cyclic-partition-score/

class Solution {
    function maximumScore($nums, $k) {
        $n = count($nums);
        $a = array_merge($nums, $nums);
        if ($k > $n) $k = $n;
        $best = 0;
        $NEG = -9007199254740991;
        for ($start = 0; $start < $n; $start++) {
            $seg = array_slice($a, $start, $n);
            $dp = [];
            for ($i = 0; $i <= $n; $i++) $dp[$i] = array_fill(0, $k + 1, $NEG);
            $dp[0][0] = 0;
            for ($i = 1; $i <= $n; $i++) {
                for ($j = 1; $j <= $k && $j <= $i; $j++) {
                    $mx = $NEG;
                    for ($t = $i; $t >= $j; $t--) {
                        if ($seg[$t - 1] > $mx) $mx = $seg[$t - 1];
                        if ($dp[$t - 1][$j - 1] > $NEG) {
                            $cand = $dp[$t - 1][$j - 1] + $mx;
                            if ($cand > $dp[$i][$j]) $dp[$i][$j] = $cand;
                        }
                    }
                }
            }
            if ($dp[$n][$k] > $best) $best = $dp[$n][$k];
        }
        return $best;
    }
}
''')

add("3744_find_kth_character_in_expanded_string", r'''<?php
// LeetCode 3744 - Find Kth Character in Expanded String
// https://leetcode.com/problems/find-kth-character-in-expanded-string/

class Solution {
    function kthCharacter($s, $k) {
        $words = preg_split('/\s+/', trim($s));
        foreach ($words as $w) {
            $m = (1 + strlen($w)) * strlen($w) / 2;
            if ($k == $m) return ' ';
            if ($k > $m) {
                $k -= $m + 1;
            } else {
                $cur = 0;
                for ($i = 0; ; $i++) {
                    $cur += $i + 1;
                    if ($k < $cur) return $w[$i];
                }
            }
        }
        return ' ';
    }
}
''')


def main():
    for folder, body in SOLUTIONS.items():
        path = ROOT / folder / "solution.php"
        path.write_text(body, encoding="utf-8", newline="\n")
        print("wrote", folder)
    print("count", len(SOLUTIONS))

if __name__ == "__main__":
    main()

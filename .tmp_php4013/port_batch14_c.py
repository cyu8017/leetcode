#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
SOLUTIONS = {}

def add(folder, body):
    SOLUTIONS[folder] = body if body.endswith("\n") else body + "\n"

add("3125_maximum_number_that_makes_result_of_bitwise_and_zero", r'''<?php
// LeetCode 3125 - Maximum Number That Makes Result of Bitwise AND Zero
// https://leetcode.com/problems/maximum-number-that-makes-result-of-bitwise-and-zero/

class Solution {
    function maxNumber($n) {
        $len = 0;
        $x = $n;
        while ($x > 0) { $len++; $x >>= 1; }
        return (1 << ($len - 1)) - 1;
    }
}
''')

add("3127_make_a_square_with_the_same_color", r'''<?php
// LeetCode 3127 - Make a Square with the Same Color
// https://leetcode.com/problems/make-a-square-with-the-same-color/

class Solution {
    function canMakeSquare($grid) {
        $dirs = [0, 0, 1, 1, 0];
        for ($i = 0; $i < 2; $i++) {
            for ($j = 0; $j < 2; $j++) {
                $cnt1 = 0;
                $cnt2 = 0;
                for ($k = 0; $k < 4; $k++) {
                    $x = $i + $dirs[$k];
                    $y = $j + $dirs[$k + 1];
                    if ($grid[$x][$y] === "W") $cnt1++;
                    else $cnt2++;
                }
                if ($cnt1 !== $cnt2) return true;
            }
        }
        return false;
    }
}
''')

add("3128_right_triangles", r'''<?php
// LeetCode 3128 - Right Triangles
// https://leetcode.com/problems/right-triangles/

class Solution {
    function numberOfRightTriangles($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        $rows = array_fill(0, $m, 0);
        $cols = array_fill(0, $n, 0);
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                $rows[$i] += $grid[$i][$j];
                $cols[$j] += $grid[$i][$j];
            }
        }
        $ans = 0;
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if ($grid[$i][$j] === 1)
                    $ans += ($rows[$i] - 1) * ($cols[$j] - 1);
            }
        }
        return $ans;
    }
}
''')

add("3129_find_all_possible_stable_binary_arrays_i", r'''<?php
// LeetCode 3129 - Find All Possible Stable Binary Arrays I
// https://leetcode.com/problems/find-all-possible-stable-binary-arrays-i/

class Solution {
    public $limit;
    public $f;
    function numberOfStableArrays($zero, $one, $limit) {
        $MOD = 1000000007;
        $this->limit = $limit;
        $this->f = [];
        for ($i = 0; $i <= $zero; $i++) {
            $this->f[$i] = [];
            for ($j = 0; $j <= $one; $j++) $this->f[$i][$j] = [-1, -1];
        }
        return ($this->dfs($zero, $one, 0) + $this->dfs($zero, $one, 1)) % $MOD;
    }
    function dfs($i, $j, $k) {
        $MOD = 1000000007;
        $limit = $this->limit;
        if ($i < 0 || $j < 0) return 0;
        if ($i === 0) return ($k === 1 && $j <= $limit) ? 1 : 0;
        if ($j === 0) return ($k === 0 && $i <= $limit) ? 1 : 0;
        if ($this->f[$i][$j][$k] !== -1) return $this->f[$i][$j][$k];
        if ($k === 0)
            $res = ($this->dfs($i - 1, $j, 0) + $this->dfs($i - 1, $j, 1) - $this->dfs($i - $limit - 1, $j, 1) + $MOD) % $MOD;
        else
            $res = ($this->dfs($i, $j - 1, 0) + $this->dfs($i, $j - 1, 1) - $this->dfs($i, $j - $limit - 1, 0) + $MOD) % $MOD;
        return $this->f[$i][$j][$k] = $res;
    }
}
''')

add("3130_find_all_possible_stable_binary_arrays_ii", r'''<?php
// LeetCode 3130 - Find All Possible Stable Binary Arrays II
// https://leetcode.com/problems/find-all-possible-stable-binary-arrays-ii/

class Solution {
    public $limit;
    public $f;
    function numberOfStableArrays($zero, $one, $limit) {
        $MOD = 1000000007;
        $this->limit = $limit;
        $this->f = [];
        for ($i = 0; $i <= $zero; $i++) {
            $this->f[$i] = [];
            for ($j = 0; $j <= $one; $j++) $this->f[$i][$j] = [-1, -1];
        }
        return ($this->dfs($zero, $one, 0) + $this->dfs($zero, $one, 1)) % $MOD;
    }
    function dfs($i, $j, $k) {
        $MOD = 1000000007;
        $limit = $this->limit;
        if ($i < 0 || $j < 0) return 0;
        if ($i === 0) return ($k === 1 && $j <= $limit) ? 1 : 0;
        if ($j === 0) return ($k === 0 && $i <= $limit) ? 1 : 0;
        if ($this->f[$i][$j][$k] !== -1) return $this->f[$i][$j][$k];
        if ($k === 0)
            $res = ($this->dfs($i - 1, $j, 0) + $this->dfs($i - 1, $j, 1) - $this->dfs($i - $limit - 1, $j, 1) + $MOD) % $MOD;
        else
            $res = ($this->dfs($i, $j - 1, 0) + $this->dfs($i, $j - 1, 1) - $this->dfs($i, $j - $limit - 1, 0) + $MOD) % $MOD;
        return $this->f[$i][$j][$k] = $res;
    }
}
''')

add("3131_find_the_integer_added_to_array_i", r'''<?php
// LeetCode 3131 - Find the Integer Added to Array I
// https://leetcode.com/problems/find-the-integer-added-to-array-i/

class Solution {
    function addedInteger($nums1, $nums2) {
        return min($nums2) - min($nums1);
    }
}
''')

add("3132_find_the_integer_added_to_array_ii", r'''<?php
// LeetCode 3132 - Find the Integer Added to Array II
// https://leetcode.com/problems/find-the-integer-added-to-array-ii/

class Solution {
    public $nums1;
    public $nums2;
    function minimumAddedInteger($nums1, $nums2) {
        sort($nums1);
        sort($nums2);
        $this->nums1 = $nums1;
        $this->nums2 = $nums2;
        $ans = 1 << 30;
        for ($t = 0; $t < 3; $t++) {
            $x = $nums2[0] - $nums1[$t];
            if ($this->ok($x)) $ans = min($ans, $x);
        }
        return $ans;
    }
    function ok($x) {
        $i = 0;
        $j = 0;
        $cnt = 0;
        $n1 = count($this->nums1);
        $n2 = count($this->nums2);
        while ($i < $n1 && $j < $n2) {
            if ($this->nums2[$j] - $this->nums1[$i] !== $x) $cnt++;
            else $j++;
            $i++;
        }
        return $cnt <= 2;
    }
}
''')

add("3133_minimum_array_end", r'''<?php
// LeetCode 3133 - Minimum Array End
// https://leetcode.com/problems/minimum-array-end/

class Solution {
    function minEnd($n, $x) {
        $n--;
        $ans = $x;
        for ($i = 0; $i < 31; $i++) {
            if ((($x >> $i) & 1) === 0) {
                $ans |= ($n & 1) << $i;
                $n >>= 1;
            }
        }
        $ans |= $n << 31;
        return $ans;
    }
}
''')

add("3134_find_the_median_of_the_uniqueness_array", r'''<?php
// LeetCode 3134 - Find the Median of the Uniqueness Array
// https://leetcode.com/problems/find-the-median-of-the-uniqueness-array/

class Solution {
    public $nums;
    public $n;
    public $m;
    function medianOfUniquenessArray($nums) {
        $this->nums = $nums;
        $this->n = count($nums);
        $this->m = (1 + $this->n) * $this->n / 2;
        $lo = 1;
        $hi = $this->n;
        while ($lo < $hi) {
            $mid = $lo + intdiv($hi - $lo, 2);
            if ($this->check($mid)) $hi = $mid;
            else $lo = $mid + 1;
        }
        return $lo;
    }
    function check($mx) {
        $cnt = [];
        $l = 0;
        $k = 0;
        $n = $this->n;
        for ($r = 0; $r < $n; $r++) {
            $x = $this->nums[$r];
            $cnt[$x] = ($cnt[$x] ?? 0) + 1;
            while (count($cnt) > $mx) {
                $y = $this->nums[$l++];
                $nv = $cnt[$y] - 1;
                if ($nv === 0) unset($cnt[$y]);
                else $cnt[$y] = $nv;
            }
            $k += $r - $l + 1;
            if ($k >= intdiv($this->m + 1, 2)) return true;
        }
        return false;
    }
}
''')

add("3135_equalize_strings_by_adding_or_removing_characters_at_ends", r'''<?php
// LeetCode 3135 - Equalize Strings by Adding or Removing Characters at Ends
// https://leetcode.com/problems/equalize-strings-by-adding-or-removing-characters-at-ends/

class Solution {
    function minOperations($initial, $target) {
        $m = strlen($initial);
        $n = strlen($target);
        $f = [];
        for ($i = 0; $i <= $m; $i++) $f[] = array_fill(0, $n + 1, 0);
        $mx = 0;
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if ($initial[$i] === $target[$j]) {
                    $f[$i + 1][$j + 1] = $f[$i][$j] + 1;
                    $mx = max($mx, $f[$i + 1][$j + 1]);
                }
            }
        }
        return $m + $n - 2 * $mx;
    }
}
''')

add("3136_valid_word", r'''<?php
// LeetCode 3136 - Valid Word
// https://leetcode.com/problems/valid-word/

class Solution {
    function isValid($word) {
        if (strlen($word) < 3) return false;
        $hasVowel = false;
        $hasConsonant = false;
        $vs = array_fill(0, 26, false);
        foreach (str_split("aeiou") as $c) $vs[ord($c) - 97] = true;
        $n = strlen($word);
        for ($i = 0; $i < $n; $i++) {
            $c = $word[$i];
            if (ctype_alpha($c)) {
                $lower = strtolower($c);
                if ($vs[ord($lower) - 97]) $hasVowel = true;
                else $hasConsonant = true;
            } else if (!ctype_digit($c)) {
                return false;
            }
        }
        return $hasVowel && $hasConsonant;
    }
}
''')

add("3137_minimum_number_of_operations_to_make_word_k_periodic", r'''<?php
// LeetCode 3137 - Minimum Number of Operations to Make Word K-Periodic
// https://leetcode.com/problems/minimum-number-of-operations-to-make-word-k-periodic/

class Solution {
    function minimumOperationsToMakeKPeriodic($word, $k) {
        $cnt = [];
        $n = strlen($word);
        $mx = 0;
        for ($i = 0; $i < $n; $i += $k) {
            $s = substr($word, $i, $k);
            $v = ($cnt[$s] ?? 0) + 1;
            $cnt[$s] = $v;
            $mx = max($mx, $v);
        }
        return intdiv($n, $k) - $mx;
    }
}
''')

add("3138_minimum_length_of_anagram_concatenation", r'''<?php
// LeetCode 3138 - Minimum Length of Anagram Concatenation
// https://leetcode.com/problems/minimum-length-of-anagram-concatenation/

class Solution {
    public $s;
    public $n;
    public $cnt;
    function minAnagramLength($s) {
        $this->s = $s;
        $this->n = strlen($s);
        $this->cnt = array_fill(0, 26, 0);
        for ($i = 0; $i < $this->n; $i++) $this->cnt[ord($s[$i]) - 97]++;
        for ($i = 1; ; $i++) {
            if ($this->n % $i === 0 && $this->check($i)) return $i;
        }
    }
    function check($k) {
        $n = $this->n;
        $s = $this->s;
        for ($i = 0; $i < $n; $i += $k) {
            $cnt1 = array_fill(0, 26, 0);
            for ($j = $i; $j < $i + $k; $j++) $cnt1[ord($s[$j]) - 97]++;
            for ($j = 0; $j < 26; $j++) {
                if ($cnt1[$j] * intdiv($n, $k) !== $this->cnt[$j]) return false;
            }
        }
        return true;
    }
}
''')

add("3139_minimum_cost_to_equalize_array", r'''<?php
// LeetCode 3139 - Minimum Cost to Equalize Array
// https://leetcode.com/problems/minimum-cost-to-equalize-array/

class Solution {
    function minCostToEqualizeArray($nums, $cost1, $cost2) {
        $MOD = 1000000007;
        $n = count($nums);
        $minNum = min($nums);
        $maxNum = max($nums);
        $sum = array_sum($nums);
        if ($cost1 * 2 <= $cost2 || $n < 3) {
            $totalGap = $maxNum * $n - $sum;
            return ($cost1 * $totalGap) % $MOD;
        }
        $ans = PHP_INT_MAX;
        for ($target = $maxNum; $target < 2 * $maxNum; $target++) {
            $maxGap = $target - $minNum;
            $totalGap = $target * $n - $sum;
            $pairs = intdiv($totalGap, 2);
            $alt = $totalGap - $maxGap;
            if ($alt < $pairs) $pairs = $alt;
            $cost = $cost1 * ($totalGap - 2 * $pairs) + $cost2 * $pairs;
            $ans = min($ans, $cost);
        }
        return $ans % $MOD;
    }
}
''')

add("3141_maximum_hamming_distances", r'''<?php
// LeetCode 3141 - Maximum Hamming Distances
// https://leetcode.com/problems/maximum-hamming-distances/

class Solution {
    function maxHammingDistances($nums, $m) {
        $dist = array_fill(0, 1 << $m, -1);
        $q = [];
        foreach ($nums as $x) {
            $dist[$x] = 0;
            $q[] = $x;
        }
        for ($k = 1; $q; $k++) {
            $t = [];
            foreach ($q as $x) {
                for ($i = 0; $i < $m; $i++) {
                    $y = $x ^ (1 << $i);
                    if ($dist[$y] === -1) {
                        $dist[$y] = $k;
                        $t[] = $y;
                    }
                }
            }
            $q = $t;
        }
        $ans = $nums;
        $mask = (1 << $m) - 1;
        for ($i = 0; $i < count($ans); $i++) {
            $x = $ans[$i];
            $ans[$i] = $m - $dist[$x ^ $mask];
        }
        return $ans;
    }
}
''')

add("3142_check_if_grid_satisfies_conditions", r'''<?php
// LeetCode 3142 - Check if Grid Satisfies Conditions
// https://leetcode.com/problems/check-if-grid-satisfies-conditions/

class Solution {
    function satisfiesConditions($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                $x = $grid[$i][$j];
                if ($i + 1 < $m && $x !== $grid[$i + 1][$j]) return false;
                if ($j + 1 < $n && $x === $grid[$i][$j + 1]) return false;
            }
        }
        return true;
    }
}
''')

add("3143_maximum_points_inside_the_square", r'''<?php
// LeetCode 3143 - Maximum Points Inside the Square
// https://leetcode.com/problems/maximum-points-inside-the-square/

class Solution {
    function maxPointsInsideSquare($points, $s) {
        $g = [];
        $keys = [];
        for ($i = 0; $i < count($points); $i++) {
            $key = max(abs($points[$i][0]), abs($points[$i][1]));
            if (!isset($g[$key])) {
                $g[$key] = [];
                $lo = 0;
                $hi = count($keys);
                while ($lo < $hi) {
                    $mid = ($lo + $hi) >> 1;
                    if ($keys[$mid] < $key) $lo = $mid + 1;
                    else $hi = $mid;
                }
                array_splice($keys, $lo, 0, [$key]);
            }
            $g[$key][] = $i;
        }
        $vis = array_fill(0, 26, false);
        $ans = 0;
        foreach ($keys as $key) {
            $list = $g[$key];
            foreach ($list as $i) {
                $j = ord($s[$i]) - 97;
                if ($vis[$j]) return $ans;
                $vis[$j] = true;
            }
            $ans += count($list);
        }
        return $ans;
    }
}
''')

add("3144_minimum_substring_partition_of_equal_character_frequency", r'''<?php
// LeetCode 3144 - Minimum Substring Partition of Equal Character Frequency
// https://leetcode.com/problems/minimum-substring-partition-of-equal-character-frequency/

class Solution {
    public $s;
    public $n;
    public $memo;
    function minimumSubstringsInPartition($s) {
        $this->s = $s;
        $this->n = strlen($s);
        $this->memo = array_fill(0, $this->n, -1);
        return $this->dfs(0);
    }
    function dfs($i) {
        $n = $this->n;
        if ($i >= $n) return 0;
        if ($this->memo[$i] !== -1) return $this->memo[$i];
        $cnt = array_fill(0, 26, 0);
        $freq = [];
        $this->memo[$i] = $n - $i;
        for ($j = $i; $j < $n; $j++) {
            $k = ord($this->s[$j]) - 97;
            if ($cnt[$k] > 0) {
                $c = $cnt[$k];
                $nv = $freq[$c] - 1;
                if ($nv === 0) unset($freq[$c]);
                else $freq[$c] = $nv;
            }
            $cnt[$k]++;
            $freq[$cnt[$k]] = ($freq[$cnt[$k]] ?? 0) + 1;
            if (count($freq) === 1) {
                $this->memo[$i] = min($this->memo[$i], 1 + $this->dfs($j + 1));
            }
        }
        return $this->memo[$i];
    }
}
''')

add("3145_find_products_of_elements_of_big_array", r'''<?php
// LeetCode 3145 - Find Products of Elements of Big Array
// https://leetcode.com/problems/find-products-of-elements-of-big-array/

class Solution {
    public $cnt;
    public $s;
    function findProductsOfElements($queries) {
        $M = 50;
        $this->cnt = array_fill(0, $M + 1, 0);
        $this->s = array_fill(0, $M + 1, 0);
        $p = 1;
        for ($i = 1; $i <= $M; $i++) {
            $this->cnt[$i] = $this->cnt[$i - 1] * 2 + $p;
            $this->s[$i] = $this->s[$i - 1] * 2 + $p * ($i - 1);
            $p *= 2;
        }
        $ans = [];
        for ($i = 0; $i < count($queries); $i++) {
            $left = $queries[$i][0];
            $right = $queries[$i][1];
            $mod = $queries[$i][2];
            $power = $this->f($right + 1) - $this->f($left);
            $ans[$i] = $this->qpow(2, $power, $mod);
        }
        return $ans;
    }
    function numIdxAndSum($x) {
        $idx = 0;
        $totalSum = 0;
        while ($x > 0) {
            $i = 0;
            $t = $x;
            while ($t > 1) { $t >>= 1; $i++; }
            $idx += $this->cnt[$i];
            $totalSum += $this->s[$i];
            $x -= 1 << $i;
            $totalSum += ($x + 1) * $i;
            $idx += $x + 1;
        }
        return [$idx, $totalSum];
    }
    function f($i) {
        $M = 50;
        $l = 0;
        $r = 1 << $M;
        while ($l < $r) {
            $mid = ($l + $r + 1) >> 1;
            $p = $this->numIdxAndSum($mid);
            if ($p[0] < $i) $l = $mid;
            else $r = $mid - 1;
        }
        $p = $this->numIdxAndSum($l);
        $totalSum = $p[1];
        $i -= $p[0];
        $x = $l + 1;
        for ($j = 0; $j < $i; $j++) {
            $y = $x & -$x;
            $tz = 0;
            $yy = $y;
            while (($yy & 1) === 0) { $tz++; $yy >>= 1; }
            $totalSum += $tz;
            $x -= $y;
        }
        return $totalSum;
    }
    function qpow($a, $n, $mod) {
        $ans = 1 % $mod;
        $a %= $mod;
        while ($n > 0) {
            if (($n & 1) !== 0) $ans = $ans * $a % $mod;
            $a = $a * $a % $mod;
            $n >>= 1;
        }
        return $ans;
    }
}
''')

add("3146_permutation_difference_between_two_strings", r'''<?php
// LeetCode 3146 - Permutation Difference between Two Strings
// https://leetcode.com/problems/permutation-difference-between-two-strings/

class Solution {
    function findPermutationDifference($s, $t) {
        $d = array_fill(0, 26, 0);
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) $d[ord($s[$i]) - 97] = $i;
        $ans = 0;
        $nt = strlen($t);
        for ($i = 0; $i < $nt; $i++) $ans += abs($d[ord($t[$i]) - 97] - $i);
        return $ans;
    }
}
''')

add("3147_taking_maximum_energy_from_the_mystic_dungeon", r'''<?php
// LeetCode 3147 - Taking Maximum Energy From the Mystic Dungeon
// https://leetcode.com/problems/taking-maximum-energy-from-the-mystic-dungeon/

class Solution {
    function maximumEnergy($energy, $k) {
        $ans = -(1 << 30);
        $n = count($energy);
        for ($i = $n - $k; $i < $n; $i++) {
            for ($j = $i, $s = 0; $j >= 0; $j -= $k) {
                $s += $energy[$j];
                $ans = max($ans, $s);
            }
        }
        return $ans;
    }
}
''')

add("3148_maximum_difference_score_in_a_grid", r'''<?php
// LeetCode 3148 - Maximum Difference Score in a Grid
// https://leetcode.com/problems/maximum-difference-score-in-a-grid/

class Solution {
    function maxScore($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        $INF = 1 << 30;
        $f = [];
        for ($i = 0; $i < $m; $i++) $f[] = array_fill(0, $n, 0);
        $ans = -$INF;
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                $x = $grid[$i][$j];
                $mi = $INF;
                if ($i > 0) $mi = min($mi, $f[$i - 1][$j]);
                if ($j > 0) $mi = min($mi, $f[$i][$j - 1]);
                $ans = max($ans, $x - $mi);
                $f[$i][$j] = min($x, $mi);
            }
        }
        return $ans;
    }
}
''')

add("3149_find_the_minimum_cost_array_permutation", r'''<?php
// LeetCode 3149 - Find the Minimum Cost Array Permutation
// https://leetcode.com/problems/find-the-minimum-cost-array-permutation/

class Solution {
    public $nums;
    public $n;
    public $memo;
    public $ans;
    function findPermutation($nums) {
        $this->nums = $nums;
        $this->n = count($nums);
        $this->memo = [];
        for ($i = 0; $i < (1 << $this->n); $i++) $this->memo[] = array_fill(0, $this->n, -1);
        $this->ans = [];
        $this->g(1, 0);
        return $this->ans;
    }
    function absv($x) { return $x < 0 ? -$x : $x; }
    function dfs($mask, $pre) {
        $n = $this->n;
        $nums = $this->nums;
        if ($mask === (1 << $n) - 1) return $this->absv($pre - $nums[0]);
        if ($this->memo[$mask][$pre] !== -1) return $this->memo[$mask][$pre];
        $res = PHP_INT_MAX;
        for ($cur = 1; $cur < $n; $cur++) {
            if ((($mask >> $cur) & 1) === 0) {
                $res = min($res, $this->absv($pre - $nums[$cur]) + $this->dfs($mask | (1 << $cur), $cur));
            }
        }
        return $this->memo[$mask][$pre] = $res;
    }
    function g($mask, $pre) {
        $this->ans[] = $pre;
        $n = $this->n;
        $nums = $this->nums;
        if ($mask === (1 << $n) - 1) return;
        $res = $this->dfs($mask, $pre);
        for ($cur = 1; $cur < $n; $cur++) {
            if ((($mask >> $cur) & 1) === 0) {
                if ($this->absv($pre - $nums[$cur]) + $this->dfs($mask | (1 << $cur), $cur) === $res) {
                    $this->g($mask | (1 << $cur), $cur);
                    break;
                }
            }
        }
    }
}
''')

add("3151_special_array_i", r'''<?php
// LeetCode 3151 - Special Array I
// https://leetcode.com/problems/special-array-i/

class Solution {
    function isArraySpecial($nums) {
        $n = count($nums);
        for ($i = 1; $i < $n; $i++) {
            if ($nums[$i] % 2 === $nums[$i - 1] % 2) return false;
        }
        return true;
    }
}
''')

add("3152_special_array_ii", r'''<?php
// LeetCode 3152 - Special Array II
// https://leetcode.com/problems/special-array-ii/

class Solution {
    function isArraySpecial($nums, $queries) {
        $n = count($nums);
        $d = range(0, $n - 1);
        for ($i = 1; $i < $n; $i++) {
            if ($nums[$i] % 2 !== $nums[$i - 1] % 2) $d[$i] = $d[$i - 1];
        }
        $ans = [];
        for ($i = 0; $i < count($queries); $i++)
            $ans[$i] = $d[$queries[$i][1]] <= $queries[$i][0];
        return $ans;
    }
}
''')

add("3153_sum_of_digit_differences_of_all_pairs", r'''<?php
// LeetCode 3153 - Sum of Digit Differences of All Pairs
// https://leetcode.com/problems/sum-of-digit-differences-of-all-pairs/

class Solution {
    function sumDigitDifferences($nums) {
        $n = count($nums);
        $m = (int)floor(log10($nums[0])) + 1;
        $ans = 0;
        $vals = $nums;
        for ($k = 0; $k < $m; $k++) {
            $cnt = array_fill(0, 10, 0);
            for ($i = 0; $i < $n; $i++) {
                $cnt[$vals[$i] % 10]++;
                $vals[$i] = intdiv($vals[$i], 10);
            }
            foreach ($cnt as $v) $ans += $v * ($n - $v);
        }
        return intdiv($ans, 2);
    }
}
''')

add("3154_find_number_of_ways_to_reach_the_k_th_stair", r'''<?php
// LeetCode 3154 - Find Number of Ways to Reach the K-th Stair
// https://leetcode.com/problems/find-number-of-ways-to-reach-the-k-th-stair/

class Solution {
    public $k;
    public $f = [];
    function waysToReachStair($k) {
        $this->k = $k;
        $this->f = [];
        return $this->dfs(1, 0, 0);
    }
    function dfs($i, $j, $jump) {
        if ($i > $this->k + 1) return 0;
        $key = $i . "," . $j . "," . $jump;
        if (isset($this->f[$key])) return $this->f[$key];
        $ans = 0;
        if ($i === $this->k) $ans++;
        if ($i > 0 && $j === 0) $ans += $this->dfs($i - 1, 1, $jump);
        $ans += $this->dfs($i + (1 << $jump), 0, $jump + 1);
        $this->f[$key] = $ans;
        return $ans;
    }
}
''')

add("3155_maximum_number_of_upgradable_servers", r'''<?php
// LeetCode 3155 - Maximum Number of Upgradable Servers
// https://leetcode.com/problems/maximum-number-of-upgradable-servers/

class Solution {
    function maxUpgrades($count, $upgrade, $sell, $money) {
        $ans = [];
        for ($i = 0; $i < count($count); $i++) {
            $cnt = $count[$i];
            $ans[$i] = min($cnt, intdiv($cnt * $sell[$i] + $money[$i], $upgrade[$i] + $sell[$i]));
        }
        return $ans;
    }
}
''')

add("3157_find_the_level_of_tree_with_minimum_sum", r'''<?php
// LeetCode 3157 - Find the Level of Tree with Minimum Sum
// https://leetcode.com/problems/find-the-level-of-tree-with-minimum-sum/

class TreeNode {
    public $val = 0;
    public $left = null;
    public $right = null;
    function __construct($val = 0, $left = null, $right = null) {
        $this->val = $val;
        $this->left = $left;
        $this->right = $right;
    }
}

class Solution {
    function minimumLevel($root) {
        $q = [$root];
        $s = PHP_INT_MAX;
        $ans = 0;
        for ($level = 1; $q; $level++) {
            $t = 0;
            $m = count($q);
            while ($m-- > 0) {
                $node = array_shift($q);
                $t += $node->val;
                if ($node->left !== null) $q[] = $node->left;
                if ($node->right !== null) $q[] = $node->right;
            }
            if ($s > $t) {
                $s = $t;
                $ans = $level;
            }
        }
        return $ans;
    }
}
''')

add("3158_find_the_xor_of_numbers_which_appear_twice", r'''<?php
// LeetCode 3158 - Find the XOR of Numbers Which Appear Twice
// https://leetcode.com/problems/find-the-xor-of-numbers-which-appear-twice/

class Solution {
    function duplicateNumbersXOR($nums) {
        $cnt = array_fill(0, 51, 0);
        $ans = 0;
        foreach ($nums as $x) {
            $cnt[$x]++;
            if ($cnt[$x] === 2) $ans ^= $x;
        }
        return $ans;
    }
}
''')

add("3159_find_occurrences_of_an_element_in_an_array", r'''<?php
// LeetCode 3159 - Find Occurrences of an Element in an Array
// https://leetcode.com/problems/find-occurrences-of-an-element-in-an-array/

class Solution {
    function occurrencesOfElement($nums, $queries, $x) {
        $ids = [];
        for ($i = 0; $i < count($nums); $i++) if ($nums[$i] === $x) $ids[] = $i;
        $ans = [];
        for ($qi = 0; $qi < count($queries); $qi++) {
            $i = $queries[$qi];
            if ($i - 1 < count($ids)) $ans[$qi] = $ids[$i - 1];
            else $ans[$qi] = -1;
        }
        return $ans;
    }
}
''')

add("3160_find_the_number_of_distinct_colors_among_the_balls", r'''<?php
// LeetCode 3160 - Find the Number of Distinct Colors Among the Balls
// https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/

class Solution {
    function queryResults($limit, $queries) {
        $g = [];
        $cnt = [];
        $ans = [];
        $ai = 0;
        foreach ($queries as $q) {
            $x = $q[0];
            $y = $q[1];
            $cnt[$y] = ($cnt[$y] ?? 0) + 1;
            if (isset($g[$x])) {
                $old = $g[$x];
                $nv = $cnt[$old] - 1;
                if ($nv === 0) unset($cnt[$old]);
                else $cnt[$old] = $nv;
            }
            $g[$x] = $y;
            $ans[$ai++] = count($cnt);
        }
        return $ans;
    }
}
''')

add("3161_block_placement_queries", r'''<?php
// LeetCode 3161 - Block Placement Queries
// https://leetcode.com/problems/block-placement-queries/

class FenwickMax {
    public $vals;
    function __construct($n) {
        $this->vals = array_fill(0, $n + 1, 0);
    }
    function maximize($i, $val) {
        for (; $i < count($this->vals); $i += $i & -$i)
            $this->vals[$i] = max($this->vals[$i], $val);
    }
    function get($i) {
        $res = 0;
        for (; $i > 0; $i -= $i & -$i) $res = max($res, $this->vals[$i]);
        return $res;
    }
}

class Solution {
    function getResults($queries) {
        $n = count($queries) * 3;
        if ($n > 50000) $n = 50000;
        $tree = new FenwickMax($n + 1);
        $obs = [0, $n];
        foreach ($queries as $q) {
            if ($q[0] === 1) {
                $x = $q[1];
                $idx = $this->lowerBound($obs, $x);
                if ($idx === count($obs) || $obs[$idx] !== $x) array_splice($obs, $idx, 0, [$x]);
            }
        }
        for ($i = 0; $i + 1 < count($obs); $i++) {
            $tree->maximize($obs[$i + 1], $obs[$i + 1] - $obs[$i]);
        }
        $ans = [];
        for ($i = count($queries) - 1; $i >= 0; $i--) {
            $typ = $queries[$i][0];
            $x = $queries[$i][1];
            if ($typ === 1) {
                $j = $this->lowerBound($obs, $x);
                $prev = $obs[$j - 1];
                $next = $obs[$j + 1];
                array_splice($obs, $j, 1);
                $tree->maximize($next, $next - $prev);
            } else {
                $sz = $queries[$i][2];
                $j = $this->lowerBound($obs, $x + 1) - 1;
                $prev = $obs[$j];
                $ans[] = $tree->get($prev) >= $sz || $x - $prev >= $sz;
            }
        }
        return array_reverse($ans);
    }
    function lowerBound($a, $x) {
        $lo = 0;
        $hi = count($a);
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi, 2);
            if ($a[$mid] < $x) $lo = $mid + 1;
            else $hi = $mid;
        }
        return $lo;
    }
}
''')

add("3162_find_the_number_of_good_pairs_i", r'''<?php
// LeetCode 3162 - Find the Number of Good Pairs I
// https://leetcode.com/problems/find-the-number-of-good-pairs-i/

class Solution {
    function numberOfPairs($nums1, $nums2, $k) {
        $ans = 0;
        foreach ($nums1 as $x)
            foreach ($nums2 as $y)
                if ($x % ($y * $k) === 0) $ans++;
        return $ans;
    }
}
''')

add("3163_string_compression_iii", r'''<?php
// LeetCode 3163 - String Compression III
// https://leetcode.com/problems/string-compression-iii/

class Solution {
    function compressedString($word) {
        $ans = "";
        $n = strlen($word);
        for ($i = 0; $i < $n; ) {
            $j = $i + 1;
            while ($j < $n && $word[$j] === $word[$i]) $j++;
            $k = $j - $i;
            while ($k > 0) {
                $x = min(9, $k);
                $ans .= (string)$x . $word[$i];
                $k -= $x;
            }
            $i = $j;
        }
        return $ans;
    }
}
''')

add("3164_find_the_number_of_good_pairs_ii", r'''<?php
// LeetCode 3164 - Find the Number of Good Pairs II
// https://leetcode.com/problems/find-the-number-of-good-pairs-ii/

class Solution {
    function numberOfPairs($nums1, $nums2, $k) {
        $cnt1 = [];
        foreach ($nums1 as $x) {
            if ($x % $k === 0) {
                $v = intdiv($x, $k);
                $cnt1[$v] = ($cnt1[$v] ?? 0) + 1;
            }
        }
        if (!$cnt1) return 0;
        $cnt2 = [];
        foreach ($nums2 as $x) $cnt2[$x] = ($cnt2[$x] ?? 0) + 1;
        $mx = 0;
        foreach ($cnt1 as $x => $_) $mx = max($mx, $x);
        $ans = 0;
        foreach ($cnt2 as $x => $v) {
            $s = 0;
            for ($y = $x; $y <= $mx; $y += $x) {
                if (isset($cnt1[$y])) $s += $cnt1[$y];
            }
            $ans += $s * $v;
        }
        return $ans;
    }
}
''')

add("3165_maximum_sum_of_subsequence_with_non_adjacent_elements", r'''<?php
// LeetCode 3165 - Maximum Sum of Subsequence With Non-adjacent Elements
// https://leetcode.com/problems/maximum-sum-of-subsequence-with-non-adjacent-elements/

class SegNode {
    public $l = 0;
    public $r = 0;
    public $s00 = 0;
    public $s01 = 0;
    public $s10 = 0;
    public $s11 = 0;
}

class Solution {
    public $tr;
    function maximumSumSubsequence($nums, $queries) {
        $n = count($nums);
        $this->tr = [];
        for ($i = 0; $i < $n * 4; $i++) $this->tr[] = new SegNode();
        $this->build(1, 1, $n);
        for ($i = 0; $i < $n; $i++) $this->modify(1, $i + 1, $nums[$i]);
        $MOD = 1000000007;
        $ans = 0;
        foreach ($queries as $q) {
            $this->modify(1, $q[0] + 1, $q[1]);
            $ans = ($ans + $this->query(1, 1, $n)) % $MOD;
        }
        return $ans;
    }
    function build($u, $l, $r) {
        $this->tr[$u]->l = $l;
        $this->tr[$u]->r = $r;
        if ($l === $r) return;
        $mid = ($l + $r) >> 1;
        $this->build($u << 1, $l, $mid);
        $this->build($u << 1 | 1, $mid + 1, $r);
    }
    function pushup($u) {
        $left = $this->tr[$u << 1];
        $right = $this->tr[$u << 1 | 1];
        $this->tr[$u]->s00 = max($left->s00 + $right->s10, $left->s01 + $right->s00);
        $this->tr[$u]->s01 = max($left->s00 + $right->s11, $left->s01 + $right->s01);
        $this->tr[$u]->s10 = max($left->s10 + $right->s10, $left->s11 + $right->s00);
        $this->tr[$u]->s11 = max($left->s10 + $right->s11, $left->s11 + $right->s01);
    }
    function modify($u, $x, $v) {
        if ($this->tr[$u]->l === $this->tr[$u]->r) {
            $this->tr[$u]->s11 = max(0, $v);
            return;
        }
        $mid = ($this->tr[$u]->l + $this->tr[$u]->r) >> 1;
        if ($x <= $mid) $this->modify($u << 1, $x, $v);
        else $this->modify($u << 1 | 1, $x, $v);
        $this->pushup($u);
    }
    function query($u, $l, $r) {
        if ($this->tr[$u]->l >= $l && $this->tr[$u]->r <= $r) return $this->tr[$u]->s11;
        $mid = ($this->tr[$u]->l + $this->tr[$u]->r) >> 1;
        $ans = 0;
        if ($r <= $mid) $ans = $this->query($u << 1, $l, $r);
        if ($l > $mid) $ans = max($ans, $this->query($u << 1 | 1, $l, $r));
        return $ans;
    }
}
''')

add("3167_better_compression_of_string", r'''<?php
// LeetCode 3167 - Better Compression of String
// https://leetcode.com/problems/better-compression-of-string/

class Solution {
    function betterCompression($compressed) {
        $cnt = array_fill(0, 26, 0);
        $n = strlen($compressed);
        for ($i = 0; $i < $n; ) {
            $c = $compressed[$i];
            $j = $i + 1;
            $x = 0;
            while ($j < $n) {
                $d = $compressed[$j];
                if ($d < "0" || $d > "9") break;
                $x = $x * 10 + (ord($d) - 48);
                $j++;
            }
            $cnt[ord($c) - 97] += $x;
            $i = $j;
        }
        $ans = "";
        for ($c = 0; $c < 26; $c++) {
            if ($cnt[$c] > 0) $ans .= chr(97 + $c) . (string)$cnt[$c];
        }
        return $ans;
    }
}
''')

add("3168_minimum_number_of_chairs_in_a_waiting_room", r'''<?php
// LeetCode 3168 - Minimum Number of Chairs in a Waiting Room
// https://leetcode.com/problems/minimum-number-of-chairs-in-a-waiting-room/

class Solution {
    function minimumChairs($s) {
        $cnt = 0;
        $left = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $c = $s[$i];
            if ($c === "E") {
                if ($left > 0) $left--;
                else $cnt++;
            } else $left++;
        }
        return $cnt;
    }
}
''')

add("3169_count_days_without_meetings", r'''<?php
// LeetCode 3169 - Count Days Without Meetings
// https://leetcode.com/problems/count-days-without-meetings/

class Solution {
    function countDays($days, $meetings) {
        usort($meetings, function ($a, $b) { return $a[0] <=> $b[0]; });
        $last = 0;
        $ans = 0;
        foreach ($meetings as $e) {
            $st = $e[0];
            $ed = $e[1];
            if ($last < $st) $ans += $st - $last - 1;
            $last = max($last, $ed);
        }
        $ans += $days - $last;
        return $ans;
    }
}
''')

add("3170_lexicographically_minimum_string_after_removing_stars", r'''<?php
// LeetCode 3170 - Lexicographically Minimum String After Removing Stars
// https://leetcode.com/problems/lexicographically-minimum-string-after-removing-stars/

class Solution {
    function clearStars($s) {
        $g = array_fill(0, 26, []);
        $n = strlen($s);
        $rem = array_fill(0, $n, false);
        for ($i = 0; $i < $n; $i++) {
            if ($s[$i] === "*") {
                $rem[$i] = true;
                for ($j = 0; $j < 26; $j++) {
                    if ($g[$j]) {
                        $rem[array_pop($g[$j])] = true;
                        break;
                    }
                }
            } else {
                $g[ord($s[$i]) - 97][] = $i;
            }
        }
        $ans = "";
        for ($i = 0; $i < $n; $i++) if (!$rem[$i]) $ans .= $s[$i];
        return $ans;
    }
}
''')

add("3171_find_subarray_with_bitwise_or_closest_to_k", r'''<?php
// LeetCode 3171 - Find Subarray With Bitwise OR Closest to K
// https://leetcode.com/problems/find-subarray-with-bitwise-or-closest-to-k/

function leadingZeroCount($x) {
    if ($x === 0) return 32;
    $n = 0;
    for ($bit = 31; $bit >= 0; $bit--) {
        if ((($x >> $bit) & 1) !== 0) break;
        $n++;
    }
    return $n;
}

class Solution {
    function minimumDifference($nums, $k) {
        $mx = 0;
        foreach ($nums as $v) $mx = max($mx, $v);
        $m = $mx === 0 ? 1 : 32 - leadingZeroCount($mx);
        $cnt = array_fill(0, $m, 0);
        $ans = PHP_INT_MAX;
        $s = 0;
        $i = 0;
        $n = count($nums);
        for ($j = 0; $j < $n; $j++) {
            $x = $nums[$j];
            $s |= $x;
            $ans = min($ans, abs($s - $k));
            for ($h = 0; $h < $m; $h++) if ((($x >> $h) & 1) !== 0) $cnt[$h]++;
            while ($i < $j && $s > $k) {
                $y = $nums[$i];
                for ($h = 0; $h < $m; $h++) {
                    if ((($y >> $h) & 1) !== 0) {
                        $cnt[$h]--;
                        if ($cnt[$h] === 0) $s ^= 1 << $h;
                    }
                }
                $ans = min($ans, abs($s - $k));
                $i++;
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

#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
SOLUTIONS = {}

def add(folder, body):
    SOLUTIONS[folder] = body


add("2832_maximal_range_that_each_element_is_maximum_in_it", r'''<?php
// LeetCode 2832 - Maximal Range That Each Element Is Maximum in It
// https://leetcode.com/problems/maximal-range-that-each-element-is-maximum-in-it/

class Solution {
    function maximumLength($nums) {
        $n = count($nums);
        $left = array_fill(0, $n, 0);
        $right = array_fill(0, $n, 0);
        $st = [];
        for ($i = 0; $i < $n; $i++) {
            while (count($st) && $nums[$st[count($st) - 1]] < $nums[$i]) array_pop($st);
            $left[$i] = count($st) ? $st[count($st) - 1] : -1;
            $st[] = $i;
        }
        $st = [];
        for ($i = $n - 1; $i >= 0; $i--) {
            while (count($st) && $nums[$st[count($st) - 1]] <= $nums[$i]) array_pop($st);
            $right[$i] = count($st) ? $st[count($st) - 1] : $n;
            $st[] = $i;
        }
        $ans = array_fill(0, $n, 0);
        for ($i = 0; $i < $n; $i++) $ans[$i] = $right[$i] - $left[$i] - 1;
        return $ans;
    }
}
''')

add("2833_furthest_point_from_origin", r'''<?php
// LeetCode 2833 - Furthest Point From Origin
// https://leetcode.com/problems/furthest-point-from-origin/

class Solution {
    function furthestDistanceFromOrigin($moves) {
        $L = 0;
        $R = 0;
        $u = 0;
        $n = strlen($moves);
        for ($i = 0; $i < $n; $i++) {
            $c = $moves[$i];
            if ($c === 'L') $L++;
            else if ($c === 'R') $R++;
            else $u++;
        }
        return abs($L - $R) + $u;
    }
}
''')

add("2834_find_the_minimum_possible_sum_of_a_beautiful_array", r'''<?php
// LeetCode 2834 - Find the Minimum Possible Sum of a Beautiful Array
// https://leetcode.com/problems/find-the-minimum-possible-sum-of-a-beautiful-array/

class Solution {
    function minimumPossibleSum($n, $target) {
        $MOD = 1000000007;
        $m = intdiv($target, 2);
        if ($n <= $m) return (int)(($n * ($n + 1) / 2) % $MOD);
        $sum = $m * ($m + 1) / 2;
        $remain = $n - $m;
        $sum += $remain * $target + $remain * ($remain - 1) / 2;
        return (int)($sum % $MOD);
    }
}
''')

add("2835_minimum_operations_to_form_subsequence_with_target_sum", r'''<?php
// LeetCode 2835 - Minimum Operations to Form Subsequence With Target Sum
// https://leetcode.com/problems/minimum-operations-to-form-subsequence-with-target-sum/

class Solution {
    function minOperations($nums, $target) {
        $cnt = array_fill(0, 32, 0);
        $sum = 0;
        foreach ($nums as $v) {
            $sum += $v;
            $b = 0;
            while ((1 << $b) < $v) $b++;
            $cnt[$b]++;
        }
        if ($sum < $target) return -1;
        $ans = 0;
        for ($i = 0; $i < 31; $i++) {
            if (($target & (1 << $i)) !== 0) {
                if ($cnt[$i] > 0) $cnt[$i]--;
                else {
                    $j = $i + 1;
                    while ($j < 32 && $cnt[$j] === 0) $j++;
                    if ($j === 32) return -1;
                    while ($j > $i) {
                        $cnt[$j]--;
                        $cnt[$j - 1] += 2;
                        $ans++;
                        $j--;
                    }
                    $cnt[$i]--;
                }
            }
            $cnt[$i + 1] += intdiv($cnt[$i], 2);
        }
        return $ans;
    }
}
''')

add("2836_maximize_value_of_function_in_a_ball_passing_game", r'''<?php
// LeetCode 2836 - Maximize Value of Function in a Ball Passing Game
// https://leetcode.com/problems/maximize-value-of-function-in-a-ball-passing-game/

class Solution {
    function getMaxFunctionValue($receiver, $k) {
        $n = count($receiver);
        $LOG = 36;
        $up = [];
        $sum = [];
        for ($j = 0; $j < $LOG; $j++) {
            $up[$j] = array_fill(0, $n, 0);
            $sum[$j] = array_fill(0, $n, 0);
        }
        for ($i = 0; $i < $n; $i++) {
            $up[0][$i] = $receiver[$i];
            $sum[0][$i] = $receiver[$i];
        }
        for ($j = 1; $j < $LOG; $j++) {
            for ($i = 0; $i < $n; $i++) {
                $mid = $up[$j - 1][$i];
                $up[$j][$i] = $up[$j - 1][$mid];
                $sum[$j][$i] = $sum[$j - 1][$i] + $sum[$j - 1][$mid];
            }
        }
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            $cur = $i;
            $total = $i;
            $kk = $k;
            for ($j = 0; $j < $LOG; $j++) {
                if (($kk & (1 << $j)) !== 0) {
                    $total += $sum[$j][$cur];
                    $cur = $up[$j][$cur];
                }
            }
            if ($total > $ans) $ans = $total;
        }
        return $ans;
    }
}
''')

add("2838_maximum_coins_heroes_can_collect", r'''<?php
// LeetCode 2838 - Maximum Coins Heroes Can Collect
// https://leetcode.com/problems/maximum-coins-heroes-can-collect/

class Solution {
    function maximumCoins($heroes, $monsters, $coins) {
        $n = count($monsters);
        $idx = range(0, $n - 1);
        usort($idx, function($a, $b) use ($monsters) {
            return $monsters[$a] <=> $monsters[$b];
        });
        $pref = array_fill(0, $n + 1, 0);
        $ms = array_fill(0, $n, 0);
        for ($i = 0; $i < $n; $i++) {
            $ms[$i] = $monsters[$idx[$i]];
            $pref[$i + 1] = $pref[$i] + $coins[$idx[$i]];
        }
        $ans = [];
        foreach ($heroes as $h) {
            $lo = 0;
            $hi = $n;
            while ($lo < $hi) {
                $mid = intdiv($lo + $hi, 2);
                if ($ms[$mid] <= $h) $lo = $mid + 1;
                else $hi = $mid;
            }
            $ans[] = $pref[$lo];
        }
        return $ans;
    }
}
''')

add("2839_check_if_strings_can_be_made_equal_with_operations_i", r'''<?php
// LeetCode 2839 - Check if Strings Can be Made Equal With Operations I
// https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-i/

class Solution {
    function canBeEqual($s1, $s2) {
        $a = [$s1[0], $s1[2]];
        $b = [$s2[0], $s2[2]];
        $c = [$s1[1], $s1[3]];
        $d = [$s2[1], $s2[3]];
        sort($a);
        sort($b);
        sort($c);
        sort($d);
        return $a === $b && $c === $d;
    }
}
''')

add("2840_check_if_strings_can_be_made_equal_with_operations_ii", r'''<?php
// LeetCode 2840 - Check if Strings Can be Made Equal With Operations II
// https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-ii/

class Solution {
    function checkStrings($s1, $s2) {
        $even1 = array_fill(0, 26, 0);
        $odd1 = array_fill(0, 26, 0);
        $even2 = array_fill(0, 26, 0);
        $odd2 = array_fill(0, 26, 0);
        $n = strlen($s1);
        for ($i = 0; $i < $n; $i++) {
            if ($i % 2 === 0) {
                $even1[ord($s1[$i]) - 97]++;
                $even2[ord($s2[$i]) - 97]++;
            } else {
                $odd1[ord($s1[$i]) - 97]++;
                $odd2[ord($s2[$i]) - 97]++;
            }
        }
        return $even1 === $even2 && $odd1 === $odd2;
    }
}
''')

add("2841_maximum_sum_of_almost_unique_subarray", r'''<?php
// LeetCode 2841 - Maximum Sum of Almost Unique Subarray
// https://leetcode.com/problems/maximum-sum-of-almost-unique-subarray/

class Solution {
    function maxSum($nums, $m, $k) {
        $freq = [];
        $sum = 0;
        $ans = 0;
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            if (!isset($freq[$nums[$i]])) $freq[$nums[$i]] = 0;
            $freq[$nums[$i]]++;
            $sum += $nums[$i];
            if ($i >= $k) {
                $out = $nums[$i - $k];
                $sum -= $out;
                $freq[$out]--;
                if ($freq[$out] === 0) unset($freq[$out]);
            }
            if ($i >= $k - 1 && count($freq) >= $m && $sum > $ans) $ans = $sum;
        }
        return $ans;
    }
}
''')

add("2842_count_k_subsequences_of_a_string_with_maximum_beauty", r'''<?php
// LeetCode 2842 - Count K-Subsequences of a String With Maximum Beauty
// https://leetcode.com/problems/count-k-subsequences-of-a-string-with-maximum-beauty/

class Solution {
    private $MOD = 1000000007;

    function countKSubsequencesWithMaxBeauty($s, $k) {
        $freq = array_fill(0, 26, 0);
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) $freq[ord($s[$i]) - 97]++;
        $vals = [];
        foreach ($freq as $f) if ($f > 0) $vals[] = $f;
        rsort($vals);
        if (count($vals) < $k) return 0;
        $threshold = $vals[$k - 1];
        $need = 0;
        $avail = 0;
        $prod = 1;
        foreach ($vals as $v) {
            if ($v > $threshold) {
                $prod = ($prod * $v) % $this->MOD;
                $need++;
            } else if ($v === $threshold) $avail++;
        }
        $remain = $k - $need;
        $prod = ($prod * $this->comb($avail, $remain)) % $this->MOD;
        for ($i = 0; $i < $remain; $i++) $prod = ($prod * $threshold) % $this->MOD;
        return (int)$prod;
    }

    private function modPow($a, $b) {
        $res = 1;
        $a %= $this->MOD;
        while ($b > 0) {
            if ($b % 2 === 1) $res = ($res * $a) % $this->MOD;
            $a = ($a * $a) % $this->MOD;
            $b = intdiv($b, 2);
        }
        return $res;
    }

    private function comb($n, $r) {
        if ($r < 0 || $r > $n) return 0;
        $num = 1;
        $den = 1;
        for ($i = 0; $i < $r; $i++) {
            $num = ($num * ($n - $i)) % $this->MOD;
            $den = ($den * ($i + 1)) % $this->MOD;
        }
        return ($num * $this->modPow($den, $this->MOD - 2)) % $this->MOD;
    }
}
''')

add("2843_count_symmetric_integers", r'''<?php
// LeetCode 2843 - Count Symmetric Integers
// https://leetcode.com/problems/count-symmetric-integers/

class Solution {
    function countSymmetricIntegers($low, $high) {
        $ans = 0;
        for ($x = $low; $x <= $high; $x++) {
            $s = (string)$x;
            $len = strlen($s);
            if ($len % 2 !== 0) continue;
            $mid = intdiv($len, 2);
            $a = 0;
            $b = 0;
            for ($i = 0; $i < $mid; $i++) {
                $a += ord($s[$i]) - 48;
                $b += ord($s[$mid + $i]) - 48;
            }
            if ($a === $b) $ans++;
        }
        return $ans;
    }
}
''')

add("2844_minimum_operations_to_make_a_special_number", r'''<?php
// LeetCode 2844 - Minimum Operations to Make a Special Number
// https://leetcode.com/problems/minimum-operations-to-make-a-special-number/

class Solution {
    function minimumOperations($num) {
        $n = strlen($num);
        $ans = $n;
        if (strpos($num, '0') !== false) $ans = min($ans, $n - 1);
        foreach (['00', '25', '50', '75'] as $t) {
            $j = $n - 1;
            while ($j >= 0 && $num[$j] !== $t[1]) $j--;
            if ($j < 0) continue;
            $i = $j - 1;
            while ($i >= 0 && $num[$i] !== $t[0]) $i--;
            if ($i < 0) continue;
            $ans = min($ans, $n - $i - 2);
        }
        return $ans;
    }
}
''')

add("2845_count_of_interesting_subarrays", r'''<?php
// LeetCode 2845 - Count of Interesting Subarrays
// https://leetcode.com/problems/count-of-interesting-subarrays/

class Solution {
    function countInterestingSubarrays($nums, $modulo, $k) {
        $freq = [0 => 1];
        $ans = 0;
        $pref = 0;
        foreach ($nums as $v) {
            if ($v % $modulo === $k) $pref++;
            $need = ($pref - $k) % $modulo;
            if ($need < 0) $need += $modulo;
            $ans += $freq[$need] ?? 0;
            $key = $pref % $modulo;
            if (!isset($freq[$key])) $freq[$key] = 0;
            $freq[$key]++;
        }
        return $ans;
    }
}
''')

add("2846_minimum_edge_weight_equilibrium_queries_in_a_tree", r'''<?php
// LeetCode 2846 - Minimum Edge Weight Equilibrium Queries in a Tree
// https://leetcode.com/problems/minimum-edge-weight-equilibrium-queries-in-a-tree/

class Solution {
    function minOperationsQueries($n, $edges, $queries) {
        $LOG = 15;
        $g = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $g[$e[0]][] = [$e[1], $e[2]];
            $g[$e[1]][] = [$e[0], $e[2]];
        }
        $up = [];
        for ($j = 0; $j < $LOG; $j++) $up[$j] = array_fill(0, $n, 0);
        $depth = array_fill(0, $n, 0);
        $cnt = [];
        for ($i = 0; $i < $n; $i++) $cnt[$i] = array_fill(0, 27, 0);
        $dfs = function($u, $p) use (&$dfs, &$g, &$up, &$depth, &$cnt) {
            $up[0][$u] = $p;
            foreach ($g[$u] as $ew) {
                $v = $ew[0];
                $w = $ew[1];
                if ($v === $p) continue;
                $depth[$v] = $depth[$u] + 1;
                for ($i = 0; $i < 27; $i++) $cnt[$v][$i] = $cnt[$u][$i];
                $cnt[$v][$w]++;
                $dfs($v, $u);
            }
        };
        $dfs(0, 0);
        for ($j = 1; $j < $LOG; $j++)
            for ($i = 0; $i < $n; $i++) $up[$j][$i] = $up[$j - 1][$up[$j - 1][$i]];
        $lca = function($a, $b) use ($LOG, &$up, &$depth) {
            if ($depth[$a] < $depth[$b]) {
                $tmp = $a; $a = $b; $b = $tmp;
            }
            $diff = $depth[$a] - $depth[$b];
            for ($j = 0; $j < $LOG; $j++) if (($diff & (1 << $j)) !== 0) $a = $up[$j][$a];
            if ($a === $b) return $a;
            for ($j = $LOG - 1; $j >= 0; $j--) {
                if ($up[$j][$a] !== $up[$j][$b]) {
                    $a = $up[$j][$a];
                    $b = $up[$j][$b];
                }
            }
            return $up[0][$a];
        };
        $ans = [];
        foreach ($queries as $q) {
            $a = $q[0];
            $b = $q[1];
            $c = $lca($a, $b);
            $total = $depth[$a] + $depth[$b] - 2 * $depth[$c];
            $best = 0;
            for ($w = 1; $w <= 26; $w++) {
                $f = $cnt[$a][$w] + $cnt[$b][$w] - 2 * $cnt[$c][$w];
                if ($f > $best) $best = $f;
            }
            $ans[] = $total - $best;
        }
        return $ans;
    }
}
''')

add("2847_smallest_number_with_given_digit_product", r'''<?php
// LeetCode 2847 - Smallest Number With Given Digit Product
// https://leetcode.com/problems/smallest-number-with-given-digit-product/

class Solution {
    function smallestNumber($n) {
        if ($n === 0) return '0';
        if ($n === 1) return '1';
        $digits = [];
        for ($d = 9; $d >= 2; $d--) {
            while ($n % $d === 0) {
                $digits[] = (string)$d;
                $n = intdiv($n, $d);
            }
        }
        if ($n > 1) return '-1';
        return implode('', array_reverse($digits));
    }
}
''')

add("2848_points_that_intersect_with_cars", r'''<?php
// LeetCode 2848 - Points That Intersect With Cars
// https://leetcode.com/problems/points-that-intersect-with-cars/

class Solution {
    function numberOfPoints($nums) {
        $cov = array_fill(0, 102, 0);
        foreach ($nums as $ab) {
            for ($x = $ab[0]; $x <= $ab[1]; $x++) $cov[$x] = 1;
        }
        $s = 0;
        foreach ($cov as $v) $s += $v;
        return $s;
    }
}
''')

add("2849_determine_if_a_cell_is_reachable_at_a_given_time", r'''<?php
// LeetCode 2849 - Determine if a Cell Is Reachable at a Given Time
// https://leetcode.com/problems/determine-if-a-cell-is-reachable-at-a-given-time/

class Solution {
    function isReachableAtTime($sx, $sy, $fx, $fy, $t) {
        $need = max(abs($sx - $fx), abs($sy - $fy));
        if ($need === 0) return $t !== 1;
        return $t >= $need;
    }
}
''')

add("2850_minimum_moves_to_spread_stones_over_grid", r'''<?php
// LeetCode 2850 - Minimum Moves to Spread Stones Over Grid
// https://leetcode.com/problems/minimum-moves-to-spread-stones-over-grid/

class Solution {
    function minimumMoves($grid) {
        $extras = [];
        $zeros = [];
        for ($i = 0; $i < 3; $i++) {
            for ($j = 0; $j < 3; $j++) {
                if ($grid[$i][$j] === 0) $zeros[] = [$i, $j];
                else if ($grid[$i][$j] > 1) {
                    for ($k = 0; $k < $grid[$i][$j] - 1; $k++) $extras[] = [$i, $j];
                }
            }
        }
        if (!count($zeros)) return 0;
        $best = 1 << 30;
        $dfs = function($i, $cost) use (&$dfs, &$extras, &$zeros, &$best) {
            if ($cost >= $best) return;
            if ($i === count($zeros)) {
                $best = $cost;
                return;
            }
            for ($j = 0; $j < count($extras); $j++) {
                if ($extras[$j][0] < 0) continue;
                $e = $extras[$j];
                $extras[$j] = [-1, $e[1]];
                $d = abs($e[0] - $zeros[$i][0]) + abs($e[1] - $zeros[$i][1]);
                $dfs($i + 1, $cost + $d);
                $extras[$j] = $e;
            }
        };
        $dfs(0, 0);
        return $best;
    }
}
''')

add("2851_string_transformation", r'''<?php
// LeetCode 2851 - String Transformation
// https://leetcode.com/problems/string-transformation/

class Solution {
    private $MOD = 1000000007;

    function numberOfWays($s, $t, $k) {
        $n = strlen($s);
        $ss = $s . $s;
        $found = false;
        $cnt = 0;
        for ($i = 0; $i < $n; $i++) {
            if (substr($ss, $i, $n) === $t) {
                $cnt++;
                $found = true;
            }
        }
        if (!$found) return 0;
        $same = $s === $t;
        $pk = $this->modPow($n - 1, $k);
        $invn = $this->modPow($n, $this->MOD - 2);
        $sign = ($k % 2 === 1) ? ($this->MOD - 1) : 1;
        $waysSame = (($pk + (($n - 1) % $this->MOD) * $sign % $this->MOD) % $this->MOD * $invn) % $this->MOD;
        $waysDiff = (($pk - $sign + $this->MOD) % $this->MOD * $invn) % $this->MOD;
        if ($same) return (int)$waysSame;
        return (int)(($waysDiff * $cnt) % $this->MOD);
    }

    private function modPow($a, $b) {
        $res = 1;
        $a %= $this->MOD;
        while ($b > 0) {
            if ($b % 2 === 1) $res = ($res * $a) % $this->MOD;
            $a = ($a * $a) % $this->MOD;
            $b = intdiv($b, 2);
        }
        return $res;
    }
}
''')

add("2852_sum_of_remoteness_of_all_cells", r'''<?php
// LeetCode 2852 - Sum of Remoteness of All Cells
// https://leetcode.com/problems/sum-of-remoteness-of-all-cells/

class Solution {
    function sumRemoteness($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        $seen = [];
        for ($i = 0; $i < $m; $i++) $seen[$i] = array_fill(0, $n, false);
        $dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];
        $total = 0;
        for ($i = 0; $i < $m; $i++)
            for ($j = 0; $j < $n; $j++)
                if ($grid[$i][$j] !== -1) $total += $grid[$i][$j];
        $ans = 0;
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if ($grid[$i][$j] === -1 || $seen[$i][$j]) continue;
                $q = [[$i, $j]];
                $seen[$i][$j] = true;
                $sum = 0;
                $cnt = 0;
                $qi = 0;
                while ($qi < count($q)) {
                    $x = $q[$qi][0];
                    $y = $q[$qi][1];
                    $qi++;
                    $sum += $grid[$x][$y];
                    $cnt++;
                    foreach ($dirs as $d) {
                        $ni = $x + $d[0];
                        $nj = $y + $d[1];
                        if ($ni >= 0 && $nj >= 0 && $ni < $m && $nj < $n && !$seen[$ni][$nj] && $grid[$ni][$nj] !== -1) {
                            $seen[$ni][$nj] = true;
                            $q[] = [$ni, $nj];
                        }
                    }
                }
                $ans += ($total - $sum) * $cnt;
            }
        }
        return $ans;
    }
}
''')

add("2855_minimum_right_shifts_to_sort_the_array", r'''<?php
// LeetCode 2855 - Minimum Right Shifts to Sort the Array
// https://leetcode.com/problems/minimum-right-shifts-to-sort-the-array/

class Solution {
    function minimumRightShifts($nums) {
        $n = count($nums);
        $drops = 0;
        $idx = -1;
        for ($i = 0; $i < $n; $i++) {
            if ($nums[$i] > $nums[($i + 1) % $n]) {
                $drops++;
                $idx = $i;
            }
        }
        if ($drops === 0) return 0;
        if ($drops > 1) return -1;
        return $n - 1 - $idx;
    }
}
''')

add("2856_minimum_array_length_after_pair_removals", r'''<?php
// LeetCode 2856 - Minimum Array Length After Pair Removals
// https://leetcode.com/problems/minimum-array-length-after-pair-removals/

class Solution {
    function minLengthAfterRemovals($nums) {
        $n = count($nums);
        $freq = [];
        $mx = 0;
        foreach ($nums as $v) {
            if (!isset($freq[$v])) $freq[$v] = 0;
            $freq[$v]++;
            if ($freq[$v] > $mx) $mx = $freq[$v];
        }
        if ($mx <= intdiv($n, 2)) return $n % 2;
        return 2 * $mx - $n;
    }
}
''')

add("2857_count_pairs_of_points_with_distance_k", r'''<?php
// LeetCode 2857 - Count Pairs of Points With Distance k
// https://leetcode.com/problems/count-pairs-of-points-with-distance-k/

class Solution {
    function countPairs($coordinates, $k) {
        $freq = [];
        $ans = 0;
        foreach ($coordinates as $xy) {
            $x = $xy[0];
            $y = $xy[1];
            for ($a = 0; $a <= $k; $a++) {
                $b = $k - $a;
                $key = ($x ^ $a) . ',' . ($y ^ $b);
                $ans += $freq[$key] ?? 0;
            }
            $k0 = $x . ',' . $y;
            if (!isset($freq[$k0])) $freq[$k0] = 0;
            $freq[$k0]++;
        }
        return $ans;
    }
}
''')

add("2858_minimum_edge_reversals_so_every_node_is_reachable", r'''<?php
// LeetCode 2858 - Minimum Edge Reversals So Every Node Is Reachable
// https://leetcode.com/problems/minimum-edge-reversals-so-every-node-is-reachable/

class Solution {
    function minEdgeReversals($n, $edges) {
        $g = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $g[$e[0]][] = [$e[1], 0];
            $g[$e[1]][] = [$e[0], 1];
        }
        $ans = array_fill(0, $n, 0);
        $dfs1 = function($u, $p) use (&$dfs1, &$g, &$ans) {
            foreach ($g[$u] as $ew) {
                $v = $ew[0];
                $ww = $ew[1];
                if ($v === $p) continue;
                $ans[0] += $ww;
                $dfs1($v, $u);
            }
        };
        $dfs2 = function($u, $p) use (&$dfs2, &$g, &$ans) {
            foreach ($g[$u] as $ew) {
                $v = $ew[0];
                $ww = $ew[1];
                if ($v === $p) continue;
                $ans[$v] = $ww === 0 ? $ans[$u] + 1 : $ans[$u] - 1;
                $dfs2($v, $u);
            }
        };
        $dfs1(0, -1);
        $dfs2(0, -1);
        return $ans;
    }
}
''')

add("2859_sum_of_values_at_indices_with_k_set_bits", r'''<?php
// LeetCode 2859 - Sum of Values at Indices With K Set Bits
// https://leetcode.com/problems/sum-of-values-at-indices-with-k-set-bits/

class Solution {
    function sumIndicesWithKSetBits($nums, $k) {
        $ans = 0;
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            $x = $i;
            $bits = 0;
            while ($x) {
                $bits += $x & 1;
                $x >>= 1;
            }
            if ($bits === $k) $ans += $nums[$i];
        }
        return $ans;
    }
}
''')

add("2860_happy_students", r'''<?php
// LeetCode 2860 - Happy Students
// https://leetcode.com/problems/happy-students/

class Solution {
    function countWays($nums) {
        sort($nums);
        $n = count($nums);
        $ans = 0;
        if ($nums[0] > 0) $ans++;
        for ($i = 0; $i < $n; $i++) {
            $selected = $i + 1;
            if ($selected > $nums[$i] && ($i === $n - 1 || $selected < $nums[$i + 1])) $ans++;
        }
        return $ans;
    }
}
''')

add("2861_maximum_number_of_alloys", r'''<?php
// LeetCode 2861 - Maximum Number of Alloys
// https://leetcode.com/problems/maximum-number-of-alloys/

class Solution {
    function maxNumberOfAlloys($n, $k, $budget, $composition, $stock, $cost) {
        $ok = function($machines) use ($n, $composition, $stock, $cost, $budget) {
            foreach ($composition as $comp) {
                $spend = 0;
                for ($i = 0; $i < $n; $i++) {
                    $need = $machines * $comp[$i] - $stock[$i];
                    if ($need > 0) $spend += $need * $cost[$i];
                }
                if ($spend <= $budget) return true;
            }
            return false;
        };
        $lo = 0;
        $hi = 1000000000;
        $ans = 0;
        while ($lo <= $hi) {
            $mid = intdiv($lo + $hi, 2);
            if ($ok($mid)) {
                $ans = $mid;
                $lo = $mid + 1;
            } else $hi = $mid - 1;
        }
        return $ans;
    }
}
''')

add("2862_maximum_element_sum_of_a_complete_subset_of_indices", r'''<?php
// LeetCode 2862 - Maximum Element-Sum of a Complete Subset of Indices
// https://leetcode.com/problems/maximum-element-sum-of-a-complete-subset-of-indices/

class Solution {
    function maximumSum($nums) {
        $squareFree = function($x) {
            $res = 1;
            for ($p = 2; $p * $p <= $x; $p++) {
                $cnt = 0;
                while ($x % $p === 0) {
                    $x = intdiv($x, $p);
                    $cnt++;
                }
                if ($cnt % 2 === 1) $res *= $p;
            }
            if ($x > 1) $res *= $x;
            return $res;
        };
        $n = count($nums);
        $groups = [];
        $ans = 0;
        for ($i = 1; $i <= $n; $i++) {
            $sf = $squareFree($i);
            $sum = ($groups[$sf] ?? 0) + $nums[$i - 1];
            $groups[$sf] = $sum;
            if ($sum > $ans) $ans = $sum;
        }
        return $ans;
    }
}
''')

add("2863_maximum_length_of_semi_decreasing_subarrays", r'''<?php
// LeetCode 2863 - Maximum Length of Semi-Decreasing Subarrays
// https://leetcode.com/problems/maximum-length-of-semi-decreasing-subarrays/

class Solution {
    function maxSubarrayLength($nums) {
        $n = count($nums);
        $ans = 0;
        $st = [];
        for ($i = $n - 1; $i >= 0; $i--) {
            if (!count($st) || $nums[$i] > $nums[$st[count($st) - 1]]) $st[] = $i;
        }
        for ($i = 0; $i < $n; $i++) {
            while (count($st) && $nums[$i] > $nums[$st[count($st) - 1]]) {
                $j = array_pop($st);
                if ($j - $i + 1 > $ans) $ans = $j - $i + 1;
            }
        }
        return $ans;
    }
}
''')

add("2864_maximum_odd_binary_number", r'''<?php
// LeetCode 2864 - Maximum Odd Binary Number
// https://leetcode.com/problems/maximum-odd-binary-number/

class Solution {
    function maximumOddBinaryNumber($s) {
        $ones = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) if ($s[$i] === '1') $ones++;
        $zeros = $n - $ones;
        return str_repeat('1', $ones - 1) . str_repeat('0', $zeros) . '1';
    }
}
''')

add("2865_beautiful_towers_i", r'''<?php
// LeetCode 2865 - Beautiful Towers I
// https://leetcode.com/problems/beautiful-towers-i/

class Solution {
    function maximumSumOfHeights($heights) {
        $n = count($heights);
        $ans = 0;
        for ($peak = 0; $peak < $n; $peak++) {
            $sum = $heights[$peak];
            $mn = $heights[$peak];
            for ($i = $peak - 1; $i >= 0; $i--) {
                if ($heights[$i] < $mn) $mn = $heights[$i];
                $sum += $mn;
            }
            $mn = $heights[$peak];
            for ($i = $peak + 1; $i < $n; $i++) {
                if ($heights[$i] < $mn) $mn = $heights[$i];
                $sum += $mn;
            }
            if ($sum > $ans) $ans = $sum;
        }
        return $ans;
    }
}
''')

add("2866_beautiful_towers_ii", r'''<?php
// LeetCode 2866 - Beautiful Towers II
// https://leetcode.com/problems/beautiful-towers-ii/

class Solution {
    function maximumSumOfHeights($maxHeights) {
        $n = count($maxHeights);
        $left = array_fill(0, $n, 0);
        $st = [-1];
        $sum = 0;
        for ($i = 0; $i < $n; $i++) {
            while (count($st) > 1 && $maxHeights[$st[count($st) - 1]] >= $maxHeights[$i]) {
                $j = array_pop($st);
                $sum -= $maxHeights[$j] * ($j - $st[count($st) - 1]);
            }
            $sum += $maxHeights[$i] * ($i - $st[count($st) - 1]);
            $left[$i] = $sum;
            $st[] = $i;
        }
        $right = array_fill(0, $n, 0);
        $st = [$n];
        $sum = 0;
        for ($i = $n - 1; $i >= 0; $i--) {
            while (count($st) > 1 && $maxHeights[$st[count($st) - 1]] >= $maxHeights[$i]) {
                $j = array_pop($st);
                $sum -= $maxHeights[$j] * ($st[count($st) - 1] - $j);
            }
            $sum += $maxHeights[$i] * ($st[count($st) - 1] - $i);
            $right[$i] = $sum;
            $st[] = $i;
        }
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            $cand = $left[$i] + $right[$i] - $maxHeights[$i];
            if ($cand > $ans) $ans = $cand;
        }
        return $ans;
    }
}
''')

add("2867_count_valid_paths_in_a_tree", r'''<?php
// LeetCode 2867 - Count Valid Paths in a Tree
// https://leetcode.com/problems/count-valid-paths-in-a-tree/

class Solution {
    function countPaths($n, $edges) {
        $isPrime = array_fill(0, $n + 1, true);
        $isPrime[0] = false;
        $isPrime[1] = false;
        for ($i = 2; $i * $i <= $n; $i++) {
            if ($isPrime[$i]) {
                for ($j = $i * $i; $j <= $n; $j += $i) $isPrime[$j] = false;
            }
        }
        $g = array_fill(0, $n + 1, []);
        foreach ($edges as $e) {
            $g[$e[0]][] = $e[1];
            $g[$e[1]][] = $e[0];
        }
        $dfs = function($u, $p) use (&$dfs, &$g, &$isPrime) {
            if ($isPrime[$u]) return 0;
            $sz = 1;
            foreach ($g[$u] as $v) if ($v !== $p) $sz += $dfs($v, $u);
            return $sz;
        };
        $ans = 0;
        for ($u = 1; $u <= $n; $u++) {
            if (!$isPrime[$u]) continue;
            $total = 0;
            foreach ($g[$u] as $v) {
                $c = $dfs($v, $u);
                $ans += $c;
                $ans += $total * $c;
                $total += $c;
            }
        }
        return $ans;
    }
}
''')

add("2868_the_wording_game", r'''<?php
// LeetCode 2868 - The Wording Game
// https://leetcode.com/problems/the-wording-game/

class Solution {
    function canAliceWin($a, $b) {
        $i = 0;
        $j = 0;
        $last = chr(0);
        $alice = true;
        while (true) {
            if ($alice) {
                while ($i < count($a) && $a[$i][0] <= $last) $i++;
                if ($i === count($a)) return false;
                $w = $a[$i];
                $last = $w[strlen($w) - 1];
                $i++;
            } else {
                while ($j < count($b) && $b[$j][0] <= $last) $j++;
                if ($j === count($b)) return true;
                $w = $b[$j];
                $last = $w[strlen($w) - 1];
                $j++;
            }
            $alice = !$alice;
        }
    }
}
''')

add("2869_minimum_operations_to_collect_elements", r'''<?php
// LeetCode 2869 - Minimum Operations to Collect Elements
// https://leetcode.com/problems/minimum-operations-to-collect-elements/

class Solution {
    function minOperations($nums, $k) {
        $need = [];
        for ($i = 1; $i <= $k; $i++) $need[$i] = true;
        $n = count($nums);
        for ($i = $n - 1; $i >= 0; $i--) {
            unset($need[$nums[$i]]);
            if (count($need) === 0) return $n - $i;
        }
        return $n;
    }
}
''')

add("2870_minimum_number_of_operations_to_make_array_empty", r'''<?php
// LeetCode 2870 - Minimum Number of Operations to Make Array Empty
// https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/

class Solution {
    function minOperations($nums) {
        $freq = [];
        foreach ($nums as $v) {
            if (!isset($freq[$v])) $freq[$v] = 0;
            $freq[$v]++;
        }
        $ans = 0;
        foreach ($freq as $c) {
            if ($c === 1) return -1;
            $ans += intdiv($c + 2, 3);
        }
        return $ans;
    }
}
''')

add("2871_split_array_into_maximum_number_of_subarrays", r'''<?php
// LeetCode 2871 - Split Array Into Maximum Number of Subarrays
// https://leetcode.com/problems/split-array-into-maximum-number-of-subarrays/

class Solution {
    function maxSubarrays($nums) {
        $ans = 0;
        $cur = -1;
        foreach ($nums as $v) {
            if ($cur === -1) $cur = $v;
            else $cur &= $v;
            if ($cur === 0) {
                $ans++;
                $cur = -1;
            }
        }
        return $ans === 0 ? 1 : $ans;
    }
}
''')

add("2872_maximum_number_of_k_divisible_components", r'''<?php
// LeetCode 2872 - Maximum Number of K-Divisible Components
// https://leetcode.com/problems/maximum-number-of-k-divisible-components/

class Solution {
    function maxKDivisibleComponents($n, $edges, $values, $k) {
        $g = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $g[$e[0]][] = $e[1];
            $g[$e[1]][] = $e[0];
        }
        $ans = 0;
        $dfs = function($u, $p) use (&$dfs, &$g, &$values, $k, &$ans) {
            $sum = $values[$u] % $k;
            foreach ($g[$u] as $v) {
                if ($v === $p) continue;
                $sum = ($sum + $dfs($v, $u)) % $k;
            }
            if ($sum === 0) $ans++;
            return $sum;
        };
        $dfs(0, -1);
        return $ans;
    }
}
''')

add("2873_maximum_value_of_an_ordered_triplet_i", r'''<?php
// LeetCode 2873 - Maximum Value of an Ordered Triplet I
// https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-i/

class Solution {
    function maximumTripletValue($nums) {
        $n = count($nums);
        $ans = 0;
        for ($i = 0; $i < $n; $i++)
            for ($j = $i + 1; $j < $n; $j++)
                for ($k = $j + 1; $k < $n; $k++) {
                    $cand = ($nums[$i] - $nums[$j]) * $nums[$k];
                    if ($cand > $ans) $ans = $cand;
                }
        return $ans;
    }
}
''')

add("2874_maximum_value_of_an_ordered_triplet_ii", r'''<?php
// LeetCode 2874 - Maximum Value of an Ordered Triplet II
// https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-ii/

class Solution {
    function maximumTripletValue($nums) {
        $ans = 0;
        $maxI = 0;
        $maxDiff = 0;
        foreach ($nums as $v) {
            if ($maxDiff * $v > $ans) $ans = $maxDiff * $v;
            if ($maxI - $v > $maxDiff) $maxDiff = $maxI - $v;
            if ($v > $maxI) $maxI = $v;
        }
        return $ans;
    }
}
''')

add("2875_minimum_size_subarray_in_infinite_array", r'''<?php
// LeetCode 2875 - Minimum Size Subarray in Infinite Array
// https://leetcode.com/problems/minimum-size-subarray-in-infinite-array/

class Solution {
    function minSizeSubarray($nums, $target) {
        $n = count($nums);
        $total = 0;
        foreach ($nums as $v) $total += $v;
        $INF = 1 << 30;
        $ans = $INF;
        if ($total > 0) {
            $loops = intdiv($target, $total);
            $remain = $target % $total;
            if ($remain === 0) return $loops * $n;
            $arr = array_merge($nums, $nums);
            $left = 0;
            $sum = 0;
            $best = $INF;
            $len = count($arr);
            for ($right = 0; $right < $len; $right++) {
                $sum += $arr[$right];
                while ($sum > $remain && $left <= $right) {
                    $sum -= $arr[$left];
                    $left++;
                }
                if ($sum === $remain && $right - $left + 1 < $best) $best = $right - $left + 1;
            }
            if ($best < $INF) $ans = $loops * $n + $best;
        }
        return $ans === $INF ? -1 : $ans;
    }
}
''')

add("2876_count_visited_nodes_in_a_directed_graph", r'''<?php
// LeetCode 2876 - Count Visited Nodes in a Directed Graph
// https://leetcode.com/problems/count-visited-nodes-in-a-directed-graph/

class Solution {
    function countVisitedNodes($edgesList) {
        $n = count($edgesList);
        $edges = $edgesList;
        $ans = array_fill(0, $n, 0);
        $state = array_fill(0, $n, 0);
        $stack = [];
        $dfs = function($u) use (&$dfs, &$edges, &$ans, &$state, &$stack) {
            $state[$u] = 1;
            $stack[] = $u;
            $v = $edges[$u];
            if ($state[$v] === 0) $dfs($v);
            else if ($state[$v] === 1) {
                $idx = count($stack) - 1;
                while ($stack[$idx] !== $v) $idx--;
                $cyc = count($stack) - $idx;
                for ($i = $idx; $i < count($stack); $i++) $ans[$stack[$i]] = $cyc;
            }
            if ($ans[$u] === 0) $ans[$u] = $ans[$edges[$u]] + 1;
            $state[$u] = 2;
            array_pop($stack);
        };
        for ($i = 0; $i < $n; $i++) if ($state[$i] === 0) $dfs($i);
        return $ans;
    }
}
''')

written = 0
for folder, body in SOLUTIONS.items():
    path = ROOT / folder / "solution.php"
    path.write_text(body, encoding="utf-8", newline="\n")
    written += 1
print(f"wrote {written}")

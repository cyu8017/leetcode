#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")

def w(folder, body):
    (ROOT / folder / "solution.php").write_text(body if body.endswith("\n") else body + "\n", encoding="utf-8")
    print("wrote", folder)

w("3461_check_if_digits_are_equal_in_string_after_operations_i", r'''<?php
// LeetCode 3461 - Check If Digits Are Equal in String After Operations I
// https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i/

class Solution {
    function hasSameDigits($s) {
        $b = str_split($s);
        while (count($b) > 2) {
            $nb = array_fill(0, count($b) - 1, "0");
            for ($i = 0; $i + 1 < count($b); $i++) {
                $nb[$i] = strval((ord($b[$i]) - 48 + ord($b[$i + 1]) - 48) % 10);
            }
            $b = $nb;
        }
        return $b[0] === $b[1];
    }
}
''')

w("3462_maximum_sum_with_at_most_k_elements", r'''<?php
// LeetCode 3462 - Maximum Sum With at Most K Elements
// https://leetcode.com/problems/maximum-sum-with-at-most-k-elements/

class Solution {
    function maxSum($grid, $limits, $k) {
        $h = [];
        $sum = 0;
        $push = function($v) use (&$h) {
            $h[] = $v;
            sort($h);
        };
        $poll = function() use (&$h) { return array_shift($h); };
        for ($i = 0; $i < count($grid); $i++) {
            $r = $grid[$i];
            sort($r);
            $lim = $limits[$i];
            if ($lim > count($r)) $lim = count($r);
            for ($j = 0; $j < $lim; $j++) {
                $val = $r[count($r) - 1 - $j];
                $push($val);
                $sum += $val;
                if (count($h) > $k) $sum -= $poll();
            }
        }
        return $sum;
    }
}
''')

w("3463_check_if_digits_are_equal_in_string_after_operations_ii", r'''<?php
// LeetCode 3463 - Check If Digits Are Equal in String After Operations II
// https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-ii/

class Solution {
    private function modPowP($a, $e, $p) {
        $r = 1;
        while ($e > 0) {
            if ($e % 2 === 1) $r = $r * $a % $p;
            $a = $a * $a % $p;
            $e = intdiv($e, 2);
        }
        return $r;
    }

    private function modInvPrime($a, $p) {
        return $this->modPowP($a, $p - 2, $p);
    }

    private function binomMod($n, $k, $p) {
        if ($k < 0 || $k > $n) return 0;
        $num = 1;
        $den = 1;
        for ($i = 0; $i < $k; $i++) {
            $num = $num * ($n - $i) % $p;
            $den = $den * ($i + 1) % $p;
        }
        return $num * $this->modInvPrime($den, $p) % $p;
    }

    private function crt($a1, $m1, $a2, $m2) {
        for ($x = 0; $x < $m1 * $m2; $x++) {
            if ($x % $m1 === $a1 && $x % $m2 === $a2) return $x;
        }
        return 0;
    }

    private function binomMod10($n, $k) {
        return $this->crt($this->binomMod($n, $k, 2), 2, $this->binomMod($n, $k, 5), 5);
    }

    private function combineDigit($s, $offset) {
        $n = strlen($s);
        $sum = 0;
        for ($i = 0; $i <= $n - 2; $i++) {
            $sum = ($sum + $this->binomMod10($n - 2, $i) * (ord($s[$i + $offset]) - 48)) % 10;
        }
        return $sum;
    }

    function hasSameDigits($s) {
        return $this->combineDigit($s, 0) === $this->combineDigit($s, 1);
    }
}
''')

w("3464_maximize_the_distance_between_points_on_a_square", r'''<?php
// LeetCode 3464 - Maximize the Distance Between Points on a Square
// https://leetcode.com/problems/maximize-the-distance-between-points-on-a-square/

class Solution {
    private function canPlace($arr, $perim, $mid, $k) {
        $n = count($arr);
        for ($s = 0; $s < $n; $s++) {
            $cnt = 1;
            $last = $arr[$s];
            $idx = $s;
            for (; $cnt < $k; ) {
                $target = $last + $mid;
                $found = false;
                for ($step = 1; $step < $n; $step++) {
                    $ni = ($idx + $step) % $n;
                    $val = $arr[$ni];
                    $add = $ni <= $idx ? $perim : 0;
                    if ($val + $add >= $target) {
                        $last = $val + $add;
                        $idx = $ni;
                        $cnt++;
                        $found = true;
                        break;
                    }
                }
                if (!$found) break;
            }
            if ($cnt === $k && $last - $arr[$s] <= $perim - $mid) return true;
        }
        return false;
    }

    function maxDistance($side, $points, $k) {
        $arr = array_fill(0, count($points), 0);
        for ($i = 0; $i < count($points); $i++) {
            $x = $points[$i][0];
            $y = $points[$i][1];
            if ($y === 0) $d = $x;
            else if ($x === $side) $d = $side + $y;
            else if ($y === $side) $d = 2 * $side + ($side - $x);
            else $d = 3 * $side + ($side - $y);
            $arr[$i] = $d;
        }
        sort($arr);
        $perim = 4 * $side;
        $lo = 0;
        $hi = 2 * $side;
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi + 1, 2);
            if ($this->canPlace($arr, $perim, $mid, $k)) $lo = $mid;
            else $hi = $mid - 1;
        }
        return $lo;
    }
}
''')

w("3466_maximum_coin_collection", r'''<?php
// LeetCode 3466 - Maximum Coin Collection
// https://leetcode.com/problems/maximum-coin-collection/

class Solution {
    function maxCoins($lane1, $lane2) {
        $n = count($lane1);
        $neg = intdiv(PHP_INT_MIN, 4);
        $dp = [[$lane1[0], $neg], [$lane2[0], $neg]];
        $ans = max($dp[0][0], $dp[1][0]);
        for ($i = 1; $i < $n; $i++) {
            $ndp = [[0, 0], [0, 0]];
            $ndp[0][0] = max($dp[0][0], 0) + $lane1[$i];
            $ndp[1][0] = max($dp[1][0], 0) + $lane2[$i];
            $ndp[0][1] = max($dp[0][1], $dp[1][0]) + $lane1[$i];
            $ndp[1][1] = max($dp[1][1], $dp[0][0]) + $lane2[$i];
            if ($lane1[$i] > $ndp[0][0]) $ndp[0][0] = $lane1[$i];
            if ($lane2[$i] > $ndp[1][0]) $ndp[1][0] = $lane2[$i];
            for ($a = 0; $a < 2; $a++)
                for ($b = 0; $b < 2; $b++) {
                    $dp[$a][$b] = $ndp[$a][$b];
                    if ($dp[$a][$b] > $ans) $ans = $dp[$a][$b];
                }
        }
        return $ans;
    }
}
''')

w("3467_transform_array_by_parity", r'''<?php
// LeetCode 3467 - Transform Array by Parity
// https://leetcode.com/problems/transform-array-by-parity/

class Solution {
    function transformArray($nums) {
        for ($i = 0; $i < count($nums); $i++) $nums[$i] %= 2;
        $j = 0;
        for ($i = 0; $i < count($nums); $i++) {
            if ($nums[$i] === 0) {
                $t = $nums[$i]; $nums[$i] = $nums[$j]; $nums[$j] = $t;
                $j++;
            }
        }
        return $nums;
    }
}
''')

w("3468_find_the_number_of_copy_arrays", r'''<?php
// LeetCode 3468 - Find the Number of Copy Arrays
// https://leetcode.com/problems/find-the-number-of-copy-arrays/

class Solution {
    function countArrays($original, $bounds) {
        $n = count($original);
        $lo = $bounds[0][0];
        $hi = $bounds[0][1];
        for ($i = 1; $i < $n; $i++) {
            $diff = $original[$i] - $original[$i - 1];
            $lo2 = $bounds[$i][0];
            $hi2 = $bounds[$i][1];
            $nlo = $lo + $diff;
            $nhi = $hi + $diff;
            if ($nlo < $lo2) $nlo = $lo2;
            if ($nhi > $hi2) $nhi = $hi2;
            if ($nlo > $nhi) return 0;
            $lo = $nlo;
            $hi = $nhi;
        }
        return $hi - $lo + 1;
    }
}
''')

w("3469_find_minimum_cost_to_remove_array_elements", r'''<?php
// LeetCode 3469 - Find Minimum Cost to Remove Array Elements
// https://leetcode.com/problems/find-minimum-cost-to-remove-array-elements/

class Solution {
    function minCost($nums) {
        $n = count($nums);
        $memo = [];
        $max2 = function($a, $b) { return $a > $b ? $a : $b; };
        $min3 = function($a, $b, $c) { return min($a, min($b, $c)); };
        $dfs = null;
        $dfs = function($i, $prev) use (&$dfs, $n, $nums, &$memo, $max2, $min3) {
            if ($i >= $n) return $prev === -1 ? 0 : $nums[$prev];
            $k = $i . "," . $prev;
            if (isset($memo[$k])) return $memo[$k];
            if ($prev === -1) {
                if ($i + 1 >= $n) $res = $nums[$i];
                else if ($i + 2 >= $n) $res = $max2($nums[$i], $nums[$i + 1]);
                else {
                    $a = $nums[$i]; $b = $nums[$i + 1]; $c = $nums[$i + 2];
                    $res = $min3($max2($b, $c) + $dfs($i + 3, $i), $max2($a, $c) + $dfs($i + 3, $i + 1), $max2($a, $b) + $dfs($i + 3, $i + 2));
                }
            } else {
                if ($i + 1 >= $n) $res = $max2($nums[$prev], $nums[$i]);
                else {
                    $a = $nums[$prev]; $b = $nums[$i]; $c = $nums[$i + 1];
                    $res = $min3($max2($b, $c) + $dfs($i + 2, $prev), $max2($a, $c) + $dfs($i + 2, $i), $max2($a, $b) + $dfs($i + 2, $i + 1));
                }
            }
            $memo[$k] = $res;
            return $res;
        };
        return $dfs(0, -1);
    }
}
''')

w("3470_permutations_iv", r'''<?php
// LeetCode 3470 - Permutations IV
// https://leetcode.com/problems/permutations-iv/

class Solution {
    function permute($n, $k) {
        $fact = array_fill(0, $n + 1, 1);
        $cap = 10 ** 18 + 1;
        for ($i = 1; $i <= $n; $i++) {
            $fact[$i] = $fact[$i - 1] * $i;
            if ($fact[$i] > $cap) $fact[$i] = $cap;
        }
        $used = array_fill(0, $n + 1, false);
        $ans = [];
        $kk = $k;
        $dfs = null;
        $dfs = function($pos) use (&$dfs, $n, &$kk, $fact, &$used, &$ans) {
            if ($pos === $n) return true;
            for ($x = 1; $x <= $n; $x++) {
                if ($used[$x]) continue;
                if ($pos > 0 && ($ans[$pos - 1] % 2 === $x % 2)) continue;
                $rem = $n - $pos - 1;
                $cnt = $fact[$rem];
                if ($cnt >= $kk) {
                    $used[$x] = true;
                    $ans[] = $x;
                    if ($dfs($pos + 1)) return true;
                    array_pop($ans);
                    $used[$x] = false;
                } else {
                    $kk -= $cnt;
                }
            }
            return false;
        };
        if (!$dfs(0)) return [];
        return $ans;
    }
}
''')

w("3471_find_the_largest_almost_missing_integer", r'''<?php
// LeetCode 3471 - Find the Largest Almost Missing Integer
// https://leetcode.com/problems/find-the-largest-almost-missing-integer/

class Solution {
    function largestInteger($nums, $k) {
        $n = count($nums);
        $cnt = [];
        for ($i = 0; $i + $k <= $n; $i++) {
            $seen = [];
            for ($j = $i; $j < $i + $k; $j++) $seen[$nums[$j]] = true;
            foreach ($seen as $x => $_) $cnt[$x] = ($cnt[$x] ?? 0) + 1;
        }
        $ans = -1;
        foreach ($cnt as $key => $value) {
            if ($value === 1 && $key > $ans) $ans = $key;
        }
        return $ans;
    }
}
''')

w("3472_longest_palindromic_subsequence_after_at_most_k_operations", r'''<?php
// LeetCode 3472 - Longest Palindromic Subsequence After at Most K Operations
// https://leetcode.com/problems/longest-palindromic-subsequence-after-at-most-k-operations/

class Solution {
    private function distCirc($a, $b) {
        $d = abs(ord($a) - ord($b));
        return min($d, 26 - $d);
    }

    function longestPalindromicSubsequence($s, $k) {
        $n = strlen($s);
        $dp = [];
        for ($i = 0; $i < $n; $i++) {
            $dp[$i] = [];
            for ($j = 0; $j < $n; $j++) $dp[$i][$j] = array_fill(0, $k + 1, -1);
        }
        $dfs = null;
        $dfs = function($i, $j, $ops) use (&$dfs, $s, &$dp) {
            if ($i > $j) return 0;
            if ($i === $j) return 1;
            if ($dp[$i][$j][$ops] !== -1) return $dp[$i][$j][$ops];
            $best = $dfs($i + 1, $j, $ops);
            $best = max($best, $dfs($i, $j - 1, $ops));
            $cost = $this->distCirc($s[$i], $s[$j]);
            if ($cost <= $ops) $best = max($best, 2 + $dfs($i + 1, $j - 1, $ops - $cost));
            return $dp[$i][$j][$ops] = $best;
        };
        return $dfs(0, $n - 1, $k);
    }
}
''')

w("3473_sum_of_k_subarrays_with_length_at_least_m", r'''<?php
// LeetCode 3473 - Sum of K Subarrays With Length at Least M
// https://leetcode.com/problems/sum-of-k-subarrays-with-length-at-least-m/

class Solution {
    function maxSum($nums, $k, $m) {
        $n = count($nums);
        $pref = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; $i++) $pref[$i + 1] = $pref[$i] + $nums[$i];
        $neg = intdiv(PHP_INT_MIN, 4);
        $dp = [];
        for ($t = 0; $t <= $k; $t++) $dp[$t] = array_fill(0, $n + 1, $neg);
        for ($i = 0; $i <= $n; $i++) $dp[0][$i] = 0;
        for ($t = 1; $t <= $k; $t++) {
            $best = $neg;
            for ($i = $t * $m; $i <= $n; $i++) {
                $j = $i - $m;
                $best = max($best, $dp[$t - 1][$j] - $pref[$j]);
                $dp[$t][$i] = $best + $pref[$i];
            }
            for ($i = 1; $i <= $n; $i++) $dp[$t][$i] = max($dp[$t][$i], $dp[$t][$i - 1]);
        }
        return $dp[$k][$n];
    }
}
''')

w("3474_lexicographically_smallest_generated_string", r'''<?php
// LeetCode 3474 - Lexicographically Smallest Generated String
// https://leetcode.com/problems/lexicographically-smallest-generated-string/

class Solution {
    function generateString($str1, $str2) {
        $n = strlen($str1);
        $m = strlen($str2);
        $L = $n + $m - 1;
        $ans = array_fill(0, $L, "?");
        for ($i = 0; $i < $n; $i++) {
            if ($str1[$i] === "T") {
                for ($j = 0; $j < $m; $j++) {
                    if ($ans[$i + $j] !== "?" && $ans[$i + $j] !== $str2[$j]) return "";
                    $ans[$i + $j] = $str2[$j];
                }
            }
        }
        for ($i = 0; $i < $L; $i++) if ($ans[$i] === "?") $ans[$i] = "a";
        for ($i = 0; $i < $n; $i++) {
            if ($str1[$i] === "F") {
                $match = true;
                for ($j = 0; $j < $m; $j++) if ($ans[$i + $j] !== $str2[$j]) { $match = false; break; }
                if ($match) {
                    $changed = false;
                    for ($j = $m - 1; $j >= 0; $j--) {
                        $pos = $i + $j;
                        $forced = false;
                        for ($t = 0; $t < $n; $t++) {
                            if ($str1[$t] === "T" && $pos >= $t && $pos < $t + $m) { $forced = true; break; }
                        }
                        if (!$forced) {
                            $ans[$pos] = "b";
                            $changed = true;
                            break;
                        }
                    }
                    if (!$changed) return "";
                }
            }
        }
        for ($i = 0; $i < $n; $i++) {
            $match = true;
            for ($j = 0; $j < $m; $j++) if ($ans[$i + $j] !== $str2[$j]) { $match = false; break; }
            if ($str1[$i] === "T" && !$match) return "";
            if ($str1[$i] === "F" && $match) return "";
        }
        return implode("", $ans);
    }
}
''')

w("3476_maximize_profit_from_task_assignment", r'''<?php
// LeetCode 3476 - Maximize Profit from Task Assignment
// https://leetcode.com/problems/maximize-profit-from-task-assignment/

class Solution {
    function maxProfit($workers, $tasks) {
        sort($workers);
        usort($tasks, function($a, $b) { return $a[0] <=> $b[0]; });
        $ans = 0;
        $used = array_fill(0, count($tasks), false);
        foreach ($workers as $w) {
            $best = -1;
            $bi = -1;
            for ($i = 0; $i < count($tasks); $i++) {
                if ($used[$i]) continue;
                if ($tasks[$i][0] > $w) break;
                if ($tasks[$i][1] > $best) {
                    $best = $tasks[$i][1];
                    $bi = $i;
                }
            }
            if ($bi >= 0) {
                $used[$bi] = true;
                $ans += $best;
            }
        }
        return $ans;
    }
}
''')

w("3477_fruits_into_baskets_ii", r'''<?php
// LeetCode 3477 - Fruits Into Baskets II
// https://leetcode.com/problems/fruits-into-baskets-ii/

class Solution {
    function numOfUnplacedFruits($fruits, $baskets) {
        $used = array_fill(0, count($baskets), false);
        $unplaced = 0;
        foreach ($fruits as $f) {
            $placed = false;
            for ($j = 0; $j < count($baskets); $j++) {
                if (!$used[$j] && $baskets[$j] >= $f) {
                    $used[$j] = true;
                    $placed = true;
                    break;
                }
            }
            if (!$placed) $unplaced++;
        }
        return $unplaced;
    }
}
''')

print("e done")

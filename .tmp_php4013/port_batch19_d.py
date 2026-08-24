#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
SOLUTIONS = {}

def add(folder, body):
    SOLUTIONS[folder] = body


add("3693_climbing_stairs_ii", r'''<?php
// LeetCode 3693 - Climbing Stairs II
// https://leetcode.com/problems/climbing-stairs-ii/

class Solution {
    function climbStairs($n, $costs) {
        $inf = 1000000000;
        $f = array_fill(0, $n + 1, $inf);
        $f[0] = 0;
        for ($i = 1; $i <= $n; $i++) {
            $x = $costs[$i - 1];
            for ($j = max(0, $i - 3); $j < $i; $j++) {
                $f[$i] = min($f[$i], $f[$j] + $x + ($i - $j) * ($i - $j));
            }
        }
        return $f[$n];
    }
}
''')

add("3694_distinct_points_reachable_after_substring_removal", r'''<?php
// LeetCode 3694 - Distinct Points Reachable After Substring Removal
// https://leetcode.com/problems/distinct-points-reachable-after-substring-removal/

class Solution {
    function distinctPoints($s, $k) {
        $n = strlen($s);
        $f = array_fill(0, $n + 1, 0);
        $g = array_fill(0, $n + 1, 0);
        $x = 0;
        $y = 0;
        for ($i = 1; $i <= $n; $i++) {
            $c = $s[$i - 1];
            if ($c === 'U') $y++;
            else if ($c === 'D') $y--;
            else if ($c === 'L') $x--;
            else $x++;
            $f[$i] = $x;
            $g[$i] = $y;
        }
        $st = [];
        for ($i = $k; $i <= $n; $i++) {
            $a = $f[$n] - ($f[$i] - $f[$i - $k]);
            $b = $g[$n] - ($g[$i] - $g[$i - $k]);
            $st[$a . ',' . $b] = true;
        }
        return count($st);
    }
}
''')

add("3695_maximize_alternating_sum_using_swaps", r'''<?php
// LeetCode 3695 - Maximize Alternating Sum Using Swaps
// https://leetcode.com/problems/maximize-alternating-sum-using-swaps/

class Solution {
    function maxAlternatingSum($nums, $swaps) {
        $n = count($nums);
        $parent = range(0, $n - 1);
        $find = function($x) use (&$parent, &$find) {
            if ($parent[$x] !== $x) $parent[$x] = $find($parent[$x]);
            return $parent[$x];
        };
        foreach ($swaps as $s) {
            $a = $find($s[0]);
            $b = $find($s[1]);
            if ($a !== $b) $parent[$a] = $b;
        }
        $compVals = [];
        $compIdx = [];
        for ($i = 0; $i < $n; $i++) {
            $r = $find($i);
            if (!isset($compVals[$r])) { $compVals[$r] = []; $compIdx[$r] = []; }
            $compVals[$r][] = $nums[$i];
            $compIdx[$r][] = $i;
        }
        $arr = array_fill(0, $n, 0);
        foreach ($compVals as $r => $vals) {
            $idxs = $compIdx[$r];
            rsort($vals);
            $even = [];
            $odd = [];
            foreach ($idxs as $i) {
                if ($i % 2 === 0) $even[] = $i;
                else $odd[] = $i;
            }
            sort($even);
            sort($odd);
            $ei = 0;
            $en = count($even);
            foreach ($vals as $v) {
                if ($ei < $en) {
                    $arr[$even[$ei]] = $v;
                    $ei++;
                } else {
                    $arr[$odd[$ei - $en]] = $v;
                    $ei++;
                }
            }
        }
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            if ($i % 2 === 0) $ans += $arr[$i];
            else $ans -= $arr[$i];
        }
        return $ans;
    }
}
''')

add("3696_maximum_distance_between_unequal_words_in_array_i", r'''<?php
// LeetCode 3696 - Maximum Distance Between Unequal Words in Array I
// https://leetcode.com/problems/maximum-distance-between-unequal-words-in-array-i/

class Solution {
    function maxDistance($words) {
        $n = count($words);
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            if ($words[$i] !== $words[0]) $ans = max($ans, $i + 1);
            if ($words[$i] !== $words[$n - 1]) $ans = max($ans, $n - $i);
        }
        return $ans;
    }
}
''')

add("3697_compute_decimal_representation", r'''<?php
// LeetCode 3697 - Compute Decimal Representation
// https://leetcode.com/problems/compute-decimal-representation/

class Solution {
    function decimalRepresentation($n) {
        $ans = [];
        $p = 1;
        while ($n > 0) {
            $v = $n % 10;
            $n = intdiv($n, 10);
            if ($v !== 0) $ans[] = $p * $v;
            $p *= 10;
        }
        return array_reverse($ans);
    }
}
''')

add("3698_split_array_with_minimum_difference", r'''<?php
// LeetCode 3698 - Split Array With Minimum Difference
// https://leetcode.com/problems/split-array-with-minimum-difference/

class Solution {
    function splitArray($nums) {
        $n = count($nums);
        $s = array_fill(0, $n, 0);
        $f = array_fill(0, $n, true);
        $g = array_fill(0, $n, true);
        $s[0] = $nums[0];
        for ($i = 1; $i < $n; $i++) {
            $s[$i] = $s[$i - 1] + $nums[$i];
            $f[$i] = $f[$i - 1];
            if ($nums[$i] <= $nums[$i - 1]) $f[$i] = false;
        }
        for ($i = $n - 2; $i >= 0; $i--) {
            $g[$i] = $g[$i + 1];
            if ($nums[$i] <= $nums[$i + 1]) $g[$i] = false;
        }
        $inf = PHP_INT_MAX >> 2;
        $ans = $inf;
        for ($i = 0; $i < $n - 1; $i++) {
            if ($f[$i] && $g[$i + 1]) {
                $s1 = $s[$i];
                $s2 = $s[$n - 1] - $s[$i];
                $ans = min($ans, abs($s1 - $s2));
            }
        }
        return $ans < $inf ? $ans : -1;
    }
}
''')

add("3699_number_of_zigzag_arrays_i", r'''<?php
// LeetCode 3699 - Number of ZigZag Arrays I
// https://leetcode.com/problems/number-of-zigzag-arrays-i/

class Solution {
    function zigZagArrays($n, $l, $r) {
        $MOD = 1000000007;
        $m = $r - $l + 1;
        if ($n === 1) return $m % $MOD;
        $up = array_fill(0, $m, 1);
        $down = array_fill(0, $m, 1);
        for ($len_ = 2; $len_ <= $n; $len_++) {
            $prefDown = array_fill(0, $m + 1, 0);
            for ($j = 0; $j < $m; $j++) $prefDown[$j + 1] = ($prefDown[$j] + $down[$j]) % $MOD;
            $nup = [];
            for ($j = 0; $j < $m; $j++) $nup[$j] = $prefDown[$j];
            $sufUp = array_fill(0, $m + 1, 0);
            for ($j = $m - 1; $j >= 0; $j--) $sufUp[$j] = ($sufUp[$j + 1] + $up[$j]) % $MOD;
            $ndown = [];
            for ($j = 0; $j < $m; $j++) $ndown[$j] = $sufUp[$j + 1];
            $up = $nup;
            $down = $ndown;
        }
        $ans = 0;
        for ($j = 0; $j < $m; $j++) {
            $ans = ($ans + $up[$j]) % $MOD;
            $ans = ($ans + $down[$j]) % $MOD;
        }
        return $ans;
    }
}
''')

add("3700_number_of_zigzag_arrays_ii", r'''<?php
// LeetCode 3700 - Number of ZigZag Arrays II
// https://leetcode.com/problems/number-of-zigzag-arrays-ii/

class Solution {
    function zigZagArrays($n, $l, $r) {
        $MOD = 1000000007;
        $m = $r - $l + 1;
        if ($n === 1) return $m % $MOD;
        $up = array_fill(0, $m, 1);
        $down = array_fill(0, $m, 1);
        for ($length = 2; $length <= $n; $length++) {
            $pref = array_fill(0, $m + 1, 0);
            for ($j = 0; $j < $m; $j++) $pref[$j + 1] = ($pref[$j] + $down[$j]) % $MOD;
            $nup = [];
            for ($j = 0; $j < $m; $j++) $nup[$j] = $pref[$j];
            $suf = array_fill(0, $m + 1, 0);
            for ($j = $m - 1; $j >= 0; $j--) $suf[$j] = ($suf[$j + 1] + $up[$j]) % $MOD;
            $ndown = [];
            for ($j = 0; $j < $m; $j++) $ndown[$j] = $suf[$j + 1];
            $up = $nup;
            $down = $ndown;
        }
        $ans = 0;
        for ($j = 0; $j < $m; $j++) {
            $ans = ($ans + $up[$j]) % $MOD;
            $ans = ($ans + $down[$j]) % $MOD;
        }
        return $ans;
    }
}
''')

add("3701_compute_alternating_sum", r'''<?php
// LeetCode 3701 - Compute Alternating Sum
// https://leetcode.com/problems/compute-alternating-sum/

class Solution {
    function alternatingSum($nums) {
        $ans = 0;
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            if ($i % 2 === 0) $ans += $nums[$i];
            else $ans -= $nums[$i];
        }
        return $ans;
    }
}
''')

add("3702_longest_subsequence_with_non_zero_bitwise_xor", r'''<?php
// LeetCode 3702 - Longest Subsequence With Non-Zero Bitwise XOR
// https://leetcode.com/problems/longest-subsequence-with-non-zero-bitwise-xor/

class Solution {
    function longestSubsequence($nums) {
        $xorv = 0;
        $cnt0 = 0;
        foreach ($nums as $x) {
            $xorv ^= $x;
            if ($x === 0) $cnt0++;
        }
        $n = count($nums);
        if ($xorv !== 0) return $n;
        if ($cnt0 === $n) return 0;
        return $n - 1;
    }
}
''')

add("3703_remove_k_balanced_substrings", r'''<?php
// LeetCode 3703 - Remove K-Balanced Substrings
// https://leetcode.com/problems/remove-k-balanced-substrings/

class Solution {
    function removeSubstring($s, $k) {
        $stk = [];
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $c = $s[$i];
            $sn = count($stk);
            if ($sn && $stk[$sn - 1][0] === $c)
                $stk[$sn - 1][1]++;
            else $stk[] = [$c, 1];
            $sn = count($stk);
            if ($c === ')' && $sn > 1) {
                $top = $stk[$sn - 1];
                if ($top[1] === $k && $stk[$sn - 2][1] >= $k) {
                    array_pop($stk);
                    $stk[$sn - 2][1] -= $k;
                    if ($stk[$sn - 2][1] === 0) array_pop($stk);
                }
            }
        }
        $res = '';
        foreach ($stk as $p)
            for ($i = 0; $i < $p[1]; $i++) $res .= $p[0];
        return $res;
    }
}
''')

add("3704_count_no_zero_pairs_that_sum_to_n", r'''<?php
// LeetCode 3704 - Count No-Zero Pairs That Sum to N
// https://leetcode.com/problems/count-no-zero-pairs-that-sum-to-n/

class Solution {
    function countNoZeroPairs($n) {
        $s = (string)$n;
        $m = strlen($s);
        $digits = array_fill(0, $m + 1, 0);
        for ($i = 0; $i < $m; $i++) $digits[$i] = ord($s[$m - 1 - $i]) - 48;
        $dp = [];
        for ($c = 0; $c < 2; $c++)
            for ($a = 0; $a < 2; $a++)
                $dp[$c][$a] = [0, 0];
        $dp[0][1][1] = 1;
        for ($pos = 0; $pos < $m + 1; $pos++) {
            $ndp = [];
            for ($c = 0; $c < 2; $c++)
                for ($a = 0; $a < 2; $a++)
                    $ndp[$c][$a] = [0, 0];
            $target = $digits[$pos];
            for ($carry = 0; $carry <= 1; $carry++) {
                for ($aliveA = 0; $aliveA <= 1; $aliveA++) {
                    for ($aliveB = 0; $aliveB <= 1; $aliveB++) {
                        $ways = $dp[$carry][$aliveA][$aliveB];
                        if ($ways === 0) continue;
                        $A = [];
                        if ($aliveA === 1) {
                            for ($d = 1; $d <= 9; $d++) $A[] = [$d, 1];
                            if ($pos > 0) $A[] = [0, 0];
                        } else {
                            $A[] = [0, 0];
                        }
                        $B = [];
                        if ($aliveB === 1) {
                            for ($d = 1; $d <= 9; $d++) $B[] = [$d, 1];
                            if ($pos > 0) $B[] = [0, 0];
                        } else {
                            $B[] = [0, 0];
                        }
                        foreach ($A as $pa) {
                            $da = $pa[0];
                            $na = $pa[1];
                            foreach ($B as $pb) {
                                $db = $pb[0];
                                $nb = $pb[1];
                                $sum = $da + $db + $carry;
                                if ($sum % 10 !== $target) continue;
                                $ncarry = intdiv($sum, 10);
                                $ndp[$ncarry][$na][$nb] += $ways;
                            }
                        }
                    }
                }
            }
            $dp = $ndp;
        }
        return $dp[0][0][0];
    }
}
''')

add("3706_maximum_distance_between_unequal_words_in_array_ii", r'''<?php
// LeetCode 3706 - Maximum Distance Between Unequal Words in Array II
// https://leetcode.com/problems/maximum-distance-between-unequal-words-in-array-ii/

class Solution {
    function maxDistance($words) {
        $n = count($words);
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            if ($words[$i] !== $words[0]) $ans = max($ans, $i + 1);
            if ($words[$i] !== $words[$n - 1]) $ans = max($ans, $n - $i);
        }
        return $ans;
    }
}
''')

add("3707_equal_score_substrings", r'''<?php
// LeetCode 3707 - Equal Score Substrings
// https://leetcode.com/problems/equal-score-substrings/

class Solution {
    function scoreBalance($s) {
        $l = 0;
        $r = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) $r += (ord($s[$i]) - 97) + 1;
        for ($i = 0; $i + 1 < $n; $i++) {
            $x = (ord($s[$i]) - 97) + 1;
            $l += $x;
            $r -= $x;
            if ($l === $r) return true;
        }
        return false;
    }
}
''')

add("3708_longest_fibonacci_subarray", r'''<?php
// LeetCode 3708 - Longest Fibonacci Subarray
// https://leetcode.com/problems/longest-fibonacci-subarray/

class Solution {
    function longestSubarray($nums) {
        $f = 2;
        $ans = $f;
        $n = count($nums);
        for ($i = 2; $i < $n; $i++) {
            if ($nums[$i] === $nums[$i - 1] + $nums[$i - 2]) {
                $f++;
                $ans = max($ans, $f);
            } else $f = 2;
        }
        return $ans;
    }
}
''')

add("3709_design_exam_scores_tracker", r'''<?php
// LeetCode 3709 - Design Exam Scores Tracker
// https://leetcode.com/problems/design-exam-scores-tracker/

class ExamTracker {
    private $times;
    private $pre;

    function __construct() {
        $this->times = [0];
        $this->pre = [0];
    }

    function record($time, $score) {
        $this->times[] = $time;
        $this->pre[] = $this->pre[count($this->pre) - 1] + $score;
    }

    function totalScore($startTime, $endTime) {
        $lowerBound = function($a, $target) {
            $lo = 0;
            $hi = count($a);
            while ($lo < $hi) {
                $mid = ($lo + $hi) >> 1;
                if ($a[$mid] < $target) $lo = $mid + 1;
                else $hi = $mid;
            }
            return $lo;
        };
        $l = $lowerBound($this->times, $startTime) - 1;
        $r = $lowerBound($this->times, $endTime + 1) - 1;
        return $this->pre[$r] - $this->pre[$l];
    }
}
''')

add("3710_maximum_partition_factor", r'''<?php
// LeetCode 3710 - Maximum Partition Factor
// https://leetcode.com/problems/maximum-partition-factor/

class Solution {
    function maxPartitionFactor($points) {
        $n = count($points);
        if ($n === 2) return 0;
        $dist = function($i, $j) use ($points) {
            return abs($points[$i][0] - $points[$j][0]) + abs($points[$i][1] - $points[$j][1]);
        };
        $ok = function($d) use ($n, $dist) {
            $g = array_fill(0, $n, []);
            for ($i = 0; $i < $n; $i++) {
                for ($j = $i + 1; $j < $n; $j++) {
                    if ($dist($i, $j) < $d) {
                        $g[$i][] = $j;
                        $g[$j][] = $i;
                    }
                }
            }
            $color = array_fill(0, $n, -1);
            for ($i = 0; $i < $n; $i++) {
                if ($color[$i] !== -1) continue;
                $q = [$i];
                $color[$i] = 0;
                while ($q) {
                    $u = array_shift($q);
                    foreach ($g[$u] as $v) {
                        if ($color[$v] === -1) {
                            $color[$v] = $color[$u] ^ 1;
                            $q[] = $v;
                        } else if ($color[$v] === $color[$u]) return false;
                    }
                }
            }
            return true;
        };
        $lo = 0;
        $hi = 0;
        for ($i = 0; $i < $n; $i++)
            for ($j = $i + 1; $j < $n; $j++)
                $hi = max($hi, $dist($i, $j));
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi + 1, 2);
            if ($ok($mid)) $lo = $mid;
            else $hi = $mid - 1;
        }
        return $lo;
    }
}
''')

add("3711_maximum_transactions_without_negative_balance", r'''<?php
// LeetCode 3711 - Maximum Transactions Without Negative Balance
// https://leetcode.com/problems/maximum-transactions-without-negative-balance/

class Solution {
    function maxTransactions($transactions) {
        $tm = [];
        $ans = count($transactions);
        $s = 0;
        foreach ($transactions as $x) {
            $s += $x;
            if (!isset($tm[$x])) $tm[$x] = 0;
            $tm[$x]++;
            while ($s < 0) {
                $y = null;
                foreach ($tm as $k => $_) {
                    if ($y === null || $k < $y) $y = $k;
                }
                $s -= $y;
                $ans--;
                $c = $tm[$y];
                if ($c === 1) unset($tm[$y]);
                else $tm[$y] = $c - 1;
            }
        }
        return $ans;
    }
}
''')

add("3712_sum_of_elements_with_frequency_divisible_by_k", r'''<?php
// LeetCode 3712 - Sum of Elements With Frequency Divisible by K
// https://leetcode.com/problems/sum-of-elements-with-frequency-divisible-by-k/

class Solution {
    function sumDivisibleByK($nums, $k) {
        $cnt = [];
        foreach ($nums as $x) {
            if (!isset($cnt[$x])) $cnt[$x] = 0;
            $cnt[$x]++;
        }
        $ans = 0;
        foreach ($cnt as $key => $val) {
            if ($val % $k === 0) $ans += $key * $val;
        }
        return $ans;
    }
}
''')

add("3713_longest_balanced_substring_i", r'''<?php
// LeetCode 3713 - Longest Balanced Substring I
// https://leetcode.com/problems/longest-balanced-substring-i/

class Solution {
    function longestBalanced($s) {
        $n = strlen($s);
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            $cnt = array_fill(0, 26, 0);
            $mx = 0;
            $v = 0;
            for ($j = $i; $j < $n; $j++) {
                $c = ord($s[$j]) - 97;
                $cnt[$c]++;
                if ($cnt[$c] === 1) $v++;
                $mx = max($mx, $cnt[$c]);
                if ($mx * $v === $j - $i + 1) $ans = max($ans, $j - $i + 1);
            }
        }
        return $ans;
    }
}
''')

add("3714_longest_balanced_substring_ii", r'''<?php
// LeetCode 3714 - Longest Balanced Substring II
// https://leetcode.com/problems/longest-balanced-substring-ii/

class Solution {
    function longestBalanced($s) {
        $calc1 = function($str) {
            $res = 0;
            $n = strlen($str);
            $i = 0;
            while ($i < $n) {
                $j = $i + 1;
                while ($j < $n && $str[$j] === $str[$i]) $j++;
                $res = max($res, $j - $i);
                $i = $j;
            }
            return $res;
        };
        $calc2 = function($str, $a, $b) {
            $res = 0;
            $n = strlen($str);
            $i = 0;
            while ($i < $n) {
                while ($i < $n && $str[$i] !== $a && $str[$i] !== $b) $i++;
                $pos = [];
                $pos[0] = $i - 1;
                $d = 0;
                while ($i < $n && ($str[$i] === $a || $str[$i] === $b)) {
                    if ($str[$i] === $a) $d++;
                    else $d--;
                    if (isset($pos[$d])) $res = max($res, $i - $pos[$d]);
                    else $pos[$d] = $i;
                    $i++;
                }
            }
            return $res;
        };
        $calc3 = function($str) {
            $pos = [];
            $pos['0,0'] = -1;
            $cnt = [0, 0, 0];
            $res = 0;
            $n = strlen($str);
            for ($i = 0; $i < $n; $i++) {
                $cnt[ord($str[$i]) - 97]++;
                $x = $cnt[0] - $cnt[1];
                $y = $cnt[1] - $cnt[2];
                $k = $x . ',' . $y;
                if (isset($pos[$k])) $res = max($res, $i - $pos[$k]);
                else $pos[$k] = $i;
            }
            return $res;
        };
        $x = $calc1($s);
        $y = max($calc2($s, 'a', 'b'), max($calc2($s, 'b', 'c'), $calc2($s, 'a', 'c')));
        $z = $calc3($s);
        return max($x, max($y, $z));
    }
}
''')

add("3715_sum_of_perfect_square_ancestors", r'''<?php
// LeetCode 3715 - Sum of Perfect Square Ancestors
// https://leetcode.com/problems/sum-of-perfect-square-ancestors/

class Solution {
    function sumOfAncestors($n, $edges, $nums) {
        $graph = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $graph[$e[0]][] = $e[1];
            $graph[$e[1]][] = $e[0];
        }
        $kernel = function($x) {
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
        $ks = [];
        for ($i = 0; $i < $n; $i++) $ks[$i] = $kernel($nums[$i]);
        $freq = [];
        $ans = 0;
        $dfs = function($u, $p) use (&$dfs, &$freq, &$ans, $ks, $graph) {
            $ans += isset($freq[$ks[$u]]) ? $freq[$ks[$u]] : 0;
            if (!isset($freq[$ks[$u]])) $freq[$ks[$u]] = 0;
            $freq[$ks[$u]]++;
            foreach ($graph[$u] as $v) if ($v !== $p) $dfs($v, $u);
            $freq[$ks[$u]]--;
        };
        $dfs(0, -1);
        return $ans;
    }
}
''')

add("3717_minimum_operations_to_make_the_array_beautiful", r'''<?php
// LeetCode 3717 - Minimum Operations to Make the Array Beautiful
// https://leetcode.com/problems/minimum-operations-to-make-the-array-beautiful/

class Solution {
    function minOperations($nums) {
        $f = [];
        $f[$nums[0]] = 0;
        $n = count($nums);
        for ($i = 1; $i < $n; $i++) {
            $x = $nums[$i];
            $g = [];
            foreach ($f as $pre => $s) {
                $cur = (int)ceil($x / $pre) * $pre;
                while ($cur <= 100) {
                    $val = $s + ($cur - $x);
                    if (!isset($g[$cur]) || $g[$cur] > $val) $g[$cur] = $val;
                    $cur += $pre;
                }
            }
            $f = $g;
        }
        $ans = PHP_INT_MAX;
        foreach ($f as $v) $ans = min($ans, $v);
        return $ans;
    }
}
''')

add("3718_smallest_missing_multiple_of_k", r'''<?php
// LeetCode 3718 - Smallest Missing Multiple of K
// https://leetcode.com/problems/smallest-missing-multiple-of-k/

class Solution {
    function missingMultiple($nums, $k) {
        $s = [];
        foreach ($nums as $x) $s[$x] = true;
        for ($i = 1; ; $i++) {
            $x = $k * $i;
            if (!isset($s[$x])) return $x;
        }
    }
}
''')

add("3719_longest_balanced_subarray_i", r'''<?php
// LeetCode 3719 - Longest Balanced Subarray I
// https://leetcode.com/problems/longest-balanced-subarray-i/

class Solution {
    function longestBalanced($nums) {
        $n = count($nums);
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            $vis = [];
            $cnt = [0, 0];
            for ($j = $i; $j < $n; $j++) {
                if (!isset($vis[$nums[$j]])) {
                    $vis[$nums[$j]] = true;
                    $cnt[$nums[$j] & 1]++;
                }
                if ($cnt[0] === $cnt[1]) $ans = max($ans, $j - $i + 1);
            }
        }
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

#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
SOLUTIONS = {}

def add(folder, body):
    SOLUTIONS[folder] = body


add("3341_find_minimum_time_to_reach_last_room_i", r'''<?php
// LeetCode 3341 - Find Minimum Time to Reach Last Room I
// https://leetcode.com/problems/find-minimum-time-to-reach-last-room-i/

class Solution {
    function minTimeToReach($moveTime) {
        $m = count($moveTime);
        $n = count($moveTime[0]);
        $dist = [];
        for ($i = 0; $i < $m; $i++) $dist[$i] = array_fill(0, $n, 1 << 30);
        $h = [[0, 0, 0]];
        $dist[0][0] = 0;
        $dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]];
        $pq = new SplPriorityQueue();
        $pq->setExtractFlags(SplPriorityQueue::EXTR_DATA);
        $pq->insert([0, 0, 0], 0);
        while (!$pq->isEmpty()) {
            $cur = $pq->extract();
            $t = $cur[0];
            $r = $cur[1];
            $c = $cur[2];
            if ($t !== $dist[$r][$c]) continue;
            if ($r === $m - 1 && $c === $n - 1) return $t;
            foreach ($dirs as $d) {
                $nr = $r + $d[0];
                $nc = $c + $d[1];
                if ($nr < 0 || $nc < 0 || $nr >= $m || $nc >= $n) continue;
                $start = max($t, $moveTime[$nr][$nc]);
                $nt = $start + 1;
                if ($nt < $dist[$nr][$nc]) {
                    $dist[$nr][$nc] = $nt;
                    $pq->insert([$nt, $nr, $nc], -$nt);
                }
            }
        }
        return -1;
    }
}
''')

add("3342_find_minimum_time_to_reach_last_room_ii", r'''<?php
// LeetCode 3342 - Find Minimum Time to Reach Last Room II
// https://leetcode.com/problems/find-minimum-time-to-reach-last-room-ii/

class Solution {
    function minTimeToReach($moveTime) {
        $m = count($moveTime);
        $n = count($moveTime[0]);
        $INF = 1 << 30;
        $dist = [];
        for ($i = 0; $i < $m; $i++) {
            $dist[$i] = [];
            for ($j = 0; $j < $n; $j++) $dist[$i][$j] = [$INF, $INF];
        }
        $dist[0][0][0] = 0;
        $dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]];
        $pq = new SplPriorityQueue();
        $pq->setExtractFlags(SplPriorityQueue::EXTR_DATA);
        $pq->insert([0, 0, 0, 0], 0);
        while (!$pq->isEmpty()) {
            $cur = $pq->extract();
            $t = $cur[0];
            $r = $cur[1];
            $c = $cur[2];
            $parity = $cur[3];
            if ($t !== $dist[$r][$c][$parity]) continue;
            if ($r === $m - 1 && $c === $n - 1) return $t;
            $cost = $parity === 1 ? 2 : 1;
            foreach ($dirs as $d) {
                $nr = $r + $d[0];
                $nc = $c + $d[1];
                if ($nr < 0 || $nc < 0 || $nr >= $m || $nc >= $n) continue;
                $start = max($t, $moveTime[$nr][$nc]);
                $nt = $start + $cost;
                $np = 1 - $parity;
                if ($nt < $dist[$nr][$nc][$np]) {
                    $dist[$nr][$nc][$np] = $nt;
                    $pq->insert([$nt, $nr, $nc, $np], -$nt);
                }
            }
        }
        return -1;
    }
}
''')

add("3343_count_number_of_balanced_permutations", r'''<?php
// LeetCode 3343 - Count Number of Balanced Permutations
// https://leetcode.com/problems/count-number-of-balanced-permutations/

class Solution {
    function modPow($a, $e, $mod) {
        $r = 1;
        $a %= $mod;
        while ($e > 0) {
            if ($e & 1) $r = $r * $a % $mod;
            $a = $a * $a % $mod;
            $e >>= 1;
        }
        return $r;
    }

    function key($a, $b) {
        return $a . ',' . $b;
    }

    function countBalancedPermutations($num) {
        $mod = 1000000007;
        $cnt = array_fill(0, 10, 0);
        $sum = 0;
        $n = strlen($num);
        for ($i = 0; $i < $n; $i++) {
            $d = ord($num[$i]) - 48;
            $cnt[$d]++;
            $sum += $d;
        }
        if ($sum % 2 === 1) return 0;
        $halfN = intdiv($n, 2);
        $halfS = intdiv($sum, 2);
        $fact = [1];
        $invF = [];
        for ($i = 1; $i <= $n; $i++) $fact[$i] = $fact[$i - 1] * $i % $mod;
        $invF[$n] = $this->modPow($fact[$n], $mod - 2, $mod);
        for ($i = $n; $i > 0; $i--) $invF[$i - 1] = $invF[$i] * $i % $mod;
        $dp = [];
        $dp[$this->key(0, 0)] = 1;
        for ($d = 0; $d <= 9; $d++) {
            $ndp = [];
            foreach ($dp as $st => $ways) {
                $parts = explode(',', $st);
                $used = intval($parts[0]);
                $s = intval($parts[1]);
                for ($take = 0; $take <= $cnt[$d]; $take++) {
                    $nu = $used + $take;
                    $ns = $s + $take * $d;
                    if ($nu > $halfN || $ns > $halfS) continue;
                    $w = $ways * $invF[$take] % $mod * $invF[$cnt[$d] - $take] % $mod;
                    $nk = $this->key($nu, $ns);
                    $ndp[$nk] = (($ndp[$nk] ?? 0) + $w) % $mod;
                }
            }
            $dp = $ndp;
        }
        $ans = $dp[$this->key($halfN, $halfS)] ?? 0;
        $ans = $ans * $fact[$halfN] % $mod * $fact[$n - $halfN] % $mod;
        for ($d = 0; $d <= 9; $d++) $ans = $ans * $fact[$cnt[$d]] % $mod;
        return $ans;
    }
}
''')

add("3344_maximum_sized_array", r'''<?php
// LeetCode 3344 - Maximum Sized Array
// https://leetcode.com/problems/maximum-sized-array/

class Solution {
    function ok($n, $s) {
        $sum = 0;
        for ($i = 0; $i < $n; $i++) {
            for ($j = 0; $j < $n; $j++) {
                $ij = $i | $j;
                $sum += $ij * ($n - 1) * $n / 2;
                if ($sum > $s) return false;
            }
        }
        return $sum <= $s;
    }

    function maxSizedArray($s) {
        $lo = 1;
        $hi = 2000;
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi + 1, 2);
            if ($this->ok($mid, $s)) $lo = $mid;
            else $hi = $mid - 1;
        }
        return $lo;
    }
}
''')

add("3345_smallest_divisible_digit_product_i", r'''<?php
// LeetCode 3345 - Smallest Divisible Digit Product I
// https://leetcode.com/problems/smallest-divisible-digit-product-i/

class Solution {
    function smallestNumber($n, $t) {
        for ($x = $n; ; $x++) {
            $p = 1;
            $y = $x;
            while ($y > 0) {
                $p *= $y % 10;
                $y = intdiv($y, 10);
            }
            if ($p % $t === 0) return $x;
        }
    }
}
''')

add("3346_maximum_frequency_of_an_element_after_performing_operations_i", r'''<?php
// LeetCode 3346 - Maximum Frequency of an Element After Performing Operations I
// https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-i/

class Solution {
    function lowerBound($a, $x) {
        $lo = 0;
        $hi = count($a);
        while ($lo < $hi) {
            $mid = ($lo + $hi) >> 1;
            if ($a[$mid] < $x) $lo = $mid + 1; else $hi = $mid;
        }
        return $lo;
    }

    function upperBound($a, $x) {
        $lo = 0;
        $hi = count($a);
        while ($lo < $hi) {
            $mid = ($lo + $hi) >> 1;
            if ($a[$mid] <= $x) $lo = $mid + 1; else $hi = $mid;
        }
        return $lo;
    }

    function maxFrequency($nums, $k, $numOperations) {
        sort($nums);
        $n = count($nums);
        $freq = [];
        foreach ($nums as $x) $freq[$x] = ($freq[$x] ?? 0) + 1;
        $ans = 1;
        foreach ($freq as $t => $f) {
            $lo = $this->lowerBound($nums, $t - $k);
            $hi = $this->upperBound($nums, $t + $k);
            $can = $hi - $lo;
            $use = min($can, $f + $numOperations);
            if ($use > $ans) $ans = $use;
        }
        $l = 0;
        for ($r = 0; $r < $n; $r++) {
            while ($nums[$r] - $nums[$l] > 2 * $k) $l++;
            $window = min($r - $l + 1, $numOperations);
            if ($window > $ans) $ans = $window;
        }
        return $ans;
    }
}
''')

add("3347_maximum_frequency_of_an_element_after_performing_operations_ii", r'''<?php
// LeetCode 3347 - Maximum Frequency of an Element After Performing Operations II
// https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-ii/

class Solution {
    function lowerBound($a, $x) {
        $lo = 0;
        $hi = count($a);
        while ($lo < $hi) {
            $mid = ($lo + $hi) >> 1;
            if ($a[$mid] < $x) $lo = $mid + 1; else $hi = $mid;
        }
        return $lo;
    }

    function upperBound($a, $x) {
        $lo = 0;
        $hi = count($a);
        while ($lo < $hi) {
            $mid = ($lo + $hi) >> 1;
            if ($a[$mid] <= $x) $lo = $mid + 1; else $hi = $mid;
        }
        return $lo;
    }

    function maxFrequency($nums, $k, $numOperations) {
        sort($nums);
        $freq = [];
        foreach ($nums as $x) $freq[$x] = ($freq[$x] ?? 0) + 1;
        $ans = 1;
        $candidates = [];
        $seen = [];
        foreach ($nums as $x) {
            foreach ([$x - $k, $x, $x + $k] as $t) {
                if (!isset($seen[$t])) { $seen[$t] = true; $candidates[] = $t; }
            }
        }
        foreach ($candidates as $t) {
            $lo = $this->lowerBound($nums, $t - $k);
            $hi = $this->upperBound($nums, $t + $k);
            $can = $hi - $lo;
            $f = $freq[$t] ?? 0;
            $use = min($can, $f + $numOperations);
            if ($use > $ans) $ans = $use;
        }
        return $ans;
    }
}
''')

add("3348_smallest_divisible_digit_product_ii", r'''<?php
// LeetCode 3348 - Smallest Divisible Digit Product II
// https://leetcode.com/problems/smallest-divisible-digit-product-ii/

class Solution {
    function dfs(&$res, $i, $tight, $sameLen, $num, $t) {
        if ($i === count($res)) {
            $prod = 1;
            foreach ($res as $c) {
                $prod *= (ord($c) - 48);
                if ($prod === 0) break;
            }
            return $prod % $t === 0 && $prod > 0;
        }
        $start = ($i === 0) ? '1' : '0';
        if ($tight && $sameLen && $i < strlen($num)) $start = $num[$i];
        for ($cc = ord($start); $cc <= 57; $cc++) {
            $c = chr($cc);
            $res[$i] = $c;
            $nt = $tight && $sameLen && $i < strlen($num) && $c === $num[$i];
            if ($this->dfs($res, $i + 1, $nt, $sameLen, $num, $t)) return true;
        }
        return false;
    }

    function smallestNumber($num, $t) {
        $tt = $t;
        for ($d = 9; $d >= 2; $d--) {
            while ($tt % $d === 0) $tt = intdiv($tt, $d);
        }
        if ($tt > 1) return '-1';
        for ($extra = 0; $extra <= 60; $extra++) {
            $L = strlen($num) + $extra;
            $res = array_fill(0, $L, '0');
            if ($this->dfs($res, 0, true, $extra === 0, $num, $t)) return implode('', $res);
        }
        return '-1';
    }
}
''')

add("3349_adjacent_increasing_subarrays_detection_i", r'''<?php
// LeetCode 3349 - Adjacent Increasing Subarrays Detection I
// https://leetcode.com/problems/adjacent-increasing-subarrays-detection-i/

class Solution {
    function inc($nums, $start, $k) {
        for ($i = $start; $i + 1 < $start + $k; $i++) {
            if ($nums[$i] >= $nums[$i + 1]) return false;
        }
        return true;
    }

    function hasIncreasingSubarrays($nums, $k) {
        $n = count($nums);
        for ($i = 0; $i + 2 * $k <= $n; $i++) {
            if ($this->inc($nums, $i, $k) && $this->inc($nums, $i + $k, $k)) return true;
        }
        return false;
    }
}
''')

add("3350_adjacent_increasing_subarrays_detection_ii", r'''<?php
// LeetCode 3350 - Adjacent Increasing Subarrays Detection II
// https://leetcode.com/problems/adjacent-increasing-subarrays-detection-ii/

class Solution {
    function ok($up, $n, $k) {
        for ($i = 0; $i + 2 * $k <= $n; $i++) {
            if ($up[$i] >= $k && $up[$i + $k] >= $k) return true;
        }
        return false;
    }

    function maxIncreasingSubarrays($nums) {
        $n = count($nums);
        $up = [];
        $up[$n - 1] = 1;
        for ($i = $n - 2; $i >= 0; $i--) {
            $up[$i] = ($nums[$i] < $nums[$i + 1]) ? $up[$i + 1] + 1 : 1;
        }
        $lo = 1;
        $hi = intdiv($n, 2);
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi + 1, 2);
            if ($this->ok($up, $n, $mid)) $lo = $mid;
            else $hi = $mid - 1;
        }
        return $lo;
    }
}
''')

add("3351_sum_of_good_subsequences", r'''<?php
// LeetCode 3351 - Sum of Good Subsequences
// https://leetcode.com/problems/sum-of-good-subsequences/

class Solution {
    function sumOfGoodSubsequences($nums) {
        $mod = 1000000007;
        $cnt = [];
        $sum = [];
        $ans = 0;
        foreach ($nums as $x) {
            $c = 1;
            $s = $x;
            if (($cnt[$x - 1] ?? 0) > 0) {
                $c = ($c + $cnt[$x - 1]) % $mod;
                $s = ($s + $sum[$x - 1] + $cnt[$x - 1] * $x % $mod) % $mod;
            }
            if (($cnt[$x + 1] ?? 0) > 0) {
                $c = ($c + $cnt[$x + 1]) % $mod;
                $s = ($s + $sum[$x + 1] + $cnt[$x + 1] * $x % $mod) % $mod;
            }
            $cnt[$x] = (($cnt[$x] ?? 0) + $c) % $mod;
            $sum[$x] = (($sum[$x] ?? 0) + $s) % $mod;
            $ans = ($ans + $s) % $mod;
        }
        return $ans;
    }
}
''')

add("3352_count_k_reducible_numbers_less_than_n", r'''<?php
// LeetCode 3352 - Count K-Reducible Numbers Less Than N
// https://leetcode.com/problems/count-k-reducible-numbers-less-than-n/

class Solution {
    public $s;
    public $k;
    public $red;
    public $memo;
    public $mod;

    function bitsPop($x) {
        $c = 0;
        while ($x > 0) { $c += $x & 1; $x >>= 1; }
        return $c;
    }

    function dfs($pos, $tight, $ones) {
        if ($pos === strlen($this->s)) {
            if ($ones === 0) return 0;
            return $this->red[$ones] <= $this->k - 1 ? 1 : 0;
        }
        $ky = $pos . ',' . ($tight ? 1 : 0) . ',' . $ones;
        if (isset($this->memo[$ky])) return $this->memo[$ky];
        $up = $tight ? (ord($this->s[$pos]) - 48) : 1;
        $ans = 0;
        for ($d = 0; $d <= $up; $d++) {
            $nt = $tight && $d === $up;
            $ans = ($ans + $this->dfs($pos + 1, $nt, $ones + $d)) % $this->mod;
        }
        return $this->memo[$ky] = $ans;
    }

    function countKReducibleNumbers($s, $k) {
        $this->mod = 1000000007;
        $this->s = $s;
        $this->k = $k;
        $this->red = [];
        $this->red[1] = 0;
        for ($i = 2; $i <= 800; $i++) $this->red[$i] = 1 + $this->red[$this->bitsPop($i)];
        $this->memo = [];
        return $this->dfs(0, true, 0);
    }
}
''')

add("3353_minimum_total_operations", r'''<?php
// LeetCode 3353 - Minimum Total Operations
// https://leetcode.com/problems/minimum-total-operations/

class Solution {
    function minimumOperations($nums) {
        $ops = 0;
        for ($i = count($nums) - 2; $i >= 0; $i--) {
            if ($nums[$i] !== $nums[$i + 1]) $ops++;
        }
        return $ops;
    }
}
''')

add("3354_make_array_elements_equal_to_zero", r'''<?php
// LeetCode 3354 - Make Array Elements Equal to Zero
// https://leetcode.com/problems/make-array-elements-equal-to-zero/

class Solution {
    function countValidSelections($nums) {
        $n = count($nums);
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            if ($nums[$i] !== 0) continue;
            foreach ([-1, 1] as $dir) {
                $a = $nums;
                $cur = $i;
                $d = $dir;
                while ($cur >= 0 && $cur < $n) {
                    if ($a[$cur] === 0) $cur += $d;
                    else {
                        $a[$cur]--;
                        $d = -$d;
                        $cur += $d;
                    }
                }
                $ok = true;
                foreach ($a as $v) if ($v !== 0) { $ok = false; break; }
                if ($ok) $ans++;
            }
        }
        return $ans;
    }
}
''')

add("3355_zero_array_transformation_i", r'''<?php
// LeetCode 3355 - Zero Array Transformation I
// https://leetcode.com/problems/zero-array-transformation-i/

class Solution {
    function isZeroArray($nums, $queries) {
        $n = count($nums);
        $diff = array_fill(0, $n + 1, 0);
        foreach ($queries as $q) {
            $diff[$q[0]]++;
            $diff[$q[1] + 1]--;
        }
        $cur = 0;
        for ($i = 0; $i < $n; $i++) {
            $cur += $diff[$i];
            if ($cur < $nums[$i]) return false;
        }
        return true;
    }
}
''')

add("3356_zero_array_transformation_ii", r'''<?php
// LeetCode 3356 - Zero Array Transformation II
// https://leetcode.com/problems/zero-array-transformation-ii/

class Solution {
    function ok($k, $nums, $queries, $n) {
        $diff = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $k; $i++) {
            $q = $queries[$i];
            $diff[$q[0]] += $q[2];
            $diff[$q[1] + 1] -= $q[2];
        }
        $cur = 0;
        for ($i = 0; $i < $n; $i++) {
            $cur += $diff[$i];
            if ($cur < $nums[$i]) return false;
        }
        return true;
    }

    function minZeroArray($nums, $queries) {
        $n = count($nums);
        if ($this->ok(0, $nums, $queries, $n)) return 0;
        $lo = 1;
        $hi = count($queries) + 1;
        while ($lo < $hi) {
            $mid = ($lo + $hi) >> 1;
            if ($mid <= count($queries) && $this->ok($mid, $nums, $queries, $n)) $hi = $mid;
            else $lo = $mid + 1;
        }
        if ($lo > count($queries)) return -1;
        return $lo;
    }
}
''')

add("3357_minimize_the_maximum_adjacent_element_difference", r'''<?php
// LeetCode 3357 - Minimize the Maximum Adjacent Element Difference
// https://leetcode.com/problems/minimize-the-maximum-adjacent-element-difference/

class Solution {
    function ok($d, $nums, $n) {
        $prev = -1;
        for ($i = 0; $i < $n; $i++) {
            if ($nums[$i] !== -1) {
                if ($prev !== -1 && abs($nums[$i] - $prev) > $d) return false;
                $prev = $nums[$i];
                continue;
            }
            $j = $i;
            while ($j < $n && $nums[$j] === -1) $j++;
            $left = $prev;
            $right = ($j < $n) ? $nums[$j] : -1;
            $gap = $j - $i;
            if ($left === -1 && $right === -1) return true;
            if ($left === -1 || $right === -1) {
                $prev = -1;
                $i = $j - 1;
                continue;
            }
            if (abs($left - $right) > $d * ($gap + 1)) return false;
            $prev = -1;
            $i = $j - 1;
        }
        return true;
    }

    function minDifference($nums) {
        $n = count($nums);
        $lo = 0;
        $hi = 1000000000;
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi, 2);
            if ($this->ok($mid, $nums, $n)) $hi = $mid;
            else $lo = $mid + 1;
        }
        return $lo;
    }
}
''')

add("3359_find_sorted_submatrices_with_maximum_element_at_most_k", r'''<?php
// LeetCode 3359 - Find Sorted Submatrices With Maximum Element at Most K
// https://leetcode.com/problems/find-sorted-submatrices-with-maximum-element-at-most-k/

class Solution {
    function countSortedMatrices($grid, $k) {
        $m = count($grid);
        $n = count($grid[0]);
        $ans = 0;
        for ($r1 = 0; $r1 < $m; $r1++) {
            for ($r2 = $r1; $r2 < $m; $r2++) {
                for ($c1 = 0; $c1 < $n; $c1++) {
                    for ($c2 = $c1; $c2 < $n; $c2++) {
                        $ok = true;
                        for ($i = $r1; $i <= $r2 && $ok; $i++) {
                            for ($j = $c1; $j <= $c2; $j++) {
                                if ($grid[$i][$j] > $k) { $ok = false; break; }
                                if ($j > $c1 && $grid[$i][$j] < $grid[$i][$j - 1]) { $ok = false; break; }
                                if ($i > $r1 && $grid[$i][$j] < $grid[$i - 1][$j]) { $ok = false; break; }
                            }
                        }
                        if ($ok) $ans++;
                    }
                }
            }
        }
        return $ans;
    }
}
''')

add("3360_stone_removal_game", r'''<?php
// LeetCode 3360 - Stone Removal Game
// https://leetcode.com/problems/stone-removal-game/

class Solution {
    function canAliceWin($n) {
        $take = 10;
        $alice = true;
        while ($n >= $take && $take > 0) {
            $n -= $take;
            $take--;
            $alice = !$alice;
        }
        return !$alice;
    }
}
''')

add("3361_shift_distance_between_two_strings", r'''<?php
// LeetCode 3361 - Shift Distance Between Two Strings
// https://leetcode.com/problems/shift-distance-between-two-strings/

class Solution {
    function shiftDistance($s, $t, $nextCost, $previousCost) {
        $ans = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $a = ord($s[$i]) - 97;
            $b = ord($t[$i]) - 97;
            if ($a === $b) continue;
            $fwd = 0;
            for ($x = $a; $x !== $b; $x = ($x + 1) % 26) $fwd += $nextCost[$x];
            $bwd = 0;
            for ($x = $a; $x !== $b; $x = ($x + 25) % 26) $bwd += $previousCost[$x];
            $ans += $fwd < $bwd ? $fwd : $bwd;
        }
        return $ans;
    }
}
''')

add("3362_zero_array_transformation_iii", r'''<?php
// LeetCode 3362 - Zero Array Transformation III
// https://leetcode.com/problems/zero-array-transformation-iii/

class Solution {
    function maxRemoval($nums, $queries) {
        usort($queries, function($a, $b) { return $a[0] <=> $b[0]; });
        $n = count($nums);
        $diff = array_fill(0, $n + 1, 0);
        $j = 0;
        $used = 0;
        $cur = 0;
        $pq = new SplPriorityQueue();
        $pq->setExtractFlags(SplPriorityQueue::EXTR_DATA);
        for ($i = 0; $i < $n; $i++) {
            $cur += $diff[$i];
            while ($j < count($queries) && $queries[$j][0] === $i) {
                $pq->insert($queries[$j][1], $queries[$j][1]);
                $j++;
            }
            while ($cur < $nums[$i]) {
                if ($pq->isEmpty()) return -1;
                $r = $pq->extract();
                if ($r < $i) return -1;
                $cur++;
                $diff[$r + 1]--;
                $used++;
            }
        }
        return count($queries) - $used;
    }
}
''')

add("3363_find_the_maximum_number_of_fruits_collected", r'''<?php
// LeetCode 3363 - Find the Maximum Number of Fruits Collected
// https://leetcode.com/problems/find-the-maximum-number-of-fruits-collected/

class Solution {
    function maxCollectedFruits($fruits) {
        $n = count($fruits);
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            $ans += $fruits[$i][$i];
            $fruits[$i][$i] = 0;
        }
        $neg = -(1 << 30);
        $dp2 = [];
        $dp3 = [];
        for ($i = 0; $i < $n; $i++) {
            $dp2[$i] = array_fill(0, $n, $neg);
            $dp3[$i] = array_fill(0, $n, $neg);
        }
        $dp2[0][$n - 1] = $fruits[0][$n - 1];
        for ($i = 0; $i < $n; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if ($dp2[$i][$j] === $neg) continue;
                foreach ([-1, 0, 1] as $dj) {
                    $ni = $i + 1;
                    $nj = $j + $dj;
                    if ($ni < $n && $nj >= 0 && $nj < $n && $nj > $ni) {
                        $v = $dp2[$i][$j] + $fruits[$ni][$nj];
                        if ($v > $dp2[$ni][$nj]) $dp2[$ni][$nj] = $v;
                    }
                }
            }
        }
        $dp3[$n - 1][0] = $fruits[$n - 1][0];
        for ($j = 0; $j < $n; $j++) {
            for ($i = 0; $i < $n; $i++) {
                if ($dp3[$i][$j] === $neg) continue;
                foreach ([-1, 0, 1] as $di) {
                    $ni = $i + $di;
                    $nj = $j + 1;
                    if ($ni >= 0 && $ni < $n && $nj < $n && $ni > $nj) {
                        $v = $dp3[$i][$j] + $fruits[$ni][$nj];
                        if ($v > $dp3[$ni][$nj]) $dp3[$ni][$nj] = $v;
                    }
                }
            }
        }
        $ans += $dp2[$n - 1][$n - 1] + $dp3[$n - 1][$n - 1];
        return $ans;
    }
}
''')

add("3364_minimum_positive_sum_subarray", r'''<?php
// LeetCode 3364 - Minimum Positive Sum Subarray
// https://leetcode.com/problems/minimum-positive-sum-subarray/

class Solution {
    function minimumSumSubarray($nums, $l, $r) {
        $n = count($nums);
        $pref = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; $i++) $pref[$i + 1] = $pref[$i] + $nums[$i];
        $ans = 2147483647;
        $found = false;
        for ($i = 0; $i < $n; $i++) {
            for ($length = $l; $length <= $r && $i + $length <= $n; $length++) {
                $s = $pref[$i + $length] - $pref[$i];
                if ($s > 0 && $s < $ans) {
                    $ans = $s;
                    $found = true;
                }
            }
        }
        return $found ? $ans : -1;
    }
}
''')

add("3365_rearrange_k_substrings_to_form_target_string", r'''<?php
// LeetCode 3365 - Rearrange K Substrings to Form Target String
// https://leetcode.com/problems/rearrange-k-substrings-to-form-target-string/

class Solution {
    function isPossibleToRearrange($s, $t, $k) {
        $n = strlen($s);
        $sz = intdiv($n, $k);
        $cnt = [];
        for ($i = 0; $i < $n; $i += $sz) {
            $a = substr($s, $i, $sz);
            $b = substr($t, $i, $sz);
            $cnt[$a] = ($cnt[$a] ?? 0) + 1;
            $cnt[$b] = ($cnt[$b] ?? 0) - 1;
        }
        foreach ($cnt as $v) if ($v !== 0) return false;
        return true;
    }
}
''')

add("3366_minimum_array_sum", r'''<?php
// LeetCode 3366 - Minimum Array Sum
// https://leetcode.com/problems/minimum-array-sum/

class Solution {
    function tryCand(&$ndp, $base, $na, $nb, $v) {
        if ($base + $v < $ndp[$na][$nb]) $ndp[$na][$nb] = $base + $v;
    }

    function minArraySum($nums, $k, $op1, $op2) {
        $inf = 1e18;
        $dp = [];
        for ($a = 0; $a <= $op1; $a++) $dp[$a] = array_fill(0, $op2 + 1, $inf);
        $dp[0][0] = 0;
        foreach ($nums as $x) {
            $ndp = [];
            for ($a = 0; $a <= $op1; $a++) $ndp[$a] = array_fill(0, $op2 + 1, $inf);
            for ($a = 0; $a <= $op1; $a++) {
                for ($b = 0; $b <= $op2; $b++) {
                    if ($dp[$a][$b] === $inf) continue;
                    $this->tryCand($ndp, $dp[$a][$b], $a, $b, $x);
                    if ($a < $op1) $this->tryCand($ndp, $dp[$a][$b], $a + 1, $b, intdiv($x + 1, 2));
                    if ($b < $op2 && $x >= $k) $this->tryCand($ndp, $dp[$a][$b], $a, $b + 1, $x - $k);
                    if ($a < $op1 && $b < $op2) {
                        $v1 = intdiv($x + 1, 2);
                        if ($v1 >= $k) $this->tryCand($ndp, $dp[$a][$b], $a + 1, $b + 1, $v1 - $k);
                        if ($x >= $k) $this->tryCand($ndp, $dp[$a][$b], $a + 1, $b + 1, intdiv($x - $k + 1, 2));
                    }
                }
            }
            $dp = $ndp;
        }
        $ans = $inf;
        for ($a = 0; $a <= $op1; $a++)
            for ($b = 0; $b <= $op2; $b++)
                if ($dp[$a][$b] < $ans) $ans = $dp[$a][$b];
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

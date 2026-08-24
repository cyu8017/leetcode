#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
SOLUTIONS = {}

def add(folder, body):
    SOLUTIONS[folder] = body


add("3505_minimum_operations_to_make_elements_within_k_subarrays_equal", r'''<?php
// LeetCode 3505 - Minimum Operations to Make Elements Within K Subarrays Equal
// https://leetcode.com/problems/minimum-operations-to-make-elements-within-k-subarrays-equal/

class Solution {
    function minOperations($nums, $x, $k) {
        $n = count($nums);
        $minOps = array_fill(0, $n - $x + 1, 0);
        for ($i = 0; $i + $x <= $n; $i++) {
            $w = array_slice($nums, $i, $x);
            sort($w);
            $med = $w[intdiv($x - 1, 2)];
            $ops = 0;
            foreach ($w as $v) $ops += abs($v - $med);
            $minOps[$i] = $ops;
        }
        $Inf = PHP_INT_MAX >> 2;
        $dp = [];
        for ($i = 0; $i <= $n; $i++) $dp[$i] = array_fill(0, $k + 1, $Inf);
        $dp[$n][0] = 0;
        for ($i = $n - 1; $i >= 0; $i--) {
            for ($j = 0; $j <= $k; $j++) {
                $dp[$i][$j] = $dp[$i + 1][$j];
                if ($j > 0 && $i + $x <= $n && $minOps[$i] + $dp[$i + $x][$j - 1] < $dp[$i][$j])
                    $dp[$i][$j] = $minOps[$i] + $dp[$i + $x][$j - 1];
            }
        }
        return $dp[0][$k];
    }
}
''')

add("3506_find_time_required_to_eliminate_bacterial_strains", r'''<?php
// LeetCode 3506 - Find Time Required to Eliminate Bacterial Strains
// https://leetcode.com/problems/find-time-required-to-eliminate-bacterial-strains/

class Solution {
    function minEliminationTime($timeReq, $splitTime) {
        $pq = $timeReq;
        sort($pq);
        $pq = array_values($pq);
        while (count($pq) > 1) {
            array_shift($pq);
            $x = array_shift($pq);
            $v = $x + $splitTime;
            $lo = 0;
            $hi = count($pq);
            while ($lo < $hi) {
                $mid = ($lo + $hi) >> 1;
                if ($pq[$mid] < $v) $lo = $mid + 1;
                else $hi = $mid;
            }
            array_splice($pq, $lo, 0, [$v]);
        }
        return $pq[0];
    }
}
''')

add("3507_minimum_pair_removal_to_sort_array_i", r'''<?php
// LeetCode 3507 - Minimum Pair Removal to Sort Array I
// https://leetcode.com/problems/minimum-pair-removal-to-sort-array-i/

class Solution {
    private function isNonDecreasing($a) {
        $n = count($a);
        for ($i = 1; $i < $n; $i++) if ($a[$i] < $a[$i - 1]) return false;
        return true;
    }

    function minimumPairRemoval($nums) {
        $arr = $nums;
        $ans = 0;
        while (!$this->isNonDecreasing($arr)) {
            $k = 0;
            $s = $arr[0] + $arr[1];
            $n = count($arr);
            for ($i = 1; $i + 1 < $n; $i++) {
                $t = $arr[$i] + $arr[$i + 1];
                if ($s > $t) { $s = $t; $k = $i; }
            }
            $arr[$k] = $s;
            array_splice($arr, $k + 1, 1);
            $ans++;
        }
        return $ans;
    }
}
''')

add("3508_implement_router", r'''<?php
// LeetCode 3508 - Implement Router
// https://leetcode.com/problems/implement-router/

class Router {
    private $lim;
    private $vis;
    private $q;
    private $idx;
    private $d;

    function __construct($memoryLimit) {
        $this->lim = $memoryLimit;
        $this->vis = [];
        $this->q = [];
        $this->idx = [];
        $this->d = [];
    }

    private function f($a, $b, $c) {
        return $a . ',' . $b . ',' . $c;
    }

    function addPacket($source, $destination, $timestamp) {
        $x = $this->f($source, $destination, $timestamp);
        if (isset($this->vis[$x])) return false;
        $this->vis[$x] = true;
        if (count($this->q) >= $this->lim) $this->forwardPacket();
        $this->q[] = [$source, $destination, $timestamp];
        if (!isset($this->d[$destination])) $this->d[$destination] = [];
        $this->d[$destination][] = $timestamp;
        return true;
    }

    function forwardPacket() {
        if (count($this->q) === 0) return [];
        $packet = array_shift($this->q);
        $s = $packet[0];
        $dest = $packet[1];
        $t = $packet[2];
        unset($this->vis[$this->f($s, $dest, $t)]);
        $this->idx[$dest] = ($this->idx[$dest] ?? 0) + 1;
        return [$s, $dest, $t];
    }

    function getCount($destination, $startTime, $endTime) {
        if (!isset($this->d[$destination])) return 0;
        $ls = $this->d[$destination];
        $k = $this->idx[$destination] ?? 0;
        return $this->lowerBound($ls, $k, $endTime + 1) - $this->lowerBound($ls, $k, $startTime);
    }

    private function lowerBound($a, $from, $target) {
        $lo = $from;
        $hi = count($a);
        while ($lo < $hi) {
            $mid = ($lo + $hi) >> 1;
            if ($a[$mid] < $target) $lo = $mid + 1;
            else $hi = $mid;
        }
        return $lo;
    }
}
''')

add("3509_maximum_product_of_subsequences_with_an_alternating_sum_equal_to_k", r'''<?php
// LeetCode 3509 - Maximum Product of Subsequences With an Alternating Sum Equal to K
// https://leetcode.com/problems/maximum-product-of-subsequences-with-an-alternating-sum-equal-to-k/

class Solution {
    private $nums;
    private $limit;
    private $memo;
    private $MIN;

    function maxProduct($nums, $k, $limit) {
        $this->nums = $nums;
        $this->limit = $limit;
        $this->MIN = -5000;
        $this->memo = [];
        $sumAll = 0;
        foreach ($nums as $v) $sumAll += $v;
        if (abs($k) > $sumAll) return -1;
        $ans = $this->dp(0, 1, 0, $k);
        return $ans === $this->MIN ? -1 : $ans;
    }

    private function dp($i, $product, $state, $kk) {
        $n = count($this->nums);
        if ($i === $n) {
            if ($kk === 0 && $state !== 0 && $product <= $this->limit) return $product;
            return $this->MIN;
        }
        $key = $i . ',' . $product . ',' . $state . ',' . $kk;
        if (isset($this->memo[$key])) return $this->memo[$key];
        $res = $this->dp($i + 1, $product, $state, $kk);
        if ($state === 0) $res = max($res, $this->dp($i + 1, $this->nums[$i], 1, $kk - $this->nums[$i]));
        if ($state === 1) {
            $np = $product * $this->nums[$i];
            if ($np > $this->limit + 1) $np = $this->limit + 1;
            $res = max($res, $this->dp($i + 1, $np, 2, $kk + $this->nums[$i]));
        }
        if ($state === 2) {
            $np = $product * $this->nums[$i];
            if ($np > $this->limit + 1) $np = $this->limit + 1;
            $res = max($res, $this->dp($i + 1, $np, 1, $kk - $this->nums[$i]));
        }
        return $this->memo[$key] = $res;
    }
}
''')

add("3510_minimum_pair_removal_to_sort_array_ii", r'''<?php
// LeetCode 3510 - Minimum Pair Removal to Sort Array II
// https://leetcode.com/problems/minimum-pair-removal-to-sort-array-ii/

class Solution {
    private $sl;
    private $slMap;

    private function key($sum, $i) {
        return $sum * 1000000007 + $i;
    }

    private function addSl($sum, $i) {
        $k = $this->key($sum, $i);
        $this->slMap[$k] = [$sum, $i];
        $lo = 0;
        $hi = count($this->sl);
        while ($lo < $hi) {
            $mid = ($lo + $hi) >> 1;
            if ($this->sl[$mid][0] < $sum || ($this->sl[$mid][0] === $sum && $this->sl[$mid][1] < $i)) $lo = $mid + 1;
            else $hi = $mid;
        }
        array_splice($this->sl, $lo, 0, [[$sum, $i]]);
    }

    private function remSl($sum, $i) {
        $k = $this->key($sum, $i);
        if (!isset($this->slMap[$k])) return;
        unset($this->slMap[$k]);
        $n = count($this->sl);
        for ($t = 0; $t < $n; $t++) {
            if ($this->sl[$t][0] === $sum && $this->sl[$t][1] === $i) {
                array_splice($this->sl, $t, 1);
                break;
            }
        }
    }

    private function ceiling($idx, $x) {
        $best = null;
        foreach ($idx as $v => $_) {
            if ($v >= $x && ($best === null || $v < $best)) $best = $v;
        }
        return $best;
    }

    private function floorIdx($idx, $x) {
        $best = null;
        foreach ($idx as $v => $_) {
            if ($v <= $x && ($best === null || $v > $best)) $best = $v;
        }
        return $best;
    }

    function minimumPairRemoval($nums) {
        $n = count($nums);
        $inv = 0;
        $ans = 0;
        $this->sl = [];
        $this->slMap = [];
        $idx = [];
        for ($i = 0; $i < $n; $i++) $idx[$i] = true;
        for ($i = 0; $i < $n - 1; $i++) {
            if ($nums[$i] > $nums[$i + 1]) $inv++;
            $this->addSl($nums[$i] + $nums[$i + 1], $i);
        }
        while ($inv > 0) {
            $ans++;
            $p = array_shift($this->sl);
            unset($this->slMap[$this->key($p[0], $p[1])]);
            $s = $p[0];
            $i = $p[1];
            $j = $this->ceiling($idx, $i + 1);
            if ($nums[$i] > $nums[$j]) $inv--;
            $h = $this->floorIdx($idx, $i - 1);
            if ($h !== null) {
                if ($nums[$h] > $nums[$i]) $inv--;
                $this->remSl($nums[$h] + $nums[$i], $h);
                if ($nums[$h] > $s) $inv++;
                $this->addSl($nums[$h] + $s, $h);
            }
            $kk = $this->ceiling($idx, $j + 1);
            if ($kk !== null) {
                if ($nums[$j] > $nums[$kk]) $inv--;
                $this->remSl($nums[$j] + $nums[$kk], $j);
                if ($s > $nums[$kk]) $inv++;
                $this->addSl($s + $nums[$kk], $i);
            }
            $nums[$i] = $s;
            unset($idx[$j]);
        }
        return $ans;
    }
}
''')

add("3511_make_a_positive_array", r'''<?php
// LeetCode 3511 - Make a Positive Array
// https://leetcode.com/problems/make-a-positive-array/

class Solution {
    function makeArrayPositive($nums) {
        $ans = 0;
        $l = -1;
        $preMx = 0;
        $s = 0;
        $n = count($nums);
        for ($r = 0; $r < $n; $r++) {
            $s += $nums[$r];
            if ($r - $l > 2 && $s <= $preMx) {
                $ans++;
                $l = $r;
                $preMx = 0;
                $s = 0;
            } else if ($r - $l >= 2) {
                $preMx = max($preMx, $s - $nums[$r] - $nums[$r - 1]);
            }
        }
        return $ans;
    }
}
''')

add("3512_minimum_operations_to_make_array_sum_divisible_by_k", r'''<?php
// LeetCode 3512 - Minimum Operations to Make Array Sum Divisible by K
// https://leetcode.com/problems/minimum-operations-to-make-array-sum-divisible-by-k/

class Solution {
    function minOperations($nums, $k) {
        $ans = 0;
        foreach ($nums as $x) $ans = ($ans + $x) % $k;
        return $ans;
    }
}
''')

add("3513_number_of_unique_xor_triplets_i", r'''<?php
// LeetCode 3513 - Number of Unique XOR Triplets I
// https://leetcode.com/problems/number-of-unique-xor-triplets-i/

class Solution {
    function uniqueXorTriplets($nums) {
        $n = count($nums);
        if ($n <= 2) return $n;
        $x = $n;
        $len = 0;
        while ($x !== 0) { $len++; $x >>= 1; }
        return 1 << $len;
    }
}
''')

add("3514_number_of_unique_xor_triplets_ii", r'''<?php
// LeetCode 3514 - Number of Unique XOR Triplets II
// https://leetcode.com/problems/number-of-unique-xor-triplets-ii/

class Solution {
    function uniqueXorTriplets($nums) {
        $mx = 0;
        foreach ($nums as $v) $mx = max($mx, $v);
        $mx <<= 1;
        $st = array_fill(0, $mx, false);
        foreach ($nums as $a)
            foreach ($nums as $b) $st[$a ^ $b] = true;
        $s = array_fill(0, $mx, 0);
        for ($ab = 0; $ab < $mx; $ab++) {
            if ($st[$ab]) foreach ($nums as $c) $s[$ab ^ $c] = 1;
        }
        $ans = 0;
        foreach ($s as $v) $ans += $v;
        return $ans;
    }
}
''')

add("3515_shortest_path_in_a_weighted_tree", r'''<?php
// LeetCode 3515 - Shortest Path in a Weighted Tree
// https://leetcode.com/problems/shortest-path-in-a-weighted-tree/

class Solution {
    private $g;
    private $inT;
    private $outT;
    private $dist;
    private $parent;
    private $time;
    private $bit;
    private $n;

    private function dfs($u, $p) {
        $this->inT[$u] = $this->time++;
        foreach ($this->g[$u] as $e) {
            $to = $e[0];
            $w = $e[1];
            if ($to === $p) continue;
            $this->parent[$to] = $u;
            $this->dist[$to] = $this->dist[$u] + $w;
            $this->dfs($to, $u);
        }
        $this->outT[$u] = $this->time - 1;
    }

    private function add($i, $v) {
        for (; $i <= $this->n; $i += $i & -$i) $this->bit[$i] += $v;
    }

    private function rangeAdd($l, $r, $v) {
        $this->add($l + 1, $v);
        $this->add($r + 2, -$v);
    }

    private function point($i) {
        $s = 0;
        for ($i++; $i > 0; $i -= $i & -$i) $s += $this->bit[$i];
        return $s;
    }

    function treeQueries($n, $edges, $queries) {
        $this->n = $n;
        $this->g = array_fill(0, $n + 1, []);
        $weight = [];
        foreach ($edges as $e) {
            $u = $e[0];
            $v = $e[1];
            $w = $e[2];
            $this->g[$u][] = [$v, $w];
            $this->g[$v][] = [$u, $w];
            $a = min($u, $v);
            $b = max($u, $v);
            $weight[$a . ',' . $b] = $w;
        }
        $this->inT = array_fill(0, $n + 1, 0);
        $this->outT = array_fill(0, $n + 1, 0);
        $this->dist = array_fill(0, $n + 1, 0);
        $this->parent = array_fill(0, $n + 1, 0);
        $this->time = 0;
        $this->dfs(1, 0);
        $this->bit = array_fill(0, $n + 2, 0);
        for ($i = 1; $i <= $n; $i++) $this->rangeAdd($this->inT[$i], $this->inT[$i], $this->dist[$i]);
        $ans = [];
        foreach ($queries as $q) {
            if ($q[0] === 1) {
                $u = $q[1];
                $v = $q[2];
                $nw = $q[3];
                $a = min($u, $v);
                $b = max($u, $v);
                $key = $a . ',' . $b;
                $ow = $weight[$key];
                $delta = $nw - $ow;
                $weight[$key] = $nw;
                $child = $this->parent[$u] === $v ? $u : $v;
                $this->rangeAdd($this->inT[$child], $this->outT[$child], $delta);
            } else {
                $ans[] = $this->point($this->inT[$q[1]]);
            }
        }
        return $ans;
    }
}
''')

add("3516_find_closest_person", r'''<?php
// LeetCode 3516 - Find Closest Person
// https://leetcode.com/problems/find-closest-person/

class Solution {
    function findClosest($x, $y, $z) {
        $a = abs($x - $z);
        $b = abs($y - $z);
        if ($a === $b) return 0;
        return $a < $b ? 1 : 2;
    }
}
''')

add("3517_smallest_palindromic_rearrangement_i", r'''<?php
// LeetCode 3517 - Smallest Palindromic Rearrangement I
// https://leetcode.com/problems/smallest-palindromic-rearrangement-i/

class Solution {
    function smallestPalindrome($s) {
        $cnt = array_fill(0, 26, 0);
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) $cnt[ord($s[$i]) - 97]++;
        $t = '';
        $ch = '';
        for ($i = 0; $i < 26; $i++) {
            $c = chr(97 + $i);
            $v = intdiv($cnt[$i], 2);
            $t .= str_repeat($c, $v);
            $cnt[$i] -= $v * 2;
            if ($cnt[$i] === 1) $ch = $c;
        }
        $sb = $t;
        if ($ch !== '') $sb .= $ch;
        for ($i = strlen($t) - 1; $i >= 0; $i--) $sb .= $t[$i];
        return $sb;
    }
}
''')

add("3518_smallest_palindromic_rearrangement_ii", r'''<?php
// LeetCode 3518 - Smallest Palindromic Rearrangement II
// https://leetcode.com/problems/smallest-palindromic-rearrangement-ii/

class Solution {
    private $MAX = 1000001;

    private function nCk($n, $kk) {
        if ($kk < 0 || $kk > $n) return 0;
        $res = 1;
        if ($kk > $n - $kk) $kk = $n - $kk;
        for ($i = 1; $i <= $kk; $i++) {
            $res = intdiv($res * ($n - $i + 1), $i);
            if ($res >= $this->MAX) return $this->MAX;
        }
        return $res;
    }

    private function countArr($h) {
        $total = 0;
        foreach ($h as $f) $total += $f;
        $res = 1;
        foreach ($h as $f) {
            $res *= $this->nCk($total, $f);
            if ($res >= $this->MAX) return $this->MAX;
            $total -= $f;
        }
        return $res;
    }

    function smallestPalindrome($s, $k) {
        $cnt = array_fill(0, 26, 0);
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) $cnt[ord($s[$i]) - 97]++;
        $odd = 0;
        foreach ($cnt as $c) if ($c % 2 !== 0) $odd++;
        if ($odd > 1) return '';
        $half = array_fill(0, 26, 0);
        $mid = '';
        for ($i = 0; $i < 26; $i++) {
            $half[$i] = intdiv($cnt[$i], 2);
            if ($cnt[$i] % 2 !== 0) $mid = chr(97 + $i);
        }
        if ($this->countArr($half) < $k) return '';
        $halfLen = 0;
        foreach ($half as $f) $halfLen += $f;
        $left = '';
        for ($t = 0; $t < $halfLen; $t++) {
            for ($i = 0; $i < 26; $i++) {
                if ($half[$i] === 0) continue;
                $half[$i]--;
                $arr = $this->countArr($half);
                if ($arr >= $k) {
                    $left .= chr(97 + $i);
                    break;
                }
                $k -= $arr;
                $half[$i]++;
            }
        }
        $res = $left;
        if ($mid !== '') $res .= $mid;
        for ($i = strlen($left) - 1; $i >= 0; $i--) $res .= $left[$i];
        return $res;
    }
}
''')

add("3519_count_numbers_with_non_decreasing_digits", r'''<?php
// LeetCode 3519 - Count Numbers with Non-Decreasing Digits
// https://leetcode.com/problems/count-numbers-with-non-decreasing-digits/

class Solution {
    private $MOD = 1000000007;

    private function toDigits($s, $b) {
        if ($s === '0') return [0];
        $digs = [];
        while (!(strlen($s) === 1 && $s[0] === '0')) {
            $rem = 0;
            $q = '';
            $n = strlen($s);
            for ($i = 0; $i < $n; $i++) {
                $cur = $rem * 10 + (ord($s[$i]) - 48);
                $d = intdiv($cur, $b);
                $rem = $cur % $b;
                if (strlen($q) > 0 || $d !== 0) $q .= (string)$d;
            }
            $digs[] = $rem;
            $s = strlen($q) === 0 ? '0' : $q;
        }
        return array_reverse($digs);
    }

    private function dec($s) {
        $a = str_split($s);
        $i = count($a) - 1;
        while ($i >= 0 && $a[$i] === '0') { $a[$i] = '9'; $i--; }
        if ($i < 0) return '0';
        $a[$i] = chr(ord($a[$i]) - 1);
        $t = implode('', $a);
        $p = 0;
        while ($p + 1 < strlen($t) && $t[$p] === '0') $p++;
        return substr($t, $p);
    }

    private function countUpto($digs, $b) {
        $m = count($digs);
        $memo = [];
        $dfs = function($pos, $last, $tight) use (&$dfs, &$memo, $m, $digs, $b) {
            if ($pos === $m) return 1;
            $key = $pos . ',' . $last . ',' . ($tight ? 1 : 0);
            if (isset($memo[$key])) return $memo[$key];
            $up = $tight ? $digs[$pos] : $b - 1;
            $res = 0;
            for ($d = $last; $d <= $up; $d++)
                $res = ($res + $dfs($pos + 1, $d, $tight && $d === $up)) % 1000000007;
            return $memo[$key] = $res;
        };
        return $dfs(0, 0, true);
    }

    function countNumbers($l, $r, $b) {
        $rd = $this->toDigits($r, $b);
        $ld = $this->toDigits($this->dec($l), $b);
        return ($this->countUpto($rd, $b) - $this->countUpto($ld, $b) + $this->MOD) % $this->MOD;
    }
}
''')

add("3520_minimum_threshold_for_inversion_pairs_count", r'''<?php
// LeetCode 3520 - Minimum Threshold for Inversion Pairs Count
// https://leetcode.com/problems/minimum-threshold-for-inversion-pairs-count/

class Solution {
    private function upperBound($a, $target) {
        $lo = 0;
        $hi = count($a);
        while ($lo < $hi) {
            $mid = ($lo + $hi) >> 1;
            if ($a[$mid] <= $target) $lo = $mid + 1;
            else $hi = $mid;
        }
        return $lo;
    }

    private function countInv($nums, $k, $threshold) {
        $sorted = [];
        $inv = 0;
        foreach ($nums as $num) {
            $left = $this->upperBound($sorted, $num);
            $right = $this->upperBound($sorted, $num + $threshold);
            $inv += $right - $left;
            array_splice($sorted, $this->upperBound($sorted, $num), 0, [$num]);
        }
        return $inv >= $k;
    }

    function minThreshold($nums, $k) {
        $mx = 0;
        foreach ($nums as $v) if ($v > $mx) $mx = $v;
        $l = 0;
        $r = $mx + 1;
        while ($l < $r) {
            $m = ($l + $r) >> 1;
            if ($this->countInv($nums, $k, $m)) $r = $m;
            else $l = $m + 1;
        }
        return $l > $mx ? -1 : $l;
    }
}
''')

add("3522_calculate_score_after_performing_instructions", r'''<?php
// LeetCode 3522 - Calculate Score After Performing Instructions
// https://leetcode.com/problems/calculate-score-after-performing-instructions/

class Solution {
    function calculateScore($instructions, $values) {
        $n = count($values);
        $vis = array_fill(0, $n, false);
        $ans = 0;
        $i = 0;
        while ($i >= 0 && $i < $n && !$vis[$i]) {
            $vis[$i] = true;
            if ($instructions[$i][0] === 'a') {
                $ans += $values[$i];
                $i += 1;
            } else {
                $i += $values[$i];
            }
        }
        return $ans;
    }
}
''')

add("3523_make_array_non_decreasing", r'''<?php
// LeetCode 3523 - Make Array Non-decreasing
// https://leetcode.com/problems/make-array-non-decreasing/

class Solution {
    function maximumPossibleSize($nums) {
        $ans = 0;
        $mx = 0;
        foreach ($nums as $x) {
            if ($mx <= $x) {
                $ans++;
                $mx = $x;
            }
        }
        return $ans;
    }
}
''')

add("3524_find_x_value_of_array_i", r'''<?php
// LeetCode 3524 - Find X Value of Array I
// https://leetcode.com/problems/find-x-value-of-array-i/

class Solution {
    function resultArray($nums, $k) {
        $ans = array_fill(0, $k, 0);
        $dp = array_fill(0, $k, 0);
        foreach ($nums as $num) {
            $newDp = array_fill(0, $k, 0);
            $nm = $num % $k;
            $newDp[$nm] = 1;
            for ($i = 0; $i < $k; $i++) $newDp[($i * $nm) % $k] += $dp[$i];
            for ($i = 0; $i < $k; $i++) $ans[$i] += $newDp[$i];
            $dp = $newDp;
        }
        return $ans;
    }
}
''')

add("3525_find_x_value_of_array_ii", r'''<?php
// LeetCode 3525 - Find X Value of Array II
// https://leetcode.com/problems/find-x-value-of-array-ii/

class Solution {
    function resultArray($nums, $k, $queries) {
        $n = count($nums);
        $ans = array_fill(0, count($queries), 0);
        for ($qi = 0; $qi < count($queries); $qi++) {
            $idx = $queries[$qi][0];
            $val = $queries[$qi][1];
            $start = $queries[$qi][2];
            $x = $queries[$qi][3];
            $nums[$idx] = $val;
            $prod = 1;
            $cnt = 0;
            for ($i = $start; $i < $n; $i++) {
                $prod = $prod * ($nums[$i] % $k) % $k;
                if ($prod === $x) $cnt++;
            }
            $ans[$qi] = $cnt;
        }
        return $ans;
    }
}
''')

add("3526_range_xor_queries_with_subarray_reversals", r'''<?php
// LeetCode 3526 - Range XOR Queries with Subarray Reversals
// https://leetcode.com/problems/range-xor-queries-with-subarray-reversals/

class Solution {
    function getResults($nums, $queries) {
        $a = $nums;
        $ans = [];
        foreach ($queries as $q) {
            $typ = $q[0];
            if ($typ === 1) {
                $l = $q[1];
                $r = $q[2];
                while ($l < $r) {
                    $tmp = $a[$l];
                    $a[$l] = $a[$r];
                    $a[$r] = $tmp;
                    $l++;
                    $r--;
                }
            } else if ($typ === 2) {
                $x = 0;
                for ($i = $q[1]; $i <= $q[2]; $i++) $x ^= $a[$i];
                $ans[] = $x;
            } else {
                $a[$q[1]] = $q[2];
            }
        }
        return $ans;
    }
}
''')

add("3527_find_the_most_common_response", r'''<?php
// LeetCode 3527 - Find the Most Common Response
// https://leetcode.com/problems/find-the-most-common-response/

class Solution {
    function findCommonResponse($responses) {
        $cnt = [];
        foreach ($responses as $ws) {
            $s = [];
            foreach ($ws as $w) {
                if (!isset($s[$w])) {
                    $s[$w] = true;
                    $cnt[$w] = ($cnt[$w] ?? 0) + 1;
                }
            }
        }
        $ans = $responses[0][0];
        foreach ($cnt as $w => $v) {
            if ($cnt[$ans] < $v || ($cnt[$ans] === $v && $w < $ans)) $ans = $w;
        }
        return $ans;
    }
}
''')

add("3528_unit_conversion_i", r'''<?php
// LeetCode 3528 - Unit Conversion I
// https://leetcode.com/problems/unit-conversion-i/

class Solution {
    private $g;
    private $ans;
    private $mod = 1000000007;

    private function dfs($s, $mul) {
        $this->ans[$s] = $mul;
        foreach ($this->g[$s] as $e)
            $this->dfs($e[0], (int)(($mul * $e[1]) % $this->mod));
    }

    function baseUnitConversions($conversions) {
        $n = count($conversions) + 1;
        $this->g = array_fill(0, $n, []);
        foreach ($conversions as $e) $this->g[$e[0]][] = [$e[1], $e[2]];
        $this->ans = array_fill(0, $n, 0);
        $this->dfs(0, 1);
        return $this->ans;
    }
}
''')

add("3529_count_cells_in_overlapping_horizontal_and_vertical_substrings", r'''<?php
// LeetCode 3529 - Count Cells in Overlapping Horizontal and Vertical Substrings
// https://leetcode.com/problems/count-cells-in-overlapping-horizontal-and-vertical-substrings/

class Solution {
    function countCells($grid, $pattern) {
        $m = count($grid);
        $n = count($grid[0]);
        $row = '';
        $col = '';
        for ($i = 0; $i < $m; $i++) for ($j = 0; $j < $n; $j++) $row .= $grid[$i][$j];
        for ($j = 0; $j < $n; $j++) for ($i = 0; $i < $m; $i++) $col .= $grid[$i][$j];
        $hMark = [];
        $vMark = [];
        for ($i = 0; $i < $m; $i++) {
            $hMark[$i] = array_fill(0, $n, false);
            $vMark[$i] = array_fill(0, $n, false);
        }
        $plen = strlen($pattern);
        $rlen = strlen($row);
        for ($i = 0; $i + $plen <= $rlen; $i++) {
            if (substr($row, $i, $plen) === $pattern) {
                for ($t = 0; $t < $plen; $t++) {
                    $pos = $i + $t;
                    $hMark[intdiv($pos, $n)][$pos % $n] = true;
                }
            }
        }
        $clen = strlen($col);
        for ($i = 0; $i + $plen <= $clen; $i++) {
            if (substr($col, $i, $plen) === $pattern) {
                for ($t = 0; $t < $plen; $t++) {
                    $pos = $i + $t;
                    $vMark[$pos % $m][intdiv($pos, $m)] = true;
                }
            }
        }
        $ans = 0;
        for ($i = 0; $i < $m; $i++) for ($j = 0; $j < $n; $j++)
            if ($hMark[$i][$j] && $vMark[$i][$j]) $ans++;
        return $ans;
    }
}
''')

add("3530_maximum_profit_from_valid_topological_order_in_dag", r'''<?php
// LeetCode 3530 - Maximum Profit from Valid Topological Order in DAG
// https://leetcode.com/problems/maximum-profit-from-valid-topological-order-in-dag/

class Solution {
    private function popcount($x) {
        $c = 0;
        while ($x !== 0) { $c += $x & 1; $x >>= 1; }
        return $c;
    }

    function maxProfit($n, $edges, $score) {
        $need = array_fill(0, $n, 0);
        $dp = array_fill(0, 1 << $n, -1);
        $dp[0] = 0;
        foreach ($edges as $e) $need[$e[1]] |= 1 << $e[0];
        for ($mask = 0; $mask < (1 << $n); $mask++) {
            if ($dp[$mask] < 0) continue;
            $pos = $this->popcount($mask) + 1;
            for ($i = 0; $i < $n; $i++) {
                if ((($mask >> $i) & 1) !== 0) continue;
                if (($mask & $need[$i]) === $need[$i]) {
                    $nm = $mask | (1 << $i);
                    $v = $dp[$mask] + $score[$i] * $pos;
                    if ($v > $dp[$nm]) $dp[$nm] = $v;
                }
            }
        }
        return $dp[(1 << $n) - 1];
    }
}
''')

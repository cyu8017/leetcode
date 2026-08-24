#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
SOLUTIONS = {}

def add(folder, body):
    SOLUTIONS[folder] = body


add("3583_count_special_triplets", r'''<?php
// LeetCode 3583 - Count Special Triplets
// https://leetcode.com/problems/count-special-triplets/

class Solution {
    function specialTriplets($nums) {
        $left = [];
        $right = [];
        foreach ($nums as $x) $right[$x] = ($right[$x] ?? 0) + 1;
        $ans = 0;
        $mod = 1000000007;
        foreach ($nums as $x) {
            $right[$x] = $right[$x] - 1;
            $lv = $left[$x * 2] ?? 0;
            $rv = $right[$x * 2] ?? 0;
            $ans = ($ans + $lv * $rv % $mod) % $mod;
            $left[$x] = ($left[$x] ?? 0) + 1;
        }
        return $ans;
    }
}
''')

add("3584_maximum_product_of_first_and_last_elements_of_a_subsequence", r'''<?php
// LeetCode 3584 - Maximum Product of First and Last Elements of a Subsequence
// https://leetcode.com/problems/maximum-product-of-first-and-last-elements-of-a-subsequence/

class Solution {
    function maximumProduct($nums, $m) {
        $ans = PHP_INT_MIN;
        $mx = PHP_INT_MIN;
        $mi = PHP_INT_MAX;
        $n = count($nums);
        for ($i = $m - 1; $i < $n; $i++) {
            $x = $nums[$i];
            $y = $nums[$i - $m + 1];
            $mi = min($mi, $y);
            $mx = max($mx, $y);
            $ans = max($ans, max($x * $mi, $x * $mx));
        }
        return $ans;
    }
}
''')

add("3585_find_weighted_median_node_in_tree", r'''<?php
// LeetCode 3585 - Find Weighted Median Node in Tree
// https://leetcode.com/problems/find-weighted-median-node-in-tree/

class Solution {
    function findMedian($n, $edges, $queries) {
        $g = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $g[$e[0]][] = [$e[1], $e[2]];
            $g[$e[1]][] = [$e[0], $e[2]];
        }
        $ans = array_fill(0, count($queries), 0);
        for ($qi = 0; $qi < count($queries); $qi++) {
            $u = $queries[$qi][0];
            $v = $queries[$qi][1];
            $parent = array_fill(0, $n, -2);
            $pw = array_fill(0, $n, 0);
            $parent[$u] = -1;
            $q = [$u];
            while (count($q)) {
                $x = array_shift($q);
                if ($x === $v) break;
                foreach ($g[$x] as $e) {
                    if ($parent[$e[0]] === -2) {
                        $parent[$e[0]] = $x;
                        $pw[$e[0]] = $e[1];
                        $q[] = $e[0];
                    }
                }
            }
            $nodes = [$v];
            $weights = [];
            $cur = $v;
            while ($cur !== $u) {
                $weights[] = $pw[$cur];
                $cur = $parent[$cur];
                $nodes[] = $cur;
            }
            $nodes = array_reverse($nodes);
            $weights = array_reverse($weights);
            $total = 0;
            foreach ($weights as $w) $total += $w;
            $need = intdiv($total + 1, 2);
            $sum = 0;
            $med = $u;
            for ($i = 0; $i < count($weights); $i++) {
                $sum += $weights[$i];
                $med = $nodes[$i + 1];
                if ($sum >= $need) break;
            }
            $ans[$qi] = $med;
        }
        return $ans;
    }
}
''')

add("3587_minimum_adjacent_swaps_to_alternate_parity", r'''<?php
// LeetCode 3587 - Minimum Adjacent Swaps to Alternate Parity
// https://leetcode.com/problems/minimum-adjacent-swaps-to-alternate-parity/

class Solution {
    private function calc($pos, $n, $k) {
        $res = 0;
        for ($i = 0; $i < $n; $i += 2) $res += abs($pos[$k][intdiv($i, 2)] - $i);
        return $res;
    }

    function minSwaps($nums) {
        $pos = [[], []];
        for ($i = 0; $i < count($nums); $i++) $pos[$nums[$i] & 1][] = $i;
        if (abs(count($pos[0]) - count($pos[1])) > 1) return -1;
        if (count($pos[0]) > count($pos[1])) return $this->calc($pos, count($nums), 0);
        if (count($pos[0]) < count($pos[1])) return $this->calc($pos, count($nums), 1);
        return min($this->calc($pos, count($nums), 0), $this->calc($pos, count($nums), 1));
    }
}
''')

add("3588_find_maximum_area_of_a_triangle", r'''<?php
// LeetCode 3588 - Find Maximum Area of a Triangle
// https://leetcode.com/problems/find-maximum-area-of-a-triangle/

class Solution {
    private function calc(&$coords) {
        $mn = 1e9;
        $mx = 0;
        $f = [];
        $g = [];
        foreach ($coords as $c) {
            $x = $c[0];
            $y = $c[1];
            $mn = min($mn, $x);
            $mx = max($mx, $x);
            if (isset($f[$x])) {
                $f[$x] = min($f[$x], $y);
                $g[$x] = max($g[$x], $y);
            } else {
                $f[$x] = $y;
                $g[$x] = $y;
            }
        }
        $ans = 0;
        foreach ($f as $x => $y) {
            $d = $g[$x] - $y;
            $ans = max($ans, $d * max($mx - $x, $x - $mn));
        }
        return $ans;
    }

    function maxArea($coords) {
        $ans = $this->calc($coords);
        foreach ($coords as &$c) {
            $t = $c[0];
            $c[0] = $c[1];
            $c[1] = $t;
        }
        unset($c);
        $ans = max($ans, $this->calc($coords));
        return $ans > 0 ? $ans : -1;
    }
}
''')

add("3589_count_prime_gap_balanced_subarrays", r'''<?php
// LeetCode 3589 - Count Prime-Gap Balanced Subarrays
// https://leetcode.com/problems/count-prime-gap-balanced-subarrays/

class Solution {
    function primeSubarray($nums, $k) {
        $mx = 0;
        foreach ($nums as $v) $mx = max($mx, $v);
        $isPrime = array_fill(0, $mx + 1, false);
        for ($i = 2; $i <= $mx; $i++) $isPrime[$i] = true;
        for ($i = 2; $i * $i <= $mx; $i++)
            if ($isPrime[$i])
                for ($j = $i * $i; $j <= $mx; $j += $i) $isPrime[$j] = false;
        $n = count($nums);
        $ans = 0;
        for ($l = 0; $l < $n; $l++) {
            $primes = [];
            for ($r = $l; $r < $n; $r++) {
                if ($isPrime[$nums[$r]]) $primes[] = $nums[$r];
                if (count($primes) >= 2) {
                    $mn = $primes[0];
                    $mxp = $primes[0];
                    foreach ($primes as $p) {
                        $mn = min($mn, $p);
                        $mxp = max($mxp, $p);
                    }
                    if ($mxp - $mn <= $k) $ans++;
                }
            }
        }
        return $ans;
    }
}
''')

add("3590_kth_smallest_path_xor_sum", r'''<?php
// LeetCode 3590 - Kth Smallest Path XOR Sum
// https://leetcode.com/problems/kth-smallest-path-xor-sum/

class Solution {
    private $g;
    private $vals;
    private $xorPath;
    private $inT;
    private $outT;
    private $order;

    private function dfs($u) {
        $this->xorPath[$u] ^= $this->vals[$u];
        foreach ($this->g[$u] as $v) {
            $this->xorPath[$v] = $this->xorPath[$u];
            $this->dfs($v);
        }
    }

    private function dfs2($u) {
        $this->inT[$u] = count($this->order);
        $this->order[] = $this->xorPath[$u];
        foreach ($this->g[$u] as $v) $this->dfs2($v);
        $this->outT[$u] = count($this->order);
    }

    function kthSmallest($par, $vals, $queries) {
        $n = count($par);
        $this->g = array_fill(0, $n, []);
        for ($i = 1; $i < $n; $i++) $this->g[$par[$i]][] = $i;
        $this->vals = $vals;
        $this->xorPath = array_fill(0, $n, 0);
        $this->dfs(0);
        $this->inT = array_fill(0, $n, 0);
        $this->outT = array_fill(0, $n, 0);
        $this->order = [];
        $this->dfs2(0);
        $ans = array_fill(0, count($queries), 0);
        for ($i = 0; $i < count($queries); $i++) {
            $u = $queries[$i][0];
            $k = $queries[$i][1];
            $sub = array_slice($this->order, $this->inT[$u], $this->outT[$u] - $this->inT[$u]);
            sort($sub);
            $uniq = [];
            foreach ($sub as $x) if (count($uniq) === 0 || $uniq[count($uniq) - 1] !== $x) $uniq[] = $x;
            $ans[$i] = $k > count($uniq) ? -1 : $uniq[$k - 1];
        }
        return $ans;
    }
}
''')

add("3591_check_if_any_element_has_prime_frequency", r'''<?php
// LeetCode 3591 - Check if Any Element Has Prime Frequency
// https://leetcode.com/problems/check-if-any-element-has-prime-frequency/

class Solution {
    private function isPrime($x) {
        if ($x < 2) return false;
        for ($i = 2; $i * $i <= $x; $i++) if ($x % $i === 0) return false;
        return true;
    }

    function checkPrimeFrequency($nums) {
        $cnt = [];
        foreach ($nums as $x) $cnt[$x] = ($cnt[$x] ?? 0) + 1;
        foreach ($cnt as $v) if ($this->isPrime($v)) return true;
        return false;
    }
}
''')

add("3592_inverse_coin_change", r'''<?php
// LeetCode 3592 - Inverse Coin Change
// https://leetcode.com/problems/inverse-coin-change/

class Solution {
    function findCoins($numWays) {
        $n = count($numWays);
        $dp = array_fill(0, $n + 1, 0);
        $coins = [];
        $dp[0] = 1;
        for ($amt = 1; $amt <= $n; $amt++) {
            $ways = $numWays[$amt - 1];
            if ($dp[$amt] === $ways) continue;
            if ($dp[$amt] + 1 === $ways) {
                $coins[] = $amt;
                for ($x = $amt; $x <= $n; $x++) $dp[$x] += $dp[$x - $amt];
                if ($dp[$amt] !== $ways) return [];
                continue;
            }
            return [];
        }
        return $coins;
    }
}
''')

add("3593_minimum_increments_to_equalize_leaf_paths", r'''<?php
// LeetCode 3593 - Minimum Increments to Equalize Leaf Paths
// https://leetcode.com/problems/minimum-increments-to-equalize-leaf-paths/

class Solution {
    private $graph;
    private $cost;
    private $ans;

    private function dfs($u, $p) {
        if (count($this->graph[$u]) === 1 && $p !== -1) return $this->cost[$u];
        $childVals = [];
        foreach ($this->graph[$u] as $v) {
            if ($v === $p) continue;
            $childVals[] = $this->dfs($v, $u);
        }
        if (count($childVals) === 0) return $this->cost[$u];
        $mx = 0;
        foreach ($childVals as $c) $mx = max($mx, $c);
        foreach ($childVals as $c) if ($c < $mx) $this->ans++;
        return $mx + $this->cost[$u];
    }

    function minIncrease($n, $edges, $cost) {
        $this->graph = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $this->graph[$e[0]][] = $e[1];
            $this->graph[$e[1]][] = $e[0];
        }
        $this->cost = $cost;
        $this->ans = 0;
        $this->dfs(0, -1);
        return $this->ans;
    }
}
''')

add("3594_minimum_time_to_transport_all_individuals", r'''<?php
// LeetCode 3594 - Minimum Time to Transport All Individuals
// https://leetcode.com/problems/minimum-time-to-transport-all-individuals/

class Solution {
    function minTime($n, $k, $m, $time, $mul) {
        $t = $time;
        sort($t);
        $total = 0;
        $stage = 0;
        $left = $n;
        while ($left > 0) {
            $take = min($k, $left);
            $slow = $t[$left - 1];
            $total += $slow * $mul[$stage % $m];
            $left -= $take;
            $stage++;
            if ($left > 0) {
                $total += $t[0] * $mul[$stage % $m];
                $stage++;
            }
        }
        return $total;
    }
}
''')

add("3595_once_twice", r'''<?php
// LeetCode 3595 - Once Twice
// https://leetcode.com/problems/once-twice/

class Solution {
    function onceTwice($nums) {
        $freq = [];
        foreach ($nums as $x) $freq[$x] = ($freq[$x] ?? 0) + 1;
        $a = 0;
        $b = 0;
        foreach ($freq as $k => $v) {
            if ($v === 1) $a = $k;
            else if ($v === 2) $b = $k;
        }
        return [$a, $b];
    }
}
''')

add("3596_minimum_cost_path_with_alternating_directions_i", r'''<?php
// LeetCode 3596 - Minimum Cost Path with Alternating Directions I
// https://leetcode.com/problems/minimum-cost-path-with-alternating-directions-i/

class Solution {
    function minCost($m, $n) {
        if ($m === 1 && $n === 1) return 1;
        if ($m === 1 && $n === 2) return 3;
        if ($m === 2 && $n === 1) return 3;
        return -1;
    }
}
''')

add("3597_partition_string", r'''<?php
// LeetCode 3597 - Partition String
// https://leetcode.com/problems/partition-string/

class Solution {
    function partitionString($s) {
        $vis = [];
        $ans = [];
        $t = '';
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $t .= $s[$i];
            if (!isset($vis[$t])) {
                $vis[$t] = true;
                $ans[] = $t;
                $t = '';
            }
        }
        return $ans;
    }
}
''')

add("3598_longest_common_prefix_between_adjacent_strings_after_removals", r'''<?php
// LeetCode 3598 - Longest Common Prefix Between Adjacent Strings After Removals
// https://leetcode.com/problems/longest-common-prefix-between-adjacent-strings-after-removals/

class Solution {
    private $n;
    private $words;
    private $tm;
    private $keys;

    private function calc($s, $t) {
        $m = min(strlen($s), strlen($t));
        for ($k = 0; $k < $m; $k++) if ($s[$k] !== $t[$k]) return $k;
        return $m;
    }

    private function addKey($x) {
        if (!isset($this->tm[$x])) {
            $this->tm[$x] = 0;
            $lo = 0;
            $hi = count($this->keys);
            while ($lo < $hi) {
                $mid = ($lo + $hi) >> 1;
                if ($this->keys[$mid] < $x) $lo = $mid + 1;
                else $hi = $mid;
            }
            array_splice($this->keys, $lo, 0, [$x]);
        }
        $this->tm[$x]++;
    }

    private function remKey($x) {
        $c = $this->tm[$x] - 1;
        if ($c === 0) {
            unset($this->tm[$x]);
            $ix = array_search($x, $this->keys, true);
            if ($ix !== false) array_splice($this->keys, $ix, 1);
        } else $this->tm[$x] = $c;
    }

    private function add($i, $j) {
        if ($i >= 0 && $i < $this->n && $j >= 0 && $j < $this->n)
            $this->addKey($this->calc($this->words[$i], $this->words[$j]));
    }

    private function remove($i, $j) {
        if ($i >= 0 && $i < $this->n && $j >= 0 && $j < $this->n)
            $this->remKey($this->calc($this->words[$i], $this->words[$j]));
    }

    function longestCommonPrefix($words) {
        $this->n = count($words);
        $this->words = $words;
        $this->tm = [];
        $this->keys = [];
        for ($i = 0; $i + 1 < $this->n; $i++) $this->add($i, $i + 1);
        $ans = array_fill(0, $this->n, 0);
        for ($i = 0; $i < $this->n; $i++) {
            $this->remove($i, $i + 1);
            $this->remove($i - 1, $i);
            $this->add($i - 1, $i + 1);
            if (count($this->keys) && $this->keys[count($this->keys) - 1] > 0)
                $ans[$i] = $this->keys[count($this->keys) - 1];
            $this->remove($i - 1, $i + 1);
            $this->add($i - 1, $i);
            $this->add($i, $i + 1);
        }
        return $ans;
    }
}
''')

add("3599_partition_array_to_minimize_xor", r'''<?php
// LeetCode 3599 - Partition Array to Minimize XOR
// https://leetcode.com/problems/partition-array-to-minimize-xor/

class Solution {
    function minXor($nums, $k) {
        $n = count($nums);
        $g = array_fill(0, $n + 1, 0);
        for ($i = 1; $i <= $n; $i++) $g[$i] = $g[$i - 1] ^ $nums[$i - 1];
        $Inf = intdiv(2147483647, 2);
        $f = [];
        for ($i = 0; $i <= $n; $i++) $f[$i] = array_fill(0, $k + 1, $Inf);
        $f[0][0] = 0;
        for ($i = 1; $i <= $n; $i++) {
            for ($j = 1; $j <= min($i, $k); $j++) {
                for ($h = $j - 1; $h < $i; $h++) {
                    $f[$i][$j] = min($f[$i][$j], max($f[$h][$j - 1], $g[$i] ^ $g[$h]));
                }
            }
        }
        return $f[$n][$k];
    }
}
''')

add("3600_maximize_spanning_tree_stability_with_upgrades", r'''<?php
// LeetCode 3600 - Maximize Spanning Tree Stability with Upgrades
// https://leetcode.com/problems/maximize-spanning-tree-stability-with-upgrades/

class UnionFind3600 {
    public $p;
    public $size;
    public $cnt;

    function __construct($n) {
        $this->p = [];
        $this->size = [];
        $this->cnt = $n;
        for ($i = 0; $i < $n; $i++) { $this->p[$i] = $i; $this->size[$i] = 1; }
    }

    function find($x) {
        if ($this->p[$x] !== $x) $this->p[$x] = $this->find($this->p[$x]);
        return $this->p[$x];
    }

    function unite($a, $b) {
        $pa = $this->find($a);
        $pb = $this->find($b);
        if ($pa === $pb) return false;
        if ($this->size[$pa] > $this->size[$pb]) {
            $this->p[$pb] = $pa;
            $this->size[$pa] += $this->size[$pb];
        } else {
            $this->p[$pa] = $pb;
            $this->size[$pb] += $this->size[$pa];
        }
        $this->cnt--;
        return true;
    }
}

class Solution {
    private $n;
    private $edges;
    private $k;

    private function check($lim) {
        $uf = new UnionFind3600($this->n);
        foreach ($this->edges as $e) if ($e[2] >= $lim) $uf->unite($e[0], $e[1]);
        $rem = $this->k;
        foreach ($this->edges as $e) {
            if ($e[2] * 2 >= $lim && $rem > 0) {
                if ($uf->unite($e[0], $e[1])) $rem--;
            }
        }
        return $uf->cnt === 1;
    }

    function maxStability($n, $edges, $k) {
        $this->n = $n;
        $this->edges = $edges;
        $this->k = $k;
        $uf = new UnionFind3600($n);
        $mn = 1000000;
        foreach ($edges as $e) {
            if ($e[3] === 1) {
                $mn = min($mn, $e[2]);
                if (!$uf->unite($e[0], $e[1])) return -1;
            }
        }
        foreach ($edges as $e) $uf->unite($e[0], $e[1]);
        if ($uf->cnt > 1) return -1;
        $l = 1;
        $r = $mn;
        while ($l < $r) {
            $mid = ($l + $r + 1) >> 1;
            if ($this->check($mid)) $l = $mid;
            else $r = $mid - 1;
        }
        return $l;
    }
}
''')

add("3602_hexadecimal_and_hexatrigesimal_conversion", r'''<?php
// LeetCode 3602 - Hexadecimal and Hexatrigesimal Conversion
// https://leetcode.com/problems/hexadecimal-and-hexatrigesimal-conversion/

class Solution {
    private function f($x, $k) {
        $res = '';
        while ($x > 0) {
            $v = $x % $k;
            $res .= $v <= 9 ? chr(48 + $v) : chr(65 + $v - 10);
            $x = intdiv($x, $k);
        }
        return strrev($res);
    }

    function concatHex36($n) {
        return $this->f($n * $n, 16) . $this->f($n * $n * $n, 36);
    }
}
''')

add("3603_minimum_cost_path_with_alternating_directions_ii", r'''<?php
// LeetCode 3603 - Minimum Cost Path with Alternating Directions II
// https://leetcode.com/problems/minimum-cost-path-with-alternating-directions-ii/

class Solution {
    private function entry($i, $j) {
        return ($i + 1) * ($j + 1);
    }

    function minCost($m, $n, $waitCost) {
        $INF = PHP_INT_MAX >> 2;
        $dp = [];
        for ($i = 0; $i < $m; $i++) $dp[$i] = array_fill(0, $n, $INF);
        $dp[0][0] = $this->entry(0, 0);
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if ($i === 0 && $j === 0) continue;
                if ($i > 0) {
                    $cand = $dp[$i - 1][$j] + $this->entry($i, $j);
                    if (!($i - 1 === 0 && $j === 0)) $cand += $waitCost[$i - 1][$j];
                    $dp[$i][$j] = min($dp[$i][$j], $cand);
                }
                if ($j > 0) {
                    $cand = $dp[$i][$j - 1] + $this->entry($i, $j);
                    if (!($i === 0 && $j - 1 === 0)) $cand += $waitCost[$i][$j - 1];
                    $dp[$i][$j] = min($dp[$i][$j], $cand);
                }
            }
        }
        return $dp[$m - 1][$n - 1];
    }
}
''')

add("3604_minimum_time_to_reach_destination_in_directed_graph", r'''<?php
// LeetCode 3604 - Minimum Time to Reach Destination in Directed Graph
// https://leetcode.com/problems/minimum-time-to-reach-destination-in-directed-graph/

class Solution {
    function minTime($n, $edges) {
        $g = array_fill(0, $n, []);
        foreach ($edges as $e) $g[$e[0]][] = [$e[1], $e[2], $e[3]];
        $Inf = 1e18;
        $dist = array_fill(0, $n, $Inf);
        $dist[0] = 0;
        $pq = [[0, 0]];
        $push = function($t, $u) use (&$pq) {
            $lo = 0;
            $hi = count($pq);
            while ($lo < $hi) {
                $mid = ($lo + $hi) >> 1;
                if ($pq[$mid][0] < $t) $lo = $mid + 1;
                else $hi = $mid;
            }
            array_splice($pq, $lo, 0, [[$t, $u]]);
        };
        while (count($pq)) {
            $cur = array_shift($pq);
            $t = $cur[0];
            $u = $cur[1];
            if ($t !== $dist[$u]) continue;
            if ($u === $n - 1) return $t;
            foreach ($g[$u] as $e) {
                $nt = $t;
                if ($nt > $e[2]) continue;
                if ($nt < $e[1]) $nt = $e[1];
                $nt += 1;
                if ($nt < $dist[$e[0]]) {
                    $dist[$e[0]] = $nt;
                    $push($nt, $e[0]);
                }
            }
        }
        return $dist[$n - 1] === $Inf ? -1 : $dist[$n - 1];
    }
}
''')

add("3605_minimum_stability_factor_of_array", r'''<?php
// LeetCode 3605 - Minimum Stability Factor of Array
// https://leetcode.com/problems/minimum-stability-factor-of-array/

class Solution {
    private function gcd($a, $b) {
        while ($b !== 0) { $t = $a % $b; $a = $b; $b = $t; }
        return $a;
    }

    private function ok($nums, $maxC, $x) {
        $n = count($nums);
        if ($x >= $n) return true;
        $changes = 0;
        $i = 0;
        while ($i + $x < $n) {
            $g = $nums[$i];
            for ($j = $i + 1; $j <= $i + $x; $j++) $g = $this->gcd($g, $nums[$j]);
            if ($g > 1) {
                $changes++;
                $i += $x + 1;
            } else {
                $i++;
            }
        }
        return $changes <= $maxC;
    }

    function minStable($nums, $maxC) {
        $n = count($nums);
        $lo = 0;
        $hi = $n;
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi, 2);
            if ($this->ok($nums, $maxC, $mid)) $hi = $mid;
            else $lo = $mid + 1;
        }
        return $lo;
    }
}
''')

add("3606_coupon_code_validator", r'''<?php
// LeetCode 3606 - Coupon Code Validator
// https://leetcode.com/problems/coupon-code-validator/

class Solution {
    private function check($s) {
        if ($s === '' || $s === null) return false;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $c = $s[$i];
            if (!(($c >= 'A' && $c <= 'Z') || ($c >= 'a' && $c <= 'z') || ($c >= '0' && $c <= '9') || $c === '_'))
                return false;
        }
        return true;
    }

    function validateCoupons($code, $businessLine, $isActive) {
        $bs = ['electronics' => 1, 'grocery' => 1, 'pharmacy' => 1, 'restaurant' => 1];
        $idx = [];
        for ($i = 0; $i < count($code); $i++) {
            if ($isActive[$i] && isset($bs[$businessLine[$i]]) && $this->check($code[$i])) $idx[] = $i;
        }
        usort($idx, function($i, $j) use ($businessLine, $code) {
            $c = $businessLine[$i] <=> $businessLine[$j];
            if ($c !== 0) return $c;
            return $code[$i] <=> $code[$j];
        });
        $ans = [];
        foreach ($idx as $i) $ans[] = $code[$i];
        return $ans;
    }
}
''')

add("3607_power_grid_maintenance", r'''<?php
// LeetCode 3607 - Power Grid Maintenance
// https://leetcode.com/problems/power-grid-maintenance/

class Solution {
    private $parent;

    private function find($x) {
        if ($this->parent[$x] !== $x) $this->parent[$x] = $this->find($this->parent[$x]);
        return $this->parent[$x];
    }

    private function unite($a, $b) {
        $ra = $this->find($a);
        $rb = $this->find($b);
        if ($ra !== $rb) {
            if ($ra < $rb) $this->parent[$rb] = $ra;
            else $this->parent[$ra] = $rb;
        }
    }

    function processQueries($c, $connections, $queries) {
        $this->parent = [];
        for ($i = 0; $i <= $c; $i++) $this->parent[$i] = $i;
        foreach ($connections as $e) $this->unite($e[0], $e[1]);
        $online = array_fill(0, $c + 1, true);
        $comp = [];
        for ($i = 1; $i <= $c; $i++) {
            $r = $this->find($i);
            if (!isset($comp[$r])) $comp[$r] = [];
            $comp[$r][] = $i;
        }
        foreach ($comp as &$ids) sort($ids);
        unset($ids);
        $ptr = [];
        $ans = [];
        foreach ($queries as $q) {
            $t = $q[0];
            $x = $q[1];
            if ($t === 2) {
                $online[$x] = false;
                continue;
            }
            if ($online[$x]) {
                $ans[] = $x;
                continue;
            }
            $r = $this->find($x);
            $ids = $comp[$r];
            $p = $ptr[$r] ?? 0;
            while ($p < count($ids) && !$online[$ids[$p]]) $p++;
            $ptr[$r] = $p;
            $ans[] = $p < count($ids) ? $ids[$p] : -1;
        }
        return $ans;
    }
}
''')

add("3608_minimum_time_for_k_connected_components", r'''<?php
// LeetCode 3608 - Minimum Time for K Connected Components
// https://leetcode.com/problems/minimum-time-for-k-connected-components/

class UnionFind3608 {
    public $p;
    public $size;

    function __construct($n) {
        $this->p = [];
        $this->size = [];
        for ($i = 0; $i < $n; $i++) { $this->p[$i] = $i; $this->size[$i] = 1; }
    }

    function find($x) {
        if ($this->p[$x] !== $x) $this->p[$x] = $this->find($this->p[$x]);
        return $this->p[$x];
    }

    function unite($a, $b) {
        $pa = $this->find($a);
        $pb = $this->find($b);
        if ($pa === $pb) return false;
        if ($this->size[$pa] > $this->size[$pb]) {
            $this->p[$pb] = $pa;
            $this->size[$pa] += $this->size[$pb];
        } else {
            $this->p[$pa] = $pb;
            $this->size[$pb] += $this->size[$pa];
        }
        return true;
    }
}

class Solution {
    function minTime($n, $edges, $k) {
        usort($edges, function($a, $b) { return $a[2] <=> $b[2]; });
        $uf = new UnionFind3608($n);
        $cnt = $n;
        for ($i = count($edges) - 1; $i >= 0; $i--) {
            if ($uf->unite($edges[$i][0], $edges[$i][1])) {
                $cnt--;
                if ($cnt < $k) return $edges[$i][2];
            }
        }
        return 0;
    }
}
''')

add("3609_minimum_moves_to_reach_target_in_grid", r'''<?php
// LeetCode 3609 - Minimum Moves to Reach Target in Grid
// https://leetcode.com/problems/minimum-moves-to-reach-target-in-grid/

class Solution {
    function minMoves($sx, $sy, $tx, $ty) {
        $ans = 0;
        while ($tx > $sx || $ty > $sy) {
            if ($tx < $sx || $ty < $sy) return -1;
            if ($tx === $ty) return -1;
            if ($tx > $ty) {
                if ($ty > $sy) {
                    if ($tx >= 2 * $ty) {
                        if ($tx % 2 !== 0) return -1;
                        $tx = intdiv($tx, 2);
                    } else {
                        $tx -= $ty;
                    }
                    $ans++;
                } else {
                    if ($ty !== $sy) return -1;
                    while ($tx > $sx) {
                        if ($tx >= 2 * $ty) {
                            if ($tx % 2 !== 0) return -1;
                            $tx = intdiv($tx, 2);
                        } else {
                            $tx -= $ty;
                        }
                        $ans++;
                        if ($tx < $sx) return -1;
                    }
                }
            } else {
                if ($tx > $sx) {
                    if ($ty >= 2 * $tx) {
                        if ($ty % 2 !== 0) return -1;
                        $ty = intdiv($ty, 2);
                    } else {
                        $ty -= $tx;
                    }
                    $ans++;
                } else {
                    if ($tx !== $sx) return -1;
                    while ($ty > $sy) {
                        if ($ty >= 2 * $tx) {
                            if ($ty % 2 !== 0) return -1;
                            $ty = intdiv($ty, 2);
                        } else {
                            $ty -= $tx;
                        }
                        $ans++;
                        if ($ty < $sy) return -1;
                    }
                }
            }
        }
        return ($tx === $sx && $ty === $sy) ? $ans : -1;
    }
}
''')

add("3610_minimum_number_of_primes_to_sum_to_target", r'''<?php
// LeetCode 3610 - Minimum Number of Primes to Sum to Target
// https://leetcode.com/problems/minimum-number-of-primes-to-sum-to-target/

class Solution {
    private static $primes = [];

    private function ensurePrimes() {
        if (count(self::$primes) > 0) return;
        $x = 2;
        while (count(self::$primes) < 1000) {
            $isPrime = true;
            foreach (self::$primes as $p) {
                if ($p * $p > $x) break;
                if ($x % $p === 0) { $isPrime = false; break; }
            }
            if ($isPrime) self::$primes[] = $x;
            $x++;
        }
    }

    function minNumberOfPrimes($n, $m) {
        $this->ensurePrimes();
        $Inf = intdiv(2147483647, 2);
        $f = array_fill(0, $n + 1, $Inf);
        $f[0] = 0;
        for ($pi = 0; $pi < $m; $pi++) {
            $x = self::$primes[$pi];
            for ($i = $x; $i <= $n; $i++)
                if ($f[$i - $x] + 1 < $f[$i]) $f[$i] = $f[$i - $x] + 1;
        }
        return $f[$n] < $Inf ? $f[$n] : -1;
    }
}
''')

add("3612_process_string_with_special_operations_i", r'''<?php
// LeetCode 3612 - Process String with Special Operations I
// https://leetcode.com/problems/process-string-with-special-operations-i/

class Solution {
    function processStr($s) {
        $result = [];
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $c = $s[$i];
            if (($c >= 'a' && $c <= 'z') || ($c >= 'A' && $c <= 'Z')) $result[] = $c;
            else if ($c === '*') {
                if (count($result) > 0) array_pop($result);
            } else if ($c === '#') $result = array_merge($result, $result);
            else if ($c === '%') $result = array_reverse($result);
        }
        return implode('', $result);
    }
}
''')

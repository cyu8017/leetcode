#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
SOLUTIONS = {}

def add(folder, body):
    SOLUTIONS[folder] = body


add("3556_sum_of_largest_prime_substrings", r'''<?php
// LeetCode 3556 - Sum of Largest Prime Substrings
// https://leetcode.com/problems/sum-of-largest-prime-substrings/

class Solution {
    private function isPrime($x) {
        if ($x < 2) return false;
        $sqrtX = (int)sqrt($x);
        for ($i = 2; $i <= $sqrtX; $i++) if ($x % $i === 0) return false;
        return true;
    }

    function sumOfLargestPrimes($s) {
        $st = [];
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $x = 0;
            for ($j = $i; $j < $n; $j++) {
                $x = $x * 10 + (ord($s[$j]) - 48);
                if ($this->isPrime($x)) $st[$x] = true;
            }
        }
        $nums = array_keys($st);
        sort($nums);
        $ans = 0;
        for ($i = count($nums) - 1; $i >= 0 && count($nums) - $i <= 3; $i--)
            $ans += $nums[$i];
        return $ans;
    }
}
''')

add("3557_find_maximum_number_of_non_intersecting_substrings", r'''<?php
// LeetCode 3557 - Find Maximum Number of Non Intersecting Substrings
// https://leetcode.com/problems/find-maximum-number-of-non-intersecting-substrings/

class Solution {
    function maxSubstrings($word) {
        $ans = 0;
        $first = [];
        $n = strlen($word);
        for ($i = 0; $i < $n; $i++) {
            $c = $word[$i];
            if (!isset($first[$c])) $first[$c] = $i;
            else if ($i - $first[$c] + 1 >= 4) {
                $ans++;
                $first = [];
            }
        }
        return $ans;
    }
}
''')

add("3558_number_of_ways_to_assign_edge_weights_i", r'''<?php
// LeetCode 3558 - Number of Ways to Assign Edge Weights I
// https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-i/

class Solution {
    private $g;

    private function dfs($i, $fa) {
        $res = 0;
        foreach ($this->g[$i] as $j) if ($j !== $fa) $res = max($res, $this->dfs($j, $i) + 1);
        return $res;
    }

    private function pow2($exp) {
        $a = 2;
        $res = 1;
        $m = 1000000007;
        while ($exp > 0) {
            if ($exp & 1) $res = (int)(($res * $a) % $m);
            $a = (int)(($a * $a) % $m);
            $exp >>= 1;
        }
        return $res;
    }

    function assignEdgeWeights($edges) {
        $n = count($edges) + 1;
        $this->g = array_fill(0, $n + 1, []);
        foreach ($edges as $e) {
            $this->g[$e[0]][] = $e[1];
            $this->g[$e[1]][] = $e[0];
        }
        return $this->pow2($this->dfs(1, 0) - 1);
    }
}
''')

add("3559_number_of_ways_to_assign_edge_weights_ii", r'''<?php
// LeetCode 3559 - Number of Ways to Assign Edge Weights II
// https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-ii/

class Solution {
    private $MOD = 1000000007;
    private $LOG = 17;
    private $depth;
    private $graph;
    private $parent;

    private function dfs($u, $p) {
        $this->parent[0][$u] = $p;
        foreach ($this->graph[$u] as $v) {
            if ($v !== $p) {
                $this->depth[$v] = $this->depth[$u] + 1;
                $this->dfs($v, $u);
            }
        }
    }

    private function lca($u, $v) {
        if ($this->depth[$u] < $this->depth[$v]) { $t = $u; $u = $v; $v = $t; }
        for ($k = $this->LOG - 1; $k >= 0; $k--)
            if ($this->parent[$k][$u] !== -1 && $this->depth[$this->parent[$k][$u]] >= $this->depth[$v]) $u = $this->parent[$k][$u];
        if ($u === $v) return $u;
        for ($k = $this->LOG - 1; $k >= 0; $k--)
            if ($this->parent[$k][$u] !== -1 && $this->parent[$k][$u] !== $this->parent[$k][$v]) {
                $u = $this->parent[$k][$u];
                $v = $this->parent[$k][$v];
            }
        return $this->parent[0][$u];
    }

    private function modPow($exp) {
        $base = 2;
        $res = 1;
        $m = $this->MOD;
        while ($exp > 0) {
            if ($exp & 1) $res = (int)(($res * $base) % $m);
            $base = (int)(($base * $base) % $m);
            $exp >>= 1;
        }
        return $res;
    }

    function assignEdgeWeights($edges, $queries) {
        $n = count($edges) + 1;
        $this->depth = array_fill(0, $n + 1, 0);
        $this->graph = array_fill(0, $n + 1, []);
        $this->parent = [];
        for ($k = 0; $k < $this->LOG; $k++) $this->parent[$k] = array_fill(0, $n + 1, -1);
        foreach ($edges as $e) {
            $this->graph[$e[0]][] = $e[1];
            $this->graph[$e[1]][] = $e[0];
        }
        $this->dfs(1, -1);
        for ($k = 1; $k < $this->LOG; $k++)
            for ($v = 1; $v <= $n; $v++)
                if ($this->parent[$k - 1][$v] !== -1) $this->parent[$k][$v] = $this->parent[$k - 1][$this->parent[$k - 1][$v]];
        $ans = array_fill(0, count($queries), 0);
        for ($i = 0; $i < count($queries); $i++) {
            $u = $queries[$i][0];
            $v = $queries[$i][1];
            if ($u === $v) { $ans[$i] = 0; continue; }
            $a = $this->lca($u, $v);
            $d = $this->depth[$u] + $this->depth[$v] - 2 * $this->depth[$a];
            $ans[$i] = $this->modPow($d - 1);
        }
        return $ans;
    }
}
''')

add("3560_find_minimum_log_transportation_cost", r'''<?php
// LeetCode 3560 - Find Minimum Log Transportation Cost
// https://leetcode.com/problems/find-minimum-log-transportation-cost/

class Solution {
    function minCuttingCost($n, $m, $k) {
        $x = max($n, $m);
        if ($x <= $k) return 0;
        return $k * ($x - $k);
    }
}
''')

add("3561_resulting_string_after_adjacent_removals", r'''<?php
// LeetCode 3561 - Resulting String After Adjacent Removals
// https://leetcode.com/problems/resulting-string-after-adjacent-removals/

class Solution {
    private function isContiguous($a, $b) {
        $x = abs(ord($a) - ord($b));
        return $x === 1 || $x === 25;
    }

    function resultingString($s) {
        $stk = [];
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $c = $s[$i];
            if (count($stk) > 0 && $this->isContiguous($stk[count($stk) - 1], $c))
                array_pop($stk);
            else $stk[] = $c;
        }
        return implode('', $stk);
    }
}
''')

add("3562_maximum_profit_from_trading_stocks_with_discounts", r'''<?php
// LeetCode 3562 - Maximum Profit from Trading Stocks with Discounts
// https://leetcode.com/problems/maximum-profit-from-trading-stocks-with-discounts/

class Solution {
    private $g;
    private $present;
    private $future;
    private $budget;

    private function dfs($u) {
        $nxt = [];
        for ($j = 0; $j <= $this->budget; $j++) $nxt[$j] = [0, 0];
        foreach ($this->g[$u] as $v) {
            $fv = $this->dfs($v);
            for ($j = $this->budget; $j >= 0; $j--) {
                for ($jv = 0; $jv <= $j; $jv++) {
                    for ($pre = 0; $pre < 2; $pre++) {
                        $nxt[$j][$pre] = max($nxt[$j][$pre], $nxt[$j - $jv][$pre] + $fv[$jv][$pre]);
                    }
                }
            }
        }
        $f = [];
        for ($j = 0; $j <= $this->budget; $j++) $f[$j] = [0, 0];
        $price = $this->future[$u - 1];
        for ($j = 0; $j <= $this->budget; $j++) {
            for ($pre = 0; $pre < 2; $pre++) {
                $cost = intdiv($this->present[$u - 1], $pre + 1);
                if ($j >= $cost) {
                    $buyProfit = $nxt[$j - $cost][1] + ($price - $cost);
                    $f[$j][$pre] = max($nxt[$j][0], $buyProfit);
                } else {
                    $f[$j][$pre] = $nxt[$j][0];
                }
            }
        }
        return $f;
    }

    function maxProfit($n, $present, $future, $hierarchy, $budget) {
        $this->g = array_fill(0, $n + 1, []);
        foreach ($hierarchy as $e) $this->g[$e[0]][] = $e[1];
        $this->present = $present;
        $this->future = $future;
        $this->budget = $budget;
        return $this->dfs(1)[$budget][0];
    }
}
''')

add("3563_lexicographically_smallest_string_after_adjacent_removals", r'''<?php
// LeetCode 3563 - Lexicographically Smallest String After Adjacent Removals
// https://leetcode.com/problems/lexicographically-smallest-string-after-adjacent-removals/

class Solution {
    private function isConsec($a, $b) {
        $d = abs(ord($a) - ord($b));
        return $d === 1 || $d === 25;
    }

    function lexicographicallySmallestString($s) {
        $n = strlen($s);
        $dp = [];
        for ($i = 0; $i <= $n; $i++) $dp[$i] = array_fill(0, $n + 1, '');
        for ($length = 1; $length <= $n; $length++) {
            for ($i = 0; $i + $length <= $n; $i++) {
                $j = $i + $length;
                $minStr = $s[$i] . $dp[$i + 1][$j];
                for ($k = $i + 1; $k < $j; $k++) {
                    if ($this->isConsec($s[$i], $s[$k]) && $dp[$i + 1][$k] === '') {
                        $cand = $dp[$k + 1][$j];
                        if ($cand < $minStr) $minStr = $cand;
                    }
                }
                $dp[$i][$j] = $minStr;
            }
        }
        return $dp[0][$n];
    }
}
''')

add("3565_sequential_grid_path_cover", r'''<?php
// LeetCode 3565 - Sequential Grid Path Cover
// https://leetcode.com/problems/sequential-grid-path-cover/

class Solution {
    private $grid;
    private $m;
    private $n;
    private $dirs;
    private $st;
    private $path;

    private function f($i, $j) {
        return $i * $this->n + $j;
    }

    private function dfs($i, $j, $v) {
        $this->path[] = [$i, $j];
        if (count($this->path) === $this->m * $this->n) return true;
        $idx = $this->f($i, $j);
        $this->st |= 1 << $idx;
        if ($this->grid[$i][$j] === $v) $v++;
        for ($t = 0; $t < 4; $t++) {
            $x = $i + $this->dirs[$t];
            $y = $j + $this->dirs[$t + 1];
            if (0 <= $x && $x < $this->m && 0 <= $y && $y < $this->n) {
                $idx2 = $this->f($x, $y);
                if ((($this->st >> $idx2) & 1) === 0 && ($this->grid[$x][$y] === 0 || $this->grid[$x][$y] === $v)) {
                    if ($this->dfs($x, $y, $v)) return true;
                }
            }
        }
        array_pop($this->path);
        $this->st ^= 1 << $idx;
        return false;
    }

    function findPath($grid, $k) {
        $this->grid = $grid;
        $this->m = count($grid);
        $this->n = count($grid[0]);
        $this->dirs = [-1, 0, 1, 0, -1];
        $this->st = 0;
        $this->path = [];
        for ($i = 0; $i < $this->m; $i++) {
            for ($j = 0; $j < $this->n; $j++) {
                if ($grid[$i][$j] === 0 || $grid[$i][$j] === 1) {
                    if ($this->dfs($i, $j, 1)) return $this->path;
                    $this->path = [];
                    $this->st = 0;
                }
            }
        }
        return [];
    }
}
''')

add("3566_partition_array_into_two_equal_product_subsets", r'''<?php
// LeetCode 3566 - Partition Array into Two Equal Product Subsets
// https://leetcode.com/problems/partition-array-into-two-equal-product-subsets/

class Solution {
    function checkEqualPartitions($nums, $target) {
        $n = count($nums);
        for ($i = 0; $i < (1 << $n); $i++) {
            $x = 1;
            $y = 1;
            for ($j = 0; $j < $n; $j++) {
                if ((($i >> $j) & 1) !== 0) $x *= $nums[$j];
                else $y *= $nums[$j];
                if ($x > $target || $y > $target) break;
            }
            if ($x === $target && $y === $target) return true;
        }
        return false;
    }
}
''')

add("3567_minimum_absolute_difference_in_sliding_submatrix", r'''<?php
// LeetCode 3567 - Minimum Absolute Difference in Sliding Submatrix
// https://leetcode.com/problems/minimum-absolute-difference-in-sliding-submatrix/

class Solution {
    function minAbsDiff($grid, $k) {
        $m = count($grid);
        $n = count($grid[0]);
        $ans = [];
        for ($i = 0; $i <= $m - $k; $i++) $ans[$i] = array_fill(0, $n - $k + 1, 0);
        for ($i = 0; $i <= $m - $k; $i++) {
            for ($j = 0; $j <= $n - $k; $j++) {
                $nums = [];
                for ($x = $i; $x < $i + $k; $x++)
                    for ($y = $j; $y < $j + $k; $y++) $nums[] = $grid[$x][$y];
                sort($nums);
                $d = 2147483647;
                for ($t = 1; $t < count($nums); $t++) {
                    if ($nums[$t] !== $nums[$t - 1]) $d = min($d, abs($nums[$t] - $nums[$t - 1]));
                }
                if ($d !== 2147483647) $ans[$i][$j] = $d;
            }
        }
        return $ans;
    }
}
''')

add("3568_minimum_moves_to_clean_the_classroom", r'''<?php
// LeetCode 3568 - Minimum Moves to Clean the Classroom
// https://leetcode.com/problems/minimum-moves-to-clean-the-classroom/

class Solution {
    function minMoves($classroom, $energy) {
        $m = count($classroom);
        $n = strlen($classroom[0]);
        $d = [];
        for ($i = 0; $i < $m; $i++) $d[$i] = array_fill(0, $n, 0);
        $x = 0;
        $y = 0;
        $cnt = 0;
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                $c = $classroom[$i][$j];
                if ($c === 'S') { $x = $i; $y = $j; }
                else if ($c === 'L') $d[$i][$j] = $cnt++;
            }
        }
        if ($cnt === 0) return 0;
        $vis = [];
        for ($i = 0; $i < $m; $i++) {
            $vis[$i] = [];
            for ($j = 0; $j < $n; $j++) {
                $vis[$i][$j] = [];
                for ($e = 0; $e <= $energy; $e++)
                    $vis[$i][$j][$e] = array_fill(0, 1 << $cnt, false);
            }
        }
        $q = [[$x, $y, $energy, (1 << $cnt) - 1]];
        $vis[$x][$y][$energy][(1 << $cnt) - 1] = true;
        $dirs = [-1, 0, 1, 0, -1];
        $ans = 0;
        while (count($q)) {
            $t = $q;
            $q = [];
            foreach ($t as $s) {
                $i = $s[0];
                $j = $s[1];
                $curEnergy = $s[2];
                $mask = $s[3];
                if ($mask === 0) return $ans;
                if ($curEnergy <= 0) continue;
                for ($k = 0; $k < 4; $k++) {
                    $nx = $i + $dirs[$k];
                    $ny = $j + $dirs[$k + 1];
                    if ($nx >= 0 && $nx < $m && $ny >= 0 && $ny < $n && $classroom[$nx][$ny] !== 'X') {
                        $nxtEnergy = $classroom[$nx][$ny] === 'R' ? $energy : $curEnergy - 1;
                        $nxtMask = $mask;
                        if ($classroom[$nx][$ny] === 'L') $nxtMask &= ~(1 << $d[$nx][$ny]);
                        if (!$vis[$nx][$ny][$nxtEnergy][$nxtMask]) {
                            $vis[$nx][$ny][$nxtEnergy][$nxtMask] = true;
                            $q[] = [$nx, $ny, $nxtEnergy, $nxtMask];
                        }
                    }
                }
            }
            $ans++;
        }
        return -1;
    }
}
''')

add("3569_maximize_count_of_distinct_primes_after_split", r'''<?php
// LeetCode 3569 - Maximize Count of Distinct Primes After Split
// https://leetcode.com/problems/maximize-count-of-distinct-primes-after-split/

class Solution {
    function maximumCount($nums, $queries) {
        $mx = 0;
        foreach ($nums as $v) $mx = max($mx, $v);
        foreach ($queries as $q) $mx = max($mx, $q[1]);
        $isP = array_fill(0, $mx + 1, false);
        for ($i = 2; $i <= $mx; $i++) $isP[$i] = true;
        for ($i = 2; $i * $i <= $mx; $i++) {
            if ($isP[$i]) for ($j = $i * $i; $j <= $mx; $j += $i) $isP[$j] = false;
        }
        $ans = array_fill(0, count($queries), 0);
        for ($qi = 0; $qi < count($queries); $qi++) {
            $nums[$queries[$qi][0]] = $queries[$qi][1];
            $best = 0;
            $left = [];
            $right = [];
            foreach ($nums as $v) if ($v <= $mx && $isP[$v]) $right[$v] = ($right[$v] ?? 0) + 1;
            for ($i = 0; $i < count($nums) - 1; $i++) {
                $v = $nums[$i];
                if ($v <= $mx && $isP[$v]) {
                    $left[$v] = ($left[$v] ?? 0) + 1;
                    $c = $right[$v] - 1;
                    if ($c === 0) unset($right[$v]);
                    else $right[$v] = $c;
                }
                $best = max($best, count($left) + count($right));
            }
            $ans[$qi] = $best;
        }
        return $ans;
    }
}
''')

add("3571_find_the_shortest_superstring_ii", r'''<?php
// LeetCode 3571 - Find the Shortest Superstring II
// https://leetcode.com/problems/find-the-shortest-superstring-ii/

class Solution {
    function shortestSuperstring($s1, $s2) {
        if (strlen($s1) > strlen($s2)) return $this->shortestSuperstring($s2, $s1);
        $m = strlen($s1);
        if (strpos($s2, $s1) !== false) return $s2;
        for ($i = 0; $i < $m; $i++) {
            if (str_starts_with($s2, substr($s1, $i))) return substr($s1, 0, $i) . $s2;
            $len = $m - $i;
            if (strlen($s2) >= $len && substr($s2, -$len) === substr($s1, 0, $len))
                return $s2 . substr($s1, $m - $i);
        }
        return $s1 . $s2;
    }
}
''')

add("3572_maximize_ysum_by_picking_a_triplet_of_distinct_xvalues", r'''<?php
// LeetCode 3572 - Maximize Y-Sum by Picking a Triplet of Distinct X-Values
// https://leetcode.com/problems/maximize-ysum-by-picking-a-triplet-of-distinct-xvalues/

class Solution {
    function maxSumDistinctTriplet($x, $y) {
        $n = count($x);
        $arr = [];
        for ($i = 0; $i < $n; $i++) $arr[] = [$x[$i], $y[$i]];
        usort($arr, function($a, $b) { return $b[1] <=> $a[1]; });
        $ans = 0;
        $vis = [];
        for ($i = 0; $i < $n; $i++) {
            $a = $arr[$i][0];
            $b = $arr[$i][1];
            if (!isset($vis[$a])) {
                $vis[$a] = true;
                $ans += $b;
                if (count($vis) === 3) return $ans;
            }
        }
        return -1;
    }
}
''')

add("3573_best_time_to_buy_and_sell_stock_v", r'''<?php
// LeetCode 3573 - Best Time to Buy and Sell Stock V
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-v/

class Solution {
    function maximumProfit($prices, $k) {
        $n = count($prices);
        $f = [];
        for ($i = 0; $i < $n; $i++) {
            $f[$i] = [];
            for ($j = 0; $j <= $k; $j++) $f[$i][$j] = [0, 0, 0];
        }
        for ($j = 1; $j <= $k; $j++) {
            $f[0][$j][1] = -$prices[0];
            $f[0][$j][2] = $prices[0];
        }
        for ($i = 1; $i < $n; $i++) {
            for ($j = 1; $j <= $k; $j++) {
                $f[$i][$j][0] = max($f[$i - 1][$j][0], max($f[$i - 1][$j][1] + $prices[$i], $f[$i - 1][$j][2] - $prices[$i]));
                $f[$i][$j][1] = max($f[$i - 1][$j][1], $f[$i - 1][$j - 1][0] - $prices[$i]);
                $f[$i][$j][2] = max($f[$i - 1][$j][2], $f[$i - 1][$j - 1][0] + $prices[$i]);
            }
        }
        return $f[$n - 1][$k][0];
    }
}
''')

add("3574_maximize_subarray_gcd_score", r'''<?php
// LeetCode 3574 - Maximize Subarray GCD Score
// https://leetcode.com/problems/maximize-subarray-gcd-score/

class Solution {
    private function gcd($a, $b) {
        while ($b !== 0) { $t = $a % $b; $a = $b; $b = $t; }
        return $a;
    }

    function maxGCDScore($nums, $k) {
        $n = count($nums);
        $cnt = array_fill(0, $n, 0);
        for ($i = 0; $i < $n; $i++) {
            $x = $nums[$i];
            while ($x % 2 === 0) { $cnt[$i]++; $x = intdiv($x, 2); }
        }
        $ans = 0;
        for ($l = 0; $l < $n; $l++) {
            $g = 0;
            $mi = 2147483647;
            $t = 0;
            for ($r = $l; $r < $n; $r++) {
                $g = $this->gcd($g, $nums[$r]);
                if ($cnt[$r] < $mi) { $mi = $cnt[$r]; $t = 1; }
                else if ($cnt[$r] === $mi) $t++;
                $score = $g * ($r - $l + 1);
                if ($t <= $k) $score *= 2;
                $ans = max($ans, $score);
            }
        }
        return $ans;
    }
}
''')

add("3575_maximum_good_subtree_score", r'''<?php
// LeetCode 3575 - Maximum Good Subtree Score
// https://leetcode.com/problems/maximum-good-subtree-score/

class Solution {
    private $MOD = 1000000007;
    private $g;
    private $vals;
    private $ans;

    private function digitMask($x) {
        $v = $x;
        $mask = 0;
        if ($x === 0) return [1, 1, 0];
        while ($x > 0) {
            $d = $x % 10;
            if (($mask & (1 << $d)) !== 0) return [0, 0, 0];
            $mask |= 1 << $d;
            $x = intdiv($x, 10);
        }
        return [$mask, 1, $v];
    }

    private function dfs($u) {
        $dp = [0 => 0];
        $dm = $this->digitMask($this->vals[$u]);
        if ($dm[1] === 1) $dp[$dm[0]] = $dm[2];
        foreach ($this->g[$u] as $c) {
            $child = $this->dfs($c);
            $ndp = [];
            foreach ($dp as $k1 => $v1) {
                foreach ($child as $k2 => $v2) {
                    if (($k1 & $k2) === 0) {
                        $nm = $k1 | $k2;
                        $ndp[$nm] = max($ndp[$nm] ?? 0, $v1 + $v2);
                    }
                }
            }
            foreach ($dp as $k => $v) $ndp[$k] = max($ndp[$k] ?? 0, $v);
            foreach ($child as $k => $v) $ndp[$k] = max($ndp[$k] ?? 0, $v);
            $dp = $ndp;
        }
        $best = 0;
        foreach ($dp as $s) $best = max($best, $s);
        $this->ans = ($this->ans + $best) % $this->MOD;
        return $dp;
    }

    function goodSubtreeSum($vals, $par) {
        $n = count($vals);
        $this->g = array_fill(0, $n, []);
        for ($i = 1; $i < $n; $i++) $this->g[$par[$i]][] = $i;
        $this->vals = $vals;
        $this->ans = 0;
        $this->dfs(0);
        return $this->ans;
    }
}
''')

add("3576_transform_array_to_all_equal_elements", r'''<?php
// LeetCode 3576 - Transform Array to All Equal Elements
// https://leetcode.com/problems/transform-array-to-all-equal-elements/

class Solution {
    private function check($nums, $target, $kk) {
        $cnt = 0;
        $sign = 1;
        $n = count($nums);
        for ($i = 0; $i < $n - 1; $i++) {
            $x = $nums[$i] * $sign;
            if ($x === $target) $sign = 1;
            else {
                $sign = -1;
                $cnt++;
            }
        }
        return $cnt <= $kk && $nums[$n - 1] * $sign === $target;
    }

    function canMakeEqual($nums, $k) {
        return $this->check($nums, $nums[0], $k) || $this->check($nums, -$nums[0], $k);
    }
}
''')

add("3577_count_the_number_of_computer_unlocking_permutations", r'''<?php
// LeetCode 3577 - Count the Number of Computer Unlocking Permutations
// https://leetcode.com/problems/count-the-number-of-computer-unlocking-permutations/

class Solution {
    function countPermutations($complexity) {
        $mod = 1000000007;
        $ans = 1;
        for ($i = 1; $i < count($complexity); $i++) {
            if ($complexity[$i] <= $complexity[0]) return 0;
            $ans = (int)(($ans * $i) % $mod);
        }
        return $ans;
    }
}
''')

add("3578_count_partitions_with_max_min_difference_at_most_k", r'''<?php
// LeetCode 3578 - Count Partitions With Max-Min Difference at Most K
// https://leetcode.com/problems/count-partitions-with-max-min-difference-at-most-k/

class Solution {
    private $sl;
    private $keys;

    private function add($v) {
        if (!isset($this->sl[$v])) {
            $this->sl[$v] = 0;
            $lo = 0;
            $hi = count($this->keys);
            while ($lo < $hi) {
                $mid = ($lo + $hi) >> 1;
                if ($this->keys[$mid] < $v) $lo = $mid + 1;
                else $hi = $mid;
            }
            array_splice($this->keys, $lo, 0, [$v]);
        }
        $this->sl[$v]++;
    }

    private function rem($v) {
        $c = $this->sl[$v] - 1;
        if ($c === 0) {
            unset($this->sl[$v]);
            $ix = array_search($v, $this->keys, true);
            if ($ix !== false) array_splice($this->keys, $ix, 1);
        } else $this->sl[$v] = $c;
    }

    function countPartitions($nums, $k) {
        $mod = 1000000007;
        $this->sl = [];
        $this->keys = [];
        $n = count($nums);
        $f = array_fill(0, $n + 1, 0);
        $g = array_fill(0, $n + 1, 0);
        $f[0] = $g[0] = 1;
        for ($l = 1, $r = 1; $r <= $n; $r++) {
            $this->add($nums[$r - 1]);
            while ($this->keys[count($this->keys) - 1] - $this->keys[0] > $k) {
                $this->rem($nums[$l - 1]);
                $l++;
            }
            $f[$r] = $g[$r - 1];
            if ($l >= 2) $f[$r] = ($f[$r] - $g[$l - 2] + $mod) % $mod;
            $g[$r] = ($g[$r - 1] + $f[$r]) % $mod;
        }
        return $f[$n];
    }
}
''')

add("3579_minimum_steps_to_convert_string_with_operations", r'''<?php
// LeetCode 3579 - Minimum Steps to Convert String with Operations
// https://leetcode.com/problems/minimum-steps-to-convert-string-with-operations/

class Solution {
    private $word1;
    private $word2;

    private function calc($l, $r, $rev) {
        $cnt = [];
        for ($i = 0; $i < 26; $i++) $cnt[$i] = array_fill(0, 26, 0);
        $res = 0;
        for ($i = $l; $i <= $r; $i++) {
            $j = $rev ? $r - ($i - $l) : $i;
            $a = ord($this->word1[$j]) - 97;
            $b = ord($this->word2[$i]) - 97;
            if ($a !== $b) {
                if ($cnt[$b][$a] > 0) $cnt[$b][$a]--;
                else {
                    $cnt[$a][$b]++;
                    $res++;
                }
            }
        }
        return $res;
    }

    function minOperations($word1, $word2) {
        $this->word1 = $word1;
        $this->word2 = $word2;
        $n = strlen($word1);
        $f = array_fill(0, $n + 1, intdiv(2147483647, 2));
        $f[0] = 0;
        for ($i = 1; $i <= $n; $i++) {
            for ($j = 0; $j < $i; $j++) {
                $a = $this->calc($j, $i - 1, false);
                $b = 1 + $this->calc($j, $i - 1, true);
                $f[$i] = min($f[$i], $f[$j] + min($a, $b));
            }
        }
        return $f[$n];
    }
}
''')

add("3581_count_odd_letters_from_number", r'''<?php
// LeetCode 3581 - Count Odd Letters from Number
// https://leetcode.com/problems/count-odd-letters-from-number/

class Solution {
    function countOddLetters($n) {
        $d = ['zero','one','two','three','four','five','six','seven','eight','nine'];
        $mask = 0;
        while ($n > 0) {
            $word = $d[$n % 10];
            $len = strlen($word);
            for ($i = 0; $i < $len; $i++) $mask ^= 1 << (ord($word[$i]) - 97);
            $n = intdiv($n, 10);
        }
        $cnt = 0;
        while ($mask) { $cnt += $mask & 1; $mask >>= 1; }
        return $cnt;
    }
}
''')

add("3582_generate_tag_for_video_caption", r'''<?php
// LeetCode 3582 - Generate Tag for Video Caption
// https://leetcode.com/problems/generate-tag-for-video-caption/

class Solution {
    function generateTag($caption) {
        $ans = '#';
        $words = preg_split('/\s+/', trim($caption));
        $i = 0;
        foreach ($words as $word) {
            if ($word === '') continue;
            $w = strtolower($word);
            if ($i === 0) $ans .= $w;
            else {
                if (strlen($w) > 0) $w = strtoupper($w[0]) . substr($w, 1);
                $ans .= $w;
            }
            if (strlen($ans) >= 100) break;
            $i++;
        }
        if (strlen($ans) > 100) $ans = substr($ans, 0, 100);
        return $ans;
    }
}
''')

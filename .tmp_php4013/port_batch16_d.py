#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
SOLUTIONS = {}

def add(folder, body):
    SOLUTIONS[folder] = body


add("3367_maximize_sum_of_weights_after_edge_removals", r'''<?php
// LeetCode 3367 - Maximize Sum of Weights after Edge Removals
// https://leetcode.com/problems/maximize-sum-of-weights-after-edge-removals/

class Solution {
    public $g;
    public $k;

    function dfs($u, $p) {
        $base = 0;
        $gains = [];
        foreach ($this->g[$u] as $e) {
            $to = $e[0];
            $w = $e[1];
            if ($to === $p) continue;
            $child = $this->dfs($to, $u);
            $base += $child[1];
            $gain = $child[0] + $w - $child[1];
            if ($gain > 0) $gains[] = $gain;
        }
        rsort($gains);
        $withP = $base;
        $without = $base;
        for ($i = 0; $i < count($gains) && $i < $this->k - 1; $i++) $withP += $gains[$i];
        for ($i = 0; $i < count($gains) && $i < $this->k; $i++) $without += $gains[$i];
        return [$withP, $without];
    }

    function maximizeSumOfWeights($edges, $k) {
        $n = count($edges) + 1;
        $this->g = array_fill(0, $n, []);
        $this->k = $k;
        foreach ($edges as $e) {
            $this->g[$e[0]][] = [$e[1], $e[2]];
            $this->g[$e[1]][] = [$e[0], $e[2]];
        }
        return $this->dfs(0, -1)[1];
    }
}
''')

add("3369_design_an_array_statistics_tracker", r'''<?php
// LeetCode 3369 - Design an Array Statistics Tracker
// https://leetcode.com/problems/design-an-array-statistics-tracker/

class StatisticsTracker {
    public $arr;
    public $sum;
    public $freq;
    public $modeFreq;
    public $modes;

    function __construct() {
        $this->arr = [];
        $this->sum = 0;
        $this->freq = [];
        $this->modeFreq = 0;
        $this->modes = [];
    }

    function addNumber($num) {
        $this->arr[] = $num;
        $this->sum += $num;
        $f = ($this->freq[$num] ?? 0) + 1;
        $this->freq[$num] = $f;
        if ($f > $this->modeFreq) {
            $this->modeFreq = $f;
            $this->modes = [$num => true];
        } else if ($f === $this->modeFreq) {
            $this->modes[$num] = true;
        }
    }

    function removeFirstAddedNumber() {
        if (!$this->arr) return;
        $num = array_shift($this->arr);
        $this->sum -= $num;
        $f = $this->freq[$num] - 1;
        if ($f === 0) unset($this->freq[$num]);
        else $this->freq[$num] = $f;
        $this->modeFreq = 0;
        $this->modes = [];
        foreach ($this->freq as $v => $ff) {
            if ($ff > $this->modeFreq) {
                $this->modeFreq = $ff;
                $this->modes = [$v => true];
            } else if ($ff === $this->modeFreq) {
                $this->modes[$v] = true;
            }
        }
    }

    function getMean() {
        if (!$this->arr) return 0;
        return intdiv($this->sum, count($this->arr));
    }

    function getMedian() {
        $n = count($this->arr);
        $tmp = $this->arr;
        sort($tmp);
        if ($n % 2 === 1) return $tmp[intdiv($n, 2)];
        return $tmp[intdiv($n, 2) - 1];
    }

    function getMode() {
        $best = PHP_INT_MAX;
        foreach ($this->modes as $v => $_) if ($v < $best) $best = $v;
        if ($best === PHP_INT_MAX) return 0;
        return $best;
    }
}
''')

add("3370_smallest_number_with_all_set_bits", r'''<?php
// LeetCode 3370 - Smallest Number With All Set Bits
// https://leetcode.com/problems/smallest-number-with-all-set-bits/

class Solution {
    function smallestNumber($n) {
        $x = 1;
        while ($x < $n) $x = $x * 2 + 1;
        return $x;
    }
}
''')

add("3371_identify_the_largest_outlier_in_an_array", r'''<?php
// LeetCode 3371 - Identify the Largest Outlier in an Array
// https://leetcode.com/problems/identify-the-largest-outlier-in-an-array/

class Solution {
    function getLargestOutlier($nums) {
        $sum = 0;
        $freq = [];
        foreach ($nums as $x) {
            $sum += $x;
            $freq[$x] = ($freq[$x] ?? 0) + 1;
        }
        $ans = -2147483648;
        foreach ($nums as $x) {
            $freq[$x]--;
            $rem = $sum - $x;
            if ($rem % 2 === 0) {
                $cand = intdiv($rem, 2);
                if (($freq[$cand] ?? 0) > 0 && $x > $ans) $ans = $x;
            }
            $freq[$x]++;
        }
        return $ans;
    }
}
''')

add("3372_maximize_the_number_of_target_nodes_after_connecting_trees_i", r'''<?php
// LeetCode 3372 - Maximize the Number of Target Nodes After Connecting Trees I
// https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-i/

class Solution {
    function buildTree($n, $edges) {
        $g = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $g[$e[0]][] = $e[1];
            $g[$e[1]][] = $e[0];
        }
        return $g;
    }

    function countWithin($g, $start, $k) {
        if ($k < 0) return 0;
        $n = count($g);
        $vis = array_fill(0, $n, false);
        $q = [[$start, 0]];
        $vis[$start] = true;
        $cnt = 0;
        $head = 0;
        while ($head < count($q)) {
            $cur = $q[$head++];
            $u = $cur[0];
            $d = $cur[1];
            $cnt++;
            if ($d === $k) continue;
            foreach ($g[$u] as $v) {
                if (!$vis[$v]) {
                    $vis[$v] = true;
                    $q[] = [$v, $d + 1];
                }
            }
        }
        return $cnt;
    }

    function maxTargetNodes($edges1, $edges2, $k) {
        $n = count($edges1) + 1;
        $m = count($edges2) + 1;
        $g1 = $this->buildTree($n, $edges1);
        $g2 = $this->buildTree($m, $edges2);
        $cnt1 = [];
        for ($i = 0; $i < $n; $i++) $cnt1[$i] = $this->countWithin($g1, $i, $k);
        $best2 = 0;
        if ($k > 0) {
            for ($i = 0; $i < $m; $i++) {
                $c = $this->countWithin($g2, $i, $k - 1);
                if ($c > $best2) $best2 = $c;
            }
        }
        $ans = [];
        for ($i = 0; $i < $n; $i++) $ans[$i] = $cnt1[$i] + $best2;
        return $ans;
    }
}
''')

add("3373_maximize_the_number_of_target_nodes_after_connecting_trees_ii", r'''<?php
// LeetCode 3373 - Maximize the Number of Target Nodes After Connecting Trees II
// https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-ii/

class Solution {
    function buildTree($n, $edges) {
        $g = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $g[$e[0]][] = $e[1];
            $g[$e[1]][] = $e[0];
        }
        return $g;
    }

    function bipartiteCount($g, &$color) {
        $n = count($g);
        $color = array_fill(0, $n, -1);
        $q = [0];
        $color[0] = 0;
        $cnt = [1, 0];
        $head = 0;
        while ($head < count($q)) {
            $u = $q[$head++];
            foreach ($g[$u] as $v) {
                if ($color[$v] === -1) {
                    $color[$v] = $color[$u] ^ 1;
                    $cnt[$color[$v]]++;
                    $q[] = $v;
                }
            }
        }
        return $cnt;
    }

    function maxTargetNodes($edges1, $edges2) {
        $n = count($edges1) + 1;
        $m = count($edges2) + 1;
        $g1 = $this->buildTree($n, $edges1);
        $g2 = $this->buildTree($m, $edges2);
        $color1 = [];
        $color2 = [];
        $c1 = $this->bipartiteCount($g1, $color1);
        $c2 = $this->bipartiteCount($g2, $color2);
        $best2 = max($c2[0], $c2[1]);
        $ans = [];
        for ($i = 0; $i < $n; $i++) $ans[$i] = $c1[$color1[$i]] + $best2;
        return $ans;
    }
}
''')

add("3375_minimum_operations_to_make_array_values_equal_to_k", r'''<?php
// LeetCode 3375 - Minimum Operations to Make Array Values Equal to K
// https://leetcode.com/problems/minimum-operations-to-make-array-values-equal-to-k/

class Solution {
    function minOperations($nums, $k) {
        $seen = [];
        foreach ($nums as $x) {
            if ($x < $k) return -1;
            if ($x > $k) $seen[$x] = true;
        }
        return count($seen);
    }
}
''')

add("3376_minimum_time_to_break_locks_i", r'''<?php
// LeetCode 3376 - Minimum Time to Break Locks I
// https://leetcode.com/problems/minimum-time-to-break-locks-i/

class Solution {
    function bitsOnes($x) {
        $c = 0;
        while ($x > 0) { $c += $x & 1; $x >>= 1; }
        return $c;
    }

    function findMinimumTime($strength, $k) {
        $n = count($strength);
        $inf = 1000000000;
        $N = 1 << $n;
        $dp = array_fill(0, $N, $inf);
        $dp[0] = 0;
        for ($mask = 0; $mask < $N; $mask++) {
            if ($dp[$mask] === $inf) continue;
            $opened = $this->bitsOnes($mask);
            $x = 1 + $opened * $k;
            for ($i = 0; $i < $n; $i++) {
                if (($mask & (1 << $i)) !== 0) continue;
                $t = intdiv($strength[$i] + $x - 1, $x);
                $nmask = $mask | (1 << $i);
                if ($dp[$mask] + $t < $dp[$nmask]) $dp[$nmask] = $dp[$mask] + $t;
            }
        }
        return $dp[$N - 1];
    }
}
''')

add("3377_digit_operations_to_make_two_integers_equal", r'''<?php
// LeetCode 3377 - Digit Operations to Make Two Integers Equal
// https://leetcode.com/problems/digit-operations-to-make-two-integers-equal/

class Solution {
    function sieve($n) {
        $isP = array_fill(0, $n, false);
        for ($i = 2; $i < $n; $i++) $isP[$i] = true;
        for ($i = 2; $i * $i < $n; $i++) {
            if ($isP[$i]) {
                for ($j = $i * $i; $j < $n; $j += $i) $isP[$j] = false;
            }
        }
        return $isP;
    }

    function minOperations($n, $m) {
        $isPrime = $this->sieve(100000);
        if ($isPrime[$n]) return -1;
        $dist = array_fill(0, 100000, -1);
        $pq = new SplPriorityQueue();
        $pq->setExtractFlags(SplPriorityQueue::EXTR_DATA);
        $pq->insert([$n, $n], -$n);
        $dist[$n] = $n;
        while (!$pq->isEmpty()) {
            $cur = $pq->extract();
            $cost = $cur[0];
            $val = $cur[1];
            if ($cost !== $dist[$val]) continue;
            if ($val === $m) return $cost;
            $s = str_split(strval($val));
            $len = count($s);
            for ($i = 0; $i < $len; $i++) {
                $orig = $s[$i];
                foreach ([-1, 1] as $d) {
                    $nd = (ord($orig) - 48) + $d;
                    if ($nd < 0 || $nd > 9) continue;
                    if ($i === 0 && $nd === 0 && $len > 1) continue;
                    $s[$i] = strval($nd);
                    $nv = intval(implode('', $s));
                    $s[$i] = $orig;
                    if ($isPrime[$nv]) continue;
                    $nc = $cost + $nv;
                    if ($dist[$nv] === -1 || $nc < $dist[$nv]) {
                        $dist[$nv] = $nc;
                        $pq->insert([$nc, $nv], -$nc);
                    }
                }
            }
        }
        return -1;
    }
}
''')

add("3378_count_connected_components_in_lcm_graph", r'''<?php
// LeetCode 3378 - Count Connected Components in LCM Graph
// https://leetcode.com/problems/count-connected-components-in-lcm-graph/

class Solution {
    public $parent;

    function gcd($a, $b) {
        while ($b !== 0) { $t = $a % $b; $a = $b; $b = $t; }
        return $a;
    }

    function find($x) {
        if ($this->parent[$x] !== $x) $this->parent[$x] = $this->find($this->parent[$x]);
        return $this->parent[$x];
    }

    function unite($a, $b) {
        $ra = $this->find($a);
        $rb = $this->find($b);
        if ($ra !== $rb) $this->parent[$ra] = $rb;
    }

    function countComponents($nums, $threshold) {
        $n = count($nums);
        $this->parent = range(0, $n - 1);
        $idx = [];
        for ($i = 0; $i < $n; $i++) $idx[$nums[$i]] = $i;
        for ($d = 1; $d <= $threshold; $d++) {
            $first = -1;
            for ($m = $d; $m <= $threshold; $m += $d) {
                if (isset($idx[$m])) {
                    $i = $idx[$m];
                    if ($first === -1) $first = $i;
                    else if (intdiv($nums[$first] * $nums[$i], $this->gcd($nums[$first], $nums[$i])) <= $threshold)
                        $this->unite($first, $i);
                }
            }
        }
        for ($i = 0; $i < $n; $i++) {
            for ($j = $i + 1; $j < $n; $j++) {
                $a = $nums[$i];
                $b = $nums[$j];
                $g = $this->gcd($a, $b);
                if (intdiv($a, $g) * $b <= $threshold) $this->unite($i, $j);
            }
        }
        $comp = [];
        for ($i = 0; $i < $n; $i++) $comp[$this->find($i)] = true;
        return count($comp);
    }
}
''')

add("3379_transformed_array", r'''<?php
// LeetCode 3379 - Transformed Array
// https://leetcode.com/problems/transformed-array/

class Solution {
    function constructTransformedArray($nums) {
        $n = count($nums);
        $ans = [];
        for ($i = 0; $i < $n; $i++) {
            $j = (($i + $nums[$i]) % $n + $n) % $n;
            $ans[$i] = $nums[$j];
        }
        return $ans;
    }
}
''')

add("3380_maximum_area_rectangle_with_point_constraints_i", r'''<?php
// LeetCode 3380 - Maximum Area Rectangle With Point Constraints I
// https://leetcode.com/problems/maximum-area-rectangle-with-point-constraints-i/

class Solution {
    function pack($x, $y) {
        return $x . ',' . $y;
    }

    function maxRectangleArea($points) {
        $set = [];
        foreach ($points as $p) $set[$this->pack($p[0], $p[1])] = true;
        $ans = -1;
        $n = count($points);
        for ($i = 0; $i < $n; $i++) {
            for ($j = $i + 1; $j < $n; $j++) {
                $x1 = $points[$i][0];
                $y1 = $points[$i][1];
                $x2 = $points[$j][0];
                $y2 = $points[$j][1];
                if ($x1 === $x2 || $y1 === $y2) continue;
                if (!isset($set[$this->pack($x1, $y2)]) || !isset($set[$this->pack($x2, $y1)])) continue;
                $minX = min($x1, $x2);
                $maxX = max($x1, $x2);
                $minY = min($y1, $y2);
                $maxY = max($y1, $y2);
                $ok = true;
                foreach ($points as $p) {
                    $x = $p[0];
                    $y = $p[1];
                    if ($x > $minX && $x < $maxX && $y > $minY && $y < $maxY) { $ok = false; break; }
                    $onBorder = (($x === $minX || $x === $maxX) && $y >= $minY && $y <= $maxY) ||
                            (($y === $minY || $y === $maxY) && $x >= $minX && $x <= $maxX);
                    if ($onBorder) {
                        $isCorner = ($x === $minX || $x === $maxX) && ($y === $minY || $y === $maxY);
                        if (!$isCorner) { $ok = false; break; }
                    }
                }
                if ($ok) {
                    $area = ($maxX - $minX) * ($maxY - $minY);
                    if ($area > $ans) $ans = $area;
                }
            }
        }
        return $ans;
    }
}
''')

add("3381_maximum_subarray_sum_with_length_divisible_by_k", r'''<?php
// LeetCode 3381 - Maximum Subarray Sum With Length Divisible by K
// https://leetcode.com/problems/maximum-subarray-sum-with-length-divisible-by-k/

class Solution {
    function maxSubarraySum($nums, $k) {
        $n = count($nums);
        $pref = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; $i++) $pref[$i + 1] = $pref[$i] + $nums[$i];
        $INF = PHP_INT_MAX;
        $best = array_fill(0, $k, $INF);
        $best[0] = 0;
        $ans = PHP_INT_MIN;
        for ($i = 1; $i <= $n; $i++) {
            $r = $i % $k;
            if ($best[$r] !== $INF) {
                $cand = $pref[$i] - $best[$r];
                if ($cand > $ans) $ans = $cand;
            }
            if ($pref[$i] < $best[$r]) $best[$r] = $pref[$i];
        }
        return $ans;
    }
}
''')

add("3382_maximum_area_rectangle_with_point_constraints_ii", r'''<?php
// LeetCode 3382 - Maximum Area Rectangle With Point Constraints II
// https://leetcode.com/problems/maximum-area-rectangle-with-point-constraints-ii/

class Solution {
    function pack($x, $y) {
        return $x . ',' . $y;
    }

    function maxRectangleArea($xCoord, $yCoord) {
        $n = count($xCoord);
        $points = [];
        for ($i = 0; $i < $n; $i++) $points[] = [$xCoord[$i], $yCoord[$i]];
        $set = [];
        foreach ($points as $p) $set[$this->pack($p[0], $p[1])] = true;
        $ans = -1;
        for ($i = 0; $i < $n; $i++) {
            for ($j = $i + 1; $j < $n; $j++) {
                $x1 = $points[$i][0];
                $y1 = $points[$i][1];
                $x2 = $points[$j][0];
                $y2 = $points[$j][1];
                if ($x1 === $x2 || $y1 === $y2) continue;
                if (!isset($set[$this->pack($x1, $y2)]) || !isset($set[$this->pack($x2, $y1)])) continue;
                $minX = min($x1, $x2);
                $maxX = max($x1, $x2);
                $minY = min($y1, $y2);
                $maxY = max($y1, $y2);
                $ok = true;
                foreach ($points as $p) {
                    $x = $p[0];
                    $y = $p[1];
                    if ($x > $minX && $x < $maxX && $y > $minY && $y < $maxY) { $ok = false; break; }
                    $onBorder = (($x === $minX || $x === $maxX) && $y >= $minY && $y <= $maxY) ||
                            (($y === $minY || $y === $maxY) && $x >= $minX && $x <= $maxX);
                    if ($onBorder) {
                        $isCorner = ($x === $minX || $x === $maxX) && ($y === $minY || $y === $maxY);
                        if (!$isCorner) { $ok = false; break; }
                    }
                }
                if ($ok) {
                    $area = ($maxX - $minX) * ($maxY - $minY);
                    if ($area > $ans) $ans = $area;
                }
            }
        }
        return $ans;
    }
}
''')

add("3383_minimum_runes_to_add_to_cast_spell", r'''<?php
// LeetCode 3383 - Minimum Runes to Add to Cast Spell
// https://leetcode.com/problems/minimum-runes-to-add-to-cast-spell/

class Solution {
    public $g;
    public $rg;
    public $vis;
    public $order;
    public $comp;
    public $cid;

    function dfs1($u) {
        $this->vis[$u] = true;
        foreach ($this->g[$u] as $v) if (!$this->vis[$v]) $this->dfs1($v);
        $this->order[] = $u;
    }

    function dfs2($u) {
        $this->comp[$u] = $this->cid;
        foreach ($this->rg[$u] as $v) if ($this->comp[$v] === -1) $this->dfs2($v);
    }

    function minRunesToAdd($n, $crystals, $flowFrom, $flowTo) {
        $this->g = array_fill(0, $n, []);
        $this->rg = array_fill(0, $n, []);
        for ($i = 0; $i < count($flowFrom); $i++) {
            $a = $flowFrom[$i];
            $b = $flowTo[$i];
            $this->g[$a][] = $b;
            $this->rg[$b][] = $a;
        }
        $this->vis = array_fill(0, $n, false);
        $this->order = [];
        for ($i = 0; $i < $n; $i++) if (!$this->vis[$i]) $this->dfs1($i);
        $this->comp = array_fill(0, $n, -1);
        $this->cid = 0;
        for ($i = $n - 1; $i >= 0; $i--) {
            $u = $this->order[$i];
            if ($this->comp[$u] === -1) {
                $this->dfs2($u);
                $this->cid++;
            }
        }
        $hasCrystal = array_fill(0, $this->cid, false);
        foreach ($crystals as $c) $hasCrystal[$this->comp[$c]] = true;
        $indeg = array_fill(0, $this->cid, 0);
        for ($u = 0; $u < $n; $u++) {
            foreach ($this->g[$u] as $v) {
                if ($this->comp[$u] !== $this->comp[$v]) $indeg[$this->comp[$v]]++;
            }
        }
        $ans = 0;
        for ($i = 0; $i < $this->cid; $i++) {
            if ($indeg[$i] === 0 && !$hasCrystal[$i]) $ans++;
        }
        return $ans;
    }
}
''')

add("3385_minimum_time_to_break_locks_ii", r'''<?php
// LeetCode 3385 - Minimum Time to Break Locks II
// https://leetcode.com/problems/minimum-time-to-break-locks-ii/

class Solution {
    function bitsOnes($x) {
        $c = 0;
        while ($x > 0) { $c += $x & 1; $x >>= 1; }
        return $c;
    }

    function findMinimumTime($strength) {
        $n = count($strength);
        $N = 1 << $n;
        $inf = 1e18;
        $dp = array_fill(0, $N, $inf);
        $dp[0] = 0;
        $k = 1;
        for ($mask = 0; $mask < $N; $mask++) {
            if ($dp[$mask] === $inf) continue;
            $opened = $this->bitsOnes($mask);
            $x = 1 + $opened * $k;
            for ($i = 0; $i < $n; $i++) {
                if (($mask & (1 << $i)) !== 0) continue;
                $t = intdiv($strength[$i] + $x - 1, $x);
                $nmask = $mask | (1 << $i);
                if ($dp[$mask] + $t < $dp[$nmask]) $dp[$nmask] = $dp[$mask] + $t;
            }
        }
        return $dp[$N - 1];
    }
}
''')

add("3386_button_with_longest_push_time", r'''<?php
// LeetCode 3386 - Button with Longest Push Time
// https://leetcode.com/problems/button-with-longest-push-time/

class Solution {
    function buttonWithLongestTime($events) {
        $bestT = $events[0][1];
        $bestI = $events[0][0];
        $n = count($events);
        for ($i = 1; $i < $n; $i++) {
            $t = $events[$i][1] - $events[$i - 1][1];
            if ($t > $bestT || ($t === $bestT && $events[$i][0] < $bestI)) {
                $bestT = $t;
                $bestI = $events[$i][0];
            }
        }
        return $bestI;
    }
}
''')

add("3387_maximize_amount_after_two_days_of_conversions", r'''<?php
// LeetCode 3387 - Maximize Amount After Two Days of Conversions
// https://leetcode.com/problems/maximize-amount-after-two-days-of-conversions/

class Solution {
    function buildRateGraph($pairs, $rates) {
        $g = [];
        for ($i = 0; $i < count($pairs); $i++) {
            $a = $pairs[$i][0];
            $b = $pairs[$i][1];
            if (!isset($g[$a])) $g[$a] = [];
            if (!isset($g[$b])) $g[$b] = [];
            $g[$a][$b] = $rates[$i];
            $g[$b][$a] = 1.0 / $rates[$i];
        }
        return $g;
    }

    function bellman($start, $pairs, $rates) {
        $g = $this->buildRateGraph($pairs, $rates);
        $dist = [];
        $dist[$start] = 1.0;
        for ($it = 0; $it < 100; $it++) {
            $updated = false;
            foreach ($g as $from => $tos) {
                if (!isset($dist[$from]) || $dist[$from] === 0) continue;
                foreach ($tos as $to => $rate) {
                    $nv = $dist[$from] * $rate;
                    if (!isset($dist[$to]) || $nv > $dist[$to]) {
                        $dist[$to] = $nv;
                        $updated = true;
                    }
                }
            }
            if (!$updated) break;
        }
        return $dist;
    }

    function maxAmount($initialCurrency, $pairs1, $rates1, $pairs2, $rates2) {
        $amt1 = $this->bellman($initialCurrency, $pairs1, $rates1);
        $ans = 1.0;
        $g2 = $this->buildRateGraph($pairs2, $rates2);
        foreach ($amt1 as $c => $a) {
            if ($a <= 0) continue;
            $dist = [];
            $dist[$c] = $a;
            $updated = true;
            for ($it = 0; $it < 100 && $updated; $it++) {
                $updated = false;
                foreach ($g2 as $from => $tos) {
                    if (!isset($dist[$from]) || $dist[$from] === 0) continue;
                    foreach ($tos as $to => $rate) {
                        $nv = $dist[$from] * $rate;
                        if (!isset($dist[$to]) || $nv > $dist[$to]) {
                            $dist[$to] = $nv;
                            $updated = true;
                        }
                    }
                }
            }
            if (isset($dist[$initialCurrency]) && $dist[$initialCurrency] > $ans) {
                $ans = $dist[$initialCurrency];
            }
        }
        return $ans;
    }
}
''')

add("3388_count_beautiful_splits_in_an_array", r'''<?php
// LeetCode 3388 - Count Beautiful Splits in an Array
// https://leetcode.com/problems/count-beautiful-splits-in-an-array/

class Solution {
    function equal($a, $as, $ae, $b, $bs, $be) {
        if ($ae - $as !== $be - $bs) return false;
        for ($i = 0; $i < $ae - $as; $i++) if ($a[$as + $i] !== $b[$bs + $i]) return false;
        return true;
    }

    function beautifulSplits($nums) {
        $n = count($nums);
        $ans = 0;
        for ($i = 1; $i < $n - 1; $i++) {
            for ($j = $i + 1; $j < $n; $j++) {
                $ok = false;
                if ($i <= $j - $i && $this->equal($nums, 0, $i, $nums, $i, $i + $i)) $ok = true;
                if (!$ok && $j - $i <= $n - $j && $this->equal($nums, $i, $j, $nums, $j, $j + ($j - $i))) $ok = true;
                if ($ok) $ans++;
            }
        }
        return $ans;
    }
}
''')

add("3389_minimum_operations_to_make_character_frequencies_equal", r'''<?php
// LeetCode 3389 - Minimum Operations to Make Character Frequencies Equal
// https://leetcode.com/problems/minimum-operations-to-make-character-frequencies-equal/

class Solution {
    function makeStringGood($s) {
        $freq = array_fill(0, 26, 0);
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) $freq[ord($s[$i]) - 97]++;
        $ans = $n;
        for ($t = 1; $t <= $n; $t++) {
            $pool = 0;
            for ($i = 0; $i < 26; $i++) if ($freq[$i] > $t) $pool += $freq[$i] - $t;
            $deficit = 0;
            for ($i = 0; $i < 26; $i++) if ($freq[$i] < $t) $deficit += $t - $freq[$i];
            $ops = max($pool, $deficit);
            if ($ops < $ans) $ans = $ops;
        }
        if ($n < $ans) $ans = $n;
        return $ans;
    }
}
''')

add("3391_design_a_3d_binary_matrix_with_efficient_layer_tracking", r'''<?php
// LeetCode 3391 - Design a 3D Binary Matrix with Efficient Layer Tracking
// https://leetcode.com/problems/design-a-3d-binary-matrix-with-efficient-layer-tracking/

class Matrix3D {
    public $n;
    public $m;
    public $ones;

    function __construct($n) {
        $this->n = $n;
        $this->m = [];
        for ($x = 0; $x < $n; $x++) {
            $this->m[$x] = [];
            for ($y = 0; $y < $n; $y++) $this->m[$x][$y] = array_fill(0, $n, 0);
        }
        $this->ones = array_fill(0, $n, 0);
    }

    function setCell($x, $y, $z) {
        if ($this->m[$x][$y][$z] === 0) {
            $this->m[$x][$y][$z] = 1;
            $this->ones[$x]++;
        }
    }

    function unsetCell($x, $y, $z) {
        if ($this->m[$x][$y][$z] === 1) {
            $this->m[$x][$y][$z] = 0;
            $this->ones[$x]--;
        }
    }

    function largestMatrix() {
        $best = -1;
        $idx = 0;
        for ($i = 0; $i < $this->n; $i++) {
            if ($this->ones[$i] >= $best) {
                $best = $this->ones[$i];
                $idx = $i;
            }
        }
        return $idx;
    }
}
''')

add("3392_count_subarrays_of_length_three_with_a_condition", r'''<?php
// LeetCode 3392 - Count Subarrays of Length Three With a Condition
// https://leetcode.com/problems/count-subarrays-of-length-three-with-a-condition/

class Solution {
    function countSubarrays($nums) {
        $ans = 0;
        $n = count($nums);
        for ($i = 0; $i + 2 < $n; $i++) {
            if ($nums[$i] * 2 + $nums[$i + 2] * 2 === $nums[$i + 1]) $ans++;
        }
        return $ans;
    }
}
''')

add("3393_count_paths_with_the_given_xor_value", r'''<?php
// LeetCode 3393 - Count Paths With the Given XOR Value
// https://leetcode.com/problems/count-paths-with-the-given-xor-value/

class Solution {
    function countPathsWithXorValue($grid, $k) {
        $mod = 1000000007;
        $m = count($grid);
        $n = count($grid[0]);
        $dp = [];
        for ($i = 0; $i < $m; $i++) {
            $dp[$i] = [];
            for ($j = 0; $j < $n; $j++) $dp[$i][$j] = array_fill(0, 16, 0);
        }
        $dp[0][0][$grid[0][0]] = 1;
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                for ($x = 0; $x < 16; $x++) {
                    if ($dp[$i][$j][$x] === 0) continue;
                    if ($i + 1 < $m) {
                        $nx = $x ^ $grid[$i + 1][$j];
                        $dp[$i + 1][$j][$nx] = ($dp[$i + 1][$j][$nx] + $dp[$i][$j][$x]) % $mod;
                    }
                    if ($j + 1 < $n) {
                        $nx = $x ^ $grid[$i][$j + 1];
                        $dp[$i][$j + 1][$nx] = ($dp[$i][$j + 1][$nx] + $dp[$i][$j][$x]) % $mod;
                    }
                }
            }
        }
        return $dp[$m - 1][$n - 1][$k];
    }
}
''')

add("3394_check_if_grid_can_be_cut_into_sections", r'''<?php
// LeetCode 3394 - Check if Grid can be Cut into Sections
// https://leetcode.com/problems/check-if-grid-can-be-cut-into-sections/

class Solution {
    function checkCut($rects, $axis) {
        $arr = [];
        foreach ($rects as $r) $arr[] = $axis === 0 ? [$r[0], $r[2]] : [$r[1], $r[3]];
        usort($arr, function($x, $y) {
            if ($x[0] === $y[0]) return $x[1] <=> $y[1];
            return $x[0] <=> $y[0];
        });
        $cuts = 0;
        $end = $arr[0][1];
        for ($i = 1; $i < count($arr); $i++) {
            if ($arr[$i][0] >= $end) {
                $cuts++;
                $end = $arr[$i][1];
                if ($cuts >= 2) return true;
            } else if ($arr[$i][1] > $end) {
                $end = $arr[$i][1];
            }
        }
        return false;
    }

    function checkValidCuts($n, $rectangles) {
        return $this->checkCut($rectangles, 0) || $this->checkCut($rectangles, 1);
    }
}
''')

add("3395_subsequences_with_a_unique_middle_mode_i", r'''<?php
// LeetCode 3395 - Subsequences with a Unique Middle Mode I
// https://leetcode.com/problems/subsequences-with-a-unique-middle-mode-i/

class Solution {
    function uniqueMode($a) {
        $freq = [];
        foreach ($a as $x) $freq[$x] = ($freq[$x] ?? 0) + 1;
        $best = 0;
        $cnt = 0;
        foreach ($freq as $f) {
            if ($f > $best) { $best = $f; $cnt = 1; }
            else if ($f === $best) $cnt++;
        }
        return $cnt === 1;
    }

    function subsequencesWithMiddleMode($nums) {
        $mod = 1000000007;
        $n = count($nums);
        $ans = 0;
        for ($mid = 2; $mid < $n - 2; $mid++) {
            for ($a = 0; $a < $mid; $a++) {
                for ($b = $a + 1; $b < $mid; $b++) {
                    for ($c = $mid + 1; $c < $n; $c++) {
                        for ($d = $c + 1; $d < $n; $d++) {
                            if ($this->uniqueMode([$nums[$a], $nums[$b], $nums[$mid], $nums[$c], $nums[$d]])) $ans++;
                        }
                    }
                }
            }
        }
        return $ans % $mod;
    }
}
''')


written = 0
for folder, body in SOLUTIONS.items():
    path = ROOT / folder / "solution.php"
    path.write_text(body, encoding="utf-8", newline="\n")
    written += 1
print(f"wrote {written}")

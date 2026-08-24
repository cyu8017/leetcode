#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")

def w(folder, body):
    p = ROOT / folder / "solution.php"
    p.write_text(body if body.endswith("\n") else body + "\n", encoding="utf-8")
    print("wrote", folder)

w("3412_find_mirror_score_of_a_string", r'''<?php
// LeetCode 3412 - Find Mirror Score of a String
// https://leetcode.com/problems/find-mirror-score-of-a-string/

class Solution {
    function calculateScore($s) {
        $stacks = [];
        for ($i = 0; $i < 26; $i++) $stacks[$i] = [];
        $ans = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $ci = ord($s[$i]) - 97;
            $mir = 25 - $ci;
            if (count($stacks[$mir])) {
                $j = array_pop($stacks[$mir]);
                $ans += $i - $j;
            } else {
                $stacks[$ci][] = $i;
            }
        }
        return $ans;
    }
}
''')

w("3413_maximum_coins_from_k_consecutive_bags", r'''<?php
// LeetCode 3413 - Maximum Coins From K Consecutive Bags
// https://leetcode.com/problems/maximum-coins-from-k-consecutive-bags/

class Solution {
    function maximumCoins($coins, $k) {
        usort($coins, function($a, $b) { return $a[0] <=> $b[0]; });
        $ans = 0;
        $n = count($coins);
        for ($i = 0; $i < $n; $i++) {
            $sum = 0;
            $start = $coins[$i][0];
            $end = $start + $k - 1;
            for ($j = $i; $j < $n && $coins[$j][0] <= $end; $j++) {
                $l = $coins[$j][0];
                $r = $coins[$j][1];
                if ($r > $end) $r = $end;
                if ($l < $start) $l = $start;
                if ($l <= $r) $sum += ($r - $l + 1) * $coins[$j][2];
            }
            if ($sum > $ans) $ans = $sum;
        }
        for ($i = 0; $i < $n; $i++) {
            $sum = 0;
            $end = $coins[$i][1];
            $start = $end - $k + 1;
            for ($j = 0; $j <= $i; $j++) {
                $l = $coins[$j][0];
                $r = $coins[$j][1];
                if ($l < $start) $l = $start;
                if ($r > $end) $r = $end;
                if ($l <= $r) $sum += ($r - $l + 1) * $coins[$j][2];
            }
            if ($sum > $ans) $ans = $sum;
        }
        return $ans;
    }
}
''')

w("3414_maximum_score_of_non_overlapping_intervals", r'''<?php
// LeetCode 3414 - Maximum Score of Non-overlapping Intervals
// https://leetcode.com/problems/maximum-score-of-non-overlapping-intervals/

class Solution {
    private function copyState($s) {
        return ['score' => $s['score'], 'idx' => $s['idx']];
    }

    private function better($a, $b) {
        if ($a['score'] !== $b['score']) return $a['score'] > $b['score'] ? $a : $b;
        $m = min(count($a['idx']), count($b['idx']));
        for ($i = 0; $i < $m; $i++) {
            if ($a['idx'][$i] !== $b['idx'][$i]) return $a['idx'][$i] < $b['idx'][$i] ? $a : $b;
        }
        return count($a['idx']) <= count($b['idx']) ? $a : $b;
    }

    function maximumWeight($intervals) {
        $n = count($intervals);
        $arr = [];
        for ($i = 0; $i < $n; $i++) {
            $it = $intervals[$i];
            $arr[] = ['l' => $it[0], 'r' => $it[1], 'w' => $it[2], 'i' => $i];
        }
        usort($arr, function($a, $b) { return $a['r'] <=> $b['r']; });
        $empty = ['score' => 0, 'idx' => []];
        $dp = [];
        for ($i = 0; $i <= $n; $i++) {
            $dp[$i] = [];
            for ($t = 0; $t <= 4; $t++) $dp[$i][$t] = $this->copyState($empty);
        }
        for ($i = 1; $i <= $n; $i++) {
            $cur = $arr[$i - 1];
            for ($t = 0; $t <= 4; $t++) $dp[$i][$t] = $this->copyState($dp[$i - 1][$t]);
            $lo = 0;
            $hi = $i - 1;
            while ($lo < $hi) {
                $mid = intdiv($lo + $hi, 2);
                if ($arr[$mid]['r'] < $cur['l']) $lo = $mid + 1;
                else $hi = $mid;
            }
            $prev = $lo;
            for ($t = 1; $t <= 4; $t++) {
                $prevState = $dp[$prev][$t - 1];
                $cand = $this->copyState($prevState);
                $cand['score'] = $prevState['score'] + $cur['w'];
                $cand['idx'][] = $cur['i'];
                sort($cand['idx']);
                $dp[$i][$t] = $this->better($dp[$i][$t], $cand);
            }
        }
        $best = $dp[$n][0];
        for ($t = 1; $t <= 4; $t++) $best = $this->better($best, $dp[$n][$t]);
        return $best['idx'];
    }
}
''')

w("3416_subsequences_with_a_unique_middle_mode_ii", r'''<?php
// LeetCode 3416 - Subsequences with a Unique Middle Mode II
// https://leetcode.com/problems/subsequences-with-a-unique-middle-mode-ii/

class Solution {
    private function uniqueMode($a) {
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
                            if ($this->uniqueMode([$nums[$a], $nums[$b], $nums[$mid], $nums[$c], $nums[$d]]))
                                $ans = ($ans + 1) % $mod;
                        }
                    }
                }
            }
        }
        return $ans;
    }
}
''')

w("3417_zigzag_grid_traversal_with_skip", r'''<?php
// LeetCode 3417 - Zigzag Grid Traversal With Skip
// https://leetcode.com/problems/zigzag-grid-traversal-with-skip/

class Solution {
    function zigzagTraversal($grid) {
        $ans = [];
        $skip = false;
        $m = count($grid);
        for ($i = 0; $i < $m; $i++) {
            $row = $grid[$i];
            if ($i % 2 === 0) {
                foreach ($row as $v) {
                    if (!$skip) $ans[] = $v;
                    $skip = !$skip;
                }
            } else {
                for ($j = count($row) - 1; $j >= 0; $j--) {
                    if (!$skip) $ans[] = $row[$j];
                    $skip = !$skip;
                }
            }
        }
        return $ans;
    }
}
''')

w("3418_maximum_amount_of_money_robot_can_earn", r'''<?php
// LeetCode 3418 - Maximum Amount of Money Robot Can Earn
// https://leetcode.com/problems/maximum-amount-of-money-robot-can-earn/

class Solution {
    function maximumAmount($coins) {
        $m = count($coins);
        $n = count($coins[0]);
        $neg = -(1 << 30);
        $dp = [];
        for ($i = 0; $i < $m; $i++) {
            $dp[$i] = [];
            for ($j = 0; $j < $n; $j++) $dp[$i][$j] = array_fill(0, 3, $neg);
        }
        if ($coins[0][0] < 0) {
            $dp[0][0][0] = $coins[0][0];
            $dp[0][0][1] = 0;
            $dp[0][0][2] = 0;
        } else {
            $dp[0][0][0] = $coins[0][0];
            $dp[0][0][1] = $coins[0][0];
            $dp[0][0][2] = $coins[0][0];
        }
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if ($i === 0 && $j === 0) continue;
                for ($k = 0; $k < 3; $k++) {
                    $best = $neg;
                    if ($i > 0) $best = max($best, $dp[$i - 1][$j][$k]);
                    if ($j > 0) $best = max($best, $dp[$i][$j - 1][$k]);
                    if ($best === $neg) continue;
                    if ($coins[$i][$j] >= 0) $dp[$i][$j][$k] = $best + $coins[$i][$j];
                    else $dp[$i][$j][$k] = max($dp[$i][$j][$k], $best + $coins[$i][$j]);
                }
                for ($k = 1; $k < 3; $k++) {
                    $best = $neg;
                    if ($i > 0) $best = max($best, $dp[$i - 1][$j][$k - 1]);
                    if ($j > 0) $best = max($best, $dp[$i][$j - 1][$k - 1]);
                    if ($best !== $neg && $coins[$i][$j] < 0)
                        $dp[$i][$j][$k] = max($dp[$i][$j][$k], $best);
                }
            }
        }
        return max($dp[$m - 1][$n - 1][0], max($dp[$m - 1][$n - 1][1], $dp[$m - 1][$n - 1][2]));
    }
}
''')

w("3419_minimize_the_maximum_edge_weight_of_graph", r'''<?php
// LeetCode 3419 - Minimize the Maximum Edge Weight of Graph
// https://leetcode.com/problems/minimize-the-maximum-edge-weight-of-graph/

class Solution {
    function minMaxWeight($n, $edges, $threshold) {
        $ok = function($mid) use ($n, $edges) {
            $g = [];
            for ($i = 0; $i < $n; $i++) $g[$i] = [];
            foreach ($edges as $e) {
                if ($e[2] <= $mid) $g[$e[1]][] = $e[0];
            }
            $vis = array_fill(0, $n, false);
            $q = [0];
            $vis[0] = true;
            $cnt = 1;
            while (count($q)) {
                $u = array_shift($q);
                foreach ($g[$u] as $v) {
                    if (!$vis[$v]) {
                        $vis[$v] = true;
                        $cnt++;
                        $q[] = $v;
                    }
                }
            }
            return $cnt === $n;
        };
        $lo = 1;
        $hi = 1000001;
        $ans = -1;
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi, 2);
            if ($ok($mid)) {
                $ans = $mid;
                $hi = $mid;
            } else $lo = $mid + 1;
        }
        return $ans;
    }
}
''')

w("3420_count_non_decreasing_subarrays_after_k_operations", r'''<?php
// LeetCode 3420 - Count Non-Decreasing Subarrays After K Operations
// https://leetcode.com/problems/count-non-decreasing-subarrays-after-k-operations/

class Solution {
    function countNonDecreasingSubarrays($nums, $k) {
        $n = count($nums);
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            $cost = 0;
            $maxV = $nums[$i];
            for ($j = $i; $j < $n; $j++) {
                if ($nums[$j] >= $maxV) $maxV = $nums[$j];
                else $cost += $maxV - $nums[$j];
                if ($cost > $k) break;
                $ans++;
            }
        }
        return $ans;
    }
}
''')

w("3422_minimum_operations_to_make_subarray_elements_equal", r'''<?php
// LeetCode 3422 - Minimum Operations to Make Subarray Elements Equal
// https://leetcode.com/problems/minimum-operations-to-make-subarray-elements-equal/

class Solution {
    function minOperations($nums, $k) {
        $n = count($nums);
        $ans = PHP_INT_MAX;
        for ($i = 0; $i + $k <= $n; $i++) {
            $sub = array_slice($nums, $i, $k);
            sort($sub);
            $med = $sub[intdiv($k, 2)];
            $cost = 0;
            foreach ($sub as $x) $cost += abs($x - $med);
            if ($cost < $ans) $ans = $cost;
        }
        return $ans;
    }
}
''')

w("3423_maximum_difference_between_adjacent_elements_in_a_circular_array", r'''<?php
// LeetCode 3423 - Maximum Difference Between Adjacent Elements in a Circular Array
// https://leetcode.com/problems/maximum-difference-between-adjacent-elements-in-a-circular-array/

class Solution {
    function maxAdjacentDistance($nums) {
        $ans = 0;
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            $d = abs($nums[$i] - $nums[($i + 1) % $n]);
            if ($d > $ans) $ans = $d;
        }
        return $ans;
    }
}
''')

w("3424_minimum_cost_to_make_arrays_identical", r'''<?php
// LeetCode 3424 - Minimum Cost to Make Arrays Identical
// https://leetcode.com/problems/minimum-cost-to-make-arrays-identical/

class Solution {
    function minCost($arr, $brr, $k) {
        $noSwap = 0;
        for ($i = 0; $i < count($arr); $i++) $noSwap += abs($arr[$i] - $brr[$i]);
        $a2 = $arr;
        $b2 = $brr;
        sort($a2);
        sort($b2);
        $withSwap = $k;
        for ($i = 0; $i < count($a2); $i++) $withSwap += abs($a2[$i] - $b2[$i]);
        return $noSwap < $withSwap ? $noSwap : $withSwap;
    }
}
''')

w("3425_longest_special_path", r'''<?php
// LeetCode 3425 - Longest Special Path
// https://leetcode.com/problems/longest-special-path/

class Solution {
    function longestSpecialPath($edges, $nums) {
        $n = count($nums);
        $g = [];
        for ($i = 0; $i < $n; $i++) $g[$i] = [];
        foreach ($edges as $e) {
            $g[$e[0]][] = [$e[1], $e[2]];
            $g[$e[1]][] = [$e[0], $e[2]];
        }
        $bestLen = 0;
        $bestNodes = 1;
        $last = [];
        $path = [];
        $dfs = null;
        $dfs = function($u, $p, $dist, $left) use (&$dfs, &$g, &$nums, &$bestLen, &$bestNodes, &$last, &$path) {
            $seen = isset($last[$nums[$u]]);
            $prevPos = $seen ? $last[$nums[$u]] : -1;
            $last[$nums[$u]] = count($path);
            $newLeft = $left;
            if ($seen && $prevPos >= $left) $newLeft = $prevPos + 1;
            $path[] = $dist;
            $length = $dist - $path[$newLeft];
            $nodes = count($path) - $newLeft;
            if ($length > $bestLen || ($length === $bestLen && $nodes < $bestNodes)) {
                $bestLen = $length;
                $bestNodes = $nodes;
            }
            foreach ($g[$u] as $e) {
                if ($e[0] === $p) continue;
                $dfs($e[0], $u, $dist + $e[1], $newLeft);
            }
            array_pop($path);
            if ($seen) $last[$nums[$u]] = $prevPos;
            else unset($last[$nums[$u]]);
        };
        $dfs(0, -1, 0, 0);
        return [$bestLen, $bestNodes];
    }
}
''')

w("3426_manhattan_distances_of_all_arrangements_of_pieces", r'''<?php
// LeetCode 3426 - Manhattan Distances of All Arrangements of Pieces
// https://leetcode.com/problems/manhattan-distances-of-all-arrangements-of-pieces/

class Solution {
    private $mod = 1000000007;

    private function modPow($a, $e) {
        $r = 1;
        $base = $a % $this->mod;
        $mod = $this->mod;
        while ($e > 0) {
            if ($e & 1) $r = ($r * $base) % $mod;
            $base = ($base * $base) % $mod;
            $e >>= 1;
        }
        return $r;
    }

    private function comb($nn, $kk) {
        if ($kk < 0 || $kk > $nn) return 0;
        $num = 1;
        $den = 1;
        $mod = $this->mod;
        for ($i = 0; $i < $kk; $i++) {
            $num = ($num * ($nn - $i)) % $mod;
            $den = ($den * ($i + 1)) % $mod;
        }
        return ($num * $this->modPow($den, $mod - 2)) % $mod;
    }

    function distanceSum($m, $n, $k) {
        $mod = $this->mod;
        if ($k < 2) return 0;
        $totalCells = $m * $n;
        $pairChoose = $this->comb($totalCells - 2, $k - 2);
        $sumDist = 0;
        for ($d = 1; $d < $m; $d++) $sumDist += $d * ($m - $d) * $n * $n;
        for ($d = 1; $d < $n; $d++) $sumDist += $d * ($n - $d) * $m * $m;
        return ($sumDist % $mod) * $pairChoose % $mod;
    }
}
''')

w("3427_sum_of_variable_length_subarrays", r'''<?php
// LeetCode 3427 - Sum of Variable Length Subarrays
// https://leetcode.com/problems/sum-of-variable-length-subarrays/

class Solution {
    function subarraySum($nums) {
        $n = count($nums);
        $pref = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; $i++) $pref[$i + 1] = $pref[$i] + $nums[$i];
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            $start = $i - $nums[$i];
            if ($start < 0) $start = 0;
            $ans += $pref[$i + 1] - $pref[$start];
        }
        return $ans;
    }
}
''')

w("3428_maximum_and_minimum_sums_of_at_most_size_k_subsequences", r'''<?php
// LeetCode 3428 - Maximum and Minimum Sums of at Most Size K Subsequences
// https://leetcode.com/problems/maximum-and-minimum-sums-of-at-most-size-k-subsequences/

class Solution {
    function minMaxSums($nums, $k) {
        $mod = 1000000007;
        sort($nums);
        $n = count($nums);
        $C = [];
        for ($i = 0; $i <= $n; $i++) $C[$i] = array_fill(0, $k, 0);
        for ($i = 0; $i <= $n; $i++) {
            $C[$i][0] = 1;
            for ($j = 1; $j < $k && $j <= $i; $j++) $C[$i][$j] = ($C[$i - 1][$j] + $C[$i - 1][$j - 1]) % $mod;
        }
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            $waysMax = 0;
            for ($j = 0; $j < $k && $j <= $i; $j++) $waysMax = ($waysMax + $C[$i][$j]) % $mod;
            $waysMin = 0;
            $right = $n - $i - 1;
            for ($j = 0; $j < $k && $j <= $right; $j++) $waysMin = ($waysMin + $C[$right][$j]) % $mod;
            $ans = ($ans + $nums[$i] * $waysMax % $mod + $nums[$i] * $waysMin % $mod) % $mod;
        }
        return $ans;
    }
}
''')

print("batch b done")

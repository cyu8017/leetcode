#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
SOLUTIONS = {}

def add(folder, body):
    SOLUTIONS[folder] = body


add("3531_count_covered_buildings", r'''<?php
// LeetCode 3531 - Count Covered Buildings
// https://leetcode.com/problems/count-covered-buildings/

class Solution {
    function countCoveredBuildings($n, $buildings) {
        $g1 = [];
        $g2 = [];
        foreach ($buildings as $b) {
            if (!isset($g1[$b[0]])) $g1[$b[0]] = [];
            if (!isset($g2[$b[1]])) $g2[$b[1]] = [];
            $g1[$b[0]][] = $b[1];
            $g2[$b[1]][] = $b[0];
        }
        foreach ($g1 as &$list) sort($list);
        unset($list);
        foreach ($g2 as &$list) sort($list);
        unset($list);
        $ans = 0;
        foreach ($buildings as $b) {
            $x = $b[0];
            $y = $b[1];
            $l1 = $g1[$x];
            $l2 = $g2[$y];
            if ($l2[0] < $x && $x < $l2[count($l2) - 1] && $l1[0] < $y && $y < $l1[count($l1) - 1]) $ans++;
        }
        return $ans;
    }
}
''')

add("3532_path_existence_queries_in_a_graph_i", r'''<?php
// LeetCode 3532 - Path Existence Queries in a Graph I
// https://leetcode.com/problems/path-existence-queries-in-a-graph-i/

class Solution {
    function pathExistenceQueries($n, $nums, $maxDiff, $queries) {
        $g = array_fill(0, $n, 0);
        $cnt = 0;
        for ($i = 1; $i < $n; $i++) {
            if ($nums[$i] - $nums[$i - 1] > $maxDiff) $cnt++;
            $g[$i] = $cnt;
        }
        $ans = array_fill(0, count($queries), false);
        for ($i = 0; $i < count($queries); $i++)
            $ans[$i] = $g[$queries[$i][0]] === $g[$queries[$i][1]];
        return $ans;
    }
}
''')

add("3533_concatenated_divisibility", r'''<?php
// LeetCode 3533 - Concatenated Divisibility
// https://leetcode.com/problems/concatenated-divisibility/

class Solution {
    private $nums;
    private $k;
    private $n;
    private $pows;
    private $memo;

    private function dp($mask, $mod) {
        if ($mask === (1 << $this->n) - 1) return $mod === 0;
        $key = $mask . ',' . $mod;
        if (isset($this->memo[$key])) return $this->memo[$key];
        for ($i = 0; $i < $this->n; $i++) {
            if ((($mask >> $i) & 1) === 0) {
                $nm = ($mod * $this->pows[$i] + $this->nums[$i]) % $this->k;
                if ($this->dp($mask | (1 << $i), $nm)) {
                    return $this->memo[$key] = true;
                }
            }
        }
        return $this->memo[$key] = false;
    }

    private function reconstruct($mask, $mod) {
        for ($i = 0; $i < $this->n; $i++) {
            if ((($mask >> $i) & 1) === 0) {
                $nm = ($mod * $this->pows[$i] + $this->nums[$i]) % $this->k;
                if ($this->dp($mask | (1 << $i), $nm)) {
                    $rest = $this->reconstruct($mask | (1 << $i), $nm);
                    array_unshift($rest, $this->nums[$i]);
                    return $rest;
                }
            }
        }
        return [];
    }

    function concatenatedDivisibility($nums, $k) {
        sort($nums);
        $this->nums = array_values($nums);
        $this->k = $k;
        $this->n = count($this->nums);
        $this->pows = array_fill(0, $this->n, 0);
        for ($i = 0; $i < $this->n; $i++) {
            $p = 1;
            $num = $this->nums[$i];
            if ($num === 0) $p = 10 % $k;
            else {
                for ($x = $num; $x > 0; $x = intdiv($x, 10)) $p = $p * 10 % $k;
            }
            $this->pows[$i] = $p;
        }
        $this->memo = [];
        if (!$this->dp(0, 0)) return [];
        return $this->reconstruct(0, 0);
    }
}
''')

add("3534_path_existence_queries_in_a_graph_ii", r'''<?php
// LeetCode 3534 - Path Existence Queries in a Graph II
// https://leetcode.com/problems/path-existence-queries-in-a-graph-ii/

class Solution {
    function pathExistenceQueries($n, $nums, $maxDiff, $queries) {
        $pairs = [];
        for ($i = 0; $i < $n; $i++) $pairs[] = [$nums[$i], $i];
        usort($pairs, function($a, $b) { return $a[0] <=> $b[0]; });
        $m = 20;
        $f = [];
        for ($i = 0; $i < $n; $i++) $f[$i] = array_fill(0, $m, 0);
        $r = $n - 1;
        for ($l = $n - 1; $l >= 0; $l--) {
            while ($pairs[$r][0] - $pairs[$l][0] > $maxDiff) $r--;
            $i = $pairs[$l][1];
            $j = $pairs[$r][1];
            $f[$i][0] = $j;
            for ($k = 1; $k < $m; $k++) $f[$i][$k] = $f[$f[$i][$k - 1]][$k - 1];
        }
        $ans = [];
        foreach ($queries as $q) {
            $i = $q[0];
            $j = $q[1];
            if ($nums[$i] > $nums[$j]) { $tmp = $i; $i = $j; $j = $tmp; }
            if ($i === $j) { $ans[] = 0; continue; }
            if ($nums[$i] === $nums[$j]) { $ans[] = 1; continue; }
            $d = 0;
            for ($k = $m - 1; $k >= 0; $k--) {
                if ($nums[$f[$i][$k]] < $nums[$j]) {
                    $d |= 1 << $k;
                    $i = $f[$i][$k];
                }
            }
            if ($nums[$f[$i][0]] < $nums[$j]) $ans[] = -1;
            else $ans[] = $d + 1;
        }
        return $ans;
    }
}
''')

add("3535_unit_conversion_ii", r'''<?php
// LeetCode 3535 - Unit Conversion II
// https://leetcode.com/problems/unit-conversion-ii/

class Solution {
    private $MOD = 1000000007;
    private $g;
    private $res;

    private function qpow($x, $n) {
        $res = 1;
        $mod = $this->MOD;
        $x %= $mod;
        while ($n > 0) {
            if ($n & 1) $res = (int)(($res * $x) % $mod);
            $x = (int)(($x * $x) % $mod);
            $n >>= 1;
        }
        return $res;
    }

    private function dfs($s, $mul) {
        $this->res[$s] = $mul;
        foreach ($this->g[$s] as $e)
            $this->dfs($e[0], (int)(($mul * $e[1]) % $this->MOD));
    }

    function queryConversions($conversions, $queries) {
        $n = count($conversions) + 1;
        $this->g = array_fill(0, $n, []);
        foreach ($conversions as $e) $this->g[$e[0]][] = [$e[1], $e[2]];
        $this->res = array_fill(0, $n, 0);
        $this->dfs(0, 1);
        $ans = array_fill(0, count($queries), 0);
        for ($i = 0; $i < count($queries); $i++)
            $ans[$i] = (int)(($this->res[$queries[$i][1]] * $this->qpow($this->res[$queries[$i][0]], $this->MOD - 2)) % $this->MOD);
        return $ans;
    }
}
''')

add("3536_maximum_product_of_two_digits", r'''<?php
// LeetCode 3536 - Maximum Product of Two Digits
// https://leetcode.com/problems/maximum-product-of-two-digits/

class Solution {
    function maxProduct($n) {
        $a = 0;
        $b = 0;
        for (; $n > 0; $n = intdiv($n, 10)) {
            $x = $n % 10;
            if ($a < $x) { $b = $a; $a = $x; }
            else if ($b < $x) $b = $x;
        }
        return $a * $b;
    }
}
''')

add("3537_fill_a_special_grid", r'''<?php
// LeetCode 3537 - Fill a Special Grid
// https://leetcode.com/problems/fill-a-special-grid/

class Solution {
    private $ans;
    private $val;

    private function dfs($x, $y, $k) {
        if ($k === 1) {
            $this->ans[$x][$y] = $this->val++;
            return;
        }
        $h = $k >> 1;
        $this->dfs($x, $y, $h);
        $this->dfs($x + $h, $y, $h);
        $this->dfs($x + $h, $y - $h, $h);
        $this->dfs($x, $y - $h, $h);
    }

    function specialGrid($n) {
        $m = 1 << $n;
        $this->ans = [];
        for ($i = 0; $i < $m; $i++) $this->ans[$i] = array_fill(0, $m, 0);
        $this->val = 0;
        $this->dfs(0, $m - 1, $m);
        return $this->ans;
    }
}
''')

add("3538_merge_operations_for_minimum_travel_time", r'''<?php
// LeetCode 3538 - Merge Operations for Minimum Travel Time
// https://leetcode.com/problems/merge-operations-for-minimum-travel-time/

class Solution {
    private $n;
    private $prefix;
    private $position;
    private $memo;
    private $INF = 1e18;

    private function dp($i, $skips, $last) {
        if ($i === $this->n - 1) return $skips === 0 ? 0 : $this->INF;
        $key = $i . ',' . $skips . ',' . $last;
        if (isset($this->memo[$key])) return $this->memo[$key];
        $rate = $this->prefix[$i];
        if ($last > 0) $rate -= $this->prefix[$last - 1];
        $res = $this->INF;
        $end = $this->n - 1;
        if ($i + $skips + 1 < $end) $end = $i + $skips + 1;
        for ($j = $i + 1; $j <= $end; $j++) {
            $cand = ($this->position[$j] - $this->position[$i]) * $rate + $this->dp($j, $skips - ($j - $i - 1), $i + 1);
            if ($cand < $res) $res = $cand;
        }
        return $this->memo[$key] = $res;
    }

    function minTravelTime($l, $n, $k, $position, $time) {
        $this->n = $n;
        $this->position = $position;
        $this->prefix = array_fill(0, $n, 0);
        $this->prefix[0] = $time[0];
        for ($i = 1; $i < $n; $i++) $this->prefix[$i] = $this->prefix[$i - 1] + $time[$i];
        $this->memo = [];
        return $this->dp(0, $k, 0);
    }
}
''')

add("3539_find_sum_of_array_product_of_magical_sequences", r'''<?php
// LeetCode 3539 - Find Sum of Array Product of Magical Sequences
// https://leetcode.com/problems/find-sum-of-array-product-of-magical-sequences/

class Solution {
    private $N = 31;
    private $MOD = 1000000007;
    private $f;
    private $g;
    private $nums;
    private $n;
    private $dp;

    private function qpow($a, $kk) {
        $res = 1;
        $mod = $this->MOD;
        $a %= $mod;
        while ($kk > 0) {
            if ($kk & 1) $res = (int)(($res * $a) % $mod);
            $a = (int)(($a * $a) % $mod);
            $kk >>= 1;
        }
        return $res;
    }

    private function initFact() {
        $this->f = array_fill(0, $this->N, 0);
        $this->g = array_fill(0, $this->N, 0);
        $this->f[0] = $this->g[0] = 1;
        for ($i = 1; $i < $this->N; $i++) {
            $this->f[$i] = (int)(($this->f[$i - 1] * $i) % $this->MOD);
            $this->g[$i] = $this->qpow($this->f[$i], $this->MOD - 2);
        }
    }

    private function comb($mm, $nn) {
        if ($nn < 0 || $nn > $mm) return 0;
        return (int)(($this->f[$mm] * $this->g[$nn] % $this->MOD) * $this->g[$mm - $nn] % $this->MOD);
    }

    private function dfs($i, $j, $kk, $st) {
        if ($kk < 0 || ($i === $this->n && $j > 0)) return 0;
        if ($i === $this->n) {
            while ($st > 0) { $kk -= $st & 1; $st >>= 1; }
            return $kk === 0 ? 1 : 0;
        }
        if ($this->dp[$i][$j][$kk][$st] !== -1) return $this->dp[$i][$j][$kk][$st];
        $res = 0;
        for ($t = 0; $t <= $j; $t++) {
            $nt = $t + $st;
            $nk = $kk - ($nt & 1);
            $p = $this->qpow($this->nums[$i], $t);
            $tmp = (int)(($this->comb($j, $t) * $p % $this->MOD) * $this->dfs($i + 1, $j - $t, $nk, $nt >> 1) % $this->MOD);
            $res = ($res + $tmp) % $this->MOD;
        }
        return $this->dp[$i][$j][$kk][$st] = $res;
    }

    function magicalSum($m, $k, $nums) {
        $this->initFact();
        $this->nums = $nums;
        $this->n = count($nums);
        $this->dp = [];
        for ($i = 0; $i <= $this->n; $i++) {
            $this->dp[$i] = [];
            for ($j = 0; $j <= $m; $j++) {
                $this->dp[$i][$j] = [];
                for ($kk = 0; $kk <= $k; $kk++)
                    $this->dp[$i][$j][$kk] = array_fill(0, $this->N, -1);
            }
        }
        return $this->dfs(0, $m, $k, 0);
    }
}
''')

add("3540_minimum_time_to_visit_all_houses", r'''<?php
// LeetCode 3540 - Minimum Time to Visit All Houses
// https://leetcode.com/problems/minimum-time-to-visit-all-houses/

class Solution {
    function minTotalTime($forward, $backward, $queries) {
        $n = count($forward);
        $sumB = 0;
        foreach ($backward as $v) $sumB += $v;
        $pf = array_fill(0, $n + 1, 0);
        $pb = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; $i++) {
            $pf[$i + 1] = $pf[$i] + $forward[$i];
            $pb[$i + 1] = $pb[$i] + $backward[$i];
        }
        $ans = 0;
        $pos = 0;
        foreach ($queries as $q) {
            $r = 0;
            if ($q < $pos) $r = $pf[$n];
            $r += $pf[$q] - $pf[$pos];
            $l = 0;
            if ($q > $pos) $l = $sumB;
            $l += $pb[$pos] - $pb[$q];
            $ans += min($l, $r);
            $pos = $q;
        }
        return $ans;
    }
}
''')

add("3541_find_most_frequent_vowel_and_consonant", r'''<?php
// LeetCode 3541 - Find Most Frequent Vowel and Consonant
// https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/

class Solution {
    function maxFreqSum($s) {
        $cnt = array_fill(0, 26, 0);
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) $cnt[ord($s[$i]) - 97]++;
        $a = 0;
        $b = 0;
        $vowels = ['a' => 1, 'e' => 1, 'i' => 1, 'o' => 1, 'u' => 1];
        for ($i = 0; $i < 26; $i++) {
            $c = chr(97 + $i);
            if (isset($vowels[$c])) $a = max($a, $cnt[$i]);
            else $b = max($b, $cnt[$i]);
        }
        return $a + $b;
    }
}
''')

add("3542_minimum_operations_to_convert_all_elements_to_zero", r'''<?php
// LeetCode 3542 - Minimum Operations to Convert All Elements to Zero
// https://leetcode.com/problems/minimum-operations-to-convert-all-elements-to-zero/

class Solution {
    function minOperations($nums) {
        $stk = [];
        $ans = 0;
        foreach ($nums as $x) {
            while (count($stk) > 0 && $stk[count($stk) - 1] > $x) {
                $ans++;
                array_pop($stk);
            }
            if ($x !== 0 && (count($stk) === 0 || $stk[count($stk) - 1] !== $x)) $stk[] = $x;
        }
        $ans += count($stk);
        return $ans;
    }
}
''')

add("3543_maximum_weighted_k_edge_path", r'''<?php
// LeetCode 3543 - Maximum Weighted K-Edge Path
// https://leetcode.com/problems/maximum-weighted-k-edge-path/

class Solution {
    function maxWeight($n, $edges, $k, $t) {
        $graph = array_fill(0, $n, []);
        foreach ($edges as $e) $graph[$e[0]][] = [$e[1], $e[2]];
        $dp = [];
        for ($u = 0; $u < $n; $u++) {
            $dp[$u] = [];
            for ($i = 0; $i <= $k; $i++) $dp[$u][$i] = [];
            $dp[$u][0][0] = true;
        }
        for ($i = 0; $i < $k; $i++) {
            for ($u = 0; $u < $n; $u++) {
                foreach ($dp[$u][$i] as $sum => $_) {
                    foreach ($graph[$u] as $e) {
                        $ns = $sum + $e[1];
                        if ($ns < $t) $dp[$e[0]][$i + 1][$ns] = true;
                    }
                }
            }
        }
        $ans = -1;
        for ($u = 0; $u < $n; $u++)
            foreach ($dp[$u][$k] as $sum => $_) if ($sum > $ans) $ans = $sum;
        return $ans;
    }
}
''')

add("3544_subtree_inversion_sum", r'''<?php
// LeetCode 3544 - Subtree Inversion Sum
// https://leetcode.com/problems/subtree-inversion-sum/

class Solution {
    private $graph;
    private $parent;
    private $nums;
    private $k;
    private $memo;

    private function dp($u, $steps, $inv) {
        $key = $u . ',' . $steps . ',' . ($inv ? 1 : 0);
        if (isset($this->memo[$key])) return $this->memo[$key];
        $num = $this->nums[$u];
        if ($inv) $num = -$num;
        $negNum = -$num;
        foreach ($this->graph[$u] as $v) {
            if ($v === $this->parent[$u]) continue;
            $this->parent[$v] = $u;
            $ns = $steps + 1;
            if ($ns > $this->k) $ns = $this->k;
            $num += $this->dp($v, $ns, $inv);
            if ($steps === $this->k) $negNum += $this->dp($v, 1, !$inv);
        }
        $res = $num;
        if ($steps === $this->k && $negNum > $res) $res = $negNum;
        return $this->memo[$key] = $res;
    }

    function subtreeInversionSum($edges, $nums, $k) {
        $n = count($edges) + 1;
        $this->graph = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $this->graph[$e[0]][] = $e[1];
            $this->graph[$e[1]][] = $e[0];
        }
        $this->parent = array_fill(0, $n, -1);
        $this->nums = $nums;
        $this->k = $k;
        $this->memo = [];
        return $this->dp(0, $k, false);
    }
}
''')

add("3545_minimum_deletions_for_at_most_k_distinct_characters", r'''<?php
// LeetCode 3545 - Minimum Deletions for At Most K Distinct Characters
// https://leetcode.com/problems/minimum-deletions-for-at-most-k-distinct-characters/

class Solution {
    function minDeletion($s, $k) {
        $cnt = array_fill(0, 26, 0);
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) $cnt[ord($s[$i]) - 97]++;
        sort($cnt);
        $ans = 0;
        for ($i = 0; $i + $k < 26; $i++) $ans += $cnt[$i];
        return $ans;
    }
}
''')

add("3546_equal_sum_grid_partition_i", r'''<?php
// LeetCode 3546 - Equal Sum Grid Partition I
// https://leetcode.com/problems/equal-sum-grid-partition-i/

class Solution {
    function canPartitionGrid($grid) {
        $s = 0;
        foreach ($grid as $row) foreach ($row as $x) $s += $x;
        if ($s % 2 !== 0) return false;
        $m = count($grid);
        $n = count($grid[0]);
        $pre = 0;
        for ($i = 0; $i < $m; $i++) {
            foreach ($grid[$i] as $x) $pre += $x;
            if ($pre * 2 === $s && $i + 1 < $m) return true;
        }
        $pre = 0;
        for ($j = 0; $j < $n; $j++) {
            for ($i = 0; $i < $m; $i++) $pre += $grid[$i][$j];
            if ($pre * 2 === $s && $j + 1 < $n) return true;
        }
        return false;
    }
}
''')

add("3547_maximum_sum_of_edge_values_in_a_graph", r'''<?php
// LeetCode 3547 - Maximum Sum of Edge Values in a Graph
// https://leetcode.com/problems/maximum-sum-of-edge-values-in-a-graph/

class Solution {
    private function calc($left, $right, $isCycle) {
        $w0 = $right;
        $w1 = $right;
        $score = 0;
        for ($value = $right - 1; $value >= $left; $value--) {
            $score += $w0 * $value;
            $w0 = $w1;
            $w1 = $value;
        }
        if ($isCycle) $score += $w0 * $w1;
        return $score;
    }

    private function getComp($start, $graph, &$seen) {
        $comp = [$start];
        $seen[$start] = true;
        for ($i = 0; $i < count($comp); $i++) {
            foreach ($graph[$comp[$i]] as $v) {
                if (!$seen[$v]) { $seen[$v] = true; $comp[] = $v; }
            }
        }
        return $comp;
    }

    function maxScore($n, $edges) {
        $graph = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $graph[$e[0]][] = $e[1];
            $graph[$e[1]][] = $e[0];
        }
        $seen = array_fill(0, $n, false);
        $cycleSizes = [];
        $pathSizes = [];
        for ($i = 0; $i < $n; $i++) {
            if ($seen[$i]) continue;
            $comp = $this->getComp($i, $graph, $seen);
            $allDeg2 = true;
            foreach ($comp as $u) if (count($graph[$u]) !== 2) { $allDeg2 = false; break; }
            if ($allDeg2) $cycleSizes[] = count($comp);
            else if (count($comp) > 1) $pathSizes[] = count($comp);
        }
        $ans = 0;
        $curN = $n;
        foreach ($cycleSizes as $cs) {
            $ans += $this->calc($curN - $cs + 1, $curN, true);
            $curN -= $cs;
        }
        rsort($pathSizes);
        foreach ($pathSizes as $ps) {
            $ans += $this->calc($curN - $ps + 1, $curN, false);
            $curN -= $ps;
        }
        return $ans;
    }
}
''')

add("3548_equal_sum_grid_partition_ii", r'''<?php
// LeetCode 3548 - Equal Sum Grid Partition II
// https://leetcode.com/problems/equal-sum-grid-partition-ii/

class Solution {
    private function rotate($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        $t = [];
        for ($j = 0; $j < $n; $j++) $t[$j] = array_fill(0, $m, 0);
        for ($i = 0; $i < $m; $i++) for ($j = 0; $j < $n; $j++) $t[$j][$i] = $grid[$i][$j];
        return $t;
    }

    private function check($g) {
        $m = count($g);
        $n = count($g[0]);
        $s1 = 0;
        $s2 = 0;
        $cnt1 = [];
        $cnt2 = [];
        foreach ($g as $row) foreach ($row as $x) {
            $s2 += $x;
            $cnt2[$x] = ($cnt2[$x] ?? 0) + 1;
        }
        for ($i = 0; $i < $m - 1; $i++) {
            foreach ($g[$i] as $x) {
                $s1 += $x;
                $s2 -= $x;
                $cnt1[$x] = ($cnt1[$x] ?? 0) + 1;
                $cnt2[$x] = $cnt2[$x] - 1;
            }
            if ($s1 === $s2) return true;
            if ($s1 < $s2) {
                $diff = $s2 - $s1;
                if (($cnt2[$diff] ?? 0) > 0) {
                    if (($m - $i - 1 > 1 && $n > 1) ||
                        ($i === $m - 2 && ($g[$i + 1][0] === $diff || $g[$i + 1][$n - 1] === $diff)) ||
                        ($n === 1 && ($g[$i + 1][0] === $diff || $g[$m - 1][0] === $diff)))
                        return true;
                }
            } else {
                $diff = $s1 - $s2;
                if (($cnt1[$diff] ?? 0) > 0) {
                    if (($i + 1 > 1 && $n > 1) ||
                        ($i === 0 && ($g[0][0] === $diff || $g[0][$n - 1] === $diff)) ||
                        ($n === 1 && ($g[0][0] === $diff || $g[$i][0] === $diff)))
                        return true;
                }
            }
        }
        return false;
    }

    function canPartitionGrid($grid) {
        return $this->check($grid) || $this->check($this->rotate($grid));
    }
}
''')

add("3549_multiply_two_polynomials", r'''<?php
// LeetCode 3549 - Multiply Two Polynomials
// https://leetcode.com/problems/multiply-two-polynomials/

class Solution {
    function multiply($poly1, $poly2) {
        $n1 = count($poly1);
        $n2 = count($poly2);
        if ($n1 === 0 || $n2 === 0) return [];
        $m = $n1 + $n2 - 1;
        $res = array_fill(0, $m, 0);
        for ($i = 0; $i < $n1; $i++)
            for ($j = 0; $j < $n2; $j++)
                $res[$i + $j] += $poly1[$i] * $poly2[$j];
        return $res;
    }
}
''')

add("3550_smallest_index_with_digit_sum_equal_to_index", r'''<?php
// LeetCode 3550 - Smallest Index With Digit Sum Equal to Index
// https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index/

class Solution {
    function smallestIndex($nums) {
        for ($i = 0; $i < count($nums); $i++) {
            $x = $nums[$i];
            $s = 0;
            for (; $x > 0; $x = intdiv($x, 10)) $s += $x % 10;
            if ($s === $i) return $i;
        }
        return -1;
    }
}
''')

add("3551_minimum_swaps_to_sort_by_digit_sum", r'''<?php
// LeetCode 3551 - Minimum Swaps to Sort by Digit Sum
// https://leetcode.com/problems/minimum-swaps-to-sort-by-digit-sum/

class Solution {
    private function f($x) {
        $s = 0;
        while ($x !== 0) { $s += $x % 10; $x = intdiv($x, 10); }
        return $s;
    }

    function minSwaps($nums) {
        $n = count($nums);
        $arr = [];
        for ($i = 0; $i < $n; $i++) $arr[] = [$this->f($nums[$i]), $nums[$i]];
        usort($arr, function($a, $b) {
            if ($a[0] !== $b[0]) return $a[0] <=> $b[0];
            return $a[1] <=> $b[1];
        });
        $d = [];
        for ($i = 0; $i < $n; $i++) $d[$arr[$i][1]] = $i;
        $vis = array_fill(0, $n, false);
        $ans = $n;
        for ($i = 0; $i < $n; $i++) {
            if (!$vis[$i]) {
                $ans--;
                $j = $i;
                while (!$vis[$j]) {
                    $vis[$j] = true;
                    $j = $d[$nums[$j]];
                }
            }
        }
        return $ans;
    }
}
''')

add("3552_grid_teleportation_traversal", r'''<?php
// LeetCode 3552 - Grid Teleportation Traversal
// https://leetcode.com/problems/grid-teleportation-traversal/

class Solution {
    function minMoves($matrix) {
        $m = count($matrix);
        $n = strlen($matrix[0]);
        $g = [];
        for ($i = 0; $i < $m; $i++)
            for ($j = 0; $j < $n; $j++) {
                $c = $matrix[$i][$j];
                if (($c >= 'A' && $c <= 'Z') || ($c >= 'a' && $c <= 'z')) {
                    if (!isset($g[$c])) $g[$c] = [];
                    $g[$c][] = [$i, $j];
                }
            }
        $dirs = [-1, 0, 1, 0, -1];
        $INF = 1 << 30;
        $dist = [];
        for ($i = 0; $i < $m; $i++) $dist[$i] = array_fill(0, $n, $INF);
        $dist[0][0] = 0;
        $q = [[0, 0]];
        while (count($q)) {
            $cur = array_shift($q);
            $i = $cur[0];
            $j = $cur[1];
            $d = $dist[$i][$j];
            if ($i === $m - 1 && $j === $n - 1) return $d;
            $c = $matrix[$i][$j];
            if (isset($g[$c])) {
                foreach ($g[$c] as $p) {
                    $x = $p[0];
                    $y = $p[1];
                    if ($d < $dist[$x][$y]) {
                        $dist[$x][$y] = $d;
                        array_unshift($q, [$x, $y]);
                    }
                }
                unset($g[$c]);
            }
            for ($idx = 0; $idx < 4; $idx++) {
                $x = $i + $dirs[$idx];
                $y = $j + $dirs[$idx + 1];
                if (0 <= $x && $x < $m && 0 <= $y && $y < $n && $matrix[$x][$y] !== '#' && $d + 1 < $dist[$x][$y]) {
                    $dist[$x][$y] = $d + 1;
                    $q[] = [$x, $y];
                }
            }
        }
        return -1;
    }
}
''')

add("3553_minimum_weighted_subgraph_with_the_required_paths_ii", r'''<?php
// LeetCode 3553 - Minimum Weighted Subgraph With the Required Paths II
// https://leetcode.com/problems/minimum-weighted-subgraph-with-the-required-paths-ii/

class Solution {
    private $LOG = 17;
    private $g;
    private $parent;
    private $depth;
    private $dist;

    private function dfs($u, $p) {
        $this->parent[0][$u] = $p;
        foreach ($this->g[$u] as $e) {
            $to = $e[0];
            $w = $e[1];
            if ($to === $p) continue;
            $this->depth[$to] = $this->depth[$u] + 1;
            $this->dist[$to] = $this->dist[$u] + $w;
            $this->dfs($to, $u);
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

    private function path($u, $v) {
        $a = $this->lca($u, $v);
        return $this->dist[$u] + $this->dist[$v] - 2 * $this->dist[$a];
    }

    function minimumWeight($edges, $queries) {
        $n = count($edges) + 1;
        $this->g = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $this->g[$e[0]][] = [$e[1], $e[2]];
            $this->g[$e[1]][] = [$e[0], $e[2]];
        }
        $this->parent = [];
        for ($k = 0; $k < $this->LOG; $k++) $this->parent[$k] = array_fill(0, $n, -1);
        $this->depth = array_fill(0, $n, 0);
        $this->dist = array_fill(0, $n, 0);
        $this->dfs(0, -1);
        for ($k = 1; $k < $this->LOG; $k++)
            for ($v = 0; $v < $n; $v++)
                if ($this->parent[$k - 1][$v] !== -1) $this->parent[$k][$v] = $this->parent[$k - 1][$this->parent[$k - 1][$v]];
        $ans = array_fill(0, count($queries), 0);
        for ($i = 0; $i < count($queries); $i++) {
            $a = $queries[$i][0];
            $b = $queries[$i][1];
            $c = $queries[$i][2];
            $ans[$i] = intdiv($this->path($a, $b) + $this->path($b, $c) + $this->path($a, $c), 2);
        }
        return $ans;
    }
}
''')

add("3555_smallest_subarray_to_sort_in_every_sliding_window", r'''<?php
// LeetCode 3555 - Smallest Subarray to Sort in Every Sliding Window
// https://leetcode.com/problems/smallest-subarray-to-sort-in-every-sliding-window/

class Solution {
    private function f($nums, $i, $j, $inf) {
        $mi = $inf;
        $mx = -$inf;
        $l = -1;
        $r = -1;
        for ($p = $i; $p <= $j; $p++) {
            if ($nums[$p] < $mx) $r = $p;
            else $mx = $nums[$p];
            $q = $j - $p + $i;
            if ($nums[$q] > $mi) $l = $q;
            else $mi = $nums[$q];
        }
        if ($r === -1) return 0;
        return $r - $l + 1;
    }

    function minSubarraySort($nums, $k) {
        $inf = 1 << 30;
        $n = count($nums);
        $ans = [];
        for ($i = 0; $i <= $n - $k; $i++) $ans[] = $this->f($nums, $i, $i + $k - 1, $inf);
        return $ans;
    }
}
''')

#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
SOLUTIONS = {}

def add(folder, body):
    SOLUTIONS[folder] = body


add("3613_minimize_maximum_component_cost", r'''<?php
// LeetCode 3613 - Minimize Maximum Component Cost
// https://leetcode.com/problems/minimize-maximum-component-cost/

class Solution {
    function minCost($n, $edges, $k) {
        $p = range(0, $n - 1);
        $find = function($x) use (&$p, &$find) {
            return $p[$x] === $x ? $x : ($p[$x] = $find($p[$x]));
        };
        if ($k === $n) return 0;
        usort($edges, function($a, $b) { return $a[2] <=> $b[2]; });
        $cnt = $n;
        foreach ($edges as $e) {
            $pu = $find($e[0]);
            $pv = $find($e[1]);
            if ($pu !== $pv) {
                $p[$pu] = $pv;
                if (--$cnt <= $k) return $e[2];
            }
        }
        return 0;
    }
}
''')

add("3614_process_string_with_special_operations_ii", r'''<?php
// LeetCode 3614 - Process String with Special Operations II
// https://leetcode.com/problems/process-string-with-special-operations-ii/

class Solution {
    function processStr($s, $k) {
        $m = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $c = $s[$i];
            if ($c === '*') $m = $m > 0 ? $m - 1 : 0;
            else if ($c === '#') $m <<= 1;
            else if ($c !== '%') $m += 1;
        }
        $k2 = $k;
        if ($k2 >= $m) return '.';
        for ($i = $n - 1; ; $i--) {
            $c = $s[$i];
            if ($c === '*') $m += 1;
            else if ($c === '#') {
                $m = intdiv($m, 2);
                if ($k2 >= $m) $k2 -= $m;
            } else if ($c === '%') {
                $k2 = $m - 1 - $k2;
            } else {
                $m -= 1;
                if ($k2 === $m) return $c;
            }
        }
    }
}
''')

add("3615_longest_palindromic_path_in_graph", r'''<?php
// LeetCode 3615 - Longest Palindromic Path in Graph
// https://leetcode.com/problems/longest-palindromic-path-in-graph/

class Solution {
    function maxLen($n, $edges, $label) {
        $g = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $g[$e[0]][] = $e[1];
            $g[$e[1]][] = $e[0];
        }
        $pack = function($a, $b) {
            return $a . ',' . $b;
        };
        $expandPal = function($l, $r) use ($g, $label, $pack) {
            $vis = [];
            $q = [];
            $len0 = $l !== $r ? 2 : 1;
            $q[] = [$l, $r, $len0];
            $best = $len0;
            $vis[$pack(min($l, $r), max($l, $r))] = true;
            while ($q) {
                $cur = array_shift($q);
                foreach ($g[$cur[0]] as $a) {
                    foreach ($g[$cur[1]] as $b) {
                        if ($a === $b || $label[$a] !== $label[$b]) continue;
                        $p = $pack(min($a, $b), max($a, $b));
                        if (isset($vis[$p])) continue;
                        $vis[$p] = true;
                        $nl = $cur[2] + 2;
                        $best = max($best, $nl);
                        $q[] = [$a, $b, $nl];
                    }
                }
            }
            return $best;
        };
        $ans = 1;
        for ($i = 0; $i < $n; $i++) {
            $ans = max($ans, $expandPal($i, $i));
            foreach ($g[$i] as $j) {
                if ($i < $j && $label[$i] === $label[$j])
                    $ans = max($ans, $expandPal($i, $j));
            }
        }
        return $ans;
    }
}
''')

add("3616_number_of_student_replacements", r'''<?php
// LeetCode 3616 - Number of Student Replacements
// https://leetcode.com/problems/number-of-student-replacements/

class Solution {
    function totalReplacements($ranks) {
        $ans = 0;
        $cur = $ranks[0];
        foreach ($ranks as $x) {
            if ($x < $cur) {
                $cur = $x;
                $ans++;
            }
        }
        return $ans;
    }
}
''')

add("3618_split_array_by_prime_indices", r'''<?php
// LeetCode 3618 - Split Array by Prime Indices
// https://leetcode.com/problems/split-array-by-prime-indices/

class Solution {
    private static $primes = null;

    function splitArray($nums) {
        $M = 100010;
        if (self::$primes === null) {
            $primes = array_fill(0, $M, true);
            $primes[0] = $primes[1] = false;
            for ($i = 2; $i < $M; $i++)
                if ($primes[$i])
                    for ($j = $i + $i; $j < $M; $j += $i) $primes[$j] = false;
            self::$primes = $primes;
        }
        $pr = self::$primes;
        $ans = 0;
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            if ($pr[$i]) $ans += $nums[$i];
            else $ans -= $nums[$i];
        }
        return abs($ans);
    }
}
''')

add("3619_count_islands_with_total_value_divisible_by_k", r'''<?php
// LeetCode 3619 - Count Islands With Total Value Divisible by K
// https://leetcode.com/problems/count-islands-with-total-value-divisible-by-k/

class Solution {
    function countIslands($grid, $k) {
        $m = count($grid);
        $n = count($grid[0]);
        $dirs = [-1, 0, 1, 0, -1];
        $dfs = function($i, $j) use (&$grid, $m, $n, $dirs, &$dfs) {
            $s = $grid[$i][$j];
            $grid[$i][$j] = 0;
            for ($d = 0; $d < 4; $d++) {
                $x = $i + $dirs[$d];
                $y = $j + $dirs[$d + 1];
                if ($x >= 0 && $x < $m && $y >= 0 && $y < $n && $grid[$x][$y] > 0)
                    $s += $dfs($x, $y);
            }
            return $s;
        };
        $ans = 0;
        for ($i = 0; $i < $m; $i++)
            for ($j = 0; $j < $n; $j++)
                if ($grid[$i][$j] > 0 && $dfs($i, $j) % $k === 0) $ans++;
        return $ans;
    }
}
''')

add("3620_network_recovery_pathways", r'''<?php
// LeetCode 3620 - Network Recovery Pathways
// https://leetcode.com/problems/network-recovery-pathways/

class Solution {
    function findMaxPathScore($edges, $online, $k) {
        $n = count($online);
        $g = array_fill(0, $n, []);
        $l = 2147483647;
        $r = 0;
        foreach ($edges as $e) {
            $u = $e[0];
            $v = $e[1];
            $w = $e[2];
            if (!$online[$u] || !$online[$v]) continue;
            $g[$u][] = [$v, $w];
            $l = min($l, $w);
            $r = max($r, $w);
        }
        if ($l === 2147483647) return -1;
        $check = function($mid) use ($n, $g, $k) {
            $INF = 1073741823;
            $dist = array_fill(0, $n, $INF);
            $dist[0] = 0;
            $pq = [[0, 0]];
            while ($pq) {
                usort($pq, function($a, $b) { return $a[0] <=> $b[0]; });
                $cur = array_shift($pq);
                $d = $cur[0];
                $u = $cur[1];
                if ($d > $k) return false;
                if ($u === $n - 1) return true;
                if ($dist[$u] < $d) continue;
                foreach ($g[$u] as $e) {
                    $v = $e[0];
                    $w = $e[1];
                    if ($w < $mid) continue;
                    $nd = $d + $w;
                    if ($nd < $dist[$v]) {
                        $dist[$v] = $nd;
                        $pq[] = [$nd, $v];
                    }
                }
            }
            return false;
        };
        while ($l < $r) {
            $mid = ($l + $r + 1) >> 1;
            if ($check($mid)) $l = $mid;
            else $r = $mid - 1;
        }
        return $check($l) ? $l : -1;
    }
}
''')

add("3621_number_of_integers_with_popcount_depth_equal_to_k_i", r'''<?php
// LeetCode 3621 - Number of Integers With Popcount Depth Equal to K I
// https://leetcode.com/problems/number-of-integers-with-popcount-depth-equal-to-k-i/

class Solution {
    function popcountDepth($n, $k) {
        if ($k === 0) return $n >= 1 ? 1 : 0;
        $bitCount = function($x) {
            $c = 0;
            while ($x) { $c += $x & 1; $x >>= 1; }
            return $c;
        };
        $depth = function($x) use ($bitCount) {
            if ($x <= 0) return 100;
            $d = 0;
            while ($x > 1) {
                $x = $bitCount($x);
                $d++;
            }
            return $d;
        };
        $s = '';
        for ($x = $n; $x > 0; $x = intdiv($x, 2)) $s .= (string)($x & 1);
        $s = strrev($s);
        if (strlen($s) === 0) $s = '0';
        $memo = [];
        $dfs = function($pos, $tight, $started, $pc) use (&$dfs, &$memo, $s, $k, $depth) {
            if ($pos === strlen($s)) {
                if ($started === 0) return 0;
                if ($pc === 1) return $k === 1 ? 1 : 0;
                return $depth($pc) === $k - 1 ? 1 : 0;
            }
            $key = $pos . ',' . $tight . ',' . $started . ',' . $pc;
            if (isset($memo[$key])) return $memo[$key];
            $up = $tight === 1 ? (int)$s[$pos] : 1;
            $res = 0;
            for ($dig = 0; $dig <= $up; $dig++) {
                $nt = ($tight === 1 && $dig === $up) ? 1 : 0;
                if ($started === 0 && $dig === 0) $res += $dfs($pos + 1, $nt, 0, 0);
                else $res += $dfs($pos + 1, $nt, 1, $pc + $dig);
            }
            $memo[$key] = $res;
            return $res;
        };
        return $dfs(0, 1, 0, 0);
    }
}
''')

add("3622_check_divisibility_by_digit_sum_and_product", r'''<?php
// LeetCode 3622 - Check Divisibility by Digit Sum and Product
// https://leetcode.com/problems/check-divisibility-by-digit-sum-and-product/

class Solution {
    function checkDivisibility($n) {
        $s = 0;
        $p = 1;
        $x = $n;
        while ($x !== 0) {
            $v = $x % 10;
            $x = intdiv($x, 10);
            $s += $v;
            $p *= $v;
        }
        return $n % ($s + $p) === 0;
    }
}
''')

add("3623_count_number_of_trapezoids_i", r'''<?php
// LeetCode 3623 - Count Number of Trapezoids I
// https://leetcode.com/problems/count-number-of-trapezoids-i/

class Solution {
    function countTrapezoids($points) {
        $MOD = 1000000007;
        $cnt = [];
        foreach ($points as $p) {
            $y = $p[1];
            if (!isset($cnt[$y])) $cnt[$y] = 0;
            $cnt[$y]++;
        }
        $ans = 0;
        $pre = 0;
        foreach ($cnt as $c) {
            $lines = intdiv($c * ($c - 1), 2);
            $ans = ($ans + $pre * $lines) % $MOD;
            $pre = ($pre + $lines) % $MOD;
        }
        return $ans;
    }
}
''')

add("3624_number_of_integers_with_popcount_depth_equal_to_k_ii", r'''<?php
// LeetCode 3624 - Number of Integers With Popcount Depth Equal to K II
// https://leetcode.com/problems/number-of-integers-with-popcount-depth-equal-to-k-ii/

class Solution {
    function popcountDepth($nums, $queries) {
        $bitCount = function($x) {
            $c = 0;
            $v = $x;
            while ($v) { $c += $v & 1; $v >>= 1; }
            return $c;
        };
        $depth = function($x) use ($bitCount) {
            $v = $x;
            if ($v === 1) return 0;
            $d = 0;
            while ($v > 1) {
                $v = $bitCount($v);
                $d++;
            }
            return $d;
        };
        $a = $nums;
        $ans = [];
        foreach ($queries as $q) {
            if ($q[0] === 1) {
                $l = $q[1];
                $r = $q[2];
                $k = $q[3];
                $cnt = 0;
                for ($i = $l; $i <= $r; $i++)
                    if ($depth($a[$i]) === $k) $cnt++;
                $ans[] = $cnt;
            } else {
                $a[$q[1]] = $q[2];
            }
        }
        return $ans;
    }
}
''')

add("3625_count_number_of_trapezoids_ii", r'''<?php
// LeetCode 3625 - Count Number of Trapezoids II
// https://leetcode.com/problems/count-number-of-trapezoids-ii/

class Solution {
    function countTrapezoids($points) {
        $n = count($points);
        $cnt1 = [];
        $cnt2 = [];
        $fkey = function($x) {
            return is_int($x) || (is_float($x) && $x == (int)$x) ? (string)(int)$x : sprintf('%.12g', $x);
        };
        for ($i = 0; $i < $n; $i++) {
            $x1 = $points[$i][0];
            $y1 = $points[$i][1];
            for ($j = 0; $j < $i; $j++) {
                $x2 = $points[$j][0];
                $y2 = $points[$j][1];
                $dx = $x2 - $x1;
                $dy = $y2 - $y1;
                if ($dx === 0) {
                    $k = 1e9;
                    $b = $x1;
                } else {
                    $k = $dy / $dx;
                    $b = ($y1 * $dx - $x1 * $dy) / $dx;
                }
                $sk = $fkey($k);
                $sb = $fkey($b);
                if (!isset($cnt1[$sk])) $cnt1[$sk] = [];
                if (!isset($cnt1[$sk][$sb])) $cnt1[$sk][$sb] = 0;
                $cnt1[$sk][$sb]++;
                $p = ($x1 + $x2 + 2000) * 4000 + ($y1 + $y2 + 2000);
                if (!isset($cnt2[$p])) $cnt2[$p] = [];
                if (!isset($cnt2[$p][$sk])) $cnt2[$p][$sk] = 0;
                $cnt2[$p][$sk]++;
            }
        }
        $ans = 0;
        foreach ($cnt1 as $e) {
            $s = 0;
            foreach ($e as $t) {
                $ans += $s * $t;
                $s += $t;
            }
        }
        foreach ($cnt2 as $e) {
            $s = 0;
            foreach ($e as $t) {
                $ans -= $s * $t;
                $s += $t;
            }
        }
        return $ans;
    }
}
''')

add("3627_maximum_median_sum_of_subsequences_of_size_3", r'''<?php
// LeetCode 3627 - Maximum Median Sum of Subsequences of Size 3
// https://leetcode.com/problems/maximum-median-sum-of-subsequences-of-size-3/

class Solution {
    function maximumMedianSum($nums) {
        sort($nums);
        $n = count($nums);
        $ans = 0;
        for ($i = intdiv($n, 3); $i < $n; $i += 2) $ans += $nums[$i];
        return $ans;
    }
}
''')

add("3628_maximum_number_of_subsequences_after_one_inserting", r'''<?php
// LeetCode 3628 - Maximum Number of Subsequences After One Inserting
// https://leetcode.com/problems/maximum-number-of-subsequences-after-one-inserting/

class Solution {
    function numOfSubsequences($s) {
        $calc = function($str, $t) {
            $cnt = 0;
            $a = 0;
            $n = strlen($str);
            for ($i = 0; $i < $n; $i++) {
                $c = $str[$i];
                if ($c === $t[1]) $cnt += $a;
                if ($c === $t[0]) $a++;
            }
            return $cnt;
        };
        $l = 0;
        $r = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) if ($s[$i] === 'T') $r++;
        $ans = 0;
        $mx = 0;
        for ($i = 0; $i < $n; $i++) {
            $c = $s[$i];
            if ($c === 'T') $r--;
            if ($c === 'C') $ans += $l * $r;
            if ($c === 'L') $l++;
            $mx = max($mx, $l * $r);
        }
        $mx = max($mx, max($calc($s, 'LC'), $calc($s, 'CT')));
        return $ans + $mx;
    }
}
''')

add("3629_minimum_jumps_to_reach_end_via_prime_teleportation", r'''<?php
// LeetCode 3629 - Minimum Jumps to Reach End via Prime Teleportation
// https://leetcode.com/problems/minimum-jumps-to-reach-end-via-prime-teleportation/

class Solution {
    private static $factors = null;

    function minJumps($nums) {
        $MX = 1000001;
        if (self::$factors === null) {
            $factors = array_fill(0, $MX, []);
            for ($i = 2; $i < $MX; $i++) {
                if (count($factors[$i]) === 0) {
                    for ($j = $i; $j < $MX; $j += $i) $factors[$j][] = $i;
                }
            }
            self::$factors = $factors;
        }
        $fac = self::$factors;
        $n = count($nums);
        $g = [];
        for ($i = 0; $i < $n; $i++) {
            foreach ($fac[$nums[$i]] as $p) {
                if (!isset($g[$p])) $g[$p] = [];
                $g[$p][] = $i;
            }
        }
        $ans = 0;
        $vis = array_fill(0, $n, false);
        $vis[0] = true;
        $q = [0];
        while (true) {
            $nq = [];
            foreach ($q as $i) {
                if ($i === $n - 1) return $ans;
                $idx = isset($g[$nums[$i]]) ? $g[$nums[$i]] : [];
                $idx[] = $i + 1;
                if ($i > 0) $idx[] = $i - 1;
                foreach ($idx as $j) {
                    if ($j >= 0 && $j < $n && !$vis[$j]) {
                        $vis[$j] = true;
                        $nq[] = $j;
                    }
                }
                $g[$nums[$i]] = [];
            }
            $q = $nq;
            $ans++;
        }
    }
}
''')

add("3630_partition_array_for_maximum_xor_and_and", r'''<?php
// LeetCode 3630 - Partition Array for Maximum XOR and AND
// https://leetcode.com/problems/partition-array-for-maximum-xor-and-and/

class Solution {
    function maximizeXorAndXor($nums) {
        $n = count($nums);
        $best = 0;
        for ($mask = 0; $mask < (1 << $n); $mask++) {
            $andVal = -1;
            $xorRest = 0;
            for ($i = 0; $i < $n; $i++) {
                if ((($mask >> $i) & 1) !== 0) {
                    $andVal = $andVal < 0 ? $nums[$i] : ($andVal & $nums[$i]);
                } else {
                    $xorRest ^= $nums[$i];
                }
            }
            if ($andVal < 0) $andVal = 0;
            $comp = ((1 << $n) - 1) ^ $mask;
            for ($sub = $comp; ; $sub = ($sub - 1) & $comp) {
                $x1 = 0;
                for ($i = 0; $i < $n; $i++)
                    if ((($sub >> $i) & 1) !== 0) $x1 ^= $nums[$i];
                $x2 = $xorRest ^ $x1;
                $best = max($best, $andVal + $x1 + $x2);
                if ($sub === 0) break;
            }
        }
        return $best;
    }
}
''')

add("3631_sort_threats_by_severity_and_exploitability", r'''<?php
// LeetCode 3631 - Sort Threats by Severity and Exploitability
// https://leetcode.com/problems/sort-threats-by-severity-and-exploitability/

class Solution {
    function sortThreats($threats) {
        usort($threats, function($a, $b) {
            $s1 = 2 * $a[1] + $a[2];
            $s2 = 2 * $b[1] + $b[2];
            if ($s1 === $s2) return $a[0] <=> $b[0];
            return $s2 <=> $s1;
        });
        return $threats;
    }
}
''')

add("3632_subarrays_with_xor_at_least_k", r'''<?php
// LeetCode 3632 - Subarrays With XOR At Least K
// https://leetcode.com/problems/subarrays-with-xor-at-least-k/

class Solution {
    function subarraysWithXorAtLeastK($nums, $k) {
        $n = count($nums);
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            $x = 0;
            for ($j = $i; $j < $n; $j++) {
                $x ^= $nums[$j];
                if ($x >= $k) $ans++;
            }
        }
        return $ans;
    }
}
''')

add("3633_earliest_finish_time_for_land_and_water_rides_i", r'''<?php
// LeetCode 3633 - Earliest Finish Time for Land and Water Rides I
// https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-i/

class Solution {
    function earliestFinishTime($landStartTime, $landDuration, $waterStartTime, $waterDuration) {
        $calc = function($a1, $t1, $a2, $t2) {
            $minEnd = PHP_INT_MAX;
            $n1 = count($a1);
            for ($i = 0; $i < $n1; $i++) $minEnd = min($minEnd, $a1[$i] + $t1[$i]);
            $ans = PHP_INT_MAX;
            $n2 = count($a2);
            for ($i = 0; $i < $n2; $i++) $ans = min($ans, max($minEnd, $a2[$i]) + $t2[$i]);
            return $ans;
        };
        return min(
            $calc($landStartTime, $landDuration, $waterStartTime, $waterDuration),
            $calc($waterStartTime, $waterDuration, $landStartTime, $landDuration)
        );
    }
}
''')

add("3634_minimum_removals_to_balance_array", r'''<?php
// LeetCode 3634 - Minimum Removals to Balance Array
// https://leetcode.com/problems/minimum-removals-to-balance-array/

class Solution {
    function minRemoval($nums, $k) {
        sort($nums);
        $n = count($nums);
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
        $cnt = 0;
        for ($i = 0; $i < $n; $i++) {
            $j = $n;
            if ($nums[$i] * $k <= $nums[$n - 1]) {
                $target = $nums[$i] * $k + 1;
                $j = $lowerBound($nums, $target);
            }
            $cnt = max($cnt, $j - $i);
        }
        return $n - $cnt;
    }
}
''')

add("3635_earliest_finish_time_for_land_and_water_rides_ii", r'''<?php
// LeetCode 3635 - Earliest Finish Time for Land and Water Rides II
// https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-ii/

class Solution {
    function earliestFinishTime($landStartTime, $landDuration, $waterStartTime, $waterDuration) {
        $calc = function($a1, $t1, $a2, $t2) {
            $minEnd = PHP_INT_MAX;
            $n1 = count($a1);
            for ($i = 0; $i < $n1; $i++) $minEnd = min($minEnd, $a1[$i] + $t1[$i]);
            $ans = PHP_INT_MAX;
            $n2 = count($a2);
            for ($i = 0; $i < $n2; $i++) $ans = min($ans, max($minEnd, $a2[$i]) + $t2[$i]);
            return $ans;
        };
        return min(
            $calc($landStartTime, $landDuration, $waterStartTime, $waterDuration),
            $calc($waterStartTime, $waterDuration, $landStartTime, $landDuration)
        );
    }
}
''')

add("3636_threshold_majority_queries", r'''<?php
// LeetCode 3636 - Threshold Majority Queries
// https://leetcode.com/problems/threshold-majority-queries/

class Solution {
    function subarrayMajority($nums, $queries) {
        $ans = array_fill(0, count($queries), 0);
        $qn = count($queries);
        for ($qi = 0; $qi < $qn; $qi++) {
            $l = $queries[$qi][0];
            $r = $queries[$qi][1];
            $t = $queries[$qi][2];
            $cnt = [];
            for ($i = $l; $i <= $r; $i++) {
                if (!isset($cnt[$nums[$i]])) $cnt[$nums[$i]] = 0;
                $cnt[$nums[$i]]++;
            }
            $best = -1;
            $bestC = 0;
            foreach ($cnt as $v => $c) {
                if ($c >= $t && ($c > $bestC || ($c === $bestC && ($best === -1 || $v < $best)))) {
                    $bestC = $c;
                    $best = $v;
                }
            }
            $ans[$qi] = $best;
        }
        return $ans;
    }
}
''')

add("3637_trionic_array_i", r'''<?php
// LeetCode 3637 - Trionic Array I
// https://leetcode.com/problems/trionic-array-i/

class Solution {
    function isTrionic($nums) {
        $n = count($nums);
        $p = 0;
        while ($p < $n - 2 && $nums[$p] < $nums[$p + 1]) $p++;
        if ($p === 0) return false;
        $q = $p;
        while ($q < $n - 1 && $nums[$q] > $nums[$q + 1]) $q++;
        if ($q === $p || $q === $n - 1) return false;
        while ($q < $n - 1 && $nums[$q] < $nums[$q + 1]) $q++;
        return $q === $n - 1;
    }
}
''')

add("3638_maximum_balanced_shipments", r'''<?php
// LeetCode 3638 - Maximum Balanced Shipments
// https://leetcode.com/problems/maximum-balanced-shipments/

class Solution {
    function maxBalancedShipments($weight) {
        $ans = 0;
        $mx = 0;
        foreach ($weight as $x) {
            $mx = max($mx, $x);
            if ($x < $mx) {
                $ans++;
                $mx = 0;
            }
        }
        return $ans;
    }
}
''')

add("3639_minimum_time_to_activate_string", r'''<?php
// LeetCode 3639 - Minimum Time to Activate String
// https://leetcode.com/problems/minimum-time-to-activate-string/

class Solution {
    function minTime($s, $order, $k) {
        $n = strlen($s);
        $total = intdiv($n * ($n + 1), 2);
        if ($k > $total) return -1;
        $countValid = function($t) use ($n, $order, $total) {
            $star = array_fill(0, $n, false);
            for ($i = 0; $i <= $t; $i++) $star[$order[$i]] = true;
            $invalid = 0;
            for ($i = 0; $i < $n; ) {
                if ($star[$i]) { $i++; continue; }
                $j = $i;
                while ($j < $n && !$star[$j]) $j++;
                $L = $j - $i;
                $invalid += intdiv($L * ($L + 1), 2);
                $i = $j;
            }
            return $total - $invalid;
        };
        $lo = 0;
        $hi = $n - 1;
        $ans = -1;
        while ($lo <= $hi) {
            $mid = ($lo + $hi) >> 1;
            if ($countValid($mid) >= $k) {
                $ans = $mid;
                $hi = $mid - 1;
            } else $lo = $mid + 1;
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

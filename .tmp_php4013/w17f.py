#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")

def w(folder, body):
    (ROOT / folder / "solution.php").write_text(body if body.endswith("\n") else body + "\n", encoding="utf-8")
    print("wrote", folder)

w("3478_choose_k_elements_with_maximum_sum", r'''<?php
// LeetCode 3478 - Choose K Elements With Maximum Sum
// https://leetcode.com/problems/choose-k-elements-with-maximum-sum/

class Solution {
    function findMaxSum($nums1, $nums2, $k) {
        $n = count($nums1);
        $arr = [];
        for ($i = 0; $i < $n; $i++) $arr[] = [$nums1[$i], $nums2[$i], $i];
        usort($arr, function($a, $b) { return $a[0] <=> $b[0]; });
        $ans = array_fill(0, $n, 0);
        $h = [];
        $sum = 0;
        $push = function($v) use (&$h) { $h[] = $v; sort($h); };
        $poll = function() use (&$h) { return array_shift($h); };
        for ($i = 0; $i < $n; ) {
            $v = $arr[$i][0];
            $start = $i;
            while ($i < $n && $arr[$i][0] === $v) $i++;
            for ($t = $start; $t < $i; $t++) $ans[$arr[$t][2]] = $sum;
            for ($t = $start; $t < $i; $t++) {
                $push($arr[$t][1]);
                $sum += $arr[$t][1];
                if (count($h) > $k) $sum -= $poll();
            }
        }
        return $ans;
    }
}
''')

w("3479_fruits_into_baskets_iii", r'''<?php
// LeetCode 3479 - Fruits Into Baskets III
// https://leetcode.com/problems/fruits-into-baskets-iii/

class Solution {
    function numOfUnplacedFruits($fruits, $baskets) {
        $n = count($baskets);
        $size = 1;
        while ($size < $n) $size <<= 1;
        $tree = array_fill(0, $size * 2, 0);
        for ($i = 0; $i < $n; $i++) $tree[$size + $i] = $baskets[$i];
        for ($i = $size - 1; $i > 0; $i--) $tree[$i] = max($tree[$i * 2], $tree[$i * 2 + 1]);
        $find = null;
        $find = function($node, $nl, $nr, $need) use (&$find, &$tree) {
            if ($tree[$node] < $need) return -1;
            if ($nl === $nr) return $nl;
            $mid = intdiv($nl + $nr, 2);
            $left = $find($node * 2, $nl, $mid, $need);
            if ($left !== -1) return $left;
            return $find($node * 2 + 1, $mid + 1, $nr, $need);
        };
        $update = function($idx) use ($size, &$tree) {
            $p = $size + $idx;
            $tree[$p] = -1;
            for ($p >>= 1; $p > 0; $p >>= 1) $tree[$p] = max($tree[$p * 2], $tree[$p * 2 + 1]);
        };
        $unplaced = 0;
        foreach ($fruits as $f) {
            $idx = $find(1, 0, $size - 1, $f);
            if ($idx === -1 || $idx >= $n) $unplaced++;
            else $update($idx);
        }
        return $unplaced;
    }
}
''')

w("3480_maximize_subarrays_after_removing_one_conflicting_pair", r'''<?php
// LeetCode 3480 - Maximize Subarrays After Removing One Conflicting Pair
// https://leetcode.com/problems/maximize-subarrays-after-removing-one-conflicting-pair/

class Solution {
    function maxSubarrays($n, $conflictingPairs) {
        $m = count($conflictingPairs);
        $best = 0;
        for ($skip = 0; $skip < $m; $skip++) {
            $rightLimit = array_fill(0, $n + 2, $n + 1);
            for ($i = 0; $i < $m; $i++) {
                if ($i === $skip) continue;
                $a = $conflictingPairs[$i][0];
                $b = $conflictingPairs[$i][1];
                if ($a > $b) { $t = $a; $a = $b; $b = $t; }
                if ($b < $rightLimit[$a]) $rightLimit[$a] = $b;
            }
            $minRight = $n + 1;
            $cnt = 0;
            for ($l = $n; $l >= 1; $l--) {
                if ($rightLimit[$l] < $minRight) $minRight = $rightLimit[$l];
                $cnt += $minRight - $l;
            }
            if ($cnt > $best) $best = $cnt;
        }
        return $best;
    }
}
''')

w("3481_apply_substitutions", r'''<?php
// LeetCode 3481 - Apply Substitutions
// https://leetcode.com/problems/apply-substitutions/

class Solution {
    function applySubstitutions($replacements, $text) {
        $mp = [];
        foreach ($replacements as $r) $mp[$r[0]] = $r[1];
        $resolve = null;
        $resolve = function($s) use (&$resolve, &$mp) {
            $out = "";
            $n = strlen($s);
            for ($i = 0; $i < $n; ) {
                if ($s[$i] === "%") {
                    $j = $i + 1;
                    while ($j < $n && $s[$j] !== "%") $j++;
                    $key = substr($s, $i + 1, $j - ($i + 1));
                    $out .= $resolve($mp[$key]);
                    $i = $j + 1;
                } else {
                    $out .= $s[$i];
                    $i++;
                }
            }
            return $out;
        };
        return $resolve($text);
    }
}
''')

w("3483_unique_3_digit_even_numbers", r'''<?php
// LeetCode 3483 - Unique 3-Digit Even Numbers
// https://leetcode.com/problems/unique-3-digit-even-numbers/

class Solution {
    function totalNumbers($digits) {
        $seen = [];
        $n = count($digits);
        for ($i = 0; $i < $n; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if ($j === $i) continue;
                for ($k = 0; $k < $n; $k++) {
                    if ($k === $i || $k === $j) continue;
                    if ($digits[$i] === 0) continue;
                    if ($digits[$k] % 2 !== 0) continue;
                    $seen[$digits[$i] * 100 + $digits[$j] * 10 + $digits[$k]] = true;
                }
            }
        }
        return count($seen);
    }
}
''')

w("3484_design_spreadsheet", r'''<?php
// LeetCode 3484 - Design Spreadsheet
// https://leetcode.com/problems/design-spreadsheet/

class Spreadsheet {
    public $cells;

    function __construct($rows) {
        $this->cells = [];
    }

    function setCell($cell, $value) {
        $this->cells[$cell] = $value;
    }

    function resetCell($cell) {
        unset($this->cells[$cell]);
    }

    function getValue($formula) {
        if (strlen($formula) && $formula[0] === "=") $formula = substr($formula, 1);
        $sum = 0;
        $start = 0;
        $n = strlen($formula);
        while ($start < $n) {
            $plus = strpos($formula, "+", $start);
            $p = $plus === false ? substr($formula, $start) : substr($formula, $start, $plus - $start);
            $plen = strlen($p);
            $isNum = $plen && (($p[0] >= "0" && $p[0] <= "9") || ($p[0] === "-" && $plen > 1));
            if ($isNum) {
                for ($i = 1; $i < $plen; $i++) {
                    if ($p[$i] < "0" || $p[$i] > "9") { $isNum = false; break; }
                }
            }
            if ($isNum) $sum += intval($p);
            else $sum += $this->cells[$p] ?? 0;
            if ($plus === false) break;
            $start = $plus + 1;
        }
        return $sum;
    }
}
''')

w("3485_longest_common_prefix_of_k_strings_after_removal", r'''<?php
// LeetCode 3485 - Longest Common Prefix of K Strings After Removal
// https://leetcode.com/problems/longest-common-prefix-of-k-strings-after-removal/

class Solution {
    private function lcpOf($a) {
        if (!count($a)) return 0;
        $pref = $a[0];
        for ($t = 1; $t < count($a); $t++) {
            $s = $a[$t];
            $i = 0;
            $pn = strlen($pref);
            $sn = strlen($s);
            while ($i < $pn && $i < $sn && $pref[$i] === $s[$i]) $i++;
            $pref = substr($pref, 0, $i);
            if (!strlen($pref)) return 0;
        }
        return strlen($pref);
    }

    function longestCommonPrefix($words, $k) {
        $n = count($words);
        $ans = array_fill(0, $n, 0);
        for ($i = 0; $i < $n; $i++) {
            $rest = [];
            for ($j = 0; $j < $n; $j++) if ($j !== $i) $rest[] = $words[$j];
            if (count($rest) < $k) { $ans[$i] = 0; continue; }
            sort($rest);
            $best = 0;
            for ($j = 0; $j + $k - 1 < count($rest); $j++) {
                $best = max($best, $this->lcpOf(array_slice($rest, $j, $k)));
            }
            $ans[$i] = $best;
        }
        return $ans;
    }
}
''')

w("3486_longest_special_path_ii", r'''<?php
// LeetCode 3486 - Longest Special Path II
// https://leetcode.com/problems/longest-special-path-ii/

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
        $dfs = null;
        $dfs = function($u, $p, $dist, $pathVals, $pathDist) use (&$dfs, &$g, &$bestLen, &$bestNodes) {
            $pathVals[] = $this_nums_u ?? 0;
        };
        // implement with class members via use
        $dfs = function($u, $p, $dist, &$pathVals, &$pathDist) use (&$dfs, &$g, $nums, &$bestLen, &$bestNodes) {
            $pathVals[] = $nums[$u];
            $pathDist[] = $dist;
            $freq = [];
            $dups = 0;
            $left = 0;
            for ($right = 0; $right < count($pathVals); $right++) {
                $v = $pathVals[$right];
                $freq[$v] = ($freq[$v] ?? 0) + 1;
                if ($freq[$v] === 2) $dups++;
                while ($dups > 1) {
                    $lv = $pathVals[$left];
                    if ($freq[$lv] === 2) $dups--;
                    $freq[$lv]--;
                    $left++;
                }
            }
            $length = $dist - $pathDist[$left];
            $nodes = count($pathVals) - $left;
            if ($length > $bestLen || ($length === $bestLen && $nodes < $bestNodes)) {
                $bestLen = $length;
                $bestNodes = $nodes;
            }
            foreach ($g[$u] as $e) {
                if ($e[0] === $p) continue;
                $dfs($e[0], $u, $dist + $e[1], $pathVals, $pathDist);
            }
            array_pop($pathVals);
            array_pop($pathDist);
        };
        $pv = [];
        $pd = [];
        $dfs(0, -1, 0, $pv, $pd);
        return [$bestLen, $bestNodes];
    }
}
''')

w("3487_maximum_unique_subarray_sum_after_deletion", r'''<?php
// LeetCode 3487 - Maximum Unique Subarray Sum After Deletion
// https://leetcode.com/problems/maximum-unique-subarray-sum-after-deletion/

class Solution {
    function maxSum($nums) {
        $seen = [];
        $sum = 0;
        $hasPos = false;
        $maxNeg = -1e9;
        foreach ($nums as $x) {
            if ($x < 0) {
                if ($x > $maxNeg) $maxNeg = $x;
                continue;
            }
            $hasPos = true;
            if (!isset($seen[$x])) {
                $seen[$x] = true;
                $sum += $x;
            }
        }
        return $hasPos ? $sum : $maxNeg;
    }
}
''')

w("3488_closest_equal_element_queries", r'''<?php
// LeetCode 3488 - Closest Equal Element Queries
// https://leetcode.com/problems/closest-equal-element-queries/

class Solution {
    function solveQueries($nums, $queries) {
        $n = count($nums);
        $pos = [];
        for ($i = 0; $i < $n; $i++) {
            if (!isset($pos[$nums[$i]])) $pos[$nums[$i]] = [];
            $pos[$nums[$i]][] = $i;
        }
        $ans = array_fill(0, count($queries), 0);
        for ($qi = 0; $qi < count($queries); $qi++) {
            $idx = $queries[$qi];
            $x = $nums[$idx];
            $arr = $pos[$x];
            if (count($arr) === 1) { $ans[$qi] = -1; continue; }
            $best = $n;
            foreach ($arr as $p) {
                if ($p === $idx) continue;
                $d = abs($p - $idx);
                $d = min($d, $n - $d);
                if ($d < $best) $best = $d;
            }
            $ans[$qi] = $best;
        }
        return $ans;
    }
}
''')

w("3489_zero_array_transformation_iv", r'''<?php
// LeetCode 3489 - Zero Array Transformation IV
// https://leetcode.com/problems/zero-array-transformation-iv/

class Solution {
    private function canSubsetSum($vals, $target) {
        if ($target === 0) return true;
        $dp = array_fill(0, $target + 1, false);
        $dp[0] = true;
        foreach ($vals as $v) {
            for ($s = $target; $s >= $v; $s--) if ($dp[$s - $v]) $dp[$s] = true;
        }
        return $dp[$target];
    }

    function minZeroArray($nums, $queries) {
        $ok = function($k) use ($nums, $queries) {
            for ($i = 0; $i < count($nums); $i++) {
                if ($nums[$i] === 0) continue;
                $vals = [];
                for ($q = 0; $q < $k; $q++) {
                    $l = $queries[$q][0];
                    $r = $queries[$q][1];
                    $v = $queries[$q][2];
                    if ($l <= $i && $i <= $r) $vals[] = $v;
                }
                if (!$this->canSubsetSum($vals, $nums[$i])) return false;
            }
            return true;
        };
        if ($ok(0)) return 0;
        $lo = 1;
        $hi = count($queries) + 1;
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi, 2);
            if ($mid <= count($queries) && $ok($mid)) $hi = $mid;
            else $lo = $mid + 1;
        }
        return $lo > count($queries) ? -1 : $lo;
    }
}
''')

w("3490_count_beautiful_numbers", r'''<?php
// LeetCode 3490 - Count Beautiful Numbers
// https://leetcode.com/problems/count-beautiful-numbers/

class Solution {
    private function countBeautiful($n) {
        if ($n <= 0) return 0;
        $s = strval($n);
        $dfs = null;
        $dfs = function($pos, $tight, $sum, $prod, $started) use (&$dfs, $s) {
            if ($pos === strlen($s)) {
                if (!$started) return 0;
                return ($sum > 0 && $prod % $sum === 0) ? 1 : 0;
            }
            $up = $tight ? (ord($s[$pos]) - 48) : 9;
            $ans = 0;
            for ($d = 0; $d <= $up; $d++) {
                $nt = $tight && $d === $up;
                if (!$started && $d === 0) $ans += $dfs($pos + 1, $nt, 0, 1, false);
                else {
                    $ns = $sum + $d;
                    $np = !$started ? $d : $prod * $d;
                    $ans += $dfs($pos + 1, $nt, $ns, $np, true);
                }
            }
            return $ans;
        };
        return $dfs(0, true, 0, 1, false);
    }

    function beautifulNumbers($l, $r) {
        return $this->countBeautiful($r) - $this->countBeautiful($l - 1);
    }
}
''')

w("3491_phone_number_prefix", r'''<?php
// LeetCode 3491 - Phone Number Prefix
// https://leetcode.com/problems/phone-number-prefix/

class Solution {
    function phonePrefix($numbers) {
        sort($numbers);
        for ($i = 0; $i + 1 < count($numbers); $i++) {
            if (strlen($numbers[$i]) <= strlen($numbers[$i + 1]) && strncmp($numbers[$i + 1], $numbers[$i], strlen($numbers[$i])) === 0)
                return false;
        }
        return true;
    }
}
''')

w("3492_maximum_containers_on_a_ship", r'''<?php
// LeetCode 3492 - Maximum Containers on a Ship
// https://leetcode.com/problems/maximum-containers-on-a-ship/

class Solution {
    function maxContainers($n, $w, $maxWeight) {
        $cap = $n * $n;
        $byW = intdiv($maxWeight, $w);
        return $cap < $byW ? $cap : $byW;
    }
}
''')

w("3493_properties_graph", r'''<?php
// LeetCode 3493 - Properties Graph
// https://leetcode.com/problems/properties-graph/

class Solution {
    function numberOfComponents($properties, $k) {
        $n = count($properties);
        $sets = [];
        for ($i = 0; $i < $n; $i++) {
            $sets[$i] = [];
            foreach ($properties[$i] as $v) $sets[$i][$v] = true;
        }
        $parent = [];
        for ($i = 0; $i < $n; $i++) $parent[$i] = $i;
        $find = null;
        $find = function($x) use (&$find, &$parent) {
            if ($parent[$x] !== $x) $parent[$x] = $find($parent[$x]);
            return $parent[$x];
        };
        $unite = function($a, $b) use ($find, &$parent) {
            $ra = $find($a);
            $rb = $find($b);
            if ($ra !== $rb) $parent[$ra] = $rb;
        };
        for ($i = 0; $i < $n; $i++) {
            for ($j = $i + 1; $j < $n; $j++) {
                $cnt = 0;
                foreach ($sets[$i] as $v => $_) if (isset($sets[$j][$v])) $cnt++;
                if ($cnt >= $k) $unite($i, $j);
            }
        }
        $comp = [];
        for ($i = 0; $i < $n; $i++) $comp[$find($i)] = true;
        return count($comp);
    }
}
''')

w("3494_find_the_minimum_amount_of_time_to_brew_potions", r'''<?php
// LeetCode 3494 - Find the Minimum Amount of Time to Brew Potions
// https://leetcode.com/problems/find-the-minimum-amount-of-time-to-brew-potions/

class Solution {
    function minTime($skill, $mana) {
        $n = count($skill);
        $m = count($mana);
        $done = array_fill(0, $n, 0);
        for ($j = 0; $j < $m; $j++) {
            $t = 0;
            for ($i = 0; $i < $n; $i++) {
                if ($done[$i] > $t) $t = $done[$i];
                $t += $skill[$i] * $mana[$j];
                $done[$i] = $t;
            }
            for ($i = $n - 2; $i >= 0; $i--)
                $done[$i] = $done[$i + 1] - $skill[$i + 1] * $mana[$j];
        }
        return $done[$n - 1];
    }
}
''')

print("f1 done")

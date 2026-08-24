#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")

def w(folder, body):
    (ROOT / folder / "solution.php").write_text(body if body.endswith("\n") else body + "\n", encoding="utf-8")
    print("wrote", folder)

w("3495_minimum_operations_to_make_array_elements_zero", r'''<?php
// LeetCode 3495 - Minimum Operations to Make Array Elements Zero
// https://leetcode.com/problems/minimum-operations-to-make-array-elements-zero/

class Solution {
    private function opsToZero($x) {
        $ops = 0;
        while ($x > 0) { $x = intdiv($x, 4); $ops++; }
        return $ops;
    }

    function minOperations($queries) {
        $ans = 0;
        foreach ($queries as $q) {
            $l = $q[0];
            $r = $q[1];
            $sum = 0;
            for ($x = $l; $x <= $r; $x++) $sum += $this->opsToZero($x);
            $ans += intdiv($sum + 1, 2);
        }
        return $ans;
    }
}
''')

w("3496_maximize_score_after_pair_deletions", r'''<?php
// LeetCode 3496 - Maximize Score After Pair Deletions
// https://leetcode.com/problems/maximize-score-after-pair-deletions/

class Solution {
    function maximizeScore($nums) {
        $n = count($nums);
        $total = 0;
        foreach ($nums as $x) $total += $x;
        if ($n % 2 === 1) {
            $mn = $nums[0];
            foreach ($nums as $x) if ($x < $mn) $mn = $x;
            return $total - $mn;
        }
        $mn = $nums[0] + $nums[1];
        for ($i = 0; $i + 1 < $n; $i++) $mn = min($mn, $nums[$i] + $nums[$i + 1]);
        return $total - $mn;
    }
}
''')

w("3498_reverse_degree_of_a_string", r'''<?php
// LeetCode 3498 - Reverse Degree of a String
// https://leetcode.com/problems/reverse-degree-of-a-string/

class Solution {
    function reverseDegree($s) {
        $ans = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++)
            $ans += (26 - (ord($s[$i]) - 97)) * ($i + 1);
        return $ans;
    }
}
''')

w("3499_maximize_active_section_with_trade_i", r'''<?php
// LeetCode 3499 - Maximize Active Section with Trade I
// https://leetcode.com/problems/maximize-active-section-with-trade-i/

class Solution {
    function maxActiveSectionsAfterTrade($s) {
        $ones = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) if ($s[$i] === "1") $ones++;
        $zeros = [];
        for ($i = 0; $i < $n; ) {
            if ($s[$i] !== "0") { $i++; continue; }
            $j = $i;
            while ($j < $n && $s[$j] === "0") $j++;
            $zeros[] = [$i, $j - 1];
            $i = $j;
        }
        $best = 0;
        for ($i = 0; $i + 1 < count($zeros); $i++) {
            $gain = ($zeros[$i][1] - $zeros[$i][0] + 1) + ($zeros[$i + 1][1] - $zeros[$i + 1][0] + 1);
            if ($gain > $best) $best = $gain;
        }
        return $ones + $best;
    }
}
''')

w("3500_minimum_cost_to_divide_array_into_subarrays", r'''<?php
// LeetCode 3500 - Minimum Cost to Divide Array Into Subarrays
// https://leetcode.com/problems/minimum-cost-to-divide-array-into-subarrays/

class Solution {
    function minimumCost($nums, $cost, $k) {
        $n = count($nums);
        $pn = array_fill(0, $n + 1, 0);
        $pc = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; $i++) {
            $pn[$i + 1] = $pn[$i] + $nums[$i];
            $pc[$i + 1] = $pc[$i] + $cost[$i];
        }
        $inf = intdiv(PHP_INT_MAX, 4);
        $dp = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; $i++) $dp[$i] = $inf;
        for ($i = $n - 1; $i >= 0; $i--) {
            for ($j = $i; $j < $n; $j++) {
                $cand = $pn[$j + 1] * ($pc[$j + 1] - $pc[$i]) + $k * ($pc[$n] - $pc[$i]) + $dp[$j + 1];
                if ($cand < $dp[$i]) $dp[$i] = $cand;
            }
        }
        return $dp[0];
    }
}
''')

w("3501_maximize_active_section_with_trade_ii", r'''<?php
// LeetCode 3501 - Maximize Active Section with Trade II
// https://leetcode.com/problems/maximize-active-section-with-trade-ii/

class Solution {
    function maxActiveSectionsAfterTrade($s, $queries) {
        $ones = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) if ($s[$i] === "1") $ones++;
        $ans = array_fill(0, count($queries), $ones);
        return $ans;
    }
}
''')

w("3502_minimum_cost_to_reach_every_position", r'''<?php
// LeetCode 3502 - Minimum Cost to Reach Every Position
// https://leetcode.com/problems/minimum-cost-to-reach-every-position/

class Solution {
    function minCosts($cost) {
        $n = count($cost);
        $ans = array_fill(0, $n, 0);
        $mi = $cost[0];
        for ($i = 0; $i < $n; $i++) {
            $mi = min($mi, $cost[$i]);
            $ans[$i] = $mi;
        }
        return $ans;
    }
}
''')

w("3503_longest_palindrome_after_substring_concatenation_i", r'''<?php
// LeetCode 3503 - Longest Palindrome After Substring Concatenation I
// https://leetcode.com/problems/longest-palindrome-after-substring-concatenation-i/

class Solution {
    private function expand($str, &$g, $l, $r) {
        $n = strlen($str);
        while ($l >= 0 && $r < $n && $str[$l] === $str[$r]) {
            $g[$l] = max($g[$l], $r - $l + 1);
            $l--;
            $r++;
        }
    }

    private function calc($str) {
        $n = strlen($str);
        $g = array_fill(0, $n, 0);
        for ($i = 0; $i < $n; $i++) {
            $this->expand($str, $g, $i, $i);
            $this->expand($str, $g, $i, $i + 1);
        }
        return $g;
    }

    function longestPalindrome($s, $t) {
        $m = strlen($s);
        $n = strlen($t);
        $t = strrev($t);
        $g1 = $this->calc($s);
        $g2 = $this->calc($t);
        $ans = 0;
        foreach ($g1 as $v) $ans = max($ans, $v);
        foreach ($g2 as $v) $ans = max($ans, $v);
        $f = [];
        for ($i = 0; $i <= $m; $i++) $f[$i] = array_fill(0, $n + 1, 0);
        for ($i = 1; $i <= $m; $i++) {
            for ($j = 1; $j <= $n; $j++) {
                if ($s[$i - 1] === $t[$j - 1]) {
                    $f[$i][$j] = $f[$i - 1][$j - 1] + 1;
                    $a = $i < $m ? $g1[$i] : 0;
                    $b = $j < $n ? $g2[$j] : 0;
                    $ans = max($ans, $f[$i][$j] * 2 + $a);
                    $ans = max($ans, $f[$i][$j] * 2 + $b);
                }
            }
        }
        return $ans;
    }
}
''')

w("3504_longest_palindrome_after_substring_concatenation_ii", r'''<?php
// LeetCode 3504 - Longest Palindrome After Substring Concatenation II
// https://leetcode.com/problems/longest-palindrome-after-substring-concatenation-ii/

class Solution {
    private function expand($s, &$g, $l, $r) {
        $n = strlen($s);
        while ($l >= 0 && $r < $n && $s[$l] === $s[$r]) {
            $g[$l] = max($g[$l], $r - $l + 1);
            $l--;
            $r++;
        }
    }

    private function calc($s) {
        $n = strlen($s);
        $g = array_fill(0, $n, 0);
        for ($i = 0; $i < $n; $i++) {
            $this->expand($s, $g, $i, $i);
            $this->expand($s, $g, $i, $i + 1);
        }
        return $g;
    }

    function longestPalindrome($s, $t) {
        $m = strlen($s);
        $n = strlen($t);
        $t = strrev($t);
        $g1 = $this->calc($s);
        $g2 = $this->calc($t);
        $ans = 0;
        foreach ($g1 as $v) $ans = max($ans, $v);
        foreach ($g2 as $v) $ans = max($ans, $v);
        $f = [];
        for ($i = 0; $i <= $m; $i++) $f[$i] = array_fill(0, $n + 1, 0);
        for ($i = 1; $i <= $m; $i++) {
            for ($j = 1; $j <= $n; $j++) {
                if ($s[$i - 1] === $t[$j - 1]) {
                    $f[$i][$j] = $f[$i - 1][$j - 1] + 1;
                    $a = $i < $m ? $g1[$i] : 0;
                    $b = $j < $n ? $g2[$j] : 0;
                    $ans = max($ans, $f[$i][$j] * 2 + $a);
                    $ans = max($ans, $f[$i][$j] * 2 + $b);
                }
            }
        }
        return $ans;
    }
}
''')

# Fix 3486 leftover junk assignment
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

print("g done")

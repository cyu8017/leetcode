#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")

def w(folder, body):
    p = ROOT / folder / "solution.php"
    p.write_text(body if body.endswith("\n") else body + "\n", encoding="utf-8")
    print("wrote", folder)

w("3396_minimum_number_of_operations_to_make_elements_in_array_distinct", r'''<?php
// LeetCode 3396 - Minimum Number of Operations to Make Elements in Array Distinct
// https://leetcode.com/problems/minimum-number-of-operations-to-make-elements-in-array-distinct/

class Solution {
    function minimumOperations($nums) {
        $list = $nums;
        $ops = 0;
        while (true) {
            $seen = [];
            $dup = false;
            foreach ($list as $x) {
                if (isset($seen[$x])) { $dup = true; break; }
                $seen[$x] = true;
            }
            if (!$dup) return $ops;
            if (count($list) <= 3) return $ops + 1;
            $list = array_slice($list, 3);
            $ops++;
        }
    }
}
''')

w("3397_maximum_number_of_distinct_elements_after_operations", r'''<?php
// LeetCode 3397 - Maximum Number of Distinct Elements After Operations
// https://leetcode.com/problems/maximum-number-of-distinct-elements-after-operations/

class Solution {
    function maxDistinctElements($nums, $k) {
        sort($nums);
        $ans = 0;
        $prev = PHP_INT_MIN / 2;
        foreach ($nums as $x) {
            $cur = $x - $k;
            if ($cur <= $prev) $cur = $prev + 1;
            if ($cur > $x + $k) continue;
            $ans++;
            $prev = $cur;
        }
        return $ans;
    }
}
''')

w("3398_smallest_substring_with_identical_characters_i", r'''<?php
// LeetCode 3398 - Smallest Substring With Identical Characters I
// https://leetcode.com/problems/smallest-substring-with-identical-characters-i/

class Solution {
    function minLength($s, $numOps) {
        $n = strlen($s);
        $ok = function($L) use ($n, $s, $numOps) {
            if ($L === 0) return false;
            $ops = 0;
            for ($i = 0; $i < $n; ) {
                $j = $i;
                while ($j < $n && $s[$j] === $s[$i]) $j++;
                $ops += intdiv($j - $i, $L + 1);
                $i = $j;
            }
            return $ops <= $numOps;
        };
        $lo = 1;
        $hi = $n;
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi, 2);
            if ($ok($mid)) $hi = $mid;
            else $lo = $mid + 1;
        }
        return $lo;
    }
}
''')

w("3399_smallest_substring_with_identical_characters_ii", r'''<?php
// LeetCode 3399 - Smallest Substring With Identical Characters II
// https://leetcode.com/problems/smallest-substring-with-identical-characters-ii/

class Solution {
    function minLength($s, $numOps) {
        $n = strlen($s);
        $ok = function($L) use ($n, $s, $numOps) {
            $ops = 0;
            for ($i = 0; $i < $n; ) {
                $j = $i;
                while ($j < $n && $s[$j] === $s[$i]) $j++;
                $ops += intdiv($j - $i, $L + 1);
                $i = $j;
            }
            return $ops <= $numOps;
        };
        $lo = 1;
        $hi = $n;
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi, 2);
            if ($ok($mid)) $hi = $mid;
            else $lo = $mid + 1;
        }
        return $lo;
    }
}
''')

w("3400_maximum_number_of_matching_indices_after_right_shifts", r'''<?php
// LeetCode 3400 - Maximum Number of Matching Indices After Right Shifts
// https://leetcode.com/problems/maximum-number-of-matching-indices-after-right-shifts/

class Solution {
    function maximumMatchingIndices($nums1, $nums2) {
        $n = count($nums1);
        $ans = 0;
        for ($shift = 0; $shift < $n; $shift++) {
            $cnt = 0;
            for ($i = 0; $i < $n; $i++) {
                if ($nums1[($i - $shift + $n) % $n] === $nums2[$i]) $cnt++;
            }
            if ($cnt > $ans) $ans = $cnt;
        }
        return $ans;
    }
}
''')

w("3402_minimum_operations_to_make_columns_strictly_increasing", r'''<?php
// LeetCode 3402 - Minimum Operations to Make Columns Strictly Increasing
// https://leetcode.com/problems/minimum-operations-to-make-columns-strictly-increasing/

class Solution {
    function minimumOperations($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        $ans = 0;
        for ($j = 0; $j < $n; $j++) {
            for ($i = 1; $i < $m; $i++) {
                if ($grid[$i][$j] <= $grid[$i - 1][$j]) {
                    $need = $grid[$i - 1][$j] + 1;
                    $ans += $need - $grid[$i][$j];
                    $grid[$i][$j] = $need;
                }
            }
        }
        return $ans;
    }
}
''')

w("3403_find_the_lexicographically_largest_string_from_the_box_i", r'''<?php
// LeetCode 3403 - Find the Lexicographically Largest String From the Box I
// https://leetcode.com/problems/find-the-lexicographically-largest-string-from-the-box-i/

class Solution {
    function answerString($word, $numFriends) {
        if ($numFriends === 1) return $word;
        $n = strlen($word);
        $maxLen = $n - ($numFriends - 1);
        $ans = "";
        for ($i = 0; $i < $n; $i++) {
            $end = $i + $maxLen;
            if ($end > $n) $end = $n;
            $cand = substr($word, $i, $end - $i);
            if ($cand > $ans) $ans = $cand;
        }
        return $ans;
    }
}
''')

w("3404_count_special_subsequences", r'''<?php
// LeetCode 3404 - Count Special Subsequences
// https://leetcode.com/problems/count-special-subsequences/

class Solution {
    function numberOfSubsequences($nums) {
        $n = count($nums);
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            for ($j = $i + 2; $j < $n; $j++) {
                for ($k = $j + 2; $k < $n; $k++) {
                    for ($l = $k + 2; $l < $n; $l++) {
                        if ($nums[$i] * $nums[$k] === $nums[$j] * $nums[$l]) $ans++;
                    }
                }
            }
        }
        return $ans;
    }
}
''')

w("3405_count_the_number_of_arrays_with_k_matching_adjacent_elements", r'''<?php
// LeetCode 3405 - Count the Number of Arrays with K Matching Adjacent Elements
// https://leetcode.com/problems/count-the-number-of-arrays-with-k-matching-adjacent-elements/

class Solution {
    private $mod = 1000000007;

    private function modPow($a, $e) {
        $r = 1;
        $base = (($a % $this->mod) + $this->mod) % $this->mod;
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

    function countGoodArrays($n, $m, $k) {
        $mod = $this->mod;
        return ($this->comb($n - 1, $k) * $m % $mod * $this->modPow($m - 1, $n - 1 - $k) % $mod);
    }
}
''')

w("3406_find_the_lexicographically_largest_string_from_the_box_ii", r'''<?php
// LeetCode 3406 - Find the Lexicographically Largest String From the Box II
// https://leetcode.com/problems/find-the-lexicographically-largest-string-from-the-box-ii/

class Solution {
    function answerString($word, $numFriends) {
        if ($numFriends === 1) return $word;
        $n = strlen($word);
        $maxLen = $n - ($numFriends - 1);
        $ans = "";
        for ($i = 0; $i < $n; $i++) {
            $end = $i + $maxLen;
            if ($end > $n) $end = $n;
            $cand = substr($word, $i, $end - $i);
            if ($cand > $ans) $ans = $cand;
        }
        return $ans;
    }
}
''')

w("3407_substring_matching_pattern", r'''<?php
// LeetCode 3407 - Substring Matching Pattern
// https://leetcode.com/problems/substring-matching-pattern/

class Solution {
    function hasMatch($s, $p) {
        $i = strpos($p, '*');
        $left = substr($p, 0, $i);
        $right = substr($p, $i + 1);
        $li = $left === '' ? 0 : strpos($s, $left);
        if ($li === false) return false;
        $from = $li + strlen($left);
        if ($right === '') return true;
        return strpos($s, $right, $from) !== false;
    }
}
''')

w("3408_design_task_manager", r'''<?php
// LeetCode 3408 - Design Task Manager
// https://leetcode.com/problems/design-task-manager/

class TaskManager {
    public $pri;
    public $user;
    public $h;

    function __construct($tasks) {
        $this->pri = [];
        $this->user = [];
        $this->h = [];
        foreach ($tasks as $t) $this->add($t[0], $t[1], $t[2]);
    }

    function add($userId, $taskId, $priority) {
        $this->pri[$taskId] = $priority;
        $this->user[$taskId] = $userId;
        $this->h[] = [$priority, $taskId, $userId];
    }

    function edit($taskId, $newPriority) {
        $this->pri[$taskId] = $newPriority;
        $this->h[] = [$newPriority, $taskId, $this->user[$taskId]];
    }

    function rmv($taskId) {
        unset($this->pri[$taskId]);
        unset($this->user[$taskId]);
    }

    function execTop() {
        usort($this->h, function($a, $b) {
            if ($a[0] !== $b[0]) return $a[0] <=> $b[0];
            return $a[1] <=> $b[1];
        });
        while (count($this->h)) {
            $top = array_pop($this->h);
            $p = $this->pri[$top[1]] ?? null;
            if ($p !== null && $p === $top[0] && ($this->user[$top[1]] ?? null) === $top[2]) {
                unset($this->pri[$top[1]]);
                $uid = $this->user[$top[1]];
                unset($this->user[$top[1]]);
                return $uid;
            }
        }
        return -1;
    }
}
''')

w("3409_longest_subsequence_with_decreasing_adjacent_difference", r'''<?php
// LeetCode 3409 - Longest Subsequence With Decreasing Adjacent Difference
// https://leetcode.com/problems/longest-subsequence-with-decreasing-adjacent-difference/

class Solution {
    function longestSubsequence($nums) {
        $n = count($nums);
        $ans = 1;
        $dp = [];
        for ($i = 0; $i < $n; $i++) $dp[$i] = array_fill(0, 301, 0);
        for ($i = 0; $i < $n; $i++) {
            for ($j = 0; $j < $i; $j++) {
                $d = abs($nums[$i] - $nums[$j]);
                $best = 1;
                for ($pd = $d; $pd <= 300; $pd++) {
                    if ($dp[$j][$pd] > $best) $best = $dp[$j][$pd];
                }
                if ($best + 1 > $dp[$i][$d]) $dp[$i][$d] = $best + 1;
                if ($dp[$i][$d] > $ans) $ans = $dp[$i][$d];
            }
            if ($dp[$i][0] < 1) $dp[$i][0] = 1;
        }
        return $ans;
    }
}
''')

w("3410_maximize_subarray_sum_after_removing_all_occurrences_of_one_element", r'''<?php
// LeetCode 3410 - Maximize Subarray Sum After Removing All Occurrences of One Element
// https://leetcode.com/problems/maximize-subarray-sum-after-removing-all-occurrences-of-one-element/

class Solution {
    private function kadane($a) {
        $best = PHP_INT_MIN;
        $cur = 0;
        foreach ($a as $x) {
            $cur += $x;
            if ($cur > $best) $best = $cur;
            if ($cur < 0) $cur = 0;
        }
        $allNeg = true;
        $mx = $a[0];
        foreach ($a as $x) {
            if ($x > $mx) $mx = $x;
            if ($x >= 0) $allNeg = false;
        }
        if ($allNeg) return $mx;
        return $best;
    }

    function maxSubarraySum($nums) {
        $ans = $this->kadane($nums);
        $uniq = [];
        foreach ($nums as $x) if ($x < 0) $uniq[$x] = true;
        foreach ($uniq as $v => $_) {
            $b = [];
            foreach ($nums as $x) if ($x !== $v) $b[] = $x;
            if (count($b) === 0) continue;
            $cand = $this->kadane($b);
            if ($cand > $ans) $ans = $cand;
        }
        return $ans;
    }
}
''')

w("3411_maximum_subarray_with_equal_products", r'''<?php
// LeetCode 3411 - Maximum Subarray With Equal Products
// https://leetcode.com/problems/maximum-subarray-with-equal-products/

class Solution {
    private function gcd($a, $b) {
        while ($b !== 0) {
            $t = $a % $b;
            $a = $b;
            $b = $t;
        }
        return $a;
    }

    function maxLength($nums) {
        $n = count($nums);
        $ans = 1;
        for ($i = 0; $i < $n; $i++) {
            $prod = 1;
            $g = 0;
            $l = 1;
            for ($j = $i; $j < $n; $j++) {
                if ($prod > intdiv(1000000000, $nums[$j])) break;
                $prod *= $nums[$j];
                if ($g === 0) {
                    $g = $nums[$j];
                    $l = $nums[$j];
                } else {
                    $g = $this->gcd($g, $nums[$j]);
                    $l = intdiv($l, $this->gcd($l, $nums[$j])) * $nums[$j];
                }
                if ($prod === $l * $g && $j - $i + 1 > $ans) $ans = $j - $i + 1;
            }
        }
        return $ans;
    }
}
''')

print("batch a done")

#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
SOLUTIONS = {}


def add(folder, body):
    SOLUTIONS[folder] = body


add("2449_minimum_number_of_operations_to_make_arrays_similar", r'''<?php
// LeetCode 2449 - Minimum Number of Operations to Make Arrays Similar
// https://leetcode.com/problems/minimum-number-of-operations-to-make-arrays-similar/

class Solution {
    function makeSimilar($nums, $target) {
        sort($nums);
        sort($target);
        $oddN = [];
        $evenN = [];
        $oddT = [];
        $evenT = [];
        foreach ($nums as $x) {
            if ($x % 2 === 0) $evenN[] = $x;
            else $oddN[] = $x;
        }
        foreach ($target as $x) {
            if ($x % 2 === 0) $evenT[] = $x;
            else $oddT[] = $x;
        }
        $ans = 0;
        for ($i = 0; $i < count($oddN); $i++) {
            $diff = $oddN[$i] - $oddT[$i];
            if ($diff > 0) $ans += intdiv($diff, 2);
        }
        for ($i = 0; $i < count($evenN); $i++) {
            $diff = $evenN[$i] - $evenT[$i];
            if ($diff > 0) $ans += intdiv($diff, 2);
        }
        return $ans;
    }
}
''')

add("2450_number_of_distinct_binary_strings_after_applying_operations", r'''<?php
// LeetCode 2450 - Number of Distinct Binary Strings After Applying Operations
// https://leetcode.com/problems/number-of-distinct-binary-strings-after-applying-operations/

class Solution {
    function countDistinctStrings($s, $k) {
        $mod = 1000000007;
        $n = strlen($s);
        $ans = 1;
        for ($i = 0; $i < $n - $k + 1; $i++) $ans = ($ans * 2) % $mod;
        return $ans;
    }
}
''')

add("2451_odd_string_difference", r'''<?php
// LeetCode 2451 - Odd String Difference
// https://leetcode.com/problems/odd-string-difference/

class Solution {
    function oddString($words) {
        $diff = function ($w) {
            $b = '';
            $len = strlen($w);
            for ($i = 1; $i < $len; $i++) {
                $d = ord($w[$i]) - ord($w[$i - 1]);
                $b .= chr($d + 128) . ',';
            }
            return $b;
        };
        $d0 = $diff($words[0]);
        $d1 = $diff($words[1]);
        if ($d0 === $d1) {
            for ($i = 2; $i < count($words); $i++) {
                if ($diff($words[$i]) !== $d0) return $words[$i];
            }
        }
        if ($diff($words[2]) === $d0) return $words[1];
        return $words[0];
    }
}
''')

add("2452_words_within_two_edits_of_dictionary", r'''<?php
// LeetCode 2452 - Words Within Two Edits of Dictionary
// https://leetcode.com/problems/words-within-two-edits-of-dictionary/

class Solution {
    function twoEditWords($queries, $dictionary) {
        $ans = [];
        foreach ($queries as $q) {
            $ok = false;
            $ql = strlen($q);
            foreach ($dictionary as $d) {
                $diff = 0;
                for ($i = 0; $i < $ql; $i++) {
                    if ($q[$i] !== $d[$i]) {
                        if (++$diff > 2) break;
                    }
                }
                if ($diff <= 2) { $ok = true; break; }
            }
            if ($ok) $ans[] = $q;
        }
        return $ans;
    }
}
''')

add("2453_destroy_sequential_targets", r'''<?php
// LeetCode 2453 - Destroy Sequential Targets
// https://leetcode.com/problems/destroy-sequential-targets/

class Solution {
    function destroyTargets($nums, $space) {
        $cnt = [];
        foreach ($nums as $x) {
            $m = $x % $space;
            if (!isset($cnt[$m])) $cnt[$m] = 0;
            $cnt[$m]++;
        }
        $bestCnt = 0;
        foreach ($cnt as $c) if ($c > $bestCnt) $bestCnt = $c;
        $ans = 1000000000;
        foreach ($cnt as $key => $value) {
            if ($value === $bestCnt) {
                foreach ($nums as $x) {
                    if ($x % $space === $key && $x < $ans) $ans = $x;
                }
            }
        }
        return $ans;
    }
}
''')

add("2454_next_greater_element_iv", r'''<?php
// LeetCode 2454 - Next Greater Element IV
// https://leetcode.com/problems/next-greater-element-iv/

class Solution {
    function secondGreaterElement($nums) {
        $n = count($nums);
        $ans = array_fill(0, $n, -1);
        $stack1 = [];
        $stack2 = [];
        for ($i = 0; $i < $n; $i++) {
            $x = $nums[$i];
            while (count($stack2) && $nums[$stack2[count($stack2) - 1]] < $x) {
                $ans[array_pop($stack2)] = $x;
            }
            $tmp = [];
            while (count($stack1) && $nums[$stack1[count($stack1) - 1]] < $x) {
                $tmp[] = array_pop($stack1);
            }
            for ($j = count($tmp) - 1; $j >= 0; $j--) $stack2[] = $tmp[$j];
            $stack1[] = $i;
        }
        return $ans;
    }
}
''')

add("2455_average_value_of_even_numbers_that_are_divisible_by_three", r'''<?php
// LeetCode 2455 - Average Value of Even Numbers That Are Divisible by Three
// https://leetcode.com/problems/average-value-of-even-numbers-that-are-divisible-by-three/

class Solution {
    function averageValue($nums) {
        $sum = 0;
        $cnt = 0;
        foreach ($nums as $x) {
            if ($x % 6 === 0) {
                $sum += $x;
                $cnt++;
            }
        }
        return $cnt === 0 ? 0 : intdiv($sum, $cnt);
    }
}
''')

add("2456_most_popular_video_creator", r'''<?php
// LeetCode 2456 - Most Popular Video Creator
// https://leetcode.com/problems/most-popular-video-creator/

class Solution {
    function mostPopularCreator($creators, $ids, $views) {
        $mp = [];
        $maxTotal = 0;
        $n = count($creators);
        for ($i = 0; $i < $n; $i++) {
            $c = $creators[$i];
            if (!isset($mp[$c])) {
                $mp[$c] = ["total" => $views[$i], "bestID" => $ids[$i], "bestViews" => $views[$i]];
            } else {
                $mp[$c]["total"] += $views[$i];
                if ($views[$i] > $mp[$c]["bestViews"] ||
                    ($views[$i] === $mp[$c]["bestViews"] && $ids[$i] < $mp[$c]["bestID"])) {
                    $mp[$c]["bestViews"] = $views[$i];
                    $mp[$c]["bestID"] = $ids[$i];
                }
            }
            if ($mp[$c]["total"] > $maxTotal) $maxTotal = $mp[$c]["total"];
        }
        $ans = [];
        foreach ($mp as $creator => $info) {
            if ($info["total"] === $maxTotal) $ans[] = [$creator, $info["bestID"]];
        }
        return $ans;
    }
}
''')

add("2457_minimum_addition_to_make_integer_beautiful", r'''<?php
// LeetCode 2457 - Minimum Addition to Make Integer Beautiful
// https://leetcode.com/problems/minimum-addition-to-make-integer-beautiful/

class Solution {
    function makeIntegerBeautiful($n, $target) {
        $digitSum = function ($x) {
            $s = 0;
            while ($x > 0) {
                $s += $x % 10;
                $x = intdiv($x, 10);
            }
            return $s;
        };
        $orig = $n;
        $pow10 = 1;
        while ($digitSum($n) > $target) {
            $n = intdiv($n, 10) + 1;
            $pow10 *= 10;
        }
        return $n * $pow10 - $orig;
    }
}
''')

add("2458_height_of_binary_tree_after_subtree_removal_queries", r'''<?php
// LeetCode 2458 - Height of Binary Tree After Subtree Removal Queries
// https://leetcode.com/problems/height-of-binary-tree-after-subtree-removal-queries/

class TreeNode {
    public $val = 0;
    public $left = null;
    public $right = null;
    function __construct($val = 0, $left = null, $right = null) {
        $this->val = $val;
        $this->left = $left;
        $this->right = $right;
    }
}

class Solution {
    function treeQueries($root, $queries) {
        $height = [];
        $level = [];
        $levelMax = [];
        $dfs = function ($node, $d) use (&$dfs, &$height, &$level, &$levelMax) {
            if ($node === null) return -1;
            $level[$node->val] = $d;
            $h = 1 + max($dfs($node->left, $d + 1), $dfs($node->right, $d + 1));
            $height[$node->val] = $h;
            if (!isset($levelMax[$d])) $levelMax[$d] = [];
            $arr =& $levelMax[$d];
            if (count($arr) === 0) $arr[] = $h;
            elseif ($h >= $arr[0]) {
                if (count($arr) === 1) $arr[] = $arr[0];
                else $arr[1] = $arr[0];
                $arr[0] = $h;
            } elseif (count($arr) === 1 || $h > $arr[1]) {
                if (count($arr) === 1) $arr[] = $h;
                else $arr[1] = $h;
            }
            unset($arr);
            return $h;
        };
        $dfs($root, 0);
        $ans = array_fill(0, count($queries), 0);
        for ($i = 0; $i < count($queries); $i++) {
            $q = $queries[$i];
            $d = $level[$q];
            $h = $height[$q];
            $top = $levelMax[$d];
            if ($top[0] === $h) {
                if (count($top) > 1) $ans[$i] = $d + $top[1];
                else $ans[$i] = $d - 1;
            } else {
                $ans[$i] = $d + $top[0];
            }
        }
        return $ans;
    }
}
''')

add("2459_sort_array_by_moving_items_to_empty_space", r'''<?php
// LeetCode 2459 - Sort Array By Moving Items to Empty Space
// https://leetcode.com/problems/sort-array-by-moving-items-to-empty-space/

class Solution {
    function sortArray($nums) {
        $solveOne = function ($startZero) use ($nums) {
            $n = count($nums);
            $arr = $nums;
            $pos = [];
            for ($i = 0; $i < $n; $i++) $pos[$arr[$i]] = $i;
            $ops = 0;
            while (true) {
                $empty = $pos[0];
                $should = $startZero ? $empty : ($empty === $n - 1 ? 0 : $empty + 1);
                if ($arr[$empty] === $should) {
                    $found = -1;
                    for ($i = 0; $i < $n; $i++) {
                        $want = $startZero ? $i : ($i === $n - 1 ? 0 : $i + 1);
                        if ($arr[$i] !== $want) { $found = $i; break; }
                    }
                    if ($found === -1) return $ops;
                    $v = $arr[$found];
                    $arr[$empty] = $arr[$found];
                    $arr[$found] = 0;
                    $pos[0] = $found;
                    $pos[$v] = $empty;
                    $ops++;
                    continue;
                }
                $j = $pos[$should];
                $vv = $arr[$j];
                $arr[$empty] = $arr[$j];
                $arr[$j] = 0;
                $pos[0] = $j;
                $pos[$vv] = $empty;
                $ops++;
            }
        };
        return min($solveOne(true), $solveOne(false));
    }
}
''')

add("2460_apply_operations_to_an_array", r'''<?php
// LeetCode 2460 - Apply Operations to an Array
// https://leetcode.com/problems/apply-operations-to-an-array/

class Solution {
    function applyOperations($nums) {
        $n = count($nums);
        $a = $nums;
        for ($i = 0; $i + 1 < $n; $i++) {
            if ($a[$i] === $a[$i + 1]) {
                $a[$i] *= 2;
                $a[$i + 1] = 0;
            }
        }
        $ans = array_fill(0, $n, 0);
        $j = 0;
        foreach ($a as $x) if ($x !== 0) $ans[$j++] = $x;
        return $ans;
    }
}
''')

add("2461_maximum_sum_of_distinct_subarrays_with_length_k", r'''<?php
// LeetCode 2461 - Maximum Sum of Distinct Subarrays With Length K
// https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/

class Solution {
    function maximumSubarraySum($nums, $k) {
        $cnt = [];
        $sum = 0;
        $ans = 0;
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            $sum += $nums[$i];
            if (!isset($cnt[$nums[$i]])) $cnt[$nums[$i]] = 0;
            $cnt[$nums[$i]]++;
            if ($i >= $k) {
                $y = $nums[$i - $k];
                $sum -= $y;
                $c = $cnt[$y] - 1;
                if ($c === 0) unset($cnt[$y]);
                else $cnt[$y] = $c;
            }
            if ($i >= $k - 1 && count($cnt) === $k && $sum > $ans) $ans = $sum;
        }
        return $ans;
    }
}
''')

add("2462_total_cost_to_hire_k_workers", r'''<?php
// LeetCode 2462 - Total Cost to Hire K Workers
// https://leetcode.com/problems/total-cost-to-hire-k-workers/

class Solution {
    function totalCost($costs, $k, $candidates) {
        $leftH = new SplPriorityQueue();
        $rightH = new SplPriorityQueue();
        $n = count($costs);
        $l = 0;
        $r = $n - 1;
        while ($l <= $r && $leftH->count() < $candidates) {
            $leftH->insert([$costs[$l], $l], [-$costs[$l], -$l]);
            $l++;
        }
        while ($r >= $l && $rightH->count() < $candidates) {
            $rightH->insert([$costs[$r], $r], [-$costs[$r], -$r]);
            $r--;
        }
        $ans = 0;
        for ($t = 0; $t < $k; $t++) {
            $useLeft = false;
            if (!$leftH->isEmpty() && !$rightH->isEmpty()) {
                $lt = $leftH->top();
                $rt = $rightH->top();
                if ($lt[0] < $rt[0] || ($lt[0] === $rt[0] && $lt[1] <= $rt[1])) $useLeft = true;
            } elseif (!$leftH->isEmpty()) {
                $useLeft = true;
            }
            if ($useLeft) {
                $ans += $leftH->extract()[0];
                if ($l <= $r) {
                    $leftH->insert([$costs[$l], $l], [-$costs[$l], -$l]);
                    $l++;
                }
            } else {
                $ans += $rightH->extract()[0];
                if ($l <= $r) {
                    $rightH->insert([$costs[$r], $r], [-$costs[$r], -$r]);
                    $r--;
                }
            }
        }
        return $ans;
    }
}
''')

add("2463_minimum_total_distance_traveled", r'''<?php
// LeetCode 2463 - Minimum Total Distance Traveled
// https://leetcode.com/problems/minimum-total-distance-traveled/

class Solution {
    function minimumTotalDistance($robot, $factory) {
        $robots = $robot;
        sort($robots);
        usort($factory, function ($a, $b) { return $a[0] <=> $b[0]; });
        $m = count($robots);
        $pos = [];
        foreach ($factory as $f) {
            for ($c = 0; $c < $f[1]; $c++) $pos[] = $f[0];
        }
        $n = count($pos);
        $INF = intdiv(PHP_INT_MAX, 4);
        $dp = [];
        for ($i = 0; $i <= $m; $i++) $dp[] = array_fill(0, $n + 1, $INF);
        for ($j = 0; $j <= $n; $j++) $dp[0][$j] = 0;
        for ($i = 1; $i <= $m; $i++) {
            for ($j = $i; $j <= $n; $j++) {
                $dp[$i][$j] = $dp[$i][$j - 1];
                $diff = $robots[$i - 1] - $pos[$j - 1];
                if ($diff < 0) $diff = -$diff;
                if ($dp[$i - 1][$j - 1] + $diff < $dp[$i][$j]) $dp[$i][$j] = $dp[$i - 1][$j - 1] + $diff;
            }
        }
        return $dp[$m][$n];
    }
}
''')

add("2464_minimum_subarrays_in_a_valid_split", r'''<?php
// LeetCode 2464 - Minimum Subarrays in a Valid Split
// https://leetcode.com/problems/minimum-subarrays-in-a-valid-split/

class Solution {
    function validSubarraySplit($nums) {
        $gcd = function ($a, $b) {
            while ($b !== 0) {
                $t = $a % $b;
                $a = $b;
                $b = $t;
            }
            return $a;
        };
        $n = count($nums);
        $INF = 1 << 30;
        $dp = array_fill(0, $n + 1, $INF);
        $dp[0] = 0;
        for ($i = 0; $i < $n; $i++) {
            if ($dp[$i] >= $INF) continue;
            for ($j = $i; $j < $n; $j++) {
                if ($gcd($nums[$i], $nums[$j]) > 1) {
                    if ($dp[$i] + 1 < $dp[$j + 1]) $dp[$j + 1] = $dp[$i] + 1;
                }
            }
        }
        return $dp[$n] >= $INF ? -1 : $dp[$n];
    }
}
''')

add("2465_number_of_distinct_averages", r'''<?php
// LeetCode 2465 - Number of Distinct Averages
// https://leetcode.com/problems/number-of-distinct-averages/

class Solution {
    function distinctAverages($nums) {
        sort($nums);
        $seen = [];
        $l = 0;
        $r = count($nums) - 1;
        while ($l < $r) {
            $seen[$nums[$l] + $nums[$r]] = true;
            $l++;
            $r--;
        }
        return count($seen);
    }
}
''')

add("2466_count_ways_to_build_good_strings", r'''<?php
// LeetCode 2466 - Count Ways To Build Good Strings
// https://leetcode.com/problems/count-ways-to-build-good-strings/

class Solution {
    function countGoodStrings($low, $high, $zero, $one) {
        $mod = 1000000007;
        $dp = array_fill(0, $high + 1, 0);
        $dp[0] = 1;
        $ans = 0;
        for ($i = 1; $i <= $high; $i++) {
            if ($i >= $zero) $dp[$i] = ($dp[$i] + $dp[$i - $zero]) % $mod;
            if ($i >= $one) $dp[$i] = ($dp[$i] + $dp[$i - $one]) % $mod;
            if ($i >= $low) $ans = ($ans + $dp[$i]) % $mod;
        }
        return $ans;
    }
}
''')

add("2467_most_profitable_path_in_a_tree", r'''<?php
// LeetCode 2467 - Most Profitable Path in a Tree
// https://leetcode.com/problems/most-profitable-path-in-a-tree/

class Solution {
    function mostProfitablePath($edges, $bob, $amount) {
        $n = count($amount);
        $g = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $g[$e[0]][] = $e[1];
            $g[$e[1]][] = $e[0];
        }
        $bobTime = array_fill(0, $n, $n);
        $findBob = function ($u, $p, $t) use (&$findBob, &$g, &$bobTime) {
            if ($u === 0) {
                $bobTime[$u] = $t;
                return true;
            }
            foreach ($g[$u] as $v) {
                if ($v === $p) continue;
                if ($findBob($v, $u, $t + 1)) {
                    $bobTime[$u] = $t;
                    return true;
                }
            }
            return false;
        };
        $findBob($bob, -1, 0);
        $ans = PHP_INT_MIN;
        $dfs = function ($u, $p, $t, $income) use (&$dfs, &$g, $amount, &$bobTime, &$ans) {
            $cur = $amount[$u];
            if ($t > $bobTime[$u]) $cur = 0;
            elseif ($t === $bobTime[$u]) $cur = intdiv($cur, 2);
            $income += $cur;
            $isLeaf = true;
            foreach ($g[$u] as $v) {
                if ($v !== $p) {
                    $isLeaf = false;
                    $dfs($v, $u, $t + 1, $income);
                }
            }
            if ($isLeaf && $income > $ans) $ans = $income;
        };
        $dfs(0, -1, 0, 0);
        return $ans;
    }
}
''')

add("2468_split_message_based_on_limit", r'''<?php
// LeetCode 2468 - Split Message Based on Limit
// https://leetcode.com/problems/split-message-based-on-limit/

class Solution {
    function splitMessage($message, $limit) {
        $n = strlen($message);
        for ($parts = 1; $parts <= $n; $parts++) {
            $sbDigits = strlen((string)$parts);
            $ok = true;
            $idx = 0;
            $res = [];
            for ($i = 1; $i <= $parts; $i++) {
                $tail = 3 + strlen((string)$i) + $sbDigits;
                $cap = $limit - $tail;
                if ($cap <= 0 || $idx >= $n) { $ok = false; break; }
                $take = $cap;
                if ($take > $n - $idx) $take = $n - $idx;
                $res[] = substr($message, $idx, $take) . '<' . $i . '/' . $parts . '>';
                $idx += $take;
            }
            if ($ok && $idx === $n) return $res;
        }
        return [];
    }
}
''')

add("2469_convert_the_temperature", r'''<?php
// LeetCode 2469 - Convert the Temperature
// https://leetcode.com/problems/convert-the-temperature/

class Solution {
    function convertTemperature($celsius) {
        return [$celsius + 273.15, $celsius * 1.80 + 32.00];
    }
}
''')

add("2470_number_of_subarrays_with_lcm_equal_to_k", r'''<?php
// LeetCode 2470 - Number of Subarrays With LCM Equal to K
// https://leetcode.com/problems/number-of-subarrays-with-lcm-equal-to-k/

class Solution {
    function subarrayLCM($nums, $k) {
        $gcd = function ($a, $b) {
            while ($b !== 0) {
                $t = $a % $b;
                $a = $b;
                $b = $t;
            }
            return $a;
        };
        $ans = 0;
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            $cur = 1;
            for ($j = $i; $j < $n; $j++) {
                $cur = intdiv($cur, $gcd($cur, $nums[$j])) * $nums[$j];
                if ($cur > $k) break;
                if ($cur === $k) $ans++;
            }
        }
        return $ans;
    }
}
''')

add("2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level", r'''<?php
// LeetCode 2471 - Minimum Number of Operations to Sort a Binary Tree by Level
// https://leetcode.com/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level/

class TreeNode {
    public $val = 0;
    public $left = null;
    public $right = null;
    function __construct($val = 0, $left = null, $right = null) {
        $this->val = $val;
        $this->left = $left;
        $this->right = $right;
    }
}

class Solution {
    function minimumOperations($root) {
        if ($root === null) return 0;
        $ans = 0;
        $q = [$root];
        while (count($q)) {
            $sz = count($q);
            $vals = array_fill(0, $sz, 0);
            for ($i = 0; $i < $sz; $i++) {
                $node = array_shift($q);
                $vals[$i] = $node->val;
                if ($node->left !== null) $q[] = $node->left;
                if ($node->right !== null) $q[] = $node->right;
            }
            $sorted = $vals;
            sort($sorted);
            $pos = [];
            for ($i = 0; $i < $sz; $i++) $pos[$vals[$i]] = $i;
            for ($i = 0; $i < $sz; $i++) {
                if ($vals[$i] !== $sorted[$i]) {
                    $j = $pos[$sorted[$i]];
                    $tmp = $vals[$i];
                    $vals[$i] = $vals[$j];
                    $vals[$j] = $tmp;
                    $pos[$vals[$j]] = $j;
                    $pos[$vals[$i]] = $i;
                    $ans++;
                }
            }
        }
        return $ans;
    }
}
''')

add("2472_maximum_number_of_non_overlapping_palindrome_substrings", r'''<?php
// LeetCode 2472 - Maximum Number of Non-overlapping Palindrome Substrings
// https://leetcode.com/problems/maximum-number-of-non-overlapping-palindrome-substrings/

class Solution {
    function maxPalindromes($s, $k) {
        $n = strlen($s);
        $isPal = [];
        for ($i = 0; $i < $n; $i++) $isPal[] = array_fill(0, $n, false);
        for ($i = 0; $i < $n; $i++) $isPal[$i][$i] = true;
        for ($i = 0; $i + 1 < $n; $i++) $isPal[$i][$i + 1] = $s[$i] === $s[$i + 1];
        for ($length = 3; $length <= $n; $length++) {
            for ($i = 0; $i + $length - 1 < $n; $i++) {
                $j = $i + $length - 1;
                $isPal[$i][$j] = $s[$i] === $s[$j] && $isPal[$i + 1][$j - 1];
            }
        }
        $dp = array_fill(0, $n + 1, 0);
        for ($i = $n - 1; $i >= 0; $i--) {
            $dp[$i] = $dp[$i + 1];
            for ($j = $i + $k - 1; $j < $n; $j++) {
                if ($isPal[$i][$j] && 1 + $dp[$j + 1] > $dp[$i]) $dp[$i] = 1 + $dp[$j + 1];
            }
        }
        return $dp[0];
    }
}
''')

add("2473_minimum_cost_to_buy_apples", r'''<?php
// LeetCode 2473 - Minimum Cost to Buy Apples
// https://leetcode.com/problems/minimum-cost-to-buy-apples/

class Solution {
    function minCost($n, $roads, $appleCost, $k) {
        $g = array_fill(0, $n + 1, []);
        foreach ($roads as $r) {
            $g[$r[0]][] = [$r[1], $r[2]];
            $g[$r[1]][] = [$r[0], $r[2]];
        }
        $ans = array_fill(0, $n, 0);
        $INF = intdiv(PHP_INT_MAX, 4);
        for ($start = 1; $start <= $n; $start++) {
            $dist = array_fill(0, $n + 1, $INF);
            $dist[$start] = 0;
            $pq = new SplPriorityQueue();
            $pq->insert([$start, 0], 0);
            while (!$pq->isEmpty()) {
                $cur = $pq->extract();
                $u = $cur[0];
                $d = $cur[1];
                if ($d !== $dist[$u]) continue;
                foreach ($g[$u] as $e) {
                    $v = $e[0];
                    $w = $e[1];
                    $nd = $d + $w;
                    if ($nd < $dist[$v]) {
                        $dist[$v] = $nd;
                        $pq->insert([$v, $nd], -$nd);
                    }
                }
            }
            $best = $INF;
            for ($city = 1; $city <= $n; $city++) {
                $cost = $dist[$city] * ($k + 1) + $appleCost[$city - 1];
                if ($cost < $best) $best = $cost;
            }
            $ans[$start - 1] = $best;
        }
        return $ans;
    }
}
''')

add("2475_number_of_unequal_triplets_in_array", r'''<?php
// LeetCode 2475 - Number of Unequal Triplets in Array
// https://leetcode.com/problems/number-of-unequal-triplets-in-array/

class Solution {
    function unequalTriplets($nums) {
        $cnt = [];
        foreach ($nums as $x) {
            if (!isset($cnt[$x])) $cnt[$x] = 0;
            $cnt[$x]++;
        }
        $ans = 0;
        $left = 0;
        $n = count($nums);
        foreach ($cnt as $c) {
            $right = $n - $left - $c;
            $ans += $left * $c * $right;
            $left += $c;
        }
        return $ans;
    }
}
''')

add("2476_closest_nodes_queries_in_a_binary_search_tree", r'''<?php
// LeetCode 2476 - Closest Nodes Queries in a Binary Search Tree
// https://leetcode.com/problems/closest-nodes-queries-in-a-binary-search-tree/

class TreeNode {
    public $val = 0;
    public $left = null;
    public $right = null;
    function __construct($val = 0, $left = null, $right = null) {
        $this->val = $val;
        $this->left = $left;
        $this->right = $right;
    }
}

class Solution {
    function closestNodes($root, $queries) {
        $vals = [];
        $inorder = function ($node) use (&$inorder, &$vals) {
            if ($node === null) return;
            $inorder($node->left);
            $vals[] = $node->val;
            $inorder($node->right);
        };
        $inorder($root);
        $lowerBound = function ($q) use ($vals) {
            $lo = 0;
            $hi = count($vals);
            while ($lo < $hi) {
                $mid = ($lo + $hi) >> 1;
                if ($vals[$mid] < $q) $lo = $mid + 1;
                else $hi = $mid;
            }
            return $lo;
        };
        $ans = [];
        foreach ($queries as $q) {
            $j = $lowerBound($q);
            $mx = $j < count($vals) ? $vals[$j] : -1;
            $mn = -1;
            if ($j < count($vals) && $vals[$j] === $q) $mn = $q;
            elseif ($j > 0) $mn = $vals[$j - 1];
            $ans[] = [$mn, $mx];
        }
        return $ans;
    }
}
''')

add("2477_minimum_fuel_cost_to_report_to_the_capital", r'''<?php
// LeetCode 2477 - Minimum Fuel Cost to Report to the Capital
// https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital/

class Solution {
    function minimumFuelCost($roads, $seats) {
        $n = count($roads) + 1;
        $g = array_fill(0, $n, []);
        foreach ($roads as $e) {
            $g[$e[0]][] = $e[1];
            $g[$e[1]][] = $e[0];
        }
        $ans = 0;
        $dfs = function ($u, $p) use (&$dfs, &$g, $seats, &$ans) {
            $people = 1;
            foreach ($g[$u] as $v) {
                if ($v !== $p) $people += $dfs($v, $u);
            }
            if ($u !== 0) $ans += intdiv($people + $seats - 1, $seats);
            return $people;
        };
        $dfs(0, -1);
        return $ans;
    }
}
''')

add("2478_number_of_beautiful_partitions", r'''<?php
// LeetCode 2478 - Number of Beautiful Partitions
// https://leetcode.com/problems/number-of-beautiful-partitions/

class Solution {
    function beautifulPartitions($s, $k, $minLength) {
        $mod = 1000000007;
        $isPrime = function ($c) {
            return $c === '2' || $c === '3' || $c === '5' || $c === '7';
        };
        $n = strlen($s);
        if (!$isPrime($s[0]) || $isPrime($s[$n - 1])) return 0;
        $dp = [];
        for ($p = 0; $p <= $k; $p++) $dp[] = array_fill(0, $n + 1, 0);
        $dp[0][0] = 1;
        for ($p = 1; $p <= $k; $p++) {
            $pref = 0;
            $j = 0;
            for ($i = 1; $i <= $n; $i++) {
                while ($j <= $i - $minLength) {
                    if ($j === 0 || ($isPrime($s[$j]) && !$isPrime($s[$j - 1]))) {
                        $pref = ($pref + $dp[$p - 1][$j]) % $mod;
                    }
                    $j++;
                }
                if (!$isPrime($s[$i - 1])) $dp[$p][$i] = $pref;
            }
        }
        return $dp[$k][$n];
    }
}
''')

written = 0
for folder, body in SOLUTIONS.items():
    path = ROOT / folder / "solution.php"
    path.write_text(body, encoding="utf-8", newline="\n")
    written += 1
print(f"wrote {written}")

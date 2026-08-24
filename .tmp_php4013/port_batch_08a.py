#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
SOLUTIONS = {}


def add(folder, body):
    SOLUTIONS[folder] = body


TREE = """class TreeNode {
    public $val = 0;
    public $left = null;
    public $right = null;
    function __construct($val = 0, $left = null, $right = null) {
        $this->val = $val;
        $this->left = $left;
        $this->right = $right;
    }
}
"""

LISTN = """class ListNode {
    public $val = 0;
    public $next = null;
    function __construct($val = 0, $next = null) {
        $this->val = $val;
        $this->next = $next;
    }
}
"""

add("2416_sum_of_prefix_scores_of_strings", r'''<?php
// LeetCode 2416 - Sum of Prefix Scores of Strings
// https://leetcode.com/problems/sum-of-prefix-scores-of-strings/

class Solution {
    function sumPrefixScores($words) {
        $root = ["child" => array_fill(0, 26, null), "cnt" => 0];
        foreach ($words as $w) {
            $cur =& $root;
            $len = strlen($w);
            for ($i = 0; $i < $len; $i++) {
                $c = ord($w[$i]) - 97;
                if ($cur["child"][$c] === null) {
                    $cur["child"][$c] = ["child" => array_fill(0, 26, null), "cnt" => 0];
                }
                $cur =& $cur["child"][$c];
                $cur["cnt"]++;
            }
            unset($cur);
        }
        $n = count($words);
        $ans = array_fill(0, $n, 0);
        for ($i = 0; $i < $n; $i++) {
            $cur = $root;
            $sum = 0;
            $w = $words[$i];
            $len = strlen($w);
            for ($j = 0; $j < $len; $j++) {
                $cur = $cur["child"][ord($w[$j]) - 97];
                $sum += $cur["cnt"];
            }
            $ans[$i] = $sum;
        }
        return $ans;
    }
}
''')

add("2417_closest_fair_integer", r'''<?php
// LeetCode 2417 - Closest Fair Integer
// https://leetcode.com/problems/closest-fair-integer/

class Solution {
    function closestFair($n) {
        for ($x = $n; ; $x++) {
            $s = (string)$x;
            $len = strlen($s);
            if ($len % 2 !== 0) {
                $p = 1;
                for ($i = 0; $i < $len; $i++) $p *= 10;
                return $this->closestFair($p);
            }
            $even = 0;
            $odd = 0;
            for ($i = 0; $i < $len; $i++) {
                if ((ord($s[$i]) - 48) % 2 === 0) $even++;
                else $odd++;
            }
            if ($even === $odd) return $x;
        }
    }
}
''')

add("2418_sort_the_people", r'''<?php
// LeetCode 2418 - Sort the People
// https://leetcode.com/problems/sort-the-people/

class Solution {
    function sortPeople($names, $heights) {
        $n = count($names);
        $idx = range(0, $n - 1);
        usort($idx, function ($a, $b) use ($heights) {
            return $heights[$b] <=> $heights[$a];
        });
        $ans = [];
        foreach ($idx as $i) $ans[] = $names[$i];
        return $ans;
    }
}
''')

add("2419_longest_subarray_with_maximum_bitwise_and", r'''<?php
// LeetCode 2419 - Longest Subarray With Maximum Bitwise AND
// https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/

class Solution {
    function longestSubarray($nums) {
        $mx = $nums[0];
        foreach ($nums as $x) if ($x > $mx) $mx = $x;
        $ans = 0;
        $cur = 0;
        foreach ($nums as $x) {
            if ($x === $mx) {
                $cur++;
                if ($cur > $ans) $ans = $cur;
            } else $cur = 0;
        }
        return $ans;
    }
}
''')

add("2420_find_all_good_indices", r'''<?php
// LeetCode 2420 - Find All Good Indices
// https://leetcode.com/problems/find-all-good-indices/

class Solution {
    function goodIndices($nums, $k) {
        $n = count($nums);
        $dec = array_fill(0, $n, 0);
        $inc = array_fill(0, $n, 0);
        $dec[0] = 1;
        for ($i = 1; $i < $n; $i++)
            $dec[$i] = $nums[$i] <= $nums[$i - 1] ? $dec[$i - 1] + 1 : 1;
        $inc[$n - 1] = 1;
        for ($i = $n - 2; $i >= 0; $i--)
            $inc[$i] = $nums[$i] <= $nums[$i + 1] ? $inc[$i + 1] + 1 : 1;
        $ans = [];
        for ($i = $k; $i < $n - $k; $i++) {
            if ($dec[$i - 1] >= $k && $inc[$i + 1] >= $k) $ans[] = $i;
        }
        return $ans;
    }
}
''')

add("2421_number_of_good_paths", r'''<?php
// LeetCode 2421 - Number of Good Paths
// https://leetcode.com/problems/number-of-good-paths/

class Solution {
    function numberOfGoodPaths($vals, $edges) {
        $n = count($vals);
        $g = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $g[$e[0]][] = $e[1];
            $g[$e[1]][] = $e[0];
        }
        $parent = range(0, $n - 1);
        $size = array_fill(0, $n, 1);
        $find = function ($x) use (&$find, &$parent) {
            if ($parent[$x] !== $x) $parent[$x] = $find($parent[$x]);
            return $parent[$x];
        };
        $nodes = range(0, $n - 1);
        usort($nodes, function ($a, $b) use ($vals) {
            return $vals[$a] <=> $vals[$b];
        });
        $ans = $n;
        for ($i = 0; $i < $n; ) {
            $j = $i;
            while ($j < $n && $vals[$nodes[$j]] === $vals[$nodes[$i]]) $j++;
            for ($k = $i; $k < $j; $k++) {
                $u = $nodes[$k];
                foreach ($g[$u] as $v) {
                    if ($vals[$v] <= $vals[$u]) {
                        $ru = $find($u);
                        $rv = $find($v);
                        if ($ru !== $rv) {
                            $parent[$ru] = $rv;
                            $size[$rv] += $size[$ru];
                        }
                    }
                }
            }
            $freq = [];
            for ($k = $i; $k < $j; $k++) {
                $r = $find($nodes[$k]);
                if (!isset($freq[$r])) $freq[$r] = 0;
                $freq[$r]++;
            }
            foreach ($freq as $c) $ans += intdiv($c * ($c - 1), 2);
            $i = $j;
        }
        return $ans;
    }
}
''')

add("2422_merge_operations_to_turn_array_into_a_palindrome", r'''<?php
// LeetCode 2422 - Merge Operations to Turn Array Into a Palindrome
// https://leetcode.com/problems/merge-operations-to-turn-array-into-a-palindrome/

class Solution {
    function minimumOperations($nums) {
        $l = 0;
        $r = count($nums) - 1;
        $left = $nums[$l];
        $right = $nums[$r];
        $ans = 0;
        while ($l < $r) {
            if ($left === $right) {
                $l++;
                $r--;
                if ($l < $r) {
                    $left = $nums[$l];
                    $right = $nums[$r];
                }
            } elseif ($left < $right) {
                $l++;
                $left += $nums[$l];
                $ans++;
            } else {
                $r--;
                $right += $nums[$r];
                $ans++;
            }
        }
        return $ans;
    }
}
''')

add("2423_remove_letter_to_equalize_frequency", r'''<?php
// LeetCode 2423 - Remove Letter To Equalize Frequency
// https://leetcode.com/problems/remove-letter-to-equalize-frequency/

class Solution {
    function equalFrequency($word) {
        $n = strlen($word);
        for ($skip = 0; $skip < $n; $skip++) {
            $cnt = array_fill(0, 26, 0);
            for ($i = 0; $i < $n; $i++) {
                if ($i === $skip) continue;
                $cnt[ord($word[$i]) - 97]++;
            }
            $freq = [];
            foreach ($cnt as $c) {
                if ($c > 0) {
                    if (!isset($freq[$c])) $freq[$c] = 0;
                    $freq[$c]++;
                }
            }
            if (count($freq) === 1) return true;
        }
        return false;
    }
}
''')

add("2424_longest_uploaded_prefix", r'''<?php
// LeetCode 2424 - Longest Uploaded Prefix
// https://leetcode.com/problems/longest-uploaded-prefix/

class LUPrefix {
    private $uploaded;
    private $prefixLen;

    function __construct($n) {
        $this->uploaded = array_fill(0, $n + 2, false);
        $this->prefixLen = 0;
    }

    function upload($video) {
        $this->uploaded[$video] = true;
        while ($this->uploaded[$this->prefixLen + 1]) $this->prefixLen++;
    }

    function longest() {
        return $this->prefixLen;
    }
}
''')

add("2425_bitwise_xor_of_all_pairings", r'''<?php
// LeetCode 2425 - Bitwise XOR of All Pairings
// https://leetcode.com/problems/bitwise-xor-of-all-pairings/

class Solution {
    function xorAllNums($nums1, $nums2) {
        $ans = 0;
        if (count($nums2) % 2 === 1) foreach ($nums1 as $x) $ans ^= $x;
        if (count($nums1) % 2 === 1) foreach ($nums2 as $x) $ans ^= $x;
        return $ans;
    }
}
''')

add("2426_number_of_pairs_satisfying_inequality", r'''<?php
// LeetCode 2426 - Number of Pairs Satisfying Inequality
// https://leetcode.com/problems/number-of-pairs-satisfying-inequality/

class Solution {
    function numberOfPairs($nums1, $nums2, $diff) {
        $n = count($nums1);
        $arr = array_fill(0, $n, 0);
        $tmp = array_fill(0, $n, 0);
        for ($i = 0; $i < $n; $i++) $arr[$i] = $nums1[$i] - $nums2[$i];
        $mergeCount = function ($l, $r) use (&$mergeCount, &$arr, &$tmp, $diff) {
            if ($r - $l <= 1) return 0;
            $m = ($l + $r) >> 1;
            $ans = $mergeCount($l, $m) + $mergeCount($m, $r);
            $j = $m;
            for ($i = $l; $i < $m; $i++) {
                while ($j < $r && $arr[$j] < $arr[$i] - $diff) $j++;
                $ans += $r - $j;
            }
            $p = $l;
            $q = $m;
            $i2 = $l;
            while ($p < $m && $q < $r) {
                if ($arr[$p] <= $arr[$q]) $tmp[$i2++] = $arr[$p++];
                else $tmp[$i2++] = $arr[$q++];
            }
            while ($p < $m) $tmp[$i2++] = $arr[$p++];
            while ($q < $r) $tmp[$i2++] = $arr[$q++];
            for ($t = $l; $t < $r; $t++) $arr[$t] = $tmp[$t];
            return $ans;
        };
        return $mergeCount(0, $n);
    }
}
''')

add("2427_number_of_common_factors", r'''<?php
// LeetCode 2427 - Number of Common Factors
// https://leetcode.com/problems/number-of-common-factors/

class Solution {
    function commonFactors($a, $b) {
        $gcd = function ($x, $y) {
            while ($y !== 0) {
                $t = $x % $y;
                $x = $y;
                $y = $t;
            }
            return $x;
        };
        $g = $gcd($a, $b);
        $ans = 0;
        for ($i = 1; $i * $i <= $g; $i++) {
            if ($g % $i === 0) {
                $ans++;
                if ($i * $i !== $g) $ans++;
            }
        }
        return $ans;
    }
}
''')

add("2428_maximum_sum_of_an_hourglass", r'''<?php
// LeetCode 2428 - Maximum Sum of an Hourglass
// https://leetcode.com/problems/maximum-sum-of-an-hourglass/

class Solution {
    function maxSum($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        $ans = PHP_INT_MIN;
        for ($i = 0; $i + 2 < $m; $i++) {
            for ($j = 0; $j + 2 < $n; $j++) {
                $s = $grid[$i][$j] + $grid[$i][$j + 1] + $grid[$i][$j + 2]
                    + $grid[$i + 1][$j + 1]
                    + $grid[$i + 2][$j] + $grid[$i + 2][$j + 1] + $grid[$i + 2][$j + 2];
                if ($s > $ans) $ans = $s;
            }
        }
        return $ans;
    }
}
''')

add("2429_minimize_xor", r'''<?php
// LeetCode 2429 - Minimize XOR
// https://leetcode.com/problems/minimize-xor/

class Solution {
    function minimizeXor($num1, $num2) {
        $bits = 0;
        for ($x = $num2; $x !== 0; $x &= $x - 1) $bits++;
        $ans = 0;
        for ($i = 31; $i >= 0 && $bits > 0; $i--) {
            if ((($num1 >> $i) & 1) !== 0) {
                $ans |= 1 << $i;
                $bits--;
            }
        }
        for ($i = 0; $i < 32 && $bits > 0; $i++) {
            if ((($ans >> $i) & 1) === 0) {
                $ans |= 1 << $i;
                $bits--;
            }
        }
        return $ans;
    }
}
''')

add("2430_maximum_deletions_on_a_string", r'''<?php
// LeetCode 2430 - Maximum Deletions on a String
// https://leetcode.com/problems/maximum-deletions-on-a-string/

class Solution {
    function deleteString($s) {
        $n = strlen($s);
        $lcp = [];
        for ($i = 0; $i <= $n; $i++) $lcp[] = array_fill(0, $n + 1, 0);
        for ($i = $n - 1; $i >= 0; $i--) {
            for ($j = $n - 1; $j >= 0; $j--) {
                if ($s[$i] === $s[$j]) $lcp[$i][$j] = $lcp[$i + 1][$j + 1] + 1;
            }
        }
        $dp = array_fill(0, $n, 0);
        for ($i = $n - 1; $i >= 0; $i--) {
            $dp[$i] = 1;
            for ($len = 1; $i + 2 * $len <= $n; $len++) {
                if ($lcp[$i][$i + $len] >= $len) $dp[$i] = max($dp[$i], 1 + $dp[$i + $len]);
            }
        }
        return $dp[0];
    }
}
''')

add("2431_maximize_total_tastiness_of_purchased_fruits", r'''<?php
// LeetCode 2431 - Maximize Total Tastiness of Purchased Fruits
// https://leetcode.com/problems/maximize-total-tastiness-of-purchased-fruits/

class Solution {
    function maxTastiness($price, $tastiness, $maxAmount, $maxCoupons) {
        $n = count($price);
        $NEG = intdiv(-2147483647, 2);
        $dp = [];
        for ($a = 0; $a <= $maxAmount; $a++) $dp[] = array_fill(0, $maxCoupons + 1, $NEG);
        $dp[0][0] = 0;
        for ($i = 0; $i < $n; $i++) {
            $p = $price[$i];
            $t = $tastiness[$i];
            for ($a = $maxAmount; $a >= 0; $a--) {
                for ($c = $maxCoupons; $c >= 0; $c--) {
                    if ($dp[$a][$c] < 0) continue;
                    if ($a + $p <= $maxAmount) $dp[$a + $p][$c] = max($dp[$a + $p][$c], $dp[$a][$c] + $t);
                    $half = intdiv($p, 2);
                    if ($c + 1 <= $maxCoupons && $a + $half <= $maxAmount)
                        $dp[$a + $half][$c + 1] = max($dp[$a + $half][$c + 1], $dp[$a][$c] + $t);
                }
            }
        }
        $ans = 0;
        for ($a = 0; $a <= $maxAmount; $a++)
            for ($c = 0; $c <= $maxCoupons; $c++)
                if ($dp[$a][$c] > $ans) $ans = $dp[$a][$c];
        return $ans;
    }
}
''')

add("2432_the_employee_that_worked_on_the_longest_task", r'''<?php
// LeetCode 2432 - The Employee That Worked on the Longest Task
// https://leetcode.com/problems/the-employee-that-worked-on-the-longest-task/

class Solution {
    function hardestWorker($n, $logs) {
        $ans = $logs[0][0];
        $best = $logs[0][1];
        $prev = 0;
        foreach ($logs as $log) {
            $dur = $log[1] - $prev;
            if ($dur > $best || ($dur === $best && $log[0] < $ans)) {
                $best = $dur;
                $ans = $log[0];
            }
            $prev = $log[1];
        }
        return $ans;
    }
}
''')

add("2433_find_the_original_array_of_prefix_xor", r'''<?php
// LeetCode 2433 - Find The Original Array of Prefix Xor
// https://leetcode.com/problems/find-the-original-array-of-prefix-xor/

class Solution {
    function findArray($pref) {
        $ans = array_fill(0, count($pref), 0);
        $ans[0] = $pref[0];
        for ($i = 1; $i < count($pref); $i++) $ans[$i] = $pref[$i] ^ $pref[$i - 1];
        return $ans;
    }
}
''')

add("2434_using_a_robot_to_print_the_lexicographically_smallest_string", r'''<?php
// LeetCode 2434 - Using a Robot to Print the Lexicographically Smallest String
// https://leetcode.com/problems/using-a-robot-to-print-the-lexicographically-smallest-string/

class Solution {
    function robotWithString($s) {
        $n = strlen($s);
        $minSuf = array_fill(0, $n + 1, '');
        $minSuf[$n] = chr(ord('z') + 1);
        for ($i = $n - 1; $i >= 0; $i--)
            $minSuf[$i] = $s[$i] < $minSuf[$i + 1] ? $s[$i] : $minSuf[$i + 1];
        $stack = [];
        $ans = [];
        for ($i = 0; $i < $n; $i++) {
            $stack[] = $s[$i];
            while (count($stack) && $stack[count($stack) - 1] <= $minSuf[$i + 1])
                $ans[] = array_pop($stack);
        }
        while (count($stack)) $ans[] = array_pop($stack);
        return implode('', $ans);
    }
}
''')

add("2435_paths_in_matrix_whose_sum_is_divisible_by_k", r'''<?php
// LeetCode 2435 - Paths in Matrix Whose Sum Is Divisible by K
// https://leetcode.com/problems/paths-in-matrix-whose-sum-is-divisible-by-k/

class Solution {
    function numberOfPaths($grid, $k) {
        $mod = 1000000007;
        $m = count($grid);
        $n = count($grid[0]);
        $dp = [];
        for ($i = 0; $i < $m; $i++) {
            $row = [];
            for ($j = 0; $j < $n; $j++) $row[] = array_fill(0, $k, 0);
            $dp[] = $row;
        }
        $dp[0][0][$grid[0][0] % $k] = 1;
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                for ($r = 0; $r < $k; $r++) {
                    if ($dp[$i][$j][$r] === 0) continue;
                    if ($i + 1 < $m) {
                        $nr = ($r + $grid[$i + 1][$j]) % $k;
                        $dp[$i + 1][$j][$nr] = ($dp[$i + 1][$j][$nr] + $dp[$i][$j][$r]) % $mod;
                    }
                    if ($j + 1 < $n) {
                        $nr = ($r + $grid[$i][$j + 1]) % $k;
                        $dp[$i][$j + 1][$nr] = ($dp[$i][$j + 1][$nr] + $dp[$i][$j][$r]) % $mod;
                    }
                }
            }
        }
        return $dp[$m - 1][$n - 1][0];
    }
}
''')

add("2436_minimum_split_into_subarrays_with_gcd_greater_than_one", r'''<?php
// LeetCode 2436 - Minimum Split Into Subarrays With GCD Greater Than One
// https://leetcode.com/problems/minimum-split-into-subarrays-with-gcd-greater-than-one/

class Solution {
    function minimumSplits($nums) {
        $gcd = function ($a, $b) {
            while ($b !== 0) {
                $t = $a % $b;
                $a = $b;
                $b = $t;
            }
            return $a;
        };
        $ans = 1;
        $g = $nums[0];
        for ($i = 1; $i < count($nums); $i++) {
            $ng = $gcd($g, $nums[$i]);
            if ($ng === 1) {
                $ans++;
                $g = $nums[$i];
            } else $g = $ng;
        }
        return $ans;
    }
}
''')

add("2437_number_of_valid_clock_times", r'''<?php
// LeetCode 2437 - Number of Valid Clock Times
// https://leetcode.com/problems/number-of-valid-clock-times/

class Solution {
    function countTime($time) {
        $ans = 0;
        for ($h = 0; $h < 24; $h++) {
            for ($m = 0; $m < 60; $m++) {
                $h0 = (string)intdiv($h, 10);
                $h1 = (string)($h % 10);
                $m0 = (string)intdiv($m, 10);
                $m1 = (string)($m % 10);
                if ($time[0] !== '?' && $time[0] !== $h0) continue;
                if ($time[1] !== '?' && $time[1] !== $h1) continue;
                if ($time[3] !== '?' && $time[3] !== $m0) continue;
                if ($time[4] !== '?' && $time[4] !== $m1) continue;
                $ans++;
            }
        }
        return $ans;
    }
}
''')

add("2438_range_product_queries_of_powers", r'''<?php
// LeetCode 2438 - Range Product Queries of Powers
// https://leetcode.com/problems/range-product-queries-of-powers/

class Solution {
    function productQueries($n, $queries) {
        $mod = 1000000007;
        $powers = [];
        for ($bit = 0; $bit < 31; $bit++) {
            if ((($n >> $bit) & 1) !== 0) $powers[] = 1 << $bit;
        }
        $ans = array_fill(0, count($queries), 0);
        for ($i = 0; $i < count($queries); $i++) {
            $prod = 1;
            for ($j = $queries[$i][0]; $j <= $queries[$i][1]; $j++)
                $prod = ($prod * $powers[$j]) % $mod;
            $ans[$i] = $prod;
        }
        return $ans;
    }
}
''')

add("2439_minimize_maximum_of_array", r'''<?php
// LeetCode 2439 - Minimize Maximum of Array
// https://leetcode.com/problems/minimize-maximum-of-array/

class Solution {
    function minimizeArrayValue($nums) {
        $sum = 0;
        $ans = 0;
        for ($i = 0; $i < count($nums); $i++) {
            $sum += $nums[$i];
            $avg = intdiv($sum + $i, $i + 1);
            if ($avg > $ans) $ans = $avg;
        }
        return $ans;
    }
}
''')

add("2440_create_components_with_same_value", r'''<?php
// LeetCode 2440 - Create Components With Same Value
// https://leetcode.com/problems/create-components-with-same-value/

class Solution {
    function componentValue($nums, $edges) {
        $n = count($nums);
        $total = 0;
        foreach ($nums as $x) $total += $x;
        $g = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $g[$e[0]][] = $e[1];
            $g[$e[1]][] = $e[0];
        }
        $dfs = function ($u, $p, $target) use (&$dfs, &$g, $nums) {
            $sum = $nums[$u];
            foreach ($g[$u] as $v) {
                if ($v === $p) continue;
                $sub = $dfs($v, $u, $target);
                if ($sub < 0) return -1;
                $sum += $sub;
            }
            if ($sum > $target) return -1;
            if ($sum === $target) return 0;
            return $sum;
        };
        for ($parts = $n; $parts >= 1; $parts--) {
            if ($total % $parts !== 0) continue;
            $target = intdiv($total, $parts);
            if ($dfs(0, -1, $target) === 0) return $parts - 1;
        }
        return 0;
    }
}
''')

add("2441_largest_positive_integer_that_exists_with_its_negative", r'''<?php
// LeetCode 2441 - Largest Positive Integer That Exists With Its Negative
// https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/

class Solution {
    function findMaxK($nums) {
        $seen = [];
        $ans = -1;
        foreach ($nums as $x) {
            $seen[$x] = true;
            if ($x > 0 && isset($seen[-$x]) && $x > $ans) $ans = $x;
            if ($x < 0 && isset($seen[-$x]) && -$x > $ans) $ans = -$x;
        }
        return $ans;
    }
}
''')

add("2442_count_number_of_distinct_integers_after_reverse_operations", r'''<?php
// LeetCode 2442 - Count Number of Distinct Integers After Reverse Operations
// https://leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations/

class Solution {
    function countDistinctIntegers($nums) {
        $rev = function ($x) {
            $r = 0;
            while ($x > 0) {
                $r = $r * 10 + $x % 10;
                $x = intdiv($x, 10);
            }
            return $r;
        };
        $seen = [];
        foreach ($nums as $x) {
            $seen[$x] = true;
            $seen[$rev($x)] = true;
        }
        return count($seen);
    }
}
''')

add("2443_sum_of_number_and_its_reverse", r'''<?php
// LeetCode 2443 - Sum of Number and Its Reverse
// https://leetcode.com/problems/sum-of-number-and-its-reverse/

class Solution {
    function sumOfNumberAndReverse($num) {
        $rev = function ($x) {
            $r = 0;
            while ($x > 0) {
                $r = $r * 10 + $x % 10;
                $x = intdiv($x, 10);
            }
            return $r;
        };
        for ($i = 0; $i <= $num; $i++) {
            if ($i + $rev($i) === $num) return true;
        }
        return false;
    }
}
''')

add("2444_count_subarrays_with_fixed_bounds", r'''<?php
// LeetCode 2444 - Count Subarrays With Fixed Bounds
// https://leetcode.com/problems/count-subarrays-with-fixed-bounds/

class Solution {
    function countSubarrays($nums, $minK, $maxK) {
        $ans = 0;
        $imin = -1;
        $imax = -1;
        $ibad = -1;
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            $x = $nums[$i];
            if ($x < $minK || $x > $maxK) $ibad = $i;
            if ($x === $minK) $imin = $i;
            if ($x === $maxK) $imax = $i;
            $bound = $imin < $imax ? $imin : $imax;
            if ($bound > $ibad) $ans += $bound - $ibad;
        }
        return $ans;
    }
}
''')

add("2445_number_of_nodes_with_value_one", r'''<?php
// LeetCode 2445 - Number of Nodes With Value One
// https://leetcode.com/problems/number-of-nodes-with-value-one/

class Solution {
    function numberOfNodes($n, $queries) {
        $flip = array_fill(0, $n + 1, 0);
        $val = array_fill(0, $n + 1, 0);
        foreach ($queries as $q) $flip[$q] ^= 1;
        $ans = 0;
        for ($i = 1; $i <= $n; $i++) {
            $val[$i] = $flip[$i];
            if ($i > 1) $val[$i] ^= $val[intdiv($i, 2)];
            $ans += $val[$i];
        }
        return $ans;
    }
}
''')

add("2446_determine_if_two_events_have_conflict", r'''<?php
// LeetCode 2446 - Determine if Two Events Have Conflict
// https://leetcode.com/problems/determine-if-two-events-have-conflict/

class Solution {
    function haveConflict($event1, $event2) {
        return $event1[0] <= $event2[1] && $event2[0] <= $event1[1];
    }
}
''')

add("2447_number_of_subarrays_with_gcd_equal_to_k", r'''<?php
// LeetCode 2447 - Number of Subarrays With GCD Equal to K
// https://leetcode.com/problems/number-of-subarrays-with-gcd-equal-to-k/

class Solution {
    function subarrayGCD($nums, $k) {
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
            $g = 0;
            for ($j = $i; $j < $n; $j++) {
                $g = $gcd($g, $nums[$j]);
                if ($g < $k) break;
                if ($g === $k) $ans++;
            }
        }
        return $ans;
    }
}
''')

add("2448_minimum_cost_to_make_array_equal", r'''<?php
// LeetCode 2448 - Minimum Cost to Make Array Equal
// https://leetcode.com/problems/minimum-cost-to-make-array-equal/

class Solution {
    function minCost($nums, $cost) {
        $n = count($nums);
        $idx = range(0, $n - 1);
        usort($idx, function ($a, $b) use ($nums) {
            return $nums[$a] <=> $nums[$b];
        });
        $totalCost = 0;
        foreach ($cost as $c) $totalCost += $c;
        $pref = 0;
        $median = 0;
        foreach ($idx as $i) {
            $pref += $cost[$i];
            if ($pref * 2 >= $totalCost) {
                $median = $nums[$i];
                break;
            }
        }
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            $diff = $nums[$i] - $median;
            if ($diff < 0) $diff = -$diff;
            $ans += $diff * $cost[$i];
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

#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
SOLUTIONS = {}

def add(folder, body):
    SOLUTIONS[folder] = body


add("2806_account_balance_after_rounded_purchase", r'''<?php
// LeetCode 2806 - Account Balance After Rounded Purchase
// https://leetcode.com/problems/account-balance-after-rounded-purchase/

class Solution {
    function accountBalanceAfterPurchase($purchaseAmount) {
        $r = intdiv($purchaseAmount + 5, 10) * 10;
        return 100 - $r;
    }
}
''')

add("2807_insert_greatest_common_divisors_in_linked_list", r'''<?php
// LeetCode 2807 - Insert Greatest Common Divisors in Linked List
// https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/

class ListNode {
    public $val = 0;
    public $next = null;
    function __construct($val = 0, $next = null) {
        $this->val = $val;
        $this->next = $next;
    }
}

class Solution {
    function insertGreatestCommonDivisors($head) {
        $gcd = function($a, $b) {
            while ($b) { $t = $a % $b; $a = $b; $b = $t; }
            return $a;
        };
        $cur = $head;
        while ($cur && $cur->next) {
            $g = $gcd($cur->val, $cur->next->val);
            $node = new ListNode($g, $cur->next);
            $cur->next = $node;
            $cur = $node->next;
        }
        return $head;
    }
}
''')

add("2808_minimum_seconds_to_equalize_a_circular_array", r'''<?php
// LeetCode 2808 - Minimum Seconds to Equalize a Circular Array
// https://leetcode.com/problems/minimum-seconds-to-equalize-a-circular-array/

class Solution {
    function minimumSeconds($nums) {
        $n = count($nums);
        $pos = [];
        for ($i = 0; $i < $n; $i++) $pos[$nums[$i]][] = $i;
        $ans = $n;
        foreach ($pos as $p) {
            $maxGap = 0;
            $m = count($p);
            for ($i = 0; $i < $m; $i++) {
                $gap = ($i + 1 < $m) ? $p[$i + 1] - $p[$i] : $p[0] + $n - $p[$i];
                $maxGap = max($maxGap, intdiv($gap, 2));
            }
            $ans = min($ans, $maxGap);
        }
        return $ans;
    }
}
''')

add("2809_minimum_time_to_make_array_sum_at_most_x", r'''<?php
// LeetCode 2809 - Minimum Time to Make Array Sum At Most x
// https://leetcode.com/problems/minimum-time-to-make-array-sum-at-most-x/

class Solution {
    function minimumTime($nums1, $nums2, $x) {
        $n = count($nums1);
        $arr = [];
        $sum1 = 0;
        $sum2 = 0;
        for ($i = 0; $i < $n; $i++) {
            $arr[] = [$nums1[$i], $nums2[$i]];
            $sum1 += $nums1[$i];
            $sum2 += $nums2[$i];
        }
        usort($arr, function($a, $b) { return $a[1] <=> $b[1]; });
        $dp = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; $i++) {
            for ($j = $i + 1; $j >= 1; $j--) {
                $dp[$j] = max($dp[$j], $dp[$j - 1] + $arr[$i][0] + $j * $arr[$i][1]);
            }
        }
        for ($t = 0; $t <= $n; $t++) {
            if ($sum1 + $sum2 * $t - $dp[$t] <= $x) return $t;
        }
        return -1;
    }
}
''')

add("2810_faulty_keyboard", r'''<?php
// LeetCode 2810 - Faulty Keyboard
// https://leetcode.com/problems/faulty-keyboard/

class Solution {
    function finalString($s) {
        $b = '';
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            if ($s[$i] === 'i') $b = strrev($b);
            else $b .= $s[$i];
        }
        return $b;
    }
}
''')

add("2811_check_if_it_is_possible_to_split_array", r'''<?php
// LeetCode 2811 - Check if it is Possible to Split Array
// https://leetcode.com/problems/check-if-it-is-possible-to-split-array/

class Solution {
    function canSplitArray($nums, $m) {
        $n = count($nums);
        if ($n <= 2) return true;
        for ($i = 0; $i + 1 < $n; $i++) {
            if ($nums[$i] + $nums[$i + 1] >= $m) return true;
        }
        return false;
    }
}
''')

add("2812_find_the_safest_path_in_a_grid", r'''<?php
// LeetCode 2812 - Find the Safest Path in a Grid
// https://leetcode.com/problems/find-the-safest-path-in-a-grid/

class Solution {
    function maximumSafenessFactor($grid) {
        $n = count($grid);
        $dist = array_fill(0, $n, array_fill(0, $n, -1));
        $q = [];
        for ($i = 0; $i < $n; $i++)
            for ($j = 0; $j < $n; $j++)
                if ($grid[$i][$j] === 1) {
                    $dist[$i][$j] = 0;
                    $q[] = [$i, $j];
                }
        $dirs = [[1,0],[-1,0],[0,1],[0,-1]];
        for ($h = 0; $h < count($q); $h++) {
            $x = $q[$h][0];
            $y = $q[$h][1];
            foreach ($dirs as $d) {
                $ni = $x + $d[0];
                $nj = $y + $d[1];
                if ($ni >= 0 && $nj >= 0 && $ni < $n && $nj < $n && $dist[$ni][$nj] === -1) {
                    $dist[$ni][$nj] = $dist[$x][$y] + 1;
                    $q[] = [$ni, $nj];
                }
            }
        }
        $ok = function($sf) use ($n, $dist, $dirs) {
            if ($dist[0][0] < $sf) return false;
            $seen = array_fill(0, $n, array_fill(0, $n, false));
            $st = [[0, 0]];
            $seen[0][0] = true;
            while ($st) {
                $cur = array_pop($st);
                $x = $cur[0];
                $y = $cur[1];
                if ($x === $n - 1 && $y === $n - 1) return true;
                foreach ($dirs as $d) {
                    $ni = $x + $d[0];
                    $nj = $y + $d[1];
                    if ($ni >= 0 && $nj >= 0 && $ni < $n && $nj < $n && !$seen[$ni][$nj] && $dist[$ni][$nj] >= $sf) {
                        $seen[$ni][$nj] = true;
                        $st[] = [$ni, $nj];
                    }
                }
            }
            return false;
        };
        $lo = 0;
        $hi = $n * $n;
        $ans = 0;
        while ($lo <= $hi) {
            $mid = ($lo + $hi) >> 1;
            if ($ok($mid)) { $ans = $mid; $lo = $mid + 1; }
            else $hi = $mid - 1;
        }
        return $ans;
    }
}
''')

add("2813_maximum_elegance_of_a_k_length_subsequence", r'''<?php
// LeetCode 2813 - Maximum Elegance of a K-Length Subsequence
// https://leetcode.com/problems/maximum-elegance-of-a-k-length-subsequence/

class Solution {
    function findMaximumElegance($items, $k) {
        usort($items, function($a, $b) { return $b[0] <=> $a[0]; });
        $seen = [];
        $total = 0;
        $dup = [];
        for ($i = 0; $i < $k; $i++) {
            $total += $items[$i][0];
            $c = $items[$i][1];
            if (isset($seen[$c])) $dup[] = $items[$i][0];
            else $seen[$c] = true;
        }
        $ans = $total + count($seen) * count($seen);
        for ($i = $k; $i < count($items); $i++) {
            $c = $items[$i][1];
            if (isset($seen[$c]) || !$dup) continue;
            $total += $items[$i][0] - array_pop($dup);
            $seen[$c] = true;
            $ans = max($ans, $total + count($seen) * count($seen));
        }
        return $ans;
    }
}
''')

add("2814_minimum_time_takes_to_reach_destination_without_drowning", r'''<?php
// LeetCode 2814 - Minimum Time Takes to Reach Destination Without Drowning
// https://leetcode.com/problems/minimum-time-takes-to-reach-destination-without-drowning/

class Solution {
    function minimumSeconds($land) {
        $m = count($land);
        $n = count($land[0]);
        $INF = 1000000000;
        $water = array_fill(0, $m, array_fill(0, $n, $INF));
        $wq = [];
        $sx = 0;
        $sy = 0;
        $dx = 0;
        $dy = 0;
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                $cell = $land[$i][$j];
                if ($cell === '*') {
                    $water[$i][$j] = 0;
                    $wq[] = [$i, $j];
                } else if ($cell === 'S') { $sx = $i; $sy = $j; }
                else if ($cell === 'D') { $dx = $i; $dy = $j; }
            }
        }
        $dirs = [[1,0],[-1,0],[0,1],[0,-1]];
        for ($h = 0; $h < count($wq); $h++) {
            $x = $wq[$h][0];
            $y = $wq[$h][1];
            foreach ($dirs as $d) {
                $ni = $x + $d[0];
                $nj = $y + $d[1];
                if ($ni < 0 || $nj < 0 || $ni >= $m || $nj >= $n) continue;
                $cell = $land[$ni][$nj];
                if ($cell === 'X' || $cell === 'D') continue;
                if ($water[$ni][$nj] > $water[$x][$y] + 1) {
                    $water[$ni][$nj] = $water[$x][$y] + 1;
                    $wq[] = [$ni, $nj];
                }
            }
        }
        $dist = array_fill(0, $m, array_fill(0, $n, -1));
        $q = [[$sx, $sy]];
        $dist[$sx][$sy] = 0;
        for ($h = 0; $h < count($q); $h++) {
            $x = $q[$h][0];
            $y = $q[$h][1];
            if ($x === $dx && $y === $dy) return $dist[$x][$y];
            foreach ($dirs as $d) {
                $ni = $x + $d[0];
                $nj = $y + $d[1];
                if ($ni < 0 || $nj < 0 || $ni >= $m || $nj >= $n || $dist[$ni][$nj] !== -1) continue;
                if ($land[$ni][$nj] === 'X') continue;
                $nd = $dist[$x][$y] + 1;
                if ($land[$ni][$nj] !== 'D' && $nd >= $water[$ni][$nj]) continue;
                $dist[$ni][$nj] = $nd;
                $q[] = [$ni, $nj];
            }
        }
        return -1;
    }
}
''')

add("2815_max_pair_sum_in_an_array", r'''<?php
// LeetCode 2815 - Max Pair Sum in an Array
// https://leetcode.com/problems/max-pair-sum-in-an-array/

class Solution {
    function maxSum($nums) {
        $best = [];
        $ans = -1;
        foreach ($nums as $v) {
            $x = $v;
            $md = 0;
            while ($x > 0) { $md = max($md, $x % 10); $x = intdiv($x, 10); }
            if (isset($best[$md])) {
                $ans = max($ans, $best[$md] + $v);
                $best[$md] = max($best[$md], $v);
            } else $best[$md] = $v;
        }
        return $ans;
    }
}
''')

add("2816_double_a_number_represented_as_a_linked_list", r'''<?php
// LeetCode 2816 - Double a Number Represented as a Linked List
// https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/

class ListNode {
    public $val = 0;
    public $next = null;
    function __construct($val = 0, $next = null) {
        $this->val = $val;
        $this->next = $next;
    }
}

class Solution {
    function doubleIt($head) {
        $rev = function($node) {
            $prev = null;
            while ($node) {
                $nxt = $node->next;
                $node->next = $prev;
                $prev = $node;
                $node = $nxt;
            }
            return $prev;
        };
        $head = $rev($head);
        $carry = 0;
        $cur = $head;
        $prev = null;
        while ($cur) {
            $val = $cur->val * 2 + $carry;
            $cur->val = $val % 10;
            $carry = intdiv($val, 10);
            $prev = $cur;
            $cur = $cur->next;
        }
        if ($carry > 0) $prev->next = new ListNode($carry);
        return $rev($head);
    }
}
''')

add("2817_minimum_absolute_difference_between_elements_with_constraint", r'''<?php
// LeetCode 2817 - Minimum Absolute Difference Between Elements With Constraint
// https://leetcode.com/problems/minimum-absolute-difference-between-elements-with-constraint/

class Solution {
    function minAbsoluteDifference($nums, $x) {
        if ($x === 0) {
            $ans0 = PHP_INT_MAX;
            for ($i = 1; $i < count($nums); $i++)
                $ans0 = min($ans0, abs($nums[$i] - $nums[$i - 1]));
            return $ans0;
        }
        $ans = PHP_INT_MAX;
        $arr = [];
        $insert = function($v) use (&$arr) {
            $lo = 0;
            $hi = count($arr);
            while ($lo < $hi) {
                $mid = ($lo + $hi) >> 1;
                if ($arr[$mid] < $v) $lo = $mid + 1;
                else $hi = $mid;
            }
            array_splice($arr, $lo, 0, [$v]);
        };
        $lowerBound = function($v) use (&$arr) {
            $lo = 0;
            $hi = count($arr);
            while ($lo < $hi) {
                $mid = ($lo + $hi) >> 1;
                if ($arr[$mid] < $v) $lo = $mid + 1;
                else $hi = $mid;
            }
            return $lo;
        };
        for ($i = $x; $i < count($nums); $i++) {
            $insert($nums[$i - $x]);
            $cur = $nums[$i];
            $idx = $lowerBound($cur);
            if ($idx < count($arr)) $ans = min($ans, $arr[$idx] - $cur);
            if ($idx > 0) $ans = min($ans, $cur - $arr[$idx - 1]);
        }
        return $ans;
    }
}
''')

add("2818_apply_operations_to_maximize_score", r'''<?php
// LeetCode 2818 - Apply Operations to Maximize Score
// https://leetcode.com/problems/apply-operations-to-maximize-score/

class Solution {
    function maximumScore($nums, $k) {
        $MOD = 1000000007;
        $n = count($nums);
        $maxV = 0;
        foreach ($nums as $v) $maxV = max($maxV, $v);
        $spf = array_fill(0, $maxV + 1, 0);
        for ($i = 2; $i <= $maxV; $i++) {
            if ($spf[$i] === 0) {
                for ($j = $i; $j <= $maxV; $j += $i) if ($spf[$j] === 0) $spf[$j] = $i;
            }
        }
        $primeScore = function($x) use ($spf) {
            $seen = [];
            while ($x > 1) {
                $p = $spf[$x];
                $seen[$p] = true;
                while ($x % $p === 0) $x = intdiv($x, $p);
            }
            return count($seen);
        };
        $score = [];
        foreach ($nums as $v) $score[] = $primeScore($v);
        $left = array_fill(0, $n, -1);
        $right = array_fill(0, $n, $n);
        $st = [];
        for ($i = 0; $i < $n; $i++) {
            while ($st && $score[$st[count($st) - 1]] < $score[$i]) array_pop($st);
            $left[$i] = $st ? $st[count($st) - 1] : -1;
            $st[] = $i;
        }
        $st = [];
        for ($i = $n - 1; $i >= 0; $i--) {
            while ($st && $score[$st[count($st) - 1]] <= $score[$i]) array_pop($st);
            $right[$i] = $st ? $st[count($st) - 1] : $n;
            $st[] = $i;
        }
        $arr = [];
        for ($i = 0; $i < $n; $i++) $arr[] = [$nums[$i], ($i - $left[$i]) * ($right[$i] - $i)];
        usort($arr, function($a, $b) { return $b[0] <=> $a[0]; });
        $modPow = function($a, $b) use ($MOD) {
            $res = 1;
            $base = $a % $MOD;
            $exp = $b;
            while ($exp > 0) {
                if ($exp % 2 === 1) $res = ($res * $base) % $MOD;
                $base = ($base * $base) % $MOD;
                $exp = intdiv($exp, 2);
            }
            return $res;
        };
        $ans = 1;
        $remain = $k;
        foreach ($arr as $item) {
            if ($remain <= 0) break;
            $use = $item[1] < $remain ? $item[1] : $remain;
            $ans = $ans * $modPow($item[0], $use) % $MOD;
            $remain -= $use;
        }
        return $ans;
    }
}
''')

add("2819_minimum_relative_loss_after_buying_chocolates", r'''<?php
// LeetCode 2819 - Minimum Relative Loss After Buying Chocolates
// https://leetcode.com/problems/minimum-relative-loss-after-buying-chocolates/

class Solution {
    function minimumRelativeLosses($prices, $queries) {
        sort($prices);
        $n = count($prices);
        $ans = array_fill(0, count($queries), 0);
        for ($qi = 0; $qi < count($queries); $qi++) {
            $kk = $queries[$qi][0];
            $m = $queries[$qi][1];
            $losses = [];
            for ($i = 0; $i < $n; $i++) {
                if ($prices[$i] <= $kk) $losses[$i] = $prices[$i];
                else $losses[$i] = 2 * $kk - $prices[$i];
            }
            sort($losses);
            $sum = 0;
            for ($i = 0; $i < $m; $i++) $sum += $losses[$i];
            $ans[$qi] = $sum;
        }
        return $ans;
    }
}
''')

add("2821_delay_the_resolution_of_each_promise", r'''<?php
// LeetCode 2821 - Delay the Resolution of Each Promise
// https://leetcode.com/problems/delay-the-resolution-of-each-promise/

class Solution {
    function delayAll($functions, $ms) {
        $out = [];
        foreach ($functions as $fn) {
            $out[] = function() use ($fn, $ms) {
                try {
                    $result = $fn();
                    return $result;
                } catch (Throwable $e) {
                    throw $e;
                }
            };
        }
        return $out;
    }
}
''')

add("2822_inversion_of_object", r'''<?php
// LeetCode 2822 - Inversion of Object
// https://leetcode.com/problems/inversion-of-object/

class Solution {
    function invertObject($obj) {
        $inverted = [];
        if (is_object($obj)) $obj = (array)$obj;
        foreach ($obj as $key => $val) {
            $val = is_bool($val) ? ($val ? 'true' : 'false') : (string)$val;
            $key = (string)$key;
            if (array_key_exists($val, $inverted)) {
                if (!is_array($inverted[$val])) $inverted[$val] = [$inverted[$val]];
                $inverted[$val][] = $key;
            } else {
                $inverted[$val] = $key;
            }
        }
        return $inverted;
    }
}
''')

add("2823_deep_object_filter", r'''<?php
// LeetCode 2823 - Deep Object Filter
// https://leetcode.com/problems/deep-object-filter/

class Solution {
    function deepFilter($obj, $fn) {
        if (!is_array($obj) && !is_object($obj)) {
            return $fn($obj) ? $obj : null;
        }
        if (is_object($obj)) $obj = (array)$obj;
        $isList = $obj === [] || array_keys($obj) === range(0, count($obj) - 1);
        if ($isList) {
            $res = [];
            foreach ($obj as $v) {
                $f = $this->deepFilter($v, $fn);
                if ($f !== null) $res[] = $f;
            }
            return $res ? $res : null;
        }
        $res = [];
        foreach ($obj as $k => $v) {
            $f = $this->deepFilter($v, $fn);
            if ($f !== null) $res[$k] = $f;
        }
        return $res ? $res : null;
    }
}
''')

add("2824_count_pairs_whose_sum_is_less_than_target", r'''<?php
// LeetCode 2824 - Count Pairs Whose Sum is Less than Target
// https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/

class Solution {
    function countPairs($nums, $target) {
        $ans = 0;
        $n = count($nums);
        for ($i = 0; $i < $n; $i++)
            for ($j = $i + 1; $j < $n; $j++)
                if ($nums[$i] + $nums[$j] < $target) $ans++;
        return $ans;
    }
}
''')

add("2825_make_string_a_subsequence_using_cyclic_increments", r'''<?php
// LeetCode 2825 - Make String a Subsequence Using Cyclic Increments
// https://leetcode.com/problems/make-string-a-subsequence-using-cyclic-increments/

class Solution {
    function canMakeSubsequence($str1, $str2) {
        $j = 0;
        $n1 = strlen($str1);
        $n2 = strlen($str2);
        for ($i = 0; $i < $n1 && $j < $n2; $i++) {
            $a = ord($str1[$i]) - 97;
            $b = ord($str2[$j]) - 97;
            if ($a === $b || ($a + 1) % 26 === $b) $j++;
        }
        return $j === $n2;
    }
}
''')

add("2826_sorting_three_groups", r'''<?php
// LeetCode 2826 - Sorting Three Groups
// https://leetcode.com/problems/sorting-three-groups/

class Solution {
    function minimumOperations($nums) {
        $n = count($nums);
        $INF = 1000000000;
        $dp = array_fill(0, $n + 1, array_fill(0, 4, $INF));
        $dp[0][1] = $dp[0][2] = $dp[0][3] = 0;
        for ($i = 1; $i <= $n; $i++) {
            $v = $nums[$i - 1];
            for ($g = 1; $g <= 3; $g++) {
                $cost = $v !== $g ? 1 : 0;
                for ($prev = 1; $prev <= $g; $prev++)
                    $dp[$i][$g] = min($dp[$i][$g], $dp[$i - 1][$prev] + $cost);
            }
        }
        return min($dp[$n][1], $dp[$n][2], $dp[$n][3]);
    }
}
''')

add("2827_number_of_beautiful_integers_in_the_range", r'''<?php
// LeetCode 2827 - Number of Beautiful Integers in the Range
// https://leetcode.com/problems/number-of-beautiful-integers-in-the-range/

class Solution {
    public $s;
    public $k;
    public $memo;
    function numberOfBeautifulIntegers($low, $high, $k) {
        $this->k = $k;
        return $this->count($high) - $this->count($low - 1);
    }
    function count($n) {
        if ($n < 0) return 0;
        $this->s = (string)$n;
        $this->memo = [];
        return $this->dfs(0, 0, 0, 1, 0);
    }
    function dfs($pos, $diff, $mod, $tight, $started) {
        if ($pos === strlen($this->s)) return ($started && $diff === 0 && $mod === 0) ? 1 : 0;
        $key = $pos . ',' . $diff . ',' . $mod . ',' . $tight . ',' . $started;
        if (isset($this->memo[$key])) return $this->memo[$key];
        $up = $tight ? ord($this->s[$pos]) - 48 : 9;
        $ans = 0;
        for ($digit = 0; $digit <= $up; $digit++) {
            $nt = ($tight && $digit === $up) ? 1 : 0;
            if (!$started) {
                if ($digit === 0) $ans += $this->dfs($pos + 1, $diff, $mod, $nt, 0);
                else {
                    $nd = $diff + ($digit % 2 === 0 ? 1 : -1);
                    $ans += $this->dfs($pos + 1, $nd, $digit % $this->k, $nt, 1);
                }
            } else {
                $nd = $diff + ($digit % 2 === 0 ? 1 : -1);
                $ans += $this->dfs($pos + 1, $nd, ($mod * 10 + $digit) % $this->k, $nt, 1);
            }
        }
        return $this->memo[$key] = $ans;
    }
}
''')

add("2828_check_if_a_string_is_an_acronym_of_words", r'''<?php
// LeetCode 2828 - Check if a String Is an Acronym of Words
// https://leetcode.com/problems/check-if-a-string-is-an-acronym-of-words/

class Solution {
    function isAcronym($words, $s) {
        if (count($words) !== strlen($s)) return false;
        for ($i = 0; $i < count($words); $i++) {
            $w = $words[$i];
            if ($w === '' || $w[0] !== $s[$i]) return false;
        }
        return true;
    }
}
''')

add("2829_determine_the_minimum_sum_of_a_k_avoiding_array", r'''<?php
// LeetCode 2829 - Determine the Minimum Sum of a k-avoiding Array
// https://leetcode.com/problems/determine-the-minimum-sum-of-a-k-avoiding-array/

class Solution {
    function minimumSum($n, $k) {
        $used = [];
        $sum = 0;
        $x = 1;
        while (count($used) < $n) {
            if (!isset($used[$k - $x])) {
                $used[$x] = true;
                $sum += $x;
            }
            $x++;
        }
        return $sum;
    }
}
''')

add("2830_maximize_the_profit_as_the_salesman", r'''<?php
// LeetCode 2830 - Maximize the Profit as the Salesman
// https://leetcode.com/problems/maximize-the-profit-as-the-salesman/

class Solution {
    function maximizeTheProfit($n, $offers) {
        $byEnd = array_fill(0, $n, []);
        foreach ($offers as $o) $byEnd[$o[1]][] = $o;
        $dp = array_fill(0, $n + 1, 0);
        for ($end = 0; $end < $n; $end++) {
            $dp[$end + 1] = $dp[$end];
            foreach ($byEnd[$end] as $o)
                $dp[$end + 1] = max($dp[$end + 1], $dp[$o[0]] + $o[2]);
        }
        return $dp[$n];
    }
}
''')

add("2831_find_the_longest_equal_subarray", r'''<?php
// LeetCode 2831 - Find the Longest Equal Subarray
// https://leetcode.com/problems/find-the-longest-equal-subarray/

class Solution {
    function longestEqualSubarray($nums, $k) {
        $pos = [];
        for ($i = 0; $i < count($nums); $i++) $pos[$nums[$i]][] = $i;
        $ans = 0;
        foreach ($pos as $p) {
            $left = 0;
            for ($right = 0; $right < count($p); $right++) {
                while ($p[$right] - $p[$left] - ($right - $left) > $k) $left++;
                $ans = max($ans, $right - $left + 1);
            }
        }
        return $ans;
    }
}
''')


def main():
    written = 0
    for folder, body in SOLUTIONS.items():
        path = ROOT / folder / "solution.php"
        path.write_text(body, encoding="utf-8", newline="\n")
        written += 1
        print("wrote", folder)
    print("C written", written)

if __name__ == "__main__":
    main()

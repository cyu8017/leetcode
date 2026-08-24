#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
SOLUTIONS = {}

def add(folder, body):
    SOLUTIONS[folder] = body


add("2553_separate_the_digits_in_an_array", r'''<?php
// LeetCode 2553 - Separate the Digits in an Array
// https://leetcode.com/problems/separate-the-digits-in-an-array/

class Solution {
    function separateDigits($nums) {
        $ans = [];
        foreach ($nums as $num) {
            $digits = [];
            while ($num > 0) {
                $digits[] = $num % 10;
                $num = intdiv($num, 10);
            }
            for ($i = count($digits) - 1; $i >= 0; $i--) $ans[] = $digits[$i];
        }
        return $ans;
    }
}
''')

add("2554_maximum_number_of_integers_to_choose_from_a_range_i", r'''<?php
// LeetCode 2554 - Maximum Number of Integers to Choose From a Range I
// https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-i/

class Solution {
    function maxCount($banned, $n, $maxSum) {
        $ban = [];
        foreach ($banned as $x) $ban[$x] = true;
        $ans = 0;
        $sum = 0;
        for ($i = 1; $i <= $n; $i++) {
            if (isset($ban[$i])) continue;
            if ($sum + $i > $maxSum) break;
            $sum += $i;
            $ans++;
        }
        return $ans;
    }
}
''')

add("2555_maximize_win_from_two_segments", r'''<?php
// LeetCode 2555 - Maximize Win From Two Segments
// https://leetcode.com/problems/maximize-win-from-two-segments/

class Solution {
    function maximizeWin($prizePositions, $k) {
        $n = count($prizePositions);
        $dp = array_fill(0, $n + 1, 0);
        $ans = 0;
        $left = 0;
        for ($right = 0; $right < $n; $right++) {
            while ($prizePositions[$right] - $prizePositions[$left] > $k) $left++;
            $cur = $right - $left + 1;
            if ($dp[$left] + $cur > $ans) $ans = $dp[$left] + $cur;
            $best = $cur;
            if ($dp[$right] > $best) $best = $dp[$right];
            $dp[$right + 1] = $best;
        }
        return $ans;
    }
}
''')

add("2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip", r'''<?php
// LeetCode 2556 - Disconnect Path in a Binary Matrix by at Most One Flip
// https://leetcode.com/problems/disconnect-path-in-a-binary-matrix-by-at-most-one-flip/

class Solution {
    function isPossibleToCutPath($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        $dfs = function($r, $c) use (&$dfs, &$grid, $m, $n) {
            if ($r === $m - 1 && $c === $n - 1) return true;
            if ($r >= $m || $c >= $n || $grid[$r][$c] === 0) return false;
            if (!($r === 0 && $c === 0)) $grid[$r][$c] = 0;
            return $dfs($r + 1, $c) || $dfs($r, $c + 1);
        };
        if (!$dfs(0, 0)) return true;
        $grid[0][0] = 1;
        return !$dfs(0, 0);
    }
}
''')

add("2557_maximum_number_of_integers_to_choose_from_a_range_ii", r'''<?php
// LeetCode 2557 - Maximum Number of Integers to Choose From a Range II
// https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-ii/

class Solution {
    function maxCount($banned, $n, $maxSum) {
        sort($banned);
        $uniq = [];
        foreach ($banned as $x) {
            if ($x >= 1 && $x <= $n && (!$uniq || $uniq[count($uniq) - 1] !== $x)) $uniq[] = $x;
        }
        $ans = 0;
        $remain = $maxSum;
        $prev = 0;
        $check = function($l, $r) use (&$ans, &$remain) {
            if ($l > $r || $remain <= 0) return;
            $lo = $l;
            $hi = $r;
            $best = $l - 1;
            while ($lo <= $hi) {
                $mid = intdiv($lo + $hi, 2);
                $cnt = $mid - $l + 1;
                $sum = intdiv(($l + $mid) * $cnt, 2);
                if ($sum <= $remain) {
                    $best = $mid;
                    $lo = $mid + 1;
                } else $hi = $mid - 1;
            }
            if ($best >= $l) {
                $cnt = $best - $l + 1;
                $ans += $cnt;
                $remain -= intdiv(($l + $best) * $cnt, 2);
            }
        };
        foreach ($uniq as $b) {
            $check($prev + 1, $b - 1);
            $prev = $b;
        }
        $check($prev + 1, $n);
        return $ans;
    }
}
''')

add("2558_take_gifts_from_the_richest_pile", r'''<?php
// LeetCode 2558 - Take Gifts From the Richest Pile
// https://leetcode.com/problems/take-gifts-from-the-richest-pile/

class Solution {
    function pickGifts($gifts, $k) {
        $h = new SplPriorityQueue();
        foreach ($gifts as $g) $h->insert($g, $g);
        for ($i = 0; $i < $k; $i++) {
            $x = $h->extract();
            $nxt = (int)floor(sqrt($x));
            $h->insert($nxt, $nxt);
        }
        $ans = 0;
        while (!$h->isEmpty()) $ans += $h->extract();
        return $ans;
    }
}
''')

add("2559_count_vowel_strings_in_ranges", r'''<?php
// LeetCode 2559 - Count Vowel Strings in Ranges
// https://leetcode.com/problems/count-vowel-strings-in-ranges/

class Solution {
    function vowelStrings($words, $queries) {
        $isV = function($c) {
            return $c === 'a' || $c === 'e' || $c === 'i' || $c === 'o' || $c === 'u';
        };
        $n = count($words);
        $pref = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; $i++) {
            $pref[$i + 1] = $pref[$i];
            $w = $words[$i];
            $len = strlen($w);
            if ($len > 0 && $isV($w[0]) && $isV($w[$len - 1])) $pref[$i + 1]++;
        }
        $ans = [];
        foreach ($queries as $q) {
            $ans[] = $pref[$q[1] + 1] - $pref[$q[0]];
        }
        return $ans;
    }
}
''')

add("2560_house_robber_iv", r'''<?php
// LeetCode 2560 - House Robber IV
// https://leetcode.com/problems/house-robber-iv/

class Solution {
    function minCapability($nums, $k) {
        $lo = min($nums);
        $hi = max($nums);
        $ok = function($cap) use ($nums, $k) {
            $cnt = 0;
            $n = count($nums);
            for ($i = 0; $i < $n; ) {
                if ($nums[$i] <= $cap) {
                    $cnt++;
                    $i += 2;
                } else $i++;
            }
            return $cnt >= $k;
        };
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi, 2);
            if ($ok($mid)) $hi = $mid;
            else $lo = $mid + 1;
        }
        return $lo;
    }
}
''')

add("2561_rearranging_fruits", r'''<?php
// LeetCode 2561 - Rearranging Fruits
// https://leetcode.com/problems/rearranging-fruits/

class Solution {
    function minCost($basket1, $basket2) {
        $freq = [];
        $mn = PHP_INT_MAX;
        foreach ($basket1 as $x) {
            $freq[$x] = ($freq[$x] ?? 0) + 1;
            if ($x < $mn) $mn = $x;
        }
        foreach ($basket2 as $x) {
            $freq[$x] = ($freq[$x] ?? 0) - 1;
            if ($x < $mn) $mn = $x;
        }
        $extra = [];
        foreach ($freq as $k => $v) {
            if ($v % 2 !== 0) return -1;
            $times = intdiv(abs($v), 2);
            for ($i = 0; $i < $times; $i++) $extra[] = $k;
        }
        sort($extra);
        $ans = 0;
        $half = intdiv(count($extra), 2);
        for ($i = 0; $i < $half; $i++) {
            $ans += min($extra[$i], 2 * $mn);
        }
        return $ans;
    }
}
''')

add("2562_find_the_array_concatenation_value", r'''<?php
// LeetCode 2562 - Find the Array Concatenation Value
// https://leetcode.com/problems/find-the-array-concatenation-value/

class Solution {
    function findTheArrayConcVal($nums) {
        $ans = 0;
        $l = 0;
        $r = count($nums) - 1;
        while ($l <= $r) {
            if ($l === $r) {
                $ans += $nums[$l];
                break;
            }
            $left = $nums[$l];
            $right = $nums[$r];
            $pow = 1;
            for ($t = $right; $t > 0; $t = intdiv($t, 10)) $pow *= 10;
            $ans += $left * $pow + $right;
            $l++;
            $r--;
        }
        return $ans;
    }
}
''')

add("2563_count_the_number_of_fair_pairs", r'''<?php
// LeetCode 2563 - Count the Number of Fair Pairs
// https://leetcode.com/problems/count-the-number-of-fair-pairs/

class Solution {
    function countFairPairs($nums, $lower, $upper) {
        sort($nums);
        $count = function($x) use ($nums) {
            $ans = 0;
            $l = 0;
            $r = count($nums) - 1;
            while ($l < $r) {
                if ($nums[$l] + $nums[$r] <= $x) {
                    $ans += $r - $l;
                    $l++;
                } else $r--;
            }
            return $ans;
        };
        return $count($upper) - $count($lower - 1);
    }
}
''')

add("2564_substring_xor_queries", r'''<?php
// LeetCode 2564 - Substring XOR Queries
// https://leetcode.com/problems/substring-xor-queries/

class Solution {
    function substringXorQueries($s, $queries) {
        $pos = [];
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            if ($s[$i] === '0') {
                if (!isset($pos[0])) $pos[0] = [$i, $i];
                continue;
            }
            $val = 0;
            for ($j = $i; $j < $n && $j < $i + 30; $j++) {
                $val = $val * 2 + (ord($s[$j]) - 48);
                if (!isset($pos[$val])) $pos[$val] = [$i, $j];
            }
        }
        $ans = [];
        foreach ($queries as $q) {
            $need = $q[0] ^ $q[1];
            $ans[] = isset($pos[$need]) ? $pos[$need] : [-1, -1];
        }
        return $ans;
    }
}
''')

add("2565_subsequence_with_the_minimum_score", r'''<?php
// LeetCode 2565 - Subsequence With the Minimum Score
// https://leetcode.com/problems/subsequence-with-the-minimum-score/

class Solution {
    function minimumScore($s, $t) {
        $n = strlen($s);
        $m = strlen($t);
        $left = array_fill(0, $m, -1);
        $right = array_fill(0, $m, -1);
        $j = 0;
        for ($i = 0; $i < $n && $j < $m; $i++) {
            if ($s[$i] === $t[$j]) {
                $left[$j] = $i;
                $j++;
            }
        }
        $j = $m - 1;
        for ($i = $n - 1; $i >= 0 && $j >= 0; $i--) {
            if ($s[$i] === $t[$j]) {
                $right[$j] = $i;
                $j--;
            }
        }
        if ($m > 0 && $left[$m - 1] !== -1) return 0;
        $ans = $m;
        for ($i = 0; $i < $m; $i++) {
            if ($right[$i] !== -1) {
                if ($i < $ans) $ans = $i;
                break;
            }
        }
        for ($i = $m - 1; $i >= 0; $i--) {
            if ($left[$i] !== -1) {
                if ($m - 1 - $i < $ans) $ans = $m - 1 - $i;
                break;
            }
        }
        $j = 0;
        for ($i = 0; $i < $m; $i++) {
            if ($left[$i] === -1) break;
            while ($j < $m && ($right[$j] === -1 || $right[$j] <= $left[$i])) $j++;
            if ($j < $m) {
                $rem = $j - $i - 1;
                if ($rem < $ans) $ans = $rem;
            }
        }
        return $ans;
    }
}
''')

add("2566_maximum_difference_by_remapping_a_digit", r'''<?php
// LeetCode 2566 - Maximum Difference by Remapping a Digit
// https://leetcode.com/problems/maximum-difference-by-remapping-a-digit/

class Solution {
    function minMaxDifference($num) {
        $s = (string)$num;
        $remap = function($from, $to) use ($s) {
            $v = 0;
            $n = strlen($s);
            for ($i = 0; $i < $n; $i++) {
                $d = $s[$i] === $from ? $to : $s[$i];
                $v = $v * 10 + (ord($d) - 48);
            }
            return $v;
        };
        $maxV = $num;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            if ($s[$i] !== '9') {
                $maxV = $remap($s[$i], '9');
                break;
            }
        }
        $minV = $remap($s[0], '0');
        return $maxV - $minV;
    }
}
''')

add("2567_minimum_score_by_changing_two_elements", r'''<?php
// LeetCode 2567 - Minimum Score by Changing Two Elements
// https://leetcode.com/problems/minimum-score-by-changing-two-elements/

class Solution {
    function minimizeSum($nums) {
        sort($nums);
        $n = count($nums);
        return min($nums[$n - 1] - $nums[2], $nums[$n - 3] - $nums[0], $nums[$n - 2] - $nums[1]);
    }
}
''')

add("2568_minimum_impossible_or", r'''<?php
// LeetCode 2568 - Minimum Impossible OR
// https://leetcode.com/problems/minimum-impossible-or/

class Solution {
    function minImpossibleOR($nums) {
        $set = [];
        foreach ($nums as $x) $set[$x] = true;
        $x = 1;
        while (isset($set[$x])) $x <<= 1;
        return $x;
    }
}
''')

add("2569_handling_sum_queries_after_update", r'''<?php
// LeetCode 2569 - Handling Sum Queries After Update
// https://leetcode.com/problems/handling-sum-queries-after-update/

class Solution {
    function handleQuery($nums1, $nums2, $queries) {
        $n = count($nums1);
        $ones = array_fill(0, 4 * $n, 0);
        $lazy = array_fill(0, 4 * $n, false);
        $build = function($idx, $l, $r) use (&$build, &$ones, $nums1) {
            if ($l === $r) {
                $ones[$idx] = $nums1[$l];
                return;
            }
            $m = ($l + $r) >> 1;
            $build($idx * 2, $l, $m);
            $build($idx * 2 + 1, $m + 1, $r);
            $ones[$idx] = $ones[$idx * 2] + $ones[$idx * 2 + 1];
        };
        $apply = function($idx, $l, $r) use (&$ones, &$lazy) {
            $ones[$idx] = ($r - $l + 1) - $ones[$idx];
            $lazy[$idx] = !$lazy[$idx];
        };
        $push = function($idx, $l, $r) use (&$lazy, $apply) {
            if ($lazy[$idx] && $l !== $r) {
                $m = ($l + $r) >> 1;
                $apply($idx * 2, $l, $m);
                $apply($idx * 2 + 1, $m + 1, $r);
                $lazy[$idx] = false;
            }
        };
        $update = function($idx, $l, $r, $ql, $qr) use (&$update, &$ones, $push, $apply) {
            if ($ql <= $l && $r <= $qr) {
                $apply($idx, $l, $r);
                return;
            }
            $push($idx, $l, $r);
            $m = ($l + $r) >> 1;
            if ($ql <= $m) $update($idx * 2, $l, $m, $ql, $qr);
            if ($qr > $m) $update($idx * 2 + 1, $m + 1, $r, $ql, $qr);
            $ones[$idx] = $ones[$idx * 2] + $ones[$idx * 2 + 1];
        };
        $build(1, 0, $n - 1);
        $sum2 = 0;
        foreach ($nums2 as $x) $sum2 += $x;
        $ans = [];
        foreach ($queries as $q) {
            if ($q[0] === 1) $update(1, 0, $n - 1, $q[1], $q[2]);
            else if ($q[0] === 2) $sum2 += $q[1] * $ones[1];
            else $ans[] = $sum2;
        }
        return $ans;
    }
}
''')

add("2570_merge_two_2d_arrays_by_summing_values", r'''<?php
// LeetCode 2570 - Merge Two 2D Arrays by Summing Values
// https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/

class Solution {
    function mergeArrays($nums1, $nums2) {
        $ans = [];
        $i = 0;
        $j = 0;
        $n1 = count($nums1);
        $n2 = count($nums2);
        while ($i < $n1 && $j < $n2) {
            if ($nums1[$i][0] === $nums2[$j][0]) {
                $ans[] = [$nums1[$i][0], $nums1[$i][1] + $nums2[$j][1]];
                $i++;
                $j++;
            } else if ($nums1[$i][0] < $nums2[$j][0]) {
                $ans[] = [$nums1[$i][0], $nums1[$i][1]];
                $i++;
            } else {
                $ans[] = [$nums2[$j][0], $nums2[$j][1]];
                $j++;
            }
        }
        while ($i < $n1) {
            $ans[] = [$nums1[$i][0], $nums1[$i][1]];
            $i++;
        }
        while ($j < $n2) {
            $ans[] = [$nums2[$j][0], $nums2[$j][1]];
            $j++;
        }
        return $ans;
    }
}
''')

add("2571_minimum_operations_to_reduce_an_integer_to_0", r'''<?php
// LeetCode 2571 - Minimum Operations to Reduce an Integer to 0
// https://leetcode.com/problems/minimum-operations-to-reduce-an-integer-to-0/

class Solution {
    function minOperations($n) {
        $ans = 0;
        while ($n > 0) {
            if (($n & 3) === 3) {
                $n++;
                $ans++;
            } else if (($n & 1) !== 0) {
                $n--;
                $ans++;
            } else {
                $n >>= 1;
            }
        }
        return $ans;
    }
}
''')

add("2572_count_the_number_of_square_free_subsets", r'''<?php
// LeetCode 2572 - Count the Number of Square-Free Subsets
// https://leetcode.com/problems/count-the-number-of-square-free-subsets/

class Solution {
    function squareFreeSubsets($nums) {
        $MOD = 1000000007;
        $PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29];
        $freq = [];
        foreach ($nums as $x) $freq[$x] = ($freq[$x] ?? 0) + 1;
        $maskOf = function($x) use ($PRIMES) {
            $mask = 0;
            for ($i = 0; $i < count($PRIMES); $i++) {
                $p = $PRIMES[$i];
                $cnt = 0;
                while ($x % $p === 0) {
                    $x = intdiv($x, $p);
                    $cnt++;
                    if ($cnt > 1) return -1;
                }
                if ($cnt === 1) $mask |= 1 << $i;
            }
            return $mask;
        };
        $dp = array_fill(0, 1 << 10, 0);
        $dp[0] = 1;
        foreach ($freq as $x => $c) {
            if ($x === 1) continue;
            $m = $maskOf($x);
            if ($m < 0) continue;
            for ($state = (1 << 10) - 1; $state >= 0; $state--) {
                if (($state & $m) === 0) {
                    $dp[$state | $m] = ($dp[$state | $m] + $dp[$state] * $c) % $MOD;
                }
            }
        }
        $ans = 0;
        foreach ($dp as $v) $ans = ($ans + $v) % $MOD;
        $ones = $freq[1] ?? 0;
        $mul = 1;
        for ($i = 0; $i < $ones; $i++) $mul = $mul * 2 % $MOD;
        $ans = $ans * $mul % $MOD;
        $ans = ($ans - 1 + $MOD) % $MOD;
        return $ans;
    }
}
''')

add("2573_find_the_string_with_lcp", r'''<?php
// LeetCode 2573 - Find the String with LCP
// https://leetcode.com/problems/find-the-string-with-lcp/

class Solution {
    function findTheString($lcp) {
        $n = count($lcp);
        $s = array_fill(0, $n, 0);
        $c = 97;
        for ($i = 0; $i < $n; $i++) {
            if ($s[$i] !== 0) continue;
            if ($c > 122) return "";
            $s[$i] = $c;
            for ($j = $i + 1; $j < $n; $j++) {
                if ($lcp[$i][$j] > 0) $s[$j] = $c;
            }
            $c++;
        }
        for ($i = $n - 1; $i >= 0; $i--) {
            for ($j = $n - 1; $j >= 0; $j--) {
                $v = 0;
                if ($s[$i] === $s[$j]) {
                    $v = 1;
                    if ($i + 1 < $n && $j + 1 < $n) $v += $lcp[$i + 1][$j + 1];
                }
                if ($lcp[$i][$j] !== $v) return "";
            }
        }
        $out = '';
        for ($i = 0; $i < $n; $i++) $out .= chr($s[$i]);
        return $out;
    }
}
''')

add("2574_left_and_right_sum_differences", r'''<?php
// LeetCode 2574 - Left and Right Sum Differences
// https://leetcode.com/problems/left-and-right-sum-differences/

class Solution {
    function leftRightDifference($nums) {
        $total = 0;
        foreach ($nums as $x) $total += $x;
        $n = count($nums);
        $ans = array_fill(0, $n, 0);
        $left = 0;
        for ($i = 0; $i < $n; $i++) {
            $right = $total - $left - $nums[$i];
            $ans[$i] = abs($left - $right);
            $left += $nums[$i];
        }
        return $ans;
    }
}
''')

add("2575_find_the_divisibility_array_of_a_string", r'''<?php
// LeetCode 2575 - Find the Divisibility Array of a String
// https://leetcode.com/problems/find-the-divisibility-array-of-a-string/

class Solution {
    function divisibilityArray($word, $m) {
        $n = strlen($word);
        $ans = array_fill(0, $n, 0);
        $cur = 0;
        for ($i = 0; $i < $n; $i++) {
            $cur = ($cur * 10 + (ord($word[$i]) - 48)) % $m;
            if ($cur === 0) $ans[$i] = 1;
        }
        return $ans;
    }
}
''')

add("2576_find_the_maximum_number_of_marked_indices", r'''<?php
// LeetCode 2576 - Find the Maximum Number of Marked Indices
// https://leetcode.com/problems/find-the-maximum-number-of-marked-indices/

class Solution {
    function maxNumOfMarkedIndices($nums) {
        sort($nums);
        $n = count($nums);
        $i = 0;
        $ans = 0;
        for ($j = intdiv($n + 1, 2); $j < $n; $j++) {
            if (2 * $nums[$i] <= $nums[$j]) {
                $ans += 2;
                $i++;
            }
        }
        return $ans;
    }
}
''')

add("2577_minimum_time_to_visit_a_cell_in_a_grid", r'''<?php
// LeetCode 2577 - Minimum Time to Visit a Cell In a Grid
// https://leetcode.com/problems/minimum-time-to-visit-a-cell-in-a-grid/

class Solution {
    function minimumTime($grid) {
        if ($grid[0][1] > 1 && $grid[1][0] > 1) return -1;
        $m = count($grid);
        $n = count($grid[0]);
        $INF = 1 << 30;
        $dist = [];
        for ($i = 0; $i < $m; $i++) $dist[] = array_fill(0, $n, $INF);
        $h = new SplPriorityQueue();
        $h->insert([0, 0, 0], 0);
        $dist[0][0] = 0;
        $dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];
        while (!$h->isEmpty()) {
            $cur = $h->extract();
            $t = $cur[0];
            $r = $cur[1];
            $c = $cur[2];
            if ($r === $m - 1 && $c === $n - 1) return $t;
            if ($t > $dist[$r][$c]) continue;
            foreach ($dirs as $d) {
                $nr = $r + $d[0];
                $nc = $c + $d[1];
                if ($nr < 0 || $nr >= $m || $nc < 0 || $nc >= $n) continue;
                $nt = $t + 1;
                if ($nt < $grid[$nr][$nc]) {
                    $wait = $grid[$nr][$nc] - $nt;
                    if ($wait % 2 === 1) $wait++;
                    $nt += $wait;
                }
                if ($nt < $dist[$nr][$nc]) {
                    $dist[$nr][$nc] = $nt;
                    $h->insert([$nt, $nr, $nc], -$nt);
                }
            }
        }
        return -1;
    }
}
''')

add("2578_split_with_minimum_sum", r'''<?php
// LeetCode 2578 - Split With Minimum Sum
// https://leetcode.com/problems/split-with-minimum-sum/

class Solution {
    function splitNum($num) {
        $digits = [];
        while ($num > 0) {
            $digits[] = $num % 10;
            $num = intdiv($num, 10);
        }
        sort($digits);
        $a = 0;
        $b = 0;
        $n = count($digits);
        for ($i = 0; $i < $n; $i++) {
            if ($i % 2 === 0) $a = $a * 10 + $digits[$i];
            else $b = $b * 10 + $digits[$i];
        }
        return $a + $b;
    }
}
''')

add("2579_count_total_number_of_colored_cells", r'''<?php
// LeetCode 2579 - Count Total Number of Colored Cells
// https://leetcode.com/problems/count-total-number-of-colored-cells/

class Solution {
    function coloredCells($n) {
        return 1 + 2 * $n * ($n - 1);
    }
}
''')

add("2580_count_ways_to_group_overlapping_ranges", r'''<?php
// LeetCode 2580 - Count Ways to Group Overlapping Ranges
// https://leetcode.com/problems/count-ways-to-group-overlapping-ranges/

class Solution {
    function countWays($ranges) {
        $MOD = 1000000007;
        usort($ranges, function($a, $b) { return $a[0] <=> $b[0]; });
        $groups = 0;
        $end = -1;
        foreach ($ranges as $r) {
            if ($r[0] > $end) {
                $groups++;
                $end = $r[1];
            } else if ($r[1] > $end) {
                $end = $r[1];
            }
        }
        $ans = 1;
        for ($i = 0; $i < $groups; $i++) $ans = $ans * 2 % $MOD;
        return $ans;
    }
}
''')

add("2581_count_number_of_possible_root_nodes", r'''<?php
// LeetCode 2581 - Count Number of Possible Root Nodes
// https://leetcode.com/problems/count-number-of-possible-root-nodes/

class Solution {
    function rootCount($edges, $guesses, $k) {
        $n = count($edges) + 1;
        $g = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $g[$e[0]][] = $e[1];
            $g[$e[1]][] = $e[0];
        }
        $guessSet = [];
        foreach ($guesses as $gu) $guessSet[$gu[0] . ',' . $gu[1]] = true;
        $dfs1 = function($u, $p) use (&$dfs1, &$g, &$guessSet) {
            $cnt = 0;
            foreach ($g[$u] as $v) {
                if ($v === $p) continue;
                if (isset($guessSet[$u . ',' . $v])) $cnt++;
                $cnt += $dfs1($v, $u);
            }
            return $cnt;
        };
        $ans = 0;
        $dfs2 = function($u, $p, $cur) use (&$dfs2, &$g, &$guessSet, $k, &$ans) {
            if ($cur >= $k) $ans++;
            foreach ($g[$u] as $v) {
                if ($v === $p) continue;
                $nxt = $cur;
                if (isset($guessSet[$u . ',' . $v])) $nxt--;
                if (isset($guessSet[$v . ',' . $u])) $nxt++;
                $dfs2($v, $u, $nxt);
            }
        };
        $baseCnt = $dfs1(0, -1);
        $dfs2(0, -1, $baseCnt);
        return $ans;
    }
}
''')

add("2582_pass_the_pillow", r'''<?php
// LeetCode 2582 - Pass the Pillow
// https://leetcode.com/problems/pass-the-pillow/

class Solution {
    function passThePillow($n, $time) {
        $cycle = 2 * ($n - 1);
        $t = $time % $cycle;
        if ($t < $n) return 1 + $t;
        return $n - ($t - ($n - 1));
    }
}
''')

add("2583_kth_largest_sum_in_a_binary_tree", r'''<?php
// LeetCode 2583 - Kth Largest Sum in a Binary Tree
// https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/

class TreeNode {
    public $val = null;
    public $left = null;
    public $right = null;
    function __construct($val = 0, $left = null, $right = null) {
        $this->val = $val;
        $this->left = $left;
        $this->right = $right;
    }
}

class Solution {
    function kthLargestLevelSum($root, $k) {
        if (!$root) return -1;
        $sums = [];
        $q = [$root];
        while ($q) {
            $sz = count($q);
            $s = 0;
            for ($i = 0; $i < $sz; $i++) {
                $node = array_shift($q);
                $s += $node->val;
                if ($node->left) $q[] = $node->left;
                if ($node->right) $q[] = $node->right;
            }
            $sums[] = $s;
        }
        rsort($sums);
        if ($k > count($sums)) return -1;
        return $sums[$k - 1];
    }
}
''')

add("2584_split_the_array_to_make_coprime_products", r'''<?php
// LeetCode 2584 - Split the Array to Make Coprime Products
// https://leetcode.com/problems/split-the-array-to-make-coprime-products/

class Solution {
    function findValidSplit($nums) {
        $first = [];
        $last = [];
        $factorize = function($x, $idx) use (&$first, &$last) {
            for ($p = 2; $p * $p <= $x; $p++) {
                if ($x % $p === 0) {
                    if (!isset($first[$p])) $first[$p] = $idx;
                    $last[$p] = $idx;
                    while ($x % $p === 0) $x = intdiv($x, $p);
                }
            }
            if ($x > 1) {
                if (!isset($first[$x])) $first[$x] = $idx;
                $last[$x] = $idx;
            }
        };
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) $factorize($nums[$i], $i);
        $far = 0;
        for ($i = 0; $i < $n - 1; $i++) {
            $x = $nums[$i];
            for ($p = 2; $p * $p <= $x; $p++) {
                if ($x % $p === 0) {
                    if ($last[$p] > $far) $far = $last[$p];
                    while ($x % $p === 0) $x = intdiv($x, $p);
                }
            }
            if ($x > 1 && $last[$x] > $far) $far = $last[$x];
            if ($far === $i) return $i;
        }
        return -1;
    }
}
''')

add("2585_number_of_ways_to_earn_points", r'''<?php
// LeetCode 2585 - Number of Ways to Earn Points
// https://leetcode.com/problems/number-of-ways-to-earn-points/

class Solution {
    function waysToReachTarget($target, $types) {
        $MOD = 1000000007;
        $dp = array_fill(0, $target + 1, 0);
        $dp[0] = 1;
        foreach ($types as $t) {
            $count = $t[0];
            $marks = $t[1];
            for ($s = $target; $s >= 0; $s--) {
                for ($k = 1; $k <= $count && $s - $k * $marks >= 0; $k++) {
                    $dp[$s] = ($dp[$s] + $dp[$s - $k * $marks]) % $MOD;
                }
            }
        }
        return $dp[$target];
    }
}
''')

written = 0
for folder, body in SOLUTIONS.items():
    path = ROOT / folder / "solution.php"
    path.write_text(body, encoding="utf-8", newline="\n")
    written += 1
print(f"wrote {written}")

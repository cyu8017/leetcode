#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
SOLUTIONS = {}

def add(folder, body):
    SOLUTIONS[folder] = body


add("3640_trionic_array_ii", r'''<?php
// LeetCode 3640 - Trionic Array II
// https://leetcode.com/problems/trionic-array-ii/

class Solution {
    function maxSumTrionic($nums) {
        $n = count($nums);
        $i = 0;
        $ans = -PHP_INT_MAX;
        while ($i < $n) {
            $l = $i;
            for ($i++; $i < $n && $nums[$i - 1] < $nums[$i];) $i++;
            if ($i === $l + 1) continue;
            $p = $i - 1;
            $s = $nums[$p - 1] + $nums[$p];
            while ($i < $n && $nums[$i - 1] > $nums[$i]) {
                $s += $nums[$i];
                $i++;
            }
            if ($i === $p + 1 || $i === $n || $nums[$i - 1] === $nums[$i]) continue;
            $q = $i - 1;
            $s += $nums[$i];
            $i++;
            $mx = 0;
            $t = 0;
            while ($i < $n && $nums[$i - 1] < $nums[$i]) {
                $t += $nums[$i];
                $i++;
                $mx = max($mx, $t);
            }
            $s += $mx;
            $mx = $t = 0;
            for ($j = $p - 2; $j >= $l; $j--) {
                $t += $nums[$j];
                $mx = max($mx, $t);
            }
            $s += $mx;
            $ans = max($ans, $s);
            $i = $q;
        }
        return $ans;
    }
}
''')

add("3641_longest_semi_repeating_subarray", r'''<?php
// LeetCode 3641 - Longest Semi-Repeating Subarray
// https://leetcode.com/problems/longest-semi-repeating-subarray/

class Solution {
    function longestSubarray($nums, $k) {
        $cnt = [];
        $ans = 0;
        $cur = 0;
        $l = 0;
        $n = count($nums);
        for ($r = 0; $r < $n; $r++) {
            $c = (isset($cnt[$nums[$r]]) ? $cnt[$nums[$r]] : 0) + 1;
            $cnt[$nums[$r]] = $c;
            if ($c === 2) $cur++;
            while ($cur > $k) {
                $c2 = (isset($cnt[$nums[$l]]) ? $cnt[$nums[$l]] : 0) - 1;
                $cnt[$nums[$l]] = $c2;
                if ($c2 === 1) $cur--;
                $l++;
            }
            $ans = max($ans, $r - $l + 1);
        }
        return $ans;
    }
}
''')

add("3643_flip_square_submatrix_vertically", r'''<?php
// LeetCode 3643 - Flip Square Submatrix Vertically
// https://leetcode.com/problems/flip-square-submatrix-vertically/

class Solution {
    function reverseSubmatrix($grid, $x, $y, $k) {
        for ($i = $x; $i < $x + intdiv($k, 2); $i++) {
            $i2 = $x + $k - 1 - ($i - $x);
            for ($j = $y; $j < $y + $k; $j++) {
                $tmp = $grid[$i][$j];
                $grid[$i][$j] = $grid[$i2][$j];
                $grid[$i2][$j] = $tmp;
            }
        }
        return $grid;
    }
}
''')

add("3644_maximum_k_to_sort_a_permutation", r'''<?php
// LeetCode 3644 - Maximum K to Sort a Permutation
// https://leetcode.com/problems/maximum-k-to-sort-a-permutation/

class Solution {
    function sortPermutation($nums) {
        $ans = -1;
        $n = count($nums);
        for ($i = 0; $i < $n; $i++)
            if ($i !== $nums[$i]) $ans &= $nums[$i];
        return max($ans, 0);
    }
}
''')

add("3645_maximum_total_from_optimal_activation_order", r'''<?php
// LeetCode 3645 - Maximum Total from Optimal Activation Order
// https://leetcode.com/problems/maximum-total-from-optimal-activation-order/

class Solution {
    function maxTotal($value, $limit) {
        $g = [];
        $n = count($value);
        for ($i = 0; $i < $n; $i++) {
            if (!isset($g[$limit[$i]])) $g[$limit[$i]] = [];
            $g[$limit[$i]][] = $value[$i];
        }
        $ans = 0;
        foreach ($g as $lim => $vs) {
            rsort($vs);
            $m = min($lim, count($vs));
            for ($i = 0; $i < $m; $i++) $ans += $vs[$i];
        }
        return $ans;
    }
}
''')

add("3646_next_special_palindrome_number", r'''<?php
// LeetCode 3646 - Next Special Palindrome Number
// https://leetcode.com/problems/next-special-palindrome-number/

class Solution {
    function specialPalindrome($n) {
        $cands = [];
        $halfCnt = [];
        $mid = 0;
        $halfLen = 0;
        $dfs = function($pos, $cur) use (&$dfs, &$cands, &$halfCnt, &$mid, &$halfLen) {
            if ($pos === $halfLen) {
                $left = implode('', $cur);
                $s = $left;
                if ($mid > 0) $s .= $mid;
                for ($i = strlen($left) - 1; $i >= 0; $i--) $s .= $left[$i];
                $cands[] = (int)$s;
                return;
            }
            for ($d = 1; $d <= 9; $d++) {
                if ($halfCnt[$d] === 0) continue;
                $halfCnt[$d]--;
                $cur[] = $d;
                $dfs($pos + 1, $cur);
                array_pop($cur);
                $halfCnt[$d]++;
            }
        };
        $gen = function($mask) use (&$cands, &$halfCnt, &$mid, &$halfLen, $dfs) {
            $total = 0;
            $odd = 0;
            for ($d = 1; $d <= 9; $d++) {
                if ((($mask >> $d) & 1) !== 0) {
                    $total += $d;
                    if ($d % 2 === 1) $odd++;
                }
            }
            if ($total === 0 || $total > 18 || $odd > 1) return;
            $halfCnt = array_fill(0, 10, 0);
            $mid = 0;
            for ($d = 1; $d <= 9; $d++) {
                if ((($mask >> $d) & 1) === 0) continue;
                $halfCnt[$d] = intdiv($d, 2);
                if ($d % 2 === 1) $mid = $d;
            }
            $halfLen = intdiv($total, 2);
            $dfs(0, []);
        };
        for ($mask = 1; $mask < (1 << 10); $mask++) {
            if (($mask & 1) !== 0) continue;
            $gen($mask);
        }
        sort($cands);
        foreach ($cands as $v)
            if ($v > $n) return $v;
        return -1;
    }
}
''')

add("3647_maximum_weight_in_two_bags", r'''<?php
// LeetCode 3647 - Maximum Weight in Two Bags
// https://leetcode.com/problems/maximum-weight-in-two-bags/

class Solution {
    function maxWeight($weights, $w1, $w2) {
        $f = [];
        for ($j = 0; $j <= $w1; $j++) $f[$j] = array_fill(0, $w2 + 1, 0);
        foreach ($weights as $x) {
            for ($j = $w1; $j >= 0; $j--) {
                for ($k = $w2; $k >= 0; $k--) {
                    if ($x <= $j) $f[$j][$k] = max($f[$j][$k], $f[$j - $x][$k] + $x);
                    if ($x <= $k) $f[$j][$k] = max($f[$j][$k], $f[$j][$k - $x] + $x);
                }
            }
        }
        return $f[$w1][$w2];
    }
}
''')

add("3648_minimum_sensors_to_cover_grid", r'''<?php
// LeetCode 3648 - Minimum Sensors to Cover Grid
// https://leetcode.com/problems/minimum-sensors-to-cover-grid/

class Solution {
    function minSensors($n, $m, $k) {
        $cover = 2 * $k + 1;
        return (int)ceil($n / $cover) * (int)ceil($m / $cover);
    }
}
''')

add("3649_number_of_perfect_pairs", r'''<?php
// LeetCode 3649 - Number of Perfect Pairs
// https://leetcode.com/problems/number-of-perfect-pairs/

class Solution {
    function perfectPairs($nums) {
        $n = count($nums);
        $absNums = [];
        foreach ($nums as $x) $absNums[] = abs($x);
        sort($absNums);
        $ans = 0;
        $j = 0;
        for ($i = 0; $i < $n; $i++) {
            if ($j < $i + 1) $j = $i + 1;
            while ($j < $n && $absNums[$j] <= 2 * $absNums[$i]) $j++;
            $ans += $j - $i - 1;
        }
        return $ans;
    }
}
''')

add("3650_minimum_cost_path_with_edge_reversals", r'''<?php
// LeetCode 3650 - Minimum Cost Path with Edge Reversals
// https://leetcode.com/problems/minimum-cost-path-with-edge-reversals/

class Solution {
    function minCost($n, $edges) {
        $g = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $u = $e[0];
            $v = $e[1];
            $w = $e[2];
            $g[$u][] = [$v, $w];
            $g[$v][] = [$u, $w * 2];
        }
        $inf = 1073741823;
        $dist = array_fill(0, $n, $inf);
        $dist[0] = 0;
        $pq = new SplPriorityQueue();
        $pq->setExtractFlags(SplPriorityQueue::EXTR_DATA);
        $pq->insert([0, 0], 0);
        while (!$pq->isEmpty()) {
            $cur = $pq->extract();
            $d = $cur[0];
            $u = $cur[1];
            if ($d > $dist[$u]) continue;
            if ($u === $n - 1) return $d;
            foreach ($g[$u] as $e) {
                $v = $e[0];
                $w = $e[1];
                $nd = $d + $w;
                if ($nd < $dist[$v]) {
                    $dist[$v] = $nd;
                    $pq->insert([$nd, $v], -$nd);
                }
            }
        }
        return -1;
    }
}
''')

add("3651_minimum_cost_path_with_teleportations", r'''<?php
// LeetCode 3651 - Minimum Cost Path with Teleportations
// https://leetcode.com/problems/minimum-cost-path-with-teleportations/

class Solution {
    function minCost($grid, $k) {
        $m = count($grid);
        $n = count($grid[0]);
        $inf = 536870911;
        $f = [];
        for ($t = 0; $t <= $k; $t++) {
            $f[$t] = [];
            for ($i = 0; $i < $m; $i++) $f[$t][$i] = array_fill(0, $n, $inf);
        }
        $f[0][0][0] = 0;
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if ($i > 0) $f[0][$i][$j] = min($f[0][$i][$j], $f[0][$i - 1][$j] + $grid[$i][$j]);
                if ($j > 0) $f[0][$i][$j] = min($f[0][$i][$j], $f[0][$i][$j - 1] + $grid[$i][$j]);
            }
        }
        $g = [];
        for ($i = 0; $i < $m; $i++)
            for ($j = 0; $j < $n; $j++) {
                if (!isset($g[$grid[$i][$j]])) $g[$grid[$i][$j]] = [];
                $g[$grid[$i][$j]][] = [$i, $j];
            }
        $keys = array_keys($g);
        rsort($keys);
        for ($t = 1; $t <= $k; $t++) {
            $mn = $inf;
            foreach ($keys as $key) {
                $pos = $g[$key];
                foreach ($pos as $p) $mn = min($mn, $f[$t - 1][$p[0]][$p[1]]);
                foreach ($pos as $p) $f[$t][$p[0]][$p[1]] = $mn;
            }
            for ($i = 0; $i < $m; $i++) {
                for ($j = 0; $j < $n; $j++) {
                    if ($i > 0) $f[$t][$i][$j] = min($f[$t][$i][$j], $f[$t][$i - 1][$j] + $grid[$i][$j]);
                    if ($j > 0) $f[$t][$i][$j] = min($f[$t][$i][$j], $f[$t][$i][$j - 1] + $grid[$i][$j]);
                }
            }
        }
        $ans = $inf;
        for ($t = 0; $t <= $k; $t++) $ans = min($ans, $f[$t][$m - 1][$n - 1]);
        return $ans;
    }
}
''')

add("3652_best_time_to_buy_and_sell_stock_using_strategy", r'''<?php
// LeetCode 3652 - Best Time to Buy and Sell Stock using Strategy
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-using-strategy/

class Solution {
    function maxProfit($prices, $strategy, $k) {
        $n = count($prices);
        $s = array_fill(0, $n + 1, 0);
        $t = array_fill(0, $n + 1, 0);
        for ($i = 1; $i <= $n; $i++) {
            $s[$i] = $s[$i - 1] + $prices[$i - 1] * $strategy[$i - 1];
            $t[$i] = $t[$i - 1] + $prices[$i - 1];
        }
        $ans = $s[$n];
        for ($i = $k; $i <= $n; $i++)
            $ans = max($ans, $s[$n] - ($s[$i] - $s[$i - $k]) + ($t[$i] - $t[$i - intdiv($k, 2)]));
        return $ans;
    }
}
''')

add("3653_xor_after_range_multiplication_queries_i", r'''<?php
// LeetCode 3653 - XOR After Range Multiplication Queries I
// https://leetcode.com/problems/xor-after-range-multiplication-queries-i/

class Solution {
    function xorAfterQueries($nums, $queries) {
        $mod = 1000000007;
        foreach ($queries as $q) {
            $l = $q[0];
            $r = $q[1];
            $k = $q[2];
            $v = $q[3];
            for ($idx = $l; $idx <= $r; $idx += $k)
                $nums[$idx] = ($nums[$idx] * $v) % $mod;
        }
        $ans = 0;
        foreach ($nums as $x) $ans ^= $x;
        return $ans;
    }
}
''')

add("3654_minimum_sum_after_divisible_sum_deletions", r'''<?php
// LeetCode 3654 - Minimum Sum After Divisible Sum Deletions
// https://leetcode.com/problems/minimum-sum-after-divisible-sum-deletions/

class Solution {
    function minArraySum($nums, $k) {
        $n = count($nums);
        $prefix = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; $i++) $prefix[$i + 1] = ($prefix[$i] + $nums[$i]) % $k;
        $inf = PHP_INT_MAX >> 1;
        $dp = array_fill(0, $n + 1, 0);
        $best = array_fill(0, $k, $inf);
        $best[0] = 0;
        for ($i = 1; $i <= $n; $i++) {
            $dp[$i] = $dp[$i - 1] + $nums[$i - 1];
            if ($best[$prefix[$i]] < $dp[$i]) $dp[$i] = $best[$prefix[$i]];
            if ($dp[$i] < $best[$prefix[$i]]) $best[$prefix[$i]] = $dp[$i];
        }
        return $dp[$n];
    }
}
''')

add("3655_xor_after_range_multiplication_queries_ii", r'''<?php
// LeetCode 3655 - XOR After Range Multiplication Queries II
// https://leetcode.com/problems/xor-after-range-multiplication-queries-ii/

class Solution {
    function xorAfterQueries($nums, $queries) {
        $MOD = 1000000007;
        $n = count($nums);
        $byK = [];
        foreach ($queries as $q) {
            if (!isset($byK[$q[2]])) $byK[$q[2]] = [];
            $byK[$q[2]][] = $q;
        }
        $res = $nums;
        foreach ($byK as $list) {
            $fac = array_fill(0, $n, 1);
            foreach ($list as $u)
                for ($i = $u[0]; $i <= $u[1]; $i += $u[2])
                    $fac[$i] = ($fac[$i] * $u[3]) % $MOD;
            for ($i = 0; $i < $n; $i++)
                $res[$i] = ($res[$i] * $fac[$i]) % $MOD;
        }
        $ans = 0;
        foreach ($res as $v) $ans ^= $v;
        return $ans;
    }
}
''')

add("3656_determine_if_a_simple_graph_exists", r'''<?php
// LeetCode 3656 - Determine if a Simple Graph Exists
// https://leetcode.com/problems/determine-if-a-simple-graph-exists/

class Solution {
    function simpleGraphExists($degrees) {
        $n = count($degrees);
        $d = $degrees;
        rsort($d);
        $sum = 0;
        foreach ($d as $x) {
            if ($x < 0 || $x >= $n) return false;
            $sum += $x;
        }
        if ($sum % 2 === 1) return false;
        $prefix = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; $i++) $prefix[$i + 1] = $prefix[$i] + $d[$i];
        for ($k = 1; $k <= $n; $k++) {
            $right = 0;
            for ($i = $k; $i < $n; $i++) $right += $d[$i] < $k ? $d[$i] : $k;
            if ($prefix[$k] > $k * ($k - 1) + $right) return false;
        }
        return true;
    }
}
''')

add("3658_gcd_of_odd_and_even_sums", r'''<?php
// LeetCode 3658 - GCD of Odd and Even Sums
// https://leetcode.com/problems/gcd-of-odd-and-even-sums/

class Solution {
    function gcdOfOddEvenSums($n) {
        return $n;
    }
}
''')

add("3659_partition_array_into_k_distinct_groups", r'''<?php
// LeetCode 3659 - Partition Array Into K-Distinct Groups
// https://leetcode.com/problems/partition-array-into-k-distinct-groups/

class Solution {
    function partitionArray($nums, $k) {
        $n = count($nums);
        if ($n % $k !== 0) return false;
        $m = intdiv($n, $k);
        $mx = 0;
        foreach ($nums as $x) $mx = max($mx, $x);
        $cnt = array_fill(0, $mx + 1, 0);
        foreach ($nums as $x)
            if (++$cnt[$x] > $m) return false;
        return true;
    }
}
''')

add("3660_jump_game_ix", r'''<?php
// LeetCode 3660 - Jump Game IX
// https://leetcode.com/problems/jump-game-ix/

class Solution {
    function maxValue($nums) {
        $n = count($nums);
        $ans = array_fill(0, $n, 0);
        $preMax = array_fill(0, $n, 0);
        $preMax[0] = $nums[0];
        for ($i = 1; $i < $n; $i++) $preMax[$i] = max($preMax[$i - 1], $nums[$i]);
        $sufMin = 1073741823;
        for ($i = $n - 1; $i >= 0; $i--) {
            if ($preMax[$i] > $sufMin) $ans[$i] = $ans[$i + 1];
            else $ans[$i] = $preMax[$i];
            $sufMin = min($sufMin, $nums[$i]);
        }
        return $ans;
    }
}
''')

add("3661_maximum_walls_destroyed_by_robots", r'''<?php
// LeetCode 3661 - Maximum Walls Destroyed by Robots
// https://leetcode.com/problems/maximum-walls-destroyed-by-robots/

class Solution {
    function maxWalls($robots, $distance, $walls) {
        $n = count($robots);
        $arr = [];
        for ($i = 0; $i < $n; $i++) $arr[] = [$robots[$i], $distance[$i]];
        usort($arr, function($a, $b) { return $a[0] <=> $b[0]; });
        sort($walls);
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
        $memo = [];
        $dfs = function($i, $j) use (&$dfs, &$memo, $arr, $walls, $lowerBound) {
            if ($i < 0) return 0;
            $key = ($i << 1) | $j;
            if (isset($memo[$key])) return $memo[$key];
            $left = $arr[$i][0] - $arr[$i][1];
            if ($i > 0) $left = max($left, $arr[$i - 1][0] + 1);
            $l = $lowerBound($walls, $left);
            $r = $lowerBound($walls, $arr[$i][0] + 1);
            $ans = $dfs($i - 1, 0) + ($r - $l);
            $right = $arr[$i][0] + $arr[$i][1];
            if ($i + 1 < count($arr)) {
                if ($j === 0) $right = min($right, $arr[$i + 1][0] - $arr[$i + 1][1] - 1);
                else $right = min($right, $arr[$i + 1][0] - 1);
            }
            $l = $lowerBound($walls, $arr[$i][0]);
            $r = $lowerBound($walls, $right + 1);
            $ans = max($ans, $dfs($i - 1, 1) + ($r - $l));
            $memo[$key] = $ans;
            return $ans;
        };
        return $dfs($n - 1, 1);
    }
}
''')

add("3662_filter_characters_by_frequency", r'''<?php
// LeetCode 3662 - Filter Characters by Frequency
// https://leetcode.com/problems/filter-characters-by-frequency/

class Solution {
    function filterCharacters($s, $k) {
        $cnt = array_fill(0, 26, 0);
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) $cnt[ord($s[$i]) - 97]++;
        $ans = '';
        for ($i = 0; $i < $n; $i++)
            if ($cnt[ord($s[$i]) - 97] < $k) $ans .= $s[$i];
        return $ans;
    }
}
''')

add("3663_find_the_least_frequent_digit", r'''<?php
// LeetCode 3663 - Find The Least Frequent Digit
// https://leetcode.com/problems/find-the-least-frequent-digit/

class Solution {
    function getLeastFrequentDigit($n) {
        $cnt = array_fill(0, 10, 0);
        $ans = 0;
        $f = 1 << 30;
        for (; $n > 0; $n = intdiv($n, 10)) $cnt[$n % 10]++;
        for ($x = 0; $x < 10; $x++) {
            if ($cnt[$x] > 0 && $cnt[$x] < $f) {
                $f = $cnt[$x];
                $ans = $x;
            }
        }
        return $ans;
    }
}
''')

add("3664_two_letter_card_game", r'''<?php
// LeetCode 3664 - Two-Letter Card Game
// https://leetcode.com/problems/two-letter-card-game/

class Solution {
    function score($cards, $x) {
        $pairGroup = function($arr) {
            $total = 0;
            $mx = 0;
            for ($i = 0; $i < 26; $i++) {
                $total += $arr[$i];
                $mx = max($mx, $arr[$i]);
            }
            $pairs = intdiv($total, 2);
            if ($total - $mx < $pairs) $pairs = $total - $mx;
            return [$pairs, $total - 2 * $pairs];
        };
        $xx = 0;
        $left = array_fill(0, 26, 0);
        $right = array_fill(0, 26, 0);
        foreach ($cards as $c) {
            $a = $c[0];
            $b = $c[1];
            if ($a === $x && $b === $x) $xx++;
            else if ($a === $x) $left[ord($b) - 97]++;
            else if ($b === $x) $right[ord($a) - 97]++;
        }
        $lp = $pairGroup($left);
        $rp = $pairGroup($right);
        $ans = $lp[0] + $rp[0];
        $rem = $lp[1] + $rp[1];
        $use = min($xx, $rem);
        $ans += $use;
        $xx -= $use;
        $ans += intdiv($xx, 2);
        return $ans;
    }
}
''')

add("3665_twisted_mirror_path_count", r'''<?php
// LeetCode 3665 - Twisted Mirror Path Count
// https://leetcode.com/problems/twisted-mirror-path-count/

class Solution {
    function uniquePaths($grid) {
        $MOD = 1000000007;
        $m = count($grid);
        $n = count($grid[0]);
        $nextCell = function($i, $j, $di, $dj) use ($grid, $m, $n) {
            $ni = $i + $di;
            $nj = $j + $dj;
            while ($ni >= 0 && $nj >= 0 && $ni < $m && $nj < $n && $grid[$ni][$nj] === 1) {
                if ($dj === 1) { $di = 1; $dj = 0; }
                else { $di = 0; $dj = 1; }
                $ni += $di;
                $nj += $dj;
            }
            if ($ni < 0 || $nj < 0 || $ni >= $m || $nj >= $n) return null;
            return [$ni, $nj];
        };
        $dp = [];
        for ($i = 0; $i < $m; $i++) $dp[$i] = array_fill(0, $n, 0);
        if ($grid[0][0] === 1) return 0;
        $dp[0][0] = 1;
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if ($grid[$i][$j] === 1 || $dp[$i][$j] === 0) continue;
                $a = $nextCell($i, $j, 0, 1);
                if ($a) $dp[$a[0]][$a[1]] = ($dp[$a[0]][$a[1]] + $dp[$i][$j]) % $MOD;
                $b = $nextCell($i, $j, 1, 0);
                if ($b) $dp[$b[0]][$b[1]] = ($dp[$b[0]][$b[1]] + $dp[$i][$j]) % $MOD;
            }
        }
        return $dp[$m - 1][$n - 1];
    }
}
''')

add("3666_minimum_operations_to_equalize_binary_string", r'''<?php
// LeetCode 3666 - Minimum Operations to Equalize Binary String
// https://leetcode.com/problems/minimum-operations-to-equalize-binary-string/

class Solution {
    function minOperations($s, $k) {
        $n = strlen($s);
        $ts = [[], []];
        for ($i = 0; $i <= $n; $i++) $ts[$i % 2][$i] = true;
        $cnt0 = 0;
        for ($i = 0; $i < $n; $i++) if ($s[$i] === '0') $cnt0++;
        unset($ts[$cnt0 % 2][$cnt0]);
        $q = [$cnt0];
        $ans = 0;
        while ($q) {
            $nq = [];
            foreach ($q as $cur) {
                if ($cur === 0) return $ans;
                $l = $cur + $k - 2 * min($cur, $k);
                $r = $cur + $k - 2 * max($k - $n + $cur, 0);
                $t = &$ts[$l % 2];
                $sorted = array_keys($t);
                sort($sorted);
                foreach ($sorted as $it) {
                    if ($it < $l) continue;
                    if ($it > $r) break;
                    $nq[] = $it;
                    unset($t[$it]);
                }
                unset($t);
            }
            $q = $nq;
            $ans++;
        }
        return -1;
    }
}
''')

written = 0
for folder, body in SOLUTIONS.items():
    path = ROOT / folder / "solution.php"
    path.write_text(body, encoding="utf-8", newline="\n")
    written += 1
print(f"wrote {written}")

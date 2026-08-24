#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
SOLUTIONS = {}

def add(folder, body):
    SOLUTIONS[folder] = body

add("2269_find_the_k_beauty_of_a_number", r'''<?php
// LeetCode 2269 - Find the K-Beauty of a Number
// https://leetcode.com/problems/find-the-k-beauty-of-a-number/

class Solution {
    function divisorSubstrings($num, $k) {
        $s = (string)$num;
        $ans = 0;
        $n = strlen($s);
        for ($i = 0; $i + $k <= $n; $i++) {
            $sub = 0;
            for ($j = 0; $j < $k; $j++) $sub = $sub * 10 + (ord($s[$i + $j]) - 48);
            if ($sub !== 0 && $num % $sub === 0) $ans++;
        }
        return $ans;
    }
}
''')

add("2270_number_of_ways_to_split_array", r'''<?php
// LeetCode 2270 - Number of Ways to Split Array
// https://leetcode.com/problems/number-of-ways-to-split-array/

class Solution {
    function waysToSplitArray($nums) {
        $total = 0;
        foreach ($nums as $v) $total += $v;
        $left = 0;
        $ans = 0;
        $n = count($nums);
        for ($i = 0; $i + 1 < $n; $i++) {
            $left += $nums[$i];
            if ($left >= $total - $left) $ans++;
        }
        return $ans;
    }
}
''')

add("2271_maximum_white_tiles_covered_by_a_carpet", r'''<?php
// LeetCode 2271 - Maximum White Tiles Covered by a Carpet
// https://leetcode.com/problems/maximum-white-tiles-covered-by-a-carpet/

class Solution {
    function maximumWhiteTiles($tiles, $carpetLen) {
        usort($tiles, function($a, $b) { return $a[0] <=> $b[0]; });
        $n = count($tiles);
        $pref = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; $i++) $pref[$i + 1] = $pref[$i] + ($tiles[$i][1] - $tiles[$i][0] + 1);
        $ans = 0;
        $j = 0;
        for ($i = 0; $i < $n; $i++) {
            $end = $tiles[$i][0] + $carpetLen - 1;
            while ($j < $n && $tiles[$j][0] <= $end) $j++;
            $cover = $pref[$j] - $pref[$i];
            if ($j > 0 && $tiles[$j - 1][1] > $end) $cover -= $tiles[$j - 1][1] - $end;
            $ans = max($ans, $cover);
        }
        return $ans;
    }
}
''')

add("2272_substring_with_largest_variance", r'''<?php
// LeetCode 2272 - Substring With Largest Variance
// https://leetcode.com/problems/substring-with-largest-variance/

class Solution {
    function largestVariance($s) {
        $ans = 0;
        $n = strlen($s);
        for ($ai = 0; $ai < 26; $ai++) {
            for ($bi = 0; $bi < 26; $bi++) {
                if ($ai === $bi) continue;
                $a = chr(97 + $ai);
                $b = chr(97 + $bi);
                $bal = 0;
                $hasB = false;
                for ($i = 0; $i < $n; $i++) {
                    $c = $s[$i];
                    if ($c === $a) $bal++;
                    else if ($c === $b) { $bal--; $hasB = true; }
                    if ($hasB) $ans = max($ans, $bal);
                    if ($bal < 0) { $bal = 0; $hasB = false; }
                }
            }
        }
        return $ans;
    }
}
''')

add("2273_find_resultant_array_after_removing_anagrams", r'''<?php
// LeetCode 2273 - Find Resultant Array After Removing Anagrams
// https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/

class Solution {
    function removeAnagrams($words) {
        $sig = function($w) {
            $c = array_fill(0, 26, 0);
            $n = strlen($w);
            for ($i = 0; $i < $n; $i++) $c[ord($w[$i]) - 97]++;
            return $c;
        };
        $eq = function($a, $b) {
            for ($i = 0; $i < 26; $i++) if ($a[$i] !== $b[$i]) return false;
            return true;
        };
        $ans = [$words[0]];
        $prev = $sig($words[0]);
        for ($i = 1; $i < count($words); $i++) {
            $cur = $sig($words[$i]);
            if (!$eq($cur, $prev)) {
                $ans[] = $words[$i];
                $prev = $cur;
            }
        }
        return $ans;
    }
}
''')

add("2274_maximum_consecutive_floors_without_special_floors", r'''<?php
// LeetCode 2274 - Maximum Consecutive Floors Without Special Floors
// https://leetcode.com/problems/maximum-consecutive-floors-without-special-floors/

class Solution {
    function maxConsecutive($bottom, $top, $special) {
        sort($special);
        $ans = $special[0] - $bottom;
        for ($i = 1; $i < count($special); $i++)
            $ans = max($ans, $special[$i] - $special[$i - 1] - 1);
        $ans = max($ans, $top - $special[count($special) - 1]);
        return $ans;
    }
}
''')

add("2275_largest_combination_with_bitwise_and_greater_than_zero", r'''<?php
// LeetCode 2275 - Largest Combination With Bitwise AND Greater Than Zero
// https://leetcode.com/problems/largest-combination-with-bitwise-and-greater-than-zero/

class Solution {
    function largestCombination($candidates) {
        $ans = 0;
        for ($bit = 0; $bit < 24; $bit++) {
            $cnt = 0;
            foreach ($candidates as $x) if ((($x >> $bit) & 1) !== 0) $cnt++;
            $ans = max($ans, $cnt);
        }
        return $ans;
    }
}
''')

add("2276_count_integers_in_intervals", r'''<?php
// LeetCode 2276 - Count Integers in Intervals
// https://leetcode.com/problems/count-integers-in-intervals/

class CountIntervals {
    private $root = null;
    private $cnt = 0;

    function __construct() {
        $this->root = null;
        $this->cnt = 0;
    }

    function add($left, $right) {
        $addRange = function($L, $R, $l, $r, $node) use (&$addRange) {
            if ($node === null) $node = ['left' => null, 'right' => null, 'covered' => false];
            if ($node['covered']) return [0, $node];
            if ($l <= $L && $R <= $r) {
                $node['covered'] = true;
                $node['left'] = $node['right'] = null;
                return [$R - $L + 1, $node];
            }
            $mid = intdiv($L + $R, 2);
            $added = 0;
            if ($l <= $mid) {
                $res = $addRange($L, $mid, $l, $r, $node['left']);
                $added += $res[0];
                $node['left'] = $res[1];
            }
            if ($r > $mid) {
                $res = $addRange($mid + 1, $R, $l, $r, $node['right']);
                $added += $res[0];
                $node['right'] = $res[1];
            }
            if ($node['left'] && $node['right'] && $node['left']['covered'] && $node['right']['covered']) {
                $node['covered'] = true;
                $node['left'] = $node['right'] = null;
            }
            return [$added, $node];
        };
        $res = $addRange(1, 1000000000, $left, $right, $this->root);
        $this->cnt += $res[0];
        $this->root = $res[1];
    }

    function count() {
        return $this->cnt;
    }
}
''')

add("2277_closest_node_to_path_in_tree", r'''<?php
// LeetCode 2277 - Closest Node to Path in Tree
// https://leetcode.com/problems/closest-node-to-path-in-tree/

class Solution {
    function solve($n, $edges, $query) {
        $LOG = 17;
        $g = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $g[$e[0]][] = $e[1];
            $g[$e[1]][] = $e[0];
        }
        $up = [];
        for ($k = 0; $k < $LOG; $k++) $up[$k] = array_fill(0, $n, 0);
        $depth = array_fill(0, $n, 0);
        $dfs = function($u, $p) use (&$dfs, &$up, &$depth, $g) {
            $up[0][$u] = $p;
            foreach ($g[$u] as $v) if ($v !== $p) {
                $depth[$v] = $depth[$u] + 1;
                $dfs($v, $u);
            }
        };
        $dfs(0, 0);
        for ($k = 1; $k < $LOG; $k++)
            for ($v = 0; $v < $n; $v++)
                $up[$k][$v] = $up[$k - 1][$up[$k - 1][$v]];
        $lift = function($v, $d) use ($LOG, $up) {
            for ($k = 0; $k < $LOG; $k++)
                if ((($d >> $k) & 1) !== 0) $v = $up[$k][$v];
            return $v;
        };
        $lca = function($a, $b) use ($depth, $lift, $LOG, $up) {
            if ($depth[$a] < $depth[$b]) { $tmp = $a; $a = $b; $b = $tmp; }
            $a = $lift($a, $depth[$a] - $depth[$b]);
            if ($a === $b) return $a;
            for ($k = $LOG - 1; $k >= 0; $k--) {
                if ($up[$k][$a] !== $up[$k][$b]) {
                    $a = $up[$k][$a];
                    $b = $up[$k][$b];
                }
            }
            return $up[0][$a];
        };
        $dist = function($a, $b) use ($lca, $depth) {
            $c = $lca($a, $b);
            return $depth[$a] + $depth[$b] - 2 * $depth[$c];
        };
        $ans = array_fill(0, count($query), 0);
        for ($i = 0; $i < count($query); $i++) {
            $a = $query[$i][0];
            $b = $query[$i][1];
            $x = $query[$i][2];
            $cands = [$lca($a, $b), $lca($a, $x), $lca($b, $x)];
            $best = $cands[0];
            $bestD = $dist($cands[0], $x);
            for ($t = 1; $t < 3; $t++) {
                $d = $dist($cands[$t], $x);
                if ($d < $bestD) { $bestD = $d; $best = $cands[$t]; }
            }
            $ans[$i] = $best;
        }
        return $ans;
    }
}
''')

add("2278_percentage_of_letter_in_string", r'''<?php
// LeetCode 2278 - Percentage of Letter in String
// https://leetcode.com/problems/percentage-of-letter-in-string/

class Solution {
    function percentageLetter($s, $letter) {
        $cnt = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) if ($s[$i] === $letter) $cnt++;
        return intdiv($cnt * 100, $n);
    }
}
''')

add("2279_maximum_bags_with_full_capacity_of_rocks", r'''<?php
// LeetCode 2279 - Maximum Bags With Full Capacity of Rocks
// https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/

class Solution {
    function maximumBags($capacity, $rocks, $additionalRocks) {
        $need = [];
        for ($i = 0; $i < count($capacity); $i++) $need[] = $capacity[$i] - $rocks[$i];
        sort($need);
        $ans = 0;
        foreach ($need as $n) {
            if ($additionalRocks < $n) break;
            $additionalRocks -= $n;
            $ans++;
        }
        return $ans;
    }
}
''')

add("2280_minimum_lines_to_represent_a_line_chart", r'''<?php
// LeetCode 2280 - Minimum Lines to Represent a Line Chart
// https://leetcode.com/problems/minimum-lines-to-represent-a-line-chart/

class Solution {
    function minimumLines($stockPrices) {
        if (count($stockPrices) <= 1) return 0;
        usort($stockPrices, function($a, $b) { return $a[0] <=> $b[0]; });
        $ans = 1;
        for ($i = 2; $i < count($stockPrices); $i++) {
            $x0 = $stockPrices[$i - 2][0];
            $y0 = $stockPrices[$i - 2][1];
            $x1 = $stockPrices[$i - 1][0];
            $y1 = $stockPrices[$i - 1][1];
            $x2 = $stockPrices[$i][0];
            $y2 = $stockPrices[$i][1];
            if (($y1 - $y0) * ($x2 - $x1) !== ($y2 - $y1) * ($x1 - $x0)) $ans++;
        }
        return $ans;
    }
}
''')

add("2281_sum_of_total_strength_of_wizards", r'''<?php
// LeetCode 2281 - Sum of Total Strength of Wizards
// https://leetcode.com/problems/sum-of-total-strength-of-wizards/

class Solution {
    function totalStrength($strength) {
        $mod = 1000000007;
        $n = count($strength);
        $left = array_fill(0, $n, 0);
        $right = array_fill(0, $n, 0);
        $stack = [];
        for ($i = 0; $i < $n; $i++) {
            while (count($stack) && $strength[$stack[count($stack) - 1]] >= $strength[$i]) array_pop($stack);
            $left[$i] = count($stack) ? $stack[count($stack) - 1] : -1;
            $stack[] = $i;
        }
        $stack = [];
        for ($i = $n - 1; $i >= 0; $i--) {
            while (count($stack) && $strength[$stack[count($stack) - 1]] > $strength[$i]) array_pop($stack);
            $right[$i] = count($stack) ? $stack[count($stack) - 1] : $n;
            $stack[] = $i;
        }
        $pref = array_fill(0, $n + 1, 0);
        $prefPref = array_fill(0, $n + 2, 0);
        for ($i = 0; $i < $n; $i++) $pref[$i + 1] = ($pref[$i] + $strength[$i]) % $mod;
        for ($i = 0; $i <= $n; $i++) $prefPref[$i + 1] = ($prefPref[$i] + $pref[$i]) % $mod;
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            $l = $left[$i] + 1;
            $r = $right[$i] - 1;
            $leftSum = ($prefPref[$i + 1] - $prefPref[$l] + $mod) % $mod;
            $rightSum = ($prefPref[$r + 2] - $prefPref[$i + 1] + $mod) % $mod;
            $leftCnt = $i - $l + 1;
            $rightCnt = $r - $i + 1;
            $contrib = ($rightCnt * $leftSum % $mod - $leftCnt * $rightSum % $mod + $mod) % $mod;
            $ans = ($ans + $contrib * $strength[$i] % $mod) % $mod;
        }
        return $ans;
    }
}
''')

add("2282_number_of_people_that_can_be_seen_in_a_grid", r'''<?php
// LeetCode 2282 - Number of People That Can Be Seen in a Grid
// https://leetcode.com/problems/number-of-people-that-can-be-seen-in-a-grid/

class Solution {
    function solve($heights) {
        $m = count($heights);
        $n = count($heights[0]);
        $ans = [];
        for ($i = 0; $i < $m; $i++) $ans[$i] = array_fill(0, $n, 0);
        for ($i = 0; $i < $m; $i++) {
            $stack = [];
            for ($j = $n - 1; $j >= 0; $j--) {
                $cnt = 0;
                while (count($stack) && $heights[$i][$stack[count($stack) - 1]] < $heights[$i][$j]) {
                    array_pop($stack);
                    $cnt++;
                }
                if (count($stack)) $cnt++;
                $ans[$i][$j] += $cnt;
                while (count($stack) && $heights[$i][$stack[count($stack) - 1]] === $heights[$i][$j]) array_pop($stack);
                $stack[] = $j;
            }
        }
        for ($j = 0; $j < $n; $j++) {
            $stack = [];
            for ($i = $m - 1; $i >= 0; $i--) {
                $cnt = 0;
                while (count($stack) && $heights[$stack[count($stack) - 1]][$j] < $heights[$i][$j]) {
                    array_pop($stack);
                    $cnt++;
                }
                if (count($stack)) $cnt++;
                $ans[$i][$j] += $cnt;
                while (count($stack) && $heights[$stack[count($stack) - 1]][$j] === $heights[$i][$j]) array_pop($stack);
                $stack[] = $i;
            }
        }
        return $ans;
    }
}
''')

add("2283_check_if_number_has_equal_digit_count_and_digit_value", r'''<?php
// LeetCode 2283 - Check if Number Has Equal Digit Count and Digit Value
// https://leetcode.com/problems/check-if-number-has-equal-digit-count-and-digit-value/

class Solution {
    function digitCount($num) {
        $cnt = array_fill(0, 10, 0);
        $n = strlen($num);
        for ($i = 0; $i < $n; $i++) $cnt[ord($num[$i]) - 48]++;
        for ($i = 0; $i < $n; $i++)
            if ($cnt[$i] !== ord($num[$i]) - 48) return false;
        return true;
    }
}
''')

add("2284_sender_with_largest_word_count", r'''<?php
// LeetCode 2284 - Sender With Largest Word Count
// https://leetcode.com/problems/sender-with-largest-word-count/

class Solution {
    function largestWordCount($messages, $senders) {
        $count = [];
        $best = '';
        $bestCnt = -1;
        for ($i = 0; $i < count($messages); $i++) {
            $words = 1;
            $n = strlen($messages[$i]);
            for ($j = 0; $j < $n; $j++) if ($messages[$i][$j] === ' ') $words++;
            $c2 = ($count[$senders[$i]] ?? 0) + $words;
            $count[$senders[$i]] = $c2;
            if ($c2 > $bestCnt || ($c2 === $bestCnt && $senders[$i] > $best)) {
                $bestCnt = $c2;
                $best = $senders[$i];
            }
        }
        return $best;
    }
}
''')

add("2285_maximum_total_importance_of_roads", r'''<?php
// LeetCode 2285 - Maximum Total Importance of Roads
// https://leetcode.com/problems/maximum-total-importance-of-roads/

class Solution {
    function maximumImportance($n, $roads) {
        $deg = array_fill(0, $n, 0);
        foreach ($roads as $r) { $deg[$r[0]]++; $deg[$r[1]]++; }
        sort($deg);
        $ans = 0;
        for ($i = 0; $i < $n; $i++) $ans += $deg[$i] * ($i + 1);
        return $ans;
    }
}
''')

add("2286_booking_concert_tickets_in_groups", r'''<?php
// LeetCode 2286 - Booking Concert Tickets in Groups
// https://leetcode.com/problems/booking-concert-tickets-in-groups/

class BookMyShow {
    private $n;
    private $m;
    private $sum;
    private $mx;

    function __construct($n, $m) {
        $this->n = $n;
        $this->m = $m;
        $this->sum = array_fill(0, 4 * $n, 0);
        $this->mx = array_fill(0, 4 * $n, 0);
        $this->build(1, 0, $n - 1);
    }

    private function pull($idx) {
        $this->sum[$idx] = $this->sum[$idx * 2] + $this->sum[$idx * 2 + 1];
        $this->mx[$idx] = max($this->mx[$idx * 2], $this->mx[$idx * 2 + 1]);
    }

    private function build($idx, $l, $r) {
        if ($l === $r) {
            $this->sum[$idx] = $this->mx[$idx] = $this->m;
            return;
        }
        $mid = ($l + $r) >> 1;
        $this->build($idx * 2, $l, $mid);
        $this->build($idx * 2 + 1, $mid + 1, $r);
        $this->pull($idx);
    }

    private function update($idx, $l, $r, $pos, $val) {
        if ($l === $r) {
            $this->sum[$idx] = $this->mx[$idx] = $val;
            return;
        }
        $mid = ($l + $r) >> 1;
        if ($pos <= $mid) $this->update($idx * 2, $l, $mid, $pos, $val);
        else $this->update($idx * 2 + 1, $mid + 1, $r, $pos, $val);
        $this->pull($idx);
    }

    private function querySum($idx, $l, $r, $ql, $qr) {
        if ($qr < $l || $r < $ql) return 0;
        if ($ql <= $l && $r <= $qr) return $this->sum[$idx];
        $mid = ($l + $r) >> 1;
        return $this->querySum($idx * 2, $l, $mid, $ql, $qr) + $this->querySum($idx * 2 + 1, $mid + 1, $r, $ql, $qr);
    }

    private function findFirst($idx, $l, $r, $maxRow, $k) {
        if ($l > $maxRow || $this->mx[$idx] < $k) return -1;
        if ($l === $r) return $l;
        $mid = ($l + $r) >> 1;
        $left = $this->findFirst($idx * 2, $l, $mid, $maxRow, $k);
        if ($left !== -1) return $left;
        return $this->findFirst($idx * 2 + 1, $mid + 1, $r, $maxRow, $k);
    }

    function gather($k, $maxRow) {
        $row = $this->findFirst(1, 0, $this->n - 1, $maxRow, $k);
        if ($row === -1) return [];
        $remain = $this->querySum(1, 0, $this->n - 1, $row, $row);
        $seat = $this->m - $remain;
        $this->update(1, 0, $this->n - 1, $row, $remain - $k);
        return [$row, $seat];
    }

    function scatter($k, $maxRow) {
        if ($this->querySum(1, 0, $this->n - 1, 0, $maxRow) < $k) return false;
        $need = $k;
        for ($row = 0; $row <= $maxRow && $need > 0; $row++) {
            $remain = $this->querySum(1, 0, $this->n - 1, $row, $row);
            if ($remain === 0) continue;
            $take = min($remain, $need);
            $this->update(1, 0, $this->n - 1, $row, $remain - $take);
            $need -= $take;
        }
        return true;
    }
}
''')

add("2287_rearrange_characters_to_make_target_string", r'''<?php
// LeetCode 2287 - Rearrange Characters to Make Target String
// https://leetcode.com/problems/rearrange-characters-to-make-target-string/

class Solution {
    function rearrangeCharacters($s, $target) {
        $sc = array_fill(0, 26, 0);
        $tc = array_fill(0, 26, 0);
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) $sc[ord($s[$i]) - 97]++;
        $tn = strlen($target);
        for ($i = 0; $i < $tn; $i++) $tc[ord($target[$i]) - 97]++;
        $ans = PHP_INT_MAX;
        for ($i = 0; $i < 26; $i++) {
            if ($tc[$i] === 0) continue;
            $ans = min($ans, intdiv($sc[$i], $tc[$i]));
        }
        return $ans;
    }
}
''')

add("2288_apply_discount_to_prices", r'''<?php
// LeetCode 2288 - Apply Discount to Prices
// https://leetcode.com/problems/apply-discount-to-prices/

class Solution {
    function discountPrices($sentence, $discount) {
        $parts = explode(' ', $sentence);
        for ($i = 0; $i < count($parts); $i++) {
            $part = $parts[$i];
            if (strlen($part) >= 2 && $part[0] === '$') {
                $ok = true;
                $pn = strlen($part);
                for ($j = 1; $j < $pn; $j++) {
                    if ($part[$j] < '0' || $part[$j] > '9') { $ok = false; break; }
                }
                if ($ok) {
                    $val = floatval(substr($part, 1));
                    $price = $val * (100 - $discount) / 100.0;
                    $parts[$i] = '$' . number_format($price, 2, '.', '');
                }
            }
        }
        return implode(' ', $parts);
    }
}
''')

add("2289_steps_to_make_array_non_decreasing", r'''<?php
// LeetCode 2289 - Steps to Make Array Non-decreasing
// https://leetcode.com/problems/steps-to-make-array-non-decreasing/

class Solution {
    function totalSteps($nums) {
        $stack = [];
        $ans = 0;
        for ($i = count($nums) - 1; $i >= 0; $i--) {
            $steps = 0;
            while (count($stack) && $nums[$i] > $stack[count($stack) - 1][0]) {
                $steps = max($steps, $stack[count($stack) - 1][1]);
                array_pop($stack);
                $steps++;
            }
            $ans = max($ans, $steps);
            $stack[] = [$nums[$i], $steps];
        }
        return $ans;
    }
}
''')

add("2290_minimum_obstacle_removal_to_reach_corner", r'''<?php
// LeetCode 2290 - Minimum Obstacle Removal to Reach Corner
// https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/

class Solution {
    function minimumObstacles($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        $INF = PHP_INT_MAX / 4;
        $dist = [];
        for ($i = 0; $i < $m; $i++) $dist[$i] = array_fill(0, $n, $INF);
        $dist[0][0] = 0;
        $dq = [[0, 0]];
        $dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];
        while (count($dq)) {
            [$r, $c] = array_shift($dq);
            foreach ($dirs as $d) {
                $nr = $r + $d[0];
                $nc = $c + $d[1];
                if ($nr < 0 || $nr >= $m || $nc < 0 || $nc >= $n) continue;
                $nd = $dist[$r][$c] + $grid[$nr][$nc];
                if ($nd < $dist[$nr][$nc]) {
                    $dist[$nr][$nc] = $nd;
                    if ($grid[$nr][$nc] === 0) array_unshift($dq, [$nr, $nc]);
                    else $dq[] = [$nr, $nc];
                }
            }
        }
        return $dist[$m - 1][$n - 1];
    }
}
''')

add("2291_maximum_profit_from_trading_stocks", r'''<?php
// LeetCode 2291 - Maximum Profit From Trading Stocks
// https://leetcode.com/problems/maximum-profit-from-trading-stocks/

class Solution {
    function solve($present, $future, $budget) {
        $n = count($present);
        $dp = array_fill(0, $budget + 1, 0);
        for ($i = 0; $i < $n; $i++) {
            $profit = $future[$i] - $present[$i];
            if ($profit <= 0) continue;
            $cost = $present[$i];
            for ($b = $budget; $b >= $cost; $b--)
                $dp[$b] = max($dp[$b], $dp[$b - $cost] + $profit);
        }
        return $dp[$budget];
    }
}
''')

add("2293_min_max_game", r'''<?php
// LeetCode 2293 - Min Max Game
// https://leetcode.com/problems/min-max-game/

class Solution {
    function minMaxGame($nums) {
        while (count($nums) > 1) {
            $next = [];
            $m = count($nums) >> 1;
            for ($i = 0; $i < $m; $i++) {
                if ($i % 2 === 0) $next[] = min($nums[2 * $i], $nums[2 * $i + 1]);
                else $next[] = max($nums[2 * $i], $nums[2 * $i + 1]);
            }
            $nums = $next;
        }
        return $nums[0];
    }
}
''')

add("2294_partition_array_such_that_maximum_difference_is_k", r'''<?php
// LeetCode 2294 - Partition Array Such That Maximum Difference Is K
// https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/

class Solution {
    function partitionArray($nums, $k) {
        sort($nums);
        $ans = 1;
        $start = $nums[0];
        for ($i = 1; $i < count($nums); $i++) {
            if ($nums[$i] - $start > $k) { $ans++; $start = $nums[$i]; }
        }
        return $ans;
    }
}
''')

add("2295_replace_elements_in_an_array", r'''<?php
// LeetCode 2295 - Replace Elements in an Array
// https://leetcode.com/problems/replace-elements-in-an-array/

class Solution {
    function arrayChange($nums, $operations) {
        $pos = [];
        for ($i = 0; $i < count($nums); $i++) $pos[$nums[$i]] = $i;
        foreach ($operations as $op) {
            $i = $pos[$op[0]];
            $nums[$i] = $op[1];
            unset($pos[$op[0]]);
            $pos[$op[1]] = $i;
        }
        return $nums;
    }
}
''')

add("2296_design_a_text_editor", r'''<?php
// LeetCode 2296 - Design a Text Editor
// https://leetcode.com/problems/design-a-text-editor/

class TextEditor {
    private $left = [];
    private $right = [];

    function __construct() {
        $this->left = [];
        $this->right = [];
    }

    private function suffix() {
        $start = max(0, count($this->left) - 10);
        return implode('', array_slice($this->left, $start));
    }

    function addText($text) {
        $n = strlen($text);
        for ($i = 0; $i < $n; $i++) $this->left[] = $text[$i];
    }

    function deleteText($k) {
        $deleted = 0;
        while ($k > 0 && count($this->left)) {
            array_pop($this->left);
            $k--;
            $deleted++;
        }
        return $deleted;
    }

    function cursorLeft($k) {
        while ($k > 0 && count($this->left)) {
            $this->right[] = array_pop($this->left);
            $k--;
        }
        return $this->suffix();
    }

    function cursorRight($k) {
        while ($k > 0 && count($this->right)) {
            $this->left[] = array_pop($this->right);
            $k--;
        }
        return $this->suffix();
    }
}
''')

add("2297_jump_game_viii", r'''<?php
// LeetCode 2297 - Jump Game VIII
// https://leetcode.com/problems/jump-game-viii/

class Solution {
    function solve($nums, $costs) {
        $n = count($nums);
        $INF = PHP_INT_MAX / 4;
        $dp = array_fill(0, $n, $INF);
        $dp[0] = 0;
        $stack1 = [];
        $stack2 = [];
        for ($i = 0; $i < $n; $i++) {
            while (count($stack1) && $nums[$stack1[count($stack1) - 1]] <= $nums[$i]) {
                $j = array_pop($stack1);
                $dp[$i] = min($dp[$i], $dp[$j] + $costs[$i]);
            }
            while (count($stack2) && $nums[$stack2[count($stack2) - 1]] > $nums[$i]) {
                $j = array_pop($stack2);
                $dp[$i] = min($dp[$i], $dp[$j] + $costs[$i]);
            }
            if (count($stack1)) $dp[$i] = min($dp[$i], $dp[$stack1[count($stack1) - 1]] + $costs[$i]);
            if (count($stack2)) $dp[$i] = min($dp[$i], $dp[$stack2[count($stack2) - 1]] + $costs[$i]);
            $stack1[] = $i;
            $stack2[] = $i;
        }
        return $dp[$n - 1];
    }
}
''')

add("2299_strong_password_checker_ii", r'''<?php
// LeetCode 2299 - Strong Password Checker II
// https://leetcode.com/problems/strong-password-checker-ii/

class Solution {
    function strongPasswordCheckerII($password) {
        if (strlen($password) < 8) return false;
        $special = '!@#$%^&*()-+';
        $hasLower = false;
        $hasUpper = false;
        $hasDigit = false;
        $hasSpecial = false;
        $n = strlen($password);
        for ($i = 0; $i < $n; $i++) {
            $c = $password[$i];
            if ($i > 0 && $c === $password[$i - 1]) return false;
            if ($c >= 'a' && $c <= 'z') $hasLower = true;
            else if ($c >= 'A' && $c <= 'Z') $hasUpper = true;
            else if ($c >= '0' && $c <= '9') $hasDigit = true;
            else if (strpos($special, $c) !== false) $hasSpecial = true;
        }
        return $hasLower && $hasUpper && $hasDigit && $hasSpecial;
    }
}
''')

add("2300_successful_pairs_of_spells_and_potions", r'''<?php
// LeetCode 2300 - Successful Pairs of Spells and Potions
// https://leetcode.com/problems/successful-pairs-of-spells-and-potions/

class Solution {
    function successfulPairs($spells, $potions, $success) {
        sort($potions);
        $m = count($potions);
        $ans = array_fill(0, count($spells), 0);
        for ($i = 0; $i < count($spells); $i++) {
            $lo = 0;
            $hi = $m;
            while ($lo < $hi) {
                $mid = ($lo + $hi) >> 1;
                if ($spells[$i] * $potions[$mid] >= $success) $hi = $mid;
                else $lo = $mid + 1;
            }
            $ans[$i] = $m - $lo;
        }
        return $ans;
    }
}
''')

add("2301_match_substring_after_replacement", r'''<?php
// LeetCode 2301 - Match Substring After Replacement
// https://leetcode.com/problems/match-substring-after-replacement/

class Solution {
    function matchReplacement($s, $sub, $mappings) {
        $allow = [];
        foreach ($mappings as $m) $allow[(ord($m[0]) << 8) | ord($m[1])] = true;
        $n = strlen($s);
        $mlen = strlen($sub);
        for ($i = 0; $i + $mlen <= $n; $i++) {
            $ok = true;
            for ($j = 0; $j < $mlen; $j++) {
                $a = $s[$i + $j];
                $b = $sub[$j];
                if ($a === $b || isset($allow[(ord($b) << 8) | ord($a)])) continue;
                $ok = false;
                break;
            }
            if ($ok) return true;
        }
        return false;
    }
}
''')

add("2302_count_subarrays_with_score_less_than_k", r'''<?php
// LeetCode 2302 - Count Subarrays With Score Less Than K
// https://leetcode.com/problems/count-subarrays-with-score-less-than-k/

class Solution {
    function countSubarrays($nums, $k) {
        $ans = 0;
        $sum = 0;
        $left = 0;
        $n = count($nums);
        for ($right = 0; $right < $n; $right++) {
            $sum += $nums[$right];
            while ($sum * ($right - $left + 1) >= $k) {
                $sum -= $nums[$left];
                $left++;
            }
            $ans += $right - $left + 1;
        }
        return $ans;
    }
}
''')

add("2303_calculate_amount_paid_in_taxes", r'''<?php
// LeetCode 2303 - Calculate Amount Paid in Taxes
// https://leetcode.com/problems/calculate-amount-paid-in-taxes/

class Solution {
    function calculateTax($brackets, $income) {
        $ans = 0.0;
        $prev = 0;
        foreach ($brackets as $b) {
            $upper = $b[0];
            $percent = $b[1];
            if ($income <= $prev) break;
            $taxable = ($income < $upper) ? $income - $prev : $upper - $prev;
            $ans += $taxable * $percent / 100.0;
            $prev = $upper;
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

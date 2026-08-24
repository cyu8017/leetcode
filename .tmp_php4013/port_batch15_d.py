#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
SOLUTIONS = {}

def add(folder, body):
    SOLUTIONS[folder] = body


add("3258_count_substrings_that_satisfy_k_constraint_i", r'''<?php
// LeetCode 3258 - Count Substrings That Satisfy K-Constraint I
// https://leetcode.com/problems/count-substrings-that-satisfy-k-constraint-i/

class Solution {
    function countKConstraintSubstrings($s, $k) {
        $ans = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $z = 0;
            $o = 0;
            for ($j = $i; $j < $n; $j++) {
                if ($s[$j] === '0') $z++; else $o++;
                if ($z <= $k || $o <= $k) $ans++;
                else break;
            }
        }
        return $ans;
    }
}
''')

add("3259_maximum_energy_boost_from_two_drinks", r'''<?php
// LeetCode 3259 - Maximum Energy Boost From Two Drinks
// https://leetcode.com/problems/maximum-energy-boost-from-two-drinks/

class Solution {
    function maxEnergyBoost($energyDrinkA, $energyDrinkB) {
        $n = count($energyDrinkA);
        $dpA = array_fill(0, $n, 0);
        $dpB = array_fill(0, $n, 0);
        $dpA[0] = $energyDrinkA[0];
        $dpB[0] = $energyDrinkB[0];
        if ($n === 1) return max($dpA[0], $dpB[0]);
        $dpA[1] = $energyDrinkA[1] + $dpA[0];
        $dpB[1] = $energyDrinkB[1] + $dpB[0];
        for ($i = 2; $i < $n; $i++) {
            $dpA[$i] = $energyDrinkA[$i] + max($dpA[$i - 1], $dpB[$i - 2]);
            $dpB[$i] = $energyDrinkB[$i] + max($dpB[$i - 1], $dpA[$i - 2]);
        }
        return max($dpA[$n - 1], $dpB[$n - 1]);
    }
}
''')

add("3260_find_the_largest_palindrome_divisible_by_k", r'''<?php
// LeetCode 3260 - Find the Largest Palindrome Divisible by K
// https://leetcode.com/problems/find-the-largest-palindrome-divisible-by-k/

class Solution {
    function largestPalindrome($n, $k) {
        $digits = array_fill(0, $n, '9');
        $half = intdiv($n + 1, 2);
        switch ($k) {
            case 1:
            case 3:
            case 9:
                return implode('', $digits);
            case 2:
                $digits[0] = $digits[$n - 1] = '8';
                return implode('', $digits);
            case 4:
                if ($n === 1) return '8';
                $digits[0] = $digits[1] = $digits[$n - 1] = $digits[$n - 2] = '8';
                return implode('', $digits);
            case 5:
                $digits[0] = $digits[$n - 1] = '5';
                return implode('', $digits);
            case 8:
                if ($n <= 2) return str_repeat('8', $n);
                $digits[0] = $digits[1] = $digits[2] = '8';
                $digits[$n - 1] = $digits[$n - 2] = $digits[$n - 3] = '8';
                return implode('', $digits);
            case 6:
                if ($n === 1) return '6';
                $digits[0] = $digits[$n - 1] = '8';
                $sum = 16 + 9 * ($n - 2);
                $need = $sum % 3;
                if ($need !== 0) {
                    $pos = $half - 1;
                    $digits[$pos] = chr(ord($digits[$pos]) - $need);
                    if ($n % 2 === 0 || $pos !== $n - 1 - $pos) $digits[$n - 1 - $pos] = $digits[$pos];
                }
                return implode('', $digits);
            case 7:
                return $this->largestPal7($n);
            default:
                return implode('', $digits);
        }
    }

    private function mod7($s) {
        $r = 0;
        $len = strlen($s);
        for ($i = 0; $i < $len; $i++) $r = ($r * 10 + (ord($s[$i]) - 48)) % 7;
        return $r;
    }

    private function largestPal7($n) {
        $halfLen = intdiv($n + 1, 2);
        $half = array_fill(0, $halfLen, '9');
        for (;;) {
            $pal = array_fill(0, $n, '0');
            for ($i = 0; $i < $halfLen; $i++) $pal[$i] = $half[$i];
            for ($i = 0; $i < intdiv($n, 2); $i++) $pal[$n - 1 - $i] = $pal[$i];
            if ($this->mod7(implode('', $pal)) === 0) return implode('', $pal);
            $idx = $halfLen - 1;
            while ($idx >= 0 && $half[$idx] === '0') { $half[$idx] = '9'; $idx--; }
            if ($idx < 0) break;
            $half[$idx] = chr(ord($half[$idx]) - 1);
        }
        return '';
    }
}
''')

add("3261_count_substrings_that_satisfy_k_constraint_ii", r'''<?php
// LeetCode 3261 - Count Substrings That Satisfy K-Constraint II
// https://leetcode.com/problems/count-substrings-that-satisfy-k-constraint-ii/

class Solution {
    function countKConstraintSubstrings($s, $k, $queries) {
        $n = strlen($s);
        $leftMost = array_fill(0, $n, 0);
        $z = 0;
        $o = 0;
        $L = 0;
        for ($R = 0; $R < $n; $R++) {
            if ($s[$R] === '0') $z++; else $o++;
            while ($z > $k && $o > $k) {
                if ($s[$L] === '0') $z--; else $o--;
                $L++;
            }
            $leftMost[$R] = $L;
        }
        $pref = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; $i++) $pref[$i + 1] = $pref[$i] + ($i - $leftMost[$i] + 1);
        $ans = array_fill(0, count($queries), 0);
        for ($qi = 0; $qi < count($queries); $qi++) {
            $l = $queries[$qi][0];
            $r = $queries[$qi][1];
            $lo = $l;
            $hi = $r + 1;
            while ($lo < $hi) {
                $mid = ($lo + $hi) >> 1;
                if ($leftMost[$mid] < $l) $lo = $mid + 1;
                else $hi = $mid;
            }
            $res = 0;
            if ($lo > $l) {
                $m = $lo - $l;
                $res += intdiv($m * ($m + 1), 2);
            }
            if ($lo <= $r) $res += $pref[$r + 1] - $pref[$lo];
            $ans[$qi] = $res;
        }
        return $ans;
    }
}
''')

add("3263_convert_doubly_linked_list_to_array_i", r'''<?php
// LeetCode 3263 - Convert Doubly Linked List to Array I
// https://leetcode.com/problems/convert-doubly-linked-list-to-array-i/

class ListNode {
    public $val = 0;
    public $prev = null;
    public $next = null;
    function __construct($val = 0) {
        $this->val = $val;
    }
}

class Solution {
    function toArray($head) {
        $ans = [];
        while ($head !== null) {
            $ans[] = $head->val;
            $head = $head->next;
        }
        return $ans;
    }
}
''')

add("3264_final_array_state_after_k_multiplication_operations_i", r'''<?php
// LeetCode 3264 - Final Array State After K Multiplication Operations I
// https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-i/

class Solution {
    function getFinalState($nums, $k, $multiplier) {
        $pq = new SplPriorityQueue();
        $pq->setExtractFlags(SplPriorityQueue::EXTR_BOTH);
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            $pq->insert($i, [-$nums[$i], -$i]);
        }
        for ($t = 0; $t < $k; $t++) {
            $item = $pq->extract();
            $i = $item['data'];
            $v = $nums[$i] * $multiplier;
            $nums[$i] = $v;
            $pq->insert($i, [-$v, -$i]);
        }
        return $nums;
    }
}
''')

add("3265_count_almost_equal_pairs_i", r'''<?php
// LeetCode 3265 - Count Almost Equal Pairs I
// https://leetcode.com/problems/count-almost-equal-pairs-i/

class Solution {
    function countPairs($nums) {
        $ans = 0;
        $n = count($nums);
        for ($i = 0; $i < $n; $i++)
            for ($j = $i + 1; $j < $n; $j++)
                if ($this->almostEqual($nums[$i], $nums[$j])) $ans++;
        return $ans;
    }

    private function almostEqual($a, $b) {
        $sa = (string)$a;
        $sb = (string)$b;
        while (strlen($sa) < strlen($sb)) $sa = '0' . $sa;
        while (strlen($sb) < strlen($sa)) $sb = '0' . $sb;
        $diff = [];
        $len = strlen($sa);
        for ($i = 0; $i < $len; $i++) if ($sa[$i] !== $sb[$i]) $diff[] = $i;
        if (count($diff) === 0) return true;
        if (count($diff) !== 2) return false;
        $i0 = $diff[0];
        $j = $diff[1];
        return $sa[$i0] === $sb[$j] && $sa[$j] === $sb[$i0];
    }
}
''')

add("3266_final_array_state_after_k_multiplication_operations_ii", r'''<?php
// LeetCode 3266 - Final Array State After K Multiplication Operations II
// https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-ii/

class Solution {
    function getFinalState($nums, $k, $multiplier) {
        $mod = 1000000007;
        if ($multiplier === 1) return $nums;
        $n = count($nums);
        $pq = new SplPriorityQueue();
        $pq->setExtractFlags(SplPriorityQueue::EXTR_BOTH);
        $maxV = 0;
        for ($i = 0; $i < $n; $i++) {
            $pq->insert($i, [-$nums[$i], -$i]);
            if ($nums[$i] > $maxV) $maxV = $nums[$i];
        }
        while ($k > 0 && !$pq->isEmpty()) {
            $item = $pq->extract();
            $i = $item['data'];
            $v = $nums[$i];
            if ($multiplier !== 0 && $v > intdiv($maxV, $multiplier) && $k >= $n) {
                $pq->insert($i, [-$v, -$i]);
                break;
            }
            $nv = $v * $multiplier;
            $nums[$i] = $nv;
            if ($nv > $maxV) $maxV = $nv;
            $pq->insert($i, [-$nv, -$i]);
            $k--;
        }
        if ($k > 0) {
            $full = intdiv($k, $n);
            $rem = $k % $n;
            $powFull = $this->modPow($multiplier, $full, $mod);
            for ($i = 0; $i < $n; $i++) $nums[$i] = (int)(($nums[$i] % $mod) * $powFull % $mod);
            $hh = new SplPriorityQueue();
            $hh->setExtractFlags(SplPriorityQueue::EXTR_BOTH);
            for ($i = 0; $i < $n; $i++) $hh->insert($i, [-$nums[$i], -$i]);
            for ($t = 0; $t < $rem; $t++) {
                $item = $hh->extract();
                $i = $item['data'];
                $v = (int)(($nums[$i] % $mod) * ($multiplier % $mod) % $mod);
                $nums[$i] = $v;
                $hh->insert($i, [-$v, -$i]);
            }
            for ($i = 0; $i < $n; $i++) $nums[$i] %= $mod;
        } else {
            for ($i = 0; $i < $n; $i++) $nums[$i] %= $mod;
        }
        return $nums;
    }

    private function modPow($a, $e, $mod) {
        $r = 1;
        $a %= $mod;
        while ($e > 0) {
            if ($e & 1) $r = (int)(($r * $a) % $mod);
            $a = (int)(($a * $a) % $mod);
            $e >>= 1;
        }
        return $r;
    }
}
''')

add("3267_count_almost_equal_pairs_ii", r'''<?php
// LeetCode 3267 - Count Almost Equal Pairs II
// https://leetcode.com/problems/count-almost-equal-pairs-ii/

class Solution {
    private $sb;

    function countPairs($nums) {
        $ans = 0;
        $n = count($nums);
        for ($i = 0; $i < $n; $i++)
            for ($j = $i + 1; $j < $n; $j++)
                if ($this->almostEqual($nums[$i], $nums[$j])) $ans++;
        return $ans;
    }

    private function dfs(&$arr, $start, $left) {
        if (implode('', $arr) === $this->sb) return true;
        if ($left === 0) return false;
        $len = count($arr);
        for ($i = $start; $i < $len; $i++) {
            if ($arr[$i] === $this->sb[$i]) continue;
            for ($j = $i + 1; $j < $len; $j++) {
                if ($arr[$j] === $this->sb[$i]) {
                    $tmp = $arr[$i]; $arr[$i] = $arr[$j]; $arr[$j] = $tmp;
                    if ($this->dfs($arr, $i + 1, $left - 1)) return true;
                    $tmp = $arr[$i]; $arr[$i] = $arr[$j]; $arr[$j] = $tmp;
                }
            }
            return false;
        }
        return implode('', $arr) === $this->sb;
    }

    private function almostEqual($a, $b) {
        $sa = (string)$a;
        $this->sb = (string)$b;
        while (strlen($sa) < strlen($this->sb)) $sa = '0' . $sa;
        while (strlen($this->sb) < strlen($sa)) $this->sb = '0' . $this->sb;
        if ($sa === $this->sb) return true;
        $arr = str_split($sa);
        return $this->dfs($arr, 0, 2);
    }
}
''')

add("3269_constructing_two_increasing_arrays", r'''<?php
// LeetCode 3269 - Constructing Two Increasing Arrays
// https://leetcode.com/problems/constructing-two-increasing-arrays/

class Solution {
    function minLargest($nums1, $nums2) {
        $n = count($nums1);
        $m = count($nums2);
        $inf = 1000000000;
        $dp = [];
        for ($i = 0; $i <= $n; $i++) $dp[$i] = array_fill(0, $m + 1, $inf);
        $dp[0][0] = 0;
        for ($i = 0; $i <= $n; $i++) {
            for ($j = 0; $j <= $m; $j++) {
                if ($dp[$i][$j] === $inf) continue;
                $prev = $dp[$i][$j];
                if ($i < $n) {
                    $need = $prev + 1;
                    if ($nums1[$i] === 0) { if ($need % 2 !== 0) $need++; }
                    else { if ($need % 2 === 0) $need++; }
                    if ($need < $dp[$i + 1][$j]) $dp[$i + 1][$j] = $need;
                }
                if ($j < $m) {
                    $need = $prev + 1;
                    if ($nums2[$j] === 0) { if ($need % 2 !== 0) $need++; }
                    else { if ($need % 2 === 0) $need++; }
                    if ($need < $dp[$i][$j + 1]) $dp[$i][$j + 1] = $need;
                }
            }
        }
        return $dp[$n][$m];
    }
}
''')

add("3270_find_the_key_of_the_numbers", r'''<?php
// LeetCode 3270 - Find the Key of the Numbers
// https://leetcode.com/problems/find-the-key-of-the-numbers/

class Solution {
    function generateKey($num1, $num2, $num3) {
        $ans = 0;
        $mul = 1;
        for ($t = 0; $t < 4; $t++) {
            $d = min($num1 % 10, $num2 % 10, $num3 % 10);
            $ans += $d * $mul;
            $mul *= 10;
            $num1 = intdiv($num1, 10);
            $num2 = intdiv($num2, 10);
            $num3 = intdiv($num3, 10);
        }
        return $ans;
    }
}
''')

add("3271_hash_divided_string", r'''<?php
// LeetCode 3271 - Hash Divided String
// https://leetcode.com/problems/hash-divided-string/

class Solution {
    function stringHash($s, $k) {
        $out = '';
        $n = strlen($s);
        for ($i = 0; $i < $n; $i += $k) {
            $sum = 0;
            for ($j = $i; $j < $i + $k; $j++) $sum += ord($s[$j]) - 97;
            $out .= chr(97 + $sum % 26);
        }
        return $out;
    }
}
''')

add("3272_find_the_count_of_good_integers", r'''<?php
// LeetCode 3272 - Find the Count of Good Integers
// https://leetcode.com/problems/find-the-count-of-good-integers/

class Solution {
    function countGoodIntegers($n, $k) {
        $half = intdiv($n + 1, 2);
        $start = 1;
        for ($i = 1; $i < $half; $i++) $start *= 10;
        $end = $start * 10;
        $seen = [];
        $ans = 0;
        $fact = array_fill(0, $n + 1, 1);
        for ($i = 1; $i <= $n; $i++) $fact[$i] = $fact[$i - 1] * $i;
        for ($h = $start; $h < $end; $h++) {
            $s = (string)$h;
            $pal = $s;
            $revStart = strlen($s) - 1;
            if ($n % 2 === 1) $revStart--;
            for ($i = $revStart; $i >= 0; $i--) $pal .= $s[$i];
            if (intval($pal) % $k !== 0) continue;
            $charsArr = str_split($pal);
            sort($charsArr);
            $chars = implode('', $charsArr);
            if (isset($seen[$chars])) continue;
            $seen[$chars] = true;
            $cnt = array_fill(0, 10, 0);
            $clen = strlen($chars);
            for ($i = 0; $i < $clen; $i++) $cnt[ord($chars[$i]) - 48]++;
            $total = $fact[$n];
            foreach ($cnt as $c) $total = intdiv($total, $fact[$c]);
            if ($cnt[0] > 0) {
                $bad = $fact[$n - 1];
                $cnt[0]--;
                foreach ($cnt as $c) $bad = intdiv($bad, $fact[$c]);
                $cnt[0]++;
                $total -= $bad;
            }
            $ans += $total;
        }
        return $ans;
    }
}
''')

add("3273_minimum_amount_of_damage_dealt_to_bob", r'''<?php
// LeetCode 3273 - Minimum Amount of Damage Dealt to Bob
// https://leetcode.com/problems/minimum-amount-of-damage-dealt-to-bob/

class Solution {
    function minDamage($power, $damage, $health) {
        $n = count($damage);
        $arr = [];
        $totalDmg = 0;
        for ($i = 0; $i < $n; $i++) {
            $hits = intdiv($health[$i] + $power - 1, $power);
            $arr[] = [$damage[$i], $hits];
            $totalDmg += $damage[$i];
        }
        usort($arr, function($a, $b) {
            return $a[1] * $b[0] <=> $b[1] * $a[0];
        });
        $ans = 0;
        $cur = $totalDmg;
        foreach ($arr as $e) {
            $ans += $cur * $e[1];
            $cur -= $e[0];
        }
        return $ans;
    }
}
''')

add("3274_check_if_two_chessboard_squares_have_the_same_color", r'''<?php
// LeetCode 3274 - Check if Two Chessboard Squares Have the Same Color
// https://leetcode.com/problems/check-if-two-chessboard-squares-have-the-same-color/

class Solution {
    function checkTwoChessboards($coordinate1, $coordinate2) {
        $c1 = (ord($coordinate1[0]) - 97) + (ord($coordinate1[1]) - 49);
        $c2 = (ord($coordinate2[0]) - 97) + (ord($coordinate2[1]) - 49);
        return $c1 % 2 === $c2 % 2;
    }
}
''')

add("3275_k_th_nearest_obstacle_queries", r'''<?php
// LeetCode 3275 - K-th Nearest Obstacle Queries
// https://leetcode.com/problems/k-th-nearest-obstacle-queries/

class Solution {
    function resultsArray($queries, $k) {
        $pq = new SplPriorityQueue();
        $ans = array_fill(0, count($queries), 0);
        for ($i = 0; $i < count($queries); $i++) {
            $d = abs($queries[$i][0]) + abs($queries[$i][1]);
            $pq->insert($d, $d);
            if ($pq->count() > $k) $pq->extract();
            $ans[$i] = $pq->count() < $k ? -1 : $pq->top();
        }
        return $ans;
    }
}
''')

add("3276_select_cells_in_grid_with_maximum_score", r'''<?php
// LeetCode 3276 - Select Cells in Grid With Maximum Score
// https://leetcode.com/problems/select-cells-in-grid-with-maximum-score/

class Solution {
    function maxScore($grid) {
        $m = count($grid);
        $vals = [];
        for ($i = 0; $i < $m; $i++) {
            $seen = [];
            foreach ($grid[$i] as $v) {
                if (!isset($seen[$v])) {
                    $seen[$v] = true;
                    if (!isset($vals[$v])) $vals[$v] = [];
                    $vals[$v][] = $i;
                }
            }
        }
        $arr = array_keys($vals);
        rsort($arr);
        $N = 1 << $m;
        $dp = array_fill(0, $N, 0);
        foreach ($arr as $v) {
            $ndp = $dp;
            foreach ($vals[$v] as $r) {
                $bit = 1 << $r;
                for ($mask = 0; $mask < $N; $mask++) {
                    if (($mask & $bit) !== 0) continue;
                    $cand = $dp[$mask] + $v;
                    $nmask = $mask | $bit;
                    if ($cand > $ndp[$nmask]) $ndp[$nmask] = $cand;
                }
            }
            $dp = $ndp;
        }
        $ans = 0;
        foreach ($dp as $x) $ans = max($ans, $x);
        return $ans;
    }
}
''')

add("3277_maximum_xor_score_subarray_queries", r'''<?php
// LeetCode 3277 - Maximum XOR Score Subarray Queries
// https://leetcode.com/problems/maximum-xor-score-subarray-queries/

class Solution {
    function maximumSubarrayXor($nums, $queries) {
        $n = count($nums);
        $f = [];
        for ($i = 0; $i < $n; $i++) $f[$i] = array_fill(0, $n, 0);
        for ($i = 0; $i < $n; $i++) $f[$i][$i] = $nums[$i];
        for ($length = 2; $length <= $n; $length++) {
            for ($i = 0; $i + $length - 1 < $n; $i++) {
                $j = $i + $length - 1;
                $f[$i][$j] = $f[$i][$j - 1] ^ $f[$i + 1][$j];
            }
        }
        $best = [];
        for ($i = 0; $i < $n; $i++) $best[$i] = array_fill(0, $n, 0);
        for ($i = 0; $i < $n; $i++) $best[$i][$i] = $f[$i][$i];
        for ($length = 2; $length <= $n; $length++) {
            for ($i = 0; $i + $length - 1 < $n; $i++) {
                $j = $i + $length - 1;
                $best[$i][$j] = max($f[$i][$j], $best[$i][$j - 1], $best[$i + 1][$j]);
            }
        }
        $ans = array_fill(0, count($queries), 0);
        for ($i = 0; $i < count($queries); $i++) $ans[$i] = $best[$queries[$i][0]][$queries[$i][1]];
        return $ans;
    }
}
''')

add("3279_maximum_total_area_occupied_by_pistons", r'''<?php
// LeetCode 3279 - Maximum Total Area Occupied by Pistons
// https://leetcode.com/problems/maximum-total-area-occupied-by-pistons/

class Solution {
    function maxArea($height, $positions, $directions) {
        $n = count($positions);
        $pos = $positions;
        $dir = str_split($directions);
        $best = 0;
        for ($t = 0; $t <= 2 * $height; $t++) {
            $sum = 0;
            for ($i = 0; $i < $n; $i++) $sum += $pos[$i];
            if ($sum > $best) $best = $sum;
            for ($i = 0; $i < $n; $i++) {
                if ($dir[$i] === 'U') {
                    if ($pos[$i] === $height) { $dir[$i] = 'D'; $pos[$i]--; }
                    else $pos[$i]++;
                } else {
                    if ($pos[$i] === 0) { $dir[$i] = 'U'; $pos[$i]++; }
                    else $pos[$i]--;
                }
            }
        }
        return $best;
    }
}
''')

add("3280_convert_date_to_binary", r'''<?php
// LeetCode 3280 - Convert Date to Binary
// https://leetcode.com/problems/convert-date-to-binary/

class Solution {
    function convertDateToBinary($date) {
        $parts = explode('-', $date);
        $y = intval($parts[0]);
        $m = intval($parts[1]);
        $d = intval($parts[2]);
        return $this->toBinary($y) . '-' . $this->toBinary($m) . '-' . $this->toBinary($d);
    }

    private function toBinary($v) {
        if ($v === 0) return '0';
        $s = '';
        while ($v > 0) { $s = (($v & 1) ? '1' : '0') . $s; $v >>= 1; }
        return $s;
    }
}
''')

add("3281_maximize_score_of_numbers_in_ranges", r'''<?php
// LeetCode 3281 - Maximize Score of Numbers in Ranges
// https://leetcode.com/problems/maximize-score-of-numbers-in-ranges/

class Solution {
    function maxPossibleScore($start, $d) {
        sort($start);
        $n = count($start);
        $ok = function($mid) use ($start, $d) {
            $prev = $start[0];
            for ($i = 1; $i < count($start); $i++) {
                $need = $prev + $mid;
                $cur = $start[$i];
                if ($need > $cur + $d) return false;
                $prev = $need > $cur ? $need : $cur;
            }
            return true;
        };
        $lo = 0;
        $hi = $start[$n - 1] + $d - $start[0] + 1;
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi + 1, 2);
            if ($ok($mid)) $lo = $mid;
            else $hi = $mid - 1;
        }
        return $lo;
    }
}
''')

add("3282_reach_end_of_array_with_max_score", r'''<?php
// LeetCode 3282 - Reach End of Array With Max Score
// https://leetcode.com/problems/reach-end-of-array-with-max-score/

class Solution {
    function findMaximumScore($nums) {
        $ans = 0;
        $maxV = 0;
        $n = count($nums);
        for ($i = 0; $i < $n - 1; $i++) {
            if ($nums[$i] > $maxV) $maxV = $nums[$i];
            $ans += $maxV;
        }
        return $ans;
    }
}
''')

add("3283_maximum_number_of_moves_to_kill_all_pawns", r'''<?php
// LeetCode 3283 - Maximum Number of Moves to Kill All Pawns
// https://leetcode.com/problems/maximum-number-of-moves-to-kill-all-pawns/

class Solution {
    private $dist;
    private $n;
    private $N;
    private $memo;

    function maxMoves($kx, $ky, $positions) {
        $this->n = count($positions);
        $n = $this->n;
        $pts = [];
        for ($i = 0; $i <= $n; $i++) $pts[$i] = [0, 0];
        $pts[0][0] = $kx;
        $pts[0][1] = $ky;
        for ($i = 0; $i < $n; $i++) {
            $pts[$i + 1][0] = $positions[$i][0];
            $pts[$i + 1][1] = $positions[$i][1];
        }
        $this->dist = [];
        for ($i = 0; $i <= $n; $i++) $this->dist[$i] = $this->knightDist($pts[$i][0], $pts[$i][1], $pts);
        $this->N = 1 << $n;
        $this->memo = [];
        for ($i = 0; $i < $this->N; $i++) $this->memo[$i] = array_fill(0, $n + 1, -1);
        return $this->dfs(0, 0, 0);
    }

    private function knightDist($x, $y, $pts) {
        $DIRS = [[1,2],[1,-2],[-1,2],[-1,-2],[2,1],[2,-1],[-2,1],[-2,-1]];
        $np = count($pts);
        $ans = array_fill(0, $np, -1);
        $vis = [];
        for ($i = 0; $i < 50; $i++) $vis[$i] = array_fill(0, 50, false);
        $q = [[$x, $y, 0]];
        $vis[$x][$y] = true;
        $need = [];
        for ($i = 0; $i < $np; $i++) {
            $key = $pts[$i][0] . ',' . $pts[$i][1];
            if (!isset($need[$key])) $need[$key] = [];
            $need[$key][] = $i;
        }
        $found = 0;
        $qi = 0;
        while ($qi < count($q) && $found < $np) {
            $cur = $q[$qi++];
            $key = $cur[0] . ',' . $cur[1];
            if (isset($need[$key])) {
                foreach ($need[$key] as $i) {
                    if ($ans[$i] === -1) { $ans[$i] = $cur[2]; $found++; }
                }
            }
            foreach ($DIRS as $d) {
                $nx = $cur[0] + $d[0];
                $ny = $cur[1] + $d[1];
                if ($nx < 0 || $ny < 0 || $nx >= 50 || $ny >= 50 || $vis[$nx][$ny]) continue;
                $vis[$nx][$ny] = true;
                $q[] = [$nx, $ny, $cur[2] + 1];
            }
        }
        return $ans;
    }

    private function dfs($mask, $cur, $turn) {
        if ($mask === $this->N - 1) return 0;
        if ($this->memo[$mask][$cur] !== -1) return $this->memo[$mask][$cur];
        $best = $turn === 0 ? -(1 << 30) : (1 << 30);
        for ($i = 0; $i < $this->n; $i++) {
            if (($mask & (1 << $i)) !== 0) continue;
            $d = $this->dist[$cur][$i + 1];
            $v = $d + $this->dfs($mask | (1 << $i), $i + 1, 1 - $turn);
            if ($turn === 0) { if ($v > $best) $best = $v; }
            else if ($v < $best) $best = $v;
        }
        return $this->memo[$mask][$cur] = $best;
    }
}
''')

add("3284_sum_of_consecutive_subarrays", r'''<?php
// LeetCode 3284 - Sum of Consecutive Subarrays
// https://leetcode.com/problems/sum-of-consecutive-subarrays/

class Solution {
    function rangeSum($nums) {
        $mod = 1000000007;
        $n = count($nums);
        $ans = 0;
        $i = 0;
        while ($i < $n) {
            $j = $i;
            while ($j + 1 < $n && ($nums[$j + 1] === $nums[$j] + 1 || $nums[$j + 1] === $nums[$j] - 1)) $j++;
            for ($L = $i; $L <= $j; $L++) {
                $s = 0;
                for ($R = $L; $R <= $j; $R++) {
                    $s += $nums[$R];
                    $ans = ($ans + $s) % $mod;
                }
            }
            $i = $j + 1;
        }
        return $ans;
    }
}
''')

add("3285_find_indices_of_stable_mountains", r'''<?php
// LeetCode 3285 - Find Indices of Stable Mountains
// https://leetcode.com/problems/find-indices-of-stable-mountains/

class Solution {
    function stableMountains($height, $threshold) {
        $ans = [];
        $n = count($height);
        for ($i = 1; $i < $n; $i++) {
            if ($height[$i - 1] > $threshold) $ans[] = $i;
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

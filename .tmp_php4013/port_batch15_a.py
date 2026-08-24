#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
SOLUTIONS = {}

def add(folder, body):
    SOLUTIONS[folder] = body


add("3173_bitwise_or_of_adjacent_elements", r'''<?php
// LeetCode 3173 - Bitwise OR of Adjacent Elements
// https://leetcode.com/problems/bitwise-or-of-adjacent-elements/

class Solution {
    function orArray($nums) {
        $n = count($nums);
        $ans = [];
        for ($i = 1; $i < $n; $i++) $ans[] = $nums[$i] | $nums[$i - 1];
        return $ans;
    }
}
''')

add("3174_clear_digits", r'''<?php
// LeetCode 3174 - Clear Digits
// https://leetcode.com/problems/clear-digits/

class Solution {
    function clearDigits($s) {
        $stk = [];
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $c = $s[$i];
            if ($c >= '0' && $c <= '9') array_pop($stk);
            else $stk[] = $c;
        }
        return implode('', $stk);
    }
}
''')

add("3175_find_the_first_player_to_win_k_games_in_a_row", r'''<?php
// LeetCode 3175 - Find The First Player to win K Games in a Row
// https://leetcode.com/problems/find-the-first-player-to-win-k-games-in-a-row/

class Solution {
    function findWinningPlayer($skills, $k) {
        $n = count($skills);
        $k = min($k, $n - 1);
        $i = 0;
        $cnt = 0;
        for ($j = 1; $j < $n; $j++) {
            if ($skills[$i] < $skills[$j]) { $i = $j; $cnt = 1; }
            else $cnt++;
            if ($cnt === $k) break;
        }
        return $i;
    }
}
''')

add("3176_find_the_maximum_length_of_a_good_subsequence_i", r'''<?php
// LeetCode 3176 - Find the Maximum Length of a Good Subsequence I
// https://leetcode.com/problems/find-the-maximum-length-of-a-good-subsequence-i/

class Solution {
    function maximumLength($nums, $k) {
        $n = count($nums);
        $f = [];
        for ($i = 0; $i < $n; $i++) $f[$i] = array_fill(0, $k + 1, 0);
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            for ($h = 0; $h <= $k; $h++) {
                for ($j = 0; $j < $i; $j++) {
                    if ($nums[$i] === $nums[$j]) $f[$i][$h] = max($f[$i][$h], $f[$j][$h]);
                    else if ($h > 0) $f[$i][$h] = max($f[$i][$h], $f[$j][$h - 1]);
                }
                $f[$i][$h]++;
            }
            $ans = max($ans, $f[$i][$k]);
        }
        return $ans;
    }
}
''')

add("3177_find_the_maximum_length_of_a_good_subsequence_ii", r'''<?php
// LeetCode 3177 - Find the Maximum Length of a Good Subsequence II
// https://leetcode.com/problems/find-the-maximum-length-of-a-good-subsequence-ii/

class Solution {
    function maximumLength($nums, $k) {
        $n = count($nums);
        $f = [];
        for ($i = 0; $i < $n; $i++) $f[$i] = array_fill(0, $k + 1, 0);
        $mp = [];
        $g = [];
        for ($h = 0; $h <= $k; $h++) {
            $mp[$h] = [];
            $g[$h] = [0, 0, 0];
        }
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            for ($h = 0; $h <= $k; $h++) {
                $f[$i][$h] = $mp[$h][$nums[$i]] ?? 0;
                if ($h > 0) {
                    if ($g[$h - 1][0] !== $nums[$i]) $f[$i][$h] = max($f[$i][$h], $g[$h - 1][1]);
                    else $f[$i][$h] = max($f[$i][$h], $g[$h - 1][2]);
                }
                $f[$i][$h]++;
                $mp[$h][$nums[$i]] = max($mp[$h][$nums[$i]] ?? 0, $f[$i][$h]);
                if ($g[$h][0] !== $nums[$i]) {
                    if ($f[$i][$h] >= $g[$h][1]) {
                        $g[$h][2] = $g[$h][1];
                        $g[$h][1] = $f[$i][$h];
                        $g[$h][0] = $nums[$i];
                    } else if ($f[$i][$h] > $g[$h][2]) {
                        $g[$h][2] = $f[$i][$h];
                    }
                } else if ($f[$i][$h] > $g[$h][1]) {
                    $g[$h][1] = $f[$i][$h];
                }
                $ans = max($ans, $f[$i][$h]);
            }
        }
        return $ans;
    }
}
''')

add("3178_find_the_child_who_has_the_ball_after_k_seconds", r'''<?php
// LeetCode 3178 - Find the Child Who Has the Ball After K Seconds
// https://leetcode.com/problems/find-the-child-who-has-the-ball-after-k-seconds/

class Solution {
    function numberOfChild($n, $k) {
        $mod = $k % ($n - 1);
        $k = intdiv($k, $n - 1);
        if ($k % 2 === 1) return $n - $mod - 1;
        return $mod;
    }
}
''')

add("3179_find_the_n_th_value_after_k_seconds", r'''<?php
// LeetCode 3179 - Find the N-th Value After K Seconds
// https://leetcode.com/problems/find-the-n-th-value-after-k-seconds/

class Solution {
    function valueAfterKSeconds($n, $k) {
        $mod = 1000000007;
        $a = array_fill(0, $n, 1);
        while ($k-- > 0) {
            for ($i = 1; $i < $n; $i++) $a[$i] = ($a[$i] + $a[$i - 1]) % $mod;
        }
        return $a[$n - 1];
    }
}
''')

add("3180_maximum_total_reward_using_operations_i", r'''<?php
// LeetCode 3180 - Maximum Total Reward Using Operations I
// https://leetcode.com/problems/maximum-total-reward-using-operations-i/

class Solution {
    private $rewardValues;
    private $f;
    private $n;

    function maxTotalReward($rewardValues) {
        sort($rewardValues);
        $this->rewardValues = $rewardValues;
        $this->n = count($rewardValues);
        $this->f = array_fill(0, $rewardValues[$this->n - 1] << 1, -1);
        return $this->dfs(0);
    }

    private function upperBound($x) {
        $lo = 0;
        $hi = $this->n;
        while ($lo < $hi) {
            $mid = ($lo + $hi) >> 1;
            if ($this->rewardValues[$mid] <= $x) $lo = $mid + 1;
            else $hi = $mid;
        }
        return $lo;
    }

    private function dfs($x) {
        if ($this->f[$x] !== -1) return $this->f[$x];
        $idx = $this->upperBound($x);
        $this->f[$x] = 0;
        for ($it = $idx; $it < $this->n; $it++) {
            $this->f[$x] = max($this->f[$x], $this->rewardValues[$it] + $this->dfs($x + $this->rewardValues[$it]));
        }
        return $this->f[$x];
    }
}
''')

add("3181_maximum_total_reward_using_operations_ii", r'''<?php
// LeetCode 3181 - Maximum Total Reward Using Operations II
// https://leetcode.com/problems/maximum-total-reward-using-operations-ii/

class Solution {
    function maxTotalReward($rewardValues) {
        sort($rewardValues);
        $uniq = [];
        foreach ($rewardValues as $x) {
            if (empty($uniq) || $x !== $uniq[count($uniq) - 1]) $uniq[] = $x;
        }
        $W = 31;
        $MASK = 0x7FFFFFFF;
        $maxBit = 100001;
        $nw = intdiv($maxBit + $W - 1, $W) + 40;
        $f = array_fill(0, $nw, 0);
        $f[0] = 1;
        foreach ($uniq as $v) {
            $maskWords = intdiv($v, $W);
            $maskRem = $v % $W;
            $shifted = array_fill(0, $nw, 0);
            $srcWords = $maskWords + ($maskRem ? 1 : 0);
            for ($i = 0; $i < $srcWords && $i < $nw; $i++) {
                $word = $f[$i];
                if ($i === $maskWords && $maskRem) $word &= (1 << $maskRem) - 1;
                $dest = $i + $maskWords;
                if ($dest < $nw) $shifted[$dest] |= (($word << $maskRem) & $MASK);
                if ($maskRem && $dest + 1 < $nw) $shifted[$dest + 1] |= ($word >> ($W - $maskRem));
            }
            for ($i = 0; $i < $nw; $i++) $f[$i] |= $shifted[$i];
        }
        for ($i = 100000; $i >= 0; $i--) {
            $wi = intdiv($i, $W);
            $bi = $i % $W;
            if (($f[$wi] >> $bi) & 1) return $i;
        }
        return 0;
    }
}
''')

add("3183_the_number_of_ways_to_make_the_sum", r'''<?php
// LeetCode 3183 - The Number of Ways to Make the Sum
// https://leetcode.com/problems/the-number-of-ways-to-make-the-sum/

class Solution {
    function numberOfWays($n) {
        $mod = 1000000007;
        $coins = [1, 2, 6];
        $f = array_fill(0, $n + 1, 0);
        $f[0] = 1;
        foreach ($coins as $x) {
            for ($j = $x; $j <= $n; $j++) $f[$j] = ($f[$j] + $f[$j - $x]) % $mod;
        }
        $ans = $f[$n];
        if ($n >= 4) $ans = ($ans + $f[$n - 4]) % $mod;
        if ($n >= 8) $ans = ($ans + $f[$n - 8]) % $mod;
        return $ans;
    }
}
''')

add("3184_count_pairs_that_form_a_complete_day_i", r'''<?php
// LeetCode 3184 - Count Pairs That Form a Complete Day I
// https://leetcode.com/problems/count-pairs-that-form-a-complete-day-i/

class Solution {
    function countCompleteDayPairs($hours) {
        $cnt = array_fill(0, 24, 0);
        $ans = 0;
        foreach ($hours as $x) {
            $ans += $cnt[(24 - $x % 24) % 24];
            $cnt[$x % 24]++;
        }
        return $ans;
    }
}
''')

add("3185_count_pairs_that_form_a_complete_day_ii", r'''<?php
// LeetCode 3185 - Count Pairs That Form a Complete Day II
// https://leetcode.com/problems/count-pairs-that-form-a-complete-day-ii/

class Solution {
    function countCompleteDayPairs($hours) {
        $cnt = array_fill(0, 24, 0);
        $ans = 0;
        foreach ($hours as $x) {
            $ans += $cnt[(24 - $x % 24) % 24];
            $cnt[$x % 24]++;
        }
        return $ans;
    }
}
''')

add("3186_maximum_total_damage_with_spell_casting", r'''<?php
// LeetCode 3186 - Maximum Total Damage With Spell Casting
// https://leetcode.com/problems/maximum-total-damage-with-spell-casting/

class Solution {
    private $power;
    private $cnt;
    private $nxt;
    private $f;
    private $n;

    function maximumTotalDamage($power) {
        $this->n = count($power);
        sort($power);
        $this->power = $power;
        $this->cnt = [];
        $this->nxt = array_fill(0, $this->n, 0);
        $this->f = array_fill(0, $this->n, 0);
        for ($i = 0; $i < $this->n; $i++) {
            $this->cnt[$power[$i]] = ($this->cnt[$power[$i]] ?? 0) + 1;
            $this->nxt[$i] = $this->lowerBound($power[$i] + 3);
        }
        return $this->dfs(0);
    }

    private function lowerBound($x) {
        $lo = 0;
        $hi = $this->n;
        while ($lo < $hi) {
            $mid = ($lo + $hi) >> 1;
            if ($this->power[$mid] < $x) $lo = $mid + 1;
            else $hi = $mid;
        }
        return $lo;
    }

    private function dfs($i) {
        if ($i >= $this->n) return 0;
        if ($this->f[$i] !== 0) return $this->f[$i];
        $a = $this->dfs($i + $this->cnt[$this->power[$i]]);
        $b = $this->power[$i] * $this->cnt[$this->power[$i]] + $this->dfs($this->nxt[$i]);
        return $this->f[$i] = max($a, $b);
    }
}
''')

add("3187_peaks_in_array", r'''<?php
// LeetCode 3187 - Peaks in Array
// https://leetcode.com/problems/peaks-in-array/

class Solution {
    private $bitN;
    private $bitC;
    private $nums;
    private $n;

    function countOfPeaks($nums, $queries) {
        $this->nums = $nums;
        $this->n = count($nums);
        $this->bitN = $this->n - 1;
        $this->bitC = array_fill(0, $this->bitN + 1, 0);
        for ($i = 1; $i < $this->n - 1; $i++) $this->updatePeak($i, 1);
        $ans = [];
        foreach ($queries as $q) {
            if ($q[0] === 1) {
                $l = $q[1] + 1;
                $r = $q[2] - 1;
                $t = 0;
                if ($l <= $r) $t = $this->bitQuery($r) - $this->bitQuery($l - 1);
                $ans[] = $t;
            } else {
                $idx = $q[1];
                $val = $q[2];
                for ($i = $idx - 1; $i <= $idx + 1; $i++) $this->updatePeak($i, -1);
                $this->nums[$idx] = $val;
                for ($i = $idx - 1; $i <= $idx + 1; $i++) $this->updatePeak($i, 1);
            }
        }
        return $ans;
    }

    private function bitUpdate($x, $delta) {
        for (; $x <= $this->bitN; $x += $x & -$x) $this->bitC[$x] += $delta;
    }

    private function bitQuery($x) {
        $s = 0;
        for (; $x > 0; $x -= $x & -$x) $s += $this->bitC[$x];
        return $s;
    }

    private function updatePeak($i, $val) {
        if ($i <= 0 || $i >= $this->n - 1) return;
        if ($this->nums[$i - 1] < $this->nums[$i] && $this->nums[$i] > $this->nums[$i + 1]) $this->bitUpdate($i, $val);
    }
}
''')

add("3189_minimum_moves_to_get_a_peaceful_board", r'''<?php
// LeetCode 3189 - Minimum Moves to Get a Peaceful Board
// https://leetcode.com/problems/minimum-moves-to-get-a-peaceful-board/

class Solution {
    function minMoves($rooks) {
        $ans = 0;
        usort($rooks, function($a, $b) { return $a[0] <=> $b[0]; });
        for ($i = 0; $i < count($rooks); $i++) $ans += abs($rooks[$i][0] - $i);
        usort($rooks, function($a, $b) { return $a[1] <=> $b[1]; });
        for ($j = 0; $j < count($rooks); $j++) $ans += abs($rooks[$j][1] - $j);
        return $ans;
    }
}
''')

add("3190_find_minimum_operations_to_make_all_elements_divisible_by_three", r'''<?php
// LeetCode 3190 - Find Minimum Operations to Make All Elements Divisible by Three
// https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/

class Solution {
    function minimumOperations($nums) {
        $ans = 0;
        foreach ($nums as $x) if ($x % 3 !== 0) $ans++;
        return $ans;
    }
}
''')

add("3191_minimum_operations_to_make_binary_array_elements_equal_to_one_i", r'''<?php
// LeetCode 3191 - Minimum Operations to Make Binary Array Elements Equal to One I
// https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i/

class Solution {
    function minOperations($nums) {
        $ans = 0;
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            if ($nums[$i] === 0) {
                if ($i + 2 >= $n) return -1;
                $nums[$i + 1] ^= 1;
                $nums[$i + 2] ^= 1;
                $ans++;
            }
        }
        return $ans;
    }
}
''')

add("3192_minimum_operations_to_make_binary_array_elements_equal_to_one_ii", r'''<?php
// LeetCode 3192 - Minimum Operations to Make Binary Array Elements Equal to One II
// https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-ii/

class Solution {
    function minOperations($nums) {
        $ans = 0;
        $v = 0;
        foreach ($nums as $raw) {
            $x = $raw ^ $v;
            if ($x === 0) { $v ^= 1; $ans++; }
        }
        return $ans;
    }
}
''')

add("3193_count_the_number_of_inversions", r'''<?php
// LeetCode 3193 - Count the Number of Inversions
// https://leetcode.com/problems/count-the-number-of-inversions/

class Solution {
    function numberOfPermutations($n, $requirements) {
        $req = array_fill(0, $n, -1);
        foreach ($requirements as $r) $req[$r[0]] = $r[1];
        if ($req[0] > 0) return 0;
        $req[0] = 0;
        $m = 0;
        foreach ($req as $v) $m = max($m, $v);
        $mod = 1000000007;
        $f = [];
        for ($i = 0; $i < $n; $i++) $f[$i] = array_fill(0, $m + 1, 0);
        $f[0][0] = 1;
        for ($i = 1; $i < $n; $i++) {
            $l = 0;
            $r = $m;
            if ($req[$i] >= 0) { $l = $req[$i]; $r = $req[$i]; }
            for ($j = $l; $j <= $r; $j++) {
                for ($k = 0; $k <= min($i, $j); $k++) {
                    $f[$i][$j] = ($f[$i][$j] + $f[$i - 1][$j - $k]) % $mod;
                }
            }
        }
        return $f[$n - 1][$req[$n - 1]];
    }
}
''')

add("3194_minimum_average_of_smallest_and_largest_elements", r'''<?php
// LeetCode 3194 - Minimum Average of Smallest and Largest Elements
// https://leetcode.com/problems/minimum-average-of-smallest-and-largest-elements/

class Solution {
    function minimumAverage($nums) {
        sort($nums);
        $n = count($nums);
        $ans = 1 << 30;
        for ($i = 0; $i * 2 < $n; $i++) $ans = min($ans, $nums[$i] + $nums[$n - $i - 1]);
        return $ans / 2.0;
    }
}
''')

add("3195_find_the_minimum_area_to_cover_all_ones_i", r'''<?php
// LeetCode 3195 - Find the Minimum Area to Cover All Ones I
// https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-i/

class Solution {
    function minimumArea($grid) {
        $x1 = count($grid);
        $y1 = count($grid[0]);
        $x2 = 0;
        $y2 = 0;
        for ($i = 0; $i < count($grid); $i++) {
            for ($j = 0; $j < count($grid[0]); $j++) {
                if ($grid[$i][$j] === 1) {
                    $x1 = min($x1, $i);
                    $y1 = min($y1, $j);
                    $x2 = max($x2, $i);
                    $y2 = max($y2, $j);
                }
            }
        }
        return ($x2 - $x1 + 1) * ($y2 - $y1 + 1);
    }
}
''')

add("3196_maximize_total_cost_of_alternating_subarrays", r'''<?php
// LeetCode 3196 - Maximize Total Cost of Alternating Subarrays
// https://leetcode.com/problems/maximize-total-cost-of-alternating-subarrays/

class Solution {
    private $nums;
    private $n;
    private $memo;
    const NEG = -1.0e18;

    function maximumTotalCost($nums) {
        $this->nums = $nums;
        $this->n = count($nums);
        $this->memo = [];
        for ($i = 0; $i < $this->n; $i++) $this->memo[$i] = [self::NEG, self::NEG];
        return $this->dfs(0, 0);
    }

    private function dfs($i, $j) {
        if ($i >= $this->n) return 0;
        if ($this->memo[$i][$j] !== self::NEG) return $this->memo[$i][$j];
        $res = $this->nums[$i] + $this->dfs($i + 1, 1);
        if ($j > 0) $res = max($res, -$this->nums[$i] + $this->dfs($i + 1, 0));
        return $this->memo[$i][$j] = $res;
    }
}
''')

add("3197_find_the_minimum_area_to_cover_all_ones_ii", r'''<?php
// LeetCode 3197 - Find the Minimum Area to Cover All Ones II
// https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-ii/

class Solution {
    private $grid;

    function minimumSum($grid) {
        $this->grid = $grid;
        $m = count($grid);
        $n = count($grid[0]);
        $ans = $m * $n;
        for ($i1 = 0; $i1 < $m - 1; $i1++) {
            for ($i2 = $i1 + 1; $i2 < $m - 1; $i2++) {
                $ans = min($ans, $this->area(0, 0, $i1, $n - 1) + $this->area($i1 + 1, 0, $i2, $n - 1) + $this->area($i2 + 1, 0, $m - 1, $n - 1));
            }
        }
        for ($j1 = 0; $j1 < $n - 1; $j1++) {
            for ($j2 = $j1 + 1; $j2 < $n - 1; $j2++) {
                $ans = min($ans, $this->area(0, 0, $m - 1, $j1) + $this->area(0, $j1 + 1, $m - 1, $j2) + $this->area(0, $j2 + 1, $m - 1, $n - 1));
            }
        }
        for ($i = 0; $i < $m - 1; $i++) {
            for ($j = 0; $j < $n - 1; $j++) {
                $ans = min($ans, $this->area(0, 0, $i, $j) + $this->area(0, $j + 1, $i, $n - 1) + $this->area($i + 1, 0, $m - 1, $n - 1));
                $ans = min($ans, $this->area(0, 0, $i, $n - 1) + $this->area($i + 1, 0, $m - 1, $j) + $this->area($i + 1, $j + 1, $m - 1, $n - 1));
                $ans = min($ans, $this->area(0, 0, $i, $j) + $this->area($i + 1, 0, $m - 1, $j) + $this->area(0, $j + 1, $m - 1, $n - 1));
                $ans = min($ans, $this->area(0, 0, $m - 1, $j) + $this->area(0, $j + 1, $i, $n - 1) + $this->area($i + 1, $j + 1, $m - 1, $n - 1));
            }
        }
        return $ans;
    }

    private function area($i1, $j1, $i2, $j2) {
        $inf = 1000000000;
        $x1 = $inf;
        $y1 = $inf;
        $x2 = -$inf;
        $y2 = -$inf;
        for ($i = $i1; $i <= $i2; $i++) {
            for ($j = $j1; $j <= $j2; $j++) {
                if ($this->grid[$i][$j] === 1) {
                    $x1 = min($x1, $i);
                    $y1 = min($y1, $j);
                    $x2 = max($x2, $i);
                    $y2 = max($y2, $j);
                }
            }
        }
        if ($x1 === $inf) return 0;
        return ($x2 - $x1 + 1) * ($y2 - $y1 + 1);
    }
}
''')

add("3199_count_triplets_with_even_xor_set_bits_i", r'''<?php
// LeetCode 3199 - Count Triplets with Even XOR Set Bits I
// https://leetcode.com/problems/count-triplets-with-even-xor-set-bits-i/

class Solution {
    function tripletCount($a, $b, $c) {
        $cnt1 = [0, 0];
        $cnt2 = [0, 0];
        $cnt3 = [0, 0];
        foreach ($a as $x) $cnt1[$this->bitCount($x) % 2]++;
        foreach ($b as $x) $cnt2[$this->bitCount($x) % 2]++;
        foreach ($c as $x) $cnt3[$this->bitCount($x) % 2]++;
        $ans = 0;
        for ($i = 0; $i < 2; $i++)
            for ($j = 0; $j < 2; $j++)
                for ($k = 0; $k < 2; $k++)
                    if (($i + $j + $k) % 2 === 0) $ans += $cnt1[$i] * $cnt2[$j] * $cnt3[$k];
        return $ans;
    }

    private function bitCount($x) {
        $n = 0;
        while ($x) { $n += $x & 1; $x >>= 1; }
        return $n;
    }
}
''')

add("3200_maximum_height_of_a_triangle", r'''<?php
// LeetCode 3200 - Maximum Height of a Triangle
// https://leetcode.com/problems/maximum-height-of-a-triangle/

class Solution {
    function maxHeightOfTriangle($red, $blue) {
        $ans = 0;
        for ($k = 0; $k < 2; $k++) {
            $c = [$red, $blue];
            for ($i = 1, $j = $k; $i <= $c[$j]; $i++, $j ^= 1) {
                $c[$j] -= $i;
                $ans = max($ans, $i);
            }
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

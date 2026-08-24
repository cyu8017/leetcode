#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOLUTIONS: dict[str, str] = {}


def add(name: str, content: str) -> None:
    SOLUTIONS[name] = content.strip() + "\n"


add("2011_final_value_of_variable_after_performing_operations", r"""<?php
// LeetCode 2011 - Final Value of Variable After Performing Operations
// https://leetcode.com/problems/final-value-of-variable-after-performing-operations/

class Solution {
    /**
     * @param String[] $operations
     * @return Integer
     */
    function finalValueAfterOperations($operations) {
        $x = 0;
        foreach ($operations as $op) {
            if ($op[1] === '+') $x++;
            else $x--;
        }
        return $x;
    }
}
""")

add("2012_sum_of_beauty_in_the_array", r"""<?php
// LeetCode 2012 - Sum of Beauty in the Array
// https://leetcode.com/problems/sum-of-beauty-in-the-array/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function sumOfBeauties($nums) {
        $n = count($nums);
        $prefixMax = array_fill(0, $n, 0);
        $suffixMin = array_fill(0, $n, 0);
        $prefixMax[0] = $nums[0];
        for ($i = 1; $i < $n; $i++) $prefixMax[$i] = max($prefixMax[$i - 1], $nums[$i]);
        $suffixMin[$n - 1] = $nums[$n - 1];
        for ($i = $n - 2; $i >= 0; $i--) $suffixMin[$i] = min($suffixMin[$i + 1], $nums[$i]);
        $ans = 0;
        for ($i = 1; $i < $n - 1; $i++) {
            if ($prefixMax[$i - 1] < $nums[$i] && $nums[$i] < $suffixMin[$i + 1]) $ans += 2;
            else if ($nums[$i - 1] < $nums[$i] && $nums[$i] < $nums[$i + 1]) $ans++;
        }
        return $ans;
    }
}
""")

add("2013_detect_squares", r"""<?php
// LeetCode 2013 - Detect Squares
// https://leetcode.com/problems/detect-squares/

class DetectSquares {
    private $cnt = [];

    function __construct() {
        $this->cnt = [];
    }

    private function key($x, $y) {
        return $x . "," . $y;
    }

    /**
     * @param Integer[] $point
     * @return NULL
     */
    function add($point) {
        $k = $this->key($point[0], $point[1]);
        $this->cnt[$k] = ($this->cnt[$k] ?? 0) + 1;
    }

    /**
     * @param Integer[] $point
     * @return Integer
     */
    function count($point) {
        $x = $point[0];
        $y = $point[1];
        $ans = 0;
        foreach ($this->cnt as $k => $c) {
            [$px, $py] = array_map('intval', explode(",", $k));
            if ($px === $x || $py === $y) continue;
            if (abs($px - $x) !== abs($py - $y)) continue;
            $c1 = $this->cnt[$this->key($px, $y)] ?? 0;
            $c2 = $this->cnt[$this->key($x, $py)] ?? 0;
            $ans += $c * $c1 * $c2;
        }
        return $ans;
    }
}
""")

add("2014_longest_subsequence_repeated_k_times", r"""<?php
// LeetCode 2014 - Longest Subsequence Repeated K Times
// https://leetcode.com/problems/longest-subsequence-repeated-k-times/

class Solution {
    /**
     * @param String $s
     * @param Integer $k
     * @return String
     */
    function longestSubsequenceRepeatedK($s, $k) {
        $freq = array_fill(0, 26, 0);
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) $freq[ord($s[$i]) - 97]++;
        $chars = "";
        for ($c = 25; $c >= 0; $c--) if ($freq[$c] >= $k) $chars .= chr(97 + $c);
        $isSubseq = function ($t) use ($s, $k) {
            $need = 0;
            $times = 0;
            $tl = strlen($t);
            $sl = strlen($s);
            for ($i = 0; $i < $sl; $i++) {
                if ($s[$i] === $t[$need]) {
                    $need++;
                    if ($need === $tl) {
                        $times++;
                        if ($times === $k) return true;
                        $need = 0;
                    }
                }
            }
            return false;
        };
        $best = "";
        $q = [""];
        $clen = strlen($chars);
        while ($q) {
            $cur = array_shift($q);
            for ($i = 0; $i < $clen; $i++) {
                $nxt = $cur . $chars[$i];
                if ($isSubseq($nxt)) {
                    if (strlen($nxt) > strlen($best) || (strlen($nxt) === strlen($best) && $nxt > $best))
                        $best = $nxt;
                    $q[] = $nxt;
                }
            }
        }
        return $best;
    }
}
""")

add("2015_average_height_of_buildings_in_each_segment", r"""<?php
// LeetCode 2015 - Average Height of Buildings in Each Segment
// https://leetcode.com/problems/average-height-of-buildings-in-each-segment/

class Solution {
    /**
     * @param Integer[][] $buildings
     * @return Integer[][]
     */
    function averageHeightOfBuildings($buildings) {
        $events = [];
        foreach ($buildings as $b) {
            $events[] = [$b[0], 1, $b[2]];
            $events[] = [$b[1], -1, $b[2]];
        }
        usort($events, function ($a, $b) {
            if ($a[0] !== $b[0]) return $a[0] <=> $b[0];
            return $a[1] <=> $b[1];
        });
        $ans = [];
        $count = 0;
        $sum = 0;
        $prev = $events[0][0];
        foreach ($events as $e) {
            if ($e[0] !== $prev && $count > 0) {
                $avg = intdiv($sum, $count);
                $last = count($ans) - 1;
                if ($last >= 0 && $ans[$last][1] === $prev && $ans[$last][2] === $avg)
                    $ans[$last][1] = $e[0];
                else $ans[] = [$prev, $e[0], $avg];
            }
            $count += $e[1];
            $sum += $e[1] * $e[2];
            $prev = $e[0];
        }
        return $ans;
    }
}
""")

add("2016_maximum_difference_between_increasing_elements", r"""<?php
// LeetCode 2016 - Maximum Difference Between Increasing Elements
// https://leetcode.com/problems/maximum-difference-between-increasing-elements/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maximumDifference($nums) {
        $ans = -1;
        $mn = $nums[0];
        $n = count($nums);
        for ($i = 1; $i < $n; $i++) {
            if ($nums[$i] > $mn) $ans = max($ans, $nums[$i] - $mn);
            else $mn = $nums[$i];
        }
        return $ans;
    }
}
""")

add("2017_grid_game", r"""<?php
// LeetCode 2017 - Grid Game
// https://leetcode.com/problems/grid-game/

class Solution {
    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function gridGame($grid) {
        $n = count($grid[0]);
        $top = 0;
        $bottom = 0;
        $ans = PHP_INT_MAX;
        foreach ($grid[0] as $v) $top += $v;
        for ($i = 0; $i < $n; $i++) {
            $top -= $grid[0][$i];
            $ans = min($ans, max($top, $bottom));
            $bottom += $grid[1][$i];
        }
        return $ans;
    }
}
""")

add("2018_check_if_word_can_be_placed_in_crossword", r"""<?php
// LeetCode 2018 - Check if Word Can Be Placed In Crossword
// https://leetcode.com/problems/check-if-word-can-be-placed-in-crossword/

class Solution {
    /**
     * @param String[][] $board
     * @param String $word
     * @return Boolean
     */
    function placeWordInCrossword($board, $word) {
        $m = count($board);
        $n = count($board[0]);
        $L = strlen($word);
        $match = function ($cells) use ($word, $L) {
            if (strlen($cells) !== $L) return false;
            $ok1 = true;
            $ok2 = true;
            for ($i = 0; $i < $L; $i++) {
                if ($cells[$i] !== ' ' && $cells[$i] !== $word[$i]) $ok1 = false;
                if ($cells[$i] !== ' ' && $cells[$i] !== $word[$L - 1 - $i]) $ok2 = false;
            }
            return $ok1 || $ok2;
        };
        for ($r = 0; $r < $m; $r++) {
            $c = 0;
            while ($c < $n) {
                while ($c < $n && $board[$r][$c] === '#') $c++;
                $start = $c;
                while ($c < $n && $board[$r][$c] !== '#') $c++;
                if ($c - $start === $L) {
                    $sb = "";
                    for ($i = $start; $i < $c; $i++) $sb .= $board[$r][$i];
                    if ($match($sb)) return true;
                }
            }
        }
        for ($c = 0; $c < $n; $c++) {
            $r = 0;
            while ($r < $m) {
                while ($r < $m && $board[$r][$c] === '#') $r++;
                $start = $r;
                while ($r < $m && $board[$r][$c] !== '#') $r++;
                if ($r - $start === $L) {
                    $sb = "";
                    for ($i = 0; $i < $L; $i++) $sb .= $board[$start + $i][$c];
                    if ($match($sb)) return true;
                }
            }
        }
        return false;
    }
}
""")

add("2019_the_score_of_students_solving_math_expression", r"""<?php
// LeetCode 2019 - The Score of Students Solving Math Expression
// https://leetcode.com/problems/the-score-of-students-solving-math-expression/

class Solution {
    /**
     * @param String $s
     * @param Integer[] $answers
     * @return Integer
     */
    function scoreOfStudents($s, $answers) {
        $evalCorrect = function ($str) {
            $nums = [];
            $ops = [];
            $len = strlen($str);
            for ($i = 0; $i < $len; $i++) {
                $c = $str[$i];
                if ($c >= '0' && $c <= '9') $nums[] = ord($c) - 48;
                else $ops[] = $c;
            }
            $newNums = [$nums[0]];
            $newOps = [];
            $ol = count($ops);
            for ($j = 0; $j < $ol; $j++) {
                if ($ops[$j] === '*') $newNums[count($newNums) - 1] *= $nums[$j + 1];
                else { $newOps[] = $ops[$j]; $newNums[] = $nums[$j + 1]; }
            }
            $res = $newNums[0];
            $nol = count($newOps);
            for ($j = 0; $j < $nol; $j++) $res += $newNums[$j + 1];
            return $res;
        };
        $n = strlen($s);
        $correct = $evalCorrect($s);
        $dp = [];
        for ($i = 0; $i < $n; $i++) $dp[$i] = array_fill(0, $n, null);
        $dfs = null;
        $dfs = function ($l, $r) use (&$dfs, &$dp, $s) {
            if ($dp[$l][$r] !== null) return $dp[$l][$r];
            $res = [];
            if ($l === $r) { $res[ord($s[$l]) - 48] = true; $dp[$l][$r] = $res; return $res; }
            for ($i = $l + 1; $i < $r; $i += 2) {
                foreach ($dfs($l, $i - 1) as $a => $_) {
                    foreach ($dfs($i + 1, $r) as $b => $__) {
                        $v = $s[$i] === '+' ? $a + $b : $a * $b;
                        if ($v <= 1000) $res[$v] = true;
                    }
                }
            }
            $dp[$l][$r] = $res;
            return $res;
        };
        $possible = $dfs(0, $n - 1);
        $ans = 0;
        foreach ($answers as $a) {
            if ($a === $correct) $ans += 5;
            else if (isset($possible[$a])) $ans += 2;
        }
        return $ans;
    }
}
""")

add("2021_brightest_position_on_street", r"""<?php
// LeetCode 2021 - Brightest Position on Street
// https://leetcode.com/problems/brightest-position-on-street/

class Solution {
    /**
     * @param Integer[][] $lights
     * @return Integer
     */
    function brightestPosition($lights) {
        $events = [];
        foreach ($lights as $light) {
            $pos = $light[0];
            $r = $light[1];
            $events[] = [$pos - $r, 1];
            $events[] = [$pos + $r + 1, -1];
        }
        usort($events, function ($a, $b) {
            if ($a[0] !== $b[0]) return $a[0] <=> $b[0];
            return $b[1] <=> $a[1];
        });
        $best = 0;
        $cur = 0;
        $ans = 0;
        foreach ($events as $e) {
            $cur += $e[1];
            if ($cur > $best) { $best = $cur; $ans = $e[0]; }
        }
        return $ans;
    }
}
""")

add("2022_convert_1d_array_into_2d_array", r"""<?php
// LeetCode 2022 - Convert 1D Array Into 2D Array
// https://leetcode.com/problems/convert-1d-array-into-2d-array/

class Solution {
    /**
     * @param Integer[] $original
     * @param Integer $m
     * @param Integer $n
     * @return Integer[][]
     */
    function construct2DArray($original, $m, $n) {
        if (count($original) !== $m * $n) return [];
        $ans = [];
        for ($i = 0; $i < $m; $i++) {
            $ans[$i] = [];
            for ($j = 0; $j < $n; $j++) $ans[$i][$j] = $original[$i * $n + $j];
        }
        return $ans;
    }
}
""")

add("2023_number_of_pairs_of_strings_with_concatenation_equal_to_target", r"""<?php
// LeetCode 2023 - Number of Pairs of Strings With Concatenation Equal to Target
// https://leetcode.com/problems/number-of-pairs-of-strings-with-concatenation-equal-to-target/

class Solution {
    /**
     * @param String[] $nums
     * @param String $target
     * @return Integer
     */
    function numOfPairs($nums, $target) {
        $ans = 0;
        $n = count($nums);
        for ($i = 0; $i < $n; $i++)
            for ($j = 0; $j < $n; $j++)
                if ($i !== $j && $nums[$i] . $nums[$j] === $target) $ans++;
        return $ans;
    }
}
""")

add("2024_maximize_the_confusion_of_an_exam", r"""<?php
// LeetCode 2024 - Maximize the Confusion of an Exam
// https://leetcode.com/problems/maximize-the-confusion-of-an-exam/

class Solution {
    /**
     * @param String $answerKey
     * @param Integer $k
     * @return Integer
     */
    function maxConsecutiveAnswers($answerKey, $k) {
        $maxWith = function ($ch) use ($answerKey, $k) {
            $left = 0;
            $bad = 0;
            $best = 0;
            $n = strlen($answerKey);
            for ($right = 0; $right < $n; $right++) {
                if ($answerKey[$right] !== $ch) $bad++;
                while ($bad > $k) {
                    if ($answerKey[$left] !== $ch) $bad--;
                    $left++;
                }
                $best = max($best, $right - $left + 1);
            }
            return $best;
        };
        return max($maxWith('T'), $maxWith('F'));
    }
}
""")

add("2025_maximum_number_of_ways_to_partition_an_array", r"""<?php
// LeetCode 2025 - Maximum Number of Ways to Partition an Array
// https://leetcode.com/problems/maximum-number-of-ways-to-partition-an-array/

class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer
     */
    function waysToPartition($nums, $k) {
        $n = count($nums);
        $pref = array_fill(0, $n, 0);
        $pref[0] = $nums[0];
        for ($i = 1; $i < $n; $i++) $pref[$i] = $pref[$i - 1] + $nums[$i];
        $total = $pref[$n - 1];
        $right = [];
        $left = [];
        for ($i = 0; $i < $n - 1; $i++) $right[$pref[$i]] = ($right[$pref[$i]] ?? 0) + 1;
        $ans = 0;
        if ($total % 2 === 0) $ans = $right[intdiv($total, 2)] ?? 0;
        for ($i = 0; $i < $n; $i++) {
            $diff = $k - $nums[$i];
            $newTotal = $total + $diff;
            $cur = 0;
            if ($newTotal % 2 === 0) {
                $half = intdiv($newTotal, 2);
                $cur = ($left[$half] ?? 0) + ($right[$half - $diff] ?? 0);
            }
            $ans = max($ans, $cur);
            if ($i < $n - 1) {
                $left[$pref[$i]] = ($left[$pref[$i]] ?? 0) + 1;
                $right[$pref[$i]]--;
            }
        }
        return $ans;
    }
}
""")

add("2027_minimum_moves_to_convert_string", r"""<?php
// LeetCode 2027 - Minimum Moves to Convert String
// https://leetcode.com/problems/minimum-moves-to-convert-string/

class Solution {
    /**
     * @param String $s
     * @return Integer
     */
    function minimumMoves($s) {
        $ans = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; ) {
            if ($s[$i] === 'X') { $ans++; $i += 3; }
            else $i++;
        }
        return $ans;
    }
}
""")

add("2028_find_missing_observations", r"""<?php
// LeetCode 2028 - Find Missing Observations
// https://leetcode.com/problems/find-missing-observations/

class Solution {
    /**
     * @param Integer[] $rolls
     * @param Integer $mean
     * @param Integer $n
     * @return Integer[]
     */
    function missingRolls($rolls, $mean, $n) {
        $sum = 0;
        foreach ($rolls as $r) $sum += $r;
        $remain = $mean * (count($rolls) + $n) - $sum;
        if ($remain < $n || $remain > 6 * $n) return [];
        $ans = [];
        $baseVal = intdiv($remain, $n);
        $extra = $remain % $n;
        for ($i = 0; $i < $n; $i++) $ans[$i] = $baseVal + ($i < $extra ? 1 : 0);
        return $ans;
    }
}
""")

add("2029_stone_game_ix", r"""<?php
// LeetCode 2029 - Stone Game IX
// https://leetcode.com/problems/stone-game-ix/

class Solution {
    /**
     * @param Integer[] $stones
     * @return Boolean
     */
    function stoneGameIX($stones) {
        $cnt = [0, 0, 0];
        foreach ($stones as $s) $cnt[$s % 3]++;
        if ($cnt[0] % 2 === 0) return $cnt[1] > 0 && $cnt[2] > 0;
        return abs($cnt[1] - $cnt[2]) > 2;
    }
}
""")

add("2030_smallest_k_length_subsequence_with_occurrences_of_a_letter", r"""<?php
// LeetCode 2030 - Smallest K-Length Subsequence With Occurrences of a Letter
// https://leetcode.com/problems/smallest-k-length-subsequence-with-occurrences-of-a-letter/

class Solution {
    /**
     * @param String $s
     * @param Integer $k
     * @param String $letter
     * @param Integer $repetition
     * @return String
     */
    function smallestSubsequence($s, $k, $letter, $repetition) {
        $n = strlen($s);
        $remainLetter = 0;
        for ($i = 0; $i < $n; $i++) if ($s[$i] === $letter) $remainLetter++;
        $stack = "";
        $inStackLetter = 0;
        for ($i = 0; $i < $n; $i++) {
            $ch = $s[$i];
            while (strlen($stack) > 0 && $ch < $stack[strlen($stack) - 1] && strlen($stack) + $n - $i > $k) {
                $top = $stack[strlen($stack) - 1];
                if ($top === $letter) {
                    if ($inStackLetter + $remainLetter - 1 < $repetition) break;
                    $inStackLetter--;
                }
                $stack = substr($stack, 0, -1);
            }
            if (strlen($stack) < $k) {
                if ($ch === $letter) { $stack .= $ch; $inStackLetter++; }
                else if ($k - strlen($stack) > $repetition - $inStackLetter) $stack .= $ch;
            }
            if ($ch === $letter) $remainLetter--;
        }
        return $stack;
    }
}
""")

add("2031_count_subarrays_with_more_ones_than_zeros", r"""<?php
// LeetCode 2031 - Count Subarrays With More Ones Than Zeros
// https://leetcode.com/problems/count-subarrays-with-more-ones-than-zeros/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function subarraysWithMoreZerosThanOnes($nums) {
        $MOD = 1000000007;
        $n = count($nums);
        $bit = array_fill(0, 2 * $n + 7, 0);
        $add = function ($i, $v) use (&$bit) {
            $len = count($bit);
            for (; $i < $len; $i += $i & -$i) $bit[$i] += $v;
        };
        $sum = function ($i) use (&$bit) {
            $s = 0;
            for (; $i > 0; $i -= $i & -$i) $s += $bit[$i];
            return $s;
        };
        $offset = $n + 1;
        $pref = 0;
        $ans = 0;
        $add($offset, 1);
        foreach ($nums as $x) {
            $pref += ($x === 1) ? 1 : -1;
            $idx = $pref + $offset;
            $ans = ($ans + $sum($idx - 1)) % $MOD;
            $add($idx, 1);
        }
        return $ans;
    }
}
""")

add("2032_two_out_of_three", r"""<?php
// LeetCode 2032 - Two Out of Three
// https://leetcode.com/problems/two-out-of-three/

class Solution {
    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @param Integer[] $nums3
     * @return Integer[]
     */
    function twoOutOfThree($nums1, $nums2, $nums3) {
        $s0 = array_flip($nums1);
        $s1 = array_flip($nums2);
        $s2 = array_flip($nums3);
        $ans = [];
        for ($v = 1; $v <= 100; $v++) {
            $c = (isset($s0[$v]) ? 1 : 0) + (isset($s1[$v]) ? 1 : 0) + (isset($s2[$v]) ? 1 : 0);
            if ($c >= 2) $ans[] = $v;
        }
        return $ans;
    }
}
""")

add("2033_minimum_operations_to_make_a_uni_value_grid", r"""<?php
// LeetCode 2033 - Minimum Operations to Make a Uni-Value Grid
// https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/

class Solution {
    /**
     * @param Integer[][] $grid
     * @param Integer $x
     * @return Integer
     */
    function minOperations($grid, $x) {
        $vals = [];
        $bas = $grid[0][0] % $x;
        foreach ($grid as $row) {
            foreach ($row as $v) {
                if ($v % $x !== $bas) return -1;
                $vals[] = $v;
            }
        }
        sort($vals);
        $median = $vals[intdiv(count($vals), 2)];
        $ans = 0;
        foreach ($vals as $v) $ans += intdiv(abs($v - $median), $x);
        return $ans;
    }
}
""")

add("2034_stock_price_fluctuation", r"""<?php
// LeetCode 2034 - Stock Price Fluctuation
// https://leetcode.com/problems/stock-price-fluctuation/

class StockPrice {
    private $latestTs = 0;
    private $priceAt = [];
    private $maxHeap;
    private $minHeap;

    function __construct() {
        $this->maxHeap = new SplPriorityQueue();
        $this->minHeap = new SplPriorityQueue();
    }

    /**
     * @param Integer $timestamp
     * @param Integer $price
     * @return NULL
     */
    function update($timestamp, $price) {
        $this->priceAt[$timestamp] = $price;
        if ($timestamp >= $this->latestTs) $this->latestTs = $timestamp;
        $this->maxHeap->insert([$price, $timestamp], $price);
        $this->minHeap->insert([$price, $timestamp], -$price);
    }

    /**
     * @return Integer
     */
    function current() {
        return $this->priceAt[$this->latestTs];
    }

    /**
     * @return Integer
     */
    function maximum() {
        while (true) {
            $top = $this->maxHeap->top();
            if ($this->priceAt[$top[1]] === $top[0]) return $top[0];
            $this->maxHeap->extract();
        }
    }

    /**
     * @return Integer
     */
    function minimum() {
        while (true) {
            $top = $this->minHeap->top();
            if ($this->priceAt[$top[1]] === $top[0]) return $top[0];
            $this->minHeap->extract();
        }
    }
}
""")

add("2035_partition_array_into_two_arrays_to_minimize_sum_difference", r"""<?php
// LeetCode 2035 - Partition Array Into Two Arrays to Minimize Sum Difference
// https://leetcode.com/problems/partition-array-into-two-arrays-to-minimize-sum-difference/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function minimumDifference($nums) {
        $n = intdiv(count($nums), 2);
        $total = array_sum($nums);
        $left = array_slice($nums, 0, $n);
        $right = array_slice($nums, $n);
        $sumsByCount = function ($arr) {
            $m = count($arr);
            $res = array_fill(0, $m + 1, []);
            $lim = 1 << $m;
            for ($mask = 0; $mask < $lim; $mask++) {
                $sum = 0;
                $c = 0;
                for ($i = 0; $i < $m; $i++) if (($mask & (1 << $i)) !== 0) { $sum += $arr[$i]; $c++; }
                $res[$c][] = $sum;
            }
            foreach ($res as &$v) sort($v);
            return $res;
        };
        $L = $sumsByCount($left);
        $R = $sumsByCount($right);
        $ans = PHP_INT_MAX;
        for ($k = 0; $k <= $n; $k++) {
            foreach ($L[$k] as $s1) {
                $need = intdiv($total, 2) - $s1;
                $arr = $R[$n - $k];
                $lo = 0;
                $hi = count($arr);
                while ($lo < $hi) {
                    $mid = ($lo + $hi) >> 1;
                    if ($arr[$mid] < $need) $lo = $mid + 1;
                    else $hi = $mid;
                }
                foreach ([$lo - 1, $lo] as $j) {
                    if ($j >= 0 && $j < count($arr)) {
                        $s2 = $arr[$j];
                        $ans = min($ans, abs($total - 2 * ($s1 + $s2)));
                    }
                }
            }
        }
        return $ans;
    }
}
""")

add("2036_maximum_alternating_subarray_sum", r"""<?php
// LeetCode 2036 - Maximum Alternating Subarray Sum
// https://leetcode.com/problems/maximum-alternating-subarray-sum/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maximumAlternatingSubarraySum($nums) {
        $ans = PHP_INT_MIN;
        $even = 0;
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            $x = $nums[$i];
            if ($i % 2 === 0) $even += $x;
            else $even = max(0, $even - $x);
            $ans = max($ans, $even);
        }
        $odd = 0;
        for ($i = 1; $i < $n; $i++) {
            $x = $nums[$i];
            if ($i % 2 === 1) $odd += $x;
            else $odd = max(0, $odd - $x);
            $ans = max($ans, $odd);
        }
        return $ans;
    }
}
""")

add("2037_minimum_number_of_moves_to_seat_everyone", r"""<?php
// LeetCode 2037 - Minimum Number of Moves to Seat Everyone
// https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/

class Solution {
    /**
     * @param Integer[] $seats
     * @param Integer[] $students
     * @return Integer
     */
    function minMovesToSeat($seats, $students) {
        sort($seats);
        sort($students);
        $ans = 0;
        $n = count($seats);
        for ($i = 0; $i < $n; $i++) $ans += abs($seats[$i] - $students[$i]);
        return $ans;
    }
}
""")

add("2038_remove_colored_pieces_if_both_neighbors_are_the_same_color", r"""<?php
// LeetCode 2038 - Remove Colored Pieces if Both Neighbors are the Same Color
// https://leetcode.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/

class Solution {
    /**
     * @param String $colors
     * @return Boolean
     */
    function winnerOfGame($colors) {
        $a = 0;
        $b = 0;
        $n = strlen($colors);
        for ($i = 1; $i + 1 < $n; $i++) {
            if ($colors[$i - 1] === $colors[$i] && $colors[$i] === $colors[$i + 1]) {
                if ($colors[$i] === 'A') $a++;
                else $b++;
            }
        }
        return $a > $b;
    }
}
""")

add("2039_the_time_when_the_network_becomes_idle", r"""<?php
// LeetCode 2039 - The Time When the Network Becomes Idle
// https://leetcode.com/problems/the-time-when-the-network-becomes-idle/

class Solution {
    /**
     * @param Integer[][] $edges
     * @param Integer[] $patience
     * @return Integer
     */
    function networkBecomesIdle($edges, $patience) {
        $n = count($patience);
        $g = array_fill(0, $n, []);
        foreach ($edges as $e) { $g[$e[0]][] = $e[1]; $g[$e[1]][] = $e[0]; }
        $dist = array_fill(0, $n, -1);
        $q = [0];
        $dist[0] = 0;
        while ($q) {
            $u = array_shift($q);
            foreach ($g[$u] as $v) if ($dist[$v] === -1) { $dist[$v] = $dist[$u] + 1; $q[] = $v; }
        }
        $ans = 0;
        for ($i = 1; $i < $n; $i++) {
            $round = $dist[$i] * 2;
            $lastSend = intdiv($round - 1, $patience[$i]) * $patience[$i];
            $ans = max($ans, $lastSend + $round);
        }
        return $ans + 1;
    }
}
""")

add("2040_kth_smallest_product_of_two_sorted_arrays", r"""<?php
// LeetCode 2040 - Kth Smallest Product of Two Sorted Arrays
// https://leetcode.com/problems/kth-smallest-product-of-two-sorted-arrays/

class Solution {
    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @param Integer $k
     * @return Integer
     */
    function kthSmallestProduct($nums1, $nums2, $k) {
        $countLE = function ($x) use ($nums1, $nums2) {
            $cnt = 0;
            $m = count($nums2);
            foreach ($nums1 as $a) {
                if ($a > 0) {
                    $lo = 0;
                    $hi = $m;
                    while ($lo < $hi) {
                        $mid = ($lo + $hi) >> 1;
                        if ($a * $nums2[$mid] <= $x) $lo = $mid + 1;
                        else $hi = $mid;
                    }
                    $cnt += $lo;
                } else if ($a < 0) {
                    $lo = 0;
                    $hi = $m;
                    while ($lo < $hi) {
                        $mid = ($lo + $hi) >> 1;
                        if ($a * $nums2[$mid] <= $x) $hi = $mid;
                        else $lo = $mid + 1;
                    }
                    $cnt += $m - $lo;
                } else if ($x >= 0) $cnt += $m;
            }
            return $cnt;
        };
        $lo = -10000000000;
        $hi = 10000000000;
        while ($lo < $hi) {
            $mid = $lo + intdiv($hi - $lo, 2);
            if ($countLE($mid) >= $k) $hi = $mid;
            else $lo = $mid + 1;
        }
        return $lo;
    }
}
""")

add("2042_check_if_numbers_are_ascending_in_a_sentence", r"""<?php
// LeetCode 2042 - Check if Numbers Are Ascending in a Sentence
// https://leetcode.com/problems/check-if-numbers-are-ascending-in-a-sentence/

class Solution {
    /**
     * @param String $s
     * @return Boolean
     */
    function areNumbersAscending($s) {
        $prev = -1;
        foreach (explode(" ", $s) as $tok) {
            if ($tok === "") continue;
            if ($tok[0] >= '0' && $tok[0] <= '9') {
                $v = intval($tok);
                if ($v <= $prev) return false;
                $prev = $v;
            }
        }
        return true;
    }
}
""")

add("2043_simple_bank_system", r"""<?php
// LeetCode 2043 - Simple Bank System
// https://leetcode.com/problems/simple-bank-system/

class Bank {
    private $bal = [];

    /**
     * @param Integer[] $balance
     */
    function __construct($balance) {
        $this->bal = $balance;
    }

    private function valid($account) {
        return $account >= 1 && $account <= count($this->bal);
    }

    /**
     * @param Integer $account1
     * @param Integer $account2
     * @param Integer $money
     * @return Boolean
     */
    function transfer($account1, $account2, $money) {
        if (!$this->valid($account1) || !$this->valid($account2) || $this->bal[$account1 - 1] < $money) return false;
        $this->bal[$account1 - 1] -= $money;
        $this->bal[$account2 - 1] += $money;
        return true;
    }

    /**
     * @param Integer $account
     * @param Integer $money
     * @return Boolean
     */
    function deposit($account, $money) {
        if (!$this->valid($account)) return false;
        $this->bal[$account - 1] += $money;
        return true;
    }

    /**
     * @param Integer $account
     * @param Integer $money
     * @return Boolean
     */
    function withdraw($account, $money) {
        if (!$this->valid($account) || $this->bal[$account - 1] < $money) return false;
        $this->bal[$account - 1] -= $money;
        return true;
    }
}
""")

add("2044_count_number_of_maximum_bitwise_or_subsets", r"""<?php
// LeetCode 2044 - Count Number of Maximum Bitwise-OR Subsets
// https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function countMaxOrSubsets($nums) {
        $maxOr = 0;
        $ans = 0;
        foreach ($nums as $x) $maxOr |= $x;
        $dfs = null;
        $dfs = function ($i, $cur) use (&$dfs, $nums, $maxOr, &$ans) {
            if ($i === count($nums)) { if ($cur === $maxOr) $ans++; return; }
            $dfs($i + 1, $cur);
            $dfs($i + 1, $cur | $nums[$i]);
        };
        $dfs(0, 0);
        return $ans;
    }
}
""")

add("2045_second_minimum_time_to_reach_destination", r"""<?php
// LeetCode 2045 - Second Minimum Time to Reach Destination
// https://leetcode.com/problems/second-minimum-time-to-reach-destination/

class Solution {
    /**
     * @param Integer $n
     * @param Integer[][] $edges
     * @param Integer $time
     * @param Integer $change
     * @return Integer
     */
    function secondMinimum($n, $edges, $time, $change) {
        $g = array_fill(0, $n + 1, []);
        foreach ($edges as $e) { $g[$e[0]][] = $e[1]; $g[$e[1]][] = $e[0]; }
        $dist1 = array_fill(0, $n + 1, -1);
        $dist2 = array_fill(0, $n + 1, -1);
        $q = [[1, 0]];
        $dist1[1] = 0;
        while ($q) {
            [$u, $d] = array_shift($q);
            foreach ($g[$u] as $v) {
                $nd = $d + 1;
                if ($dist1[$v] === -1) { $dist1[$v] = $nd; $q[] = [$v, $nd]; }
                else if ($dist2[$v] === -1 && $nd > $dist1[$v]) { $dist2[$v] = $nd; $q[] = [$v, $nd]; }
            }
        }
        $steps = $dist2[$n];
        $ans = 0;
        for ($i = 0; $i < $steps; $i++) {
            if (intdiv($ans, $change) % 2 === 1) $ans += $change - $ans % $change;
            $ans += $time;
        }
        return $ans;
    }
}
""")

add("2046_sort_linked_list_already_sorted_using_absolute_values", r"""<?php
// LeetCode 2046 - Sort Linked List Already Sorted Using Absolute Values
// https://leetcode.com/problems/sort-linked-list-already-sorted-using-absolute-values/

class ListNode {
    public $val = 0;
    public $next = null;
    function __construct($val = 0, $next = null) {
        $this->val = $val;
        $this->next = $next;
    }
}

class Solution {
    /**
     * @param ListNode $head
     * @return ListNode
     */
    function sortLinkedList($head) {
        if ($head === null) return null;
        $prev = $head;
        $cur = $head->next;
        while ($cur) {
            if ($cur->val < 0) {
                $prev->next = $cur->next;
                $cur->next = $head;
                $head = $cur;
                $cur = $prev->next;
            } else {
                $prev = $cur;
                $cur = $cur->next;
            }
        }
        return $head;
    }
}
""")

add("2047_number_of_valid_words_in_a_sentence", r"""<?php
// LeetCode 2047 - Number of Valid Words in a Sentence
// https://leetcode.com/problems/number-of-valid-words-in-a-sentence/

class Solution {
    /**
     * @param String $sentence
     * @return Integer
     */
    function countValidWords($sentence) {
        $valid = function ($w) {
            $len = strlen($w);
            if ($len === 0) return false;
            $hyphen = 0;
            for ($i = 0; $i < $len; $i++) {
                $c = $w[$i];
                if ($c >= '0' && $c <= '9') return false;
                if ($c === '-') {
                    $hyphen++;
                    if ($hyphen > 1 || $i === 0 || $i === $len - 1) return false;
                    if ($w[$i - 1] < 'a' || $w[$i - 1] > 'z' || $w[$i + 1] < 'a' || $w[$i + 1] > 'z') return false;
                } else if ($c === '!' || $c === '.' || $c === ',') {
                    if ($i !== $len - 1) return false;
                } else if ($c < 'a' || $c > 'z') return false;
            }
            return true;
        };
        $ans = 0;
        foreach (explode(" ", $sentence) as $tok)
            if ($valid($tok)) $ans++;
        return $ans;
    }
}
""")

add("2048_next_greater_numerically_balanced_number", r"""<?php
// LeetCode 2048 - Next Greater Numerically Balanced Number
// https://leetcode.com/problems/next-greater-numerically-balanced-number/

class Solution {
    /**
     * @param Integer $n
     * @return Integer
     */
    function nextBeautifulNumber($n) {
        $balanced = function ($x) {
            $cnt = array_fill(0, 10, 0);
            while ($x > 0) { $cnt[$x % 10]++; $x = intdiv($x, 10); }
            for ($d = 0; $d < 10; $d++) if ($cnt[$d] !== 0 && $cnt[$d] !== $d) return false;
            return true;
        };
        for ($x = $n + 1; ; $x++) if ($balanced($x)) return $x;
    }
}
""")

add("2049_count_nodes_with_the_highest_score", r"""<?php
// LeetCode 2049 - Count Nodes With the Highest Score
// https://leetcode.com/problems/count-nodes-with-the-highest-score/

class Solution {
    /**
     * @param Integer[] $parents
     * @return Integer
     */
    function countHighestScoreNodes($parents) {
        $n = count($parents);
        $children = array_fill(0, $n, []);
        for ($i = 1; $i < $n; $i++) $children[$parents[$i]][] = $i;
        $size = array_fill(0, $n, 0);
        $dfs = null;
        $dfs = function ($u) use (&$dfs, &$size, &$children) {
            $size[$u] = 1;
            foreach ($children[$u] as $v) $size[$u] += $dfs($v);
            return $size[$u];
        };
        $dfs(0);
        $best = 0;
        $ans = 0;
        for ($u = 0; $u < $n; $u++) {
            $score = 1;
            foreach ($children[$u] as $v) $score *= $size[$v];
            $up = $n - $size[$u];
            if ($up > 0) $score *= $up;
            if ($score > $best) { $best = $score; $ans = 1; }
            else if ($score === $best) $ans++;
        }
        return $ans;
    }
}
""")

add("2050_parallel_courses_iii", r"""<?php
// LeetCode 2050 - Parallel Courses III
// https://leetcode.com/problems/parallel-courses-iii/

class Solution {
    /**
     * @param Integer $n
     * @param Integer[][] $relations
     * @param Integer[] $time
     * @return Integer
     */
    function minimumTime($n, $relations, $time) {
        $g = array_fill(0, $n + 1, []);
        $indeg = array_fill(0, $n + 1, 0);
        $dist = array_fill(0, $n + 1, 0);
        foreach ($relations as $e) { $g[$e[0]][] = $e[1]; $indeg[$e[1]]++; }
        $q = [];
        for ($i = 1; $i <= $n; $i++) {
            $dist[$i] = $time[$i - 1];
            if ($indeg[$i] === 0) $q[] = $i;
        }
        while ($q) {
            $u = array_shift($q);
            foreach ($g[$u] as $v) {
                $dist[$v] = max($dist[$v], $dist[$u] + $time[$v - 1]);
                if (--$indeg[$v] === 0) $q[] = $v;
            }
        }
        $ans = 0;
        for ($i = 1; $i <= $n; $i++) $ans = max($ans, $dist[$i]);
        return $ans;
    }
}
""")


def main() -> None:
    ported = 0
    for folder, content in SOLUTIONS.items():
        path = ROOT / folder / "solution.php"
        path.write_text(content, encoding="utf-8", newline="\n")
        ported += 1
        print(f"ported {folder}")
    print(f"ported={ported}")


if __name__ == "__main__":
    main()

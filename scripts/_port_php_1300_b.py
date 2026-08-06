#!/usr/bin/env python3
"""Port PHP solutions for LeetCode stubs batch B (1342-1381)."""
from __future__ import annotations

import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SOLUTIONS: dict[str, str] = {
    "1342_number_of_steps_to_reduce_a_number_to_zero": r'''<?php
class Solution {
    function numberOfSteps($num) {
        $steps = 0;
        while ($num) {
            $num = $num % 2 === 0 ? intdiv($num, 2) : $num - 1;
            $steps++;
        }
        return $steps;
    }
}
''',
    "1343_number_of_sub_arrays_of_size_k_and_average_greater_than_or_equal_to_threshold": r'''<?php
class Solution {
    function numOfSubarrays($arr, $k, $threshold) {
        $window = array_sum(array_slice($arr, 0, $k));
        $answer = $window >= $k * $threshold ? 1 : 0;
        for ($i = $k; $i < count($arr); $i++) {
            $window += $arr[$i] - $arr[$i - $k];
            if ($window >= $k * $threshold) $answer++;
        }
        return $answer;
    }
}
''',
    "1344_angle_between_hands_of_a_clock": r'''<?php
class Solution {
    function angleClock($hour, $minutes) {
        $difference = abs(($hour % 12) * 30 + $minutes * 0.5 - $minutes * 6);
        return min($difference, 360 - $difference);
    }
}
''',
    "1345_jump_game_iv": r'''<?php
class Solution {
    function minJumps($arr) {
        $n = count($arr);
        $positions = [];
        for ($i = 0; $i < $n; $i++) $positions[$arr[$i]][] = $i;
        $queue = [0];
        $seen = [0 => true];
        $steps = 0;
        while ($queue) {
            $size = count($queue);
            for ($s = 0; $s < $size; $s++) {
                $i = array_shift($queue);
                if ($i === $n - 1) return $steps;
                $next = $positions[$arr[$i]] ?? [];
                unset($positions[$arr[$i]]);
                $next[] = $i - 1;
                $next[] = $i + 1;
                foreach ($next as $j) {
                    if ($j >= 0 && $j < $n && !isset($seen[$j])) {
                        $seen[$j] = true;
                        $queue[] = $j;
                    }
                }
            }
            $steps++;
        }
        return -1;
    }
}
''',
    "1346_check_if_n_and_its_double_exist": r'''<?php
class Solution {
    function checkIfExist($arr) {
        $seen = [];
        foreach ($arr as $value) {
            if (isset($seen[2 * $value]) || ($value % 2 === 0 && isset($seen[intdiv($value, 2)]))) return true;
            $seen[$value] = true;
        }
        return false;
    }
}
''',
    "1347_minimum_number_of_steps_to_make_two_strings_anagram": r'''<?php
class Solution {
    function minSteps($s, $t) {
        $count = array_fill(0, 26, 0);
        for ($i = 0; $i < strlen($s); $i++) {
            $count[ord($s[$i]) - 97]++;
            $count[ord($t[$i]) - 97]--;
        }
        $answer = 0;
        foreach ($count as $c) if ($c > 0) $answer += $c;
        return $answer;
    }
}
''',
    "1348_tweet_counts_per_frequency": r'''<?php
class TweetCounts {
    private $times = [];

    function __construct() {
        $this->times = [];
    }

    function recordTweet($tweetName, $time) {
        $this->times[$tweetName][] = $time;
        sort($this->times[$tweetName]);
    }

    function getTweetCountsPerFrequency($freq, $tweetName, $startTime, $endTime) {
        $size = ["minute" => 60, "hour" => 3600, "day" => 86400][$freq];
        $times = $this->times[$tweetName] ?? [];
        $answer = [];
        for ($start = $startTime; $start <= $endTime; $start += $size) {
            $end = min($endTime, $start + $size - 1);
            $count = 0;
            foreach ($times as $t) {
                if ($t >= $start && $t <= $end) $count++;
            }
            $answer[] = $count;
        }
        return $answer;
    }
}
''',
    "1349_maximum_students_taking_exam": r'''<?php
class Solution {
    function maxStudents($seats) {
        $rows = count($seats);
        $cols = count($seats[0]);
        $validRows = [];
        foreach ($seats as $row) {
            $available = 0;
            for ($c = 0; $c < $cols; $c++) {
                if ($row[$c] === ".") $available |= 1 << $c;
            }
            $masks = [];
            for ($mask = 0; $mask < (1 << $cols); $mask++) {
                if (($mask & ~$available) === 0 && ($mask & ($mask << 1)) === 0) $masks[] = $mask;
            }
            $validRows[] = $masks;
        }
        $dp = [0 => 0];
        foreach ($validRows as $masks) {
            $nxt = [];
            foreach ($masks as $mask) {
                foreach ($dp as $previous => $count) {
                    if (($mask & ($previous << 1)) === 0 && ($mask & ($previous >> 1)) === 0) {
                        $nxt[$mask] = max($nxt[$mask] ?? 0, $count + substr_count(decbin($mask), "1"));
                    }
                }
            }
            $dp = $nxt;
        }
        return max($dp);
    }
}
''',
    "1351_count_negative_numbers_in_a_sorted_matrix": r'''<?php
class Solution {
    function countNegatives($grid) {
        $answer = 0;
        foreach ($grid as $row) {
            $n = count($row);
            $lo = 0;
            $hi = $n;
            while ($lo < $hi) {
                $mid = intdiv($lo + $hi, 2);
                if ($row[$mid] < 0) $hi = $mid;
                else $lo = $mid + 1;
            }
            $answer += $n - $lo;
        }
        return $answer;
    }
}
''',
    "1352_product_of_the_last_k_numbers": r'''<?php
class ProductOfNumbers {
    private $p;

    function __construct() {
        $this->p = [1];
    }

    function add($num) {
        if ($num === 0) $this->p = [1];
        else $this->p[] = $this->p[count($this->p) - 1] * $num;
    }

    function getProduct($k) {
        $n = count($this->p);
        return $k >= $n ? 0 : intdiv($this->p[$n - 1], $this->p[$n - 1 - $k]);
    }
}
''',
    "1353_maximum_number_of_events_that_can_be_attended": r'''<?php
class Solution {
    function maxEvents($events) {
        usort($events, function($a, $b) { return $a[0] <=> $b[0]; });
        $h = new SplMinHeap();
        $i = 0;
        $ans = 0;
        $day = 0;
        $n = count($events);
        while ($i < $n || !$h->isEmpty()) {
            if ($h->isEmpty()) $day = max($day, $events[$i][0]);
            while ($i < $n && $events[$i][0] <= $day) {
                $h->insert($events[$i][1]);
                $i++;
            }
            while (!$h->isEmpty() && $h->top() < $day) $h->extract();
            if (!$h->isEmpty()) {
                $h->extract();
                $ans++;
                $day++;
            }
        }
        return $ans;
    }
}
''',
    "1354_construct_target_array_with_multiple_sums": r'''<?php
class Solution {
    function isPossible($target) {
        if (count($target) === 1) return $target[0] === 1;
        $h = new SplMaxHeap();
        $total = 0;
        foreach ($target as $x) {
            $h->insert($x);
            $total += $x;
        }
        while (true) {
            $x = $h->extract();
            $rest = $total - $x;
            if ($x === 1 || $rest === 1) return true;
            if ($rest === 0 || $x <= $rest) return false;
            $prev = $x % $rest;
            if ($prev === 0) return false;
            $total = $rest + $prev;
            $h->insert($prev);
        }
    }
}
''',
    "1356_sort_integers_by_the_number_of_1_bits": r'''<?php
class Solution {
    function sortByBits($arr) {
        usort($arr, function($a, $b) {
            $ca = substr_count(decbin($a), "1");
            $cb = substr_count(decbin($b), "1");
            if ($ca !== $cb) return $ca <=> $cb;
            return $a <=> $b;
        });
        return $arr;
    }
}
''',
    "1357_apply_discount_every_n_orders": r'''<?php
class Cashier {
    private $n;
    private $discount;
    private $price = [];
    private $count = 0;

    function __construct($n, $discount, $products, $prices) {
        $this->n = $n;
        $this->discount = $discount;
        foreach ($products as $i => $p) $this->price[$p] = $prices[$i];
        $this->count = 0;
    }

    function getBill($product, $amount) {
        $this->count++;
        $total = 0;
        foreach ($product as $i => $p) $total += $this->price[$p] * $amount[$i];
        if ($this->count % $this->n === 0) return $total * (100 - $this->discount) / 100.0;
        return floatval($total);
    }
}
''',
    "1358_number_of_substrings_containing_all_three_characters": r'''<?php
class Solution {
    function numberOfSubstrings($s) {
        $last = [-1, -1, -1];
        $ans = 0;
        for ($i = 0; $i < strlen($s); $i++) {
            $last[ord($s[$i]) - 97] = $i;
            $ans += min($last) + 1;
        }
        return $ans;
    }
}
''',
    "1359_count_all_valid_pickup_and_delivery_options": r'''<?php
class Solution {
    function countOrders($n) {
        $ans = 1;
        $mod = 1000000007;
        for ($i = 1; $i <= $n; $i++) $ans = $ans * $i * (2 * $i - 1) % $mod;
        return $ans;
    }
}
''',
    "1360_number_of_days_between_two_dates": r'''<?php
class Solution {
    function daysBetweenDates($date1, $date2) {
        $t1 = strtotime($date1);
        $t2 = strtotime($date2);
        return intval(abs($t1 - $t2) / 86400);
    }
}
''',
    "1361_validate_binary_tree_nodes": r'''<?php
class Solution {
    function validateBinaryTreeNodes($n, $leftChild, $rightChild) {
        $indeg = array_fill(0, $n, 0);
        foreach (array_merge($leftChild, $rightChild) as $x) {
            if ($x !== -1) {
                $indeg[$x]++;
                if ($indeg[$x] > 1) return false;
            }
        }
        $roots = [];
        for ($i = 0; $i < $n; $i++) if ($indeg[$i] === 0) $roots[] = $i;
        if (count($roots) !== 1) return false;
        $seen = [];
        $st = $roots;
        while ($st) {
            $u = array_pop($st);
            if (isset($seen[$u])) return false;
            $seen[$u] = true;
            foreach ([$leftChild[$u], $rightChild[$u]] as $v) {
                if ($v !== -1) $st[] = $v;
            }
        }
        return count($seen) === $n;
    }
}
''',
    "1362_closest_divisors": r'''<?php
class Solution {
    function closestDivisors($num) {
        $best = null;
        foreach ([$num + 1, $num + 2] as $x) {
            for ($a = intval(sqrt($x)); $a >= 1; $a--) {
                if ($x % $a === 0) {
                    $pair = [$a, intdiv($x, $a)];
                    if ($best === null || $pair[1] - $pair[0] < $best[1] - $best[0]) $best = $pair;
                    break;
                }
            }
        }
        return $best;
    }
}
''',
    "1363_largest_multiple_of_three": r'''<?php
class Solution {
    function largestMultipleOfThree($digits) {
        $cnt = array_fill(0, 10, 0);
        $sum = 0;
        foreach ($digits as $d) {
            $cnt[$d]++;
            $sum += $d;
        }
        $rem = $sum % 3;
        $remove = function($r, $k) use (&$cnt) {
            for ($d = $r; $d < 10; $d += 3) {
                while ($cnt[$d] && $k) {
                    $cnt[$d]--;
                    $k--;
                }
                if (!$k) return true;
            }
            return false;
        };
        if ($rem && !$remove($rem, 1)) $remove(3 - $rem, 2);
        $s = "";
        for ($d = 9; $d >= 0; $d--) $s .= str_repeat(strval($d), $cnt[$d]);
        if ($s !== "" && $s[0] === "0") return "0";
        return $s;
    }
}
''',
    "1365_how_many_numbers_are_smaller_than_the_current_number": r'''<?php
class Solution {
    function smallerNumbersThanCurrent($nums) {
        $sorted = $nums;
        sort($sorted);
        $rank = [];
        foreach ($sorted as $i => $x) {
            if (!array_key_exists($x, $rank)) $rank[$x] = $i;
        }
        $answer = [];
        foreach ($nums as $x) $answer[] = $rank[$x];
        return $answer;
    }
}
''',
    "1366_rank_teams_by_votes": r'''<?php
class Solution {
    function rankTeams($votes) {
        $m = strlen($votes[0]);
        $count = [];
        foreach (str_split($votes[0]) as $c) $count[$c] = array_fill(0, $m, 0);
        foreach ($votes as $v) {
            for ($i = 0; $i < $m; $i++) $count[$v[$i]][$i]++;
        }
        $teams = array_keys($count);
        usort($teams, function($a, $b) use ($count) {
            for ($i = 0; $i < count($count[$a]); $i++) {
                if ($count[$a][$i] !== $count[$b][$i]) return $count[$b][$i] <=> $count[$a][$i];
            }
            return $a <=> $b;
        });
        return implode("", $teams);
    }
}
''',
    "1367_linked_list_in_binary_tree": r'''<?php
class Solution {
    function isSubPath($head, $root) {
        $match = function($a, $b) use (&$match) {
            return !$a || ($b && $a->val === $b->val && ($match($a->next, $b->left) || $match($a->next, $b->right)));
        };
        return $root && ($match($head, $root) || $this->isSubPath($head, $root->left) || $this->isSubPath($head, $root->right));
    }
}
''',
    "1368_minimum_cost_to_make_at_least_one_valid_path_in_a_grid": r'''<?php
class Solution {
    function minCost($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        $dist = array_fill(0, $m, array_fill(0, $n, 1000000000));
        $dist[0][0] = 0;
        $q = [[0, 0]];
        $dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]];
        while ($q) {
            [$r, $c] = array_shift($q);
            foreach ($dirs as $k => [$dr, $dc]) {
                $x = $r + $dr;
                $y = $c + $dc;
                if ($x >= 0 && $x < $m && $y >= 0 && $y < $n) {
                    $w = ($k + 1) !== $grid[$r][$c] ? 1 : 0;
                    $nd = $dist[$r][$c] + $w;
                    if ($nd < $dist[$x][$y]) {
                        $dist[$x][$y] = $nd;
                        if ($w) $q[] = [$x, $y];
                        else array_unshift($q, [$x, $y]);
                    }
                }
            }
        }
        return $dist[$m - 1][$n - 1];
    }
}
''',
    "1370_increasing_decreasing_string": r'''<?php
class Solution {
    function sortString($s) {
        $c = array_fill(0, 26, 0);
        for ($i = 0; $i < strlen($s); $i++) $c[ord($s[$i]) - 97]++;
        $out = "";
        while (strlen($out) < strlen($s)) {
            for ($i = 0; $i < 26; $i++) {
                if ($c[$i]) {
                    $out .= chr(97 + $i);
                    $c[$i]--;
                }
            }
            for ($i = 25; $i >= 0; $i--) {
                if ($c[$i]) {
                    $out .= chr(97 + $i);
                    $c[$i]--;
                }
            }
        }
        return $out;
    }
}
''',
    "1371_find_the_longest_substring_containing_vowels_in_even_counts": r'''<?php
class Solution {
    function findTheLongestSubstring($s) {
        $first = [0 => -1];
        $mask = 0;
        $ans = 0;
        $vowels = "aeiou";
        for ($i = 0; $i < strlen($s); $i++) {
            $pos = strpos($vowels, $s[$i]);
            if ($pos !== false) $mask ^= 1 << $pos;
            if (array_key_exists($mask, $first)) $ans = max($ans, $i - $first[$mask]);
            else $first[$mask] = $i;
        }
        return $ans;
    }
}
''',
    "1372_longest_zigzag_path_in_a_binary_tree": r'''<?php
class Solution {
    private $ans = 0;
    function longestZigZag($root) {
        $this->ans = 0;
        $this->dfs($root);
        return $this->ans;
    }
    private function dfs($node) {
        if (!$node) return [-1, -1];
        $l = $this->dfs($node->left);
        $r = $this->dfs($node->right);
        $a = $l[1] + 1;
        $b = $r[0] + 1;
        $this->ans = max($this->ans, $a, $b);
        return [$a, $b];
    }
}
''',
    "1373_maximum_sum_bst_in_binary_tree": r'''<?php
class Solution {
    private $ans = 0;
    function maxSumBST($root) {
        $this->ans = 0;
        $this->dfs($root);
        return $this->ans;
    }
    private function dfs($node) {
        if (!$node) return [true, PHP_INT_MAX, PHP_INT_MIN, 0];
        [$a, $lx, $lh, $ls] = $this->dfs($node->left);
        [$b, $rx, $rh, $rs] = $this->dfs($node->right);
        if ($a && $b && $lh < $node->val && $node->val < $rx) {
            $s = $ls + $rs + $node->val;
            $this->ans = max($this->ans, $s);
            return [true, min($lx, $node->val), max($rh, $node->val), $s];
        }
        return [false, 0, 0, 0];
    }
}
''',
    "1374_generate_a_string_with_characters_that_have_odd_counts": r'''<?php
class Solution {
    function generateTheString($n) {
        return $n % 2 ? str_repeat("a", $n) : str_repeat("a", $n - 1) . "b";
    }
}
''',
    "1375_number_of_times_binary_string_is_prefix_aligned": r'''<?php
class Solution {
    function numTimesAllBlue($flips) {
        $ans = 0;
        $mx = 0;
        foreach ($flips as $i => $x) {
            $mx = max($mx, $x);
            if ($mx === $i + 1) $ans++;
        }
        return $ans;
    }
}
''',
    "1376_time_needed_to_inform_all_employees": r'''<?php
class Solution {
    function numOfMinutes($n, $headID, $manager, $informTime) {
        $children = array_fill(0, $n, []);
        foreach ($manager as $i => $p) {
            if ($p !== -1) $children[$p][] = $i;
        }
        $dfs = function($u) use (&$dfs, $children, $informTime) {
            $best = 0;
            foreach ($children[$u] as $v) $best = max($best, $dfs($v));
            return $informTime[$u] + $best;
        };
        return $dfs($headID);
    }
}
''',
    "1377_frog_position_after_t_seconds": r'''<?php
class Solution {
    function frogPosition($n, $edges, $t, $target) {
        $g = array_fill(0, $n + 1, []);
        foreach ($edges as [$a, $b]) {
            $g[$a][] = $b;
            $g[$b][] = $a;
        }
        $dfs = function($u, $p, $time, $prob) use (&$dfs, $g, $t, $target) {
            $kids = [];
            foreach ($g[$u] as $v) if ($v !== $p) $kids[] = $v;
            if ($time === $t || !$kids) return $u === $target ? $prob : 0.0;
            $sum = 0.0;
            foreach ($kids as $v) $sum += $dfs($v, $u, $time + 1, $prob / count($kids));
            return $sum;
        };
        return $dfs(1, 0, 0, 1.0);
    }
}
''',
    "1379_find_a_corresponding_node_of_a_binary_tree_in_a_clone_of_that_tree": r'''<?php
class Solution {
    function getTargetCopy($original, $cloned, $target) {
        $wanted = is_object($target) ? $target->val : $target;
        $stack = [[$original, $cloned]];
        while ($stack) {
            [$a, $b] = array_pop($stack);
            if ($a->val === $wanted) return $b;
            if ($a->left) $stack[] = [$a->left, $b->left];
            if ($a->right) $stack[] = [$a->right, $b->right];
        }
        return null;
    }
}
''',
    "1380_lucky_numbers_in_a_matrix": r'''<?php
class Solution {
    function luckyNumbers($matrix) {
        $mins = [];
        foreach ($matrix as $r) $mins[min($r)] = true;
        $cols = count($matrix[0]);
        $maxs = [];
        for ($c = 0; $c < $cols; $c++) {
            $mx = $matrix[0][$c];
            for ($r = 1; $r < count($matrix); $r++) $mx = max($mx, $matrix[$r][$c]);
            $maxs[$mx] = true;
        }
        $answer = [];
        foreach ($mins as $v => $_) if (isset($maxs[$v])) $answer[] = $v;
        return $answer;
    }
}
''',
    "1381_design_a_stack_with_increment_operation": r'''<?php
class CustomStack {
    private $maxSize;
    private $a = [];

    function __construct($maxSize) {
        $this->maxSize = $maxSize;
        $this->a = [];
    }

    function push($x) {
        if (count($this->a) < $this->maxSize) $this->a[] = $x;
    }

    function pop() {
        return $this->a ? array_pop($this->a) : -1;
    }

    function increment($k, $val) {
        $limit = min($k, count($this->a));
        for ($i = 0; $i < $limit; $i++) $this->a[$i] += $val;
    }
}
''',
}


def main() -> None:
    written = 0
    for folder, content in SOLUTIONS.items():
        path = os.path.join(ROOT, folder, "solution.php")
        if not os.path.isdir(os.path.join(ROOT, folder)):
            raise SystemExit(f"missing folder: {folder}")
        with open(path, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(content)
        written += 1
        print(f"wrote {folder}")
    print(f"done: {written}")


if __name__ == "__main__":
    main()

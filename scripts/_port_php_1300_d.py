#!/usr/bin/env python3
"""Port PHP solutions for LeetCode stubs batch D (1423-1462)."""
from __future__ import annotations

import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SOLUTIONS: dict[str, str] = {
    "1423_maximum_points_you_can_obtain_from_cards": r'''<?php
class Solution {
    function maxScore($cardPoints, $k) {
        $n = count($cardPoints);
        if ($k === $n) return array_sum($cardPoints);
        $window = $n - $k;
        $current = array_sum(array_slice($cardPoints, 0, $window));
        $smallest = $current;
        for ($i = $window; $i < $n; $i++) {
            $current += $cardPoints[$i] - $cardPoints[$i - $window];
            $smallest = min($smallest, $current);
        }
        return array_sum($cardPoints) - $smallest;
    }
}
''',
    "1424_diagonal_traverse_ii": r'''<?php
class Solution {
    function findDiagonalOrder($nums) {
        $diagonals = [];
        foreach ($nums as $row => $values) {
            foreach ($values as $col => $value) {
                $diagonals[$row + $col][] = $value;
            }
        }
        ksort($diagonals);
        $answer = [];
        foreach ($diagonals as $values) {
            for ($i = count($values) - 1; $i >= 0; $i--) $answer[] = $values[$i];
        }
        return $answer;
    }
}
''',
    "1425_constrained_subsequence_sum": r'''<?php
class Solution {
    function constrainedSubsetSum($nums, $k) {
        $n = count($nums);
        $best = $nums;
        $queue = [];
        for ($i = 0; $i < $n; $i++) {
            while ($queue && $queue[0] < $i - $k) array_shift($queue);
            $best[$i] = $nums[$i] + max(0, $queue ? $best[$queue[0]] : 0);
            while ($queue && $best[$queue[count($queue) - 1]] <= $best[$i]) array_pop($queue);
            $queue[] = $i;
        }
        return max($best);
    }
}
''',
    "1426_counting_elements": r'''<?php
class Solution {
    function countElements($arr) {
        $values = array_flip($arr);
        $ans = 0;
        foreach ($arr as $value) if (isset($values[$value + 1])) $ans++;
        return $ans;
    }
}
''',
    "1427_perform_string_shifts": r'''<?php
class Solution {
    function stringShift($s, $shift) {
        $offset = 0;
        foreach ($shift as [$direction, $amount]) {
            $offset += $direction ? $amount : -$amount;
        }
        $n = strlen($s);
        $offset %= $n;
        if ($offset < 0) $offset += $n;
        if (!$offset) return $s;
        return substr($s, -$offset) . substr($s, 0, $n - $offset);
    }
}
''',
    "1428_leftmost_column_with_at_least_a_one": r'''<?php
class Solution {
    function leftMostColumnWithOne($binaryMatrix) {
        [$rows, $cols] = $binaryMatrix->dimensions();
        $row = 0;
        $col = $cols - 1;
        $answer = -1;
        while ($row < $rows && $col >= 0) {
            if ($binaryMatrix->get($row, $col) === 1) {
                $answer = $col;
                $col--;
            } else {
                $row++;
            }
        }
        return $answer;
    }
}
''',
    "1429_first_unique_number": r'''<?php
class FirstUnique {
    private $counts = [];
    private $unique = [];

    function __construct($nums) {
        foreach ($nums as $value) $this->add($value);
    }

    function showFirstUnique() {
        foreach ($this->unique as $value => $_) return $value;
        return -1;
    }

    function add($value) {
        $this->counts[$value] = ($this->counts[$value] ?? 0) + 1;
        if ($this->counts[$value] === 1) $this->unique[$value] = true;
        else unset($this->unique[$value]);
    }
}
''',
    "1430_check_if_a_string_is_a_valid_sequence_from_root_to_leaves_path_in_a_binary_tree": r'''<?php
class Solution {
    function isValidSequence($root, $arr) {
        $visit = function($node, $index) use (&$visit, $arr) {
            if (!$node || $index === count($arr) || $node->val !== $arr[$index]) return false;
            if (!$node->left && !$node->right) return $index === count($arr) - 1;
            return $visit($node->left, $index + 1) || $visit($node->right, $index + 1);
        };
        return $visit($root, 0);
    }
}
''',
    "1431_kids_with_the_greatest_number_of_candies": r'''<?php
class Solution {
    function kidsWithCandies($candies, $extraCandies) {
        $maximum = max($candies);
        $answer = [];
        foreach ($candies as $value) $answer[] = $value + $extraCandies >= $maximum;
        return $answer;
    }
}
''',
    "1432_max_difference_you_can_get_from_changing_an_integer": r'''<?php
class Solution {
    function maxDiff($num) {
        $s = strval($num);
        $high = $s;
        for ($i = 0; $i < strlen($s); $i++) {
            if ($s[$i] !== "9") {
                $high = str_replace($s[$i], "9", $s);
                break;
            }
        }
        $low = $s;
        if ($s[0] !== "1") {
            $low = str_replace($s[0], "1", $s);
        } else {
            for ($i = 1; $i < strlen($s); $i++) {
                if ($s[$i] !== "0" && $s[$i] !== "1") {
                    $low = str_replace($s[$i], "0", $s);
                    break;
                }
            }
        }
        return intval($high) - intval($low);
    }
}
''',
    "1433_check_if_a_string_can_break_another_string": r'''<?php
class Solution {
    function checkIfCanBreak($s1, $s2) {
        $a = str_split($s1);
        $b = str_split($s2);
        sort($a);
        sort($b);
        $ge = true;
        $le = true;
        for ($i = 0; $i < count($a); $i++) {
            if ($a[$i] < $b[$i]) $ge = false;
            if ($a[$i] > $b[$i]) $le = false;
        }
        return $ge || $le;
    }
}
''',
    "1434_number_of_ways_to_wear_different_hats_to_each_other": r'''<?php
class Solution {
    function numberWays($hats) {
        $mod = 1000000007;
        $people = count($hats);
        $wearers = array_fill(0, 41, []);
        foreach ($hats as $person => $choices) {
            foreach ($choices as $hat) $wearers[$hat][] = $person;
        }
        $dp = array_fill(0, 1 << $people, 0);
        $dp[0] = 1;
        for ($hat = 1; $hat <= 40; $hat++) {
            $nxt = $dp;
            foreach ($dp as $mask => $ways) {
                foreach ($wearers[$hat] as $person) {
                    if ((($mask >> $person) & 1) === 0) {
                        $nxt[$mask | (1 << $person)] = ($nxt[$mask | (1 << $person)] + $ways) % $mod;
                    }
                }
            }
            $dp = $nxt;
        }
        return $dp[(1 << $people) - 1];
    }
}
''',
    "1436_destination_city": r'''<?php
class Solution {
    function destCity($paths) {
        $starts = [];
        foreach ($paths as [$start, $end]) $starts[$start] = true;
        foreach ($paths as [$start, $end]) {
            if (!isset($starts[$end])) return $end;
        }
        return "";
    }
}
''',
    "1437_check_if_all_1s_are_at_least_length_k_places_away": r'''<?php
class Solution {
    function kLengthApart($nums, $k) {
        $previous = -$k - 1;
        foreach ($nums as $i => $value) {
            if ($value) {
                if ($i - $previous <= $k) return false;
                $previous = $i;
            }
        }
        return true;
    }
}
''',
    "1438_longest_continuous_subarray_with_absolute_diff_less_than_or_equal_to_limit": r'''<?php
class Solution {
    function longestSubarray($nums, $limit) {
        $low = [];
        $high = [];
        $left = 0;
        $answer = 0;
        foreach ($nums as $right => $value) {
            while ($low && $nums[$low[count($low) - 1]] > $value) array_pop($low);
            while ($high && $nums[$high[count($high) - 1]] < $value) array_pop($high);
            $low[] = $right;
            $high[] = $right;
            while ($nums[$high[0]] - $nums[$low[0]] > $limit) {
                $left++;
                if ($low[0] < $left) array_shift($low);
                if ($high[0] < $left) array_shift($high);
            }
            $answer = max($answer, $right - $left + 1);
        }
        return $answer;
    }
}
''',
    "1439_find_the_kth_smallest_sum_of_a_matrix_with_sorted_rows": r'''<?php
class Solution {
    function kthSmallest($mat, $k) {
        $sums = [0];
        foreach ($mat as $row) {
            $heap = new SplMinHeap();
            $heap->insert([$sums[0] + $row[0], 0, 0]);
            $merged = [];
            $seen = [];
            while (!$heap->isEmpty() && count($merged) < $k) {
                [$value, $i, $j] = $heap->extract();
                $key = "$i,$j";
                if (isset($seen[$key])) continue;
                $seen[$key] = true;
                $merged[] = $value;
                if ($j + 1 < count($row)) $heap->insert([$sums[$i] + $row[$j + 1], $i, $j + 1]);
                if ($j === 0 && $i + 1 < count($sums)) $heap->insert([$sums[$i + 1] + $row[0], $i + 1, 0]);
            }
            $sums = $merged;
        }
        return $sums[$k - 1];
    }
}
''',
    "1441_build_an_array_with_stack_operations": r'''<?php
class Solution {
    function buildArray($target, $n) {
        $answer = [];
        $current = 1;
        foreach ($target as $value) {
            while ($current < $value) {
                $answer[] = "Push";
                $answer[] = "Pop";
                $current++;
            }
            $answer[] = "Push";
            $current++;
        }
        return $answer;
    }
}
''',
    "1442_count_triplets_that_can_form_two_arrays_of_equal_xor": r'''<?php
class Solution {
    function countTriplets($arr) {
        $answer = 0;
        $n = count($arr);
        for ($i = 0; $i < $n; $i++) {
            $value = 0;
            for ($k = $i; $k < $n; $k++) {
                $value ^= $arr[$k];
                if ($value === 0) $answer += $k - $i;
            }
        }
        return $answer;
    }
}
''',
    "1443_minimum_time_to_collect_all_apples_in_a_tree": r'''<?php
class Solution {
    function minTime($n, $edges, $hasApple) {
        $graph = array_fill(0, $n, []);
        foreach ($edges as [$a, $b]) {
            $graph[$a][] = $b;
            $graph[$b][] = $a;
        }
        $visit = function($node, $parent) use (&$visit, $graph, $hasApple) {
            $cost = 0;
            foreach ($graph[$node] as $child) {
                if ($child !== $parent) {
                    $childCost = $visit($child, $node);
                    if ($childCost || $hasApple[$child]) $cost += $childCost + 2;
                }
            }
            return $cost;
        };
        return $visit(0, -1);
    }
}
''',
    "1444_number_of_ways_of_cutting_a_pizza": r'''<?php
class Solution {
    function ways($pizza, $k) {
        $mod = 1000000007;
        $rows = count($pizza);
        $cols = strlen($pizza[0]);
        $apples = array_fill(0, $rows + 1, array_fill(0, $cols + 1, 0));
        for ($r = $rows - 1; $r >= 0; $r--) {
            for ($c = $cols - 1; $c >= 0; $c--) {
                $apples[$r][$c] = ($pizza[$r][$c] === "A" ? 1 : 0) + $apples[$r + 1][$c] + $apples[$r][$c + 1] - $apples[$r + 1][$c + 1];
            }
        }
        $dp = [];
        for ($r = 0; $r < $rows; $r++) {
            for ($c = 0; $c < $cols; $c++) $dp[$r][$c] = $apples[$r][$c] ? 1 : 0;
        }
        for ($cut = 1; $cut < $k; $cut++) {
            $nxt = array_fill(0, $rows, array_fill(0, $cols, 0));
            for ($r = 0; $r < $rows; $r++) {
                for ($c = 0; $c < $cols; $c++) {
                    for ($nr = $r + 1; $nr < $rows; $nr++) {
                        if ($apples[$r][$c] > $apples[$nr][$c]) $nxt[$r][$c] += $dp[$nr][$c];
                    }
                    for ($nc = $c + 1; $nc < $cols; $nc++) {
                        if ($apples[$r][$c] > $apples[$r][$nc]) $nxt[$r][$c] += $dp[$r][$nc];
                    }
                    $nxt[$r][$c] %= $mod;
                }
            }
            $dp = $nxt;
        }
        return $dp[0][0];
    }
}
''',
    "1446_consecutive_characters": r'''<?php
class Solution {
    function maxPower($s) {
        $answer = 1;
        $run = 1;
        for ($i = 1; $i < strlen($s); $i++) {
            $run = $s[$i] === $s[$i - 1] ? $run + 1 : 1;
            $answer = max($answer, $run);
        }
        return $answer;
    }
}
''',
    "1447_simplified_fractions": r'''<?php
class Solution {
    function simplifiedFractions($n) {
        $answer = [];
        for ($a = 1; $a < $n; $a++) {
            for ($b = $a + 1; $b <= $n; $b++) {
                if (gmp_intval(gmp_gcd($a, $b)) === 1 || $this->gcd($a, $b) === 1) {
                    // prefer custom gcd for environments without gmp
                }
            }
        }
        for ($a = 1; $a < $n; $a++) {
            for ($b = $a + 1; $b <= $n; $b++) {
                if ($this->gcd($a, $b) === 1) $answer[] = "$a/$b";
            }
        }
        return $answer;
    }
    private function gcd($a, $b) {
        while ($b) {
            $t = $a % $b;
            $a = $b;
            $b = $t;
        }
        return $a;
    }
}
''',
    "1448_count_good_nodes_in_binary_tree": r'''<?php
class Solution {
    function goodNodes($root) {
        $visit = function($node, $maximum) use (&$visit) {
            if (!$node) return 0;
            $good = $node->val >= $maximum ? 1 : 0;
            $maximum = max($maximum, $node->val);
            return $good + $visit($node->left, $maximum) + $visit($node->right, $maximum);
        };
        return $visit($root, PHP_INT_MIN);
    }
}
''',
    "1449_form_largest_integer_with_digits_that_add_up_to_target": r'''<?php
class Solution {
    function largestNumber($cost, $target) {
        $dp = array_fill(0, $target + 1, null);
        $dp[0] = "";
        for ($total = 1; $total <= $target; $total++) {
            $best = null;
            for ($digit = 1; $digit <= 9; $digit++) {
                $price = $cost[$digit - 1];
                if ($total >= $price && $dp[$total - $price] !== null) {
                    $candidate = strval($digit) . $dp[$total - $price];
                    if ($best === null || strlen($candidate) > strlen($best) || (strlen($candidate) === strlen($best) && $candidate > $best)) {
                        $best = $candidate;
                    }
                }
            }
            $dp[$total] = $best;
        }
        return $dp[$target] ?? "0";
    }
}
''',
    "1450_number_of_students_doing_homework_at_a_given_time": r'''<?php
class Solution {
    function busyStudent($startTime, $endTime, $queryTime) {
        $ans = 0;
        foreach ($startTime as $i => $start) {
            if ($start <= $queryTime && $queryTime <= $endTime[$i]) $ans++;
        }
        return $ans;
    }
}
''',
    "1451_rearrange_words_in_a_sentence": r'''<?php
class Solution {
    function arrangeWords($text) {
        $words = explode(" ", strtolower($text));
        usort($words, function($a, $b) {
            $la = strlen($a);
            $lb = strlen($b);
            if ($la !== $lb) return $la <=> $lb;
            return 0;
        });
        $s = implode(" ", $words);
        return $s === "" ? "" : strtoupper($s[0]) . substr($s, 1);
    }
}
''',
    "1452_people_whose_list_of_favorite_companies_is_not_a_subset_of_another_list": r'''<?php
class Solution {
    function peopleIndexes($favoriteCompanies) {
        $sets = [];
        foreach ($favoriteCompanies as $x) $sets[] = array_flip($x);
        $answer = [];
        $n = count($sets);
        for ($i = 0; $i < $n; $i++) {
            $subset = false;
            for ($j = 0; $j < $n; $j++) {
                if ($i === $j) continue;
                $ok = true;
                foreach ($sets[$i] as $c => $_) {
                    if (!isset($sets[$j][$c])) { $ok = false; break; }
                }
                if ($ok) { $subset = true; break; }
            }
            if (!$subset) $answer[] = $i;
        }
        return $answer;
    }
}
''',
    "1453_maximum_number_of_darts_inside_of_a_circular_dartboard": r'''<?php
class Solution {
    function numPoints($darts, $r) {
        $ans = $darts ? 1 : 0;
        $n = count($darts);
        for ($i = 0; $i < $n; $i++) {
            [$x1, $y1] = $darts[$i];
            for ($j = $i + 1; $j < $n; $j++) {
                [$x2, $y2] = $darts[$j];
                $dx = $x2 - $x1;
                $dy = $y2 - $y1;
                $d2 = $dx * $dx + $dy * $dy;
                if ($d2 > 4 * $r * $r || $d2 == 0) continue;
                $d = sqrt($d2);
                $h = sqrt($r * $r - $d2 / 4);
                $mx = ($x1 + $x2) / 2;
                $my = ($y1 + $y2) / 2;
                foreach ([-1, 1] as $sign) {
                    $cx = $mx + $sign * (-$dy) * $h / $d;
                    $cy = $my + $sign * $dx * $h / $d;
                    $count = 0;
                    foreach ($darts as [$x, $y]) {
                        if (($x - $cx) ** 2 + ($y - $cy) ** 2 <= $r * $r + 1e-7) $count++;
                    }
                    $ans = max($ans, $count);
                }
            }
        }
        return $ans;
    }
}
''',
    "1455_check_if_a_word_occurs_as_a_prefix_of_any_word_in_a_sentence": r'''<?php
class Solution {
    function isPrefixOfWord($sentence, $searchWord) {
        foreach (explode(" ", $sentence) as $i => $w) {
            if (strpos($w, $searchWord) === 0) return $i + 1;
        }
        return -1;
    }
}
''',
    "1456_maximum_number_of_vowels_in_a_substring_of_given_length": r'''<?php
class Solution {
    function maxVowels($s, $k) {
        $vowels = ['a'=>1,'e'=>1,'i'=>1,'o'=>1,'u'=>1];
        $cur = 0;
        for ($i = 0; $i < $k; $i++) if (isset($vowels[$s[$i]])) $cur++;
        $ans = $cur;
        for ($i = $k; $i < strlen($s); $i++) {
            if (isset($vowels[$s[$i]])) $cur++;
            if (isset($vowels[$s[$i - $k]])) $cur--;
            $ans = max($ans, $cur);
        }
        return $ans;
    }
}
''',
    "1457_pseudo_palindromic_paths_in_a_binary_tree": r'''<?php
class Solution {
    function pseudoPalindromicPaths($root) {
        $dfs = function($node, $mask) use (&$dfs) {
            if (!$node) return 0;
            $mask ^= 1 << $node->val;
            if (!$node->left && !$node->right) return ($mask & ($mask - 1)) === 0 ? 1 : 0;
            return $dfs($node->left, $mask) + $dfs($node->right, $mask);
        };
        return $dfs($root, 0);
    }
}
''',
    "1458_max_dot_product_of_two_subsequences": r'''<?php
class Solution {
    function maxDotProduct($nums1, $nums2) {
        $n = count($nums2);
        $dp = array_fill(0, $n + 1, PHP_INT_MIN);
        foreach ($nums1 as $a) {
            $prev = $dp;
            for ($j = 1; $j <= $n; $j++) {
                $b = $nums2[$j - 1];
                $product = $a * $b;
                $dp[$j] = max($dp[$j - 1], $prev[$j], $product, $product + max(0, $prev[$j - 1]));
            }
        }
        return $dp[$n];
    }
}
''',
    "1460_make_two_arrays_equal_by_reversing_subarrays": r'''<?php
class Solution {
    function canBeEqual($target, $arr) {
        sort($target);
        sort($arr);
        return $target === $arr;
    }
}
''',
    "1461_check_if_a_string_contains_all_binary_codes_of_size_k": r'''<?php
class Solution {
    function hasAllCodes($s, $k) {
        $seen = [];
        $n = strlen($s);
        for ($i = 0; $i <= $n - $k; $i++) $seen[substr($s, $i, $k)] = true;
        return count($seen) === (1 << $k);
    }
}
''',
    "1462_course_schedule_iv": r'''<?php
class Solution {
    function checkIfPrerequisite($numCourses, $prerequisites, $queries) {
        $reach = array_fill(0, $numCourses, array_fill(0, $numCourses, false));
        foreach ($prerequisites as [$a, $b]) $reach[$a][$b] = true;
        for ($k = 0; $k < $numCourses; $k++) {
            for ($i = 0; $i < $numCourses; $i++) {
                if ($reach[$i][$k]) {
                    for ($j = 0; $j < $numCourses; $j++) {
                        $reach[$i][$j] = $reach[$i][$j] || $reach[$k][$j];
                    }
                }
            }
        }
        $answer = [];
        foreach ($queries as [$a, $b]) $answer[] = $reach[$a][$b];
        return $answer;
    }
}
''',
}


def main() -> None:
    # Fix 1447 to remove dead gmp code
    SOLUTIONS["1447_simplified_fractions"] = r'''<?php
class Solution {
    function simplifiedFractions($n) {
        $answer = [];
        for ($a = 1; $a < $n; $a++) {
            for ($b = $a + 1; $b <= $n; $b++) {
                if ($this->gcd($a, $b) === 1) $answer[] = "$a/$b";
            }
        }
        return $answer;
    }
    private function gcd($a, $b) {
        while ($b) {
            $t = $a % $b;
            $a = $b;
            $b = $t;
        }
        return $a;
    }
}
'''
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

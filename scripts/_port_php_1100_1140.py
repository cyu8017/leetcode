#!/usr/bin/env python3
"""Port stub solution.php files for problems 1100-1140 (non-SQL)."""
from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SOLUTIONS: dict[str, str] = {}


def add(name: str, content: str) -> None:
    SOLUTIONS[name] = content.strip() + "\n"


add(
    "1100_find_k_length_substrings_with_no_repeated_characters",
    r"""<?php
// LeetCode 1100 - Find K-Length Substrings With No Repeated Characters
// https://leetcode.com/problems/find-k-length-substrings-with-no-repeated-characters/

class Solution {
    /**
     * @param String $s
     * @param Integer $k
     * @return Integer
     */
    function numKLenSubstrNoRepeats($s, $k) {
        $n = strlen($s);
        if ($k > $n) return 0;
        $window = [];
        for ($i = 0; $i < $k; $i++) {
            $ch = $s[$i];
            $window[$ch] = ($window[$ch] ?? 0) + 1;
        }
        $ans = count($window) === $k ? 1 : 0;
        for ($i = $k; $i < $n; $i++) {
            $ch = $s[$i];
            $window[$ch] = ($window[$ch] ?? 0) + 1;
            $left = $s[$i - $k];
            $window[$left]--;
            if ($window[$left] === 0) unset($window[$left]);
            if (count($window) === $k) $ans++;
        }
        return $ans;
    }
}
""",
)

add(
    "1101_the_earliest_moment_when_everyone_become_friends",
    r"""<?php
// LeetCode 1101 - The Earliest Moment When Everyone Become Friends
// https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends/

class Solution {
    /**
     * @param Integer[][] $logs
     * @param Integer $n
     * @return Integer
     */
    function earliestAcq($logs, $n) {
        $parent = range(0, $n - 1);
        $find = function ($x) use (&$parent, &$find) {
            while ($parent[$x] !== $x) {
                $parent[$x] = $parent[$parent[$x]];
                $x = $parent[$x];
            }
            return $x;
        };
        usort($logs, fn($a, $b) => $a[0] <=> $b[0]);
        $components = $n;
        foreach ($logs as $log) {
            [$t, $a, $b] = $log;
            $ra = $find($a);
            $rb = $find($b);
            if ($ra === $rb) continue;
            $parent[$rb] = $ra;
            $components--;
            if ($components === 1) return $t;
        }
        return -1;
    }
}
""",
)

add(
    "1102_path_with_maximum_minimum_value",
    r"""<?php
// LeetCode 1102 - Path With Maximum Minimum Value
// https://leetcode.com/problems/path-with-maximum-minimum-value/

class Solution {
    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function maximumMinimumPath($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        $heap = new SplMaxHeap();
        $heap->insert([$grid[0][0], 0, 0]);
        $seen = ['0,0' => true];
        $dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];
        while (!$heap->isEmpty()) {
            [$val, $r, $c] = $heap->extract();
            if ($r === $m - 1 && $c === $n - 1) return $val;
            foreach ($dirs as [$dr, $dc]) {
                $nr = $r + $dr;
                $nc = $c + $dc;
                $key = "$nr,$nc";
                if ($nr >= 0 && $nr < $m && $nc >= 0 && $nc < $n && !isset($seen[$key])) {
                    $seen[$key] = true;
                    $heap->insert([min($val, $grid[$nr][$nc]), $nr, $nc]);
                }
            }
        }
        return $grid[0][0];
    }
}
""",
)

add(
    "1103_distribute_candies_to_people",
    r"""<?php
// LeetCode 1103 - Distribute Candies to People
// https://leetcode.com/problems/distribute-candies-to-people/

class Solution {
    /**
     * @param Integer $candies
     * @param Integer $num_people
     * @return Integer[]
     */
    function distributeCandies($candies, $num_people) {
        $ans = array_fill(0, $num_people, 0);
        $give = 1;
        $i = 0;
        while ($candies > 0) {
            $take = min($give, $candies);
            $ans[$i] += $take;
            $candies -= $take;
            $give++;
            $i = ($i + 1) % $num_people;
        }
        return $ans;
    }
}
""",
)

add(
    "1104_path_in_zigzag_labelled_binary_tree",
    r"""<?php
// LeetCode 1104 - Path In Zigzag Labelled Binary Tree
// https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree/

class Solution {
    /**
     * @param Integer $label
     * @return Integer[]
     */
    function pathInZigZagTree($label) {
        $path = [$label];
        while ($label > 1) {
            $level = (int)floor(log($label, 2));
            $label >>= 1;
            $label = (1 << $level) - 1 - $label + (1 << ($level - 1));
            $path[] = $label;
        }
        return array_reverse($path);
    }
}
""",
)

add(
    "1105_filling_bookcase_shelves",
    r"""<?php
// LeetCode 1105 - Filling Bookcase Shelves
// https://leetcode.com/problems/filling-bookcase-shelves/

class Solution {
    /**
     * @param Integer[][] $books
     * @param Integer $shelfWidth
     * @return Integer
     */
    function minHeightShelves($books, $shelfWidth) {
        $n = count($books);
        $dp = array_fill(0, $n + 1, 0);
        for ($i = 1; $i <= $n; $i++) {
            $width = 0;
            $height = 0;
            $dp[$i] = PHP_INT_MAX;
            for ($j = $i; $j >= 1; $j--) {
                $w = $books[$j - 1][0];
                $h = $books[$j - 1][1];
                $width += $w;
                if ($width > $shelfWidth) break;
                $height = max($height, $h);
                $dp[$i] = min($dp[$i], $dp[$j - 1] + $height);
            }
        }
        return $dp[$n];
    }
}
""",
)

add(
    "1106_parsing_a_boolean_expression",
    r"""<?php
// LeetCode 1106 - Parsing A Boolean Expression
// https://leetcode.com/problems/parsing-a-boolean-expression/

class Solution {
    /**
     * @param String $expression
     * @return Boolean
     */
    function parseBoolExpr($expression) {
        $stack = [];
        $n = strlen($expression);
        for ($i = 0; $i < $n; $i++) {
            $ch = $expression[$i];
            if ($ch === ')') {
                $values = [];
                while (!empty($stack) && !in_array(end($stack), ['&', '|', '!'], true)) {
                    $token = array_pop($stack);
                    if ($token === 't' || $token === 'f') {
                        $values[] = $token === 't';
                    }
                }
                $op = array_pop($stack);
                if ($op === '!') {
                    $stack[] = !$values[0] ? 't' : 'f';
                } elseif ($op === '&') {
                    $stack[] = !in_array(false, $values, true) ? 't' : 'f';
                } else {
                    $stack[] = in_array(true, $values, true) ? 't' : 'f';
                }
            } elseif ($ch !== ',') {
                $stack[] = $ch;
            }
        }
        return end($stack) === 't';
    }
}
""",
)

add(
    "1108_defanging_an_ip_address",
    r"""<?php
// LeetCode 1108 - Defanging an IP Address
// https://leetcode.com/problems/defanging-an-ip-address/

class Solution {
    /**
     * @param String $address
     * @return String
     */
    function defangIPaddr($address) {
        return str_replace('.', '[.]', $address);
    }
}
""",
)

add(
    "1109_corporate_flight_bookings",
    r"""<?php
// LeetCode 1109 - Corporate Flight Bookings
// https://leetcode.com/problems/corporate-flight-bookings/

class Solution {
    /**
     * @param Integer[][] $bookings
     * @param Integer $n
     * @return Integer[]
     */
    function corpFlightBookings($bookings, $n) {
        $diff = array_fill(0, $n + 1, 0);
        foreach ($bookings as [$first, $last, $seats]) {
            $diff[$first - 1] += $seats;
            $diff[$last] -= $seats;
        }
        $ans = [];
        $cur = 0;
        for ($i = 0; $i < $n; $i++) {
            $cur += $diff[$i];
            $ans[] = $cur;
        }
        return $ans;
    }
}
""",
)

add(
    "1110_delete_nodes_and_return_forest",
    r"""<?php
// LeetCode 1110 - Delete Nodes And Return Forest
// https://leetcode.com/problems/delete-nodes-and-return-forest/

class Solution {
    /**
     * @param TreeNode $root
     * @param Integer[] $to_delete
     * @return TreeNode[]
     */
    function delNodes($root, $to_delete) {
        $delete = array_flip($to_delete);
        $forest = [];
        $dfs = function ($node, $isRoot) use (&$dfs, &$delete, &$forest) {
            if ($node === null) return null;
            $removed = isset($delete[$node->val]);
            if ($isRoot && !$removed) $forest[] = $node;
            $node->left = $dfs($node->left, $removed);
            $node->right = $dfs($node->right, $removed);
            return $removed ? null : $node;
        };
        $dfs($root, true);
        return $forest;
    }
}
""",
)

add(
    "1111_maximum_nesting_depth_of_two_valid_parentheses_strings",
    r"""<?php
// LeetCode 1111 - Maximum Nesting Depth of Two Valid Parentheses Strings
// https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/

class Solution {
    /**
     * @param String $seq
     * @return Integer[]
     */
    function maxDepthAfterSplit($seq) {
        $ans = [];
        $depth = 0;
        $n = strlen($seq);
        for ($i = 0; $i < $n; $i++) {
            if ($seq[$i] === '(') {
                $ans[] = $depth % 2;
                $depth++;
            } else {
                $depth--;
                $ans[] = $depth % 2;
            }
        }
        return $ans;
    }
}
""",
)

add(
    "1114_print_in_order",
    r"""<?php
// LeetCode 1114 - Print in Order
// https://leetcode.com/problems/print-in-order/

class Foo {
    private $secondReady = false;
    private $thirdReady = false;

    function first($printFirst) {
        $printFirst();
        $this->secondReady = true;
    }

    function second($printSecond) {
        while (!$this->secondReady) { usleep(100); }
        $printSecond();
        $this->thirdReady = true;
    }

    function third($printThird) {
        while (!$this->thirdReady) { usleep(100); }
        $printThird();
    }
}
""",
)

add(
    "1115_print_foobar_alternately",
    r"""<?php
// LeetCode 1115 - Print FooBar Alternately
// https://leetcode.com/problems/print-foobar-alternately/

class FooBar {
    private $n;
    private $fooTurn = true;

    function __construct($n) {
        $this->n = $n;
    }

    function foo($printFoo) {
        for ($i = 0; $i < $this->n; $i++) {
            while (!$this->fooTurn) { usleep(100); }
            $printFoo();
            $this->fooTurn = false;
        }
    }

    function bar($printBar) {
        for ($i = 0; $i < $this->n; $i++) {
            while ($this->fooTurn) { usleep(100); }
            $printBar();
            $this->fooTurn = true;
        }
    }
}
""",
)

add(
    "1116_print_zero_even_odd",
    r"""<?php
// LeetCode 1116 - Print Zero Even Odd
// https://leetcode.com/problems/print-zero-even-odd/

class ZeroEvenOdd {
    private $n;
    private $state = 0; // 0=zero, 1=odd, 2=even
    private $x = 1;

    function __construct($n) {
        $this->n = $n;
    }

    function zero($printNumber) {
        for ($i = 0; $i < $this->n; $i++) {
            while ($this->state !== 0) { usleep(100); }
            $printNumber(0);
            $this->state = ($this->x % 2 === 1) ? 1 : 2;
        }
    }

    function even($printNumber) {
        for ($i = 2; $i <= $this->n; $i += 2) {
            while ($this->state !== 2) { usleep(100); }
            $printNumber($i);
            $this->x++;
            $this->state = 0;
        }
    }

    function odd($printNumber) {
        for ($i = 1; $i <= $this->n; $i += 2) {
            while ($this->state !== 1) { usleep(100); }
            $printNumber($i);
            $this->x++;
            $this->state = 0;
        }
    }
}
""",
)

add(
    "1117_building_h2o",
    r"""<?php
// LeetCode 1117 - Building H2O
// https://leetcode.com/problems/building-h2o/

class H2O {
    private $h = 0;
    private $o = 0;

    function hydrogen($releaseHydrogen) {
        while (true) {
            if ($this->h < 2) {
                $this->h++;
                $releaseHydrogen();
                $this->maybeReset();
                return;
            }
            usleep(100);
        }
    }

    function oxygen($releaseOxygen) {
        while (true) {
            if ($this->o < 1) {
                $this->o++;
                $releaseOxygen();
                $this->maybeReset();
                return;
            }
            usleep(100);
        }
    }

    private function maybeReset() {
        if ($this->h === 2 && $this->o === 1) {
            $this->h = 0;
            $this->o = 0;
        }
    }
}
""",
)

add(
    "1118_number_of_days_in_a_month",
    r"""<?php
// LeetCode 1118 - Number of Days in a Month
// https://leetcode.com/problems/number-of-days-in-a-month/

class Solution {
    /**
     * @param Integer $year
     * @param Integer $month
     * @return Integer
     */
    function numberOfDays($year, $month) {
        $days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
        if ($month !== 2) return $days[$month];
        $leap = ($year % 4 === 0 && $year % 100 !== 0) || ($year % 400 === 0);
        return $leap ? 29 : 28;
    }
}
""",
)

add(
    "1119_remove_vowels_from_a_string",
    r"""<?php
// LeetCode 1119 - Remove Vowels From a String
// https://leetcode.com/problems/remove-vowels-from-a-string/

class Solution {
    /**
     * @param String $s
     * @return String
     */
    function removeVowels($s) {
        return preg_replace('/[aeiou]/', '', $s);
    }
}
""",
)

add(
    "1120_maximum_average_subtree",
    r"""<?php
// LeetCode 1120 - Maximum Average Subtree
// https://leetcode.com/problems/maximum-average-subtree/

class Solution {
    private $ans = 0.0;

    /**
     * @param TreeNode $root
     * @return Float
     */
    function maximumAverageSubtree($root) {
        $this->ans = 0.0;
        $this->dfs($root);
        return $this->ans;
    }

    private function dfs($node) {
        if ($node === null) return [0, 0];
        [$ls, $lc] = $this->dfs($node->left);
        [$rs, $rc] = $this->dfs($node->right);
        $sum = $ls + $rs + $node->val;
        $cnt = $lc + $rc + 1;
        $this->ans = max($this->ans, $sum / $cnt);
        return [$sum, $cnt];
    }
}
""",
)

add(
    "1121_divide_array_into_increasing_sequences",
    r"""<?php
// LeetCode 1121 - Divide Array Into Increasing Sequences
// https://leetcode.com/problems/divide-array-into-increasing-sequences/

class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Boolean
     */
    function canDivideIntoSubsequences($nums, $k) {
        $n = count($nums);
        $freq = [];
        $maxFreq = 0;
        foreach ($nums as $x) {
            $freq[$x] = ($freq[$x] ?? 0) + 1;
            $maxFreq = max($maxFreq, $freq[$x]);
        }
        return $maxFreq * $k <= $n;
    }
}
""",
)

add(
    "1122_relative_sort_array",
    r"""<?php
// LeetCode 1122 - Relative Sort Array
// https://leetcode.com/problems/relative-sort-array/

class Solution {
    /**
     * @param Integer[] $arr1
     * @param Integer[] $arr2
     * @return Integer[]
     */
    function relativeSortArray($arr1, $arr2) {
        $order = array_flip($arr2);
        usort($arr1, function ($a, $b) use ($order) {
            $ia = $order[$a] ?? PHP_INT_MAX;
            $ib = $order[$b] ?? PHP_INT_MAX;
            if ($ia !== $ib) return $ia <=> $ib;
            return $a <=> $b;
        });
        return $arr1;
    }
}
""",
)

add(
    "1123_lowest_common_ancestor_of_deepest_leaves",
    r"""<?php
// LeetCode 1123 - Lowest Common Ancestor of Deepest Leaves
// https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/

class Solution {
    /**
     * @param TreeNode $root
     * @return TreeNode
     */
    function lcaDeepestLeaves($root) {
        return $this->dfs($root)[0];
    }

    private function dfs($node) {
        if ($node === null) return [null, 0];
        [$lNode, $lDepth] = $this->dfs($node->left);
        [$rNode, $rDepth] = $this->dfs($node->right);
        if ($lDepth > $rDepth) return [$lNode, $lDepth + 1];
        if ($rDepth > $lDepth) return [$rNode, $rDepth + 1];
        return [$node, $lDepth + 1];
    }
}
""",
)

add(
    "1124_longest_well_performing_interval",
    r"""<?php
// LeetCode 1124 - Longest Well-Performing Interval
// https://leetcode.com/problems/longest-well-performing-interval/

class Solution {
    /**
     * @param Integer[] $hours
     * @return Integer
     */
    function longestWPI($hours) {
        $score = 0;
        $ans = 0;
        $seen = [];
        foreach ($hours as $i => $h) {
            $score += $h > 8 ? 1 : -1;
            if ($score > 0) {
                $ans = $i + 1;
            } else {
                if (!isset($seen[$score])) $seen[$score] = $i;
                if (isset($seen[$score - 1])) {
                    $ans = max($ans, $i - $seen[$score - 1]);
                }
            }
        }
        return $ans;
    }
}
""",
)

add(
    "1125_smallest_sufficient_team",
    r"""<?php
// LeetCode 1125 - Smallest Sufficient Team
// https://leetcode.com/problems/smallest-sufficient-team/

class Solution {
    /**
     * @param String[] $req_skills
     * @param String[][] $people
     * @return Integer[]
     */
    function smallestSufficientTeam($req_skills, $people) {
        $n = count($req_skills);
        $skillId = array_flip($req_skills);
        $m = 1 << $n;
        $dp = array_fill(0, $m, null);
        $dp[0] = [];
        foreach ($people as $i => $skills) {
            $mask = 0;
            foreach ($skills as $s) {
                if (isset($skillId[$s])) $mask |= 1 << $skillId[$s];
            }
            if ($mask === 0) continue;
            for ($prev = 0; $prev < $m; $prev++) {
                if ($dp[$prev] === null) continue;
                $comb = $prev | $mask;
                if ($dp[$comb] === null || count($dp[$comb]) > count($dp[$prev]) + 1) {
                    $dp[$comb] = array_merge($dp[$prev], [$i]);
                }
            }
        }
        return $dp[$m - 1];
    }
}
""",
)

add(
    "1128_number_of_equivalent_domino_pairs",
    r"""<?php
// LeetCode 1128 - Number of Equivalent Domino Pairs
// https://leetcode.com/problems/number-of-equivalent-domino-pairs/

class Solution {
    /**
     * @param Integer[][] $dominoes
     * @return Integer
     */
    function numEquivDominoPairs($dominoes) {
        $cnt = [];
        $ans = 0;
        foreach ($dominoes as [$a, $b]) {
            $key = min($a, $b) * 10 + max($a, $b);
            $ans += $cnt[$key] ?? 0;
            $cnt[$key] = ($cnt[$key] ?? 0) + 1;
        }
        return $ans;
    }
}
""",
)

add(
    "1129_shortest_path_with_alternating_colors",
    r"""<?php
// LeetCode 1129 - Shortest Path with Alternating Colors
// https://leetcode.com/problems/shortest-path-with-alternating-colors/

class Solution {
    /**
     * @param Integer $n
     * @param Integer[][] $redEdges
     * @param Integer[][] $blueEdges
     * @return Integer[]
     */
    function shortestAlternatingPaths($n, $redEdges, $blueEdges) {
        $red = array_fill(0, $n, []);
        $blue = array_fill(0, $n, []);
        foreach ($redEdges as [$a, $b]) $red[$a][] = $b;
        foreach ($blueEdges as [$a, $b]) $blue[$a][] = $b;
        $ans = array_fill(0, $n, -1);
        $ans[0] = 0;
        $queue = [[0, 0], [0, 1]]; // node, color (0=red next, 1=blue next) — actually last color used
        $seen = [[true, true]]; // for node 0 both colors
        for ($i = 1; $i < $n; $i++) $seen[$i] = [false, false];
        $seen[0][0] = $seen[0][1] = true;
        $queue = [[0, 0, 0], [0, 1, 0]]; // node, lastColor, dist (0=red,1=blue,-1=none)
        $seen = [];
        $seen['0,0'] = true;
        $seen['0,1'] = true;
        $queue = [[0, -1, 0]];
        $head = 0;
        while ($head < count($queue)) {
            [$node, $lastColor, $dist] = $queue[$head++];
            if ($ans[$node] === -1) $ans[$node] = $dist;
            foreach ([0, 1] as $color) {
                if ($color === $lastColor) continue;
                $edges = $color === 0 ? $red : $blue;
                foreach ($edges[$node] as $nei) {
                    $key = "$nei,$color";
                    if (!isset($seen[$key])) {
                        $seen[$key] = true;
                        $queue[] = [$nei, $color, $dist + 1];
                    }
                }
            }
        }
        return $ans;
    }
}
""",
)

add(
    "1130_minimum_cost_tree_from_leaf_values",
    r"""<?php
// LeetCode 1130 - Minimum Cost Tree From Leaf Values
// https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/

class Solution {
    /**
     * @param Integer[] $arr
     * @return Integer
     */
    function mctFromLeafValues($arr) {
        $stack = [PHP_INT_MAX];
        $ans = 0;
        foreach ($arr as $a) {
            while (end($stack) <= $a) {
                $mid = array_pop($stack);
                $ans += $mid * min(end($stack), $a);
            }
            $stack[] = $a;
        }
        while (count($stack) > 2) {
            $ans += array_pop($stack) * end($stack);
        }
        return $ans;
    }
}
""",
)

add(
    "1131_maximum_of_absolute_value_expression",
    r"""<?php
// LeetCode 1131 - Maximum of Absolute Value Expression
// https://leetcode.com/problems/maximum-of-absolute-value-expression/

class Solution {
    /**
     * @param Integer[] $arr1
     * @param Integer[] $arr2
     * @return Integer
     */
    function maxAbsValExpr($arr1, $arr2) {
        $n = count($arr1);
        $ans = 0;
        $signs = [[1, 1], [1, -1], [-1, 1], [-1, -1]];
        foreach ($signs as [$a, $b]) {
            $mx = PHP_INT_MIN;
            $mn = PHP_INT_MAX;
            for ($i = 0; $i < $n; $i++) {
                $v = $a * $arr1[$i] + $b * $arr2[$i] + $i;
                $mx = max($mx, $v);
                $mn = min($mn, $v);
            }
            $ans = max($ans, $mx - $mn);
        }
        return $ans;
    }
}
""",
)

add(
    "1133_largest_unique_number",
    r"""<?php
// LeetCode 1133 - Largest Unique Number
// https://leetcode.com/problems/largest-unique-number/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function largestUniqueNumber($nums) {
        $cnt = array_count_values($nums);
        $ans = -1;
        foreach ($cnt as $num => $c) {
            if ($c === 1) $ans = max($ans, $num);
        }
        return $ans;
    }
}
""",
)

add(
    "1134_armstrong_number",
    r"""<?php
// LeetCode 1134 - Armstrong Number
// https://leetcode.com/problems/armstrong-number/

class Solution {
    /**
     * @param Integer $n
     * @return Boolean
     */
    function isArmstrong($n) {
        $s = (string)$n;
        $k = strlen($s);
        $sum = 0;
        foreach (str_split($s) as $ch) {
            $sum += ((int)$ch) ** $k;
        }
        return $sum === $n;
    }
}
""",
)

add(
    "1135_connecting_cities_with_minimum_cost",
    r"""<?php
// LeetCode 1135 - Connecting Cities With Minimum Cost
// https://leetcode.com/problems/connecting-cities-with-minimum-cost/

class Solution {
    /**
     * @param Integer $n
     * @param Integer[][] $connections
     * @return Integer
     */
    function minimumCost($n, $connections) {
        usort($connections, fn($a, $b) => $a[2] <=> $b[2]);
        $parent = range(0, $n);
        $find = function ($x) use (&$parent, &$find) {
            if ($parent[$x] !== $x) $parent[$x] = $find($parent[$x]);
            return $parent[$x];
        };
        $cost = 0;
        $edges = 0;
        foreach ($connections as [$a, $b, $c]) {
            $ra = $find($a);
            $rb = $find($b);
            if ($ra === $rb) continue;
            $parent[$ra] = $rb;
            $cost += $c;
            $edges++;
            if ($edges === $n - 1) return $cost;
        }
        return -1;
    }
}
""",
)

add(
    "1136_parallel_courses",
    r"""<?php
// LeetCode 1136 - Parallel Courses
// https://leetcode.com/problems/parallel-courses/

class Solution {
    /**
     * @param Integer $n
     * @param Integer[][] $relations
     * @return Integer
     */
    function minimumSemesters($n, $relations) {
        $graph = array_fill(0, $n + 1, []);
        $indeg = array_fill(0, $n + 1, 0);
        foreach ($relations as [$a, $b]) {
            $graph[$a][] = $b;
            $indeg[$b]++;
        }
        $queue = [];
        for ($i = 1; $i <= $n; $i++) {
            if ($indeg[$i] === 0) $queue[] = $i;
        }
        $sem = 0;
        $taken = 0;
        $head = 0;
        while ($head < count($queue)) {
            $sz = count($queue) - $head;
            $sem++;
            for ($i = 0; $i < $sz; $i++) {
                $node = $queue[$head++];
                $taken++;
                foreach ($graph[$node] as $nei) {
                    if (--$indeg[$nei] === 0) $queue[] = $nei;
                }
            }
        }
        return $taken === $n ? $sem : -1;
    }
}
""",
)

add(
    "1137_n_th_tribonacci_number",
    r"""<?php
// LeetCode 1137 - N-th Tribonacci Number
// https://leetcode.com/problems/n-th-tribonacci-number/

class Solution {
    /**
     * @param Integer $n
     * @return Integer
     */
    function tribonacci($n) {
        if ($n === 0) return 0;
        if ($n <= 2) return 1;
        $a = 0; $b = 1; $c = 1;
        for ($i = 3; $i <= $n; $i++) {
            $d = $a + $b + $c;
            $a = $b; $b = $c; $c = $d;
        }
        return $c;
    }
}
""",
)

add(
    "1138_alphabet_board_path",
    r"""<?php
// LeetCode 1138 - Alphabet Board Path
// https://leetcode.com/problems/alphabet-board-path/

class Solution {
    /**
     * @param String $target
     * @return String
     */
    function alphabetBoardPath($target) {
        $r = 0; $c = 0;
        $ans = '';
        $n = strlen($target);
        for ($i = 0; $i < $n; $i++) {
            $ch = $target[$i];
            $nr = ord($ch) - ord('a');
            $nc = $nr % 5;
            $nr = intdiv($nr, 5);
            if ($c > $nc) $ans .= str_repeat('L', $c - $nc);
            if ($r > $nr) $ans .= str_repeat('U', $r - $nr);
            if ($c < $nc) $ans .= str_repeat('R', $nc - $c);
            if ($r < $nr) $ans .= str_repeat('D', $nr - $r);
            $ans .= '!';
            $r = $nr; $c = $nc;
        }
        return $ans;
    }
}
""",
)

add(
    "1139_largest_1_bordered_square",
    r"""<?php
// LeetCode 1139 - Largest 1-Bordered Square
// https://leetcode.com/problems/largest-1-bordered-square/

class Solution {
    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function largest1BorderedSquare($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        $hor = array_fill(0, $m, array_fill(0, $n, 0));
        $ver = array_fill(0, $m, array_fill(0, $n, 0));
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if ($grid[$i][$j] === 0) continue;
                $hor[$i][$j] = ($j > 0 ? $hor[$i][$j - 1] : 0) + 1;
                $ver[$i][$j] = ($i > 0 ? $ver[$i - 1][$j] : 0) + 1;
            }
        }
        for ($len = min($m, $n); $len >= 1; $len--) {
            for ($i = $len - 1; $i < $m; $i++) {
                for ($j = $len - 1; $j < $n; $j++) {
                    if ($hor[$i][$j] >= $len && $ver[$i][$j] >= $len
                        && $hor[$i - $len + 1][$j] >= $len
                        && $ver[$i][$j - $len + 1] >= $len) {
                        return $len * $len;
                    }
                }
            }
        }
        return 0;
    }
}
""",
)

add(
    "1140_stone_game_ii",
    r"""<?php
// LeetCode 1140 - Stone Game II
// https://leetcode.com/problems/stone-game-ii/

class Solution {
    /**
     * @param Integer[] $piles
     * @return Integer
     */
    function stoneGameII($piles) {
        $n = count($piles);
        $suffix = array_fill(0, $n + 1, 0);
        for ($i = $n - 1; $i >= 0; $i--) {
            $suffix[$i] = $suffix[$i + 1] + $piles[$i];
        }
        $memo = [];
        $dp = function ($i, $m) use (&$dp, &$memo, $n, $suffix) {
            if ($i >= $n) return 0;
            $key = "$i,$m";
            if (isset($memo[$key])) return $memo[$key];
            if ($i + 2 * $m >= $n) return $memo[$key] = $suffix[$i];
            $best = 0;
            for ($x = 1; $x <= 2 * $m; $x++) {
                $best = max($best, $suffix[$i] - $dp($i + $x, max($m, $x)));
            }
            return $memo[$key] = $best;
        };
        return $dp(0, 1);
    }
}
""",
)


def is_stub(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    return "function solve()" in text or "function solve() {" in text


def main() -> None:
    ported = 0
    for folder, content in SOLUTIONS.items():
        path = ROOT / folder / "solution.php"
        if not path.exists():
            print(f"MISSING {folder}")
            continue
        if not is_stub(path):
            print(f"skip done {folder}")
            continue
        path.write_text(content, encoding="utf-8", newline="\n")
        ported += 1
        print(f"ported {folder}")
    print(f"ported={ported} total_in_script={len(SOLUTIONS)}")


if __name__ == "__main__":
    main()

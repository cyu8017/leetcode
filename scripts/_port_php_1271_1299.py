#!/usr/bin/env python3
"""Port stub solution.php files for problems 1271-1299 (non-SQL)."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOLUTIONS: dict[str, str] = {}


def add(name: str, content: str) -> None:
    SOLUTIONS[name] = content.strip() + "\n"


add("1271_hexspeak", r"""<?php
// LeetCode 1271 - Hexspeak
// https://leetcode.com/problems/hexspeak/

class Solution {
    /**
     * @param String $num
     * @return String
     */
    function toHexspeak($num) {
        $value = (int)$num;
        $digits = '0123456789ABCDEF';
        $out = '';
        while ($value) {
            $rem = $value % 16;
            $value = intdiv($value, 16);
            if ($rem >= 2 && $rem <= 9) return 'ERROR';
            $out = $digits[$rem] . $out;
        }
        if ($out === '') $out = '0';
        return str_replace(['0', '1'], ['O', 'I'], $out);
    }
}
""")

add("1272_remove_interval", r"""<?php
// LeetCode 1272 - Remove Interval
// https://leetcode.com/problems/remove-interval/

class Solution {
    /**
     * @param Integer[][] $intervals
     * @param Integer[] $toBeRemoved
     * @return Integer[][]
     */
    function removeInterval($intervals, $toBeRemoved) {
        [$left, $right] = $toBeRemoved;
        $answer = [];
        foreach ($intervals as [$start, $end]) {
            if ($end <= $left || $start >= $right) {
                $answer[] = [$start, $end];
            } else {
                if ($start < $left) $answer[] = [$start, $left];
                if ($end > $right) $answer[] = [$right, $end];
            }
        }
        return $answer;
    }
}
""")

add("1273_delete_tree_nodes", r"""<?php
// LeetCode 1273 - Delete Tree Nodes
// https://leetcode.com/problems/delete-tree-nodes/

class Solution {
    /**
     * @param Integer $nodes
     * @param Integer[] $parent
     * @param Integer[] $value
     * @return Integer
     */
    function deleteTreeNodes($nodes, $parent, $value) {
        $children = array_fill(0, $nodes, []);
        for ($node = 1; $node < $nodes; $node++) {
            $children[$parent[$node]][] = $node;
        }
        $dfs = function ($node) use (&$dfs, $children, $value) {
            $total = $value[$node];
            $count = 1;
            foreach ($children[$node] as $child) {
                [$childSum, $childCount] = $dfs($child);
                $total += $childSum;
                $count += $childCount;
            }
            return [$total, $total === 0 ? 0 : $count];
        };
        return $dfs(0)[1];
    }
}
""")

add("1274_number_of_ships_in_a_rectangle", r"""<?php
// LeetCode 1274 - Number of Ships in a Rectangle
// https://leetcode.com/problems/number-of-ships-in-a-rectangle/

class Solution {
    /**
     * @param Sea $sea
     * @param Integer[] $topRight
     * @param Integer[] $bottomLeft
     * @return Integer
     */
    function countShips($sea, $topRight, $bottomLeft) {
        [$tx, $ty] = $topRight;
        [$bx, $by] = $bottomLeft;
        if ($tx < $bx || $ty < $by || !$sea->hasShips($topRight, $bottomLeft)) return 0;
        if ($tx === $bx && $ty === $by) return 1;
        $mx = intdiv($tx + $bx, 2);
        $my = intdiv($ty + $by, 2);
        return $this->countShips($sea, [$mx, $my], [$bx, $by])
            + $this->countShips($sea, [$tx, $my], [$mx + 1, $by])
            + $this->countShips($sea, [$mx, $ty], [$bx, $my + 1])
            + $this->countShips($sea, [$tx, $ty], [$mx + 1, $my + 1]);
    }
}
""")

add("1275_find_winner_on_a_tic_tac_toe_game", r"""<?php
// LeetCode 1275 - Find Winner on a Tic Tac Toe Game
// https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/

class Solution {
    /**
     * @param Integer[][] $moves
     * @return String
     */
    function tictactoe($moves) {
        $board = array_fill(0, 3, array_fill(0, 3, 0));
        foreach ($moves as $i => [$r, $c]) {
            $board[$r][$c] = $i % 2 === 0 ? 1 : -1;
        }
        $lines = $board;
        for ($c = 0; $c < 3; $c++) {
            $lines[] = [$board[0][$c], $board[1][$c], $board[2][$c]];
        }
        $lines[] = [$board[0][0], $board[1][1], $board[2][2]];
        $lines[] = [$board[0][2], $board[1][1], $board[2][0]];
        foreach ($lines as $line) {
            $s = array_sum($line);
            if (abs($s) === 3) return $s === 3 ? 'A' : 'B';
        }
        return count($moves) === 9 ? 'Draw' : 'Pending';
    }
}
""")

add("1276_number_of_burgers_with_no_waste_of_ingredients", r"""<?php
// LeetCode 1276 - Number of Burgers with No Waste of Ingredients
// https://leetcode.com/problems/number-of-burgers-with-no-waste-of-ingredients/

class Solution {
    /**
     * @param Integer $tomatoSlices
     * @param Integer $cheeseSlices
     * @return Integer[]
     */
    function numOfBurgers($tomatoSlices, $cheeseSlices) {
        if ($tomatoSlices % 2 !== 0) return [];
        $jumbo = intdiv($tomatoSlices, 2) - $cheeseSlices;
        $small = $cheeseSlices - $jumbo;
        return ($jumbo >= 0 && $small >= 0) ? [$jumbo, $small] : [];
    }
}
""")

add("1277_count_square_submatrices_with_all_ones", r"""<?php
// LeetCode 1277 - Count Square Submatrices with All Ones
// https://leetcode.com/problems/count-square-submatrices-with-all-ones/

class Solution {
    /**
     * @param Integer[][] $matrix
     * @return Integer
     */
    function countSquares($matrix) {
        $answer = 0;
        $m = count($matrix);
        $n = count($matrix[0]);
        for ($r = 0; $r < $m; $r++) {
            for ($c = 0; $c < $n; $c++) {
                if ($matrix[$r][$c] && $r && $c) {
                    $matrix[$r][$c] += min($matrix[$r - 1][$c], $matrix[$r][$c - 1], $matrix[$r - 1][$c - 1]);
                }
                $answer += $matrix[$r][$c];
            }
        }
        return $answer;
    }
}
""")

add("1278_palindrome_partitioning_iii", r"""<?php
// LeetCode 1278 - Palindrome Partitioning III
// https://leetcode.com/problems/palindrome-partitioning-iii/

class Solution {
    /**
     * @param String $s
     * @param Integer $k
     * @return Integer
     */
    function palindromePartition($s, $k) {
        $n = strlen($s);
        $cost = array_fill(0, $n, array_fill(0, $n, 0));
        for ($length = 2; $length <= $n; $length++) {
            for ($i = 0; $i <= $n - $length; $i++) {
                $j = $i + $length - 1;
                $cost[$i][$j] = ($length > 2 ? $cost[$i + 1][$j - 1] : 0) + ($s[$i] !== $s[$j] ? 1 : 0);
            }
        }
        $inf = $n + 1;
        $dp = array_fill(0, $k + 1, array_fill(0, $n + 1, $inf));
        $dp[0][0] = 0;
        for ($parts = 1; $parts <= $k; $parts++) {
            for ($end = $parts; $end <= $n; $end++) {
                for ($start = $parts - 1; $start < $end; $start++) {
                    $dp[$parts][$end] = min($dp[$parts][$end], $dp[$parts - 1][$start] + $cost[$start][$end - 1]);
                }
            }
        }
        return $dp[$k][$n];
    }
}
""")

add("1279_traffic_light_controlled_intersection", r"""<?php
// LeetCode 1279 - Traffic Light Controlled Intersection
// https://leetcode.com/problems/traffic-light-controlled-intersection/

class TrafficLight {
    private $greenRoad = 1;

    function __construct() {}

    /**
     * @param Integer $carId
     * @param Integer $roadId
     * @param Integer $direction
     * @param Callable $turnGreen
     * @param Callable $crossCar
     * @return NULL
     */
    function carArrived($carId, $roadId, $direction, $turnGreen, $crossCar) {
        if ($roadId !== $this->greenRoad) {
            $turnGreen();
            $this->greenRoad = $roadId;
        }
        $crossCar();
    }
}
""")

add("1281_subtract_the_product_and_sum_of_digits_of_an_integer", r"""<?php
// LeetCode 1281 - Subtract the Product and Sum of Digits of an Integer
// https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

class Solution {
    /**
     * @param Integer $n
     * @return Integer
     */
    function subtractProductAndSum($n) {
        $product = 1;
        $total = 0;
        while ($n) {
            $digit = $n % 10;
            $n = intdiv($n, 10);
            $product *= $digit;
            $total += $digit;
        }
        return $product - $total;
    }
}
""")

add("1282_group_the_people_given_the_group_size_they_belong_to", r"""<?php
// LeetCode 1282 - Group the People Given the Group Size They Belong To
// https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/

class Solution {
    /**
     * @param Integer[] $groupSizes
     * @return Integer[][]
     */
    function groupThePeople($groupSizes) {
        $pending = [];
        $answer = [];
        foreach ($groupSizes as $person => $size) {
            $pending[$size][] = $person;
            if (count($pending[$size]) === $size) {
                $answer[] = $pending[$size];
                $pending[$size] = [];
            }
        }
        usort($answer, function ($a, $b) {
            $cmp = count($a) <=> count($b);
            return $cmp !== 0 ? $cmp : $a <=> $b;
        });
        return $answer;
    }
}
""")

add("1283_find_the_smallest_divisor_given_a_threshold", r"""<?php
// LeetCode 1283 - Find the Smallest Divisor Given a Threshold
// https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/

class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $threshold
     * @return Integer
     */
    function smallestDivisor($nums, $threshold) {
        $lo = 1;
        $hi = max($nums);
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi, 2);
            $sum = 0;
            foreach ($nums as $x) $sum += intdiv($x + $mid - 1, $mid);
            if ($sum <= $threshold) $hi = $mid;
            else $lo = $mid + 1;
        }
        return $lo;
    }
}
""")

add("1284_minimum_number_of_flips_to_convert_binary_matrix_to_zero_matrix", r"""<?php
// LeetCode 1284 - Minimum Number of Flips to Convert Binary Matrix to Zero Matrix
// https://leetcode.com/problems/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/

class Solution {
    /**
     * @param Integer[][] $mat
     * @return Integer
     */
    function minFlips($mat) {
        $m = count($mat);
        $n = count($mat[0]);
        $start = 0;
        for ($r = 0; $r < $m; $r++) {
            for ($c = 0; $c < $n; $c++) {
                $start |= $mat[$r][$c] << ($r * $n + $c);
            }
        }
        $masks = [];
        for ($r = 0; $r < $m; $r++) {
            for ($c = 0; $c < $n; $c++) {
                $mask = 0;
                foreach ([[0,0],[1,0],[-1,0],[0,1],[0,-1]] as [$dr, $dc]) {
                    $nr = $r + $dr; $nc = $c + $dc;
                    if ($nr >= 0 && $nr < $m && $nc >= 0 && $nc < $n) {
                        $mask ^= 1 << ($nr * $n + $nc);
                    }
                }
                $masks[] = $mask;
            }
        }
        $queue = [[$start, 0]];
        $seen = [$start => true];
        $head = 0;
        while ($head < count($queue)) {
            [$state, $distance] = $queue[$head++];
            if ($state === 0) return $distance;
            foreach ($masks as $mask) {
                $nxt = $state ^ $mask;
                if (!isset($seen[$nxt])) {
                    $seen[$nxt] = true;
                    $queue[] = [$nxt, $distance + 1];
                }
            }
        }
        return -1;
    }
}
""")

add("1286_iterator_for_combination", r"""<?php
// LeetCode 1286 - Iterator for Combination
// https://leetcode.com/problems/iterator-for-combination/

class CombinationIterator {
    private $items = [];
    private $index = 0;

    /**
     * @param String $characters
     * @param Integer $combinationLength
     */
    function __construct($characters, $combinationLength) {
        $chars = str_split($characters);
        $n = count($chars);
        $dfs = function ($start, $path) use (&$dfs, $chars, $n, $combinationLength) {
            if (count($path) === $combinationLength) {
                $this->items[] = implode('', $path);
                return;
            }
            for ($i = $start; $i < $n; $i++) {
                $path[] = $chars[$i];
                $dfs($i + 1, $path);
                array_pop($path);
            }
        };
        $dfs(0, []);
    }

    /**
     * @return String
     */
    function next() {
        return $this->items[$this->index++];
    }

    /**
     * @return Boolean
     */
    function hasNext() {
        return $this->index < count($this->items);
    }
}
""")

add("1287_element_appearing_more_than_25_in_sorted_array", r"""<?php
// LeetCode 1287 - Element Appearing More Than 25% In Sorted Array
// https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/

class Solution {
    /**
     * @param Integer[] $arr
     * @return Integer
     */
    function findSpecialInteger($arr) {
        $n = count($arr);
        foreach ([intdiv($n, 4), intdiv($n, 2), intdiv(3 * $n, 4)] as $idx) {
            $value = $arr[$idx];
            $count = 0;
            foreach ($arr as $x) if ($x === $value) $count++;
            if ($count > intdiv($n, 4)) return $value;
        }
        return $arr[0];
    }
}
""")

add("1288_remove_covered_intervals", r"""<?php
// LeetCode 1288 - Remove Covered Intervals
// https://leetcode.com/problems/remove-covered-intervals/

class Solution {
    /**
     * @param Integer[][] $intervals
     * @return Integer
     */
    function removeCoveredIntervals($intervals) {
        usort($intervals, function ($a, $b) {
            if ($a[0] === $b[0]) return $b[1] <=> $a[1];
            return $a[0] <=> $b[0];
        });
        $answer = 0;
        $farthest = -1;
        foreach ($intervals as [, $end]) {
            if ($end > $farthest) {
                $answer++;
                $farthest = $end;
            }
        }
        return $answer;
    }
}
""")

add("1289_minimum_falling_path_sum_ii", r"""<?php
// LeetCode 1289 - Minimum Falling Path Sum II
// https://leetcode.com/problems/minimum-falling-path-sum-ii/

class Solution {
    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function minFallingPathSum($grid) {
        $dp = $grid[0];
        $m = count($grid);
        $n = count($dp);
        for ($r = 1; $r < $m; $r++) {
            $first = 0;
            for ($i = 1; $i < $n; $i++) if ($dp[$i] < $dp[$first]) $first = $i;
            $secondValue = PHP_INT_MAX;
            for ($i = 0; $i < $n; $i++) {
                if ($i !== $first) $secondValue = min($secondValue, $dp[$i]);
            }
            if ($n === 1) $secondValue = 0;
            $nxt = [];
            for ($i = 0; $i < $n; $i++) {
                $nxt[$i] = $grid[$r][$i] + ($i === $first ? $secondValue : $dp[$first]);
            }
            $dp = $nxt;
        }
        return min($dp);
    }
}
""")

add("1290_convert_binary_number_in_a_linked_list_to_integer", r"""<?php
// LeetCode 1290 - Convert Binary Number in a Linked List to Integer
// https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/

class Solution {
    /**
     * @param ListNode $head
     * @return Integer
     */
    function getDecimalValue($head) {
        $value = 0;
        while ($head !== null) {
            $value = $value * 2 + $head->val;
            $head = $head->next;
        }
        return $value;
    }
}
""")

add("1291_sequential_digits", r"""<?php
// LeetCode 1291 - Sequential Digits
// https://leetcode.com/problems/sequential-digits/

class Solution {
    /**
     * @param Integer $low
     * @param Integer $high
     * @return Integer[]
     */
    function sequentialDigits($low, $high) {
        $digits = '123456789';
        $answer = [];
        for ($length = 2; $length <= 9; $length++) {
            for ($start = 0; $start <= 9 - $length; $start++) {
                $value = (int)substr($digits, $start, $length);
                if ($value >= $low && $value <= $high) $answer[] = $value;
            }
        }
        return $answer;
    }
}
""")

add("1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold", r"""<?php
// LeetCode 1292 - Maximum Side Length of a Square with Sum Less than or Equal to Threshold
// https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/

class Solution {
    /**
     * @param Integer[][] $mat
     * @param Integer $threshold
     * @return Integer
     */
    function maxSideLength($mat, $threshold) {
        $m = count($mat);
        $n = count($mat[0]);
        $prefix = array_fill(0, $m + 1, array_fill(0, $n + 1, 0));
        for ($r = 0; $r < $m; $r++) {
            for ($c = 0; $c < $n; $c++) {
                $prefix[$r + 1][$c + 1] = $mat[$r][$c] + $prefix[$r][$c + 1] + $prefix[$r + 1][$c] - $prefix[$r][$c];
            }
        }
        $possible = function ($size) use ($prefix, $m, $n, $threshold) {
            for ($r = $size; $r <= $m; $r++) {
                for ($c = $size; $c <= $n; $c++) {
                    $sum = $prefix[$r][$c] - $prefix[$r - $size][$c] - $prefix[$r][$c - $size] + $prefix[$r - $size][$c - $size];
                    if ($sum <= $threshold) return true;
                }
            }
            return false;
        };
        $lo = 0;
        $hi = min($m, $n);
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi + 1, 2);
            if ($possible($mid)) $lo = $mid;
            else $hi = $mid - 1;
        }
        return $lo;
    }
}
""")

add("1293_shortest_path_in_a_grid_with_obstacles_elimination", r"""<?php
// LeetCode 1293 - Shortest Path in a Grid with Obstacles Elimination
// https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/

class Solution {
    /**
     * @param Integer[][] $grid
     * @param Integer $k
     * @return Integer
     */
    function shortestPath($grid, $k) {
        $m = count($grid);
        $n = count($grid[0]);
        if ($k >= $m + $n - 2) return $m + $n - 2;
        $queue = [[0, 0, $k, 0]];
        $best = ['0,0' => $k];
        $head = 0;
        while ($head < count($queue)) {
            [$r, $c, $remaining, $distance] = $queue[$head++];
            if ($r === $m - 1 && $c === $n - 1) return $distance;
            foreach ([[1,0],[-1,0],[0,1],[0,-1]] as [$dr, $dc]) {
                $nr = $r + $dr; $nc = $c + $dc;
                if ($nr >= 0 && $nr < $m && $nc >= 0 && $nc < $n) {
                    $nxt = $remaining - $grid[$nr][$nc];
                    $key = "$nr,$nc";
                    if ($nxt >= 0 && $nxt > ($best[$key] ?? -1)) {
                        $best[$key] = $nxt;
                        $queue[] = [$nr, $nc, $nxt, $distance + 1];
                    }
                }
            }
        }
        return -1;
    }
}
""")

add("1295_find_numbers_with_even_number_of_digits", r"""<?php
// LeetCode 1295 - Find Numbers with Even Number of Digits
// https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function findNumbers($nums) {
        $ans = 0;
        foreach ($nums as $value) {
            if (strlen((string)$value) % 2 === 0) $ans++;
        }
        return $ans;
    }
}
""")

add("1296_divide_array_in_sets_of_k_consecutive_numbers", r"""<?php
// LeetCode 1296 - Divide Array in Sets of K Consecutive Numbers
// https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/

class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Boolean
     */
    function isPossibleDivide($nums, $k) {
        if (count($nums) % $k !== 0) return false;
        $counts = array_count_values($nums);
        ksort($counts);
        foreach ($counts as $start => $amount) {
            if ($amount === 0) continue;
            for ($value = $start; $value < $start + $k; $value++) {
                if (($counts[$value] ?? 0) < $amount) return false;
                $counts[$value] -= $amount;
            }
        }
        return true;
    }
}
""")

add("1297_maximum_number_of_occurrences_of_a_substring", r"""<?php
// LeetCode 1297 - Maximum Number of Occurrences of a Substring
// https://leetcode.com/problems/maximum-number-of-occurrences-of-a-substring/

class Solution {
    /**
     * @param String $s
     * @param Integer $maxLetters
     * @param Integer $minSize
     * @param Integer $maxSize
     * @return Integer
     */
    function maxFreq($s, $maxLetters, $minSize, $maxSize) {
        $counts = [];
        $n = strlen($s);
        for ($i = 0; $i <= $n - $minSize; $i++) {
            $sub = substr($s, $i, $minSize);
            if (count(array_unique(str_split($sub))) <= $maxLetters) {
                $counts[$sub] = ($counts[$sub] ?? 0) + 1;
            }
        }
        return empty($counts) ? 0 : max($counts);
    }
}
""")

add("1298_maximum_candies_you_can_get_from_boxes", r"""<?php
// LeetCode 1298 - Maximum Candies You Can Get from Boxes
// https://leetcode.com/problems/maximum-candies-you-can-get-from-boxes/

class Solution {
    /**
     * @param Integer[] $status
     * @param Integer[] $candies
     * @param Integer[][] $keys
     * @param Integer[][] $containedBoxes
     * @param Integer[] $initialBoxes
     * @return Integer
     */
    function maxCandies($status, $candies, $keys, $containedBoxes, $initialBoxes) {
        $owned = [];
        foreach ($initialBoxes as $box) $owned[$box] = true;
        $opened = [];
        $queue = [];
        foreach ($initialBoxes as $box) {
            if ($status[$box]) $queue[] = $box;
        }
        $total = 0;
        $head = 0;
        while ($head < count($queue)) {
            $box = $queue[$head++];
            if (isset($opened[$box]) || !$status[$box]) continue;
            $opened[$box] = true;
            $total += $candies[$box];
            foreach ($keys[$box] as $key) {
                $status[$key] = 1;
                if (isset($owned[$key]) && !isset($opened[$key])) $queue[] = $key;
            }
            foreach ($containedBoxes[$box] as $child) {
                $owned[$child] = true;
                if ($status[$child] && !isset($opened[$child])) $queue[] = $child;
            }
        }
        return $total;
    }
}
""")

add("1299_replace_elements_with_greatest_element_on_right_side", r"""<?php
// LeetCode 1299 - Replace Elements with Greatest Element on Right Side
// https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

class Solution {
    /**
     * @param Integer[] $arr
     * @return Integer[]
     */
    function replaceElements($arr) {
        $greatest = -1;
        for ($i = count($arr) - 1; $i >= 0; $i--) {
            $cur = $arr[$i];
            $arr[$i] = $greatest;
            $greatest = max($greatest, $cur);
        }
        return $arr;
    }
}
""")


def is_stub(path: Path) -> bool:
    return "function solve()" in path.read_text(encoding="utf-8")


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
    print(f"ported={ported} total={len(SOLUTIONS)}")


if __name__ == "__main__":
    main()

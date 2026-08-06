#!/usr/bin/env python3
"""Port stub solution.php files for problems 1203-1226 (non-SQL)."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOLUTIONS: dict[str, str] = {}


def add(name: str, content: str) -> None:
    SOLUTIONS[name] = content.strip() + "\n"


add("1203_sort_items_by_groups_respecting_dependencies", r"""<?php
// LeetCode 1203 - Sort Items by Groups Respecting Dependencies
// https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/

class Solution {
    /**
     * @param Integer $n
     * @param Integer $m
     * @param Integer[] $group
     * @param Integer[][] $beforeItems
     * @return Integer[]
     */
    function sortItems($n, $m, $group, $beforeItems) {
        for ($i = 0; $i < $n; $i++) {
            if ($group[$i] === -1) {
                $group[$i] = $m;
                $m++;
            }
        }
        $itemGraph = array_fill(0, $n, []);
        $itemIndeg = array_fill(0, $n, 0);
        $groupGraph = array_fill(0, $m, []);
        $groupIndeg = array_fill(0, $m, 0);
        $groupSeen = array_fill(0, $m, []);
        for ($v = 0; $v < $n; $v++) {
            foreach ($beforeItems[$v] as $u) {
                $itemGraph[$u][] = $v;
                $itemIndeg[$v]++;
                if ($group[$u] !== $group[$v] && !isset($groupSeen[$group[$u]][$group[$v]])) {
                    $groupSeen[$group[$u]][$group[$v]] = true;
                    $groupGraph[$group[$u]][] = $group[$v];
                    $groupIndeg[$group[$v]]++;
                }
            }
        }
        $topo = function ($graph, $indeg) {
            $queue = [];
            foreach ($indeg as $i => $d) if ($d === 0) $queue[] = $i;
            $order = [];
            $head = 0;
            while ($head < count($queue)) {
                $u = $queue[$head++];
                $order[] = $u;
                foreach ($graph[$u] as $v) {
                    if (--$indeg[$v] === 0) $queue[] = $v;
                }
            }
            return count($order) === count($graph) ? $order : [];
        };
        $items = $topo($itemGraph, $itemIndeg);
        $groups = $topo($groupGraph, $groupIndeg);
        if (empty($items) || empty($groups)) return [];
        $buckets = array_fill(0, $m, []);
        foreach ($items as $item) $buckets[$group[$item]][] = $item;
        $ans = [];
        foreach ($groups as $g) foreach ($buckets[$g] as $item) $ans[] = $item;
        return $ans;
    }
}
""")

add("1206_design_skiplist", r"""<?php
// LeetCode 1206 - Design Skiplist
// https://leetcode.com/problems/design-skiplist/

class Skiplist {
    private $values = [];

    function __construct() {}

    /**
     * @param Integer $target
     * @return Boolean
     */
    function search($target) {
        $i = $this->bisectLeft($target);
        return $i < count($this->values) && $this->values[$i] === $target;
    }

    /**
     * @param Integer $num
     * @return NULL
     */
    function add($num) {
        $i = $this->bisectLeft($num);
        array_splice($this->values, $i, 0, [$num]);
    }

    /**
     * @param Integer $num
     * @return Boolean
     */
    function erase($num) {
        $i = $this->bisectLeft($num);
        if ($i === count($this->values) || $this->values[$i] !== $num) return false;
        array_splice($this->values, $i, 1);
        return true;
    }

    private function bisectLeft($target) {
        $lo = 0; $hi = count($this->values);
        while ($lo < $hi) {
            $mid = ($lo + $hi) >> 1;
            if ($this->values[$mid] < $target) $lo = $mid + 1;
            else $hi = $mid;
        }
        return $lo;
    }
}
""")

add("1207_unique_number_of_occurrences", r"""<?php
// LeetCode 1207 - Unique Number of Occurrences
// https://leetcode.com/problems/unique-number-of-occurrences/

class Solution {
    /**
     * @param Integer[] $arr
     * @return Boolean
     */
    function uniqueOccurrences($arr) {
        $counts = array_count_values($arr);
        return count($counts) === count(array_unique($counts));
    }
}
""")

add("1208_get_equal_substrings_within_budget", r"""<?php
// LeetCode 1208 - Get Equal Substrings Within Budget
// https://leetcode.com/problems/get-equal-substrings-within-budget/

class Solution {
    /**
     * @param String $s
     * @param String $t
     * @param Integer $maxCost
     * @return Integer
     */
    function equalSubstring($s, $t, $maxCost) {
        $left = $cost = $answer = 0;
        $n = strlen($s);
        for ($right = 0; $right < $n; $right++) {
            $cost += abs(ord($s[$right]) - ord($t[$right]));
            while ($cost > $maxCost) {
                $cost -= abs(ord($s[$left]) - ord($t[$left]));
                $left++;
            }
            $answer = max($answer, $right - $left + 1);
        }
        return $answer;
    }
}
""")

add("1209_remove_all_adjacent_duplicates_in_string_ii", r"""<?php
// LeetCode 1209 - Remove All Adjacent Duplicates in String II
// https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/

class Solution {
    /**
     * @param String $s
     * @param Integer $k
     * @return String
     */
    function removeDuplicates($s, $k) {
        $stack = [];
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $ch = $s[$i];
            if (!empty($stack) && end($stack)[0] === $ch) {
                $stack[count($stack) - 1][1]++;
            } else {
                $stack[] = [$ch, 1];
            }
            if (end($stack)[1] === $k) array_pop($stack);
        }
        $ans = '';
        foreach ($stack as [$ch, $count]) $ans .= str_repeat($ch, $count);
        return $ans;
    }
}
""")

add("1210_minimum_moves_to_reach_target_with_rotations", r"""<?php
// LeetCode 1210 - Minimum Moves to Reach Target with Rotations
// https://leetcode.com/problems/minimum-moves-to-reach-target-with-rotations/

class Solution {
    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function minimumMoves($grid) {
        $n = count($grid);
        $start = '0,0,0';
        $target = ($n - 1) . ',' . ($n - 2) . ',0';
        $queue = [[0, 0, 0, 0]];
        $seen = [$start => true];
        $head = 0;
        while ($head < count($queue)) {
            [$r, $c, $orient, $moves] = $queue[$head++];
            if ("$r,$c,$orient" === $target) return $moves;
            $nxt = [];
            if ($orient === 0) {
                if ($c + 2 < $n && $grid[$r][$c + 2] === 0) $nxt[] = [$r, $c + 1, 0];
                if ($r + 1 < $n && $grid[$r + 1][$c] === 0 && $grid[$r + 1][$c + 1] === 0) {
                    $nxt[] = [$r + 1, $c, 0];
                    $nxt[] = [$r, $c, 1];
                }
            } else {
                if ($r + 2 < $n && $grid[$r + 2][$c] === 0) $nxt[] = [$r + 1, $c, 1];
                if ($c + 1 < $n && $grid[$r][$c + 1] === 0 && $grid[$r + 1][$c + 1] === 0) {
                    $nxt[] = [$r, $c + 1, 1];
                    $nxt[] = [$r, $c, 0];
                }
            }
            foreach ($nxt as [$nr, $nc, $no]) {
                $key = "$nr,$nc,$no";
                if (!isset($seen[$key])) {
                    $seen[$key] = true;
                    $queue[] = [$nr, $nc, $no, $moves + 1];
                }
            }
        }
        return -1;
    }
}
""")

add("1213_intersection_of_three_sorted_arrays", r"""<?php
// LeetCode 1213 - Intersection of Three Sorted Arrays
// https://leetcode.com/problems/intersection-of-three-sorted-arrays/

class Solution {
    /**
     * @param Integer[] $arr1
     * @param Integer[] $arr2
     * @param Integer[] $arr3
     * @return Integer[]
     */
    function arraysIntersection($arr1, $arr2, $arr3) {
        $ans = array_values(array_intersect($arr1, $arr2, $arr3));
        sort($ans);
        return $ans;
    }
}
""")

add("1214_two_sum_bsts", r"""<?php
// LeetCode 1214 - Two Sum BSTs
// https://leetcode.com/problems/two-sum-bsts/

class Solution {
    /**
     * @param TreeNode $root1
     * @param TreeNode $root2
     * @param Integer $target
     * @return Boolean
     */
    function twoSumBSTs($root1, $root2, $target) {
        $values = [];
        $stack = $root1 !== null ? [$root1] : [];
        while (!empty($stack)) {
            $node = array_pop($stack);
            $values[$node->val] = true;
            if ($node->left !== null) $stack[] = $node->left;
            if ($node->right !== null) $stack[] = $node->right;
        }
        $stack = $root2 !== null ? [$root2] : [];
        while (!empty($stack)) {
            $node = array_pop($stack);
            if (isset($values[$target - $node->val])) return true;
            if ($node->left !== null) $stack[] = $node->left;
            if ($node->right !== null) $stack[] = $node->right;
        }
        return false;
    }
}
""")

add("1215_stepping_numbers", r"""<?php
// LeetCode 1215 - Stepping Numbers
// https://leetcode.com/problems/stepping-numbers/

class Solution {
    /**
     * @param Integer $low
     * @param Integer $high
     * @return Integer[]
     */
    function countSteppingNumbers($low, $high) {
        $answer = $low === 0 ? [0] : [];
        $queue = range(1, 9);
        $head = 0;
        while ($head < count($queue)) {
            $x = $queue[$head++];
            if ($x > $high) continue;
            if ($x >= $low) $answer[] = $x;
            $last = $x % 10;
            if ($last > 0) $queue[] = $x * 10 + $last - 1;
            if ($last < 9) $queue[] = $x * 10 + $last + 1;
        }
        sort($answer);
        return $answer;
    }
}
""")

add("1216_valid_palindrome_iii", r"""<?php
// LeetCode 1216 - Valid Palindrome III
// https://leetcode.com/problems/valid-palindrome-iii/

class Solution {
    /**
     * @param String $s
     * @param Integer $k
     * @return Boolean
     */
    function isValidPalindrome($s, $k) {
        $n = strlen($s);
        if ($n === 0) return true;
        $dp = array_fill(0, $n, 0);
        for ($i = $n - 1; $i >= 0; $i--) {
            $previous = 0;
            for ($j = $i + 1; $j < $n; $j++) {
                $old = $dp[$j];
                if ($s[$i] === $s[$j]) $dp[$j] = $previous;
                else $dp[$j] = 1 + min($dp[$j], $dp[$j - 1]);
                $previous = $old;
            }
        }
        return $dp[$n - 1] <= $k;
    }
}
""")

add("1217_minimum_cost_to_move_chips_to_the_same_position", r"""<?php
// LeetCode 1217 - Minimum Cost to Move Chips to The Same Position
// https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/

class Solution {
    /**
     * @param Integer[] $position
     * @return Integer
     */
    function minCostToMoveChips($position) {
        $odd = 0;
        foreach ($position as $x) if ($x & 1) $odd++;
        return min($odd, count($position) - $odd);
    }
}
""")

add("1218_longest_arithmetic_subsequence_of_given_difference", r"""<?php
// LeetCode 1218 - Longest Arithmetic Subsequence of Given Difference
// https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/

class Solution {
    /**
     * @param Integer[] $arr
     * @param Integer $difference
     * @return Integer
     */
    function longestSubsequence($arr, $difference) {
        $dp = [];
        $best = 0;
        foreach ($arr as $x) {
            $dp[$x] = ($dp[$x - $difference] ?? 0) + 1;
            $best = max($best, $dp[$x]);
        }
        return $best;
    }
}
""")

add("1219_path_with_maximum_gold", r"""<?php
// LeetCode 1219 - Path with Maximum Gold
// https://leetcode.com/problems/path-with-maximum-gold/

class Solution {
    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function getMaximumGold($grid) {
        $rows = count($grid);
        $cols = count($grid[0]);
        $dfs = function ($r, $c) use (&$dfs, &$grid, $rows, $cols) {
            $gold = $grid[$r][$c];
            $grid[$r][$c] = 0;
            $best = 0;
            foreach ([[1,0],[-1,0],[0,1],[0,-1]] as [$dr, $dc]) {
                $nr = $r + $dr; $nc = $c + $dc;
                if ($nr >= 0 && $nr < $rows && $nc >= 0 && $nc < $cols && $grid[$nr][$nc]) {
                    $best = max($best, $dfs($nr, $nc));
                }
            }
            $grid[$r][$c] = $gold;
            return $gold + $best;
        };
        $ans = 0;
        for ($r = 0; $r < $rows; $r++) {
            for ($c = 0; $c < $cols; $c++) {
                if ($grid[$r][$c]) $ans = max($ans, $dfs($r, $c));
            }
        }
        return $ans;
    }
}
""")

add("1220_count_vowels_permutation", r"""<?php
// LeetCode 1220 - Count Vowels Permutation
// https://leetcode.com/problems/count-vowels-permutation/

class Solution {
    /**
     * @param Integer $n
     * @return Integer
     */
    function countVowelPermutation($n) {
        $mod = 1000000007;
        $a = $e = $i = $o = $u = 1;
        for ($t = 1; $t < $n; $t++) {
            [$a, $e, $i, $o, $u] = [
                ($e + $i + $u) % $mod,
                ($a + $i) % $mod,
                ($e + $o) % $mod,
                $i,
                ($i + $o) % $mod
            ];
        }
        return ($a + $e + $i + $o + $u) % $mod;
    }
}
""")

add("1221_split_a_string_in_balanced_strings", r"""<?php
// LeetCode 1221 - Split a String in Balanced Strings
// https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution {
    /**
     * @param String $s
     * @return Integer
     */
    function balancedStringSplit($s) {
        $balance = $answer = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $balance += $s[$i] === 'L' ? 1 : -1;
            if ($balance === 0) $answer++;
        }
        return $answer;
    }
}
""")

add("1222_queens_that_can_attack_the_king", r"""<?php
// LeetCode 1222 - Queens That Can Attack the King
// https://leetcode.com/problems/queens-that-can-attack-the-king/

class Solution {
    /**
     * @param Integer[][] $queens
     * @param Integer[] $king
     * @return Integer[][]
     */
    function queensAttacktheKing($queens, $king) {
        $occupied = [];
        foreach ($queens as $q) $occupied[$q[0] . ',' . $q[1]] = true;
        $answer = [];
        foreach ([-1, 0, 1] as $dr) {
            foreach ([-1, 0, 1] as $dc) {
                if ($dr === 0 && $dc === 0) continue;
                $r = $king[0] + $dr; $c = $king[1] + $dc;
                while ($r >= 0 && $r < 8 && $c >= 0 && $c < 8) {
                    if (isset($occupied["$r,$c"])) {
                        $answer[] = [$r, $c];
                        break;
                    }
                    $r += $dr; $c += $dc;
                }
            }
        }
        return $answer;
    }
}
""")

add("1223_dice_roll_simulation", r"""<?php
// LeetCode 1223 - Dice Roll Simulation
// https://leetcode.com/problems/dice-roll-simulation/

class Solution {
    /**
     * @param Integer $n
     * @param Integer[] $rollMax
     * @return Integer
     */
    function dieSimulator($n, $rollMax) {
        $mod = 1000000007;
        $dp = [];
        for ($j = 0; $j < 6; $j++) {
            $dp[$j] = array_fill(0, $rollMax[$j] + 1, 0);
            $dp[$j][1] = 1;
        }
        for ($t = 1; $t < $n; $t++) {
            $totals = [];
            for ($j = 0; $j < 6; $j++) $totals[$j] = array_sum($dp[$j]) % $mod;
            $nxt = [];
            $sumAll = array_sum($totals) % $mod;
            for ($j = 0; $j < 6; $j++) {
                $nxt[$j] = array_fill(0, count($dp[$j]), 0);
                $nxt[$j][1] = ($sumAll - $totals[$j] + $mod) % $mod;
                for ($run = 2; $run < count($dp[$j]); $run++) {
                    $nxt[$j][$run] = $dp[$j][$run - 1];
                }
            }
            $dp = $nxt;
        }
        $ans = 0;
        foreach ($dp as $row) $ans = ($ans + array_sum($row)) % $mod;
        return $ans;
    }
}
""")

add("1224_maximum_equal_frequency", r"""<?php
// LeetCode 1224 - Maximum Equal Frequency
// https://leetcode.com/problems/maximum-equal-frequency/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maxEqualFreq($nums) {
        $count = [];
        $frequencies = [];
        $answer = 0;
        foreach ($nums as $i => $x) {
            $i++;
            $old = $count[$x] ?? 0;
            if ($old) {
                $frequencies[$old]--;
                if ($frequencies[$old] === 0) unset($frequencies[$old]);
            }
            $count[$x] = $old + 1;
            $frequencies[$old + 1] = ($frequencies[$old + 1] ?? 0) + 1;
            $high = max(array_keys($frequencies));
            if ($high === 1
                || ($frequencies[$high] ?? 0) * $high + 1 === $i
                || (($frequencies[$high] ?? 0) === 1 && ($frequencies[$high - 1] ?? 0) * ($high - 1) + $high === $i)) {
                $answer = $i;
            }
        }
        return $answer;
    }
}
""")

add("1226_the_dining_philosophers", r"""<?php
// LeetCode 1226 - The Dining Philosophers
// https://leetcode.com/problems/the-dining-philosophers/

class DiningPhilosophers {
    private $forks;

    function __construct() {
        $this->forks = array_fill(0, 5, false);
    }

    /**
     * @param Integer $philosopher
     * @param Callable $pickLeftFork
     * @param Callable $pickRightFork
     * @param Callable $eat
     * @param Callable $putLeftFork
     * @param Callable $putRightFork
     * @return NULL
     */
    function wantsToEat($philosopher, $pickLeftFork, $pickRightFork, $eat, $putLeftFork, $putRightFork) {
        $left = $philosopher;
        $right = ($philosopher + 1) % 5;
        if ($philosopher % 2 === 0) {
            $first = $left; $second = $right;
        } else {
            $first = $right; $second = $left;
        }
        while ($this->forks[$first]) { usleep(100); }
        $this->forks[$first] = true;
        while ($this->forks[$second]) { usleep(100); }
        $this->forks[$second] = true;
        $pickLeftFork();
        $pickRightFork();
        $eat();
        $putLeftFork();
        $putRightFork();
        $this->forks[$first] = false;
        $this->forks[$second] = false;
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

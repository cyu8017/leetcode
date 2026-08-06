#!/usr/bin/env python3
"""Port stub solution.php files for problems 1180-1220 (non-SQL)."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOLUTIONS: dict[str, str] = {}


def add(name: str, content: str) -> None:
    SOLUTIONS[name] = content.strip() + "\n"


add("1180_count_substrings_with_only_one_distinct_letter", r"""<?php
// LeetCode 1180 - Count Substrings with Only One Distinct Letter
// https://leetcode.com/problems/count-substrings-with-only-one-distinct-letter/

class Solution {
    /**
     * @param String $s
     * @return Integer
     */
    function countLetters($s) {
        $ans = $length = 1;
        $n = strlen($s);
        for ($i = 1; $i < $n; $i++) {
            $length = ($s[$i] === $s[$i - 1]) ? $length + 1 : 1;
            $ans += $length;
        }
        return $ans;
    }
}
""")

add("1181_before_and_after_puzzle", r"""<?php
// LeetCode 1181 - Before and After Puzzle
// https://leetcode.com/problems/before-and-after-puzzle/

class Solution {
    /**
     * @param String[] $phrases
     * @return String[]
     */
    function beforeAndAfterPuzzles($phrases) {
        $split = array_map(fn($p) => explode(' ', $p), $phrases);
        $result = [];
        $m = count($split);
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $m; $j++) {
                if ($i === $j) continue;
                if ($split[$i][count($split[$i]) - 1] === $split[$j][0]) {
                    $merged = array_merge($split[$i], array_slice($split[$j], 1));
                    $result[implode(' ', $merged)] = true;
                }
            }
        }
        $ans = array_keys($result);
        sort($ans);
        return $ans;
    }
}
""")

add("1182_shortest_distance_to_target_color", r"""<?php
// LeetCode 1182 - Shortest Distance to Target Color
// https://leetcode.com/problems/shortest-distance-to-target-color/

class Solution {
    /**
     * @param Integer[] $colors
     * @param Integer[][] $queries
     * @return Integer[]
     */
    function shortestDistanceColor($colors, $queries) {
        $pos = [];
        foreach ($colors as $i => $c) $pos[$c][] = $i;
        $ans = [];
        foreach ($queries as [$i, $c]) {
            if (!isset($pos[$c])) { $ans[] = -1; continue; }
            $arr = $pos[$c];
            $lo = 0; $hi = count($arr);
            while ($lo < $hi) {
                $mid = ($lo + $hi) >> 1;
                if ($arr[$mid] < $i) $lo = $mid + 1;
                else $hi = $mid;
            }
            $best = PHP_INT_MAX;
            if ($lo < count($arr)) $best = min($best, $arr[$lo] - $i);
            if ($lo > 0) $best = min($best, $i - $arr[$lo - 1]);
            $ans[] = $best === PHP_INT_MAX ? -1 : $best;
        }
        return $ans;
    }
}
""")

add("1183_maximum_number_of_ones", r"""<?php
// LeetCode 1183 - Maximum Number of Ones
// https://leetcode.com/problems/maximum-number-of-ones/

class Solution {
    /**
     * @param Integer $width
     * @param Integer $height
     * @param Integer $sideLength
     * @param Integer $maxOnes
     * @return Integer
     */
    function maximumNumberOfOnes($width, $height, $sideLength, $maxOnes) {
        $counts = [];
        for ($r = 0; $r < $sideLength; $r++) {
            for ($c = 0; $c < $sideLength; $c++) {
                $rows = intdiv($height - $r + $sideLength - 1, $sideLength);
                $cols = intdiv($width - $c + $sideLength - 1, $sideLength);
                $counts[] = $rows * $cols;
            }
        }
        rsort($counts);
        return array_sum(array_slice($counts, 0, $maxOnes));
    }
}
""")

add("1184_distance_between_bus_stops", r"""<?php
// LeetCode 1184 - Distance Between Bus Stops
// https://leetcode.com/problems/distance-between-bus-stops/

class Solution {
    /**
     * @param Integer[] $distance
     * @param Integer $start
     * @param Integer $destination
     * @return Integer
     */
    function distanceBetweenBusStops($distance, $start, $destination) {
        if ($start > $destination) [$start, $destination] = [$destination, $start];
        $clockwise = array_sum(array_slice($distance, $start, $destination - $start));
        return min($clockwise, array_sum($distance) - $clockwise);
    }
}
""")

add("1185_day_of_the_week", r"""<?php
// LeetCode 1185 - Day of the Week
// https://leetcode.com/problems/day-of-the-week/

class Solution {
    /**
     * @param Integer $day
     * @param Integer $month
     * @param Integer $year
     * @return String
     */
    function dayOfTheWeek($day, $month, $year) {
        return date('l', strtotime(sprintf('%04d-%02d-%02d', $year, $month, $day)));
    }
}
""")

add("1186_maximum_subarray_sum_with_one_deletion", r"""<?php
// LeetCode 1186 - Maximum Subarray Sum with One Deletion
// https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/

class Solution {
    /**
     * @param Integer[] $arr
     * @return Integer
     */
    function maximumSum($arr) {
        $keep = $delete = $ans = $arr[0];
        $n = count($arr);
        for ($i = 1; $i < $n; $i++) {
            $x = $arr[$i];
            $delete = max($keep, $delete + $x);
            $keep = max($keep + $x, $x);
            $ans = max($ans, $keep, $delete);
        }
        return $ans;
    }
}
""")

add("1187_make_array_strictly_increasing", r"""<?php
// LeetCode 1187 - Make Array Strictly Increasing
// https://leetcode.com/problems/make-array-strictly-increasing/

class Solution {
    /**
     * @param Integer[] $arr1
     * @param Integer[] $arr2
     * @return Integer
     */
    function makeArrayIncreasing($arr1, $arr2) {
        $arr2 = array_values(array_unique($arr2));
        sort($arr2);
        $dp = [-1 => 0];
        foreach ($arr1 as $num) {
            $newDp = [];
            foreach ($dp as $prev => $ops) {
                if ($num > $prev) {
                    $newDp[$num] = min($newDp[$num] ?? PHP_INT_MAX, $ops);
                }
                $lo = 0; $hi = count($arr2);
                while ($lo < $hi) {
                    $mid = ($lo + $hi) >> 1;
                    if ($arr2[$mid] <= $prev) $lo = $mid + 1;
                    else $hi = $mid;
                }
                if ($lo < count($arr2)) {
                    $chosen = $arr2[$lo];
                    $newDp[$chosen] = min($newDp[$chosen] ?? PHP_INT_MAX, $ops + 1);
                }
            }
            $dp = $newDp;
            if (empty($dp)) return -1;
        }
        return min($dp);
    }
}
""")

add("1188_design_bounded_blocking_queue", r"""<?php
// LeetCode 1188 - Design Bounded Blocking Queue
// https://leetcode.com/problems/design-bounded-blocking-queue/

class BoundedBlockingQueue {
    private $capacity;
    private $queue = [];

    /**
     * @param Integer $capacity
     */
    function __construct($capacity) {
        $this->capacity = $capacity;
    }

    /**
     * @param Integer $element
     * @return NULL
     */
    function enqueue($element) {
        while (count($this->queue) >= $this->capacity) { usleep(100); }
        $this->queue[] = $element;
    }

    /**
     * @return Integer
     */
    function dequeue() {
        while (empty($this->queue)) { usleep(100); }
        return array_shift($this->queue);
    }

    /**
     * @return Integer
     */
    function size() {
        return count($this->queue);
    }
}
""")

add("1189_maximum_number_of_balloons", r"""<?php
// LeetCode 1189 - Maximum Number of Balloons
// https://leetcode.com/problems/maximum-number-of-balloons/

class Solution {
    /**
     * @param String $text
     * @return Integer
     */
    function maxNumberOfBalloons($text) {
        $count = array_count_values(str_split($text));
        return min(
            $count['b'] ?? 0,
            $count['a'] ?? 0,
            intdiv($count['l'] ?? 0, 2),
            intdiv($count['o'] ?? 0, 2),
            $count['n'] ?? 0
        );
    }
}
""")

add("1190_reverse_substrings_between_each_pair_of_parentheses", r"""<?php
// LeetCode 1190 - Reverse Substrings Between Each Pair of Parentheses
// https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/

class Solution {
    /**
     * @param String $s
     * @return String
     */
    function reverseParentheses($s) {
        $stack = [];
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $ch = $s[$i];
            if ($ch === ')') {
                $chunk = [];
                while (!empty($stack) && end($stack) !== '(') $chunk[] = array_pop($stack);
                array_pop($stack);
                foreach ($chunk as $c) $stack[] = $c;
            } else {
                $stack[] = $ch;
            }
        }
        return implode('', $stack);
    }
}
""")

add("1191_k_concatenation_maximum_sum", r"""<?php
// LeetCode 1191 - K-Concatenation Maximum Sum
// https://leetcode.com/problems/k-concatenation-maximum-sum/

class Solution {
    /**
     * @param Integer[] $arr
     * @param Integer $k
     * @return Integer
     */
    function kConcatenationMaxSum($arr, $k) {
        $mod = 1000000007;
        $kadane = function ($nums) {
            $best = $cur = 0;
            foreach ($nums as $x) {
                $cur = max(0, $cur + $x);
                $best = max($best, $cur);
            }
            return $best;
        };
        $one = $kadane($arr);
        if ($k === 1) return $one % $mod;
        $two = $kadane(array_merge($arr, $arr));
        $total = array_sum($arr);
        if ($total > 0) return max($one, $two + $total * ($k - 2)) % $mod;
        return max($one, $two) % $mod;
    }
}
""")

add("1192_critical_connections_in_a_network", r"""<?php
// LeetCode 1192 - Critical Connections in a Network
// https://leetcode.com/problems/critical-connections-in-a-network/

class Solution {
    /**
     * @param Integer $n
     * @param Integer[][] $connections
     * @return Integer[][]
     */
    function criticalConnections($n, $connections) {
        $graph = array_fill(0, $n, []);
        foreach ($connections as [$a, $b]) {
            $graph[$a][] = $b;
            $graph[$b][] = $a;
        }
        $disc = array_fill(0, $n, -1);
        $low = array_fill(0, $n, -1);
        $time = 0;
        $bridges = [];
        $dfs = function ($node, $parent) use (&$dfs, &$graph, &$disc, &$low, &$time, &$bridges) {
            $disc[$node] = $low[$node] = $time++;
            foreach ($graph[$node] as $nxt) {
                if ($nxt === $parent) continue;
                if ($disc[$nxt] === -1) {
                    $dfs($nxt, $node);
                    $low[$node] = min($low[$node], $low[$nxt]);
                    if ($low[$nxt] > $disc[$node]) $bridges[] = [$node, $nxt];
                } else {
                    $low[$node] = min($low[$node], $disc[$nxt]);
                }
            }
        };
        $dfs(0, -1);
        return array_map(fn($e) => [min($e[0], $e[1]), max($e[0], $e[1])], $bridges);
    }
}
""")

add("1195_fizz_buzz_multithreaded", r"""<?php
// LeetCode 1195 - Fizz Buzz Multithreaded
// https://leetcode.com/problems/fizz-buzz-multithreaded/

class FizzBuzz {
    private $n;
    private $current = 1;

    function __construct($n) {
        $this->n = $n;
    }

    function fizz($printFizz) {
        $this->run(fn($x) => $x % 3 === 0 && $x % 5 !== 0, $printFizz);
    }

    function buzz($printBuzz) {
        $this->run(fn($x) => $x % 5 === 0 && $x % 3 !== 0, $printBuzz);
    }

    function fizzbuzz($printFizzBuzz) {
        $this->run(fn($x) => $x % 15 === 0, $printFizzBuzz);
    }

    function number($printNumber) {
        $this->run(fn($x) => $x % 3 !== 0 && $x % 5 !== 0, function () use ($printNumber) {
            $printNumber($this->current);
        });
    }

    private function run($predicate, $action) {
        while ($this->current <= $this->n) {
            if ($predicate($this->current)) {
                $action();
                $this->current++;
            } else {
                usleep(100);
            }
        }
    }
}
""")

add("1196_how_many_apples_can_you_put_into_the_basket", r"""<?php
// LeetCode 1196 - How Many Apples Can You Put into the Basket
// https://leetcode.com/problems/how-many-apples-can-you-put-into-the-basket/

class Solution {
    /**
     * @param Integer[] $weight
     * @return Integer
     */
    function maxNumberOfApples($weight) {
        sort($weight);
        $total = 0;
        foreach ($weight as $i => $w) {
            $total += $w;
            if ($total > 5000) return $i;
        }
        return count($weight);
    }
}
""")

add("1197_minimum_knight_moves", r"""<?php
// LeetCode 1197 - Minimum Knight Moves
// https://leetcode.com/problems/minimum-knight-moves/

class Solution {
    private $memo = [];

    /**
     * @param Integer $x
     * @param Integer $y
     * @return Integer
     */
    function minKnightMoves($x, $y) {
        return $this->dfs(abs($x), abs($y));
    }

    private function dfs($a, $b) {
        if ($a + $b === 0) return 0;
        if ($a + $b === 2) return 2;
        $key = "$a,$b";
        if (isset($this->memo[$key])) return $this->memo[$key];
        return $this->memo[$key] = min(
            $this->dfs(abs($a - 1), abs($b - 2)),
            $this->dfs(abs($a - 2), abs($b - 1))
        ) + 1;
    }
}
""")

add("1198_find_smallest_common_element_in_all_rows", r"""<?php
// LeetCode 1198 - Find Smallest Common Element in All Rows
// https://leetcode.com/problems/find-smallest-common-element-in-all-rows/

class Solution {
    /**
     * @param Integer[][] $mat
     * @return Integer
     */
    function smallestCommonElement($mat) {
        $common = array_flip($mat[0]);
        for ($r = 1; $r < count($mat); $r++) {
            $row = array_flip($mat[$r]);
            $common = array_intersect_key($common, $row);
            if (empty($common)) return -1;
        }
        return min(array_keys($common));
    }
}
""")

add("1199_minimum_time_to_build_blocks", r"""<?php
// LeetCode 1199 - Minimum Time to Build Blocks
// https://leetcode.com/problems/minimum-time-to-build-blocks/

class Solution {
    /**
     * @param Integer[] $blocks
     * @param Integer $split
     * @return Integer
     */
    function minBuildTime($blocks, $split) {
        $heap = new SplMinHeap();
        foreach ($blocks as $b) $heap->insert($b);
        while ($heap->count() > 1) {
            $heap->extract();
            $heap->insert($heap->extract() + $split);
        }
        return $heap->extract();
    }
}
""")

add("1200_minimum_absolute_difference", r"""<?php
// LeetCode 1200 - Minimum Absolute Difference
// https://leetcode.com/problems/minimum-absolute-difference/

class Solution {
    /**
     * @param Integer[] $arr
     * @return Integer[][]
     */
    function minimumAbsDifference($arr) {
        sort($arr);
        $best = PHP_INT_MAX;
        $n = count($arr);
        for ($i = 0; $i < $n - 1; $i++) $best = min($best, $arr[$i + 1] - $arr[$i]);
        $ans = [];
        for ($i = 0; $i < $n - 1; $i++) {
            if ($arr[$i + 1] - $arr[$i] === $best) $ans[] = [$arr[$i], $arr[$i + 1]];
        }
        return $ans;
    }
}
""")

add("1201_ugly_number_iii", r"""<?php
// LeetCode 1201 - Ugly Number III
// https://leetcode.com/problems/ugly-number-iii/

class Solution {
    /**
     * @param Integer $n
     * @param Integer $a
     * @param Integer $b
     * @param Integer $c
     * @return Integer
     */
    function nthUglyNumber($n, $a, $b, $c) {
        $gcd = function ($x, $y) use (&$gcd) {
            return $y === 0 ? $x : $gcd($y, $x % $y);
        };
        $lcm = fn($x, $y) => intdiv($x, $gcd($x, $y)) * $y;
        $ab = $lcm($a, $b); $ac = $lcm($a, $c); $bc = $lcm($b, $c);
        $abc = $lcm($ab, $c);
        $count = function ($x) use ($a, $b, $c, $ab, $ac, $bc, $abc) {
            return intdiv($x, $a) + intdiv($x, $b) + intdiv($x, $c)
                - intdiv($x, $ab) - intdiv($x, $ac) - intdiv($x, $bc) + intdiv($x, $abc);
        };
        $lo = 1; $hi = 2000000000;
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi, 2);
            if ($count($mid) >= $n) $hi = $mid;
            else $lo = $mid + 1;
        }
        return $lo;
    }
}
""")

add("1202_smallest_string_with_swaps", r"""<?php
// LeetCode 1202 - Smallest String With Swaps
// https://leetcode.com/problems/smallest-string-with-swaps/

class Solution {
    /**
     * @param String $s
     * @param Integer[][] $pairs
     * @return String
     */
    function smallestStringWithSwaps($s, $pairs) {
        $n = strlen($s);
        $parent = range(0, $n - 1);
        $find = function ($x) use (&$parent, &$find) {
            if ($parent[$x] !== $x) $parent[$x] = $find($parent[$x]);
            return $parent[$x];
        };
        foreach ($pairs as [$a, $b]) {
            $ra = $find($a); $rb = $find($b);
            if ($ra !== $rb) $parent[$rb] = $ra;
        }
        $groups = [];
        for ($i = 0; $i < $n; $i++) $groups[$find($i)][] = $i;
        $chars = str_split($s);
        foreach ($groups as $idxs) {
            $letters = [];
            foreach ($idxs as $i) $letters[] = $chars[$i];
            sort($letters);
            sort($idxs);
            foreach ($idxs as $j => $i) $chars[$i] = $letters[$j];
        }
        return implode('', $chars);
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

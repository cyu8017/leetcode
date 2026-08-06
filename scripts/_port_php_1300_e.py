#!/usr/bin/env python3
"""Port PHP solutions for LeetCode stubs batch E (1463-1499)."""
from __future__ import annotations

import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SOLUTIONS: dict[str, str] = {
    "1463_cherry_pickup_ii": r'''<?php
class Solution {
    function cherryPickup($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        $dp = ["0," . ($n - 1) => $grid[0][0] + ($n > 1 ? $grid[0][$n - 1] : 0)];
        for ($r = 1; $r < $m; $r++) {
            $nxt = [];
            foreach ($dp as $key => $score) {
                [$a, $b] = array_map('intval', explode(",", $key));
                for ($na = $a - 1; $na <= $a + 1; $na++) {
                    for ($nb = $b - 1; $nb <= $b + 1; $nb++) {
                        if ($na >= 0 && $na < $n && $nb >= 0 && $nb < $n) {
                            $val = $score + $grid[$r][$na] + ($na !== $nb ? $grid[$r][$nb] : 0);
                            $nk = "$na,$nb";
                            $nxt[$nk] = max($nxt[$nk] ?? -1, $val);
                        }
                    }
                }
            }
            $dp = $nxt;
        }
        return max($dp);
    }
}
''',
    "1464_maximum_product_of_two_elements_in_an_array": r'''<?php
class Solution {
    function maxProduct($nums) {
        sort($nums);
        $n = count($nums);
        return ($nums[$n - 2] - 1) * ($nums[$n - 1] - 1);
    }
}
''',
    "1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts": r'''<?php
class Solution {
    function maxArea($h, $w, $horizontalCuts, $verticalCuts) {
        $hs = array_merge([0, $h], $horizontalCuts);
        $vs = array_merge([0, $w], $verticalCuts);
        sort($hs);
        sort($vs);
        $maxH = 0;
        for ($i = 1; $i < count($hs); $i++) $maxH = max($maxH, $hs[$i] - $hs[$i - 1]);
        $maxV = 0;
        for ($i = 1; $i < count($vs); $i++) $maxV = max($maxV, $vs[$i] - $vs[$i - 1]);
        return ($maxH * $maxV) % 1000000007;
    }
}
''',
    "1466_reorder_routes_to_make_all_paths_lead_to_the_city_zero": r'''<?php
class Solution {
    function minReorder($n, $connections) {
        $graph = array_fill(0, $n, []);
        foreach ($connections as [$a, $b]) {
            $graph[$a][] = [$b, 1];
            $graph[$b][] = [$a, 0];
        }
        $ans = 0;
        $stack = [0];
        $seen = [0 => true];
        while ($stack) {
            $node = array_pop($stack);
            foreach ($graph[$node] as [$nei, $cost]) {
                if (!isset($seen[$nei])) {
                    $seen[$nei] = true;
                    $stack[] = $nei;
                    $ans += $cost;
                }
            }
        }
        return $ans;
    }
}
''',
    "1467_probability_of_a_two_boxes_having_the_same_number_of_distinct_balls": r'''<?php
class Solution {
    function getProbability($balls) {
        $half = intdiv(array_sum($balls), 2);
        $good = 0;
        $total = 0;
        $comb = function($n, $k) {
            if ($k < 0 || $k > $n) return 0;
            $r = 1;
            for ($i = 0; $i < $k; $i++) $r = $r * ($n - $i) / ($i + 1);
            return $r;
        };
        $dfs = function($i, $left, $dl, $ways) use (&$dfs, &$good, &$total, $balls, $half, $comb) {
            if ($i === count($balls)) {
                if ($left === $half) {
                    $total += $ways;
                    if ($dl === 0) $good += $ways;
                }
                return;
            }
            for ($x = 0; $x <= $balls[$i]; $x++) {
                if ($left + $x <= $half) {
                    $dfs($i + 1, $left + $x, $dl + ($x > 0 ? 1 : 0) - ($x < $balls[$i] ? 1 : 0), $ways * $comb($balls[$i], $x));
                }
            }
        };
        $dfs(0, 0, 0, 1);
        return $good / $total;
    }
}
''',
    "1469_find_all_the_lonely_nodes": r'''<?php
class Solution {
    function getLonelyNodes($root) {
        $ans = [];
        $dfs = function($node) use (&$dfs, &$ans) {
            if (!$node) return;
            if (boolval($node->left) xor boolval($node->right)) {
                $ans[] = ($node->left ?: $node->right)->val;
            }
            $dfs($node->left);
            $dfs($node->right);
        };
        $dfs($root);
        return $ans;
    }
}
''',
    "1470_shuffle_the_array": r'''<?php
class Solution {
    function shuffle($nums, $n) {
        $answer = [];
        for ($i = 0; $i < $n; $i++) {
            $answer[] = $nums[$i];
            $answer[] = $nums[$i + $n];
        }
        return $answer;
    }
}
''',
    "1471_the_k_strongest_values_in_an_array": r'''<?php
class Solution {
    function getStrongest($arr, $k) {
        sort($arr);
        $median = $arr[intdiv(count($arr) - 1, 2)];
        usort($arr, function($a, $b) use ($median) {
            $da = abs($a - $median);
            $db = abs($b - $median);
            if ($da !== $db) return $db <=> $da;
            return $b <=> $a;
        });
        return array_slice($arr, 0, $k);
    }
}
''',
    "1472_design_browser_history": r'''<?php
class BrowserHistory {
    private $history;
    private $index;

    function __construct($homepage) {
        $this->history = [$homepage];
        $this->index = 0;
    }

    function visit($url) {
        $this->history = array_slice($this->history, 0, $this->index + 1);
        $this->history[] = $url;
        $this->index++;
    }

    function back($steps) {
        $this->index = max(0, $this->index - $steps);
        return $this->history[$this->index];
    }

    function forward($steps) {
        $this->index = min(count($this->history) - 1, $this->index + $steps);
        return $this->history[$this->index];
    }
}
''',
    "1473_paint_house_iii": r'''<?php
class Solution {
    function minCost($houses, $cost, $m, $n, $target) {
        $inf = 10 ** 15;
        $dp = ["0,0" => 0];
        foreach ($houses as $i => $painted) {
            $nxt = [];
            $colors = $painted ? [$painted] : range(1, $n);
            foreach ($dp as $key => $value) {
                [$prev, $groups] = array_map('intval', explode(",", $key));
                foreach ($colors as $color) {
                    $ng = $groups + ($color !== $prev ? 1 : 0);
                    if ($ng <= $target) {
                        $nv = $value + ($painted ? 0 : $cost[$i][$color - 1]);
                        $nk = "$color,$ng";
                        $nxt[$nk] = min($nxt[$nk] ?? $inf, $nv);
                    }
                }
            }
            $dp = $nxt;
        }
        $ans = $inf;
        foreach ($dp as $key => $v) {
            [, $g] = array_map('intval', explode(",", $key));
            if ($g === $target) $ans = min($ans, $v);
        }
        return $ans === $inf ? -1 : $ans;
    }
}
''',
    "1474_delete_n_nodes_after_m_nodes_of_a_linked_list": r'''<?php
class Solution {
    function deleteNodes($head, $m, $n) {
        $cur = $head;
        while ($cur) {
            for ($kept = 1; $kept < $m && $cur; $kept++) $cur = $cur->next;
            if (!$cur) break;
            $drop = $cur->next;
            for ($count = 0; $count < $n && $drop; $count++) $drop = $drop->next;
            $cur->next = $drop;
            $cur = $drop;
        }
        return $head;
    }
}
''',
    "1475_final_prices_with_a_special_discount_in_a_shop": r'''<?php
class Solution {
    function finalPrices($prices) {
        $ans = $prices;
        $stack = [];
        foreach ($prices as $i => $price) {
            while ($stack && $prices[$stack[count($stack) - 1]] >= $price) {
                $j = array_pop($stack);
                $ans[$j] -= $price;
            }
            $stack[] = $i;
        }
        return $ans;
    }
}
''',
    "1476_subrectangle_queries": r'''<?php
class SubrectangleQueries {
    private $rectangle;

    function __construct($rectangle) {
        $this->rectangle = $rectangle;
    }

    function updateSubrectangle($row1, $col1, $row2, $col2, $newValue) {
        for ($r = $row1; $r <= $row2; $r++) {
            for ($c = $col1; $c <= $col2; $c++) {
                $this->rectangle[$r][$c] = $newValue;
            }
        }
    }

    function getValue($row, $col) {
        return $this->rectangle[$row][$col];
    }
}
''',
    "1477_find_two_non_overlapping_sub_arrays_each_with_target_sum": r'''<?php
class Solution {
    function minSumOfLengths($arr, $target) {
        $inf = 1000000000;
        $left = 0;
        $total = 0;
        $best = $inf;
        $ans = $inf;
        $shortest = array_fill(0, count($arr), $inf);
        foreach ($arr as $right => $x) {
            $total += $x;
            while ($total > $target) {
                $total -= $arr[$left];
                $left++;
            }
            if ($total === $target) {
                $length = $right - $left + 1;
                if ($left) $ans = min($ans, $length + $shortest[$left - 1]);
                $best = min($best, $length);
            }
            $shortest[$right] = $best;
        }
        return $ans === $inf ? -1 : $ans;
    }
}
''',
    "1478_allocate_mailboxes": r'''<?php
class Solution {
    function minDistance($houses, $k) {
        sort($houses);
        $n = count($houses);
        $cost = array_fill(0, $n, array_fill(0, $n, 0));
        for ($i = 0; $i < $n; $i++) {
            for ($j = $i; $j < $n; $j++) {
                $mid = $houses[intdiv($i + $j, 2)];
                $s = 0;
                for ($t = $i; $t <= $j; $t++) $s += abs($houses[$t] - $mid);
                $cost[$i][$j] = $s;
            }
        }
        $dp = array_fill(0, $n + 1, 10 ** 15);
        $dp[0] = 0;
        for ($mb = 0; $mb < $k; $mb++) {
            $ndp = array_fill(0, $n + 1, 10 ** 15);
            $ndp[0] = 0;
            for ($j = 1; $j <= $n; $j++) {
                for ($i = 0; $i < $j; $i++) {
                    $ndp[$j] = min($ndp[$j], $dp[$i] + $cost[$i][$j - 1]);
                }
            }
            $dp = $ndp;
        }
        return $dp[$n];
    }
}
''',
    "1480_running_sum_of_1d_array": r'''<?php
class Solution {
    function runningSum($nums) {
        for ($i = 1; $i < count($nums); $i++) $nums[$i] += $nums[$i - 1];
        return $nums;
    }
}
''',
    "1481_least_number_of_unique_integers_after_k_removals": r'''<?php
class Solution {
    function findLeastNumOfUniqueInts($arr, $k) {
        $counts = array_values(array_count_values($arr));
        sort($counts);
        $removed = 0;
        foreach ($counts as $count) {
            if ($k < $count) break;
            $k -= $count;
            $removed++;
        }
        return count($counts) - $removed;
    }
}
''',
    "1482_minimum_number_of_days_to_make_m_bouquets": r'''<?php
class Solution {
    function minDays($bloomDay, $m, $k) {
        if ($m * $k > count($bloomDay)) return -1;
        $possible = function($day) use ($bloomDay, $m, $k) {
            $bouquets = 0;
            $run = 0;
            foreach ($bloomDay as $x) {
                $run = $x <= $day ? $run + 1 : 0;
                if ($run === $k) {
                    $bouquets++;
                    $run = 0;
                }
            }
            return $bouquets >= $m;
        };
        $lo = min($bloomDay);
        $hi = max($bloomDay);
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi, 2);
            if ($possible($mid)) $hi = $mid;
            else $lo = $mid + 1;
        }
        return $lo;
    }
}
''',
    "1483_kth_ancestor_of_a_tree_node": r'''<?php
class TreeAncestor {
    private $up;

    function __construct($n, $parent) {
        $width = max(1, intval(log($n, 2)) + 1);
        $this->up = [$parent];
        for ($bit = 1; $bit < $width; $bit++) {
            $prev = $this->up[$bit - 1];
            $row = [];
            foreach ($prev as $p) $row[] = $p === -1 ? -1 : $prev[$p];
            $this->up[] = $row;
        }
    }

    function getKthAncestor($node, $k) {
        $bit = 0;
        while ($k && $node !== -1) {
            if ($k & 1) {
                if ($bit >= count($this->up)) return -1;
                $node = $this->up[$bit][$node];
            }
            $bit++;
            $k >>= 1;
        }
        return $node;
    }
}
''',
    "1485_clone_binary_tree_with_random_pointer": r'''<?php
class Node {
    public $val;
    public $left = null;
    public $right = null;
    public $random = null;
    function __construct($val = 0) {
        $this->val = $val;
    }
}

class Solution {
    function copyRandomBinaryTree($root) {
        $copies = new SplObjectStorage();
        $clone = function($node) use (&$clone, $copies) {
            if ($node === null) return null;
            if (!$copies->contains($node)) {
                $copy = new Node($node->val);
                $copies[$node] = $copy;
                $copy->left = $clone($node->left);
                $copy->right = $clone($node->right);
                $copy->random = $clone($node->random);
            }
            return $copies[$node];
        };
        return $clone($root);
    }
}
''',
    "1486_xor_operation_in_an_array": r'''<?php
class Solution {
    function xorOperation($n, $start) {
        $ans = 0;
        for ($i = 0; $i < $n; $i++) $ans ^= $start + 2 * $i;
        return $ans;
    }
}
''',
    "1487_making_file_names_unique": r'''<?php
class Solution {
    function getFolderNames($names) {
        $used = [];
        $ans = [];
        foreach ($names as $name) {
            if (!isset($used[$name])) {
                $candidate = $name;
            } else {
                $k = $used[$name];
                while (isset($used["$name($k)"])) $k++;
                $candidate = "$name($k)";
                $used[$name] = $k + 1;
            }
            $used[$candidate] = 1;
            $ans[] = $candidate;
        }
        return $ans;
    }
}
''',
    "1488_avoid_flood_in_the_city": r'''<?php
class Solution {
    function avoidFlood($rains) {
        $n = count($rains);
        $ans = array_fill(0, $n, -1);
        $full = [];
        $dry = [];
        foreach ($rains as $i => $lake) {
            if ($lake === 0) {
                $dry[] = $i;
                $ans[$i] = 1;
            } else {
                if (isset($full[$lake])) {
                    $found = -1;
                    foreach ($dry as $di => $day) {
                        if ($day > $full[$lake]) {
                            $found = $di;
                            break;
                        }
                    }
                    if ($found === -1) return [];
                    $ans[$dry[$found]] = $lake;
                    array_splice($dry, $found, 1);
                }
                $full[$lake] = $i;
            }
        }
        return $ans;
    }
}
''',
    "1489_find_critical_and_pseudo_critical_edges_in_minimum_spanning_tree": r'''<?php
class Solution {
    function findCriticalAndPseudoCriticalEdges($n, $edges) {
        $es = [];
        foreach ($edges as $i => [$a, $b, $w]) $es[] = [$w, $a, $b, $i];
        usort($es, function($x, $y) { return $x[0] <=> $y[0]; });
        $mst = function($skip = -1, $force = -1) use ($n, $es) {
            $parent = range(0, $n - 1);
            $find = function($x) use (&$parent, &$find) {
                while ($x !== $parent[$x]) {
                    $parent[$x] = $parent[$parent[$x]];
                    $x = $parent[$x];
                }
                return $x;
            };
            $total = 0;
            $used = 0;
            if ($force >= 0) {
                [$w, $a, $b] = $es[$force];
                $parent[$find($a)] = $find($b);
                $total += $w;
                $used++;
            }
            foreach ($es as $j => [$w, $a, $b]) {
                if ($j === $skip || $j === $force) continue;
                $x = $find($a);
                $y = $find($b);
                if ($x !== $y) {
                    $parent[$x] = $y;
                    $total += $w;
                    $used++;
                }
            }
            return $used === $n - 1 ? $total : PHP_INT_MAX;
        };
        $base = $mst();
        $critical = [];
        $pseudo = [];
        foreach ($es as $j => $edge) {
            if ($mst($j) > $base) $critical[] = $edge[3];
            elseif ($mst(-1, $j) === $base) $pseudo[] = $edge[3];
        }
        sort($critical);
        sort($pseudo);
        return [$critical, $pseudo];
    }
}
''',
    "1490_clone_n_ary_tree": r'''<?php
class Solution {
    function cloneTree($root) {
        if ($root === null) return null;
        $copy = (object)['val' => $root->val, 'children' => []];
        foreach ($root->children as $child) $copy->children[] = $this->cloneTree($child);
        return $copy;
    }
}
''',
    "1491_average_salary_excluding_the_minimum_and_maximum_salary": r'''<?php
class Solution {
    function average($salary) {
        return (array_sum($salary) - min($salary) - max($salary)) / (count($salary) - 2);
    }
}
''',
    "1492_the_kth_factor_of_n": r'''<?php
class Solution {
    function kthFactor($n, $k) {
        for ($x = 1; $x <= $n; $x++) {
            if ($n % $x === 0) {
                $k--;
                if ($k === 0) return $x;
            }
        }
        return -1;
    }
}
''',
    "1493_longest_subarray_of_1s_after_deleting_one_element": r'''<?php
class Solution {
    function longestSubarray($nums) {
        $left = 0;
        $zeros = 0;
        $ans = 0;
        foreach ($nums as $right => $x) {
            if ($x === 0) $zeros++;
            while ($zeros > 1) {
                if ($nums[$left] === 0) $zeros--;
                $left++;
            }
            $ans = max($ans, $right - $left);
        }
        return $ans;
    }
}
''',
    "1494_parallel_courses_ii": r'''<?php
class Solution {
    function minNumberOfSemesters($n, $relations, $k) {
        $prereq = array_fill(0, $n, 0);
        foreach ($relations as [$a, $b]) $prereq[$b - 1] |= 1 << ($a - 1);
        $full = (1 << $n) - 1;
        $inf = 1000000000;
        $dp = array_fill(0, 1 << $n, $inf);
        $dp[0] = 0;
        for ($mask = 0; $mask <= $full; $mask++) {
            if ($dp[$mask] === $inf) continue;
            $available = 0;
            for ($c = 0; $c < $n; $c++) {
                if ((($mask >> $c) & 1) === 0 && ($prereq[$c] & $mask) === $prereq[$c]) {
                    $available |= 1 << $c;
                }
            }
            $bitCount = substr_count(decbin($available), "1");
            $choices = [];
            if ($bitCount <= $k) {
                $choices[] = $available;
            } else {
                $sub = $available;
                while ($sub) {
                    if (substr_count(decbin($sub), "1") === $k) $choices[] = $sub;
                    $sub = ($sub - 1) & $available;
                }
            }
            foreach ($choices as $take) {
                $dp[$mask | $take] = min($dp[$mask | $take], $dp[$mask] + 1);
            }
        }
        return $dp[$full];
    }
}
''',
    "1496_path_crossing": r'''<?php
class Solution {
    function isPathCrossing($path) {
        $x = 0;
        $y = 0;
        $seen = ["0,0" => true];
        $move = ["N" => [0, 1], "S" => [0, -1], "E" => [1, 0], "W" => [-1, 0]];
        for ($i = 0; $i < strlen($path); $i++) {
            [$dx, $dy] = $move[$path[$i]];
            $x += $dx;
            $y += $dy;
            $key = "$x,$y";
            if (isset($seen[$key])) return true;
            $seen[$key] = true;
        }
        return false;
    }
}
''',
    "1497_check_if_array_pairs_are_divisible_by_k": r'''<?php
class Solution {
    function canArrange($arr, $k) {
        $count = array_fill(0, $k, 0);
        foreach ($arr as $x) {
            $r = $x % $k;
            if ($r < 0) $r += $k;
            $count[$r]++;
        }
        if ($count[0] % 2) return false;
        for ($r = 1; $r < $k; $r++) {
            if ($count[$r] !== $count[$k - $r]) return false;
        }
        return true;
    }
}
''',
    "1498_number_of_subsequences_that_satisfy_the_given_sum_condition": r'''<?php
class Solution {
    function numSubseq($nums, $target) {
        sort($nums);
        $mod = 1000000007;
        $left = 0;
        $right = count($nums) - 1;
        $ans = 0;
        $powers = array_fill(0, count($nums) + 1, 1);
        for ($i = 1; $i < count($powers); $i++) $powers[$i] = $powers[$i - 1] * 2 % $mod;
        while ($left <= $right) {
            if ($nums[$left] + $nums[$right] <= $target) {
                $ans = ($ans + $powers[$right - $left]) % $mod;
                $left++;
            } else {
                $right--;
            }
        }
        return $ans;
    }
}
''',
    "1499_max_value_of_equation": r'''<?php
class Solution {
    function findMaxValueOfEquation($points, $k) {
        $q = [];
        $ans = -10 ** 20;
        foreach ($points as [$x, $y]) {
            while ($q && $x - $q[0][0] > $k) array_shift($q);
            if ($q) $ans = max($ans, $x + $y + $q[0][1]);
            $value = $y - $x;
            while ($q && $q[count($q) - 1][1] <= $value) array_pop($q);
            $q[] = [$x, $value];
        }
        return $ans;
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

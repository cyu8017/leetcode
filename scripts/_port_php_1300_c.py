#!/usr/bin/env python3
"""Port PHP solutions for LeetCode stubs batch C (1382-1422)."""
from __future__ import annotations

import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SOLUTIONS: dict[str, str] = {
    "1382_balance_a_binary_search_tree": r'''<?php
class Solution {
    function balanceBST($root) {
        $nodes = [];
        $walk = function($x) use (&$walk, &$nodes) {
            if ($x) {
                $walk($x->left);
                $nodes[] = $x;
                $walk($x->right);
            }
        };
        $walk($root);
        $build = function($l, $r) use (&$build, $nodes) {
            if ($l >= $r) return null;
            $m = intdiv($l + $r, 2);
            $x = $nodes[$m];
            $x->left = $build($l, $m);
            $x->right = $build($m + 1, $r);
            return $x;
        };
        return $build(0, count($nodes));
    }
}
''',
    "1383_maximum_performance_of_a_team": r'''<?php
class Solution {
    function maxPerformance($n, $speed, $efficiency, $k) {
        $pairs = [];
        for ($i = 0; $i < $n; $i++) $pairs[] = [$efficiency[$i], $speed[$i]];
        usort($pairs, function($a, $b) { return $b[0] <=> $a[0]; });
        $h = new SplMinHeap();
        $total = 0;
        $ans = 0;
        foreach ($pairs as [$e, $s]) {
            $h->insert($s);
            $total += $s;
            if ($h->count() > $k) $total -= $h->extract();
            $ans = max($ans, $total * $e);
        }
        return $ans % 1000000007;
    }
}
''',
    "1385_find_the_distance_value_between_two_arrays": r'''<?php
class Solution {
    function findTheDistanceValue($arr1, $arr2, $d) {
        sort($arr2);
        $ans = 0;
        foreach ($arr1 as $x) {
            $lo = 0;
            $hi = count($arr2);
            while ($lo < $hi) {
                $mid = intdiv($lo + $hi, 2);
                if ($arr2[$mid] < $x) $lo = $mid + 1;
                else $hi = $mid;
            }
            $ok = true;
            if ($lo < count($arr2) && abs($arr2[$lo] - $x) <= $d) $ok = false;
            if ($lo > 0 && abs($arr2[$lo - 1] - $x) <= $d) $ok = false;
            if ($ok) $ans++;
        }
        return $ans;
    }
}
''',
    "1386_cinema_seat_allocation": r'''<?php
class Solution {
    function maxNumberOfFamilies($n, $reservedSeats) {
        $rows = [];
        foreach ($reservedSeats as [$r, $c]) {
            if ($c >= 2 && $c <= 9) $rows[$r] = ($rows[$r] ?? 0) | (1 << ($c - 2));
        }
        $ans = 2 * ($n - count($rows));
        foreach ($rows as $m) {
            $left = ($m & 0b00001111) === 0;
            $right = ($m & 0b11110000) === 0;
            $middle = ($m & 0b00111100) === 0;
            $ans += ($left && $right) ? 2 : (($left || $right || $middle) ? 1 : 0);
        }
        return $ans;
    }
}
''',
    "1387_sort_integers_by_the_power_value": r'''<?php
class Solution {
    private $memo = [];
    function getKth($lo, $hi, $k) {
        $this->memo = [];
        $vals = range($lo, $hi);
        usort($vals, function($a, $b) {
            $pa = $this->power($a);
            $pb = $this->power($b);
            if ($pa !== $pb) return $pa <=> $pb;
            return $a <=> $b;
        });
        return $vals[$k - 1];
    }
    private function power($x) {
        if ($x === 1) return 0;
        if (isset($this->memo[$x])) return $this->memo[$x];
        return $this->memo[$x] = 1 + $this->power($x % 2 === 0 ? intdiv($x, 2) : 3 * $x + 1);
    }
}
''',
    "1388_pizza_with_3n_slices": r'''<?php
class Solution {
    function maxSizeSlices($slices) {
        $k = intdiv(count($slices), 3);
        $line = function($a) use ($k) {
            $n = count($a);
            $dp = array_fill(0, $n + 2, array_fill(0, $k + 1, 0));
            for ($i = 0; $i < $n; $i++) {
                for ($j = 1; $j <= $k; $j++) {
                    $dp[$i + 2][$j] = max($dp[$i + 1][$j], $dp[$i][$j - 1] + $a[$i]);
                }
            }
            return $dp[$n + 1][$k];
        };
        return max($line(array_slice($slices, 0, -1)), $line(array_slice($slices, 1)));
    }
}
''',
    "1389_create_target_array_in_the_given_order": r'''<?php
class Solution {
    function createTargetArray($nums, $index) {
        $out = [];
        foreach ($nums as $i => $x) {
            array_splice($out, $index[$i], 0, [$x]);
        }
        return $out;
    }
}
''',
    "1390_four_divisors": r'''<?php
class Solution {
    function sumFourDivisors($nums) {
        $ans = 0;
        foreach ($nums as $x) {
            $ds = [];
            $lim = intval(sqrt($x));
            for ($d = 1; $d <= $lim; $d++) {
                if ($x % $d === 0) {
                    $ds[$d] = true;
                    $ds[intdiv($x, $d)] = true;
                }
                if (count($ds) > 4) break;
            }
            if (count($ds) === 4) $ans += array_sum(array_keys($ds));
        }
        return $ans;
    }
}
''',
    "1391_check_if_there_is_a_valid_path_in_a_grid": r'''<?php
class Solution {
    function hasValidPath($grid) {
        $dirs = [
            1 => [[0, -1], [0, 1]],
            2 => [[-1, 0], [1, 0]],
            3 => [[0, -1], [1, 0]],
            4 => [[0, 1], [1, 0]],
            5 => [[0, -1], [-1, 0]],
            6 => [[0, 1], [-1, 0]],
        ];
        $m = count($grid);
        $n = count($grid[0]);
        $seen = ["0,0" => true];
        $st = [[0, 0]];
        while ($st) {
            [$r, $c] = array_pop($st);
            if ($r === $m - 1 && $c === $n - 1) return true;
            foreach ($dirs[$grid[$r][$c]] as [$dr, $dc]) {
                $x = $r + $dr;
                $y = $c + $dc;
                $key = "$x,$y";
                if ($x >= 0 && $x < $m && $y >= 0 && $y < $n && !isset($seen[$key])) {
                    $ok = false;
                    foreach ($dirs[$grid[$x][$y]] as [$adr, $adc]) {
                        if ($adr === -$dr && $adc === -$dc) $ok = true;
                    }
                    if ($ok) {
                        $seen[$key] = true;
                        $st[] = [$x, $y];
                    }
                }
            }
        }
        return false;
    }
}
''',
    "1392_longest_happy_prefix": r'''<?php
class Solution {
    function longestPrefix($s) {
        $n = strlen($s);
        if (!$n) return "";
        $pi = array_fill(0, $n, 0);
        for ($i = 1; $i < $n; $i++) {
            $j = $pi[$i - 1];
            while ($j && $s[$i] !== $s[$j]) $j = $pi[$j - 1];
            if ($s[$i] === $s[$j]) $j++;
            $pi[$i] = $j;
        }
        return substr($s, 0, $pi[$n - 1]);
    }
}
''',
    "1394_find_lucky_integer_in_an_array": r'''<?php
class Solution {
    function findLucky($arr) {
        $c = array_count_values($arr);
        $ans = -1;
        foreach ($c as $x => $cnt) if ($x === $cnt) $ans = max($ans, $x);
        return $ans;
    }
}
''',
    "1395_count_number_of_teams": r'''<?php
class Solution {
    function numTeams($rating) {
        $ans = 0;
        $n = count($rating);
        for ($j = 0; $j < $n; $j++) {
            $x = $rating[$j];
            $ll = 0;
            for ($i = 0; $i < $j; $i++) if ($rating[$i] < $x) $ll++;
            $lg = $j - $ll;
            $rg = 0;
            for ($i = $j + 1; $i < $n; $i++) if ($rating[$i] > $x) $rg++;
            $rl = $n - $j - 1 - $rg;
            $ans += $ll * $rg + $lg * $rl;
        }
        return $ans;
    }
}
''',
    "1396_design_underground_system": r'''<?php
class UndergroundSystem {
    private $ins = [];
    private $stats = [];

    function __construct() {
        $this->ins = [];
        $this->stats = [];
    }

    function checkIn($id, $stationName, $t) {
        $this->ins[$id] = [$stationName, $t];
    }

    function checkOut($id, $stationName, $t) {
        [$start, $begin] = $this->ins[$id];
        unset($this->ins[$id]);
        $key = $start . "|" . $stationName;
        [$total, $count] = $this->stats[$key] ?? [0, 0];
        $this->stats[$key] = [$total + $t - $begin, $count + 1];
    }

    function getAverageTime($startStation, $endStation) {
        [$total, $count] = $this->stats[$startStation . "|" . $endStation];
        return $total / $count;
    }
}
''',
    "1397_find_all_good_strings": r'''<?php
class Solution {
    private $mod = 1000000007;
    private $n;
    private $s1;
    private $s2;
    private $evil;
    private $m;
    private $trans;
    private $memo;

    function findGoodStrings($n, $s1, $s2, $evil) {
        $this->n = $n;
        $this->s1 = $s1;
        $this->s2 = $s2;
        $this->evil = $evil;
        $this->m = strlen($evil);
        $pi = array_fill(0, $this->m, 0);
        for ($i = 1; $i < $this->m; $i++) {
            $j = $pi[$i - 1];
            while ($j && $evil[$i] !== $evil[$j]) $j = $pi[$j - 1];
            if ($evil[$i] === $evil[$j]) $j++;
            $pi[$i] = $j;
        }
        $this->trans = array_fill(0, $this->m, array_fill(0, 26, 0));
        for ($j = 0; $j < $this->m; $j++) {
            for ($x = 0; $x < 26; $x++) {
                $c = chr(97 + $x);
                $k = $j;
                while ($k && $evil[$k] !== $c) $k = $pi[$k - 1];
                if ($evil[$k] === $c) $k++;
                $this->trans[$j][$x] = $k;
            }
        }
        $this->memo = [];
        return $this->dp(0, 0, 1, 1);
    }

    private function dp($i, $j, $lo, $hi) {
        if ($j === $this->m) return 0;
        if ($i === $this->n) return 1;
        $key = "$i,$j,$lo,$hi";
        if (isset($this->memo[$key])) return $this->memo[$key];
        $a = $lo ? ord($this->s1[$i]) - 97 : 0;
        $b = $hi ? ord($this->s2[$i]) - 97 : 25;
        $ans = 0;
        for ($x = $a; $x <= $b; $x++) {
            $ans = ($ans + $this->dp($i + 1, $this->trans[$j][$x], $lo && $x === $a ? 1 : 0, $hi && $x === $b ? 1 : 0)) % $this->mod;
        }
        return $this->memo[$key] = $ans;
    }
}
''',
    "1399_count_largest_group": r'''<?php
class Solution {
    function countLargestGroup($n) {
        $c = [];
        for ($x = 1; $x <= $n; $x++) {
            $s = array_sum(array_map('intval', str_split(strval($x))));
            $c[$s] = ($c[$s] ?? 0) + 1;
        }
        $m = max($c);
        $ans = 0;
        foreach ($c as $v) if ($v === $m) $ans++;
        return $ans;
    }
}
''',
    "1400_construct_k_palindrome_strings": r'''<?php
class Solution {
    function canConstruct($s, $k) {
        if ($k > strlen($s)) return false;
        $c = array_count_values(str_split($s));
        $odd = 0;
        foreach ($c as $v) if ($v % 2) $odd++;
        return $odd <= $k;
    }
}
''',
    "1401_circle_and_rectangle_overlapping": r'''<?php
class Solution {
    function checkOverlap($radius, $xCenter, $yCenter, $x1, $y1, $x2, $y2) {
        $x = min(max($xCenter, $x1), $x2);
        $y = min(max($yCenter, $y1), $y2);
        return ($x - $xCenter) ** 2 + ($y - $yCenter) ** 2 <= $radius ** 2;
    }
}
''',
    "1402_reducing_dishes": r'''<?php
class Solution {
    function maxSatisfaction($satisfaction) {
        rsort($satisfaction);
        $total = 0;
        $answer = 0;
        foreach ($satisfaction as $value) {
            if ($total + $value <= 0) break;
            $total += $value;
            $answer += $total;
        }
        return $answer;
    }
}
''',
    "1403_minimum_subsequence_in_non_increasing_order": r'''<?php
class Solution {
    function minSubsequence($nums) {
        rsort($nums);
        $answer = [];
        $chosen = 0;
        $total = array_sum($nums);
        foreach ($nums as $value) {
            $answer[] = $value;
            $chosen += $value;
            if ($chosen > $total - $chosen) return $answer;
        }
        return $answer;
    }
}
''',
    "1404_number_of_steps_to_reduce_a_number_in_binary_representation_to_one": r'''<?php
class Solution {
    function numSteps($s) {
        $steps = 0;
        $carry = 0;
        for ($i = strlen($s) - 1; $i >= 1; $i--) {
            $value = intval($s[$i]) + $carry;
            if ($value === 1) {
                $steps += 2;
                $carry = 1;
            } else {
                $steps += 1;
            }
        }
        return $steps + $carry;
    }
}
''',
    "1405_longest_happy_string": r'''<?php
class Solution {
    function longestDiverseString($a, $b, $c) {
        $heap = new SplMaxHeap();
        foreach ([[$a, "a"], [$b, "b"], [$c, "c"]] as [$count, $char]) {
            if ($count) $heap->insert([$count, $char]);
        }
        $answer = "";
        while (!$heap->isEmpty()) {
            [$count, $char] = $heap->extract();
            $len = strlen($answer);
            if ($len >= 2 && $answer[$len - 1] === $char && $answer[$len - 2] === $char) {
                if ($heap->isEmpty()) break;
                [$count2, $char2] = $heap->extract();
                $answer .= $char2;
                if ($count2 - 1 > 0) $heap->insert([$count2 - 1, $char2]);
                $heap->insert([$count, $char]);
            } else {
                $answer .= $char;
                if ($count - 1 > 0) $heap->insert([$count - 1, $char]);
            }
        }
        return $answer;
    }
}
''',
    "1406_stone_game_iii": r'''<?php
class Solution {
    function stoneGameIII($stoneValue) {
        $n = count($stoneValue);
        $dp = array_fill(0, $n + 1, 0);
        for ($i = $n - 1; $i >= 0; $i--) {
            $take = 0;
            $dp[$i] = -10 ** 18;
            for ($j = $i; $j < min($i + 3, $n); $j++) {
                $take += $stoneValue[$j];
                $dp[$i] = max($dp[$i], $take - $dp[$j + 1]);
            }
        }
        if ($dp[0] > 0) return "Alice";
        if ($dp[0] < 0) return "Bob";
        return "Tie";
    }
}
''',
    "1408_string_matching_in_an_array": r'''<?php
class Solution {
    function stringMatching($words) {
        $answer = [];
        foreach ($words as $i => $word) {
            foreach ($words as $j => $other) {
                if ($i !== $j && strpos($other, $word) !== false) {
                    $answer[] = $word;
                    break;
                }
            }
        }
        return $answer;
    }
}
''',
    "1409_queries_on_a_permutation_with_key": r'''<?php
class Solution {
    function processQueries($queries, $m) {
        $values = range(1, $m);
        $answer = [];
        foreach ($queries as $query) {
            $index = array_search($query, $values);
            $answer[] = $index;
            array_splice($values, $index, 1);
            array_unshift($values, $query);
        }
        return $answer;
    }
}
''',
    "1410_html_entity_parser": r'''<?php
class Solution {
    function entityParser($text) {
        $entities = ["&quot;" => '"', "&apos;" => "'", "&amp;" => "&", "&gt;" => ">", "&lt;" => "<", "&frasl;" => "/"];
        // Replace &amp; last so other entities aren't broken; process longer first except amp last
        $order = ["&quot;", "&apos;", "&gt;", "&lt;", "&frasl;", "&amp;"];
        foreach ($order as $encoded) {
            $text = str_replace($encoded, $entities[$encoded], $text);
        }
        return $text;
    }
}
''',
    "1411_number_of_ways_to_paint_n_3_grid": r'''<?php
class Solution {
    function numOfWays($n) {
        $mod = 1000000007;
        $aba = 6;
        $abc = 6;
        for ($i = 1; $i < $n; $i++) {
            $naba = (3 * $aba + 2 * $abc) % $mod;
            $nabc = (2 * $aba + 2 * $abc) % $mod;
            $aba = $naba;
            $abc = $nabc;
        }
        return ($aba + $abc) % $mod;
    }
}
''',
    "1413_minimum_value_to_get_positive_step_by_step_sum": r'''<?php
class Solution {
    function minStartValue($nums) {
        $prefix = 0;
        $lowest = 0;
        foreach ($nums as $value) {
            $prefix += $value;
            $lowest = min($lowest, $prefix);
        }
        return 1 - $lowest;
    }
}
''',
    "1414_find_the_minimum_number_of_fibonacci_numbers_whose_sum_is_k": r'''<?php
class Solution {
    function findMinFibonacciNumbers($k) {
        $fib = [1, 1];
        while ($fib[count($fib) - 1] < $k) $fib[] = $fib[count($fib) - 1] + $fib[count($fib) - 2];
        $answer = 0;
        for ($i = count($fib) - 1; $i >= 0; $i--) {
            if ($fib[$i] <= $k) {
                $k -= $fib[$i];
                $answer++;
            }
        }
        return $answer;
    }
}
''',
    "1415_the_k_th_lexicographical_string_of_all_happy_strings_of_length_n": r'''<?php
class Solution {
    function getHappyString($n, $k) {
        $answer = [];
        $build = function($path) use (&$build, &$answer, $n) {
            if (strlen($path) === $n) {
                $answer[] = $path;
                return;
            }
            foreach (["a", "b", "c"] as $char) {
                if ($path === "" || $path[strlen($path) - 1] !== $char) $build($path . $char);
            }
        };
        $build("");
        return $k <= count($answer) ? $answer[$k - 1] : "";
    }
}
''',
    "1416_restore_the_array": r'''<?php
class Solution {
    function numberOfArrays($s, $k) {
        $mod = 1000000007;
        $n = strlen($s);
        $dp = array_fill(0, $n + 1, 0);
        $dp[$n] = 1;
        for ($i = $n - 1; $i >= 0; $i--) {
            if ($s[$i] === "0") continue;
            $value = 0;
            for ($j = $i; $j < $n; $j++) {
                $value = $value * 10 + intval($s[$j]);
                if ($value > $k) break;
                $dp[$i] = ($dp[$i] + $dp[$j + 1]) % $mod;
            }
        }
        return $dp[0];
    }
}
''',
    "1417_reformat_the_string": r'''<?php
class Solution {
    function reformat($s) {
        $letters = [];
        $digits = [];
        for ($i = 0; $i < strlen($s); $i++) {
            if (ctype_alpha($s[$i])) $letters[] = $s[$i];
            else $digits[] = $s[$i];
        }
        if (abs(count($letters) - count($digits)) > 1) return "";
        if (count($digits) >= count($letters)) {
            $tmp = $letters;
            $letters = $digits;
            $digits = $tmp;
        }
        $answer = "";
        foreach ($letters as $i => $char) {
            $answer .= $char;
            if ($i < count($digits)) $answer .= $digits[$i];
        }
        return $answer;
    }
}
''',
    "1418_display_table_of_food_orders_in_a_restaurant": r'''<?php
class Solution {
    function displayTable($orders) {
        $foods = [];
        $tables = [];
        $counts = [];
        foreach ($orders as [$customer, $table, $food]) {
            $foods[$food] = true;
            $tables[intval($table)] = true;
            $key = intval($table) . "|" . $food;
            $counts[$key] = ($counts[$key] ?? 0) + 1;
        }
        $foodList = array_keys($foods);
        sort($foodList);
        $tableList = array_keys($tables);
        sort($tableList);
        $result = [array_merge(["Table"], $foodList)];
        foreach ($tableList as $table) {
            $row = [strval($table)];
            foreach ($foodList as $food) $row[] = strval($counts[$table . "|" . $food] ?? 0);
            $result[] = $row;
        }
        return $result;
    }
}
''',
    "1419_minimum_number_of_frogs_croaking": r'''<?php
class Solution {
    function minNumberOfFrogs($croakOfFrogs) {
        $order = ["c" => 0, "r" => 1, "o" => 2, "a" => 3, "k" => 4];
        $counts = array_fill(0, 5, 0);
        $active = 0;
        $answer = 0;
        for ($i = 0; $i < strlen($croakOfFrogs); $i++) {
            $char = $croakOfFrogs[$i];
            if (!isset($order[$char])) return -1;
            $idx = $order[$char];
            if ($idx && $counts[$idx - 1] === 0) return -1;
            if ($idx) $counts[$idx - 1]--;
            $counts[$idx]++;
            if ($idx === 0) {
                $active++;
                $answer = max($answer, $active);
            } elseif ($idx === 4) {
                $counts[4]--;
                $active--;
            }
        }
        return $active === 0 ? $answer : -1;
    }
}
''',
    "1420_build_array_where_you_can_find_the_maximum_exactly_k_comparisons": r'''<?php
class Solution {
    function numOfArrays($n, $m, $k) {
        $mod = 1000000007;
        $dp = array_fill(0, $k + 1, array_fill(0, $m + 1, 0));
        for ($maximum = 1; $maximum <= $m; $maximum++) $dp[1][$maximum] = 1;
        for ($len = 1; $len < $n; $len++) {
            $nxt = array_fill(0, $k + 1, array_fill(0, $m + 1, 0));
            for ($cost = 1; $cost <= $k; $cost++) {
                $prefix = 0;
                for ($maximum = 1; $maximum <= $m; $maximum++) {
                    $prefix = ($prefix + $dp[$cost - 1][$maximum - 1]) % $mod;
                    $nxt[$cost][$maximum] = ($maximum * $dp[$cost][$maximum] + $prefix) % $mod;
                }
            }
            $dp = $nxt;
        }
        return array_sum($dp[$k]) % $mod;
    }
}
''',
    "1422_maximum_score_after_splitting_a_string": r'''<?php
class Solution {
    function maxScore($s) {
        $ones = substr_count($s, "1");
        $leftZeros = 0;
        $answer = 0;
        for ($i = 0; $i < strlen($s) - 1; $i++) {
            if ($s[$i] === "0") $leftZeros++;
            else $ones--;
            $answer = max($answer, $leftZeros + $ones);
        }
        return $answer;
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

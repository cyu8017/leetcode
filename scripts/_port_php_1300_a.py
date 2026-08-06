#!/usr/bin/env python3
"""Port PHP solutions for LeetCode stubs batch A (1300-1340 range)."""
from __future__ import annotations

import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SOLUTIONS: dict[str, str] = {
    "1300_sum_of_mutated_array_closest_to_target": r'''<?php
class Solution {
    function findBestValue($arr, $target) {
        $lo = 0;
        $hi = max($arr);
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi, 2);
            $sum = 0;
            foreach ($arr as $x) $sum += min($x, $mid);
            if ($sum < $target) $lo = $mid + 1;
            else $hi = $mid;
        }
        $before = 0;
        $after = 0;
        foreach ($arr as $x) {
            $before += min($x, $lo - 1);
            $after += min($x, $lo);
        }
        return $target - $before <= $after - $target ? $lo - 1 : $lo;
    }
}
''',
    "1301_number_of_paths_with_max_score": r'''<?php
class Solution {
    function pathsWithMaxScore($board) {
        $mod = 1000000007;
        $n = count($board);
        $score = array_fill(0, $n, array_fill(0, $n, -1));
        $ways = array_fill(0, $n, array_fill(0, $n, 0));
        $score[$n - 1][$n - 1] = 0;
        $ways[$n - 1][$n - 1] = 1;
        for ($r = $n - 1; $r >= 0; $r--) {
            for ($c = $n - 1; $c >= 0; $c--) {
                if ($board[$r][$c] === "X" || ($r === $n - 1 && $c === $n - 1)) continue;
                $best = -1;
                $count = 0;
                foreach ([[$r + 1, $c], [$r, $c + 1], [$r + 1, $c + 1]] as [$nr, $nc]) {
                    if ($nr < $n && $nc < $n && $score[$nr][$nc] >= 0) {
                        if ($score[$nr][$nc] > $best) {
                            $best = $score[$nr][$nc];
                            $count = $ways[$nr][$nc];
                        } elseif ($score[$nr][$nc] === $best) {
                            $count = ($count + $ways[$nr][$nc]) % $mod;
                        }
                    }
                }
                if ($best >= 0) {
                    $ch = $board[$r][$c];
                    $score[$r][$c] = $best + (ctype_digit($ch) ? intval($ch) : 0);
                    $ways[$r][$c] = $count;
                }
            }
        }
        return [max($score[0][0], 0), $ways[0][0]];
    }
}
''',
    "1302_deepest_leaves_sum": r'''<?php
class Solution {
    function deepestLeavesSum($root) {
        $level = [$root];
        $answer = 0;
        while ($level) {
            $answer = 0;
            $next = [];
            foreach ($level as $node) {
                $answer += $node->val;
                if ($node->left) $next[] = $node->left;
                if ($node->right) $next[] = $node->right;
            }
            $level = $next;
        }
        return $answer;
    }
}
''',
    "1304_find_n_unique_integers_sum_up_to_zero": r'''<?php
class Solution {
    function sumZero($n) {
        $answer = [];
        for ($value = 1; $value <= intdiv($n, 2); $value++) {
            $answer[] = -$value;
            $answer[] = $value;
        }
        if ($n % 2) $answer[] = 0;
        return $answer;
    }
}
''',
    "1305_all_elements_in_two_binary_search_trees": r'''<?php
class Solution {
    function getAllElements($root1, $root2) {
        $inorder = function($root) use (&$inorder) {
            if (!$root) return [];
            return array_merge($inorder($root->left), [$root->val], $inorder($root->right));
        };
        $a = $inorder($root1);
        $b = $inorder($root2);
        $answer = [];
        $i = 0;
        $j = 0;
        while ($i < count($a) || $j < count($b)) {
            if ($j === count($b) || ($i < count($a) && $a[$i] <= $b[$j])) $answer[] = $a[$i++];
            else $answer[] = $b[$j++];
        }
        return $answer;
    }
}
''',
    "1306_jump_game_iii": r'''<?php
class Solution {
    function canReach($arr, $start) {
        $stack = [$start];
        $seen = [];
        while ($stack) {
            $i = array_pop($stack);
            if (isset($seen[$i]) || $i < 0 || $i >= count($arr)) continue;
            if ($arr[$i] === 0) return true;
            $seen[$i] = true;
            $stack[] = $i - $arr[$i];
            $stack[] = $i + $arr[$i];
        }
        return false;
    }
}
''',
    "1307_verbal_arithmetic_puzzle": r'''<?php
class Solution {
    private $words;
    private $result;
    private $value = [];
    private $used;
    private $leading = [];
    private $width;

    function isSolvable($words, $result) {
        $this->words = $words;
        $this->result = $result;
        $this->value = [];
        $this->used = array_fill(0, 10, false);
        $this->leading = [];
        $maxWord = 0;
        $letters = [];
        foreach ($words as $w) {
            $maxWord = max($maxWord, strlen($w));
            foreach (str_split($w) as $c) $letters[$c] = true;
            if (strlen($w) > 1) $this->leading[$w[0]] = true;
        }
        foreach (str_split($result) as $c) $letters[$c] = true;
        if (strlen($result) > 1) $this->leading[$result[0]] = true;
        if ($maxWord > strlen($result) || count($letters) > 10) return false;
        $this->width = strlen($result);
        return $this->solve(0, 0, 0);
    }

    private function solve($column, $row, $total) {
        if ($column === $this->width) return $total === 0;
        if ($row < count($this->words)) {
            if ($column >= strlen($this->words[$row])) return $this->solve($column, $row + 1, $total);
            $ch = $this->words[$row][strlen($this->words[$row]) - 1 - $column];
            if (array_key_exists($ch, $this->value)) return $this->solve($column, $row + 1, $total + $this->value[$ch]);
            for ($digit = 0; $digit < 10; $digit++) {
                if (!$this->used[$digit] && ($digit !== 0 || !isset($this->leading[$ch]))) {
                    $this->value[$ch] = $digit;
                    $this->used[$digit] = true;
                    if ($this->solve($column, $row + 1, $total + $digit)) return true;
                    $this->used[$digit] = false;
                    unset($this->value[$ch]);
                }
            }
            return false;
        }
        $ch = $this->result[strlen($this->result) - 1 - $column];
        $digit = $total % 10;
        $carry = intdiv($total, 10);
        if (array_key_exists($ch, $this->value)) {
            return $this->value[$ch] === $digit && $this->solve($column + 1, 0, $carry);
        }
        if ($this->used[$digit] || ($digit === 0 && isset($this->leading[$ch]))) return false;
        $this->value[$ch] = $digit;
        $this->used[$digit] = true;
        $ok = $this->solve($column + 1, 0, $carry);
        $this->used[$digit] = false;
        unset($this->value[$ch]);
        return $ok;
    }
}
''',
    "1309_decrypt_string_from_alphabet_to_integer_mapping": r'''<?php
class Solution {
    function freqAlphabets($s) {
        $answer = [];
        $i = strlen($s) - 1;
        while ($i >= 0) {
            if ($s[$i] === "#") {
                $answer[] = chr(96 + intval(substr($s, $i - 2, 2)));
                $i -= 3;
            } else {
                $answer[] = chr(96 + intval($s[$i]));
                $i -= 1;
            }
        }
        return implode("", array_reverse($answer));
    }
}
''',
    "1310_xor_queries_of_a_subarray": r'''<?php
class Solution {
    function xorQueries($arr, $queries) {
        $prefix = [0];
        foreach ($arr as $value) $prefix[] = $prefix[count($prefix) - 1] ^ $value;
        $answer = [];
        foreach ($queries as $q) {
            $answer[] = $prefix[$q[1] + 1] ^ $prefix[$q[0]];
        }
        return $answer;
    }
}
''',
    "1311_get_watched_videos_by_your_friends": r'''<?php
class Solution {
    function watchedVideosByFriends($watchedVideos, $friends, $id, $level) {
        $queue = [[$id, 0]];
        $seen = [$id => true];
        $people = [];
        while ($queue) {
            [$person, $distance] = array_shift($queue);
            if ($distance === $level) {
                $people[] = $person;
                continue;
            }
            foreach ($friends[$person] as $friend) {
                if (!isset($seen[$friend])) {
                    $seen[$friend] = true;
                    $queue[] = [$friend, $distance + 1];
                }
            }
        }
        $counts = [];
        foreach ($people as $person) {
            foreach ($watchedVideos[$person] as $video) {
                $counts[$video] = ($counts[$video] ?? 0) + 1;
            }
        }
        $keys = array_keys($counts);
        usort($keys, function($a, $b) use ($counts) {
            if ($counts[$a] !== $counts[$b]) return $counts[$a] <=> $counts[$b];
            return $a <=> $b;
        });
        return $keys;
    }
}
''',
    "1312_minimum_insertion_steps_to_make_a_string_palindrome": r'''<?php
class Solution {
    function minInsertions($s) {
        $n = strlen($s);
        $dp = array_fill(0, $n, 0);
        for ($left = $n - 2; $left >= 0; $left--) {
            $diagonal = 0;
            for ($right = $left + 1; $right < $n; $right++) {
                $old = $dp[$right];
                if ($s[$left] === $s[$right]) $dp[$right] = $diagonal;
                else $dp[$right] = 1 + min($dp[$right], $dp[$right - 1]);
                $diagonal = $old;
            }
        }
        return $n ? $dp[$n - 1] : 0;
    }
}
''',
    "1313_decompress_run_length_encoded_list": r'''<?php
class Solution {
    function decompressRLElist($nums) {
        $answer = [];
        for ($i = 0; $i < count($nums); $i += 2) {
            for ($j = 0; $j < $nums[$i]; $j++) $answer[] = $nums[$i + 1];
        }
        return $answer;
    }
}
''',
    "1314_matrix_block_sum": r'''<?php
class Solution {
    function matrixBlockSum($mat, $k) {
        $m = count($mat);
        $n = count($mat[0]);
        $prefix = array_fill(0, $m + 1, array_fill(0, $n + 1, 0));
        for ($r = 0; $r < $m; $r++) {
            for ($c = 0; $c < $n; $c++) {
                $prefix[$r + 1][$c + 1] = $mat[$r][$c] + $prefix[$r][$c + 1] + $prefix[$r + 1][$c] - $prefix[$r][$c];
            }
        }
        $answer = array_fill(0, $m, array_fill(0, $n, 0));
        for ($r = 0; $r < $m; $r++) {
            for ($c = 0; $c < $n; $c++) {
                $r1 = max(0, $r - $k);
                $c1 = max(0, $c - $k);
                $r2 = min($m, $r + $k + 1);
                $c2 = min($n, $c + $k + 1);
                $answer[$r][$c] = $prefix[$r2][$c2] - $prefix[$r1][$c2] - $prefix[$r2][$c1] + $prefix[$r1][$c1];
            }
        }
        return $answer;
    }
}
''',
    "1315_sum_of_nodes_with_even_valued_grandparent": r'''<?php
class Solution {
    function sumEvenGrandparent($root) {
        $dfs = function($node, $parent, $grandparent) use (&$dfs) {
            if (!$node) return 0;
            $add = ($grandparent && $grandparent->val % 2 === 0) ? $node->val : 0;
            return $add + $dfs($node->left, $node, $parent) + $dfs($node->right, $node, $parent);
        };
        return $dfs($root, null, null);
    }
}
''',
    "1316_distinct_echo_substrings": r'''<?php
class Solution {
    function distinctEchoSubstrings($text) {
        $n = strlen($text);
        $mod1 = 1000000007;
        $mod2 = 1000000009;
        $base = 911382323;
        $h1 = array_fill(0, $n + 1, 0);
        $h2 = array_fill(0, $n + 1, 0);
        $p1 = array_fill(0, $n + 1, 1);
        $p2 = array_fill(0, $n + 1, 1);
        for ($i = 0; $i < $n; $i++) {
            $code = ord($text[$i]);
            $h1[$i + 1] = ($h1[$i] * $base + $code) % $mod1;
            $h2[$i + 1] = ($h2[$i] * $base + $code) % $mod2;
            $p1[$i + 1] = ($p1[$i] * $base) % $mod1;
            $p2[$i + 1] = ($p2[$i] * $base) % $mod2;
        }
        $hashed = function($left, $right) use ($h1, $h2, $p1, $p2, $mod1, $mod2) {
            $length = $right - $left;
            return [
                (($h1[$right] - $h1[$left] * $p1[$length]) % $mod1 + $mod1) % $mod1,
                (($h2[$right] - $h2[$left] * $p2[$length]) % $mod2 + $mod2) % $mod2,
            ];
        };
        $echoes = [];
        for ($half = 1; $half <= intdiv($n, 2); $half++) {
            for ($left = 0; $left <= $n - 2 * $half; $left++) {
                $a = $hashed($left, $left + $half);
                $b = $hashed($left + $half, $left + 2 * $half);
                if ($a[0] === $b[0] && $a[1] === $b[1]) {
                    $full = $hashed($left, $left + 2 * $half);
                    $echoes[(2 * $half) . "," . $full[0] . "," . $full[1]] = true;
                }
            }
        }
        return count($echoes);
    }
}
''',
    "1317_convert_integer_to_the_sum_of_two_no_zero_integers": r'''<?php
class Solution {
    function getNoZeroIntegers($n) {
        $valid = function($value) {
            return strpos(strval($value), "0") === false;
        };
        for ($first = 1; $first < $n; $first++) {
            if ($valid($first) && $valid($n - $first)) return [$first, $n - $first];
        }
        return [];
    }
}
''',
    "1318_minimum_flips_to_make_a_or_b_equal_to_c": r'''<?php
class Solution {
    function minFlips($a, $b, $c) {
        $flips = 0;
        while ($a || $b || $c) {
            $x = $a & 1;
            $y = $b & 1;
            $z = $c & 1;
            $flips += $z === 0 ? $x + $y : (($x === 0 && $y === 0) ? 1 : 0);
            $a >>= 1;
            $b >>= 1;
            $c >>= 1;
        }
        return $flips;
    }
}
''',
    "1319_number_of_operations_to_make_network_connected": r'''<?php
class Solution {
    function makeConnected($n, $connections) {
        if (count($connections) < $n - 1) return -1;
        $parent = range(0, $n - 1);
        $find = function($x) use (&$parent, &$find) {
            while ($x !== $parent[$x]) {
                $parent[$x] = $parent[$parent[$x]];
                $x = $parent[$x];
            }
            return $x;
        };
        foreach ($connections as [$a, $b]) {
            $ra = $find($a);
            $rb = $find($b);
            if ($ra !== $rb) $parent[$ra] = $rb;
        }
        $roots = [];
        for ($i = 0; $i < $n; $i++) $roots[$find($i)] = true;
        return count($roots) - 1;
    }
}
''',
    "1320_minimum_distance_to_type_a_word_using_two_fingers": r'''<?php
class Solution {
    function minimumDistance($word) {
        $distance = function($a, $b) {
            if ($a === 26) return 0;
            return abs(intdiv($a, 6) - intdiv($b, 6)) + abs($a % 6 - $b % 6);
        };
        $letters = [];
        for ($i = 0; $i < strlen($word); $i++) $letters[] = ord($word[$i]) - 65;
        $dp = [26 => 0];
        $previous = $letters[0];
        for ($idx = 1; $idx < count($letters); $idx++) {
            $current = $letters[$idx];
            $nxt = [];
            foreach ($dp as $free => $cost) {
                $v1 = $cost + $distance($previous, $current);
                $nxt[$free] = min($nxt[$free] ?? PHP_INT_MAX, $v1);
                $v2 = $cost + $distance($free, $current);
                $nxt[$previous] = min($nxt[$previous] ?? PHP_INT_MAX, $v2);
            }
            $dp = $nxt;
            $previous = $current;
        }
        return min($dp);
    }
}
''',
    "1323_maximum_69_number": r'''<?php
class Solution {
    function maximum69Number($num) {
        $s = strval($num);
        $pos = strpos($s, "6");
        if ($pos !== false) $s[$pos] = "9";
        return intval($s);
    }
}
''',
    "1324_print_words_vertically": r'''<?php
class Solution {
    function printVertically($s) {
        $words = explode(" ", $s);
        $maxLen = 0;
        foreach ($words as $w) $maxLen = max($maxLen, strlen($w));
        $answer = [];
        for ($i = 0; $i < $maxLen; $i++) {
            $row = "";
            foreach ($words as $word) {
                $row .= $i < strlen($word) ? $word[$i] : " ";
            }
            $answer[] = rtrim($row);
        }
        return $answer;
    }
}
''',
    "1325_delete_leaves_with_a_given_value": r'''<?php
class Solution {
    function removeLeafNodes($root, $target) {
        if (!$root) return null;
        $root->left = $this->removeLeafNodes($root->left, $target);
        $root->right = $this->removeLeafNodes($root->right, $target);
        if (!$root->left && !$root->right && $root->val === $target) return null;
        return $root;
    }
}
''',
    "1326_minimum_number_of_taps_to_open_to_water_a_garden": r'''<?php
class Solution {
    function minTaps($n, $ranges) {
        $farthest = array_fill(0, $n + 1, 0);
        foreach ($ranges as $center => $radius) {
            $left = max(0, $center - $radius);
            $right = min($n, $center + $radius);
            $farthest[$left] = max($farthest[$left], $right);
        }
        $taps = 0;
        $end = 0;
        $reach = 0;
        for ($position = 0; $position < $n; $position++) {
            $reach = max($reach, $farthest[$position]);
            if ($position === $end) {
                if ($reach <= $position) return -1;
                $taps++;
                $end = $reach;
            }
        }
        return $taps;
    }
}
''',
    "1328_break_a_palindrome": r'''<?php
class Solution {
    function breakPalindrome($palindrome) {
        if (strlen($palindrome) === 1) return "";
        $chars = str_split($palindrome);
        $n = count($chars);
        for ($i = 0; $i < intdiv($n, 2); $i++) {
            if ($chars[$i] !== "a") {
                $chars[$i] = "a";
                return implode("", $chars);
            }
        }
        $chars[$n - 1] = "b";
        return implode("", $chars);
    }
}
''',
    "1329_sort_the_matrix_diagonally": r'''<?php
class Solution {
    function diagonalSort($mat) {
        $diagonals = [];
        foreach ($mat as $r => $row) {
            foreach ($row as $c => $value) {
                $diagonals[$r - $c][] = $value;
            }
        }
        foreach ($diagonals as $k => $values) {
            rsort($diagonals[$k]);
        }
        foreach ($mat as $r => $row) {
            foreach ($row as $c => $_) {
                $mat[$r][$c] = array_pop($diagonals[$r - $c]);
            }
        }
        return $mat;
    }
}
''',
    "1330_reverse_subarray_to_maximize_array_value": r'''<?php
class Solution {
    function maxValueAfterReverse($nums) {
        $base = 0;
        $n = count($nums);
        for ($i = 0; $i < $n - 1; $i++) $base += abs($nums[$i] - $nums[$i + 1]);
        $gain = 0;
        $low = 1000000000;
        $high = -1000000000;
        for ($i = 0; $i < $n - 1; $i++) {
            $a = $nums[$i];
            $b = $nums[$i + 1];
            $gain = max($gain, abs($nums[0] - $b) - abs($a - $b), abs($nums[$n - 1] - $a) - abs($a - $b));
            $low = min($low, max($a, $b));
            $high = max($high, min($a, $b));
        }
        return $base + max($gain, 2 * ($high - $low));
    }
}
''',
    "1331_rank_transform_of_an_array": r'''<?php
class Solution {
    function arrayRankTransform($arr) {
        $uniq = array_values(array_unique($arr));
        sort($uniq);
        $rank = [];
        foreach ($uniq as $i => $value) $rank[$value] = $i + 1;
        $answer = [];
        foreach ($arr as $value) $answer[] = $rank[$value];
        return $answer;
    }
}
''',
    "1332_remove_palindromic_subsequences": r'''<?php
class Solution {
    function removePalindromeSub($s) {
        if ($s === "") return 0;
        return $s === strrev($s) ? 1 : 2;
    }
}
''',
    "1333_filter_restaurants_by_vegan_friendly_price_and_distance": r'''<?php
class Solution {
    function filterRestaurants($restaurants, $veganFriendly, $maxPrice, $maxDistance) {
        $valid = [];
        foreach ($restaurants as $row) {
            if ((!$veganFriendly || $row[2]) && $row[3] <= $maxPrice && $row[4] <= $maxDistance) {
                $valid[] = $row;
            }
        }
        usort($valid, function($a, $b) {
            if ($a[1] !== $b[1]) return $b[1] <=> $a[1];
            return $b[0] <=> $a[0];
        });
        $answer = [];
        foreach ($valid as $row) $answer[] = $row[0];
        return $answer;
    }
}
''',
    "1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance": r'''<?php
class Solution {
    function findTheCity($n, $edges, $distanceThreshold) {
        $inf = 10 ** 15;
        $dist = array_fill(0, $n, array_fill(0, $n, $inf));
        for ($i = 0; $i < $n; $i++) $dist[$i][$i] = 0;
        foreach ($edges as [$a, $b, $weight]) {
            $dist[$a][$b] = $weight;
            $dist[$b][$a] = $weight;
        }
        for ($k = 0; $k < $n; $k++) {
            for ($i = 0; $i < $n; $i++) {
                for ($j = 0; $j < $n; $j++) {
                    $dist[$i][$j] = min($dist[$i][$j], $dist[$i][$k] + $dist[$k][$j]);
                }
            }
        }
        $bestCity = 0;
        $bestCount = $n;
        for ($city = 0; $city < $n; $city++) {
            $count = 0;
            foreach ($dist[$city] as $d) {
                if ($d <= $distanceThreshold) $count++;
            }
            if ($count < $bestCount || ($count === $bestCount && $city > $bestCity)) {
                $bestCount = $count;
                $bestCity = $city;
            }
        }
        return $bestCity;
    }
}
''',
    "1335_minimum_difficulty_of_a_job_schedule": r'''<?php
class Solution {
    function minDifficulty($jobDifficulty, $d) {
        $n = count($jobDifficulty);
        if ($n < $d) return -1;
        $dp = array_fill(0, $n, 1000000000);
        $hardest = 0;
        for ($i = 0; $i < $n; $i++) {
            $hardest = max($hardest, $jobDifficulty[$i]);
            $dp[$i] = $hardest;
        }
        for ($day = 1; $day < $d; $day++) {
            $nxt = array_fill(0, $n, 1000000000);
            for ($end = $day; $end < $n; $end++) {
                $hardest = 0;
                for ($start = $end; $start >= $day; $start--) {
                    $hardest = max($hardest, $jobDifficulty[$start]);
                    $nxt[$end] = min($nxt[$end], $dp[$start - 1] + $hardest);
                }
            }
            $dp = $nxt;
        }
        return $dp[$n - 1];
    }
}
''',
    "1337_the_k_weakest_rows_in_a_matrix": r'''<?php
class Solution {
    function kWeakestRows($mat, $k) {
        $idx = range(0, count($mat) - 1);
        usort($idx, function($i, $j) use ($mat) {
            $si = array_sum($mat[$i]);
            $sj = array_sum($mat[$j]);
            if ($si !== $sj) return $si <=> $sj;
            return $i <=> $j;
        });
        return array_slice($idx, 0, $k);
    }
}
''',
    "1338_reduce_array_size_to_the_half": r'''<?php
class Solution {
    function minSetSize($arr) {
        $counts = array_count_values($arr);
        rsort($counts);
        $removed = 0;
        $need = intdiv(count($arr), 2);
        $answer = 0;
        foreach ($counts as $c) {
            $removed += $c;
            $answer++;
            if ($removed >= $need) return $answer;
        }
        return $answer;
    }
}
''',
    "1339_maximum_product_of_splitted_binary_tree": r'''<?php
class Solution {
    function maxProduct($root) {
        $mod = 1000000007;
        $total = 0;
        $sum = function($node) use (&$sum, &$total) {
            if (!$node) return 0;
            return $node->val + $sum($node->left) + $sum($node->right);
        };
        $total = $sum($root);
        $best = 0;
        $dfs = function($node) use (&$dfs, &$best, $total) {
            if (!$node) return 0;
            $s = $node->val + $dfs($node->left) + $dfs($node->right);
            $best = max($best, $s * ($total - $s));
            return $s;
        };
        $dfs($root);
        return $best % $mod;
    }
}
''',
    "1340_jump_game_v": r'''<?php
class Solution {
    function maxJumps($arr, $d) {
        $n = count($arr);
        $dp = array_fill(0, $n, 1);
        $order = [];
        for ($i = 0; $i < $n; $i++) $order[] = [$arr[$i], $i];
        usort($order, function($a, $b) { return $a[0] <=> $b[0]; });
        foreach ($order as [, $i]) {
            foreach ([-1, 1] as $step) {
                $j = $i + $step;
                while ($j >= 0 && $j < $n && abs($j - $i) <= $d && $arr[$j] < $arr[$i]) {
                    $dp[$i] = max($dp[$i], 1 + $dp[$j]);
                    $j += $step;
                }
            }
        }
        return max($dp);
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

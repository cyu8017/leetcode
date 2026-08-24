#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
SOLUTIONS: dict[str, str] = {}


def add(name: str, content: str) -> None:
    SOLUTIONS[name] = content.strip() + "\n"


TREE = """class TreeNode {
    public $val = 0;
    public $left = null;
    public $right = null;
    function __construct($val = 0, $left = null, $right = null) {
        $this->val = $val;
        $this->left = $left;
        $this->right = $right;
    }
}
"""

add("0730_count_different_palindromic_subsequences", r"""<?php
// LeetCode 0730 - Count Different Palindromic Subsequences
// https://leetcode.com/problems/count-different-palindromic-subsequences/

class Solution {
    function countPalindromicSubsequences($s) {
        $mod = 1000000007;
        $n = strlen($s);
        $dp = array_fill(0, $n, array_fill(0, $n, 0));
        for ($i = 0; $i < $n; $i++) $dp[$i][$i] = 1;
        for ($length = 2; $length <= $n; $length++) {
            for ($i = 0; $i <= $n - $length; $i++) {
                $j = $i + $length - 1;
                if ($s[$i] !== $s[$j]) $dp[$i][$j] = $dp[$i + 1][$j] + $dp[$i][$j - 1] - $dp[$i + 1][$j - 1];
                else {
                    $left = $i + 1;
                    $right = $j - 1;
                    while ($left <= $right && $s[$left] !== $s[$i]) $left++;
                    while ($left <= $right && $s[$right] !== $s[$i]) $right--;
                    if ($left > $right) $dp[$i][$j] = $dp[$i + 1][$j - 1] * 2 + 2;
                    else if ($left === $right) $dp[$i][$j] = $dp[$i + 1][$j - 1] * 2 + 1;
                    else $dp[$i][$j] = $dp[$i + 1][$j - 1] * 2 - $dp[$left + 1][$right - 1];
                }
                $dp[$i][$j] = (($dp[$i][$j] % $mod) + $mod) % $mod;
            }
        }
        return $dp[0][$n - 1];
    }
}
""")

add("0731_my_calendar_ii", r"""<?php
// LeetCode 0731 - My Calendar II
// https://leetcode.com/problems/my-calendar-ii/

class MyCalendarTwo {
    private $booked = [];
    private $overlaps = [];

    function __construct() {
        $this->booked = [];
        $this->overlaps = [];
    }

    function book($startTime, $endTime) {
        foreach ($this->overlaps as $o) {
            if ($o[0] < $endTime && $startTime < $o[1]) return false;
        }
        foreach ($this->booked as $b) {
            if ($b[0] < $endTime && $startTime < $b[1]) {
                $this->overlaps[] = [max($b[0], $startTime), min($b[1], $endTime)];
            }
        }
        $this->booked[] = [$startTime, $endTime];
        return true;
    }
}
""")

add("0732_my_calendar_iii", r"""<?php
// LeetCode 0732 - My Calendar III
// https://leetcode.com/problems/my-calendar-iii/

class MyCalendarThree {
    private $delta = [];

    function __construct() {
        $this->delta = [];
    }

    function book($startTime, $endTime) {
        $this->delta[$startTime] = ($this->delta[$startTime] ?? 0) + 1;
        $this->delta[$endTime] = ($this->delta[$endTime] ?? 0) - 1;
        $current = 0;
        $best = 0;
        $keys = array_keys($this->delta);
        sort($keys);
        foreach ($keys as $key) {
            $current += $this->delta[$key];
            $best = max($best, $current);
        }
        return $best;
    }
}
""")

add("0733_flood_fill", r"""<?php
// LeetCode 0733 - Flood Fill
// https://leetcode.com/problems/flood-fill/

class Solution {
    function floodFill($image, $sr, $sc, $color) {
        $original = $image[$sr][$sc];
        if ($original === $color) return $image;
        $dfs = function ($r, $c) use (&$dfs, &$image, $original, $color) {
            if ($r < 0 || $r >= count($image) || $c < 0 || $c >= count($image[0]) || $image[$r][$c] !== $original) return;
            $image[$r][$c] = $color;
            $dfs($r + 1, $c);
            $dfs($r - 1, $c);
            $dfs($r, $c + 1);
            $dfs($r, $c - 1);
        };
        $dfs($sr, $sc);
        return $image;
    }
}
""")

add("0734_sentence_similarity", r"""<?php
// LeetCode 0734 - Sentence Similarity
// https://leetcode.com/problems/sentence-similarity/

class Solution {
    function areSentencesSimilar($sentence1, $sentence2, $similarPairs) {
        if (count($sentence1) !== count($sentence2)) return false;
        $pairs = [];
        foreach ($similarPairs as $pair) {
            $pairs[$pair[0] . '#' . $pair[1]] = true;
            $pairs[$pair[1] . '#' . $pair[0]] = true;
        }
        $n = count($sentence1);
        for ($i = 0; $i < $n; $i++) {
            if ($sentence1[$i] !== $sentence2[$i] && !isset($pairs[$sentence1[$i] . '#' . $sentence2[$i]])) return false;
        }
        return true;
    }
}
""")

add("0735_asteroid_collision", r"""<?php
// LeetCode 0735 - Asteroid Collision
// https://leetcode.com/problems/asteroid-collision/

class Solution {
    function asteroidCollision($asteroids) {
        $stack = [];
        foreach ($asteroids as $asteroid) {
            $alive = true;
            while ($alive && count($stack) > 0 && $asteroid < 0 && $stack[count($stack) - 1] > 0) {
                if ($stack[count($stack) - 1] < -$asteroid) { array_pop($stack); continue; }
                if ($stack[count($stack) - 1] === -$asteroid) array_pop($stack);
                $alive = false;
            }
            if ($alive) $stack[] = $asteroid;
        }
        return $stack;
    }
}
""")

add("0736_parse_lisp_expression", r"""<?php
// LeetCode 0736 - Parse Lisp Expression
// https://leetcode.com/problems/parse-lisp-expression/

class Solution {
    function evaluate($expression) {
        $tokens = [];
        $cur = '';
        $len = strlen($expression);
        for ($ti = 0; $ti < $len; $ti++) {
            $ch = $expression[$ti];
            if ($ch === '(' || $ch === ')') {
                if (strlen($cur) > 0) { $tokens[] = $cur; $cur = ''; }
                $tokens[] = $ch;
            } else if (preg_match('/\s/', $ch)) {
                if (strlen($cur) > 0) { $tokens[] = $cur; $cur = ''; }
            } else $cur .= $ch;
        }
        if (strlen($cur) > 0) $tokens[] = $cur;
        $pos = 0;
        $parse = function ($env) use (&$parse, &$tokens, &$pos) {
            $token = $tokens[$pos];
            if ($token !== '(') {
                $pos++;
                if (($token[0] >= '0' && $token[0] <= '9') || ($token[0] === '-' && strlen($token) > 1))
                    return intval($token, 10);
                for ($i = count($env) - 1; $i >= 0; $i--) {
                    if (array_key_exists($token, $env[$i])) return $env[$i][$token];
                }
                return 0;
            }
            $pos++;
            $op = $tokens[$pos++];
            if ($op === 'let') {
                $env[] = [];
                $ei = count($env) - 1;
                while ($tokens[$pos] !== ')') {
                    if ($tokens[$pos] === '(' || $tokens[$pos + 1] === ')') {
                        $value = $parse($env);
                        $pos++;
                        array_pop($env);
                        return $value;
                    }
                    $v = $tokens[$pos++];
                    $env[$ei][$v] = $parse($env);
                    $ei = count($env) - 1;
                }
            }
            if ($op === 'add') {
                $left = $parse($env);
                $right = $parse($env);
                $pos++;
                return $left + $right;
            }
            if ($op === 'mult') {
                $left = $parse($env);
                $right = $parse($env);
                $pos++;
                return $left * $right;
            }
            return 0;
        };
        return $parse([]);
    }
}
""")

add("0737_sentence_similarity_ii", r"""<?php
// LeetCode 0737 - Sentence Similarity II
// https://leetcode.com/problems/sentence-similarity-ii/

class Solution {
    function areSentencesSimilarTwo($sentence1, $sentence2, $similarPairs) {
        if (count($sentence1) !== count($sentence2)) return false;
        $parent = [];
        $find = function ($x) use (&$parent) {
            if (!array_key_exists($x, $parent)) $parent[$x] = $x;
            while ($parent[$x] !== $x) {
                $parent[$x] = $parent[$parent[$x]];
                $x = $parent[$x];
            }
            return $x;
        };
        $unite = function ($a, $b) use (&$find, &$parent) {
            $parent[$find($a)] = $find($b);
        };
        foreach ($similarPairs as $pair) $unite($pair[0], $pair[1]);
        $n = count($sentence1);
        for ($i = 0; $i < $n; $i++) {
            if ($find($sentence1[$i]) !== $find($sentence2[$i])) return false;
        }
        return true;
    }
}
""")

add("0738_monotone_increasing_digits", r"""<?php
// LeetCode 0738 - Monotone Increasing Digits
// https://leetcode.com/problems/monotone-increasing-digits/

class Solution {
    function monotoneIncreasingDigits($n) {
        $digits = str_split((string)$n);
        $mark = count($digits);
        for ($i = count($digits) - 1; $i > 0; $i--) {
            if ($digits[$i] < $digits[$i - 1]) {
                $digits[$i - 1] = chr(ord($digits[$i - 1]) - 1);
                $mark = $i;
            }
        }
        for ($i = $mark; $i < count($digits); $i++) $digits[$i] = '9';
        return intval(implode('', $digits), 10);
    }
}
""")

add("0739_daily_temperatures", r"""<?php
// LeetCode 0739 - Daily Temperatures
// https://leetcode.com/problems/daily-temperatures/

class Solution {
    function dailyTemperatures($temperatures) {
        $n = count($temperatures);
        $answer = array_fill(0, $n, 0);
        $stack = [];
        for ($i = 0; $i < $n; $i++) {
            while (count($stack) > 0 && $temperatures[$stack[count($stack) - 1]] < $temperatures[$i]) {
                $prev = array_pop($stack);
                $answer[$prev] = $i - $prev;
            }
            $stack[] = $i;
        }
        return $answer;
    }
}
""")

add("0740_delete_and_earn", r"""<?php
// LeetCode 0740 - Delete and Earn
// https://leetcode.com/problems/delete-and-earn/

class Solution {
    function deleteAndEarn($nums) {
        if (count($nums) === 0) return 0;
        $maxNum = 0;
        foreach ($nums as $num) $maxNum = max($maxNum, $num);
        $points = array_fill(0, $maxNum + 1, 0);
        foreach ($nums as $num) $points[$num] += $num;
        $take = 0;
        $skip = 0;
        foreach ($points as $value) {
            $newTake = $skip + $value;
            $newSkip = max($skip, $take);
            $take = $newTake;
            $skip = $newSkip;
        }
        return max($take, $skip);
    }
}
""")

add("0741_cherry_pickup", r"""<?php
// LeetCode 0741 - Cherry Pickup
// https://leetcode.com/problems/cherry-pickup/

class Solution {
    function cherryPickup($grid) {
        $n = count($grid);
        $UNSET = -INF;
        $memo = array_fill(0, $n, array_fill(0, $n, array_fill(0, $n, $UNSET)));
        $dp = function ($r1, $c1, $c2) use (&$dp, &$memo, &$grid, $n, $UNSET) {
            $r2 = $r1 + $c1 - $c2;
            if ($r1 >= $n || $c1 >= $n || $r2 >= $n || $c2 >= $n || $grid[$r1][$c1] === -1 || $grid[$r2][$c2] === -1)
                return -1000000000;
            if ($r1 === $n - 1 && $c1 === $n - 1) return $grid[$r1][$c1];
            if ($memo[$r1][$c1][$c2] !== $UNSET) return $memo[$r1][$c1][$c2];
            $cherries = $grid[$r1][$c1];
            if ($r1 !== $r2 || $c1 !== $c2) $cherries += $grid[$r2][$c2];
            $cherries += max(
                max($dp($r1 + 1, $c1, $c2), $dp($r1, $c1 + 1, $c2)),
                max($dp($r1 + 1, $c1, $c2 + 1), $dp($r1, $c1 + 1, $c2 + 1))
            );
            $memo[$r1][$c1][$c2] = $cherries;
            return $cherries;
        };
        return max(0, $dp(0, 0, 0));
    }
}
""")

add("0742_closest_leaf_in_a_binary_tree", """<?php
// LeetCode 0742 - Closest Leaf in a Binary Tree
// https://leetcode.com/problems/closest-leaf-in-a-binary-tree/

""" + TREE + r"""
class Solution {
    function findClosestLeaf($root, $k) {
        $graph = [];
        $leaves = [];
        $build = function ($node, $parent) use (&$build, &$graph, &$leaves) {
            if ($node === null) return;
            if (!isset($graph[$node->val])) $graph[$node->val] = [];
            if ($parent !== null) {
                if (!isset($graph[$parent->val])) $graph[$parent->val] = [];
                $graph[$node->val][] = $parent->val;
                $graph[$parent->val][] = $node->val;
            }
            if ($node->left === null && $node->right === null) $leaves[$node->val] = true;
            $build($node->right, $node);
            $build($node->left, $node);
        };
        $build($root, null);
        $q = [$k];
        $seen = [$k => true];
        while (count($q) > 0) {
            $value = array_shift($q);
            if (isset($leaves[$value])) return $value;
            if (!isset($graph[$value])) continue;
            foreach ($graph[$value] as $neighbor) {
                if (!isset($seen[$neighbor])) {
                    $seen[$neighbor] = true;
                    $q[] = $neighbor;
                }
            }
        }
        return -1;
    }
}
""")

add("0743_network_delay_time", r"""<?php
// LeetCode 0743 - Network Delay Time
// https://leetcode.com/problems/network-delay-time/

class Solution {
    function networkDelayTime($times, $n, $k) {
        $graph = array_fill(0, $n + 1, []);
        foreach ($times as $edge) $graph[$edge[0]][] = [$edge[1], $edge[2]];
        $INF = intdiv(PHP_INT_MAX, 4);
        $dist = array_fill(0, $n + 1, $INF);
        $dist[$k] = 0;
        $heap = [[0, $k]];
        while (count($heap) > 0) {
            usort($heap, function ($a, $b) { return $a[0] - $b[0]; });
            $item = array_shift($heap);
            $d = $item[0];
            $node = $item[1];
            if ($d > $dist[$node]) continue;
            foreach ($graph[$node] as $e) {
                $nd = $d + $e[1];
                if ($nd < $dist[$e[0]]) {
                    $dist[$e[0]] = $nd;
                    $heap[] = [$nd, $e[0]];
                }
            }
        }
        $ans = 0;
        for ($i = 1; $i <= $n; $i++) $ans = max($ans, $dist[$i]);
        return $ans === $INF ? -1 : $ans;
    }
}
""")

add("0744_find_smallest_letter_greater_than_target", r"""<?php
// LeetCode 0744 - Find Smallest Letter Greater Than Target
// https://leetcode.com/problems/find-smallest-letter-greater-than-target/

class Solution {
    function nextGreatestLetter($letters, $target) {
        $left = 0;
        $right = count($letters);
        while ($left < $right) {
            $mid = $left + intdiv($right - $left, 2);
            if ($letters[$mid] <= $target) $left = $mid + 1;
            else $right = $mid;
        }
        return $letters[$left % count($letters)];
    }
}
""")

add("0745_prefix_and_suffix_search", r"""<?php
// LeetCode 0745 - Prefix and Suffix Search
// https://leetcode.com/problems/prefix-and-suffix-search/

class WordFilter {
    private $lookup = [];

    function __construct($words) {
        $this->lookup = [];
        for ($index = 0; $index < count($words); $index++) {
            $word = $words[$index];
            $size = strlen($word);
            for ($i = 0; $i <= $size; $i++) {
                for ($j = 0; $j <= $size; $j++) {
                    $this->lookup[substr($word, 0, $i) . '#' . substr($word, $j)] = $index;
                }
            }
        }
    }

    function f($pref, $suff) {
        $key = $pref . '#' . $suff;
        return array_key_exists($key, $this->lookup) ? $this->lookup[$key] : -1;
    }
}
""")

add("0746_min_cost_climbing_stairs", r"""<?php
// LeetCode 0746 - Min Cost Climbing Stairs
// https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution {
    function minCostClimbingStairs($cost) {
        $a = 0;
        $b = 0;
        for ($i = count($cost) - 1; $i >= 0; $i--) {
            $nextA = $cost[$i] + min($a, $b);
            $b = $a;
            $a = $nextA;
        }
        return min($a, $b);
    }
}
""")

add("0747_largest_number_at_least_twice_of_others", r"""<?php
// LeetCode 0747 - Largest Number At Least Twice of Others
// https://leetcode.com/problems/largest-number-at-least-twice-of-others/

class Solution {
    function dominantIndex($nums) {
        $first = -1;
        $second = -1;
        $index = -1;
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            if ($nums[$i] > $first) { $second = $first; $first = $nums[$i]; $index = $i; }
            else if ($nums[$i] > $second) $second = $nums[$i];
        }
        return $first >= 2 * $second ? $index : -1;
    }
}
""")

add("0748_shortest_completing_word", r"""<?php
// LeetCode 0748 - Shortest Completing Word
// https://leetcode.com/problems/shortest-completing-word/

class Solution {
    function shortestCompletingWord($licensePlate, $words) {
        $need = array_fill(0, 26, 0);
        $plen = strlen($licensePlate);
        for ($i = 0; $i < $plen; $i++) {
            $lower = strtolower($licensePlate[$i]);
            if ($lower >= 'a' && $lower <= 'z') $need[ord($lower) - 97]++;
        }
        $best = '';
        foreach ($words as $word) {
            $counts = array_fill(0, 26, 0);
            $wlen = strlen($word);
            for ($i = 0; $i < $wlen; $i++) $counts[ord($word[$i]) - 97]++;
            $ok = true;
            for ($i = 0; $i < 26; $i++) if ($counts[$i] < $need[$i]) { $ok = false; break; }
            if ($ok && (strlen($best) === 0 || $wlen < strlen($best))) $best = $word;
        }
        return $best;
    }
}
""")

add("0749_contain_virus", r"""<?php
// LeetCode 0749 - Contain Virus
// https://leetcode.com/problems/contain-virus/

class Solution {
    function containVirus($isInfected) {
        $m = count($isInfected);
        $n = count($isInfected[0]);
        $walls = 0;
        $pack = function ($r, $c) { return $r * 1000000 + $c; };
        $unpack = function ($key) { return [intdiv($key, 1000000), $key % 1000000]; };
        while (true) {
            $seen = [];
            $regions = [];
            $frontiers = [];
            $perimeters = [];
            for ($i = 0; $i < $m; $i++) {
                for ($j = 0; $j < $n; $j++) {
                    $key = $pack($i, $j);
                    if ($isInfected[$i][$j] === 1 && !isset($seen[$key])) {
                        $stack = [[$i, $j]];
                        $seen[$key] = true;
                        $region = [];
                        $frontier = [];
                        $perimeter = 0;
                        $dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]];
                        while (count($stack) > 0) {
                            $cell = array_pop($stack);
                            $r = $cell[0];
                            $c = $cell[1];
                            $region[$pack($r, $c)] = true;
                            foreach ($dirs as $d) {
                                $nr = $r + $d[0];
                                $nc = $c + $d[1];
                                if ($nr < 0 || $nr >= $m || $nc < 0 || $nc >= $n) continue;
                                $nk = $pack($nr, $nc);
                                if ($isInfected[$nr][$nc] === 1) {
                                    if (!isset($seen[$nk])) {
                                        $seen[$nk] = true;
                                        $stack[] = [$nr, $nc];
                                    }
                                } else if ($isInfected[$nr][$nc] === 0) {
                                    $frontier[$nk] = true;
                                    $perimeter++;
                                }
                            }
                        }
                        $regions[] = $region;
                        $frontiers[] = $frontier;
                        $perimeters[] = $perimeter;
                    }
                }
            }
            if (count($regions) === 0) break;
            $quarantine = 0;
            for ($i = 1; $i < count($regions); $i++)
                if (count($frontiers[$i]) > count($frontiers[$quarantine])) $quarantine = $i;
            if (count($frontiers[$quarantine]) === 0) break;
            $walls += $perimeters[$quarantine];
            foreach ($regions[$quarantine] as $cell => $_) {
                [$r, $c] = $unpack($cell);
                $isInfected[$r][$c] = -1;
            }
            for ($index = 0; $index < count($frontiers); $index++) {
                if ($index === $quarantine) continue;
                foreach ($frontiers[$index] as $cell => $_) {
                    [$r, $c] = $unpack($cell);
                    $isInfected[$r][$c] = 1;
                }
            }
        }
        return $walls;
    }
}
""")

add("0750_number_of_corner_rectangles", r"""<?php
// LeetCode 0750 - Number Of Corner Rectangles
// https://leetcode.com/problems/number-of-corner-rectangles/

class Solution {
    function countCornerRectangles($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        $ans = 0;
        for ($i = 0; $i < $m; $i++) {
            for ($j = $i + 1; $j < $m; $j++) {
                $count = 0;
                for ($c = 0; $c < $n; $c++) if ($grid[$i][$c] === 1 && $grid[$j][$c] === 1) $count++;
                $ans += intdiv($count * ($count - 1), 2);
            }
        }
        return $ans;
    }
}
""")

add("0751_ip_to_cidr", r"""<?php
// LeetCode 0751 - IP to CIDR
// https://leetcode.com/problems/ip-to-cidr/

class Solution {
    function ipToCIDR($ip, $n) {
        $ipToInt = function ($value) {
            $result = 0;
            foreach (explode('.', $value) as $part) $result = $result * 256 + intval($part, 10);
            return $result;
        };
        $intToIp = function ($value) {
            return implode('.', [
                intdiv($value, 16777216) % 256,
                intdiv($value, 65536) % 256,
                intdiv($value, 256) % 256,
                $value % 256
            ]);
        };
        $bitLength = function ($value) {
            $len = 0;
            while ($value > 0) { $value = intdiv($value, 2); $len++; }
            return $len;
        };
        $start = $ipToInt($ip);
        $answer = [];
        while ($n > 0) {
            $lowbit = $start === 0 ? (1 << 32) : ($start & -$start);
            while ($lowbit > $n) $lowbit = intdiv($lowbit, 2);
            $mask = 32 - ($bitLength($lowbit) - 1);
            $answer[] = $intToIp($start) . '/' . $mask;
            $start += $lowbit;
            $n -= $lowbit;
        }
        return $answer;
    }
}
""")

add("0752_open_the_lock", r"""<?php
// LeetCode 0752 - Open the Lock
// https://leetcode.com/problems/open-the-lock/

class Solution {
    function openLock($deadends, $target) {
        $dead = [];
        foreach ($deadends as $d) $dead[$d] = true;
        if (isset($dead['0000'])) return -1;
        $q = ['0000'];
        $stepsQ = [0];
        $seen = ['0000' => true];
        while (count($q) > 0) {
            $state = array_shift($q);
            $steps = array_shift($stepsQ);
            if ($state === $target) return $steps;
            $chars = str_split($state);
            for ($i = 0; $i < 4; $i++) {
                $digit = ord($chars[$i]) - 48;
                foreach ([-1, 1] as $delta) {
                    $chars[$i] = (string)(($digit + $delta + 10) % 10);
                    $nxt = implode('', $chars);
                    $chars[$i] = (string)$digit;
                    if (!isset($seen[$nxt]) && !isset($dead[$nxt])) {
                        $seen[$nxt] = true;
                        $q[] = $nxt;
                        $stepsQ[] = $steps + 1;
                    }
                }
            }
        }
        return -1;
    }
}
""")

add("0753_cracking_the_safe", r"""<?php
// LeetCode 0753 - Cracking the Safe
// https://leetcode.com/problems/cracking-the-safe/

class Solution {
    function crackSafe($n, $k) {
        $seen = [];
        $path = [];
        $start = '';
        for ($i = 0; $i < $n - 1; $i++) $start .= '0';
        $dfs = function ($node) use (&$dfs, &$seen, &$path, $k) {
            for ($d = 0; $d < $k; $d++) {
                $digit = (string)$d;
                $edge = $node . $digit;
                if (!isset($seen[$edge])) {
                    $seen[$edge] = true;
                    $dfs(substr($edge, 1));
                    $path[] = $digit;
                }
            }
        };
        $dfs($start);
        return implode('', $path) . $start;
    }
}
""")

add("0754_reach_a_number", r"""<?php
// LeetCode 0754 - Reach a Number
// https://leetcode.com/problems/reach-a-number/

class Solution {
    function reachNumber($target) {
        $target = abs($target);
        $steps = 0;
        $total = 0;
        while ($total < $target || ($total - $target) % 2 !== 0) {
            $steps++;
            $total += $steps;
        }
        return $steps;
    }
}
""")

add("0755_pour_water", r"""<?php
// LeetCode 0755 - Pour Water
// https://leetcode.com/problems/pour-water/

class Solution {
    function pourWater($heights, $volume, $k) {
        for ($v = 0; $v < $volume; $v++) {
            $index = $k;
            for ($i = $k - 1; $i >= 0; $i--) {
                if ($heights[$i] > $heights[$index]) break;
                if ($heights[$i] < $heights[$index]) $index = $i;
            }
            if ($index !== $k) { $heights[$index]++; continue; }
            $index = $k;
            for ($i = $k + 1; $i < count($heights); $i++) {
                if ($heights[$i] > $heights[$index]) break;
                if ($heights[$i] < $heights[$index]) $index = $i;
            }
            $heights[$index]++;
        }
        return $heights;
    }
}
""")

add("0756_pyramid_transition_matrix", r"""<?php
// LeetCode 0756 - Pyramid Transition Matrix
// https://leetcode.com/problems/pyramid-transition-matrix/

class Solution {
    function pyramidTransition($bottom, $allowed) {
        $transitions = [];
        $memo = [];
        foreach ($allowed as $triple) {
            $key = substr($triple, 0, 2);
            if (!isset($transitions[$key])) $transitions[$key] = [];
            $transitions[$key][] = $triple[2];
        }
        $dfs = null;
        $build = function ($index, $options, $path) use (&$build, &$dfs) {
            if ($index === count($options)) return $dfs($path);
            foreach ($options[$index] as $ch) {
                if ($build($index + 1, $options, $path . $ch)) return true;
            }
            return false;
        };
        $dfs = function ($row) use (&$dfs, &$build, &$transitions, &$memo) {
            if (strlen($row) === 1) return true;
            if (array_key_exists($row, $memo)) return $memo[$row];
            $options = [];
            $rlen = strlen($row);
            for ($i = 0; $i + 1 < $rlen; $i++) {
                $key = substr($row, $i, 2);
                if (!isset($transitions[$key])) {
                    $memo[$row] = false;
                    return false;
                }
                $options[] = $transitions[$key];
            }
            $ok = $build(0, $options, '');
            $memo[$row] = $ok;
            return $ok;
        };
        return $dfs($bottom);
    }
}
""")

add("0757_set_intersection_size_at_least_two", r"""<?php
// LeetCode 0757 - Set Intersection Size At Least Two
// https://leetcode.com/problems/set-intersection-size-at-least-two/

class Solution {
    function intersectionSizeTwo($intervals) {
        usort($intervals, function ($a, $b) {
            return $a[1] !== $b[1] ? $a[1] - $b[1] : $a[0] - $b[0];
        });
        $size = 0;
        $first = -1;
        $second = -1;
        foreach ($intervals as $interval) {
            $left = $interval[0];
            $right = $interval[1];
            if ($left <= $first) continue;
            if ($left <= $second) { $size++; $first = $second; $second = $right; }
            else { $size += 2; $first = $right - 1; $second = $right; }
        }
        return $size;
    }
}
""")

add("0758_bold_words_in_string", r"""<?php
// LeetCode 0758 - Bold Words in String
// https://leetcode.com/problems/bold-words-in-string/

class Solution {
    function boldWords($words, $s) {
        $n = strlen($s);
        $bold = array_fill(0, $n, false);
        foreach ($words as $word) {
            $start = strpos($s, $word);
            while ($start !== false) {
                $wlen = strlen($word);
                for ($i = $start; $i < $start + $wlen; $i++) $bold[$i] = true;
                $start = strpos($s, $word, $start + 1);
            }
        }
        $parts = '';
        $i2 = 0;
        while ($i2 < $n) {
            if ($bold[$i2]) {
                $parts .= '**';
                while ($i2 < $n && $bold[$i2]) $parts .= $s[$i2++];
                $parts .= '**';
            } else $parts .= $s[$i2++];
        }
        return $parts;
    }
}
""")

add("0759_employee_free_time", r"""<?php
// LeetCode 0759 - Employee Free Time
// https://leetcode.com/problems/employee-free-time/

class Solution {
    function employeeFreeTime($schedule) {
        $intervals = [];
        foreach ($schedule as $employee)
            foreach ($employee as $item)
                $intervals[] = [$item[0], $item[1]];
        usort($intervals, function ($a, $b) { return $a[0] - $b[0]; });
        $merged = [];
        foreach ($intervals as $iv) {
            if (count($merged) === 0 || $merged[count($merged) - 1][1] < $iv[0]) $merged[] = $iv;
            else $merged[count($merged) - 1][1] = max($merged[count($merged) - 1][1], $iv[1]);
        }
        $result = [];
        for ($i = 1; $i < count($merged); $i++)
            $result[] = [$merged[$i - 1][1], $merged[$i][0]];
        return $result;
    }
}
""")

add("0760_find_anagram_mappings", r"""<?php
// LeetCode 0760 - Find Anagram Mappings
// https://leetcode.com/problems/find-anagram-mappings/

class Solution {
    function anagramMappings($nums1, $nums2) {
        $positions = [];
        $n2 = count($nums2);
        for ($i = 0; $i < $n2; $i++) {
            if (!isset($positions[$nums2[$i]])) $positions[$nums2[$i]] = [];
            $positions[$nums2[$i]][] = $i;
        }
        $n1 = count($nums1);
        $result = array_fill(0, $n1, 0);
        for ($i = 0; $i < $n1; $i++) {
            $result[$i] = array_shift($positions[$nums1[$i]]);
        }
        return $result;
    }
}
""")

add("0761_special_binary_string", r"""<?php
// LeetCode 0761 - Special Binary String
// https://leetcode.com/problems/special-binary-string/

class Solution {
    function makeLargestSpecial($s) {
        $parts = [];
        $balance = 0;
        $start = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $balance += $s[$i] === '1' ? 1 : -1;
            if ($balance === 0) {
                $parts[] = '1' . $this->makeLargestSpecial(substr($s, $start + 1, $i - $start - 1)) . '0';
                $start = $i + 1;
            }
        }
        rsort($parts);
        return implode('', $parts);
    }
}
""")

add("0762_prime_number_of_set_bits_in_binary_representation", r"""<?php
// LeetCode 0762 - Prime Number of Set Bits in Binary Representation
// https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/

class Solution {
    function countPrimeSetBits($left, $right) {
        $primes = [2 => true, 3 => true, 5 => true, 7 => true, 11 => true, 13 => true, 17 => true, 19 => true];
        $ans = 0;
        for ($num = $left; $num <= $right; $num++) {
            $bits = 0;
            $x = $num;
            while ($x > 0) { $bits += $x & 1; $x >>= 1; }
            if (isset($primes[$bits])) $ans++;
        }
        return $ans;
    }
}
""")

add("0763_partition_labels", r"""<?php
// LeetCode 0763 - Partition Labels
// https://leetcode.com/problems/partition-labels/

class Solution {
    function partitionLabels($s) {
        $last = array_fill(0, 26, 0);
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) $last[ord($s[$i]) - 97] = $i;
        $start = 0;
        $end = 0;
        $answer = [];
        for ($i = 0; $i < $n; $i++) {
            $end = max($end, $last[ord($s[$i]) - 97]);
            if ($i === $end) {
                $answer[] = $end - $start + 1;
                $start = $i + 1;
            }
        }
        return $answer;
    }
}
""")

add("0764_largest_plus_sign", r"""<?php
// LeetCode 0764 - Largest Plus Sign
// https://leetcode.com/problems/largest-plus-sign/

class Solution {
    function orderOfLargestPlusSign($n, $mines) {
        $banned = [];
        foreach ($mines as $mine) $banned[$mine[0] * $n + $mine[1]] = true;
        $arms = array_fill(0, $n, array_fill(0, $n, 0));
        $best = 0;
        for ($r = 0; $r < $n; $r++) {
            $count = 0;
            for ($c = 0; $c < $n; $c++) {
                $count = isset($banned[$r * $n + $c]) ? 0 : $count + 1;
                $arms[$r][$c] = $count;
            }
            $count = 0;
            for ($c = $n - 1; $c >= 0; $c--) {
                $count = isset($banned[$r * $n + $c]) ? 0 : $count + 1;
                $arms[$r][$c] = min($arms[$r][$c], $count);
            }
        }
        for ($c = 0; $c < $n; $c++) {
            $count = 0;
            for ($r = 0; $r < $n; $r++) {
                $count = isset($banned[$r * $n + $c]) ? 0 : $count + 1;
                $arms[$r][$c] = min($arms[$r][$c], $count);
            }
            $count = 0;
            for ($r = $n - 1; $r >= 0; $r--) {
                $count = isset($banned[$r * $n + $c]) ? 0 : $count + 1;
                $arms[$r][$c] = min($arms[$r][$c], $count);
                $best = max($best, $arms[$r][$c]);
            }
        }
        return $best;
    }
}
""")

add("0765_couples_holding_hands", r"""<?php
// LeetCode 0765 - Couples Holding Hands
// https://leetcode.com/problems/couples-holding-hands/

class Solution {
    function minSwapsCouples($row) {
        $pos = [];
        $n = count($row);
        for ($i = 0; $i < $n; $i++) $pos[$row[$i]] = $i;
        $swaps = 0;
        for ($i = 0; $i < $n; $i += 2) {
            $partner = $row[$i] ^ 1;
            if ($row[$i + 1] === $partner) continue;
            $j = $pos[$partner];
            $pos[$row[$i + 1]] = $j;
            $row[$j] = $row[$i + 1];
            $row[$i + 1] = $partner;
            $pos[$partner] = $i + 1;
            $swaps++;
        }
        return $swaps;
    }
}
""")

add("0766_toeplitz_matrix", r"""<?php
// LeetCode 0766 - Toeplitz Matrix
// https://leetcode.com/problems/toeplitz-matrix/

class Solution {
    function isToeplitzMatrix($matrix) {
        for ($r = 1; $r < count($matrix); $r++) {
            for ($c = 1; $c < count($matrix[0]); $c++) {
                if ($matrix[$r][$c] !== $matrix[$r - 1][$c - 1]) return false;
            }
        }
        return true;
    }
}
""")

add("0767_reorganize_string", r"""<?php
// LeetCode 0767 - Reorganize String
// https://leetcode.com/problems/reorganize-string/

class Solution {
    function reorganizeString($s) {
        $freq = array_fill(0, 26, 0);
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) $freq[ord($s[$i]) - 97]++;
        $heap = [];
        for ($i = 0; $i < 26; $i++) {
            if ($freq[$i] > 0) $heap[] = [$freq[$i], $i];
        }
        usort($heap, function ($a, $b) { return $b[0] - $a[0]; });
        if (count($heap) > 0 && $heap[0][0] > intdiv($n + 1, 2)) return '';
        $result = '';
        while (count($heap) >= 2) {
            usort($heap, function ($a, $b) { return $b[0] - $a[0]; });
            $x = array_shift($heap);
            $y = array_shift($heap);
            $result .= chr(97 + $x[1]);
            $result .= chr(97 + $y[1]);
            if (--$x[0] > 0) $heap[] = $x;
            if (--$y[0] > 0) $heap[] = $y;
        }
        if (count($heap) > 0) $result .= chr(97 + $heap[0][1]);
        return $result;
    }
}
""")

add("0768_max_chunks_to_make_sorted_ii", r"""<?php
// LeetCode 0768 - Max Chunks To Make Sorted II
// https://leetcode.com/problems/max-chunks-to-make-sorted-ii/

class Solution {
    function maxChunksToSorted($arr) {
        $n = count($arr);
        $maxLeft = array_fill(0, $n, 0);
        $minRight = array_fill(0, $n, 0);
        $maxLeft[0] = $arr[0];
        for ($i = 1; $i < $n; $i++) $maxLeft[$i] = max($maxLeft[$i - 1], $arr[$i]);
        $minRight[$n - 1] = $arr[$n - 1];
        for ($i = $n - 2; $i >= 0; $i--) $minRight[$i] = min($minRight[$i + 1], $arr[$i]);
        $chunks = 1;
        for ($i = 0; $i < $n - 1; $i++) if ($maxLeft[$i] <= $minRight[$i + 1]) $chunks++;
        return $chunks;
    }
}
""")

add("0769_max_chunks_to_make_sorted", r"""<?php
// LeetCode 0769 - Max Chunks To Make Sorted
// https://leetcode.com/problems/max-chunks-to-make-sorted/

class Solution {
    function maxChunksToSorted($arr) {
        $chunks = 0;
        $maxSoFar = 0;
        $n = count($arr);
        for ($i = 0; $i < $n; $i++) {
            $maxSoFar = max($maxSoFar, $arr[$i]);
            if ($maxSoFar === $i) $chunks++;
        }
        return $chunks;
    }
}
""")

add("0770_basic_calculator_iv", r"""<?php
// LeetCode 0770 - Basic Calculator IV
// https://leetcode.com/problems/basic-calculator-iv/

class Solution {
    function basicCalculatorIV($expression, $evalvars, $evalints) {
        $values = [];
        for ($i = 0; $i < count($evalvars); $i++) $values[$evalvars[$i]] = $evalints[$i];
        $tokens = [];
        $cur = '';
        $elen = strlen($expression);
        for ($ti = 0; $ti < $elen; $ti++) {
            $ch = $expression[$ti];
            if ($ch === '(' || $ch === ')') {
                if (strlen($cur) > 0) { $tokens[] = $cur; $cur = ''; }
                $tokens[] = $ch;
            } else if (preg_match('/\s/', $ch)) {
                if (strlen($cur) > 0) { $tokens[] = $cur; $cur = ''; }
            } else $cur .= $ch;
        }
        if (strlen($cur) > 0) $tokens[] = $cur;
        $pos = 0;

        $keyOf = function ($items) { return implode("\0", $items); };
        $itemsOf = function ($key) { return $key === '' ? [] : explode("\0", $key); };

        $clean = function ($poly) {
            foreach ($poly as $k => $v) if ($v === 0) unset($poly[$k]);
            return $poly;
        };

        $add = function ($left, $right) use ($clean) {
            $result = $left;
            foreach ($right as $k => $v) $result[$k] = ($result[$k] ?? 0) + $v;
            return $clean($result);
        };

        $negate = function ($poly) {
            $result = [];
            foreach ($poly as $k => $v) $result[$k] = -$v;
            return $result;
        };

        $mul = function ($left, $right) use ($clean, $itemsOf, $keyOf) {
            $result = [];
            foreach ($left as $lk => $lv) {
                foreach ($right as $rk => $rv) {
                    $keyList = array_merge($itemsOf($lk), $itemsOf($rk));
                    sort($keyList);
                    $key = $keyOf($keyList);
                    $result[$key] = ($result[$key] ?? 0) + $lv * $rv;
                }
            }
            return $clean($result);
        };

        $atom = function ($token) use ($values, $clean, $keyOf) {
            $poly = [];
            if (preg_match('/[a-zA-Z]/', $token[0])) {
                if (array_key_exists($token, $values)) $poly[''] = $values[$token];
                else $poly[$keyOf([$token])] = 1;
            } else $poly[''] = intval($token, 10);
            return $clean($poly);
        };

        $parseExpr = null;
        $parseFactor = function () use (&$parseFactor, &$parseExpr, &$tokens, &$pos, $atom) {
            if ($tokens[$pos] === '(') {
                $pos++;
                $poly = $parseExpr();
                $pos++;
                return $poly;
            }
            return $atom($tokens[$pos++]);
        };

        $parseTerm = function () use (&$parseFactor, &$tokens, &$pos, $mul) {
            $poly = $parseFactor();
            while ($pos < count($tokens) && $tokens[$pos] === '*') {
                $pos++;
                $poly = $mul($poly, $parseFactor());
            }
            return $poly;
        };

        $parseExpr = function () use (&$parseTerm, &$tokens, &$pos, $add, $negate) {
            $poly = $parseTerm();
            while ($pos < count($tokens) && ($tokens[$pos] === '+' || $tokens[$pos] === '-')) {
                $op = $tokens[$pos++];
                $right = $parseTerm();
                $poly = $add($poly, $op === '+' ? $right : $negate($right));
            }
            return $poly;
        };

        $compareLists = function ($a, $b) {
            $n = min(count($a), count($b));
            for ($i = 0; $i < $n; $i++) {
                if ($a[$i] < $b[$i]) return -1;
                if ($a[$i] > $b[$i]) return 1;
            }
            return count($a) - count($b);
        };

        $poly = $parseExpr();
        $keys = [];
        foreach ($poly as $k => $v) $keys[] = [$k, $v];
        usort($keys, function ($a, $b) use ($itemsOf, $compareLists) {
            $ai = $itemsOf($a[0]);
            $bi = $itemsOf($b[0]);
            if (count($ai) !== count($bi)) return count($bi) - count($ai);
            return $compareLists($ai, $bi);
        });
        $answer = [];
        foreach ($keys as $pair) {
            $k = $pair[0];
            $v = $pair[1];
            if ($v === 0) continue;
            $items = $itemsOf($k);
            if (count($items) === 0) $answer[] = (string)$v;
            else $answer[] = (string)$v . '*' . implode('*', $items);
        }
        return $answer;
    }
}
""")

add("0771_jewels_and_stones", r"""<?php
// LeetCode 0771 - Jewels and Stones
// https://leetcode.com/problems/jewels-and-stones/

class Solution {
    function numJewelsInStones($jewels, $stones) {
        $jewelSet = [];
        $jlen = strlen($jewels);
        for ($i = 0; $i < $jlen; $i++) $jewelSet[$jewels[$i]] = true;
        $count = 0;
        $slen = strlen($stones);
        for ($i = 0; $i < $slen; $i++) if (isset($jewelSet[$stones[$i]])) $count++;
        return $count;
    }
}
""")

add("0772_basic_calculator_iii", r"""<?php
// LeetCode 0772 - Basic Calculator III
// https://leetcode.com/problems/basic-calculator-iii/

class Solution {
    function calculate($s) {
        $expr = '';
        $slen = strlen($s);
        for ($si = 0; $si < $slen; $si++) if (!preg_match('/\s/', $s[$si])) $expr .= $s[$si];
        $i = 0;
        $parse = function () use (&$parse, &$expr, &$i) {
            $stack = [];
            $num = 0;
            $sign = '+';
            $elen = strlen($expr);
            while ($i < $elen) {
                $ch = $expr[$i];
                if ($ch >= '0' && $ch <= '9') $num = $num * 10 + (ord($ch) - 48);
                else if ($ch === '(') {
                    $i++;
                    $num = $parse();
                }
                if ((!($ch >= '0' && $ch <= '9') && $ch !== '(') || $i === $elen - 1) {
                    if ($ch === '+' || $ch === '-' || $ch === '*' || $ch === '/' || $ch === ')' || $i === $elen - 1) {
                        if ($sign === '+') $stack[] = $num;
                        else if ($sign === '-') $stack[] = -$num;
                        else if ($sign === '*') $stack[count($stack) - 1] *= $num;
                        else if ($sign === '/') {
                            $top = array_pop($stack);
                            $stack[] = (int)($top / $num);
                        }
                        if ($ch === ')') {
                            $sum = 0;
                            foreach ($stack as $v) $sum += $v;
                            return $sum;
                        }
                        $sign = $ch;
                        $num = 0;
                    }
                }
                $i++;
            }
            $total = 0;
            foreach ($stack as $v) $total += $v;
            return $total;
        };
        return $parse();
    }
}
""")

add("0773_sliding_puzzle", r"""<?php
// LeetCode 0773 - Sliding Puzzle
// https://leetcode.com/problems/sliding-puzzle/

class Solution {
    function slidingPuzzle($board) {
        $start = '';
        foreach ($board as $row) foreach ($row as $cell) $start .= (string)$cell;
        $target = '123450';
        $neighbors = [[1, 3], [0, 2, 4], [1, 5], [0, 4], [1, 3, 5], [2, 4]];
        $q = [$start];
        $stepsQ = [0];
        $seen = [$start => true];
        while (count($q) > 0) {
            $state = array_shift($q);
            $steps = array_shift($stepsQ);
            if ($state === $target) return $steps;
            $zero = strpos($state, '0');
            foreach ($neighbors[$zero] as $nei) {
                $nxt = str_split($state);
                $tmp = $nxt[$zero];
                $nxt[$zero] = $nxt[$nei];
                $nxt[$nei] = $tmp;
                $ns = implode('', $nxt);
                if (!isset($seen[$ns])) {
                    $seen[$ns] = true;
                    $q[] = $ns;
                    $stepsQ[] = $steps + 1;
                }
            }
        }
        return -1;
    }
}
""")

add("0774_minimize_max_distance_to_gas_station", r"""<?php
// LeetCode 0774 - Minimize Max Distance to Gas Station
// https://leetcode.com/problems/minimize-max-distance-to-gas-station/

class Solution {
    function minmaxGasDist($stations, $k) {
        $can = function ($dist) use ($stations, $k) {
            $needed = 0;
            for ($i = 1; $i < count($stations); $i++)
                $needed += (int)floor(($stations[$i] - $stations[$i - 1]) / $dist);
            return $needed <= $k;
        };
        $lo = 0.0;
        $hi = $stations[count($stations) - 1] - $stations[0];
        while ($hi - $lo > 1e-6) {
            $mid = ($lo + $hi) / 2.0;
            if ($can($mid)) $hi = $mid;
            else $lo = $mid;
        }
        return $hi;
    }
}
""")

add("0775_global_and_local_inversions", r"""<?php
// LeetCode 0775 - Global and Local Inversions
// https://leetcode.com/problems/global-and-local-inversions/

class Solution {
    function isIdealPermutation($nums) {
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            if (abs($nums[$i] - $i) > 1) return false;
        }
        return true;
    }
}
""")

add("0776_split_bst", """<?php
// LeetCode 0776 - Split BST
// https://leetcode.com/problems/split-bst/

""" + TREE + r"""
class Solution {
    function splitBST($root, $target) {
        if ($root === null) return [null, null];
        if ($root->val <= $target) {
            $parts = $this->splitBST($root->right, $target);
            $root->right = $parts[0];
            return [$root, $parts[1]];
        }
        $leftParts = $this->splitBST($root->left, $target);
        $root->left = $leftParts[1];
        return [$leftParts[0], $root];
    }
}
""")

add("0777_swap_adjacent_in_lr_string", r"""<?php
// LeetCode 0777 - Swap Adjacent in LR String
// https://leetcode.com/problems/swap-adjacent-in-lr-string/

class Solution {
    function canTransform($start, $result) {
        $a = '';
        $b = '';
        $n = strlen($start);
        for ($i = 0; $i < $n; $i++) if ($start[$i] !== 'X') $a .= $start[$i];
        $rn = strlen($result);
        for ($i = 0; $i < $rn; $i++) if ($result[$i] !== 'X') $b .= $result[$i];
        if ($a !== $b) return false;
        $i = 0;
        $j = 0;
        while ($i < $n && $j < $n) {
            while ($i < $n && $start[$i] === 'X') $i++;
            while ($j < $n && $result[$j] === 'X') $j++;
            if ($i === $n || $j === $n) break;
            if ($start[$i] !== $result[$j]) return false;
            if ($start[$i] === 'L' && $i < $j) return false;
            if ($start[$i] === 'R' && $i > $j) return false;
            $i++;
            $j++;
        }
        return true;
    }
}
""")

add("0778_swim_in_rising_water", r"""<?php
// LeetCode 0778 - Swim in Rising Water
// https://leetcode.com/problems/swim-in-rising-water/

class Solution {
    function swimInWater($grid) {
        $n = count($grid);
        $heap = [[$grid[0][0], 0, 0]];
        $seen = array_fill(0, $n, array_fill(0, $n, false));
        $seen[0][0] = true;
        $dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]];
        while (count($heap) > 0) {
            usort($heap, function ($a, $b) { return $a[0] - $b[0]; });
            $item = array_shift($heap);
            $time = $item[0];
            $r = $item[1];
            $c = $item[2];
            if ($r === $n - 1 && $c === $n - 1) return $time;
            foreach ($dirs as $d) {
                $nr = $r + $d[0];
                $nc = $c + $d[1];
                if ($nr >= 0 && $nr < $n && $nc >= 0 && $nc < $n && !$seen[$nr][$nc]) {
                    $seen[$nr][$nc] = true;
                    $nt = max($time, $grid[$nr][$nc]);
                    $heap[] = [$nt, $nr, $nc];
                }
            }
        }
        return -1;
    }
}
""")

add("0779_k_th_symbol_in_grammar", r"""<?php
// LeetCode 0779 - K-th Symbol in Grammar
// https://leetcode.com/problems/k-th-symbol-in-grammar/

class Solution {
    function kthGrammar($n, $k) {
        if ($n === 1) return 0;
        $mid = 1 << ($n - 2);
        if ($k <= $mid) return $this->kthGrammar($n - 1, $k);
        return 1 - $this->kthGrammar($n - 1, $k - $mid);
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

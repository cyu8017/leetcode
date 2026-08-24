#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
SOLUTIONS = {}

def add(folder, body):
    SOLUTIONS[folder] = body


add("2727_is_object_empty", r'''<?php
// LeetCode 2727 - Is Object Empty
// https://leetcode.com/problems/is-object-empty/

class Solution {
    function isEmpty($obj) {
        if (is_array($obj)) return count($obj) === 0;
        if (is_object($obj)) return count(get_object_vars($obj)) === 0;
        return empty($obj);
    }
}
''')

add("2728_count_houses_in_a_circular_street", r'''<?php
// LeetCode 2728 - Count Houses in a Circular Street
// https://leetcode.com/problems/count-houses-in-a-circular-street/

class Street {
    public $doors;
    public $i = 0;
    function __construct($doors) {
        $this->doors = $doors;
    }
    function closeDoor() { $this->doors[$this->i] = 0; }
    function openDoor() { $this->doors[$this->i] = 1; }
    function isDoorOpen() { return $this->doors[$this->i] == 1; }
    function moveRight() { $this->i = ($this->i + 1) % count($this->doors); }
}

class Solution {
    function houseCount($street, $k) {
        if (is_array($street)) $street = new Street($street);
        for ($i = 0; $i < $k; $i++) {
            $street->closeDoor();
            $street->moveRight();
        }
        $ans = 0;
        for (;;) {
            $ans++;
            $street->openDoor();
            $street->moveRight();
            if ($street->isDoorOpen()) break;
        }
        return $ans;
    }
}
''')

add("2729_check_if_the_number_is_fascinating", r'''<?php
// LeetCode 2729 - Check if The Number is Fascinating
// https://leetcode.com/problems/check-if-the-number-is-fascinating/

class Solution {
    function isFascinating($n) {
        $s = (string)$n . (string)(2 * $n) . (string)(3 * $n);
        if (strlen($s) !== 9) return false;
        $cnt = array_fill(0, 10, 0);
        for ($i = 0; $i < 9; $i++) $cnt[ord($s[$i]) - 48]++;
        if ($cnt[0] !== 0) return false;
        for ($i = 1; $i <= 9; $i++) if ($cnt[$i] !== 1) return false;
        return true;
    }
}
''')

add("2730_find_the_longest_semi_repetitive_substring", r'''<?php
// LeetCode 2730 - Find the Longest Semi-Repetitive Substring
// https://leetcode.com/problems/find-the-longest-semi-repetitive-substring/

class Solution {
    function longestSemiRepetitiveSubstring($s) {
        $ans = 0;
        $left = 0;
        $lastPair = -1;
        $n = strlen($s);
        for ($right = 0; $right < $n; $right++) {
            if ($right > 0 && $s[$right] === $s[$right - 1]) {
                if ($lastPair >= $left) $left = $lastPair + 1;
                $lastPair = $right - 1;
            }
            $ans = max($ans, $right - $left + 1);
        }
        return $ans;
    }
}
''')

add("2731_movement_of_robots", r'''<?php
// LeetCode 2731 - Movement of Robots
// https://leetcode.com/problems/movement-of-robots/

class Solution {
    function sumDistance($nums, $s, $d) {
        $MOD = 1000000007;
        $n = count($nums);
        $pos = [];
        for ($i = 0; $i < $n; $i++) $pos[$i] = $nums[$i] + ($s[$i] === 'R' ? $d : -$d);
        sort($pos);
        $ans = 0;
        $pref = 0;
        for ($i = 0; $i < $n; $i++) {
            $ans = ($ans + (($pos[$i] * $i - $pref) % $MOD + $MOD) % $MOD) % $MOD;
            $pref += $pos[$i];
        }
        return ($ans % $MOD + $MOD) % $MOD;
    }
}
''')

add("2732_find_a_good_subset_of_the_matrix", r'''<?php
// LeetCode 2732 - Find a Good Subset of the Matrix
// https://leetcode.com/problems/find-a-good-subset-of-the-matrix/

class Solution {
    function goodSubsetofBinaryMatrix($grid) {
        $n = count($grid[0]);
        $first = [];
        for ($i = 0; $i < count($grid); $i++) {
            $mask = 0;
            for ($j = 0; $j < $n; $j++) if ($grid[$i][$j] === 1) $mask |= 1 << $j;
            if ($mask === 0) return [$i];
            foreach ($first as $pm => $idx) {
                if (($pm & $mask) === 0) {
                    return $idx < $i ? [$idx, $i] : [$i, $idx];
                }
            }
            if (!array_key_exists($mask, $first)) $first[$mask] = $i;
        }
        return [];
    }
}
''')

add("2733_neither_minimum_nor_maximum", r'''<?php
// LeetCode 2733 - Neither Minimum nor Maximum
// https://leetcode.com/problems/neither-minimum-nor-maximum/

class Solution {
    function findNonMinOrMax($nums) {
        if (count($nums) < 3) return -1;
        $a = $nums[0];
        $b = $nums[1];
        $c = $nums[2];
        return $a + $b + $c - max($a, $b, $c) - min($a, $b, $c);
    }
}
''')

add("2734_lexicographically_smallest_string_after_substring_operation", r'''<?php
// LeetCode 2734 - Lexicographically Smallest String After Substring Operation
// https://leetcode.com/problems/lexicographically-smallest-string-after-substring-operation/

class Solution {
    function smallestString($s) {
        $arr = str_split($s);
        $n = count($arr);
        $i = 0;
        while ($i < $n && $arr[$i] === 'a') $i++;
        if ($i === $n) {
            $arr[$n - 1] = 'z';
            return implode('', $arr);
        }
        while ($i < $n && $arr[$i] !== 'a') {
            $arr[$i] = chr(ord($arr[$i]) - 1);
            $i++;
        }
        return implode('', $arr);
    }
}
''')

add("2735_collecting_chocolates", r'''<?php
// LeetCode 2735 - Collecting Chocolates
// https://leetcode.com/problems/collecting-chocolates/

class Solution {
    function minCost($nums, $x) {
        $n = count($nums);
        $best = $nums;
        $ans = 0;
        foreach ($nums as $v) $ans += $v;
        for ($rot = 1; $rot < $n; $rot++) {
            $cur = $rot * $x;
            for ($i = 0; $i < $n; $i++) {
                $best[$i] = min($best[$i], $nums[($i + $rot) % $n]);
                $cur += $best[$i];
            }
            $ans = min($ans, $cur);
        }
        return $ans;
    }
}
''')

add("2736_maximum_sum_queries", r'''<?php
// LeetCode 2736 - Maximum Sum Queries
// https://leetcode.com/problems/maximum-sum-queries/

class Solution {
    function maximumSumQueries($nums1, $nums2, $queries) {
        $n = count($nums1);
        $pts = [];
        for ($i = 0; $i < $n; $i++) $pts[] = [$nums1[$i], $nums2[$i], $nums1[$i] + $nums2[$i]];
        usort($pts, function($a, $b) { return $b[0] <=> $a[0]; });
        $qs = [];
        foreach ($queries as $i => $q) $qs[] = [$q[0], $q[1], $i];
        usort($qs, function($a, $b) { return $b[0] <=> $a[0]; });
        $ys = array_merge($nums2, array_map(function($q) { return $q[1]; }, $queries));
        sort($ys);
        $uniq = [];
        foreach ($ys as $y) {
            if (!$uniq || $uniq[count($uniq) - 1] !== $y) $uniq[] = $y;
        }
        $m = count($uniq);
        $bit = array_fill(0, $m + 2, -1);
        $rank = function($y) use ($uniq, $m) {
            $lo = 0;
            $hi = $m;
            while ($lo < $hi) {
                $mid = ($lo + $hi) >> 1;
                if ($uniq[$mid] < $y) $lo = $mid + 1;
                else $hi = $mid;
            }
            return $lo + 1;
        };
        $update = function($i, $v) use (&$bit, $m) {
            for (; $i <= $m; $i += $i & -$i) $bit[$i] = max($bit[$i], $v);
        };
        $query = function($i) use (&$bit) {
            $best = -1;
            for (; $i > 0; $i -= $i & -$i) $best = max($best, $bit[$i]);
            return $best;
        };
        $ans = array_fill(0, count($queries), -1);
        $j = 0;
        foreach ($qs as $q) {
            while ($j < $n && $pts[$j][0] >= $q[0]) {
                $update($m - $rank($pts[$j][1]) + 1, $pts[$j][2]);
                $j++;
            }
            $ans[$q[2]] = $query($m - $rank($q[1]) + 1);
        }
        return $ans;
    }
}
''')

add("2737_find_the_closest_marked_node", r'''<?php
// LeetCode 2737 - Find the Closest Marked Node
// https://leetcode.com/problems/find-the-closest-marked-node/

class Solution {
    function minimumDistance($n, $edges, $s, $marked) {
        $g = array_fill(0, $n, []);
        foreach ($edges as $e) $g[$e[0]][] = [$e[1], $e[2]];
        $mark = array_fill_keys($marked, true);
        $INF = 1000000000000;
        $dist = array_fill(0, $n, $INF);
        $dist[$s] = 0;
        $pq = new SplPriorityQueue();
        $pq->insert([$s, 0], 0);
        while (!$pq->isEmpty()) {
            $cur = $pq->extract();
            $u = $cur[0];
            $d = $cur[1];
            if (isset($mark[$u])) return $d;
            if ($d > $dist[$u]) continue;
            foreach ($g[$u] as $e) {
                $v = $e[0];
                $w = $e[1];
                if ($d + $w < $dist[$v]) {
                    $dist[$v] = $d + $w;
                    $pq->insert([$v, $dist[$v]], -$dist[$v]);
                }
            }
        }
        return -1;
    }
}
''')

add("2739_total_distance_traveled", r'''<?php
// LeetCode 2739 - Total Distance Traveled
// https://leetcode.com/problems/total-distance-traveled/

class Solution {
    function distanceTraveled($mainTank, $additionalTank) {
        $ans = 0;
        while ($mainTank > 0) {
            if ($mainTank >= 5) {
                $ans += 50;
                $mainTank -= 5;
                if ($additionalTank > 0) {
                    $additionalTank--;
                    $mainTank++;
                }
            } else {
                $ans += $mainTank * 10;
                $mainTank = 0;
            }
        }
        return $ans;
    }
}
''')

add("2740_find_the_value_of_the_partition", r'''<?php
// LeetCode 2740 - Find the Value of the Partition
// https://leetcode.com/problems/find-the-value-of-the-partition/

class Solution {
    function findValueOfPartition($nums) {
        sort($nums);
        $ans = PHP_INT_MAX;
        for ($i = 1; $i < count($nums); $i++) $ans = min($ans, $nums[$i] - $nums[$i - 1]);
        return $ans;
    }
}
''')

add("2741_special_permutations", r'''<?php
// LeetCode 2741 - Special Permutations
// https://leetcode.com/problems/special-permutations/

class Solution {
    public $nums;
    public $memo;
    public $n;
    function specialPerm($nums) {
        $this->nums = $nums;
        $this->n = count($nums);
        $this->memo = array_fill(0, 1 << $this->n, array_fill(0, $this->n, -1));
        $ans = 0;
        for ($i = 0; $i < $this->n; $i++) $ans = ($ans + $this->dfs(1 << $i, $i)) % 1000000007;
        return $ans;
    }
    function dfs($mask, $last) {
        $MOD = 1000000007;
        if ($mask === (1 << $this->n) - 1) return 1;
        if ($this->memo[$mask][$last] !== -1) return $this->memo[$mask][$last];
        $res = 0;
        for ($i = 0; $i < $this->n; $i++) {
            if ($mask & (1 << $i)) continue;
            if ($this->nums[$i] % $this->nums[$last] === 0 || $this->nums[$last] % $this->nums[$i] === 0)
                $res = ($res + $this->dfs($mask | (1 << $i), $i)) % $MOD;
        }
        return $this->memo[$mask][$last] = $res;
    }
}
''')

add("2742_painting_the_walls", r'''<?php
// LeetCode 2742 - Painting the Walls
// https://leetcode.com/problems/painting-the-walls/

class Solution {
    function paintWalls($cost, $time) {
        $n = count($cost);
        $INF = 1000000000000;
        $dp = array_fill(0, $n + 1, $INF);
        $dp[0] = 0;
        for ($i = 0; $i < $n; $i++) {
            for ($j = $n; $j >= 0; $j--) {
                $nj = min($n, $j + $time[$i] + 1);
                if ($dp[$j] + $cost[$i] < $dp[$nj]) $dp[$nj] = $dp[$j] + $cost[$i];
            }
        }
        return $dp[$n];
    }
}
''')

add("2743_count_substrings_without_repeating_character", r'''<?php
// LeetCode 2743 - Count Substrings Without Repeating Character
// https://leetcode.com/problems/count-substrings-without-repeating-character/

class Solution {
    function numberOfSpecialSubstrings($s) {
        $n = strlen($s);
        $ans = 0;
        $left = 0;
        $cnt = array_fill(0, 26, 0);
        for ($i = 0; $i < $n; $i++) {
            $c = ord($s[$i]) - 97;
            $cnt[$c]++;
            while ($cnt[$c] > 1) {
                $cnt[ord($s[$left]) - 97]--;
                $left++;
            }
            $ans += $i - $left + 1;
        }
        return $ans;
    }
}
''')

add("2744_find_maximum_number_of_string_pairs", r'''<?php
// LeetCode 2744 - Find Maximum Number of String Pairs
// https://leetcode.com/problems/find-maximum-number-of-string-pairs/

class Solution {
    function maximumNumberOfStringPairs($words) {
        $freq = [];
        $ans = 0;
        foreach ($words as $w) {
            $rev = strrev($w);
            $c = $freq[$rev] ?? 0;
            if ($c > 0) {
                $ans++;
                $freq[$rev] = $c - 1;
            } else {
                $freq[$w] = ($freq[$w] ?? 0) + 1;
            }
        }
        return $ans;
    }
}
''')

add("2745_construct_the_longest_new_string", r'''<?php
// LeetCode 2745 - Construct the Longest New String
// https://leetcode.com/problems/construct-the-longest-new-string/

class Solution {
    function longestString($x, $y, $z) {
        if ($x < $y) return (2 * $x + 1 + $z) * 2;
        if ($y < $x) return (2 * $y + 1 + $z) * 2;
        return ($x + $y + $z) * 2;
    }
}
''')

add("2746_decremental_string_concatenation", r'''<?php
// LeetCode 2746 - Decremental String Concatenation
// https://leetcode.com/problems/decremental-string-concatenation/

class Solution {
    public $words;
    public $memo;
    public $n;
    function minimizeConcatenatedLength($words) {
        $this->words = $words;
        $this->n = count($words);
        $this->memo = [];
        $w0 = $words[0];
        return strlen($w0) + $this->dfs(1, $w0[0], $w0[strlen($w0) - 1]);
    }
    function dfs($i, $first, $last) {
        if ($i === $this->n) return 0;
        $key = $i . ',' . $first . ',' . $last;
        if (isset($this->memo[$key])) return $this->memo[$key];
        $w = $this->words[$i];
        $wf = $w[0];
        $wl = $w[strlen($w) - 1];
        $add1 = strlen($w) - ($last === $wf ? 1 : 0);
        $add2 = strlen($w) - ($wl === $first ? 1 : 0);
        $a = $add1 + $this->dfs($i + 1, $first, $wl);
        $b = $add2 + $this->dfs($i + 1, $wf, $last);
        return $this->memo[$key] = min($a, $b);
    }
}
''')

add("2747_count_zero_request_servers", r'''<?php
// LeetCode 2747 - Count Zero Request Servers
// https://leetcode.com/problems/count-zero-request-servers/

class Solution {
    function countServers($n, $logs, $x, $queries) {
        usort($logs, function($a, $b) { return $a[1] <=> $b[1]; });
        $qs = [];
        foreach ($queries as $i => $t) $qs[] = [$t, $i];
        usort($qs, function($a, $b) { return $a[0] <=> $b[0]; });
        $ans = array_fill(0, count($queries), 0);
        $cnt = [];
        $active = 0;
        $l = 0;
        $r = 0;
        $m = count($logs);
        foreach ($qs as $q) {
            $t = $q[0];
            $qi = $q[1];
            while ($r < $m && $logs[$r][1] <= $t) {
                $id = $logs[$r][0];
                $c = $cnt[$id] ?? 0;
                if ($c === 0) $active++;
                $cnt[$id] = $c + 1;
                $r++;
            }
            while ($l < $r && $logs[$l][1] < $t - $x) {
                $id = $logs[$l][0];
                $c = $cnt[$id] - 1;
                $cnt[$id] = $c;
                if ($c === 0) $active--;
                $l++;
            }
            $ans[$qi] = $n - $active;
        }
        return $ans;
    }
}
''')

add("2748_number_of_beautiful_pairs", r'''<?php
// LeetCode 2748 - Number of Beautiful Pairs
// https://leetcode.com/problems/number-of-beautiful-pairs/

class Solution {
    function countBeautifulPairs($nums) {
        $gcd = function($a, $b) {
            while ($b) { $t = $a % $b; $a = $b; $b = $t; }
            return $a;
        };
        $firstDigit = function($x) {
            while ($x >= 10) $x = intdiv($x, 10);
            return $x;
        };
        $ans = 0;
        $freq = array_fill(0, 10, 0);
        foreach ($nums as $x) {
            $last = $x % 10;
            for ($d = 1; $d <= 9; $d++)
                if ($freq[$d] > 0 && $gcd($d, $last) === 1) $ans += $freq[$d];
            $freq[$firstDigit($x)]++;
        }
        return $ans;
    }
}
''')

add("2749_minimum_operations_to_make_the_integer_zero", r'''<?php
// LeetCode 2749 - Minimum Operations to Make the Integer Zero
// https://leetcode.com/problems/minimum-operations-to-make-the-integer-zero/

class Solution {
    function makeTheIntegerZero($num1, $num2) {
        $popcount = function($x) {
            $c = 0;
            while ($x > 0) {
                $c += $x & 1;
                $x = intdiv($x, 2);
            }
            return $c;
        };
        for ($k = 1; $k <= 60; $k++) {
            $rem = $num1 - $k * $num2;
            if ($rem < $k) continue;
            if ($popcount($rem) <= $k) return $k;
        }
        return -1;
    }
}
''')

add("2750_ways_to_split_array_into_good_subarrays", r'''<?php
// LeetCode 2750 - Ways to Split Array Into Good Subarrays
// https://leetcode.com/problems/ways-to-split-array-into-good-subarrays/

class Solution {
    function numberOfGoodSubarraySplits($nums) {
        $MOD = 1000000007;
        $ones = [];
        for ($i = 0; $i < count($nums); $i++) if ($nums[$i] === 1) $ones[] = $i;
        if (!$ones) return 0;
        $ans = 1;
        for ($i = 1; $i < count($ones); $i++)
            $ans = $ans * ($ones[$i] - $ones[$i - 1]) % $MOD;
        return $ans;
    }
}
''')

add("2751_robot_collisions", r'''<?php
// LeetCode 2751 - Robot Collisions
// https://leetcode.com/problems/robot-collisions/

class Solution {
    function survivedRobotsHealths($positions, $healths, $directions) {
        $n = count($positions);
        $idx = range(0, $n - 1);
        usort($idx, function($a, $b) use ($positions) { return $positions[$a] <=> $positions[$b]; });
        $stack = [];
        foreach ($idx as $i) {
            $cur = [$i, $healths[$i], $directions[$i]];
            while ($stack && $stack[count($stack) - 1][2] === 'R' && $cur[2] === 'L') {
                $top = &$stack[count($stack) - 1];
                if ($top[1] === $cur[1]) {
                    array_pop($stack);
                    unset($top);
                    $cur[1] = 0;
                    break;
                } else if ($top[1] > $cur[1]) {
                    $top[1]--;
                    unset($top);
                    $cur[1] = 0;
                    break;
                } else {
                    $cur[1]--;
                    unset($top);
                    array_pop($stack);
                }
            }
            if ($cur[1] > 0) $stack[] = $cur;
        }
        $alive = [];
        foreach ($stack as $item) $alive[$item[0]] = $item[1];
        $ans = [];
        for ($i = 0; $i < $n; $i++) if (isset($alive[$i])) $ans[] = $alive[$i];
        return $ans;
    }
}
''')

add("2753_count_houses_in_a_circular_street_ii", r'''<?php
// LeetCode 2753 - Count Houses in a Circular Street II
// https://leetcode.com/problems/count-houses-in-a-circular-street-ii/

class Street {
    public $doors;
    public $i = 0;
    function __construct($doors) {
        $this->doors = $doors;
    }
    function closeDoor() { $this->doors[$this->i] = 0; }
    function isDoorOpen() { return $this->doors[$this->i] == 1; }
    function moveRight() { $this->i = ($this->i + 1) % count($this->doors); }
}

class Solution {
    function houseCount($street, $k) {
        if (is_array($street)) $street = new Street($street);
        while (!$street->isDoorOpen()) $street->moveRight();
        $street->closeDoor();
        $street->moveRight();
        $ans = 1;
        for ($i = 1; $i < $k; $i++) {
            if ($street->isDoorOpen()) {
                $street->closeDoor();
                $ans = 0;
            }
            $ans++;
            $street->moveRight();
        }
        return $ans;
    }
}
''')

add("2754_bind_function_to_context", r'''<?php
// LeetCode 2754 - Bind Function to Context
// https://leetcode.com/problems/bind-function-to-context/

class Solution {
    function bindPolyfill($fn, $obj) {
        return function(...$args) use ($fn, $obj) {
            if (is_callable($fn)) {
                return $fn($obj, ...$args);
            }
            return null;
        };
    }
}
''')

add("2755_deep_merge_of_two_objects", r'''<?php
// LeetCode 2755 - Deep Merge of Two Objects
// https://leetcode.com/problems/deep-merge-of-two-objects/

class Solution {
    function deepMerge($obj1, $obj2) {
        $isList = function($x) {
            if (!is_array($x)) return false;
            if ($x === []) return true;
            return array_keys($x) === range(0, count($x) - 1);
        };
        $isObj = function($x) use ($isList) {
            return is_array($x) && !$isList($x) || is_object($x);
        };
        if ($isObj($obj1) && $isObj($obj2)) {
            $a = (array)$obj1;
            $b = (array)$obj2;
            $res = $a;
            foreach ($b as $k => $v) {
                if (array_key_exists($k, $res)) $res[$k] = $this->deepMerge($res[$k], $v);
                else $res[$k] = $v;
            }
            return $res;
        }
        if ($isList($obj1) && $isList($obj2)) {
            $n = max(count($obj1), count($obj2));
            $res = [];
            for ($i = 0; $i < $n; $i++) {
                if ($i >= count($obj1)) $res[$i] = $obj2[$i];
                else if ($i >= count($obj2)) $res[$i] = $obj1[$i];
                else $res[$i] = $this->deepMerge($obj1[$i], $obj2[$i]);
            }
            return $res;
        }
        return $obj2;
    }
}
''')

add("2756_query_batching", r'''<?php
// LeetCode 2756 - Query Batching
// https://leetcode.com/problems/query-batching/

class QueryBatcher {
    public $queryMultiple;
    public $t;
    public $pending = [];
    public $busyUntil = 0;
    function __construct($queryMultiple, $t) {
        $this->queryMultiple = $queryMultiple;
        $this->t = $t;
    }
    function getValue($key, $now = null) {
        if ($now === null) $now = (int)(microtime(true) * 1000);
        $this->pending[] = $key;
        if ($now >= $this->busyUntil) {
            return $this->flush($now);
        }
        return $this->pending;
    }
    function flush($now = null) {
        if (!$this->pending) return [];
        $batch = $this->pending;
        $this->pending = [];
        if ($now === null) $now = (int)(microtime(true) * 1000);
        $this->busyUntil = $now + $this->t;
        $fn = $this->queryMultiple;
        return $fn($batch);
    }
}
''')

add("2757_generate_circular_array_values", r'''<?php
// LeetCode 2757 - Generate Circular Array Values
// https://leetcode.com/problems/generate-circular-array-values/

class Solution {
    function cycleGenerator($arr, $steps, $startIndex) {
        $i = $startIndex;
        $n = count($arr);
        $out = [$arr[$i]];
        foreach ($steps as $jump) {
            $i = (($i + $jump) % $n + $n) % $n;
            $out[] = $arr[$i];
        }
        return $out;
    }
}
''')

add("2758_next_day", r'''<?php
// LeetCode 2758 - Next Day
// https://leetcode.com/problems/next-day/

class Solution {
    function nextDay($date) {
        $d = new DateTime($date);
        $d->modify('+1 day');
        return $d->format('Y-m-d');
    }
}
''')

add("2759_convert_json_string_to_object", r'''<?php
// LeetCode 2759 - Convert JSON String to Object
// https://leetcode.com/problems/convert-json-string-to-object/

class Solution {
    public $str;
    public $i;
    function jsonParse($str) {
        $this->str = $str;
        $this->i = 0;
        return $this->parse();
    }
    function parse() {
        $str = $this->str;
        if ($str[$this->i] === '"') {
            $this->i++;
            $s = '';
            while ($str[$this->i] !== '"') $s .= $str[$this->i++];
            $this->i++;
            return $s;
        }
        if ($str[$this->i] === 't') { $this->i += 4; return true; }
        if ($str[$this->i] === 'f') { $this->i += 5; return false; }
        if ($str[$this->i] === 'n') { $this->i += 4; return null; }
        if ($str[$this->i] === '[') {
            $this->i++;
            $arr = [];
            if ($str[$this->i] === ']') { $this->i++; return $arr; }
            while (true) {
                $arr[] = $this->parse();
                if ($str[$this->i] === ',') { $this->i++; continue; }
                $this->i++;
                return $arr;
            }
        }
        if ($str[$this->i] === '{') {
            $this->i++;
            $obj = [];
            if ($str[$this->i] === '}') { $this->i++; return $obj; }
            while (true) {
                $key = $this->parse();
                $this->i++;
                $obj[$key] = $this->parse();
                if ($str[$this->i] === ',') { $this->i++; continue; }
                $this->i++;
                return $obj;
            }
        }
        $start = $this->i;
        if ($str[$this->i] === '-') $this->i++;
        $n = strlen($str);
        while ($this->i < $n && (($str[$this->i] >= '0' && $str[$this->i] <= '9') || $str[$this->i] === '.')) $this->i++;
        $num = substr($str, $start, $this->i - $start);
        return strpos($num, '.') !== false ? (float)$num : (int)$num;
    }
}
''')

add("2760_longest_even_odd_subarray_with_threshold", r'''<?php
// LeetCode 2760 - Longest Even Odd Subarray With Threshold
// https://leetcode.com/problems/longest-even-odd-subarray-with-threshold/

class Solution {
    function longestAlternatingSubarray($nums, $threshold) {
        $ans = 0;
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            if ($nums[$i] % 2 !== 0 || $nums[$i] > $threshold) continue;
            $j = $i;
            while ($j + 1 < $n && $nums[$j + 1] <= $threshold && $nums[$j + 1] % 2 !== $nums[$j] % 2) $j++;
            $ans = max($ans, $j - $i + 1);
        }
        return $ans;
    }
}
''')

add("2761_prime_pairs_with_target_sum", r'''<?php
// LeetCode 2761 - Prime Pairs With Target Sum
// https://leetcode.com/problems/prime-pairs-with-target-sum/

class Solution {
    function findPrimePairs($n) {
        $isPrime = array_fill(0, $n + 1, true);
        $isPrime[0] = $isPrime[1] = false;
        for ($i = 2; $i * $i <= $n; $i++) {
            if ($isPrime[$i]) {
                for ($j = $i * $i; $j <= $n; $j += $i) $isPrime[$j] = false;
            }
        }
        $ans = [];
        for ($x = 2; $x <= intdiv($n, 2); $x++) {
            $y = $n - $x;
            if ($isPrime[$x] && $isPrime[$y]) $ans[] = [$x, $y];
        }
        return $ans;
    }
}
''')

add("2762_continuous_subarrays", r'''<?php
// LeetCode 2762 - Continuous Subarrays
// https://leetcode.com/problems/continuous-subarrays/

class Solution {
    function continuousSubarrays($nums) {
        $ans = 0;
        $left = 0;
        $minQ = [];
        $maxQ = [];
        $n = count($nums);
        for ($right = 0; $right < $n; $right++) {
            while ($minQ && $nums[$minQ[count($minQ) - 1]] > $nums[$right]) array_pop($minQ);
            while ($maxQ && $nums[$maxQ[count($maxQ) - 1]] < $nums[$right]) array_pop($maxQ);
            $minQ[] = $right;
            $maxQ[] = $right;
            while ($nums[$maxQ[0]] - $nums[$minQ[0]] > 2) {
                $left++;
                if ($minQ[0] < $left) array_shift($minQ);
                if ($maxQ[0] < $left) array_shift($maxQ);
            }
            $ans += $right - $left + 1;
        }
        return $ans;
    }
}
''')

add("2763_sum_of_imbalance_numbers_of_all_subarrays", r'''<?php
// LeetCode 2763 - Sum of Imbalance Numbers of All Subarrays
// https://leetcode.com/problems/sum-of-imbalance-numbers-of-all-subarrays/

class Solution {
    function sumImbalanceNumbers($nums) {
        $n = count($nums);
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            $seen = [];
            $sorted = [];
            $imbalance = 0;
            for ($j = $i; $j < $n; $j++) {
                $x = $nums[$j];
                if (!isset($seen[$x])) {
                    $seen[$x] = true;
                    $lo = 0;
                    $hi = count($sorted);
                    while ($lo < $hi) {
                        $mid = ($lo + $hi) >> 1;
                        if ($sorted[$mid] < $x) $lo = $mid + 1;
                        else $hi = $mid;
                    }
                    $idx = $lo;
                    $next = $idx < count($sorted) ? $sorted[$idx] : null;
                    $prev = $idx > 0 ? $sorted[$idx - 1] : null;
                    if ($prev !== null && $x - $prev !== 1) $imbalance++;
                    if ($next !== null && $next - $x !== 1) $imbalance++;
                    if ($prev !== null && $next !== null && $next - $prev > 1) $imbalance--;
                    array_splice($sorted, $idx, 0, [$x]);
                }
                $ans += $imbalance;
            }
        }
        return $ans;
    }
}
''')

add("2764_is_array_a_preorder_of_some_binary_tree", r'''<?php
// LeetCode 2764 - Is Array a Preorder of Some Binary Tree
// https://leetcode.com/problems/is-array-a-preorder-of-some-binary-tree/

class Solution {
    function isPreorder($nodes) {
        if (!$nodes) return true;
        $stack = [$nodes[0][0]];
        for ($i = 1; $i < count($nodes); $i++) {
            $id = $nodes[$i][0];
            $parent = $nodes[$i][1];
            while ($stack && $stack[count($stack) - 1] !== $parent) array_pop($stack);
            if (!$stack) return false;
            $stack[] = $id;
        }
        return true;
    }
}
''')

add("2765_longest_alternating_subarray", r'''<?php
// LeetCode 2765 - Longest Alternating Subarray
// https://leetcode.com/problems/longest-alternating-subarray/

class Solution {
    function alternatingSubarray($nums) {
        $ans = -1;
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            for ($j = $i + 1; $j < $n; $j++) {
                $expect = (($j - $i) % 2 === 0) ? -1 : 1;
                if ($nums[$j] - $nums[$j - 1] !== $expect) break;
                if ($nums[$i + 1] - $nums[$i] !== 1) break;
                $ans = max($ans, $j - $i + 1);
            }
        }
        return $ans;
    }
}
''')

add("2766_relocate_marbles", r'''<?php
// LeetCode 2766 - Relocate Marbles
// https://leetcode.com/problems/relocate-marbles/

class Solution {
    function relocateMarbles($nums, $moveFrom, $moveTo) {
        $pos = array_fill_keys($nums, true);
        for ($i = 0; $i < count($moveFrom); $i++) {
            unset($pos[$moveFrom[$i]]);
            $pos[$moveTo[$i]] = true;
        }
        $keys = array_map('intval', array_keys($pos));
        sort($keys);
        return $keys;
    }
}
''')

add("2767_partition_string_into_minimum_beautiful_substrings", r'''<?php
// LeetCode 2767 - Partition String Into Minimum Beautiful Substrings
// https://leetcode.com/problems/partition-string-into-minimum-beautiful-substrings/

class Solution {
    function minimumBeautifulSubstrings($s) {
        $n = strlen($s);
        $pow5 = [];
        $x = 1;
        while (true) {
            $b = decbin($x);
            if (strlen($b) > $n) break;
            $pow5[$b] = true;
            $x *= 5;
        }
        $INF = 1000000000;
        $dp = array_fill(0, $n + 1, $INF);
        $dp[0] = 0;
        for ($i = 0; $i < $n; $i++) {
            if ($dp[$i] === $INF || $s[$i] === '0') continue;
            for ($j = $i + 1; $j <= $n; $j++) {
                $sub = substr($s, $i, $j - $i);
                if (isset($pow5[$sub])) $dp[$j] = min($dp[$j], $dp[$i] + 1);
            }
        }
        return $dp[$n] === $INF ? -1 : $dp[$n];
    }
}
''')

add("2768_number_of_black_blocks", r'''<?php
// LeetCode 2768 - Number of Black Blocks
// https://leetcode.com/problems/number-of-black-blocks/

class Solution {
    function countBlackBlocks($m, $n, $coordinates) {
        $cnt = [];
        foreach ($coordinates as $c) {
            $x = $c[0];
            $y = $c[1];
            for ($i = $x - 1; $i <= $x; $i++) {
                for ($j = $y - 1; $j <= $y; $j++) {
                    if ($i >= 0 && $j >= 0 && $i < $m - 1 && $j < $n - 1) {
                        $key = $i . ',' . $j;
                        $cnt[$key] = ($cnt[$key] ?? 0) + 1;
                    }
                }
            }
        }
        $out = array_fill(0, 5, 0);
        $out[0] = ($m - 1) * ($n - 1);
        foreach ($cnt as $v) {
            $out[$v]++;
            $out[0]--;
        }
        return $out;
    }
}
''')

add("2769_find_the_maximum_achievable_number", r'''<?php
// LeetCode 2769 - Find the Maximum Achievable Number
// https://leetcode.com/problems/find-the-maximum-achievable-number/

class Solution {
    function theMaximumAchievableX($num, $t) {
        return $num + 2 * $t;
    }
}
''')

add("2770_maximum_number_of_jumps_to_reach_the_last_index", r'''<?php
// LeetCode 2770 - Maximum Number of Jumps to Reach the Last Index
// https://leetcode.com/problems/maximum-number-of-jumps-to-reach-the-last-index/

class Solution {
    function maximumJumps($nums, $target) {
        $n = count($nums);
        $dp = array_fill(0, $n, -1);
        $dp[0] = 0;
        for ($i = 0; $i < $n; $i++) {
            if ($dp[$i] < 0) continue;
            for ($j = $i + 1; $j < $n; $j++) {
                if (abs($nums[$j] - $nums[$i]) <= $target)
                    $dp[$j] = max($dp[$j], $dp[$i] + 1);
            }
        }
        return $dp[$n - 1];
    }
}
''')

add("2771_longest_non_decreasing_subarray_from_two_arrays", r'''<?php
// LeetCode 2771 - Longest Non-decreasing Subarray From Two Arrays
// https://leetcode.com/problems/longest-non-decreasing-subarray-from-two-arrays/

class Solution {
    function maxNonDecreasingLength($nums1, $nums2) {
        $n = count($nums1);
        $dp1 = 1;
        $dp2 = 1;
        $ans = 1;
        for ($i = 1; $i < $n; $i++) {
            $nd1 = 1;
            $nd2 = 1;
            if ($nums1[$i] >= $nums1[$i - 1]) $nd1 = max($nd1, $dp1 + 1);
            if ($nums1[$i] >= $nums2[$i - 1]) $nd1 = max($nd1, $dp2 + 1);
            if ($nums2[$i] >= $nums1[$i - 1]) $nd2 = max($nd2, $dp1 + 1);
            if ($nums2[$i] >= $nums2[$i - 1]) $nd2 = max($nd2, $dp2 + 1);
            $dp1 = $nd1;
            $dp2 = $nd2;
            $ans = max($ans, $dp1, $dp2);
        }
        return $ans;
    }
}
''')

add("2772_apply_operations_to_make_all_array_elements_equal_to_zero", r'''<?php
// LeetCode 2772 - Apply Operations to Make All Array Elements Equal to Zero
// https://leetcode.com/problems/apply-operations-to-make-all-array-elements-equal-to-zero/

class Solution {
    function checkArray($nums, $k) {
        $n = count($nums);
        $diff = array_fill(0, $n + 1, 0);
        $cur = 0;
        for ($i = 0; $i < $n; $i++) {
            $cur += $diff[$i];
            $need = $nums[$i] - $cur;
            if ($need < 0) return false;
            if ($need > 0) {
                if ($i + $k > $n) return false;
                $cur += $need;
                $diff[$i + $k] -= $need;
            }
        }
        return true;
    }
}
''')


def main():
    written = 0
    for folder, body in SOLUTIONS.items():
        path = ROOT / folder / "solution.php"
        path.write_text(body, encoding="utf-8", newline="\n")
        written += 1
        print("wrote", folder)
    print("A written", written)

if __name__ == "__main__":
    main()

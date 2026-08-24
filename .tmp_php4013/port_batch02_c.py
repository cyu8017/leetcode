#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
SOLUTIONS: dict[str, str] = {}


def add(name: str, content: str) -> None:
    SOLUTIONS[name] = content.strip() + "\n"


add("0830_positions_of_large_groups", r"""<?php
// LeetCode 0830 - Positions of Large Groups
// https://leetcode.com/problems/positions-of-large-groups/

class Solution {
    /**
     * @param String $s
     * @return Integer[][]
     */
    function largeGroupPositions($s) {
        $ans = [];
        $n = strlen($s);
        $i = 0;
        while ($i < $n) {
            $j = $i;
            while ($j < $n && $s[$j] === $s[$i]) $j++;
            if ($j - $i >= 3) $ans[] = [$i, $j - 1];
            $i = $j;
        }
        return $ans;
    }
}
""")

add("0831_masking_personal_information", r"""<?php
// LeetCode 0831 - Masking Personal Information
// https://leetcode.com/problems/masking-personal-information/

class Solution {
    /**
     * @param String $s
     * @return String
     */
    function maskPII($s) {
        $at = strpos($s, '@');
        if ($at !== false) {
            $s = strtolower($s);
            $at = strpos($s, '@');
            $name = substr($s, 0, $at);
            $domain = substr($s, $at + 1);
            return $name[0] . "*****" . $name[strlen($name) - 1] . "@" . $domain;
        }
        $digits = "";
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            if (ctype_digit($s[$i])) $digits .= $s[$i];
        }
        $local = substr($digits, -4);
        $country = strlen($digits) - 10;
        if ($country === 0) return "***-***-" . $local;
        return "+" . str_repeat("*", $country) . "-***-***-" . $local;
    }
}
""")

add("0832_flipping_an_image", r"""<?php
// LeetCode 0832 - Flipping an Image
// https://leetcode.com/problems/flipping-an-image/

class Solution {
    /**
     * @param Integer[][] $image
     * @return Integer[][]
     */
    function flipAndInvertImage($image) {
        foreach ($image as &$row) {
            $i = 0;
            $j = count($row) - 1;
            while ($i <= $j) {
                $a = 1 - $row[$i];
                $b = 1 - $row[$j];
                $row[$i] = $b;
                $row[$j] = $a;
                $i++;
                $j--;
            }
        }
        unset($row);
        return $image;
    }
}
""")

add("0833_find_and_replace_in_string", r"""<?php
// LeetCode 0833 - Find And Replace in String
// https://leetcode.com/problems/find-and-replace-in-string/

class Solution {
    /**
     * @param String $s
     * @param Integer[] $indices
     * @param String[] $sources
     * @param String[] $targets
     * @return String
     */
    function findReplaceString($s, $indices, $sources, $targets) {
        $replaceLen = [];
        $replaceStr = [];
        $kn = count($indices);
        for ($k = 0; $k < $kn; $k++) {
            $i = $indices[$k];
            if (substr($s, $i, strlen($sources[$k])) === $sources[$k]) {
                $replaceLen[$i] = strlen($sources[$k]);
                $replaceStr[$i] = $targets[$k];
            }
        }
        $out = "";
        $i = 0;
        $n = strlen($s);
        while ($i < $n) {
            if (isset($replaceStr[$i])) {
                $out .= $replaceStr[$i];
                $i += $replaceLen[$i];
            } else {
                $out .= $s[$i];
                $i++;
            }
        }
        return $out;
    }
}
""")

add("0834_sum_of_distances_in_tree", r"""<?php
// LeetCode 0834 - Sum of Distances in Tree
// https://leetcode.com/problems/sum-of-distances-in-tree/

class Solution {
    /**
     * @param Integer $n
     * @param Integer[][] $edges
     * @return Integer[]
     */
    function sumOfDistancesInTree($n, $edges) {
        $graph = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $graph[$e[0]][] = $e[1];
            $graph[$e[1]][] = $e[0];
        }
        $count = array_fill(0, $n, 1);
        $ans = array_fill(0, $n, 0);
        $post = function($node, $parent) use (&$post, $graph, &$count, &$ans) {
            foreach ($graph[$node] as $child) {
                if ($child === $parent) continue;
                $post($child, $node);
                $count[$node] += $count[$child];
                $ans[$node] += $ans[$child] + $count[$child];
            }
        };
        $reroot = function($node, $parent) use (&$reroot, $graph, $count, &$ans, $n) {
            foreach ($graph[$node] as $child) {
                if ($child === $parent) continue;
                $ans[$child] = $ans[$node] - $count[$child] + ($n - $count[$child]);
                $reroot($child, $node);
            }
        };
        $post(0, -1);
        $reroot(0, -1);
        return $ans;
    }
}
""")

add("0835_image_overlap", r"""<?php
// LeetCode 0835 - Image Overlap
// https://leetcode.com/problems/image-overlap/

class Solution {
    /**
     * @param Integer[][] $img1
     * @param Integer[][] $img2
     * @return Integer
     */
    function largestOverlap($img1, $img2) {
        $n = count($img1);
        $ones1 = [];
        $ones2 = [];
        for ($i = 0; $i < $n; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if ($img1[$i][$j] === 1) $ones1[] = [$i, $j];
                if ($img2[$i][$j] === 1) $ones2[] = [$i, $j];
            }
        }
        if (!count($ones1) || !count($ones2)) return 0;
        $shifts = [];
        $best = 0;
        foreach ($ones1 as $a) {
            foreach ($ones2 as $b) {
                $key = (($a[0] - $b[0] + $n) << 16) | ($a[1] - $b[1] + $n);
                $v = ($shifts[$key] ?? 0) + 1;
                $shifts[$key] = $v;
                $best = max($best, $v);
            }
        }
        return $best;
    }
}
""")

add("0836_rectangle_overlap", r"""<?php
// LeetCode 0836 - Rectangle Overlap
// https://leetcode.com/problems/rectangle-overlap/

class Solution {
    /**
     * @param Integer[] $rec1
     * @param Integer[] $rec2
     * @return Boolean
     */
    function isRectangleOverlap($rec1, $rec2) {
        return !($rec1[2] <= $rec2[0] || $rec1[0] >= $rec2[2] || $rec1[3] <= $rec2[1] || $rec1[1] >= $rec2[3]);
    }
}
""")

add("0837_new_21_game", r"""<?php
// LeetCode 0837 - New 21 Game
// https://leetcode.com/problems/new-21-game/

class Solution {
    /**
     * @param Integer $n
     * @param Integer $k
     * @param Integer $maxPts
     * @return Float
     */
    function new21Game($n, $k, $maxPts) {
        if ($k === 0 || $n >= $k - 1 + $maxPts) return 1.0;
        $dp = array_fill(0, $n + 1, 0.0);
        $dp[0] = 1.0;
        $window = 1.0;
        $ans = 0.0;
        for ($i = 1; $i <= $n; $i++) {
            $dp[$i] = $window / $maxPts;
            if ($i < $k) $window += $dp[$i];
            else $ans += $dp[$i];
            if ($i - $maxPts >= 0 && $i - $maxPts < $k) $window -= $dp[$i - $maxPts];
        }
        return $ans;
    }
}
""")

add("0838_push_dominoes", r"""<?php
// LeetCode 0838 - Push Dominoes
// https://leetcode.com/problems/push-dominoes/

class Solution {
    /**
     * @param String $dominoes
     * @return String
     */
    function pushDominoes($dominoes) {
        $arr = str_split($dominoes);
        $n = count($arr);
        $force = array_fill(0, $n, 0);
        $f = 0;
        for ($i = 0; $i < $n; $i++) {
            if ($arr[$i] === 'R') $f = $n;
            elseif ($arr[$i] === 'L') $f = 0;
            else $f = max($f - 1, 0);
            $force[$i] += $f;
        }
        $f = 0;
        for ($i = $n - 1; $i >= 0; $i--) {
            if ($arr[$i] === 'L') $f = $n;
            elseif ($arr[$i] === 'R') $f = 0;
            else $f = max($f - 1, 0);
            $force[$i] -= $f;
        }
        for ($i = 0; $i < $n; $i++) {
            if ($force[$i] > 0) $arr[$i] = 'R';
            elseif ($force[$i] < 0) $arr[$i] = 'L';
            else $arr[$i] = '.';
        }
        return implode('', $arr);
    }
}
""")

add("0839_similar_string_groups", r"""<?php
// LeetCode 0839 - Similar String Groups
// https://leetcode.com/problems/similar-string-groups/

class Solution {
    /**
     * @param String[] $strs
     * @return Integer
     */
    function numSimilarGroups($strs) {
        $n = count($strs);
        $parent = range(0, $n - 1);
        $find = function($x) use (&$parent) {
            while ($parent[$x] !== $x) {
                $parent[$x] = $parent[$parent[$x]];
                $x = $parent[$x];
            }
            return $x;
        };
        $similar = function($a, $b) {
            $d0 = -1;
            $d1 = -1;
            $diffs = 0;
            $len = strlen($a);
            for ($i = 0; $i < $len; $i++) {
                if ($a[$i] !== $b[$i]) {
                    $diffs++;
                    if ($diffs > 2) return false;
                    if ($d0 < 0) $d0 = $i;
                    else $d1 = $i;
                }
            }
            return $diffs === 0 || ($diffs === 2 && $a[$d0] === $b[$d1] && $a[$d1] === $b[$d0]);
        };
        $groups = $n;
        for ($i = 0; $i < $n; $i++) {
            for ($j = $i + 1; $j < $n; $j++) {
                if ($similar($strs[$i], $strs[$j])) {
                    $pi = $find($i);
                    $pj = $find($j);
                    if ($pi !== $pj) {
                        $parent[$pi] = $pj;
                        $groups--;
                    }
                }
            }
        }
        return $groups;
    }
}
""")

add("0840_magic_squares_in_grid", r"""<?php
// LeetCode 0840 - Magic Squares In Grid
// https://leetcode.com/problems/magic-squares-in-grid/

class Solution {
    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function numMagicSquaresInside($grid) {
        $rows = count($grid);
        $cols = count($grid[0]);
        if ($rows < 3 || $cols < 3) return 0;
        $magic = function($r, $c) use ($grid) {
            $vals = [];
            for ($i = 0; $i < 3; $i++) for ($j = 0; $j < 3; $j++) $vals[] = $grid[$r + $i][$c + $j];
            sort($vals);
            for ($i = 0; $i < 9; $i++) if ($vals[$i] !== $i + 1) return false;
            return $grid[$r][$c] + $grid[$r][$c + 1] + $grid[$r][$c + 2] === 15
                && $grid[$r + 1][$c] + $grid[$r + 1][$c + 1] + $grid[$r + 1][$c + 2] === 15
                && $grid[$r + 2][$c] + $grid[$r + 2][$c + 1] + $grid[$r + 2][$c + 2] === 15
                && $grid[$r][$c] + $grid[$r + 1][$c] + $grid[$r + 2][$c] === 15
                && $grid[$r][$c + 1] + $grid[$r + 1][$c + 1] + $grid[$r + 2][$c + 1] === 15
                && $grid[$r][$c + 2] + $grid[$r + 1][$c + 2] + $grid[$r + 2][$c + 2] === 15
                && $grid[$r][$c] + $grid[$r + 1][$c + 1] + $grid[$r + 2][$c + 2] === 15
                && $grid[$r][$c + 2] + $grid[$r + 1][$c + 1] + $grid[$r + 2][$c] === 15;
        };
        $ans = 0;
        for ($i = 0; $i < $rows - 2; $i++) {
            for ($j = 0; $j < $cols - 2; $j++) {
                if ($magic($i, $j)) $ans++;
            }
        }
        return $ans;
    }
}
""")

add("0841_keys_and_rooms", r"""<?php
// LeetCode 0841 - Keys and Rooms
// https://leetcode.com/problems/keys-and-rooms/

class Solution {
    /**
     * @param Integer[][] $rooms
     * @return Boolean
     */
    function canVisitAllRooms($rooms) {
        $seen = [0 => true];
        $stack = [0];
        while (count($stack)) {
            $room = array_pop($stack);
            foreach ($rooms[$room] as $key) {
                if (!isset($seen[$key])) {
                    $seen[$key] = true;
                    $stack[] = $key;
                }
            }
        }
        return count($seen) === count($rooms);
    }
}
""")

add("0842_split_array_into_fibonacci_sequence", r"""<?php
// LeetCode 0842 - Split Array into Fibonacci Sequence
// https://leetcode.com/problems/split-array-into-fibonacci-sequence/

class Solution {
    /**
     * @param String $num
     * @return Integer[]
     */
    function splitIntoFibonacci($num) {
        $path = [];
        $dfs = function($start) use (&$dfs, $num, &$path) {
            $n = strlen($num);
            if ($start === $n) return count($path) >= 3;
            $val = 0;
            for ($end = $start; $end < $n; $end++) {
                if ($num[$start] === '0' && $end > $start) break;
                $val = $val * 10 + (ord($num[$end]) - 48);
                if ($val > 2147483647) break;
                if (count($path) >= 2) {
                    $total = $path[count($path) - 1] + $path[count($path) - 2];
                    if ($val < $total) continue;
                    if ($val > $total) break;
                }
                $path[] = $val;
                if ($dfs($end + 1)) return true;
                array_pop($path);
            }
            return false;
        };
        $dfs(0);
        return $path;
    }
}
""")

add("0843_guess_the_word", r"""<?php
// LeetCode 0843 - Guess the Word
// https://leetcode.com/problems/guess-the-word/

class Solution {
    /**
     * @param String[] $words
     * @param Master $master
     * @return NULL
     */
    function findSecretWord($words, $master) {
        $match = function($a, $b) {
            $m = 0;
            $len = strlen($a);
            for ($i = 0; $i < $len; $i++) if ($a[$i] === $b[$i]) $m++;
            return $m;
        };
        $candidates = $words;
        while (count($candidates)) {
            $best = $candidates[0];
            $bestWorst = count($candidates) + 1;
            foreach ($candidates as $w) {
                $buckets = array_fill(0, 7, 0);
                foreach ($candidates as $c) $buckets[$match($w, $c)]++;
                $worst = 0;
                foreach ($buckets as $b) $worst = max($worst, $b);
                if ($worst < $bestWorst) {
                    $bestWorst = $worst;
                    $best = $w;
                }
            }
            $score = $master->guess($best);
            if ($score === 6) return;
            $next = [];
            foreach ($candidates as $c) {
                if ($match($c, $best) === $score) $next[] = $c;
            }
            $candidates = $next;
        }
    }
}
""")

add("0844_backspace_string_compare", r"""<?php
// LeetCode 0844 - Backspace String Compare
// https://leetcode.com/problems/backspace-string-compare/

class Solution {
    /**
     * @param String $s
     * @param String $t
     * @return Boolean
     */
    function backspaceCompare($s, $t) {
        $build = function($text) {
            $stack = [];
            $n = strlen($text);
            for ($i = 0; $i < $n; $i++) {
                $ch = $text[$i];
                if ($ch === '#') {
                    if (count($stack)) array_pop($stack);
                } else {
                    $stack[] = $ch;
                }
            }
            return implode('', $stack);
        };
        return $build($s) === $build($t);
    }
}
""")

add("0845_longest_mountain_in_array", r"""<?php
// LeetCode 0845 - Longest Mountain in Array
// https://leetcode.com/problems/longest-mountain-in-array/

class Solution {
    /**
     * @param Integer[] $arr
     * @return Integer
     */
    function longestMountain($arr) {
        $n = count($arr);
        $ans = 0;
        $i = 0;
        while ($i < $n) {
            $j = $i;
            if ($j + 1 < $n && $arr[$j] < $arr[$j + 1]) {
                while ($j + 1 < $n && $arr[$j] < $arr[$j + 1]) $j++;
                if ($j + 1 < $n && $arr[$j] > $arr[$j + 1]) {
                    while ($j + 1 < $n && $arr[$j] > $arr[$j + 1]) $j++;
                    $ans = max($ans, $j - $i + 1);
                    $i = $j;
                    continue;
                }
            }
            $i++;
        }
        return $ans;
    }
}
""")

add("0846_hand_of_straights", r"""<?php
// LeetCode 0846 - Hand of Straights
// https://leetcode.com/problems/hand-of-straights/

class Solution {
    /**
     * @param Integer[] $hand
     * @param Integer $groupSize
     * @return Boolean
     */
    function isNStraightHand($hand, $groupSize) {
        if (count($hand) % $groupSize !== 0) return false;
        $count = [];
        foreach ($hand as $x) $count[$x] = ($count[$x] ?? 0) + 1;
        $keys = array_keys($count);
        sort($keys);
        foreach ($keys as $start) {
            $need = $count[$start] ?? 0;
            if ($need === 0) continue;
            for ($x = $start; $x < $start + $groupSize; $x++) {
                $c = $count[$x] ?? 0;
                if ($c < $need) return false;
                $count[$x] = $c - $need;
            }
        }
        return true;
    }
}
""")

add("0847_shortest_path_visiting_all_nodes", r"""<?php
// LeetCode 0847 - Shortest Path Visiting All Nodes
// https://leetcode.com/problems/shortest-path-visiting-all-nodes/

class Solution {
    /**
     * @param Integer[][] $graph
     * @return Integer
     */
    function shortestPathLength($graph) {
        $n = count($graph);
        $target = (1 << $n) - 1;
        $queue = [];
        $seen = [];
        for ($i = 0; $i < $n; $i++) {
            $queue[] = [$i, 1 << $i, 0];
            $seen[($i << 20) | (1 << $i)] = true;
        }
        $qi = 0;
        while ($qi < count($queue)) {
            $node = $queue[$qi][0];
            $mask = $queue[$qi][1];
            $dist = $queue[$qi][2];
            $qi++;
            if ($mask === $target) return $dist;
            foreach ($graph[$node] as $nxt) {
                $nmask = $mask | (1 << $nxt);
                $state = ($nxt << 20) | $nmask;
                if (!isset($seen[$state])) {
                    $seen[$state] = true;
                    $queue[] = [$nxt, $nmask, $dist + 1];
                }
            }
        }
        return -1;
    }
}
""")

add("0848_shifting_letters", r"""<?php
// LeetCode 0848 - Shifting Letters
// https://leetcode.com/problems/shifting-letters/

class Solution {
    /**
     * @param String $s
     * @param Integer[] $shifts
     * @return String
     */
    function shiftingLetters($s, $shifts) {
        $arr = str_split($s);
        $total = 0;
        for ($i = count($arr) - 1; $i >= 0; $i--) {
            $total = ($total + $shifts[$i]) % 26;
            $arr[$i] = chr((ord($arr[$i]) - 97 + $total) % 26 + 97);
        }
        return implode('', $arr);
    }
}
""")

add("0849_maximize_distance_to_closest_person", r"""<?php
// LeetCode 0849 - Maximize Distance to Closest Person
// https://leetcode.com/problems/maximize-distance-to-closest-person/

class Solution {
    /**
     * @param Integer[] $seats
     * @return Integer
     */
    function maxDistToClosest($seats) {
        $n = count($seats);
        $prev = -1;
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            if ($seats[$i] === 1) {
                if ($prev === -1) $ans = $i;
                else $ans = max($ans, intdiv($i - $prev, 2));
                $prev = $i;
            }
        }
        return max($ans, $n - 1 - $prev);
    }
}
""")

add("0850_rectangle_area_ii", r"""<?php
// LeetCode 0850 - Rectangle Area II
// https://leetcode.com/problems/rectangle-area-ii/

class Solution {
    /**
     * @param Integer[][] $rectangles
     * @return Integer
     */
    function rectangleArea($rectangles) {
        $MOD = 1000000007;
        $events = [];
        foreach ($rectangles as $r) {
            $events[] = [$r[0], 1, $r[1], $r[3]];
            $events[] = [$r[2], -1, $r[1], $r[3]];
        }
        usort($events, function($a, $b) { return $a[0] <=> $b[0]; });
        $coveredLength = function($active) {
            if (!count($active)) return 0;
            $sorted = $active;
            usort($sorted, function($a, $b) { return $a[0] <=> $b[0]; });
            $total = 0;
            $curStart = $sorted[0][0];
            $curEnd = $sorted[0][1];
            $len = count($sorted);
            for ($i = 1; $i < $len; $i++) {
                $start = $sorted[$i][0];
                $end = $sorted[$i][1];
                if ($start > $curEnd) {
                    $total += $curEnd - $curStart;
                    $curStart = $start;
                    $curEnd = $end;
                } else {
                    $curEnd = max($curEnd, $end);
                }
            }
            $total += $curEnd - $curStart;
            return $total;
        };
        $active = [];
        $area = 0;
        $prevX = $events[0][0];
        foreach ($events as $e) {
            $x = $e[0];
            $typ = $e[1];
            $y1 = $e[2];
            $y2 = $e[3];
            $area += $coveredLength($active) * ($x - $prevX);
            if ($typ === 1) $active[] = [$y1, $y2];
            else {
                $len = count($active);
                for ($i = 0; $i < $len; $i++) {
                    if ($active[$i][0] === $y1 && $active[$i][1] === $y2) {
                        array_splice($active, $i, 1);
                        break;
                    }
                }
            }
            $prevX = $x;
        }
        return $area % $MOD;
    }
}
""")

add("0851_loud_and_rich", r"""<?php
// LeetCode 0851 - Loud and Rich
// https://leetcode.com/problems/loud-and-rich/

class Solution {
    /**
     * @param Integer[][] $richer
     * @param Integer[] $quiet
     * @return Integer[]
     */
    function loudAndRich($richer, $quiet) {
        $n = count($quiet);
        $graph = array_fill(0, $n, []);
        foreach ($richer as $e) $graph[$e[1]][] = $e[0];
        $ans = array_fill(0, $n, -1);
        $dfs = function($person) use (&$dfs, $graph, $quiet, &$ans) {
            if ($ans[$person] !== -1) return $ans[$person];
            $best = $person;
            foreach ($graph[$person] as $richerPerson) {
                $cand = $dfs($richerPerson);
                if ($quiet[$cand] < $quiet[$best]) $best = $cand;
            }
            $ans[$person] = $best;
            return $best;
        };
        for ($i = 0; $i < $n; $i++) $dfs($i);
        return $ans;
    }
}
""")

add("0852_peak_index_in_a_mountain_array", r"""<?php
// LeetCode 0852 - Peak Index in a Mountain Array
// https://leetcode.com/problems/peak-index-in-a-mountain-array/

class Solution {
    /**
     * @param Integer[] $arr
     * @return Integer
     */
    function peakIndexInMountainArray($arr) {
        $lo = 0;
        $hi = count($arr) - 1;
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi, 2);
            if ($arr[$mid] < $arr[$mid + 1]) $lo = $mid + 1;
            else $hi = $mid;
        }
        return $lo;
    }
}
""")

add("0853_car_fleet", r"""<?php
// LeetCode 0853 - Car Fleet
// https://leetcode.com/problems/car-fleet/

class Solution {
    /**
     * @param Integer $target
     * @param Integer[] $position
     * @param Integer[] $speed
     * @return Integer
     */
    function carFleet($target, $position, $speed) {
        $n = count($position);
        $cars = [];
        for ($i = 0; $i < $n; $i++) $cars[] = [$position[$i], $speed[$i]];
        usort($cars, function($a, $b) { return $b[0] <=> $a[0]; });
        $fleets = 0;
        $maxTime = 0;
        foreach ($cars as $car) {
            $time = ($target - $car[0]) / $car[1];
            if ($time > $maxTime) {
                $fleets++;
                $maxTime = $time;
            }
        }
        return $fleets;
    }
}
""")

add("0854_k_similar_strings", r"""<?php
// LeetCode 0854 - K-Similar Strings
// https://leetcode.com/problems/k-similar-strings/

class Solution {
    /**
     * @param String $s1
     * @param String $s2
     * @return Integer
     */
    function kSimilarity($s1, $s2) {
        if ($s1 === $s2) return 0;
        $neighbors = function($s) use ($s2) {
            $arr = str_split($s);
            $i = 0;
            while ($arr[$i] === $s2[$i]) $i++;
            $res = [];
            $len = count($arr);
            for ($j = $i + 1; $j < $len; $j++) {
                if ($arr[$j] === $s2[$i] && $arr[$j] !== $s2[$j]) {
                    $tmp = $arr[$i];
                    $arr[$i] = $arr[$j];
                    $arr[$j] = $tmp;
                    $res[] = implode('', $arr);
                    $tmp = $arr[$i];
                    $arr[$i] = $arr[$j];
                    $arr[$j] = $tmp;
                }
            }
            return $res;
        };
        $queue = [$s1];
        $dist = [$s1 => 0];
        $qi = 0;
        while ($qi < count($queue)) {
            $cur = $queue[$qi++];
            $d = $dist[$cur];
            foreach ($neighbors($cur) as $nxt) {
                if ($nxt === $s2) return $d + 1;
                if (!isset($dist[$nxt])) {
                    $dist[$nxt] = $d + 1;
                    $queue[] = $nxt;
                }
            }
        }
        return -1;
    }
}
""")


def main() -> None:
    ported = 0
    for folder, content in SOLUTIONS.items():
        path = ROOT / folder / "solution.php"
        path.write_text(content, encoding="utf-8", newline="\n")
        ported += 1
        print(f"wrote {folder}")
    print(f"wrote={ported}")


if __name__ == "__main__":
    main()

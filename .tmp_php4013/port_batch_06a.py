#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")

SOLUTIONS = {}

def add(folder, body):
    SOLUTIONS[folder] = body


add("2197_replace_non_coprime_numbers_in_array", r'''<?php
// LeetCode 2197 - Replace Non-Coprime Numbers in Array
// https://leetcode.com/problems/replace-non-coprime-numbers-in-array/

class Solution {
    function replaceNonCoprimes($nums) {
        $gcd = function($a, $b) {
            while ($b !== 0) {
                $t = $a % $b;
                $a = $b;
                $b = $t;
            }
            return $a;
        };
        $stack = [];
        foreach ($nums as $x0) {
            $x = $x0;
            while (count($stack) > 0) {
                $g = $gcd($stack[count($stack) - 1], $x);
                if ($g === 1) break;
                $x = intdiv($stack[count($stack) - 1], $g) * $x;
                array_pop($stack);
            }
            $stack[] = $x;
        }
        return $stack;
    }
}
''')

add("2198_number_of_single_divisor_triplets", r'''<?php
// LeetCode 2198 - Number of Single Divisor Triplets
// https://leetcode.com/problems/number-of-single-divisor-triplets/

class Solution {
    function solve($nums) {
        $freq = array_fill(0, 101, 0);
        foreach ($nums as $x) $freq[$x]++;
        $ans = 0;
        for ($a = 1; $a <= 100; $a++) {
            if (!$freq[$a]) continue;
            for ($b = $a; $b <= 100; $b++) {
                if (!$freq[$b]) continue;
                for ($c = $b; $c <= 100; $c++) {
                    if (!$freq[$c]) continue;
                    $s = $a + $b + $c;
                    $cnt = 0;
                    if ($s % $a === 0) $cnt++;
                    if ($s % $b === 0) $cnt++;
                    if ($s % $c === 0) $cnt++;
                    if ($cnt !== 1) continue;
                    if ($a === $b && $b === $c) $ans += $freq[$a] * ($freq[$a] - 1) * ($freq[$a] - 2);
                    else if ($a === $b) $ans += $freq[$a] * ($freq[$a] - 1) * $freq[$c] * 3;
                    else if ($b === $c) $ans += $freq[$b] * ($freq[$b] - 1) * $freq[$a] * 3;
                    else if ($a === $c) $ans += $freq[$a] * ($freq[$a] - 1) * $freq[$b] * 3;
                    else $ans += $freq[$a] * $freq[$b] * $freq[$c] * 6;
                }
            }
        }
        return $ans;
    }
}
''')

add("2200_find_all_k_distant_indices_in_an_array", r'''<?php
// LeetCode 2200 - Find All K-Distant Indices in an Array
// https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/

class Solution {
    function findKDistantIndices($nums, $key, $k) {
        $n = count($nums);
        $mark = array_fill(0, $n, false);
        for ($i = 0; $i < $n; $i++) {
            if ($nums[$i] === $key) {
                $l = max(0, $i - $k);
                $r = min($n - 1, $i + $k);
                for ($j = $l; $j <= $r; $j++) $mark[$j] = true;
            }
        }
        $ans = [];
        for ($i = 0; $i < $n; $i++) if ($mark[$i]) $ans[] = $i;
        return $ans;
    }
}
''')

add("2201_count_artifacts_that_can_be_extracted", r'''<?php
// LeetCode 2201 - Count Artifacts That Can Be Extracted
// https://leetcode.com/problems/count-artifacts-that-can-be-extracted/

class Solution {
    function digArtifacts($n, $artifacts, $dig) {
        $dug = [];
        foreach ($dig as $d) $dug[$d[0] . ',' . $d[1]] = true;
        $ans = 0;
        foreach ($artifacts as $a) {
            $ok = true;
            for ($r = $a[0]; $r <= $a[2] && $ok; $r++) {
                for ($c = $a[1]; $c <= $a[3]; $c++) {
                    if (!isset($dug[$r . ',' . $c])) { $ok = false; break; }
                }
            }
            if ($ok) $ans++;
        }
        return $ans;
    }
}
''')

add("2202_maximize_the_topmost_element_after_k_moves", r'''<?php
// LeetCode 2202 - Maximize the Topmost Element After K Moves
// https://leetcode.com/problems/maximize-the-topmost-element-after-k-moves/

class Solution {
    function maximumTop($nums, $k) {
        $n = count($nums);
        if ($n === 1) return $k % 2 !== 0 ? -1 : $nums[0];
        if ($k === 0) return $nums[0];
        $ans = -1;
        $limit = min($k - 1, $n);
        for ($i = 0; $i < $limit; $i++) $ans = max($ans, $nums[$i]);
        if ($k < $n) $ans = max($ans, $nums[$k]);
        return $ans;
    }
}
''')

add("2203_minimum_weighted_subgraph_with_the_required_paths", r'''<?php
// LeetCode 2203 - Minimum Weighted Subgraph With the Required Paths
// https://leetcode.com/problems/minimum-weighted-subgraph-with-the-required-paths/

class Solution {
    function minimumWeight($n, $edges, $src1, $src2, $dest) {
        $INF = PHP_INT_MAX / 4;
        $dijkstra = function($g, $src) use ($n, $INF) {
            $dist = array_fill(0, $n, $INF);
            $dist[$src] = 0;
            $pq = new SplPriorityQueue();
            $pq->insert($src, 0);
            while (!$pq->isEmpty()) {
                $u = $pq->extract();
                $d = $dist[$u];
                foreach ($g[$u] as $ew) {
                    $v = $ew[0];
                    $w = $ew[1];
                    if ($d + $w < $dist[$v]) {
                        $dist[$v] = $d + $w;
                        $pq->insert($v, -$dist[$v]);
                    }
                }
            }
            return $dist;
        };
        $g = array_fill(0, $n, []);
        $rg = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $g[$e[0]][] = [$e[1], $e[2]];
            $rg[$e[1]][] = [$e[0], $e[2]];
        }
        $d1 = $dijkstra($g, $src1);
        $d2 = $dijkstra($g, $src2);
        $dd = $dijkstra($rg, $dest);
        $ans = $INF;
        for ($i = 0; $i < $n; $i++) {
            if ($d1[$i] >= $INF || $d2[$i] >= $INF || $dd[$i] >= $INF) continue;
            $ans = min($ans, $d1[$i] + $d2[$i] + $dd[$i]);
        }
        return $ans >= $INF ? -1 : $ans;
    }
}
''')

add("2204_distance_to_a_cycle_in_undirected_graph", r'''<?php
// LeetCode 2204 - Distance to a Cycle in Undirected Graph
// https://leetcode.com/problems/distance-to-a-cycle-in-undirected-graph/

class Solution {
    function solve($n, $edges) {
        $g = array_fill(0, $n, []);
        $deg = array_fill(0, $n, 0);
        foreach ($edges as $e) {
            $g[$e[0]][] = $e[1];
            $g[$e[1]][] = $e[0];
            $deg[$e[0]]++;
            $deg[$e[1]]++;
        }
        $q = [];
        for ($i = 0; $i < $n; $i++) if ($deg[$i] === 1) $q[] = $i;
        $onCycle = array_fill(0, $n, true);
        $qi = 0;
        while ($qi < count($q)) {
            $u = $q[$qi++];
            $onCycle[$u] = false;
            foreach ($g[$u] as $v) {
                $deg[$v]--;
                if ($deg[$v] === 1) $q[] = $v;
            }
        }
        $ans = array_fill(0, $n, -1);
        $qq = [];
        for ($i = 0; $i < $n; $i++) if ($onCycle[$i]) {
            $ans[$i] = 0;
            $qq[] = $i;
        }
        $qi = 0;
        while ($qi < count($qq)) {
            $u = $qq[$qi++];
            foreach ($g[$u] as $v) if ($ans[$v] === -1) {
                $ans[$v] = $ans[$u] + 1;
                $qq[] = $v;
            }
        }
        return $ans;
    }
}
''')

add("2205_the_number_of_users_that_are_eligible_for_discount", r'''<?php
// LeetCode 2205 - The Number of Users That Are Eligible for Discount
// https://leetcode.com/problems/the-number-of-users-that-are-eligible-for-discount/

const QUERY = <<<'SQL'
CREATE FUNCTION getUserIDs(startDate DATE, endDate DATE, minAmount INT) RETURNS INT
READS SQL DATA
BEGIN
  RETURN (
    SELECT COUNT(DISTINCT user_id) AS user_cnt
    FROM Purchases
    WHERE time_stamp BETWEEN startDate AND endDate
      AND amount >= minAmount
  );
END
SQL;
''')

add("2206_divide_array_into_equal_pairs", r'''<?php
// LeetCode 2206 - Divide Array Into Equal Pairs
// https://leetcode.com/problems/divide-array-into-equal-pairs/

class Solution {
    function divideArray($nums) {
        $freq = [];
        foreach ($nums as $x) $freq[$x] = ($freq[$x] ?? 0) + 1;
        foreach ($freq as $c) if ($c % 2 !== 0) return false;
        return true;
    }
}
''')

add("2207_maximize_number_of_subsequences_in_a_string", r'''<?php
// LeetCode 2207 - Maximize Number of Subsequences in a String
// https://leetcode.com/problems/maximize-number-of-subsequences-in-a-string/

class Solution {
    function maximumSubsequenceCount($text, $pattern) {
        $a = $pattern[0];
        $b = $pattern[1];
        $count = function($s) use ($a, $b) {
            $ca = 0;
            $ans = 0;
            $n = strlen($s);
            for ($i = 0; $i < $n; $i++) {
                $ch = $s[$i];
                if ($ch === $b) $ans += $ca;
                if ($ch === $a) $ca++;
            }
            return $ans;
        };
        return max($count($a . $text), $count($text . $b));
    }
}
''')

add("2208_minimum_operations_to_halve_array_sum", r'''<?php
// LeetCode 2208 - Minimum Operations to Halve Array Sum
// https://leetcode.com/problems/minimum-operations-to-halve-array-sum/

class Solution {
    function halveArray($nums) {
        $pq = new SplPriorityQueue();
        $sum = 0.0;
        foreach ($nums as $x) {
            $pq->insert((float)$x, (float)$x);
            $sum += $x;
        }
        $target = $sum / 2.0;
        $ans = 0;
        while ($sum > $target) {
            $top = $pq->extract();
            $x = $top / 2.0;
            $sum -= $x;
            $pq->insert($x, $x);
            $ans++;
        }
        return $ans;
    }
}
''')

add("2209_minimum_white_tiles_after_covering_with_carpets", r'''<?php
// LeetCode 2209 - Minimum White Tiles After Covering With Carpets
// https://leetcode.com/problems/minimum-white-tiles-after-covering-with-carpets/

class Solution {
    function minimumWhiteTiles($floor, $numCarpets, $carpetLen) {
        $n = strlen($floor);
        $INF = 1 << 30;
        $dp = [];
        for ($c = 0; $c <= $numCarpets; $c++) $dp[$c] = array_fill(0, $n + 1, $INF);
        $dp[0][0] = 0;
        for ($j = 1; $j <= $n; $j++)
            $dp[0][$j] = $dp[0][$j - 1] + ($floor[$j - 1] === '1' ? 1 : 0);
        for ($c = 1; $c <= $numCarpets; $c++) {
            $dp[$c][0] = 0;
            for ($j = 1; $j <= $n; $j++) {
                $dp[$c][$j] = $dp[$c][$j - 1] + ($floor[$j - 1] === '1' ? 1 : 0);
                $start = max(0, $j - $carpetLen);
                $dp[$c][$j] = min($dp[$c][$j], $dp[$c - 1][$start]);
            }
        }
        return $dp[$numCarpets][$n];
    }
}
''')

add("2210_count_hills_and_valleys_in_an_array", r'''<?php
// LeetCode 2210 - Count Hills and Valleys in an Array
// https://leetcode.com/problems/count-hills-and-valleys-in-an-array/

class Solution {
    function countHillValley($nums) {
        $compact = [$nums[0]];
        $n = count($nums);
        for ($i = 1; $i < $n; $i++)
            if ($nums[$i] !== $compact[count($compact) - 1]) $compact[] = $nums[$i];
        $ans = 0;
        $m = count($compact);
        for ($i = 1; $i + 1 < $m; $i++)
            if (($compact[$i] > $compact[$i - 1] && $compact[$i] > $compact[$i + 1]) ||
                ($compact[$i] < $compact[$i - 1] && $compact[$i] < $compact[$i + 1]))
                $ans++;
        return $ans;
    }
}
''')

add("2211_count_collisions_on_a_road", r'''<?php
// LeetCode 2211 - Count Collisions on a Road
// https://leetcode.com/problems/count-collisions-on-a-road/

class Solution {
    function countCollisions($directions) {
        $i = 0;
        $j = strlen($directions) - 1;
        $n = strlen($directions);
        while ($i < $n && $directions[$i] === 'L') $i++;
        while ($j >= 0 && $directions[$j] === 'R') $j--;
        $ans = 0;
        for ($k = $i; $k <= $j; $k++) if ($directions[$k] !== 'S') $ans++;
        return $ans;
    }
}
''')

add("2212_maximum_points_in_an_archery_competition", r'''<?php
// LeetCode 2212 - Maximum Points in an Archery Competition
// https://leetcode.com/problems/maximum-points-in-an-archery-competition/

class Solution {
    function maximumBobPoints($numArrows, $aliceArrows) {
        $bestScore = -1;
        $best = array_fill(0, 12, 0);
        $bob = array_fill(0, 12, 0);
        $dfs = function($i, $remain, $score) use (&$dfs, &$bestScore, &$best, &$bob, $aliceArrows) {
            if ($i === 12) {
                if ($score > $bestScore) {
                    $bestScore = $score;
                    $best = $bob;
                    if ($remain > 0) $best[0] += $remain;
                }
                return;
            }
            $dfs($i + 1, $remain, $score);
            $need = $aliceArrows[$i] + 1;
            if ($remain >= $need) {
                $bob[$i] = $need;
                $dfs($i + 1, $remain - $need, $score + $i);
                $bob[$i] = 0;
            }
        };
        $dfs(0, $numArrows, 0);
        return $best;
    }
}
''')

add("2213_longest_substring_of_one_repeating_character", r'''<?php
// LeetCode 2213 - Longest Substring of One Repeating Character
// https://leetcode.com/problems/longest-substring-of-one-repeating-character/

class Solution {
    function longestRepeating($s_, $queryCharacters, $queryIndices) {
        $merge = function($a, $b) {
            if ($a === null || ($a['size'] ?? 0) === 0) return $b;
            if ($b === null || ($b['size'] ?? 0) === 0) return $a;
            $res = [
                'lChar' => $a['lChar'],
                'rChar' => $b['rChar'],
                'size' => $a['size'] + $b['size'],
                'best' => max($a['best'], $b['best']),
                'lLen' => $a['lLen'],
                'rLen' => $b['rLen'],
            ];
            if ($a['rChar'] === $b['lChar']) {
                $mid = $a['rLen'] + $b['lLen'];
                $res['best'] = max($res['best'], $mid);
                if ($a['lLen'] === $a['size']) $res['lLen'] = $a['size'] + $b['lLen'];
                if ($b['rLen'] === $b['size']) $res['rLen'] = $b['size'] + $a['rLen'];
            }
            return $res;
        };
        $s = str_split($s_);
        $n = count($s);
        $tree = array_fill(0, 4 * $n + 5, null);
        $build = function($idx, $l, $r) use (&$build, &$tree, &$s, $merge) {
            if ($l === $r) {
                $tree[$idx] = ['lChar' => $s[$l], 'rChar' => $s[$l], 'lLen' => 1, 'rLen' => 1, 'best' => 1, 'size' => 1];
                return;
            }
            $mid = ($l + $r) >> 1;
            $build($idx * 2, $l, $mid);
            $build($idx * 2 + 1, $mid + 1, $r);
            $tree[$idx] = $merge($tree[$idx * 2], $tree[$idx * 2 + 1]);
        };
        $update = function($idx, $l, $r, $pos, $ch) use (&$update, &$tree, &$s, $merge) {
            if ($l === $r) {
                $s[$pos] = $ch;
                $tree[$idx] = ['lChar' => $ch, 'rChar' => $ch, 'lLen' => 1, 'rLen' => 1, 'best' => 1, 'size' => 1];
                return;
            }
            $mid = ($l + $r) >> 1;
            if ($pos <= $mid) $update($idx * 2, $l, $mid, $pos, $ch);
            else $update($idx * 2 + 1, $mid + 1, $r, $pos, $ch);
            $tree[$idx] = $merge($tree[$idx * 2], $tree[$idx * 2 + 1]);
        };
        $build(1, 0, $n - 1);
        $ans = array_fill(0, count($queryIndices), 0);
        for ($i = 0; $i < count($queryIndices); $i++) {
            $update(1, 0, $n - 1, $queryIndices[$i], $queryCharacters[$i]);
            $ans[$i] = $tree[1]['best'];
        }
        return $ans;
    }
}
''')

add("2214_minimum_health_to_beat_game", r'''<?php
// LeetCode 2214 - Minimum Health to Beat Game
// https://leetcode.com/problems/minimum-health-to-beat-game/

class Solution {
    function solve($damage, $armor) {
        $sum = 0;
        $mx = 0;
        foreach ($damage as $d) { $sum += $d; $mx = max($mx, $d); }
        return $sum - min($armor, $mx) + 1;
    }
}
''')

add("2215_find_the_difference_of_two_arrays", r'''<?php
// LeetCode 2215 - Find the Difference of Two Arrays
// https://leetcode.com/problems/find-the-difference-of-two-arrays/

class Solution {
    function findDifference($nums1, $nums2) {
        $s1 = [];
        $s2 = [];
        foreach ($nums1 as $x) $s1[$x] = true;
        foreach ($nums2 as $x) $s2[$x] = true;
        $a = [];
        $b = [];
        foreach ($s1 as $x => $_) if (!isset($s2[$x])) $a[] = $x;
        foreach ($s2 as $x => $_) if (!isset($s1[$x])) $b[] = $x;
        return [$a, $b];
    }
}
''')

add("2216_minimum_deletions_to_make_array_beautiful", r'''<?php
// LeetCode 2216 - Minimum Deletions to Make Array Beautiful
// https://leetcode.com/problems/minimum-deletions-to-make-array-beautiful/

class Solution {
    function minDeletion($nums) {
        $ans = 0;
        $i = 0;
        $n = count($nums);
        while ($i + 1 < $n) {
            if ($nums[$i] === $nums[$i + 1]) { $ans++; $i++; }
            else $i += 2;
        }
        if (($n - $ans) % 2 !== 0) $ans++;
        return $ans;
    }
}
''')

add("2217_find_palindrome_with_fixed_length", r'''<?php
// LeetCode 2217 - Find Palindrome With Fixed Length
// https://leetcode.com/problems/find-palindrome-with-fixed-length/

class Solution {
    function kthPalindrome($queries, $intLength) {
        $half = ($intLength + 1) >> 1;
        $start = 1;
        for ($i = 1; $i < $half; $i++) $start *= 10;
        $total = $start * 9;
        $ans = array_fill(0, count($queries), 0);
        for ($i = 0; $i < count($queries); $i++) {
            $q = $queries[$i];
            if ($q > $total) { $ans[$i] = -1; continue; }
            $left = $start + $q - 1;
            $pal = $left;
            $x = $left;
            if ($intLength % 2 !== 0) $x = intdiv($x, 10);
            while ($x > 0) { $pal = $pal * 10 + $x % 10; $x = intdiv($x, 10); }
            $ans[$i] = $pal;
        }
        return $ans;
    }
}
''')

add("2218_maximum_value_of_k_coins_from_piles", r'''<?php
// LeetCode 2218 - Maximum Value of K Coins From Piles
// https://leetcode.com/problems/maximum-value-of-k-coins-from-piles/

class Solution {
    function maxValueOfCoins($piles, $k) {
        $dp = array_fill(0, $k + 1, 0);
        foreach ($piles as $pile) {
            $ndp = $dp;
            $sum = 0;
            $plen = count($pile);
            for ($take = 1; $take <= $plen && $take <= $k; $take++) {
                $sum += $pile[$take - 1];
                for ($j = $take; $j <= $k; $j++)
                    $ndp[$j] = max($ndp[$j], $dp[$j - $take] + $sum);
            }
            $dp = $ndp;
        }
        return $dp[$k];
    }
}
''')

add("2219_maximum_sum_score_of_array", r'''<?php
// LeetCode 2219 - Maximum Sum Score of Array
// https://leetcode.com/problems/maximum-sum-score-of-array/

class Solution {
    function solve($nums) {
        $total = 0;
        $pref = 0;
        foreach ($nums as $x) $total += $x;
        $ans = PHP_INT_MIN;
        foreach ($nums as $x) {
            $pref += $x;
            $ans = max($ans, max($pref, $total - $pref + $x));
        }
        return $ans;
    }
}
''')

add("2220_minimum_bit_flips_to_convert_number", r'''<?php
// LeetCode 2220 - Minimum Bit Flips to Convert Number
// https://leetcode.com/problems/minimum-bit-flips-to-convert-number/

class Solution {
    function minBitFlips($start, $goal) {
        $x = $start ^ $goal;
        $ans = 0;
        while ($x > 0) { $ans += $x & 1; $x >>= 1; }
        return $ans;
    }
}
''')

add("2221_find_triangular_sum_of_an_array", r'''<?php
// LeetCode 2221 - Find Triangular Sum of an Array
// https://leetcode.com/problems/find-triangular-sum-of-an-array/

class Solution {
    function triangularSum($nums) {
        while (count($nums) > 1) {
            $next = [];
            $n = count($nums);
            for ($i = 0; $i < $n - 1; $i++)
                $next[] = ($nums[$i] + $nums[$i + 1]) % 10;
            $nums = $next;
        }
        return $nums[0];
    }
}
''')

add("2222_number_of_ways_to_select_buildings", r'''<?php
// LeetCode 2222 - Number of Ways to Select Buildings
// https://leetcode.com/problems/number-of-ways-to-select-buildings/

class Solution {
    function numberOfWays($s) {
        $total0 = 0;
        $total1 = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            if ($s[$i] === '0') $total0++;
            else $total1++;
        }
        $left0 = 0;
        $left1 = 0;
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            if ($s[$i] === '0') {
                $ans += $left1 * ($total1 - $left1);
                $left0++;
            } else {
                $ans += $left0 * ($total0 - $left0);
                $left1++;
            }
        }
        return $ans;
    }
}
''')

add("2223_sum_of_scores_of_built_strings", r'''<?php
// LeetCode 2223 - Sum of Scores of Built Strings
// https://leetcode.com/problems/sum-of-scores-of-built-strings/

class Solution {
    function sumScores($s) {
        $n = strlen($s);
        $z = array_fill(0, $n, 0);
        $l = 0;
        $r = 0;
        for ($i = 1; $i < $n; $i++) {
            if ($i <= $r) $z[$i] = min($r - $i + 1, $z[$i - $l]);
            while ($i + $z[$i] < $n && $s[$z[$i]] === $s[$i + $z[$i]]) $z[$i]++;
            if ($i + $z[$i] - 1 > $r) { $l = $i; $r = $i + $z[$i] - 1; }
        }
        $ans = $n;
        for ($i = 1; $i < $n; $i++) $ans += $z[$i];
        return $ans;
    }
}
''')

add("2224_minimum_number_of_operations_to_convert_time", r'''<?php
// LeetCode 2224 - Minimum Number of Operations to Convert Time
// https://leetcode.com/problems/minimum-number-of-operations-to-convert-time/

class Solution {
    function convertTime($current, $correct) {
        $toMin = function($t) {
            return (ord($t[0]) - 48) * 600 + (ord($t[1]) - 48) * 60
                + (ord($t[3]) - 48) * 10 + (ord($t[4]) - 48);
        };
        $diff = $toMin($correct) - $toMin($current);
        $ans = 0;
        foreach ([60, 15, 5, 1] as $step) {
            $ans += intdiv($diff, $step);
            $diff %= $step;
        }
        return $ans;
    }
}
''')

add("2225_find_players_with_zero_or_one_losses", r'''<?php
// LeetCode 2225 - Find Players With Zero or One Losses
// https://leetcode.com/problems/find-players-with-zero-or-one-losses/

class Solution {
    function findWinners($matches) {
        $lose = [];
        $seen = [];
        foreach ($matches as $m) {
            $seen[$m[0]] = true;
            $seen[$m[1]] = true;
            $lose[$m[1]] = ($lose[$m[1]] ?? 0) + 1;
        }
        $zero = [];
        $one = [];
        foreach ($seen as $p => $_) {
            $L = $lose[$p] ?? 0;
            if ($L === 0) $zero[] = $p;
            else if ($L === 1) $one[] = $p;
        }
        sort($zero);
        sort($one);
        return [$zero, $one];
    }
}
''')

add("2226_maximum_candies_allocated_to_k_children", r'''<?php
// LeetCode 2226 - Maximum Candies Allocated to K Children
// https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

class Solution {
    function maximumCandies($candies, $k) {
        $mx = 0;
        foreach ($candies as $c) $mx = max($mx, $c);
        $lo = 0;
        $hi = $mx;
        $can = function($mid) use ($candies, $k) {
            if ($mid === 0) return true;
            $cnt = 0;
            foreach ($candies as $c) {
                $cnt += intdiv($c, $mid);
                if ($cnt >= $k) return true;
            }
            return false;
        };
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi + 1, 2);
            if ($can($mid)) $lo = $mid;
            else $hi = $mid - 1;
        }
        return $lo;
    }
}
''')

add("2227_encrypt_and_decrypt_strings", r'''<?php
// LeetCode 2227 - Encrypt and Decrypt Strings
// https://leetcode.com/problems/encrypt-and-decrypt-strings/

class Encrypter {
    private $enc = [];
    private $cnt = [];

    function __construct($keys, $values, $dictionary) {
        for ($i = 0; $i < count($keys); $i++) $this->enc[$keys[$i]] = $values[$i];
        foreach ($dictionary as $w) {
            $e = $this->encrypt($w);
            $this->cnt[$e] = ($this->cnt[$e] ?? 0) + 1;
        }
    }

    function encrypt($word1) {
        $b = '';
        $n = strlen($word1);
        for ($i = 0; $i < $n; $i++) {
            $c = $word1[$i];
            if (!isset($this->enc[$c])) return '';
            $b .= $this->enc[$c];
        }
        return $b;
    }

    function decrypt($word2) {
        return $this->cnt[$word2] ?? 0;
    }
}
''')

add("2229_check_if_an_array_is_consecutive", r'''<?php
// LeetCode 2229 - Check if an Array Is Consecutive
// https://leetcode.com/problems/check-if-an-array-is-consecutive/

class Solution {
    function solve($nums) {
        $mn = $nums[0];
        $mx = $nums[0];
        $seen = [];
        foreach ($nums as $x) {
            if (isset($seen[$x])) return false;
            $seen[$x] = true;
            $mn = min($mn, $x);
            $mx = max($mx, $x);
        }
        return $mx - $mn + 1 === count($nums);
    }
}
''')

add("2230_the_users_that_are_eligible_for_discount", r'''<?php
// LeetCode 2230 - The Users That Are Eligible for Discount
// https://leetcode.com/problems/the-users-that-are-eligible-for-discount/

const QUERY = <<<'SQL'
CREATE PROCEDURE getUserIDs(startDate DATE, endDate DATE, minAmount INT)
BEGIN
  SELECT DISTINCT user_id
  FROM Purchases
  WHERE time_stamp BETWEEN startDate AND endDate
    AND amount >= minAmount
  ORDER BY user_id;
END
SQL;
''')

add("2231_largest_number_after_digit_swaps_by_parity", r'''<?php
// LeetCode 2231 - Largest Number After Digit Swaps by Parity
// https://leetcode.com/problems/largest-number-after-digit-swaps-by-parity/

class Solution {
    function largestInteger($num) {
        $digits = array_map('intval', str_split((string)$num));
        $even = [];
        $odd = [];
        foreach ($digits as $d) {
            if ($d % 2 === 0) $even[] = $d;
            else $odd[] = $d;
        }
        rsort($even);
        rsort($odd);
        $ei = 0;
        $oi = 0;
        $ans = 0;
        foreach ($digits as $d) {
            if ($d % 2 === 0) $ans = $ans * 10 + $even[$ei++];
            else $ans = $ans * 10 + $odd[$oi++];
        }
        return $ans;
    }
}
''')

add("2232_minimize_result_by_adding_parentheses_to_expression", r'''<?php
// LeetCode 2232 - Minimize Result by Adding Parentheses to Expression
// https://leetcode.com/problems/minimize-result-by-adding-parentheses-to-expression/

class Solution {
    function minimizeResult($expression) {
        $plus = strpos($expression, '+');
        $left = substr($expression, 0, $plus);
        $right = substr($expression, $plus + 1);
        $bestVal = PHP_INT_MAX;
        $best = '';
        for ($i = 0; $i < strlen($left); $i++) {
            for ($j = 1; $j <= strlen($right); $j++) {
                $a = substr($left, 0, $i);
                $b = substr($left, $i);
                $c = substr($right, 0, $j);
                $d = substr($right, $j);
                $val = intval($b) + intval($c);
                if (strlen($a)) $val *= intval($a);
                if (strlen($d)) $val *= intval($d);
                $cand = $a . '(' . $b . '+' . $c . ')' . $d;
                if ($val < $bestVal) { $bestVal = $val; $best = $cand; }
            }
        }
        return $best;
    }
}
''')

add("2233_maximum_product_after_k_increments", r'''<?php
// LeetCode 2233 - Maximum Product After K Increments
// https://leetcode.com/problems/maximum-product-after-k-increments/

class Solution {
    function maximumProduct($nums, $k) {
        $MOD = 1000000007;
        $pq = new SplPriorityQueue();
        foreach ($nums as $x) $pq->insert($x, -$x);
        for ($i = 0; $i < $k; $i++) {
            $x = $pq->extract();
            $pq->insert($x + 1, -($x + 1));
        }
        $ans = 1;
        while (!$pq->isEmpty()) $ans = $ans * $pq->extract() % $MOD;
        return $ans;
    }
}
''')

add("2234_maximum_total_beauty_of_the_gardens", r'''<?php
// LeetCode 2234 - Maximum Total Beauty of the Gardens
// https://leetcode.com/problems/maximum-total-beauty-of-the-gardens/

class Solution {
    function maximumBeauty($flowers, $newFlowers, $target, $full, $partial) {
        $n = count($flowers);
        for ($i = 0; $i < $n; $i++) if ($flowers[$i] > $target) $flowers[$i] = $target;
        sort($flowers);
        $sum = 0;
        foreach ($flowers as $f) $sum += $f;
        if ($target * $n - $sum <= $newFlowers) return $n * $full;
        $pref = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; $i++) $pref[$i + 1] = $pref[$i] + $flowers[$i];
        $ans = 0;
        $j = $n - 1;
        $remain = $newFlowers;
        for ($complete = 0; $complete <= $n; $complete++) {
            if ($complete > 0) {
                $need = $target - $flowers[$n - $complete];
                if ($remain < $need) break;
                $remain -= $need;
            }
            while ($j >= $n - $complete || ($j >= 0 && $flowers[$j] * ($j + 1) - $pref[$j + 1] > $remain)) $j--;
            $partialVal = 0;
            if ($j >= 0) {
                $extra = intdiv($remain - ($flowers[$j] * ($j + 1) - $pref[$j + 1]), $j + 1);
                $partialVal = $flowers[$j] + $extra;
                if ($partialVal >= $target) $partialVal = $target - 1;
            }
            $ans = max($ans, $complete * $full + $partialVal * $partial);
        }
        return $ans;
    }
}
''')

add("2235_add_two_integers", r'''<?php
// LeetCode 2235 - Add Two Integers
// https://leetcode.com/problems/add-two-integers/

class Solution {
    function sum($num1, $num2) {
        return $num1 + $num2;
    }
}
''')

written = 0
for folder, body in SOLUTIONS.items():
    path = ROOT / folder / "solution.php"
    path.write_text(body, encoding="utf-8", newline="\n")
    written += 1
print(f"wrote {written}")

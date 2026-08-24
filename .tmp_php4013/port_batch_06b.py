#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
SOLUTIONS = {}

def add(folder, body):
    SOLUTIONS[folder] = body

add("2236_root_equals_sum_of_children", r'''<?php
// LeetCode 2236 - Root Equals Sum of Children
// https://leetcode.com/problems/root-equals-sum-of-children/

class TreeNode {
    public $val = 0;
    public $left = null;
    public $right = null;
    function __construct($val = 0, $left = null, $right = null) {
        $this->val = $val;
        $this->left = $left;
        $this->right = $right;
    }
}

class Solution {
    function checkTree($root) {
        return $root->val === $root->left->val + $root->right->val;
    }
}
''')

add("2237_count_positions_on_street_with_required_brightness", r'''<?php
// LeetCode 2237 - Count Positions on Street With Required Brightness
// https://leetcode.com/problems/count-positions-on-street-with-required-brightness/

class Solution {
    function solve($n, $lights, $requirement) {
        $diff = array_fill(0, $n + 1, 0);
        foreach ($lights as $light) {
            $pos = $light[0];
            $r = $light[1];
            $l = max(0, $pos - $r);
            $rr = min($n - 1, $pos + $r);
            $diff[$l]++;
            $diff[$rr + 1]--;
        }
        $ans = 0;
        $cur = 0;
        for ($i = 0; $i < $n; $i++) {
            $cur += $diff[$i];
            if ($cur >= $requirement[$i]) $ans++;
        }
        return $ans;
    }
}
''')

add("2239_find_closest_number_to_zero", r'''<?php
// LeetCode 2239 - Find Closest Number to Zero
// https://leetcode.com/problems/find-closest-number-to-zero/

class Solution {
    function findClosestNumber($nums) {
        $ans = $nums[0];
        foreach ($nums as $x) {
            if (abs($x) < abs($ans) || (abs($x) === abs($ans) && $x > $ans)) $ans = $x;
        }
        return $ans;
    }
}
''')

add("2240_number_of_ways_to_buy_pens_and_pencils", r'''<?php
// LeetCode 2240 - Number of Ways to Buy Pens and Pencils
// https://leetcode.com/problems/number-of-ways-to-buy-pens-and-pencils/

class Solution {
    function waysToBuyPensPencils($total, $cost1, $cost2) {
        $ans = 0;
        for ($pens = 0; $pens * $cost1 <= $total; $pens++) {
            $remain = $total - $pens * $cost1;
            $ans += intdiv($remain, $cost2) + 1;
        }
        return $ans;
    }
}
''')

add("2241_design_an_atm_machine", r'''<?php
// LeetCode 2241 - Design an ATM Machine
// https://leetcode.com/problems/design-an-atm-machine/

class ATM {
    private $cnt;
    private $vals;

    function __construct() {
        $this->cnt = [0, 0, 0, 0, 0];
        $this->vals = [20, 50, 100, 200, 500];
    }

    function deposit($banknotesCount) {
        for ($i = 0; $i < 5; $i++) $this->cnt[$i] += $banknotesCount[$i];
    }

    function withdraw($amount) {
        $take = [0, 0, 0, 0, 0];
        $remain = $amount;
        $tmp = $this->cnt;
        for ($i = 4; $i >= 0; $i--) {
            $need = intdiv($remain, $this->vals[$i]);
            if ($need > $tmp[$i]) $need = $tmp[$i];
            $take[$i] = $need;
            $remain -= $need * $this->vals[$i];
        }
        if ($remain !== 0) return [-1];
        for ($i = 0; $i < 5; $i++) $this->cnt[$i] -= $take[$i];
        return $take;
    }
}
''')

add("2242_maximum_score_of_a_node_sequence", r'''<?php
// LeetCode 2242 - Maximum Score of a Node Sequence
// https://leetcode.com/problems/maximum-score-of-a-node-sequence/

class Solution {
    function maximumScore($scores, $edges) {
        $n = count($scores);
        $top = array_fill(0, $n, []);
        $g = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $g[$e[0]][] = $e[1];
            $g[$e[1]][] = $e[0];
        }
        for ($i = 0; $i < $n; $i++) {
            foreach ($g[$i] as $v) {
                $top[$i][] = $v;
                for ($j = count($top[$i]) - 1; $j > 0; $j--) {
                    if ($scores[$top[$i][$j]] > $scores[$top[$i][$j - 1]]) {
                        $tmp = $top[$i][$j];
                        $top[$i][$j] = $top[$i][$j - 1];
                        $top[$i][$j - 1] = $tmp;
                    }
                }
                if (count($top[$i]) > 3) $top[$i] = array_slice($top[$i], 0, 3);
            }
        }
        $ans = -1;
        foreach ($edges as $e) {
            $a = $e[0];
            $b = $e[1];
            foreach ($top[$a] as $c) {
                if ($c === $b) continue;
                foreach ($top[$b] as $d) {
                    if ($d === $a || $d === $c) continue;
                    $ans = max($ans, $scores[$a] + $scores[$b] + $scores[$c] + $scores[$d]);
                }
            }
        }
        return $ans;
    }
}
''')

add("2243_calculate_digit_sum_of_a_string", r'''<?php
// LeetCode 2243 - Calculate Digit Sum of a String
// https://leetcode.com/problems/calculate-digit-sum-of-a-string/

class Solution {
    function digitSum($s, $k) {
        while (strlen($s) > $k) {
            $next = '';
            $n = strlen($s);
            for ($i = 0; $i < $n; $i += $k) {
                $sum = 0;
                $end = min($i + $k, $n);
                for ($j = $i; $j < $end; $j++) $sum += ord($s[$j]) - 48;
                $next .= (string)$sum;
            }
            $s = $next;
        }
        return $s;
    }
}
''')

add("2244_minimum_rounds_to_complete_all_tasks", r'''<?php
// LeetCode 2244 - Minimum Rounds to Complete All Tasks
// https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/

class Solution {
    function minimumRounds($tasks) {
        $freq = [];
        foreach ($tasks as $t) $freq[$t] = ($freq[$t] ?? 0) + 1;
        $ans = 0;
        foreach ($freq as $c) {
            if ($c === 1) return -1;
            $ans += intdiv($c + 2, 3);
        }
        return $ans;
    }
}
''')

add("2245_maximum_trailing_zeros_in_a_cornered_path", r'''<?php
// LeetCode 2245 - Maximum Trailing Zeros in a Cornered Path
// https://leetcode.com/problems/maximum-trailing-zeros-in-a-cornered-path/

class Solution {
    function maxTrailingZeros($grid) {
        $fact = function($x) {
            $t = 0;
            $f = 0;
            while ($x % 2 === 0) { $t++; $x = intdiv($x, 2); }
            while ($x % 5 === 0) { $f++; $x = intdiv($x, 5); }
            return [$t, $f];
        };
        $m = count($grid);
        $n = count($grid[0]);
        $left2 = [];
        $left5 = [];
        $up2 = [];
        $up5 = [];
        for ($i = 0; $i < $m; $i++) {
            $left2[$i] = array_fill(0, $n, 0);
            $left5[$i] = array_fill(0, $n, 0);
            $up2[$i] = array_fill(0, $n, 0);
            $up5[$i] = array_fill(0, $n, 0);
        }
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                $p = $fact($grid[$i][$j]);
                $left2[$i][$j] = $up2[$i][$j] = $p[0];
                $left5[$i][$j] = $up5[$i][$j] = $p[1];
                if ($j > 0) {
                    $left2[$i][$j] += $left2[$i][$j - 1];
                    $left5[$i][$j] += $left5[$i][$j - 1];
                }
                if ($i > 0) {
                    $up2[$i][$j] += $up2[$i - 1][$j];
                    $up5[$i][$j] += $up5[$i - 1][$j];
                }
            }
        }
        $ans = 0;
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                $cell = $fact($grid[$i][$j]);
                $L2 = $left2[$i][$j];
                $L5 = $left5[$i][$j];
                $R2 = $left2[$i][$n - 1] - $left2[$i][$j] + $cell[0];
                $R5 = $left5[$i][$n - 1] - $left5[$i][$j] + $cell[1];
                $U2 = $up2[$i][$j];
                $U5 = $up5[$i][$j];
                $D2 = $up2[$m - 1][$j] - $up2[$i][$j] + $cell[0];
                $D5 = $up5[$m - 1][$j] - $up5[$i][$j] + $cell[1];
                $cands = [
                    [$L2 + $U2 - $cell[0], $L5 + $U5 - $cell[1]],
                    [$L2 + $D2 - $cell[0], $L5 + $D5 - $cell[1]],
                    [$R2 + $U2 - $cell[0], $R5 + $U5 - $cell[1]],
                    [$R2 + $D2 - $cell[0], $R5 + $D5 - $cell[1]],
                ];
                foreach ($cands as $ab) $ans = max($ans, min($ab[0], $ab[1]));
            }
        }
        return $ans;
    }
}
''')

add("2246_longest_path_with_different_adjacent_characters", r'''<?php
// LeetCode 2246 - Longest Path With Different Adjacent Characters
// https://leetcode.com/problems/longest-path-with-different-adjacent-characters/

class Solution {
    function longestPath($parent, $s) {
        $n = count($parent);
        $g = array_fill(0, $n, []);
        for ($i = 1; $i < $n; $i++) $g[$parent[$i]][] = $i;
        $ans = 1;
        $dfs = function($u) use (&$dfs, &$ans, $g, $s) {
            $best1 = 0;
            $best2 = 0;
            foreach ($g[$u] as $v) {
                $len = $dfs($v);
                if ($s[$v] === $s[$u]) continue;
                if ($len > $best1) { $best2 = $best1; $best1 = $len; }
                else if ($len > $best2) $best2 = $len;
            }
            $ans = max($ans, 1 + $best1 + $best2);
            return 1 + $best1;
        };
        $dfs(0);
        return $ans;
    }
}
''')

add("2247_maximum_cost_of_trip_with_k_highways", r'''<?php
// LeetCode 2247 - Maximum Cost of Trip With K Highways
// https://leetcode.com/problems/maximum-cost-of-trip-with-k-highways/

class Solution {
    function solve($n, $highways, $k) {
        if ($k + 1 > $n) return -1;
        $g = array_fill(0, $n, []);
        foreach ($highways as $h) {
            $g[$h[0]][] = [$h[1], $h[2]];
            $g[$h[1]][] = [$h[0], $h[2]];
        }
        $dp = [];
        for ($mask = 0; $mask < (1 << $n); $mask++) $dp[$mask] = array_fill(0, $n, -1);
        for ($i = 0; $i < $n; $i++) $dp[1 << $i][$i] = 0;
        $ans = -1;
        for ($mask = 0; $mask < (1 << $n); $mask++) {
            $cities = 0;
            $tmp = $mask;
            while ($tmp) { $cities += $tmp & 1; $tmp >>= 1; }
            for ($u = 0; $u < $n; $u++) {
                if ($dp[$mask][$u] < 0) continue;
                if ($cities - 1 === $k) $ans = max($ans, $dp[$mask][$u]);
                foreach ($g[$u] as $vw) {
                    $v = $vw[0];
                    $w = $vw[1];
                    if (($mask & (1 << $v)) !== 0) continue;
                    $nm = $mask | (1 << $v);
                    $dp[$nm][$v] = max($dp[$nm][$v], $dp[$mask][$u] + $w);
                }
            }
        }
        return $ans;
    }
}
''')

add("2248_intersection_of_multiple_arrays", r'''<?php
// LeetCode 2248 - Intersection of Multiple Arrays
// https://leetcode.com/problems/intersection-of-multiple-arrays/

class Solution {
    function intersection($nums) {
        $freq = [];
        foreach ($nums as $arr) {
            $seen = [];
            foreach ($arr as $x) {
                if (!isset($seen[$x])) {
                    $seen[$x] = true;
                    $freq[$x] = ($freq[$x] ?? 0) + 1;
                }
            }
        }
        $ans = [];
        foreach ($freq as $k => $v) if ($v === count($nums)) $ans[] = $k;
        sort($ans);
        return $ans;
    }
}
''')

add("2249_count_lattice_points_inside_a_circle", r'''<?php
// LeetCode 2249 - Count Lattice Points Inside a Circle
// https://leetcode.com/problems/count-lattice-points-inside-a-circle/

class Solution {
    function countLatticePoints($circles) {
        $seen = [];
        foreach ($circles as $c) {
            $x = $c[0];
            $y = $c[1];
            $r = $c[2];
            for ($i = $x - $r; $i <= $x + $r; $i++)
                for ($j = $y - $r; $j <= $y + $r; $j++)
                    if (($i - $x) * ($i - $x) + ($j - $y) * ($j - $y) <= $r * $r)
                        $seen[$i . ',' . $j] = true;
        }
        return count($seen);
    }
}
''')

add("2250_count_number_of_rectangles_containing_each_point", r'''<?php
// LeetCode 2250 - Count Number of Rectangles Containing Each Point
// https://leetcode.com/problems/count-number-of-rectangles-containing-each-point/

class Solution {
    function countRectangles($rectangles, $points) {
        $byH = [];
        for ($h = 0; $h <= 100; $h++) $byH[$h] = [];
        foreach ($rectangles as $r) $byH[$r[1]][] = $r[0];
        for ($h = 1; $h <= 100; $h++) sort($byH[$h]);
        $ans = array_fill(0, count($points), 0);
        for ($i = 0; $i < count($points); $i++) {
            $x = $points[$i][0];
            $y = $points[$i][1];
            $cnt = 0;
            for ($h = $y; $h <= 100; $h++) {
                $xs = $byH[$h];
                $lo = 0;
                $hi = count($xs);
                while ($lo < $hi) {
                    $mid = ($lo + $hi) >> 1;
                    if ($xs[$mid] < $x) $lo = $mid + 1;
                    else $hi = $mid;
                }
                $cnt += count($xs) - $lo;
            }
            $ans[$i] = $cnt;
        }
        return $ans;
    }
}
''')

add("2251_number_of_flowers_in_full_bloom", r'''<?php
// LeetCode 2251 - Number of Flowers in Full Bloom
// https://leetcode.com/problems/number-of-flowers-in-full-bloom/

class Solution {
    function fullBloomFlowers($flowers, $people) {
        $start = [];
        $end = [];
        foreach ($flowers as $f) { $start[] = $f[0]; $end[] = $f[1]; }
        sort($start);
        sort($end);
        $upperBound = function($a, $t) {
            $lo = 0;
            $hi = count($a);
            while ($lo < $hi) {
                $mid = ($lo + $hi) >> 1;
                if ($a[$mid] <= $t) $lo = $mid + 1;
                else $hi = $mid;
            }
            return $lo;
        };
        $lowerBound = function($a, $t) {
            $lo = 0;
            $hi = count($a);
            while ($lo < $hi) {
                $mid = ($lo + $hi) >> 1;
                if ($a[$mid] < $t) $lo = $mid + 1;
                else $hi = $mid;
            }
            return $lo;
        };
        $ans = array_fill(0, count($people), 0);
        for ($i = 0; $i < count($people); $i++) {
            $t = $people[$i];
            $ans[$i] = $upperBound($start, $t) - $lowerBound($end, $t);
        }
        return $ans;
    }
}
''')

add("2254_design_video_sharing_platform", r'''<?php
// LeetCode 2254 - Design Video Sharing Platform
// https://leetcode.com/problems/design-video-sharing-platform/

class VideoSharingPlatform {
    private $nextID = 0;
    private $free;
    private $videos = [];
    private $views = [];
    private $likes = [];
    private $dislikes = [];

    function __construct() {
        $this->free = new SplPriorityQueue();
    }

    function upload($video) {
        if (!$this->free->isEmpty()) $id = $this->free->extract();
        else $id = $this->nextID++;
        $this->videos[$id] = $video;
        $this->views[$id] = 0;
        $this->likes[$id] = 0;
        $this->dislikes[$id] = 0;
        return $id;
    }

    function remove($videoId) {
        if (!isset($this->videos[$videoId])) return;
        unset($this->videos[$videoId], $this->views[$videoId], $this->likes[$videoId], $this->dislikes[$videoId]);
        $this->free->insert($videoId, -$videoId);
    }

    function watch($videoId, $startMinute, $endMinute) {
        if (!isset($this->videos[$videoId])) return '-1';
        $v = $this->videos[$videoId];
        $this->views[$videoId]++;
        if ($startMinute >= strlen($v)) return '';
        $endMinute = min($endMinute, strlen($v) - 1);
        return substr($v, $startMinute, $endMinute - $startMinute + 1);
    }

    function like($videoId) {
        if (isset($this->videos[$videoId])) $this->likes[$videoId]++;
    }

    function dislike($videoId) {
        if (isset($this->videos[$videoId])) $this->dislikes[$videoId]++;
    }

    function getLikesAndDislikes($videoId) {
        if (!isset($this->videos[$videoId])) return [-1];
        return [$this->likes[$videoId], $this->dislikes[$videoId]];
    }

    function getViews($videoId) {
        if (!isset($this->videos[$videoId])) return -1;
        return $this->views[$videoId];
    }
}
''')

add("2255_count_prefixes_of_a_given_string", r'''<?php
// LeetCode 2255 - Count Prefixes of a Given String
// https://leetcode.com/problems/count-prefixes-of-a-given-string/

class Solution {
    function countPrefixes($words, $s) {
        $ans = 0;
        foreach ($words as $w)
            if (strlen($w) <= strlen($s) && strncmp($s, $w, strlen($w)) === 0) $ans++;
        return $ans;
    }
}
''')

add("2256_minimum_average_difference", r'''<?php
// LeetCode 2256 - Minimum Average Difference
// https://leetcode.com/problems/minimum-average-difference/

class Solution {
    function minimumAverageDifference($nums) {
        $n = count($nums);
        $total = 0;
        foreach ($nums as $v) $total += $v;
        $left = 0;
        $bestDiff = PHP_INT_MAX;
        $bestIdx = 0;
        for ($i = 0; $i < $n; $i++) {
            $left += $nums[$i];
            $leftAvg = intdiv($left, $i + 1);
            $rightAvg = 0;
            if ($i !== $n - 1) $rightAvg = intdiv($total - $left, $n - $i - 1);
            $diff = abs($leftAvg - $rightAvg);
            if ($diff < $bestDiff) { $bestDiff = $diff; $bestIdx = $i; }
        }
        return $bestIdx;
    }
}
''')

add("2257_count_unguarded_cells_in_the_grid", r'''<?php
// LeetCode 2257 - Count Unguarded Cells in the Grid
// https://leetcode.com/problems/count-unguarded-cells-in-the-grid/

class Solution {
    function countUnguarded($m, $n, $guards, $walls) {
        $grid = [];
        for ($i = 0; $i < $m; $i++) $grid[$i] = array_fill(0, $n, 0);
        foreach ($walls as $w) $grid[$w[0]][$w[1]] = 2;
        foreach ($guards as $g) $grid[$g[0]][$g[1]] = 2;
        $dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];
        foreach ($guards as $g) {
            foreach ($dirs as $d) {
                $r = $g[0] + $d[0];
                $c = $g[1] + $d[1];
                while ($r >= 0 && $r < $m && $c >= 0 && $c < $n && $grid[$r][$c] !== 2) {
                    $grid[$r][$c] = 1;
                    $r += $d[0];
                    $c += $d[1];
                }
            }
        }
        $ans = 0;
        for ($i = 0; $i < $m; $i++)
            for ($j = 0; $j < $n; $j++)
                if ($grid[$i][$j] === 0) $ans++;
        return $ans;
    }
}
''')

add("2258_escape_the_spreading_fire", r'''<?php
// LeetCode 2258 - Escape the Spreading Fire
// https://leetcode.com/problems/escape-the-spreading-fire/

class Solution {
    function maximumMinutes($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        $inf = 1000000000;
        $fire = [];
        for ($i = 0; $i < $m; $i++) $fire[$i] = array_fill(0, $n, $inf);
        $q = [];
        for ($i = 0; $i < $m; $i++)
            for ($j = 0; $j < $n; $j++)
                if ($grid[$i][$j] === 1) { $fire[$i][$j] = 0; $q[] = [$i, $j]; }
        $dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];
        $qi = 0;
        while ($qi < count($q)) {
            [$r, $c] = $q[$qi++];
            foreach ($dirs as $d) {
                $nr = $r + $d[0];
                $nc = $c + $d[1];
                if ($nr < 0 || $nr >= $m || $nc < 0 || $nc >= $n || $grid[$nr][$nc] === 2 || $fire[$nr][$nc] !== $inf) continue;
                $fire[$nr][$nc] = $fire[$r][$c] + 1;
                $q[] = [$nr, $nc];
            }
        }
        $can = function($wait) use ($m, $n, $grid, $fire, $dirs) {
            if ($wait >= $fire[0][0]) return false;
            $vis = [];
            for ($i = 0; $i < $m; $i++) $vis[$i] = array_fill(0, $n, false);
            $qq = [[0, 0, $wait]];
            $vis[0][0] = true;
            $qi = 0;
            while ($qi < count($qq)) {
                [$r, $c, $t] = $qq[$qi++];
                foreach ($dirs as $d) {
                    $nr = $r + $d[0];
                    $nc = $c + $d[1];
                    $nt = $t + 1;
                    if ($nr < 0 || $nr >= $m || $nc < 0 || $nc >= $n || $grid[$nr][$nc] === 2 || $vis[$nr][$nc]) continue;
                    if ($nr === $m - 1 && $nc === $n - 1) {
                        if ($nt <= $fire[$nr][$nc]) return true;
                        continue;
                    }
                    if ($nt >= $fire[$nr][$nc]) continue;
                    $vis[$nr][$nc] = true;
                    $qq[] = [$nr, $nc, $nt];
                }
            }
            return false;
        };
        $lo = 0;
        $hi = $m * $n + 10;
        $ans = -1;
        while ($lo <= $hi) {
            $mid = ($lo + $hi) >> 1;
            if ($can($mid)) { $ans = $mid; $lo = $mid + 1; }
            else $hi = $mid - 1;
        }
        if ($ans >= $m * $n) return $inf;
        return $ans;
    }
}
''')

add("2259_remove_digit_from_number_to_maximize_result", r'''<?php
// LeetCode 2259 - Remove Digit From Number to Maximize Result
// https://leetcode.com/problems/remove-digit-from-number-to-maximize-result/

class Solution {
    function removeDigit($number, $digit) {
        $best = '';
        $n = strlen($number);
        for ($i = 0; $i < $n; $i++) {
            if ($number[$i] === $digit) {
                $cand = substr($number, 0, $i) . substr($number, $i + 1);
                if ($cand > $best) $best = $cand;
            }
        }
        return $best;
    }
}
''')

add("2260_minimum_consecutive_cards_to_pick_up", r'''<?php
// LeetCode 2260 - Minimum Consecutive Cards to Pick Up
// https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up/

class Solution {
    function minimumCardPickup($cards) {
        $last = [];
        $ans = -1;
        for ($i = 0; $i < count($cards); $i++) {
            if (isset($last[$cards[$i]])) {
                $diff = $i - $last[$cards[$i]] + 1;
                if ($ans === -1 || $diff < $ans) $ans = $diff;
            }
            $last[$cards[$i]] = $i;
        }
        return $ans;
    }
}
''')

add("2261_k_divisible_elements_subarrays", r'''<?php
// LeetCode 2261 - K Divisible Elements Subarrays
// https://leetcode.com/problems/k-divisible-elements-subarrays/

class Solution {
    function countDistinct($nums, $k, $p) {
        $n = count($nums);
        $seen = [];
        for ($i = 0; $i < $n; $i++) {
            $div = 0;
            $key = '';
            for ($j = $i; $j < $n; $j++) {
                if ($nums[$j] % $p === 0) $div++;
                if ($div > $k) break;
                $key .= ($nums[$j] + 1) . ',';
                $seen[$key] = true;
            }
        }
        return count($seen);
    }
}
''')

add("2262_total_appeal_of_a_string", r'''<?php
// LeetCode 2262 - Total Appeal of A String
// https://leetcode.com/problems/total-appeal-of-a-string/

class Solution {
    function appealSum($s) {
        $last = array_fill(0, 26, -1);
        $ans = 0;
        $cur = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $c = ord($s[$i]) - 97;
            $cur += $i - $last[$c];
            $last[$c] = $i;
            $ans += $cur;
        }
        return $ans;
    }
}
''')

add("2263_make_array_non_decreasing_or_non_increasing", r'''<?php
// LeetCode 2263 - Make Array Non-decreasing or Non-increasing
// https://leetcode.com/problems/make-array-non-decreasing-or-non-increasing/

class Solution {
    function solve($nums) {
        $cost = function($arr) {
            $pq = new SplPriorityQueue();
            $ans = 0;
            foreach ($arr as $x) {
                if (!$pq->isEmpty() && $pq->top() > $x) {
                    $t = $pq->extract();
                    $ans += $t - $x;
                    $pq->insert($x, $x);
                }
                $pq->insert($x, $x);
            }
            return $ans;
        };
        $rev = array_reverse($nums);
        return min($cost($nums), $cost($rev));
    }
}
''')

add("2264_largest_3_same_digit_number_in_string", r'''<?php
// LeetCode 2264 - Largest 3-Same-Digit Number in String
// https://leetcode.com/problems/largest-3-same-digit-number-in-string/

class Solution {
    function largestGoodInteger($num) {
        $best = '';
        $n = strlen($num);
        for ($i = 0; $i + 2 < $n; $i++) {
            if ($num[$i] === $num[$i + 1] && $num[$i] === $num[$i + 2]) {
                $cand = substr($num, $i, 3);
                if ($cand > $best) $best = $cand;
            }
        }
        return $best;
    }
}
''')

add("2265_count_nodes_equal_to_average_of_subtree", r'''<?php
// LeetCode 2265 - Count Nodes Equal to Average of Subtree
// https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

class TreeNode {
    public $val = 0;
    public $left = null;
    public $right = null;
    function __construct($val = 0, $left = null, $right = null) {
        $this->val = $val;
        $this->left = $left;
        $this->right = $right;
    }
}

class Solution {
    function averageOfSubtree($root) {
        $ans = 0;
        $dfs = function($node) use (&$dfs, &$ans) {
            if ($node === null) return [0, 0];
            $L = $dfs($node->left);
            $R = $dfs($node->right);
            $sum = $L[0] + $R[0] + $node->val;
            $cnt = $L[1] + $R[1] + 1;
            if (intdiv($sum, $cnt) === $node->val) $ans++;
            return [$sum, $cnt];
        };
        $dfs($root);
        return $ans;
    }
}
''')

add("2266_count_number_of_texts", r'''<?php
// LeetCode 2266 - Count Number of Texts
// https://leetcode.com/problems/count-number-of-texts/

class Solution {
    function countTexts($pressedKeys) {
        $mod = 1000000007;
        $n = strlen($pressedKeys);
        $dp = array_fill(0, $n + 1, 0);
        $dp[0] = 1;
        for ($i = 1; $i <= $n; $i++) {
            $dp[$i] = $dp[$i - 1];
            $maxPress = ($pressedKeys[$i - 1] === '7' || $pressedKeys[$i - 1] === '9') ? 4 : 3;
            for ($j = 2; $j <= $maxPress && $j <= $i; $j++) {
                if ($pressedKeys[$i - $j] !== $pressedKeys[$i - 1]) break;
                $dp[$i] = ($dp[$i] + $dp[$i - $j]) % $mod;
            }
        }
        return $dp[$n];
    }
}
''')

add("2267_check_if_there_is_a_valid_parentheses_string_path", r'''<?php
// LeetCode 2267 - Check if There Is a Valid Parentheses String Path
// https://leetcode.com/problems/check-if-there-is-a-valid-parentheses-string-path/

class Solution {
    function hasValidPath($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        if (($m + $n - 1) % 2 === 1 || $grid[0][0] === ')' || $grid[$m - 1][$n - 1] === '(') return false;
        $vis = [];
        $dfs = function($r, $c, $bal) use (&$dfs, &$vis, $m, $n, $grid) {
            if ($r >= $m || $c >= $n) return false;
            $bal += ($grid[$r][$c] === '(') ? 1 : -1;
            if ($bal < 0) return false;
            if ($r === $m - 1 && $c === $n - 1) return $bal === 0;
            $k = (($r * $n + $c) << 10) | $bal;
            if (isset($vis[$k])) return false;
            $vis[$k] = true;
            return $dfs($r + 1, $c, $bal) || $dfs($r, $c + 1, $bal);
        };
        return $dfs(0, 0, 0);
    }
}
''')

add("2268_minimum_number_of_keypresses", r'''<?php
// LeetCode 2268 - Minimum Number of Keypresses
// https://leetcode.com/problems/minimum-number-of-keypresses/

class Solution {
    function solve($s) {
        $freq = array_fill(0, 26, 0);
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) $freq[ord($s[$i]) - 97]++;
        rsort($freq);
        $ans = 0;
        for ($i = 0; $i < 26; $i++) {
            if ($freq[$i] === 0) break;
            $ans += $freq[$i] * (intdiv($i, 9) + 1);
        }
        return $ans;
    }
}
''')

written = 0
for folder, body in SOLUTIONS.items():
    path = ROOT / folder / "solution.php"
    path.write_text(body, encoding="utf-8", newline="\n")
    written += 1
print(f"wrote {written}")

#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
SOLUTIONS = {}

def add(folder, body):
    SOLUTIONS[folder] = body


add("3229_minimum_operations_to_make_array_equal_to_target", r'''<?php
// LeetCode 3229 - Minimum Operations to Make Array Equal to Target
// https://leetcode.com/problems/minimum-operations-to-make-array-equal-to-target/

class Solution {
    function minimumOperations($nums, $target) {
        $f = abs($target[0] - $nums[0]);
        $n = count($target);
        for ($i = 1; $i < $n; $i++) {
            $x = $target[$i] - $nums[$i];
            $y = $target[$i - 1] - $nums[$i - 1];
            if ($x * $y > 0) {
                $d = abs($x) - abs($y);
                if ($d > 0) $f += $d;
            } else {
                $f += abs($x);
            }
        }
        return $f;
    }
}
''')

add("3231_minimum_number_of_increasing_subsequence_to_be_removed", r'''<?php
// LeetCode 3231 - Minimum Number of Increasing Subsequence to Be Removed
// https://leetcode.com/problems/minimum-number-of-increasing-subsequence-to-be-removed/

class Solution {
    function minOperations($nums) {
        $g = [];
        foreach ($nums as $x) {
            $l = 0;
            $r = count($g);
            while ($l < $r) {
                $mid = ($l + $r) >> 1;
                if ($g[$mid] < $x) $r = $mid;
                else $l = $mid + 1;
            }
            if ($l === count($g)) $g[] = $x;
            else $g[$l] = $x;
        }
        return count($g);
    }
}
''')

add("3232_find_if_digit_game_can_be_won", r'''<?php
// LeetCode 3232 - Find if Digit Game Can Be Won
// https://leetcode.com/problems/find-if-digit-game-can-be-won/

class Solution {
    function canAliceWin($nums) {
        $a = 0;
        $b = 0;
        foreach ($nums as $x) {
            if ($x < 10) $a += $x;
            else $b += $x;
        }
        return $a !== $b;
    }
}
''')

add("3233_find_the_count_of_numbers_which_are_not_special", r'''<?php
// LeetCode 3233 - Find the Count of Numbers Which Are Not Special
// https://leetcode.com/problems/find-the-count-of-numbers-which-are-not-special/

class Solution {
    private static $primes = null;

    function nonSpecialCount($l, $r) {
        $M = 31623;
        if (self::$primes === null) {
            $primes = array_fill(0, $M + 1, true);
            $primes[0] = false;
            $primes[1] = false;
            for ($i = 2; $i <= $M; $i++) {
                if ($primes[$i]) {
                    for ($j = $i * 2; $j <= $M; $j += $i) $primes[$j] = false;
                }
            }
            self::$primes = $primes;
        }
        $primes = self::$primes;
        $lo = (int)ceil(sqrt($l));
        $hi = (int)floor(sqrt($r));
        $cnt = 0;
        for ($i = $lo; $i <= $hi; $i++) if ($primes[$i]) $cnt++;
        return $r - $l + 1 - $cnt;
    }
}
''')

add("3234_count_the_number_of_substrings_with_dominant_ones", r'''<?php
// LeetCode 3234 - Count the Number of Substrings With Dominant Ones
// https://leetcode.com/problems/count-the-number-of-substrings-with-dominant-ones/

class Solution {
    function numberOfSubstrings($s) {
        $n = strlen($s);
        $nxt = array_fill(0, $n + 1, 0);
        $nxt[$n] = $n;
        for ($i = $n - 1; $i >= 0; $i--) {
            $nxt[$i] = $nxt[$i + 1];
            if ($s[$i] === '0') $nxt[$i] = $i;
        }
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            $cnt0 = $s[$i] === '0' ? 1 : 0;
            $j = $i;
            while ($j < $n && $cnt0 * $cnt0 <= $n) {
                $cnt1 = $nxt[$j + 1] - $i - $cnt0;
                if ($cnt1 >= $cnt0 * $cnt0) {
                    $ans += min($nxt[$j + 1] - $j, $cnt1 - $cnt0 * $cnt0 + 1);
                }
                $j = $nxt[$j + 1];
                $cnt0++;
            }
        }
        return $ans;
    }
}
''')

add("3235_check_if_the_rectangle_corner_is_reachable", r'''<?php
// LeetCode 3235 - Check if the Rectangle Corner Is Reachable
// https://leetcode.com/problems/check-if-the-rectangle-corner-is-reachable/

class Solution {
    private $circles;
    private $n;
    private $vis;
    private $xCorner;
    private $yCorner;

    function canReachCorner($xCorner, $yCorner, $circles) {
        $this->circles = $circles;
        $this->n = count($circles);
        $this->vis = array_fill(0, $this->n, false);
        $this->xCorner = $xCorner;
        $this->yCorner = $yCorner;
        for ($i = 0; $i < $this->n; $i++) {
            $x = $circles[$i][0];
            $y = $circles[$i][1];
            $r = $circles[$i][2];
            if ($this->inCircle(0, 0, $x, $y, $r) || $this->inCircle($xCorner, $yCorner, $x, $y, $r)) return false;
            if (!$this->vis[$i] && $this->crossLeftTop($x, $y, $r) && $this->dfs($i)) return false;
        }
        return true;
    }

    private function inCircle($x, $y, $cx, $cy, $r) {
        $dx = $x - $cx;
        $dy = $y - $cy;
        return $dx * $dx + $dy * $dy <= $r * $r;
    }

    private function crossLeftTop($cx, $cy, $r) {
        $a = abs($cx) <= $r && $cy >= 0 && $cy <= $this->yCorner;
        $b = abs($cy - $this->yCorner) <= $r && $cx >= 0 && $cx <= $this->xCorner;
        return $a || $b;
    }

    private function crossRightBottom($cx, $cy, $r) {
        $a = abs($cx - $this->xCorner) <= $r && $cy >= 0 && $cy <= $this->yCorner;
        $b = abs($cy) <= $r && $cx >= 0 && $cx <= $this->xCorner;
        return $a || $b;
    }

    private function dfs($i) {
        $x1 = $this->circles[$i][0];
        $y1 = $this->circles[$i][1];
        $r1 = $this->circles[$i][2];
        if ($this->crossRightBottom($x1, $y1, $r1)) return true;
        $this->vis[$i] = true;
        for ($j = 0; $j < $this->n; $j++) {
            if ($this->vis[$j]) continue;
            $x2 = $this->circles[$j][0];
            $y2 = $this->circles[$j][1];
            $r2 = $this->circles[$j][2];
            if (($x1 - $x2) * ($x1 - $x2) + ($y1 - $y2) * ($y1 - $y2) > ($r1 + $r2) * ($r1 + $r2)) continue;
            if ($x1 * $r2 + $x2 * $r1 < ($r1 + $r2) * $this->xCorner
                && $y1 * $r2 + $y2 * $r1 < ($r1 + $r2) * $this->yCorner
                && $this->dfs($j)) return true;
        }
        return false;
    }
}
''')

add("3237_alt_and_tab_simulation", r'''<?php
// LeetCode 3237 - Alt and Tab Simulation
// https://leetcode.com/problems/alt-and-tab-simulation/

class Solution {
    function simulationResult($windows, $queries) {
        $n = count($windows);
        $s = array_fill(0, $n + 1, false);
        $ans = [];
        for ($i = count($queries) - 1; $i >= 0; $i--) {
            $q = $queries[$i];
            if (!$s[$q]) { $s[$q] = true; $ans[] = $q; }
        }
        foreach ($windows as $w) if (!$s[$w]) $ans[] = $w;
        return $ans;
    }
}
''')

add("3238_find_the_number_of_winning_players", r'''<?php
// LeetCode 3238 - Find the Number of Winning Players
// https://leetcode.com/problems/find-the-number-of-winning-players/

class Solution {
    function winningPlayerCount($n, $pick) {
        $cnt = [];
        for ($i = 0; $i < $n; $i++) $cnt[$i] = array_fill(0, 11, 0);
        $s = [];
        foreach ($pick as $p) {
            $x = $p[0];
            $y = $p[1];
            $cnt[$x][$y]++;
            if ($cnt[$x][$y] > $x) $s[$x] = true;
        }
        return count($s);
    }
}
''')

add("3239_minimum_number_of_flips_to_make_binary_grid_palindromic_i", r'''<?php
// LeetCode 3239 - Minimum Number of Flips to Make Binary Grid Palindromic I
// https://leetcode.com/problems/minimum-number-of-flips-to-make-binary-grid-palindromic-i/

class Solution {
    function minFlips($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        $cnt1 = 0;
        $cnt2 = 0;
        foreach ($grid as $row) {
            for ($j = 0; $j * 2 < $n; $j++) if ($row[$j] !== $row[$n - $j - 1]) $cnt1++;
        }
        for ($j = 0; $j < $n; $j++) {
            for ($i = 0; $i * 2 < $m; $i++) if ($grid[$i][$j] !== $grid[$m - $i - 1][$j]) $cnt2++;
        }
        return min($cnt1, $cnt2);
    }
}
''')

add("3240_minimum_number_of_flips_to_make_binary_grid_palindromic_ii", r'''<?php
// LeetCode 3240 - Minimum Number of Flips to Make Binary Grid Palindromic II
// https://leetcode.com/problems/minimum-number-of-flips-to-make-binary-grid-palindromic-ii/

class Solution {
    function minFlips($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        $ans = 0;
        for ($i = 0; $i < intdiv($m, 2); $i++) {
            for ($j = 0; $j < intdiv($n, 2); $j++) {
                $x = $m - $i - 1;
                $y = $n - $j - 1;
                $cnt1 = $grid[$i][$j] + $grid[$x][$j] + $grid[$i][$y] + $grid[$x][$y];
                $ans += min($cnt1, 4 - $cnt1);
            }
        }
        if ($m % 2 === 1 && $n % 2 === 1) $ans += $grid[intdiv($m, 2)][intdiv($n, 2)];
        $diff = 0;
        $ones = 0;
        if ($m % 2 === 1) {
            for ($j = 0; $j < intdiv($n, 2); $j++) {
                if ($grid[intdiv($m, 2)][$j] === $grid[intdiv($m, 2)][$n - $j - 1]) $ones += $grid[intdiv($m, 2)][$j] * 2;
                else $diff += 1;
            }
        }
        if ($n % 2 === 1) {
            for ($i = 0; $i < intdiv($m, 2); $i++) {
                if ($grid[$i][intdiv($n, 2)] === $grid[$m - $i - 1][intdiv($n, 2)]) $ones += $grid[$i][intdiv($n, 2)] * 2;
                else $diff += 1;
            }
        }
        if ($ones % 4 === 0 || $diff > 0) $ans += $diff;
        else $ans += 2;
        return $ans;
    }
}
''')

add("3241_time_taken_to_mark_all_nodes", r'''<?php
// LeetCode 3241 - Time Taken to Mark All Nodes
// https://leetcode.com/problems/time-taken-to-mark-all-nodes/

class Solution {
    private $tree;
    private $dp;
    private $ans;

    function timeTaken($edges) {
        $n = count($edges) + 1;
        $this->ans = array_fill(0, $n, 0);
        $this->tree = array_fill(0, $n, []);
        $this->dp = [];
        for ($i = 0; $i < $n; $i++) $this->dp[$i] = [[0, 0], [0, 0]];
        foreach ($edges as $e) {
            $this->tree[$e[0]][] = $e[1];
            $this->tree[$e[1]][] = $e[0];
        }
        $this->dfs(0, -1);
        $this->reroot(0, -1, 0);
        return $this->ans;
    }

    private function getTime($u) {
        return $u % 2 === 0 ? 2 : 1;
    }

    private function dfs($u, $prev) {
        $t1 = [0, 0];
        $t2 = [0, 0];
        foreach ($this->tree[$u] as $v) {
            if ($v === $prev) continue;
            $t = $this->dfs($v, $u) + $this->getTime($v);
            if ($t >= $t1[1]) { $t2 = $t1; $t1 = [$v, $t]; }
            else if ($t > $t2[1]) $t2 = [$v, $t];
        }
        $this->dp[$u][0] = $t1;
        $this->dp[$u][1] = $t2;
        return $t1[1];
    }

    private function reroot($u, $prev, $maxTime) {
        $this->ans[$u] = $maxTime;
        if ($this->dp[$u][0][1] > $this->ans[$u]) $this->ans[$u] = $this->dp[$u][0][1];
        foreach ($this->tree[$u] as $v) {
            if ($v === $prev) continue;
            $side = $this->dp[$u][0][1];
            if ($this->dp[$u][0][0] === $v) $side = $this->dp[$u][1][1];
            $newMax = max($maxTime, $side);
            $this->reroot($v, $u, $this->getTime($u) + $newMax);
        }
    }
}
''')

add("3242_design_neighbor_sum_service", r'''<?php
// LeetCode 3242 - Design Neighbor Sum Service
// https://leetcode.com/problems/design-neighbor-sum-service/

class NeighborSum {
    private $grid;
    private $d;
    private $dirs;

    function __construct($grid) {
        $this->grid = $grid;
        $this->d = [];
        $this->dirs = [
            [-1, 0, 1, 0, -1],
            [-1, 1, 1, -1, -1]
        ];
        for ($i = 0; $i < count($grid); $i++) {
            for ($j = 0; $j < count($grid[$i]); $j++) {
                $this->d[$grid[$i][$j]] = [$i, $j];
            }
        }
    }

    function cal($value, $k) {
        $p = $this->d[$value];
        $s = 0;
        for ($q = 0; $q < 4; $q++) {
            $x = $p[0] + $this->dirs[$k][$q];
            $y = $p[1] + $this->dirs[$k][$q + 1];
            if ($x >= 0 && $x < count($this->grid) && $y >= 0 && $y < count($this->grid[0])) $s += $this->grid[$x][$y];
        }
        return $s;
    }

    function adjacentSum($value) {
        return $this->cal($value, 0);
    }

    function diagonalSum($value) {
        return $this->cal($value, 1);
    }
}
''')

add("3243_shortest_distance_after_road_addition_queries_i", r'''<?php
// LeetCode 3243 - Shortest Distance After Road Addition Queries I
// https://leetcode.com/problems/shortest-distance-after-road-addition-queries-i/

class Solution {
    private $g;
    private $n;

    function shortestDistanceAfterQueries($n, $queries) {
        $this->n = $n;
        $this->g = array_fill(0, $n, []);
        for ($i = 0; $i < $n - 1; $i++) $this->g[$i][] = $i + 1;
        $ans = [];
        foreach ($queries as $q) {
            $this->g[$q[0]][] = $q[1];
            $ans[] = $this->bfs();
        }
        return $ans;
    }

    private function bfs() {
        $q = [0];
        $vis = array_fill(0, $this->n, false);
        $vis[0] = true;
        for ($d = 0; ; $d++) {
            $k = count($q);
            while ($k-- > 0) {
                $u = array_shift($q);
                if ($u === $this->n - 1) return $d;
                foreach ($this->g[$u] as $v) {
                    if (!$vis[$v]) { $vis[$v] = true; $q[] = $v; }
                }
            }
        }
    }
}
''')

add("3244_shortest_distance_after_road_addition_queries_ii", r'''<?php
// LeetCode 3244 - Shortest Distance After Road Addition Queries II
// https://leetcode.com/problems/shortest-distance-after-road-addition-queries-ii/

class Solution {
    function shortestDistanceAfterQueries($n, $queries) {
        $nxt = [];
        for ($i = 0; $i < $n - 1; $i++) $nxt[$i] = $i + 1;
        $cnt = $n - 1;
        $ans = [];
        foreach ($queries as $q) {
            $u = $q[0];
            $v = $q[1];
            if (isset($nxt[$u]) && $nxt[$u] > 0 && $nxt[$u] < $v) {
                $i = $nxt[$u];
                while ($i < $v) {
                    $cnt--;
                    $ni = $nxt[$i];
                    $nxt[$i] = 0;
                    $i = $ni;
                }
                $nxt[$u] = $v;
            }
            $ans[] = $cnt;
        }
        return $ans;
    }
}
''')

add("3245_alternating_groups_iii", r'''<?php
// LeetCode 3245 - Alternating Groups III
// https://leetcode.com/problems/alternating-groups-iii/

class SegTree3245 {
    public $n;
    public $treeIntervalCounts;
    public $treeIntervalLengths;

    function __construct($n_) {
        $this->n = $n_;
        $this->treeIntervalCounts = array_fill(0, 4 * $n_, 0);
        $this->treeIntervalLengths = array_fill(0, 4 * $n_, 0);
    }

    function add($i, $val) { $this->addRec(0, 0, $this->n - 1, $i, $val); }

    function addRec($treeIndex, $lo, $hi, $i, $val) {
        if ($lo === $hi) {
            $this->treeIntervalCounts[$treeIndex] += $val;
            $this->treeIntervalLengths[$treeIndex] = $this->treeIntervalCounts[$treeIndex] * $i;
            return;
        }
        $mid = ($lo + $hi) >> 1;
        if ($i <= $mid) $this->addRec(2 * $treeIndex + 1, $lo, $mid, $i, $val);
        else $this->addRec(2 * $treeIndex + 2, $mid + 1, $hi, $i, $val);
        $this->treeIntervalCounts[$treeIndex] = $this->treeIntervalCounts[2 * $treeIndex + 1] + $this->treeIntervalCounts[2 * $treeIndex + 2];
        $this->treeIntervalLengths[$treeIndex] = $this->treeIntervalLengths[2 * $treeIndex + 1] + $this->treeIntervalLengths[2 * $treeIndex + 2];
    }

    function queryIntervalCounts($i) { return $this->query($this->treeIntervalCounts, 0, 0, $this->n - 1, $i, $this->n - 1); }
    function queryIntervalLengths($i) { return $this->query($this->treeIntervalLengths, 0, 0, $this->n - 1, $i, $this->n - 1); }

    function query($tree, $treeIndex, $lo, $hi, $i, $j) {
        if ($i <= $lo && $hi <= $j) return $tree[$treeIndex];
        if ($j < $lo || $hi < $i) return 0;
        $mid = ($lo + $hi) >> 1;
        return $this->query($tree, $treeIndex * 2 + 1, $lo, $mid, $i, $j) + $this->query($tree, $treeIndex * 2 + 2, $mid + 1, $hi, $i, $j);
    }
}

class Solution {
    private $n;
    private $arr;
    private $tree;
    private $intervals;

    function numberOfAlternatingGroups($colors, $queries) {
        $this->n = count($colors);
        $n = $this->n;
        $ans = [];
        $this->arr = array_fill(0, 2 * $n - 1, 0);
        for ($i = 0; $i < $n; $i++) $this->arr[$i] = $colors[$i];
        for ($i = 0; $i < $n - 1; $i++) $this->arr[$n + $i] = $colors[$i];
        $this->tree = new SegTree3245(2 * $n - 1);
        $this->intervals = [];
        $st = 0;
        for ($i = 1; $i < 2 * $n - 1; $i++) {
            if ($this->arr[$i] === $this->arr[$i - 1]) { $this->insert($st, $i - 1); $st = $i; }
        }
        $this->insert($st, 2 * $n - 2);
        foreach ($queries as $query) {
            if ($query[0] === 1) $ans[] = $this->getNum($query[1]);
            else {
                $index = $query[1];
                $color = $query[2];
                if ($this->arr[$index] !== $color) {
                    $this->update($index, $color);
                    if ($index < $n - 1) $this->update($index + $n, $color);
                }
            }
        }
        return $ans;
    }

    private function pack($l, $r) { return $l . ',' . $r; }

    private function unpack($k) {
        $p = explode(',', $k);
        return [(int)$p[0], (int)$p[1]];
    }

    private function insert($l, $r) {
        $this->intervals[$this->pack($l, $r)] = true;
        if ($l < $this->n) $this->tree->add($r - $l + 1, 1);
    }

    private function remove($l, $r) {
        unset($this->intervals[$this->pack($l, $r)]);
        if ($l < $this->n) $this->tree->add($r - $l + 1, -1);
    }

    private function findInterval($target) {
        $bestL = -1;
        $bestR = -1;
        foreach ($this->intervals as $k => $_) {
            [$kl, $kr] = $this->unpack($k);
            if ($kl <= $target && $target <= $kr && $kl > $bestL) { $bestL = $kl; $bestR = $kr; }
        }
        return [$bestL, $bestR];
    }

    private function getNum($sz) {
        $numIntervals = $this->tree->queryIntervalCounts($sz);
        $sumIntervals = $this->tree->queryIntervalLengths($sz);
        $numAlternatingGroups = $sumIntervals - $numIntervals * $sz + $numIntervals;
        [$l, $r] = $this->findInterval($this->n);
        if ($l < 0 || $l >= $this->n || $r - $l + 1 < $sz) return $numAlternatingGroups;
        if ($r >= $this->n) {
            $nonDuplicateGroups = $this->n - $l;
            $numGroups = ($r - $l + 1) - $sz + 1;
            $extra = $numGroups - $nonDuplicateGroups;
            if ($extra > 0) $numAlternatingGroups -= $extra;
        }
        return $numAlternatingGroups;
    }

    private function update($index, $color) {
        if ($this->arr[$index] === $color) return;
        $this->arr[$index] = $color;
        [$start, $end] = $this->findInterval($index);
        $this->remove($start, $end);
        if ($start < $index && $index < $end) {
            $this->insert($start, $index - 1);
            $this->insert($index, $index);
            $this->insert($index + 1, $end);
            return;
        }
        if ($start === $index && $index < $end) $this->insert($start + 1, $end);
        if ($start < $index && $index === $end) $this->insert($start, $end - 1);
        $ns = $index;
        $ne = $index;
        for (;;) {
            $merged = false;
            foreach (array_keys($this->intervals) as $k) {
                [$kl, $kr] = $this->unpack($k);
                if ($kr + 1 === $ns && $this->arr[$kr] !== $this->arr[$ns]) {
                    $this->remove($kl, $kr);
                    $ns = $kl;
                    $merged = true;
                    break;
                }
            }
            if (!$merged) break;
        }
        for (;;) {
            $merged = false;
            foreach (array_keys($this->intervals) as $k) {
                [$kl, $kr] = $this->unpack($k);
                if ($kl === $ne + 1 && $this->arr[$kl] !== $this->arr[$ne]) {
                    $this->remove($kl, $kr);
                    $ne = $kr;
                    $merged = true;
                    break;
                }
            }
            if (!$merged) break;
        }
        $this->insert($ns, $ne);
    }
}
''')

add("3247_number_of_subsequences_with_odd_sum", r'''<?php
// LeetCode 3247 - Number of Subsequences with Odd Sum
// https://leetcode.com/problems/number-of-subsequences-with-odd-sum/

class Solution {
    function subsequenceCount($nums) {
        $mod = 1000000007;
        $f = [0, 0];
        foreach ($nums as $x) {
            $g = [0, 0];
            if ($x % 2 === 1) {
                $g[0] = ($f[0] + $f[1]) % $mod;
                $g[1] = ($f[0] + $f[1] + 1) % $mod;
            } else {
                $g[0] = ($f[0] + $f[0] + 1) % $mod;
                $g[1] = ($f[1] + $f[1]) % $mod;
            }
            $f = $g;
        }
        return $f[1];
    }
}
''')

add("3248_snake_in_matrix", r'''<?php
// LeetCode 3248 - Snake in Matrix
// https://leetcode.com/problems/snake-in-matrix/

class Solution {
    function finalPositionOfSnake($n, $commands) {
        $x = 0;
        $y = 0;
        foreach ($commands as $c) {
            if ($c[0] === 'U') $x--;
            else if ($c[0] === 'D') $x++;
            else if ($c[0] === 'L') $y--;
            else if ($c[0] === 'R') $y++;
        }
        return $x * $n + $y;
    }
}
''')

add("3249_count_the_number_of_good_nodes", r'''<?php
// LeetCode 3249 - Count the Number of Good Nodes
// https://leetcode.com/problems/count-the-number-of-good-nodes/

class Solution {
    private $g;
    private $ans;

    function countGoodNodes($edges) {
        $n = count($edges) + 1;
        $this->g = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $this->g[$e[0]][] = $e[1];
            $this->g[$e[1]][] = $e[0];
        }
        $this->ans = 0;
        $this->dfs(0, -1);
        return $this->ans;
    }

    private function dfs($a, $fa) {
        $pre = -1;
        $cnt = 1;
        $ok = 1;
        foreach ($this->g[$a] as $b) {
            if ($b !== $fa) {
                $cur = $this->dfs($b, $a);
                $cnt += $cur;
                if ($pre < 0) $pre = $cur;
                else if ($pre !== $cur) $ok = 0;
            }
        }
        $this->ans += $ok;
        return $cnt;
    }
}
''')

add("3250_find_the_count_of_monotonic_pairs_i", r'''<?php
// LeetCode 3250 - Find the Count of Monotonic Pairs I
// https://leetcode.com/problems/find-the-count-of-monotonic-pairs-i/

class Solution {
    function countOfPairs($nums) {
        $mod = 1000000007;
        $n = count($nums);
        $dp = array_fill(0, 51, 0);
        for ($a = 0; $a <= $nums[0]; $a++) $dp[$a] = 1;
        for ($i = 1; $i < $n; $i++) {
            $ndp = array_fill(0, 51, 0);
            $pref = array_fill(0, 52, 0);
            for ($a = 0; $a <= 50; $a++) $pref[$a + 1] = ($pref[$a] + $dp[$a]) % $mod;
            for ($a2 = 0; $a2 <= $nums[$i]; $a2++) {
                $b2 = $nums[$i] - $a2;
                $maxA1 = $a2;
                $lim = $nums[$i - 1] - $b2;
                if ($lim < $maxA1) $maxA1 = $lim;
                if ($maxA1 < 0) continue;
                if ($maxA1 > 50) $maxA1 = 50;
                $ndp[$a2] = $pref[$maxA1 + 1];
            }
            $dp = $ndp;
        }
        $ans = 0;
        foreach ($dp as $v) $ans = ($ans + $v) % $mod;
        return $ans;
    }
}
''')

add("3251_find_the_count_of_monotonic_pairs_ii", r'''<?php
// LeetCode 3251 - Find the Count of Monotonic Pairs II
// https://leetcode.com/problems/find-the-count-of-monotonic-pairs-ii/

class Solution {
    function countOfPairs($nums) {
        $mod = 1000000007;
        $n = count($nums);
        $maxV = 0;
        foreach ($nums as $v) $maxV = max($maxV, $v);
        $dp = array_fill(0, $maxV + 1, 0);
        for ($a = 0; $a <= $nums[0]; $a++) $dp[$a] = 1;
        for ($i = 1; $i < $n; $i++) {
            $ndp = array_fill(0, $maxV + 1, 0);
            $pref = array_fill(0, $maxV + 2, 0);
            for ($a = 0; $a <= $maxV; $a++) $pref[$a + 1] = ($pref[$a] + $dp[$a]) % $mod;
            for ($a2 = 0; $a2 <= $nums[$i]; $a2++) {
                $b2 = $nums[$i] - $a2;
                $maxA1 = $a2;
                $lim = $nums[$i - 1] - $b2;
                if ($lim < $maxA1) $maxA1 = $lim;
                if ($maxA1 < 0) continue;
                if ($maxA1 > $maxV) $maxA1 = $maxV;
                $ndp[$a2] = $pref[$maxA1 + 1];
            }
            $dp = $ndp;
        }
        $ans = 0;
        foreach ($dp as $v) $ans = ($ans + $v) % $mod;
        return $ans;
    }
}
''')

add("3253_construct_string_with_minimum_cost_easy", r'''<?php
// LeetCode 3253 - Construct String with Minimum Cost (Easy)
// https://leetcode.com/problems/construct-string-with-minimum-cost-easy/

class Solution {
    function minimumCost($target, $words, $costs) {
        $inf = 1e18;
        $n = strlen($target);
        $dp = array_fill(0, $n + 1, $inf);
        $dp[0] = 0;
        $best = [];
        for ($i = 0; $i < count($words); $i++) {
            $old = $best[$words[$i]] ?? null;
            if ($old === null || $costs[$i] < $old) $best[$words[$i]] = $costs[$i];
        }
        for ($i = 0; $i < $n; $i++) {
            if ($dp[$i] === $inf) continue;
            foreach ($best as $w => $c) {
                $L = strlen($w);
                if ($i + $L <= $n && substr($target, $i, $L) === $w && $dp[$i] + $c < $dp[$i + $L]) $dp[$i + $L] = $dp[$i] + $c;
            }
        }
        if ($dp[$n] === $inf) return -1;
        return $dp[$n];
    }
}
''')

add("3254_find_the_power_of_k_size_subarrays_i", r'''<?php
// LeetCode 3254 - Find the Power of K-Size Subarrays I
// https://leetcode.com/problems/find-the-power-of-k-size-subarrays-i/

class Solution {
    function resultsArray($nums, $k) {
        $n = count($nums);
        $ans = array_fill(0, $n - $k + 1, 0);
        for ($i = 0; $i <= $n - $k; $i++) {
            $ok = true;
            for ($j = $i + 1; $j < $i + $k; $j++) {
                if ($nums[$j] !== $nums[$j - 1] + 1) { $ok = false; break; }
            }
            $ans[$i] = $ok ? $nums[$i + $k - 1] : -1;
        }
        return $ans;
    }
}
''')

add("3255_find_the_power_of_k_size_subarrays_ii", r'''<?php
// LeetCode 3255 - Find the Power of K-Size Subarrays II
// https://leetcode.com/problems/find-the-power-of-k-size-subarrays-ii/

class Solution {
    function resultsArray($nums, $k) {
        $n = count($nums);
        $ans = array_fill(0, $n - $k + 1, 0);
        if ($k === 1) return $nums;
        $streak = 1;
        for ($i = 1; $i < $n; $i++) {
            if ($nums[$i] === $nums[$i - 1] + 1) $streak++;
            else $streak = 1;
            if ($i >= $k - 1) $ans[$i - $k + 1] = $streak >= $k ? $nums[$i] : -1;
        }
        return $ans;
    }
}
''')

add("3256_maximum_value_sum_by_placing_three_rooks_i", r'''<?php
// LeetCode 3256 - Maximum Value Sum by Placing Three Rooks I
// https://leetcode.com/problems/maximum-value-sum-by-placing-three-rooks-i/

class Solution {
    function maximumValueSum($board) {
        $m = count($board);
        $n = count($board[0]);
        $tops = [];
        for ($i = 0; $i < $m; $i++) {
            $row = [];
            for ($j = 0; $j < $n; $j++) {
                $cur = [$board[$i][$j], $j];
                $placed = false;
                for ($t = 0; $t < count($row); $t++) {
                    if ($cur[0] > $row[$t][0]) {
                        array_splice($row, $t, 0, [$cur]);
                        $placed = true;
                        break;
                    }
                }
                if (!$placed) $row[] = $cur;
                if (count($row) > 3) $row = array_slice($row, 0, 3);
            }
            $tops[] = $row;
        }
        $ans = PHP_INT_MIN;
        for ($i = 0; $i < $m; $i++) {
            foreach ($tops[$i] as $a) {
                for ($j = $i + 1; $j < $m; $j++) {
                    foreach ($tops[$j] as $b) {
                        if ($a[1] === $b[1]) continue;
                        for ($k = $j + 1; $k < $m; $k++) {
                            foreach ($tops[$k] as $c) {
                                if ($c[1] === $a[1] || $c[1] === $b[1]) continue;
                                $s = $a[0] + $b[0] + $c[0];
                                if ($s > $ans) $ans = $s;
                            }
                        }
                    }
                }
            }
        }
        return $ans;
    }
}
''')

add("3257_maximum_value_sum_by_placing_three_rooks_ii", r'''<?php
// LeetCode 3257 - Maximum Value Sum by Placing Three Rooks II
// https://leetcode.com/problems/maximum-value-sum-by-placing-three-rooks-ii/

class Solution {
    function maximumValueSum($board) {
        $m = count($board);
        $n = count($board[0]);
        $tops = [];
        for ($i = 0; $i < $m; $i++) {
            $row = [];
            for ($j = 0; $j < $n; $j++) {
                $cur = [$board[$i][$j], $j];
                $placed = false;
                for ($t = 0; $t < count($row); $t++) {
                    if ($cur[0] > $row[$t][0]) {
                        array_splice($row, $t, 0, [$cur]);
                        $placed = true;
                        break;
                    }
                }
                if (!$placed) $row[] = $cur;
                if (count($row) > 3) $row = array_slice($row, 0, 3);
            }
            $tops[] = $row;
        }
        $ans = PHP_INT_MIN;
        for ($i = 0; $i < $m; $i++) {
            foreach ($tops[$i] as $a) {
                for ($j = $i + 1; $j < $m; $j++) {
                    foreach ($tops[$j] as $b) {
                        if ($a[1] === $b[1]) continue;
                        for ($k = $j + 1; $k < $m; $k++) {
                            foreach ($tops[$k] as $c) {
                                if ($c[1] === $a[1] || $c[1] === $b[1]) continue;
                                $s = $a[0] + $b[0] + $c[0];
                                if ($s > $ans) $ans = $s;
                            }
                        }
                    }
                }
            }
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

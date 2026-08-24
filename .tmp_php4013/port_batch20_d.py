#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
SOLUTIONS = {}

def add(folder, body):
    SOLUTIONS[folder] = body


add("3797_count_routes_to_climb_a_rectangular_grid", r'''<?php
// LeetCode 3797 - Count Routes to Climb a Rectangular Grid
// https://leetcode.com/problems/count-routes-to-climb-a-rectangular-grid/

class Solution {
    function countRoutes($grid, $d) {
        $MOD = 1000000007;
        $n = count($grid);
        $m = count($grid[0]);
        $upRadius = 0;
        while (($upRadius + 1) * ($upRadius + 1) + 1 <= $d * $d) $upRadius++;
        $arrived = array_fill(0, $m, 0);
        for ($c = 0; $c < $m; $c++) {
            if ($grid[$n - 1][$c] === '.') $arrived[$c] = 1;
        }
        for ($r = $n - 1; $r >= 0; $r--) {
            $pref = array_fill(0, $m + 1, 0);
            for ($i = 0; $i < $m; $i++) $pref[$i + 1] = ($pref[$i] + $arrived[$i]) % $MOD;
            $horizontal = array_fill(0, $m, 0);
            for ($c = 0; $c < $m; $c++) {
                if ($grid[$r][$c] === '#') continue;
                $l = max(0, $c - $d);
                $rr = min($m - 1, $c + $d);
                $horizontal[$c] = ($pref[$rr + 1] - $pref[$l] - $arrived[$c]) % $MOD;
                if ($horizontal[$c] < 0) $horizontal[$c] += $MOD;
            }
            if ($r === 0) {
                $ans = 0;
                for ($c = 0; $c < $m; $c++) $ans = ($ans + $arrived[$c] + $horizontal[$c]) % $MOD;
                return $ans;
            }
            $pref2 = array_fill(0, $m + 1, 0);
            for ($c = 0; $c < $m; $c++) $pref2[$c + 1] = ($pref2[$c] + $arrived[$c] + $horizontal[$c]) % $MOD;
            $next = array_fill(0, $m, 0);
            for ($c = 0; $c < $m; $c++) {
                if ($grid[$r - 1][$c] === '#') continue;
                $l = max(0, $c - $upRadius);
                $rr = min($m - 1, $c + $upRadius);
                $next[$c] = $pref2[$rr + 1] - $pref2[$l];
                if ($next[$c] < 0) $next[$c] += $MOD;
            }
            $arrived = $next;
        }
        return 0;
    }
}
''')

add("3798_largest_even_number", r'''<?php
// LeetCode 3798 - Largest Even Number
// https://leetcode.com/problems/largest-even-number/

class Solution {
    function largestEven($s) {
        while (strlen($s) > 0 && $s[strlen($s) - 1] === '1') $s = substr($s, 0, strlen($s) - 1);
        return $s;
    }
}
''')

add("3799_word_squares_ii", r'''<?php
// LeetCode 3799 - Word Squares II
// https://leetcode.com/problems/word-squares-ii/

class Solution {
    function wordSquares($words) {
        sort($words);
        $n = count($words);
        $ans = [];
        for ($i = 0; $i < $n; $i++) {
            $top = $words[$i];
            for ($j = 0; $j < $n; $j++) {
                if ($j === $i) continue;
                $left = $words[$j];
                for ($k = 0; $k < $n; $k++) {
                    if ($k === $j || $k === $i) continue;
                    $right = $words[$k];
                    for ($h = 0; $h < $n; $h++) {
                        if ($h === $k || $h === $j || $h === $i) continue;
                        $bottom = $words[$h];
                        if ($top[0] === $left[0] && $top[3] === $right[0] &&
                            $bottom[0] === $left[3] && $bottom[3] === $right[3]) {
                            $ans[] = [$top, $left, $right, $bottom];
                        }
                    }
                }
            }
        }
        return $ans;
    }
}
''')

add("3800_minimum_cost_to_make_two_binary_strings_equal", r'''<?php
// LeetCode 3800 - Minimum Cost to Make Two Binary Strings Equal
// https://leetcode.com/problems/minimum-cost-to-make-two-binary-strings-equal/

class Solution {
    function minimumCost($s, $t, $flipCost, $swapCost, $crossCost) {
        $diff = [0, 0];
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            if ($s[$i] !== $t[$i]) $diff[ord($s[$i]) - 48]++;
        }
        $ans = ($diff[0] + $diff[1]) * $flipCost;
        $mx = max($diff[0], $diff[1]);
        $mn = min($diff[0], $diff[1]);
        $ans = min($ans, $mn * $swapCost + ($mx - $mn) * $flipCost);
        $avg = intdiv($mx + $mn, 2);
        $ans = min($ans, ($avg - $mn) * $crossCost + $avg * $swapCost + ($mx + $mn - $avg * 2) * $flipCost);
        return $ans;
    }
}
''')

add("3801_minimum_cost_to_merge_sorted_lists", r'''<?php
// LeetCode 3801 - Minimum Cost to Merge Sorted Lists
// https://leetcode.com/problems/minimum-cost-to-merge-sorted-lists/

class Solution {
    function minMergeCost($lists) {
        $m = count($lists);
        $totalMasks = 1 << $m;
        $merged = array_fill(0, $totalMasks, []);
        $length = array_fill(0, $totalMasks, 0);
        $median = array_fill(0, $totalMasks, 0);
        $trailingZeros = function($bit) {
            $n = 0;
            while (($bit & 1) === 0) { $bit >>= 1; $n++; }
            return $n;
        };
        for ($mask = 1; $mask < $totalMasks; $mask++) {
            $bit = $mask & -$mask;
            $index = $trailingZeros($bit);
            $previous = $merged[$mask ^ $bit];
            $current = $lists[$index];
            $out = [];
            $i = 0;
            $j = 0;
            while ($i < count($previous) || $j < count($current)) {
                if ($j === count($current) || ($i < count($previous) && $previous[$i] <= $current[$j])) {
                    $out[] = $previous[$i++];
                } else {
                    $out[] = $current[$j++];
                }
            }
            $merged[$mask] = $out;
            $length[$mask] = count($out);
            $median[$mask] = $out[intdiv(count($out) - 1, 2)];
        }
        $INF = PHP_INT_MAX;
        $dp = array_fill(0, $totalMasks, 0);
        for ($mask = 1; $mask < $totalMasks; $mask++) {
            if (($mask & ($mask - 1)) === 0) continue;
            $dp[$mask] = $INF;
            $firstBit = $mask & -$mask;
            for ($left = ($mask - 1) & $mask; $left > 0; $left = ($left - 1) & $mask) {
                if (($left & $firstBit) === 0) continue;
                $right = $mask ^ $left;
                if ($right === 0) continue;
                $diff = $median[$left] - $median[$right];
                if ($diff < 0) $diff = -$diff;
                $candidate = $dp[$left] + $dp[$right] + $length[$mask] + $diff;
                if ($candidate < $dp[$mask]) $dp[$mask] = $candidate;
            }
        }
        return $dp[$totalMasks - 1];
    }
}
''')

add("3802_number_of_ways_to_paint_sheets", r'''<?php
// LeetCode 3802 - Number of Ways to Paint Sheets
// https://leetcode.com/problems/number-of-ways-to-paint-sheets/

class Solution {
    function numberOfWays($n, $limit) {
        $MOD = 1000000007;
        sort($limit);
        $points = [1, $n];
        foreach ($limit as $x) {
            if ($x + 1 > 1 && $x + 1 < $n) $points[] = $x + 1;
            if ($n - $x > 1 && $n - $x < $n) $points[] = $n - $x;
        }
        sort($points);
        $u = 0;
        for ($i = 0; $i < count($points); $i++) {
            if ($u === 0 || $points[$i] !== $points[$u - 1]) $points[$u++] = $points[$i];
        }
        $points = array_slice($points, 0, $u);
        $countGE = function($lim, $x) {
            $lo = 0;
            $hi = count($lim);
            while ($lo < $hi) {
                $mid = ($lo + $hi) >> 1;
                if ($lim[$mid] < $x) $lo = $mid + 1;
                else $hi = $mid;
            }
            return count($lim) - $lo;
        };
        $ans = 0;
        for ($i = 0; $i + 1 < count($points); $i++) {
            $x = $points[$i];
            $a = $countGE($limit, $x);
            $b = $countGE($limit, $n - $x);
            $same = $countGE($limit, max($x, $n - $x));
            $ways = ($a * $b - $same) % $MOD;
            $length = $points[$i + 1] - $x;
            $ans = ($ans + $ways * $length) % $MOD;
        }
        if ($ans < 0) $ans += $MOD;
        return $ans;
    }
}
''')

add("3803_count_residue_prefixes", r'''<?php
// LeetCode 3803 - Count Residue Prefixes
// https://leetcode.com/problems/count-residue-prefixes/

class Solution {
    function residuePrefixes($s) {
        $st = [];
        $ans = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $st[$s[$i]] = true;
            if (count($st) === ($i + 1) % 3) $ans++;
        }
        return $ans;
    }
}
''')

add("3804_number_of_centered_subarrays", r'''<?php
// LeetCode 3804 - Number of Centered Subarrays
// https://leetcode.com/problems/number-of-centered-subarrays/

class Solution {
    function centeredSubarrays($nums) {
        $n = count($nums);
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            $st = [];
            $s = 0;
            for ($j = $i; $j < $n; $j++) {
                $s += $nums[$j];
                $st[$nums[$j]] = true;
                if (isset($st[$s])) $ans++;
            }
        }
        return $ans;
    }
}
''')

add("3805_count_caesar_cipher_pairs", r'''<?php
// LeetCode 3805 - Count Caesar Cipher Pairs
// https://leetcode.com/problems/count-caesar-cipher-pairs/

class Solution {
    function countPairs($words) {
        $cnt = [];
        foreach ($words as $word) {
            $s = str_split($word);
            $k = ord('z') - ord($s[0]);
            for ($i = 1; $i < count($s); $i++) {
                $s[$i] = chr(97 + (ord($s[$i]) - 97 + $k) % 26);
            }
            $s[0] = 'z';
            $key = implode('', $s);
            if (!isset($cnt[$key])) $cnt[$key] = 0;
            $cnt[$key]++;
        }
        $ans = 0;
        foreach ($cnt as $v) $ans += $v * ($v - 1) / 2;
        return $ans;
    }
}
''')

add("3806_maximum_bitwise_and_after_increment_operations", r'''<?php
// LeetCode 3806 - Maximum Bitwise AND After Increment Operations
// https://leetcode.com/problems/maximum-bitwise-and-after-increment-operations/

class Solution {
    function maximumAND($nums, $k, $m) {
        $BitLen = function($x) {
            if ($x === 0) return 0;
            $n = 0;
            while ($x > 0) { $n++; $x >>= 1; }
            return $n;
        };
        $mxVal = $nums[0];
        foreach ($nums as $v) if ($v > $mxVal) $mxVal = $v;
        $mxVal += $k;
        $mx = $BitLen($mxVal);
        $ans = 0;
        $cost = array_fill(0, count($nums), 0);
        for ($bit = $mx - 1; $bit >= 0; $bit--) {
            $target = $ans | (1 << $bit);
            for ($i = 0; $i < count($nums); $i++) {
                $x = $nums[$i];
                $j = $BitLen($target & ~$x);
                $mask = (1 << $j) - 1;
                $cost[$i] = ($target & $mask) - ($x & $mask);
            }
            sort($cost);
            $sum = 0;
            for ($i = 0; $i < $m; $i++) $sum += $cost[$i];
            if ($sum <= $k) $ans = $target;
        }
        return $ans;
    }
}
''')

add("3807_minimum_cost_to_repair_edges_to_traverse_a_graph", r'''<?php
// LeetCode 3807 - Minimum Cost to Repair Edges to Traverse a Graph
// https://leetcode.com/problems/minimum-cost-to-repair-edges-to-traverse-a-graph/

class Solution {
    function minCost($n, $edges, $k) {
        usort($edges, function($a, $b) { return $a[2] <=> $b[2]; });
        $m = count($edges);
        if ($m === 0) return -1;
        $check = function($idx) use ($n, $edges, $k) {
            $g = array_fill(0, $n, []);
            for ($i = 0; $i <= $idx; $i++) {
                $g[$edges[$i][0]][] = $edges[$i][1];
                $g[$edges[$i][1]][] = $edges[$i][0];
            }
            $q = [0];
            $vis = array_fill(0, $n, false);
            $vis[0] = true;
            $dist = 0;
            while (count($q)) {
                $nq = [];
                foreach ($q as $u) {
                    if ($u === $n - 1) return $dist <= $k;
                    foreach ($g[$u] as $v) {
                        if (!$vis[$v]) {
                            $vis[$v] = true;
                            $nq[] = $v;
                        }
                    }
                }
                $q = $nq;
                $dist++;
            }
            return false;
        };
        $l = 0;
        $r = $m - 1;
        while ($l < $r) {
            $mid = ($l + $r) >> 1;
            if ($check($mid)) $r = $mid;
            else $l = $mid + 1;
        }
        if ($check($l)) return $edges[$l][2];
        return -1;
    }
}
''')

add("3809_best_reachable_tower", r'''<?php
// LeetCode 3809 - Best Reachable Tower
// https://leetcode.com/problems/best-reachable-tower/

class Solution {
    function bestTower($towers, $center, $radius) {
        $cx = $center[0];
        $cy = $center[1];
        $idx = -1;
        for ($i = 0; $i < count($towers); $i++) {
            $x = $towers[$i][0];
            $y = $towers[$i][1];
            $q = $towers[$i][2];
            $dist = abs($x - $cx) + abs($y - $cy);
            if ($dist > $radius) continue;
            if ($idx === -1 || $towers[$idx][2] < $q ||
                ($towers[$idx][2] === $q &&
                 ($x < $towers[$idx][0] || ($x === $towers[$idx][0] && $y < $towers[$idx][1])))) {
                $idx = $i;
            }
        }
        if ($idx === -1) return [-1, -1];
        return [$towers[$idx][0], $towers[$idx][1]];
    }
}
''')

add("3810_minimum_operations_to_reach_target_array", r'''<?php
// LeetCode 3810 - Minimum Operations to Reach Target Array
// https://leetcode.com/problems/minimum-operations-to-reach-target-array/

class Solution {
    function minOperations($nums, $target) {
        $s = [];
        for ($i = 0; $i < count($nums); $i++) {
            if ($nums[$i] !== $target[$i]) $s[$nums[$i]] = true;
        }
        return count($s);
    }
}
''')

add("3811_number_of_alternating_xor_partitions", r'''<?php
// LeetCode 3811 - Number of Alternating XOR Partitions
// https://leetcode.com/problems/number-of-alternating-xor-partitions/

class Solution {
    function alternatingXOR($nums, $target1, $target2) {
        $MOD = 1000000007;
        $cnt1 = [];
        $cnt2 = [];
        $cnt2[0] = 1;
        $pre = 0;
        $ans = 0;
        foreach ($nums as $x) {
            $pre ^= $x;
            $a = isset($cnt2[$pre ^ $target1]) ? $cnt2[$pre ^ $target1] : 0;
            $b = isset($cnt1[$pre ^ $target2]) ? $cnt1[$pre ^ $target2] : 0;
            $ans = ($a + $b) % $MOD;
            if (!isset($cnt1[$pre])) $cnt1[$pre] = 0;
            $cnt1[$pre] = ($cnt1[$pre] + $a) % $MOD;
            if (!isset($cnt2[$pre])) $cnt2[$pre] = 0;
            $cnt2[$pre] = ($cnt2[$pre] + $b) % $MOD;
        }
        return $ans;
    }
}
''')

add("3812_minimum_edge_toggles_on_a_tree", r'''<?php
// LeetCode 3812 - Minimum Edge Toggles on a Tree
// https://leetcode.com/problems/minimum-edge-toggles-on-a-tree/

class Solution {
    function minimumFlips($n, $edges, $start, $target) {
        $g = array_fill(0, $n, []);
        for ($i = 0; $i < $n - 1; $i++) {
            $a = $edges[$i][0];
            $b = $edges[$i][1];
            $g[$a][] = [$b, $i];
            $g[$b][] = [$a, $i];
        }
        $ans = [];
        $dfs = function($a, $fa) use (&$dfs, &$ans, $g, $start, $target) {
            $rev = $start[$a] !== $target[$a];
            foreach ($g[$a] as $e) {
                $b = $e[0];
                $i = $e[1];
                if ($b !== $fa && $dfs($b, $a)) {
                    $ans[] = $i;
                    $rev = !$rev;
                }
            }
            return $rev;
        };
        if ($dfs(0, -1)) return [-1];
        sort($ans);
        return $ans;
    }
}
''')

add("3813_vowel_consonant_score", r'''<?php
// LeetCode 3813 - Vowel-Consonant Score
// https://leetcode.com/problems/vowel-consonant-score/

class Solution {
    function vowelConsonantScore($s) {
        $v = 0;
        $c = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $ch = $s[$i];
            if (($ch >= 'a' && $ch <= 'z') || ($ch >= 'A' && $ch <= 'Z')) {
                $c++;
                if ($ch === 'a' || $ch === 'e' || $ch === 'i' || $ch === 'o' || $ch === 'u') $v++;
            }
        }
        $c -= $v;
        if ($c === 0) return 0;
        return intdiv($v, $c);
    }
}
''')

add("3814_maximum_capacity_within_budget", r'''<?php
// LeetCode 3814 - Maximum Capacity Within Budget
// https://leetcode.com/problems/maximum-capacity-within-budget/

class _MCHeap {
    public $a = [];
    public $cmp;
    function __construct($cmp) { $this->cmp = $cmp; }
    function _up($i) {
        $a = &$this->a;
        $cmp = $this->cmp;
        while ($i > 0) {
            $p = ($i - 1) >> 1;
            if ($cmp($a[$i], $a[$p]) >= 0) break;
            $t = $a[$i]; $a[$i] = $a[$p]; $a[$p] = $t;
            $i = $p;
        }
    }
    function _down($i) {
        $a = &$this->a;
        $cmp = $this->cmp;
        $n = count($a);
        while (true) {
            $s = $i;
            $l = $i * 2 + 1;
            $r = $l + 1;
            if ($l < $n && $cmp($a[$l], $a[$s]) < 0) $s = $l;
            if ($r < $n && $cmp($a[$r], $a[$s]) < 0) $s = $r;
            if ($s === $i) break;
            $t = $a[$i]; $a[$i] = $a[$s]; $a[$s] = $t;
            $i = $s;
        }
    }
    function push($x) { $this->a[] = $x; $this->_up(count($this->a) - 1); }
    function pop() {
        $a = &$this->a;
        if (!count($a)) return null;
        $top = $a[0];
        $last = array_pop($a);
        if (count($a)) { $a[0] = $last; $this->_down(0); }
        return $top;
    }
    function peek() { return $this->a[0]; }
    function size() { return count($this->a); }
}

class Solution {
    function maxCapacity($costs, $capacity, $budget) {
        $arr = [];
        for ($k = 0; $k < count($costs); $k++) {
            if ($costs[$k] < $budget) $arr[] = [$costs[$k], $capacity[$k]];
        }
        if (!count($arr)) return 0;
        usort($arr, function($a, $b) { return $a[0] <=> $b[0]; });
        $m = count($arr);
        $alive = array_fill(0, $m, true);
        $h = new _MCHeap(function($a, $b) {
            if ($a[0] !== $b[0]) return $b[0] - $a[0];
            return $b[1] - $a[1];
        });
        for ($i = 0; $i < $m; $i++) $h->push([$arr[$i][1], $i]);
        while ($h->size() && !$alive[$h->peek()[1]]) $h->pop();
        $ans = $h->peek()[0];
        $i = 0;
        $j = $m - 1;
        while ($i < $j) {
            $alive[$i] = false;
            while ($i < $j && $arr[$i][0] + $arr[$j][0] >= $budget) {
                $alive[$j] = false;
                $j--;
            }
            while ($h->size() && !$alive[$h->peek()[1]]) $h->pop();
            if ($h->size()) $ans = max($ans, $arr[$i][1] + $h->peek()[0]);
            $i++;
        }
        return $ans;
    }
}
''')

add("3815_design_auction_system", r'''<?php
// LeetCode 3815 - Design Auction System
// https://leetcode.com/problems/design-auction-system/

class _ASHeap {
    public $a = [];
    public $cmp;
    function __construct($cmp) { $this->cmp = $cmp; }
    function _up($i) {
        $a = &$this->a;
        $cmp = $this->cmp;
        while ($i > 0) {
            $p = ($i - 1) >> 1;
            if ($cmp($a[$i], $a[$p]) >= 0) break;
            $t = $a[$i]; $a[$i] = $a[$p]; $a[$p] = $t;
            $i = $p;
        }
    }
    function _down($i) {
        $a = &$this->a;
        $cmp = $this->cmp;
        $n = count($a);
        while (true) {
            $s = $i;
            $l = $i * 2 + 1;
            $r = $l + 1;
            if ($l < $n && $cmp($a[$l], $a[$s]) < 0) $s = $l;
            if ($r < $n && $cmp($a[$r], $a[$s]) < 0) $s = $r;
            if ($s === $i) break;
            $t = $a[$i]; $a[$i] = $a[$s]; $a[$s] = $t;
            $i = $s;
        }
    }
    function push($x) { $this->a[] = $x; $this->_up(count($this->a) - 1); }
    function pop() {
        $a = &$this->a;
        if (!count($a)) return null;
        $top = $a[0];
        $last = array_pop($a);
        if (count($a)) { $a[0] = $last; $this->_down(0); }
        return $top;
    }
    function peek() { return $this->a[0]; }
    function size() { return count($this->a); }
}

class AuctionSystem {
    public $bids;
    public $heaps;
    function __construct() {
        $this->bids = [];
        $this->heaps = [];
    }
    function addBid($userId, $itemId, $bidAmount) {
        if (!isset($this->bids[$itemId])) $this->bids[$itemId] = [];
        $this->bids[$itemId][$userId] = $bidAmount;
        if (!isset($this->heaps[$itemId])) {
            $this->heaps[$itemId] = new _ASHeap(function($a, $b) {
                if ($a['amount'] !== $b['amount']) return $b['amount'] - $a['amount'];
                return $b['userId'] - $a['userId'];
            });
        }
        $this->heaps[$itemId]->push(['amount' => $bidAmount, 'userId' => $userId]);
    }
    function updateBid($userId, $itemId, $newAmount) {
        $this->addBid($userId, $itemId, $newAmount);
    }
    function removeBid($userId, $itemId) {
        if (isset($this->bids[$itemId])) unset($this->bids[$itemId][$userId]);
    }
    function getHighestBidder($itemId) {
        if (!isset($this->heaps[$itemId])) return -1;
        $h = $this->heaps[$itemId];
        $m = isset($this->bids[$itemId]) ? $this->bids[$itemId] : [];
        while ($h->size()) {
            $top = $h->peek();
            if (isset($m[$top['userId']]) && $m[$top['userId']] === $top['amount']) return $top['userId'];
            $h->pop();
        }
        return -1;
    }
}
''')

add("3816_lexicographically_smallest_string_after_deleting_duplicate_characters", r'''<?php
// LeetCode 3816 - Lexicographically Smallest String After Deleting Duplicate Characters
// https://leetcode.com/problems/lexicographically-smallest-string-after-deleting-duplicate-characters/

class Solution {
    function lexSmallestAfterDeletion($s) {
        $cnt = array_fill(0, 26, 0);
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) $cnt[ord($s[$i]) - 97]++;
        $stk = [];
        for ($i = 0; $i < $n; $i++) {
            $c = $s[$i];
            while (count($stk) > 0 && $stk[count($stk) - 1] > $c
                    && $cnt[ord($stk[count($stk) - 1]) - 97] > 1) {
                $cnt[ord($stk[count($stk) - 1]) - 97]--;
                array_pop($stk);
            }
            $stk[] = $c;
        }
        while ($cnt[ord($stk[count($stk) - 1]) - 97] > 1) {
            $cnt[ord($stk[count($stk) - 1]) - 97]--;
            array_pop($stk);
        }
        return implode('', $stk);
    }
}
''')

add("3817_good_indices_in_a_digit_string", r'''<?php
// LeetCode 3817 - Good Indices in a Digit String
// https://leetcode.com/problems/good-indices-in-a-digit-string/

class Solution {
    function goodIndices($s) {
        $ans = [];
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $t = strval($i);
            $k = strlen($t);
            if ($i + 1 - $k >= 0 && substr($s, $i + 1 - $k, $k) === $t) $ans[] = $i;
        }
        return $ans;
    }
}
''')

add("3818_minimum_prefix_removal_to_make_array_strictly_increasing", r'''<?php
// LeetCode 3818 - Minimum Prefix Removal to Make Array Strictly Increasing
// https://leetcode.com/problems/minimum-prefix-removal-to-make-array-strictly-increasing/

class Solution {
    function minimumPrefixLength($nums) {
        for ($i = count($nums) - 1; $i > 0; $i--) {
            if ($nums[$i - 1] >= $nums[$i]) return $i;
        }
        return 0;
    }
}
''')

add("3819_rotate_non_negative_elements", r'''<?php
// LeetCode 3819 - Rotate Non Negative Elements
// https://leetcode.com/problems/rotate-non-negative-elements/

class Solution {
    function rotateElements($nums, $k) {
        $t = [];
        foreach ($nums as $x) if ($x >= 0) $t[] = $x;
        $m = count($t);
        if ($m === 0) return $nums;
        $d = array_fill(0, $m, 0);
        for ($i = 0; $i < $m; $i++) $d[(($i - $k) % $m + $m) % $m] = $t[$i];
        $j = 0;
        for ($i = 0; $i < count($nums); $i++) {
            if ($nums[$i] >= 0) $nums[$i] = $d[$j++];
        }
        return $nums;
    }
}
''')

add("3820_pythagorean_distance_nodes_in_a_tree", r'''<?php
// LeetCode 3820 - Pythagorean Distance Nodes in a Tree
// https://leetcode.com/problems/pythagorean-distance-nodes-in-a-tree/

class Solution {
    function specialNodes($n, $edges, $x, $y, $z) {
        $g = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $g[$e[0]][] = $e[1];
            $g[$e[1]][] = $e[0];
        }
        $bfs = function($start) use ($n, $g) {
            $dist = array_fill(0, $n, 1000000000);
            $q = [$start];
            $dist[$start] = 0;
            for ($qi = 0; $qi < count($q); $qi++) {
                $u = $q[$qi];
                foreach ($g[$u] as $v) {
                    if ($dist[$v] > $dist[$u] + 1) {
                        $dist[$v] = $dist[$u] + 1;
                        $q[] = $v;
                    }
                }
            }
            return $dist;
        };
        $d1 = $bfs($x);
        $d2 = $bfs($y);
        $d3 = $bfs($z);
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            $a = [$d1[$i], $d2[$i], $d3[$i]];
            sort($a);
            $x0 = $a[0]; $x1 = $a[1]; $x2 = $a[2];
            if ($x0 * $x0 + $x1 * $x1 === $x2 * $x2) $ans++;
        }
        return $ans;
    }
}
''')

add("3821_find_nth_smallest_integer_with_k_one_bits", r'''<?php
// LeetCode 3821 - Find Nth Smallest Integer With K One Bits
// https://leetcode.com/problems/find-nth-smallest-integer-with-k-one-bits/

class Solution {
    function nthSmallest($n, $k) {
        $MX = 50;
        $C = [];
        for ($i = 0; $i < $MX; $i++) $C[$i] = array_fill(0, $MX + 1, 0);
        for ($i = 0; $i < $MX; $i++) {
            $C[$i][0] = 1;
            for ($j = 1; $j <= $i; $j++) $C[$i][$j] = $C[$i - 1][$j - 1] + $C[$i - 1][$j];
        }
        $ans = 0;
        $nn = $n;
        for ($i = 49; $i >= 0; $i--) {
            if ($k >= 0 && $nn > $C[$i][$k]) {
                $nn -= $C[$i][$k];
                $ans |= 1 << $i;
                $k--;
                if ($k === 0) break;
            }
        }
        return $ans;
    }
}
''')

add("3822_design_order_management_system", r'''<?php
// LeetCode 3822 - Design Order Management System
// https://leetcode.com/problems/design-order-management-system/

class OrderManagementSystem {
    public $orderTypeMap;
    public $priceMap;
    public $t;
    function __construct() {
        $this->orderTypeMap = [];
        $this->priceMap = [];
        $this->t = [];
    }
    function _key($orderType, $price) {
        return $orderType . '#' . $price;
    }
    function addOrder($orderId, $orderType, $price) {
        $this->orderTypeMap[$orderId] = $orderType;
        $this->priceMap[$orderId] = $price;
        $key = $this->_key($orderType, $price);
        if (!isset($this->t[$key])) $this->t[$key] = [];
        $this->t[$key][] = $orderId;
    }
    function modifyOrder($orderId, $newPrice) {
        $orderType = $this->orderTypeMap[$orderId];
        $oldPrice = $this->priceMap[$orderId];
        $this->priceMap[$orderId] = $newPrice;
        $oldKey = $this->_key($orderType, $oldPrice);
        $oldList = &$this->t[$oldKey];
        for ($i = 0; $i < count($oldList); $i++) {
            if ($oldList[$i] === $orderId) {
                array_splice($oldList, $i, 1);
                break;
            }
        }
        $key = $this->_key($orderType, $newPrice);
        if (!isset($this->t[$key])) $this->t[$key] = [];
        $this->t[$key][] = $orderId;
    }
    function cancelOrder($orderId) {
        $orderType = $this->orderTypeMap[$orderId];
        $price = $this->priceMap[$orderId];
        unset($this->orderTypeMap[$orderId]);
        unset($this->priceMap[$orderId]);
        $key = $this->_key($orderType, $price);
        $list = &$this->t[$key];
        for ($i = 0; $i < count($list); $i++) {
            if ($list[$i] === $orderId) {
                array_splice($list, $i, 1);
                break;
            }
        }
    }
    function getOrdersAtPrice($orderType, $price) {
        $key = $this->_key($orderType, $price);
        if (!isset($this->t[$key])) return [];
        return $this->t[$key];
    }
}
''')


def main():
    for folder, body in SOLUTIONS.items():
        path = ROOT / folder / "solution.php"
        path.write_text(body, encoding="utf-8", newline="\n")
        print("wrote", folder)
    print("count", len(SOLUTIONS))

if __name__ == "__main__":
    main()

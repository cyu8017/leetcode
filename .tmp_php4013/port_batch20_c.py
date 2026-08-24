#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
SOLUTIONS = {}

def add(folder, body):
    SOLUTIONS[folder] = body


add("3770_largest_prime_from_consecutive_prime_sum", r'''<?php
// LeetCode 3770 - Largest Prime from Consecutive Prime Sum
// https://leetcode.com/problems/largest-prime-from-consecutive-prime-sum/

class Solution {
    function largestPrime($n) {
        $MX = 500000;
        $isPrime = array_fill(0, $MX + 1, true);
        $isPrime[0] = $isPrime[1] = false;
        $primes = [];
        for ($i = 2; $i <= $MX; $i++) {
            if ($isPrime[$i]) {
                $primes[] = $i;
                if ($i * $i <= $MX) {
                    for ($j = $i * $i; $j <= $MX; $j += $i) $isPrime[$j] = false;
                }
            }
        }
        $S = [0];
        $t = 0;
        foreach ($primes as $x) {
            $t += $x;
            if ($t > $MX) break;
            if ($isPrime[$t]) $S[] = $t;
        }
        $lo = 0;
        $hi = count($S);
        while ($lo < $hi) {
            $mid = ($lo + $hi) >> 1;
            if ($S[$mid] <= $n) $lo = $mid + 1;
            else $hi = $mid;
        }
        return $S[$lo - 1];
    }
}
''')

add("3771_total_score_of_dungeon_runs", r'''<?php
// LeetCode 3771 - Total Score of Dungeon Runs
// https://leetcode.com/problems/total-score-of-dungeon-runs/

class Solution {
    function totalScore($hp, $damage, $requirement) {
        $n = count($damage);
        $prefix = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; $i++) $prefix[$i + 1] = $prefix[$i] + $damage[$i];
        $answer = $n * ($n + 1) / 2;
        for ($j = 1; $j <= $n; $j++) {
            $threshold = $prefix[$j] + ($requirement[$j - 1] - $hp);
            $lo = 0;
            $hi = $j;
            while ($lo < $hi) {
                $mid = ($lo + $hi) >> 1;
                if ($prefix[$mid] < $threshold) $lo = $mid + 1;
                else $hi = $mid;
            }
            $answer -= $lo;
        }
        return $answer;
    }
}
''')

add("3772_maximum_subgraph_score_in_a_tree", r'''<?php
// LeetCode 3772 - Maximum Subgraph Score in a Tree
// https://leetcode.com/problems/maximum-subgraph-score-in-a-tree/

class Solution {
    function maxSubgraphScore($n, $edges, $good) {
        $g = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $g[$e[0]][] = $e[1];
            $g[$e[1]][] = $e[0];
        }
        $parent = array_fill(0, $n, -2);
        $parent[0] = -1;
        $order = [0];
        for ($i = 0; $i < count($order); $i++) {
            $u = $order[$i];
            foreach ($g[$u] as $v) {
                if ($parent[$v] === -2) {
                    $parent[$v] = $u;
                    $order[] = $v;
                }
            }
        }
        $down = array_fill(0, $n, 0);
        for ($i = $n - 1; $i >= 0; $i--) {
            $u = $order[$i];
            $down[$u] = 2 * $good[$u] - 1;
            foreach ($g[$u] as $v) {
                if ($parent[$v] === $u && $down[$v] > 0) $down[$u] += $down[$v];
            }
        }
        $ans = $down;
        foreach ($order as $u) {
            foreach ($g[$u] as $v) {
                if ($parent[$v] === $u) {
                    $outside = $ans[$u];
                    if ($down[$v] > 0) $outside -= $down[$v];
                    $ans[$v] = $down[$v];
                    if ($outside > 0) $ans[$v] += $outside;
                }
            }
        }
        return $ans;
    }
}
''')

add("3773_maximum_number_of_equal_length_runs", r'''<?php
// LeetCode 3773 - Maximum Number of Equal Length Runs
// https://leetcode.com/problems/maximum-number-of-equal-length-runs/

class Solution {
    function maxSameLengthRuns($s) {
        $cnt = [];
        $n = strlen($s);
        $ans = 0;
        for ($i = 0; $i < $n; ) {
            $j = $i + 1;
            while ($j < $n && $s[$j] === $s[$i]) $j++;
            $m = $j - $i;
            if (!isset($cnt[$m])) $cnt[$m] = 0;
            $cnt[$m]++;
            $ans = max($ans, $cnt[$m]);
            $i = $j;
        }
        return $ans;
    }
}
''')

add("3774_absolute_difference_between_maximum_and_minimum_k_elements", r'''<?php
// LeetCode 3774 - Absolute Difference Between Maximum and Minimum K Elements
// https://leetcode.com/problems/absolute-difference-between-maximum-and-minimum-k-elements/

class Solution {
    function absDifference($nums, $k) {
        $a = $nums;
        sort($a);
        $ans = 0;
        $n = count($a);
        for ($i = 0; $i < $k; $i++) $ans += $a[$n - $i - 1] - $a[$i];
        return $ans;
    }
}
''')

add("3775_reverse_words_with_same_vowel_count", r'''<?php
// LeetCode 3775 - Reverse Words With Same Vowel Count
// https://leetcode.com/problems/reverse-words-with-same-vowel-count/

class Solution {
    function reverseWords($s) {
        $calc = function($w) {
            $cnt = 0;
            $len = strlen($w);
            for ($i = 0; $i < $len; $i++) {
                $c = $w[$i];
                if ($c === 'a' || $c === 'e' || $c === 'i' || $c === 'o' || $c === 'u') $cnt++;
            }
            return $cnt;
        };
        $words = preg_split('/\s+/', trim($s));
        $cnt = $calc($words[0]);
        $ans = $words[0];
        for ($i = 1; $i < count($words); $i++) {
            $w = $words[$i];
            if ($calc($w) === $cnt) $w = strrev($w);
            $ans .= ' ' . $w;
        }
        return $ans;
    }
}
''')

add("3776_minimum_moves_to_balance_circular_array", r'''<?php
// LeetCode 3776 - Minimum Moves to Balance Circular Array
// https://leetcode.com/problems/minimum-moves-to-balance-circular-array/

class Solution {
    function minMoves($balance) {
        $sum = 0;
        foreach ($balance as $b) $sum += $b;
        if ($sum < 0) return -1;
        $n = count($balance);
        $mn = $balance[0];
        $idx = 0;
        for ($i = 1; $i < $n; $i++) {
            if ($balance[$i] < $mn) {
                $mn = $balance[$i];
                $idx = $i;
            }
        }
        if ($mn >= 0) return 0;
        $need = -$mn;
        $ans = 0;
        for ($j = 1; $j < $n; $j++) {
            $a = $balance[($idx - $j + $n) % $n];
            $b = $balance[($idx + $j) % $n];
            $c1 = min($a, $need);
            $need -= $c1;
            $ans += $c1 * $j;
            $c2 = min($b, $need);
            $need -= $c2;
            $ans += $c2 * $j;
        }
        return $ans;
    }
}
''')

add("3777_minimum_deletions_to_make_alternating_substring", r'''<?php
// LeetCode 3777 - Minimum Deletions to Make Alternating Substring
// https://leetcode.com/problems/minimum-deletions-to-make-alternating-substring/

class _MDBIT {
    public $n;
    public $c;
    function __construct($n_) {
        $this->n = $n_;
        $this->c = array_fill(0, $n_ + 1, 0);
    }
    function update($x, $delta) {
        for (; $x <= $this->n; $x += $x & -$x) $this->c[$x] += $delta;
    }
    function query($x) {
        $s = 0;
        for (; $x > 0; $x -= $x & -$x) $s += $this->c[$x];
        return $s;
    }
}

class Solution {
    function minDeletions($s, $queries) {
        $n = strlen($s);
        $nums = array_fill(0, $n, 0);
        $bit = new _MDBIT($n);
        for ($i = 1; $i < $n; $i++) {
            if ($s[$i] === $s[$i - 1]) {
                $nums[$i] = 1;
                $bit->update($i + 1, 1);
            }
        }
        $ans = [];
        foreach ($queries as $q) {
            if ($q[0] === 1) {
                $j = $q[1];
                $delta = ($nums[$j] ^ 1) - $nums[$j];
                $nums[$j] ^= 1;
                $bit->update($j + 1, $delta);
                if ($j + 1 < $n) {
                    $delta = ($nums[$j + 1] ^ 1) - $nums[$j + 1];
                    $nums[$j + 1] ^= 1;
                    $bit->update($j + 2, $delta);
                }
            } else {
                $l = $q[1];
                $r = $q[2];
                $ans[] = $bit->query($r + 1) - $bit->query($l + 1);
            }
        }
        return $ans;
    }
}
''')

add("3778_minimum_distance_excluding_one_maximum_weighted_edge", r'''<?php
// LeetCode 3778 - Minimum Distance Excluding One Maximum Weighted Edge
// https://leetcode.com/problems/minimum-distance-excluding-one-maximum-weighted-edge/

class _MinHeap {
    public $a = [];
    public $cmp;
    function __construct($cmp = null) {
        $this->cmp = $cmp ?: function($x, $y) { return $x - $y; };
    }
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
    function minCostExcludingMax($n, $edges) {
        $g = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $u = $e[0]; $v = $e[1]; $w = $e[2];
            $g[$u][] = [$v, $w];
            $g[$v][] = [$u, $w];
        }
        $INF = PHP_INT_MAX;
        $dist = [];
        for ($i = 0; $i < $n; $i++) $dist[$i] = [$INF, $INF];
        $dist[0][0] = 0;
        $pq = new _MinHeap(function($a, $b) { return $a[0] - $b[0]; });
        $pq->push([0, 0, 0]);
        while ($pq->size()) {
            $cur = $pq->pop();
            $c = $cur[0]; $u = $cur[1]; $used = $cur[2];
            if ($c > $dist[$u][$used]) continue;
            if ($u === $n - 1 && $used === 1) return $c;
            foreach ($g[$u] as $e) {
                $v = $e[0]; $w = $e[1];
                $nxt = $c + $w;
                if ($nxt < $dist[$v][$used]) {
                    $dist[$v][$used] = $nxt;
                    $pq->push([$nxt, $v, $used]);
                }
                if ($used === 0) {
                    $nxt = $c;
                    if ($nxt < $dist[$v][1]) {
                        $dist[$v][1] = $nxt;
                        $pq->push([$nxt, $v, 1]);
                    }
                }
            }
        }
        return $dist[$n - 1][1];
    }
}
''')

add("3779_minimum_number_of_operations_to_have_distinct_elements", r'''<?php
// LeetCode 3779 - Minimum Number of Operations to Have Distinct Elements
// https://leetcode.com/problems/minimum-number-of-operations-to-have-distinct-elements/

class Solution {
    function minOperations($nums) {
        $st = [];
        for ($i = count($nums) - 1; $i >= 0; $i--) {
            if (isset($st[$nums[$i]])) return intdiv($i, 3) + 1;
            $st[$nums[$i]] = true;
        }
        return 0;
    }
}
''')

add("3780_maximum_sum_of_three_numbers_divisible_by_three", r'''<?php
// LeetCode 3780 - Maximum Sum of Three Numbers Divisible by Three
// https://leetcode.com/problems/maximum-sum-of-three-numbers-divisible-by-three/

class Solution {
    function maximumSum($nums) {
        $a = $nums;
        sort($a);
        $g = [[], [], []];
        foreach ($a as $x) $g[$x % 3][] = $x;
        $ans = 0;
        for ($aa = 0; $aa < 3; $aa++) {
            if (count($g[$aa])) {
                $x = array_pop($g[$aa]);
                for ($b = 0; $b < 3; $b++) {
                    if (count($g[$b])) {
                        $y = array_pop($g[$b]);
                        $c = (3 - ($aa + $b) % 3) % 3;
                        if (count($g[$c])) {
                            $z = $g[$c][count($g[$c]) - 1];
                            $ans = max($ans, $x + $y + $z);
                        }
                        $g[$b][] = $y;
                    }
                }
                $g[$aa][] = $x;
            }
        }
        return $ans;
    }
}
''')

add("3781_maximum_score_after_binary_swaps", r'''<?php
// LeetCode 3781 - Maximum Score After Binary Swaps
// https://leetcode.com/problems/maximum-score-after-binary-swaps/

class Solution {
    function maximumScore($nums, $s) {
        $ans = 0;
        $pq = new SplPriorityQueue();
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            $pq->insert($nums[$i], $nums[$i]);
            if ($s[$i] === '1') $ans += $pq->extract();
        }
        return $ans;
    }
}
''')

add("3782_last_remaining_integer_after_alternating_deletion_operations", r'''<?php
// LeetCode 3782 - Last Remaining Integer After Alternating Deletion Operations
// https://leetcode.com/problems/last-remaining-integer-after-alternating-deletion-operations/

class Solution {
    function lastRemaining($n) {
        $first = 1;
        $step = 2;
        $left = true;
        while ($n > 1) {
            if (!$left && $n % 2 === 0) $first += $step;
            $n = intdiv($n + 1, 2);
            $step *= 2;
            $left = !$left;
        }
        return $first;
    }
}
''')

add("3783_mirror_distance_of_an_integer", r'''<?php
// LeetCode 3783 - Mirror Distance of an Integer
// https://leetcode.com/problems/mirror-distance-of-an-integer/

class Solution {
    function mirrorDistance($n) {
        $reverse = function($x) {
            $y = 0;
            for (; $x > 0; $x = intdiv($x, 10)) $y = $y * 10 + $x % 10;
            return $y;
        };
        return abs($n - $reverse($n));
    }
}
''')

add("3784_minimum_deletion_cost_to_make_all_characters_equal", r'''<?php
// LeetCode 3784 - Minimum Deletion Cost to Make All Characters Equal
// https://leetcode.com/problems/minimum-deletion-cost-to-make-all-characters-equal/

class Solution {
    function minCost($s, $cost) {
        $tot = 0;
        $g = [];
        for ($i = 0; $i < count($cost); $i++) {
            $tot += $cost[$i];
            if (!isset($g[$s[$i]])) $g[$s[$i]] = 0;
            $g[$s[$i]] += $cost[$i];
        }
        $ans = $tot;
        foreach ($g as $x) $ans = min($ans, $tot - $x);
        return $ans;
    }
}
''')

add("3785_minimum_swaps_to_avoid_forbidden_values", r'''<?php
// LeetCode 3785 - Minimum Swaps to Avoid Forbidden Values
// https://leetcode.com/problems/minimum-swaps-to-avoid-forbidden-values/

class Solution {
    function minSwaps($nums, $forbidden) {
        $n = count($nums);
        $freq = [];
        foreach ($nums as $x) {
            if (!isset($freq[$x])) $freq[$x] = 0;
            $freq[$x]++;
        }
        foreach ($forbidden as $x) {
            if (!isset($freq[$x])) $freq[$x] = 0;
            $freq[$x]++;
        }
        foreach ($freq as $c) {
            if ($c > $n) return -1;
        }
        $bad = [];
        $total = 0;
        $largest = 0;
        for ($i = 0; $i < $n; $i++) {
            if ($nums[$i] === $forbidden[$i]) {
                if (!isset($bad[$nums[$i]])) $bad[$nums[$i]] = 0;
                $bad[$nums[$i]]++;
                $total++;
                if ($bad[$nums[$i]] > $largest) $largest = $bad[$nums[$i]];
            }
        }
        if (intdiv($total + 1, 2) > $largest) return intdiv($total + 1, 2);
        return $largest;
    }
}
''')

add("3786_total_sum_of_interaction_cost_in_tree_groups", r'''<?php
// LeetCode 3786 - Total Sum of Interaction Cost in Tree Groups
// https://leetcode.com/problems/total-sum-of-interaction-cost-in-tree-groups/

class Solution {
    function interactionCost($n, $edges, $group) {
        $g = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $g[$e[0]][] = $e[1];
            $g[$e[1]][] = $e[0];
        }
        $total = array_fill(0, 21, 0);
        foreach ($group as $x) $total[$x]++;
        $parent = array_fill(0, $n, -2);
        $parent[0] = -1;
        $order = [0];
        for ($i = 0; $i < count($order); $i++) {
            $u = $order[$i];
            foreach ($g[$u] as $v) {
                if ($parent[$v] === -2) {
                    $parent[$v] = $u;
                    $order[] = $v;
                }
            }
        }
        $count = [];
        for ($i = 0; $i < $n; $i++) $count[$i] = array_fill(0, 21, 0);
        $ans = 0;
        for ($i = $n - 1; $i >= 0; $i--) {
            $u = $order[$i];
            $count[$u][$group[$u]]++;
            foreach ($g[$u] as $v) {
                if ($parent[$v] !== $u) continue;
                for ($c = 1; $c <= 20; $c++) {
                    $x = $count[$v][$c];
                    $ans += $x * ($total[$c] - $x);
                    $count[$u][$c] += $x;
                }
            }
        }
        return $ans;
    }
}
''')

add("3787_find_diameter_endpoints_of_a_tree", r'''<?php
// LeetCode 3787 - Find Diameter Endpoints of a Tree
// https://leetcode.com/problems/find-diameter-endpoints-of-a-tree/

class Solution {
    function findSpecialNodes($n, $edges) {
        $g = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $g[$e[0]][] = $e[1];
            $g[$e[1]][] = $e[0];
        }
        $bfs = function($start) use ($n, $g) {
            $dist = array_fill(0, $n, -1);
            $dist[$start] = 0;
            $q = [$start];
            $far = $start;
            for ($head = 0; $head < count($q); $head++) {
                $u = $q[$head];
                if ($dist[$u] > $dist[$far]) $far = $u;
                foreach ($g[$u] as $v) {
                    if ($dist[$v] === -1) {
                        $dist[$v] = $dist[$u] + 1;
                        $q[] = $v;
                    }
                }
            }
            return [$far, $dist];
        };
        $tmp = $bfs(0);
        $a = $tmp[0];
        $tmp = $bfs($a);
        $b = $tmp[0];
        $dist1 = $tmp[1];
        $tmp = $bfs($b);
        $dist2 = $tmp[1];
        $d = $dist1[$b];
        $ans = array_fill(0, $n, '0');
        for ($i = 0; $i < $n; $i++) {
            if ($dist1[$i] === $d || $dist2[$i] === $d) $ans[$i] = '1';
        }
        return implode('', $ans);
    }
}
''')

add("3788_maximum_score_of_a_split", r'''<?php
// LeetCode 3788 - Maximum Score of a Split
// https://leetcode.com/problems/maximum-score-of-a-split/

class Solution {
    function maximumScore($nums) {
        $n = count($nums);
        $suf = array_fill(0, $n, 0);
        $suf[$n - 1] = $nums[$n - 1];
        for ($i = $n - 2; $i >= 0; $i--) $suf[$i] = min($nums[$i], $suf[$i + 1]);
        $pre = 0;
        $ans = -9007199254740991;
        for ($i = 0; $i < $n - 1; $i++) {
            $pre += $nums[$i];
            $ans = max($ans, $pre - $suf[$i + 1]);
        }
        return $ans;
    }
}
''')

add("3789_minimum_cost_to_acquire_required_items", r'''<?php
// LeetCode 3789 - Minimum Cost to Acquire Required Items
// https://leetcode.com/problems/minimum-cost-to-acquire-required-items/

class Solution {
    function minimumCost($cost1, $cost2, $costBoth, $need1, $need2) {
        $a = $need1 * $cost1 + $need2 * $cost2;
        $b = $costBoth * max($need1, $need2);
        $mn = min($need1, $need2);
        $c = $costBoth * $mn + ($need1 - $mn) * $cost1 + ($need2 - $mn) * $cost2;
        return min($a, min($b, $c));
    }
}
''')

add("3790_smallest_all_ones_multiple", r'''<?php
// LeetCode 3790 - Smallest All-Ones Multiple
// https://leetcode.com/problems/smallest-all-ones-multiple/

class Solution {
    function minAllOneMultiple($k) {
        if (($k & 1) === 0) return -1;
        $x = 1 % $k;
        $ans = 1;
        for ($i = 0; $i < $k; $i++) {
            $x = ($x * 10 + 1) % $k;
            $ans++;
            if ($x === 0) return $ans;
        }
        return -1;
    }
}
''')

add("3791_number_of_balanced_integers_in_a_range", r'''<?php
// LeetCode 3791 - Number of Balanced Integers in a Range
// https://leetcode.com/problems/number-of-balanced-integers-in-a-range/

class Solution {
    function countBalanced($low, $high) {
        $BASE = 90;
        $num = '';
        $f = [];
        $initF = function() use (&$f) {
            $f = [];
            for ($i = 0; $i < 20; $i++) $f[$i] = array_fill(0, 181, -1);
        };
        $dfs = function($pos, $diff, $lim) use (&$dfs, &$f, &$num, $BASE) {
            if ($pos >= strlen($num)) return $diff === 0 ? 1 : 0;
            if (!$lim && $f[$pos][$diff + $BASE] !== -1) return $f[$pos][$diff + $BASE];
            $up = $lim ? ord($num[$pos]) - 48 : 9;
            $res = 0;
            for ($i = 0; $i <= $up; $i++) {
                if ($pos % 2 === 0) $res += $dfs($pos + 1, $diff + $i, $lim && $i === $up);
                else $res += $dfs($pos + 1, $diff - $i, $lim && $i === $up);
            }
            if (!$lim) $f[$pos][$diff + $BASE] = $res;
            return $res;
        };
        if ($high < 11) return 0;
        if ($low < 11) $low = 11;
        $num = strval($low - 1);
        $initF();
        $a = $dfs(0, 0, true);
        $num = strval($high);
        $initF();
        $b = $dfs(0, 0, true);
        return $b - $a;
    }
}
''')

add("3792_sum_of_increasing_product_blocks", r'''<?php
// LeetCode 3792 - Sum of Increasing Product Blocks
// https://leetcode.com/problems/sum-of-increasing-product-blocks/

class Solution {
    function sumOfBlocks($n) {
        $MOD = 1000000007;
        $ans = 0;
        $k = 1;
        for ($i = 1; $i <= $n; $i++) {
            $x = 1;
            for ($j = $k; $j < $k + $i; $j++) $x = ($x * $j) % $MOD;
            $ans = ($ans + $x) % $MOD;
            $k += $i;
        }
        return $ans;
    }
}
''')

add("3794_reverse_string_prefix", r'''<?php
// LeetCode 3794 - Reverse String Prefix
// https://leetcode.com/problems/reverse-string-prefix/

class Solution {
    function reversePrefix($s, $k) {
        $arr = str_split($s);
        for ($i = 0, $j = $k - 1; $i < $j; $i++, $j--) {
            $t = $arr[$i]; $arr[$i] = $arr[$j]; $arr[$j] = $t;
        }
        return implode('', $arr);
    }
}
''')

add("3795_minimum_subarray_length_with_distinct_sum_at_least_k", r'''<?php
// LeetCode 3795 - Minimum Subarray Length With Distinct Sum At Least K
// https://leetcode.com/problems/minimum-subarray-length-with-distinct-sum-at-least-k/

class Solution {
    function minLength($nums, $k) {
        $n = count($nums);
        $ans = $n + 1;
        $l = 0;
        $cnt = [];
        $s = 0;
        for ($r = 0; $r < $n; $r++) {
            $c = (isset($cnt[$nums[$r]]) ? $cnt[$nums[$r]] : 0) + 1;
            $cnt[$nums[$r]] = $c;
            if ($c === 1) $s += $nums[$r];
            while ($s >= $k) {
                if ($r - $l + 1 < $ans) $ans = $r - $l + 1;
                $left = $nums[$l];
                $nc = $cnt[$left] - 1;
                if ($nc === 0) {
                    unset($cnt[$left]);
                    $s -= $left;
                } else $cnt[$left] = $nc;
                $l++;
            }
        }
        return $ans > $n ? -1 : $ans;
    }
}
''')

add("3796_find_maximum_value_in_a_constrained_sequence", r'''<?php
// LeetCode 3796 - Find Maximum Value in a Constrained Sequence
// https://leetcode.com/problems/find-maximum-value-in-a-constrained-sequence/

class Solution {
    function maxValue($n, $restrictions, $diff) {
        $INF = intdiv(2147483647, 4);
        $bound = array_fill(0, $n, $INF);
        $bound[0] = 0;
        foreach ($restrictions as $r) $bound[$r[0]] = $r[1];
        for ($i = 1; $i < $n; $i++) $bound[$i] = min($bound[$i], $bound[$i - 1] + $diff[$i - 1]);
        for ($i = $n - 2; $i >= 0; $i--) $bound[$i] = min($bound[$i], $bound[$i + 1] + $diff[$i]);
        $ans = $bound[0];
        for ($i = 1; $i < $n; $i++) $ans = max($ans, $bound[$i]);
        return $ans;
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

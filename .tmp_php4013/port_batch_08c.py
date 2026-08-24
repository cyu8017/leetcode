#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
SOLUTIONS = {}


def add(folder, body):
    SOLUTIONS[folder] = body


add("2479_maximum_xor_of_two_non_overlapping_subtrees", r'''<?php
// LeetCode 2479 - Maximum XOR of Two Non-Overlapping Subtrees
// https://leetcode.com/problems/maximum-xor-of-two-non-overlapping-subtrees/

class Solution {
    function maxXor($n, $edges, $values) {
        $g = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $g[$e[0]][] = $e[1];
            $g[$e[1]][] = $e[0];
        }
        $sum = array_fill(0, $n, 0);
        $dfsSum = function ($u, $p) use (&$dfsSum, &$g, $values, &$sum) {
            $s = $values[$u];
            foreach ($g[$u] as $v) if ($v !== $p) $s += $dfsSum($v, $u);
            $sum[$u] = $s;
            return $s;
        };
        $dfsSum(0, -1);
        $root = ["child" => [null, null]];
        $insert = function ($x) use (&$root) {
            $cur =& $root;
            for ($b = 46; $b >= 0; $b--) {
                $bit = (int)(($x >> $b) & 1);
                if ($cur["child"][$bit] === null) $cur["child"][$bit] = ["child" => [null, null]];
                $nxt =& $cur["child"][$bit];
                unset($cur);
                $cur =& $nxt;
                unset($nxt);
            }
            unset($cur);
        };
        $query = function ($x) use (&$root) {
            $cur = $root;
            if ($cur["child"][0] === null && $cur["child"][1] === null) return 0;
            $res = 0;
            for ($b = 46; $b >= 0; $b--) {
                $bit = (int)(($x >> $b) & 1);
                $want = $bit ^ 1;
                if ($cur["child"][$want] !== null) {
                    $res |= 1 << $b;
                    $cur = $cur["child"][$want];
                } elseif ($cur["child"][$bit] !== null) {
                    $cur = $cur["child"][$bit];
                } else {
                    return $res;
                }
            }
            return $res;
        };
        $ans = 0;
        $dfs = function ($u, $p) use (&$dfs, &$g, &$sum, $insert, $query, &$ans) {
            foreach ($g[$u] as $v) {
                if ($v === $p) continue;
                $xorv = $query($sum[$v]);
                if ($xorv > $ans) $ans = $xorv;
                $dfs($v, $u);
                $insert($sum[$v]);
            }
        };
        $dfs(0, -1);
        return $ans;
    }
}
''')

add("2481_minimum_cuts_to_divide_a_circle", r'''<?php
// LeetCode 2481 - Minimum Cuts to Divide a Circle
// https://leetcode.com/problems/minimum-cuts-to-divide-a-circle/

class Solution {
    function numberOfCuts($n) {
        if ($n === 1) return 0;
        if ($n % 2 === 0) return intdiv($n, 2);
        return $n;
    }
}
''')

add("2482_difference_between_ones_and_zeros_in_row_and_column", r'''<?php
// LeetCode 2482 - Difference Between Ones and Zeros in Row and Column
// https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column/

class Solution {
    function onesMinusZeros($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        $row = array_fill(0, $m, 0);
        $col = array_fill(0, $n, 0);
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                $row[$i] += $grid[$i][$j];
                $col[$j] += $grid[$i][$j];
            }
        }
        $ans = [];
        for ($i = 0; $i < $m; $i++) {
            $ans[$i] = array_fill(0, $n, 0);
            for ($j = 0; $j < $n; $j++) {
                $ans[$i][$j] = $row[$i] + $col[$j] - ($m - $row[$i]) - ($n - $col[$j]);
            }
        }
        return $ans;
    }
}
''')

add("2483_minimum_penalty_for_a_shop", r'''<?php
// LeetCode 2483 - Minimum Penalty for a Shop
// https://leetcode.com/problems/minimum-penalty-for-a-shop/

class Solution {
    function bestClosingTime($customers) {
        $n = strlen($customers);
        $penalty = 0;
        for ($i = 0; $i < $n; $i++) if ($customers[$i] === 'Y') $penalty++;
        $best = $penalty;
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            if ($customers[$i] === 'Y') $penalty--;
            else $penalty++;
            if ($penalty < $best) {
                $best = $penalty;
                $ans = $i + 1;
            }
        }
        return $ans;
    }
}
''')

add("2484_count_palindromic_subsequences", r'''<?php
// LeetCode 2484 - Count Palindromic Subsequences
// https://leetcode.com/problems/count-palindromic-subsequences/

class Solution {
    function countPalindromes($s) {
        $mod = 1000000007;
        $n = strlen($s);
        $pref = [];
        $suf = [];
        for ($i = 0; $i < $n; $i++) {
            $row = [];
            for ($a = 0; $a < 10; $a++) $row[] = array_fill(0, 10, 0);
            $pref[] = $row;
            $row2 = [];
            for ($a = 0; $a < 10; $a++) $row2[] = array_fill(0, 10, 0);
            $suf[] = $row2;
        }
        $cnt = array_fill(0, 10, 0);
        for ($i = 0; $i < $n; $i++) {
            if ($i > 0) {
                for ($a = 0; $a < 10; $a++)
                    for ($b = 0; $b < 10; $b++) $pref[$i][$a][$b] = $pref[$i - 1][$a][$b];
            }
            $d = ord($s[$i]) - 48;
            for ($a = 0; $a < 10; $a++) $pref[$i][$a][$d] += $cnt[$a];
            $cnt[$d]++;
        }
        $cnt = array_fill(0, 10, 0);
        for ($i = $n - 1; $i >= 0; $i--) {
            if ($i + 1 < $n) {
                for ($a = 0; $a < 10; $a++)
                    for ($b = 0; $b < 10; $b++) $suf[$i][$a][$b] = $suf[$i + 1][$a][$b];
            }
            $d = ord($s[$i]) - 48;
            for ($a = 0; $a < 10; $a++) $suf[$i][$a][$d] += $cnt[$a];
            $cnt[$d]++;
        }
        $ans = 0;
        for ($i = 2; $i < $n - 2; $i++) {
            for ($a = 0; $a < 10; $a++) {
                for ($b = 0; $b < 10; $b++) {
                    $ans = ($ans + $pref[$i - 1][$a][$b] * $suf[$i + 1][$a][$b]) % $mod;
                }
            }
        }
        return $ans;
    }
}
''')

add("2485_find_the_pivot_integer", r'''<?php
// LeetCode 2485 - Find the Pivot Integer
// https://leetcode.com/problems/find-the-pivot-integer/

class Solution {
    function pivotInteger($n) {
        $total = intdiv($n * ($n + 1), 2);
        $sum = 0;
        for ($x = 1; $x <= $n; $x++) {
            $sum += $x;
            if ($sum === $total - $sum + $x) return $x;
        }
        return -1;
    }
}
''')

add("2486_append_characters_to_string_to_make_subsequence", r'''<?php
// LeetCode 2486 - Append Characters to String to Make Subsequence
// https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/

class Solution {
    function appendCharacters($s, $t) {
        $j = 0;
        $sn = strlen($s);
        $tn = strlen($t);
        for ($i = 0; $i < $sn && $j < $tn; $i++) {
            if ($s[$i] === $t[$j]) $j++;
        }
        return $tn - $j;
    }
}
''')

add("2487_remove_nodes_from_linked_list", r'''<?php
// LeetCode 2487 - Remove Nodes From Linked List
// https://leetcode.com/problems/remove-nodes-from-linked-list/

class ListNode {
    public $val = 0;
    public $next = null;
    function __construct($val = 0, $next = null) {
        $this->val = $val;
        $this->next = $next;
    }
}

class Solution {
    function removeNodes($head) {
        $rev = function ($node) {
            $prev = null;
            while ($node !== null) {
                $nxt = $node->next;
                $node->next = $prev;
                $prev = $node;
                $node = $nxt;
            }
            return $prev;
        };
        $head = $rev($head);
        $mx = 0;
        $dummy = new ListNode(0, $head);
        $prev = $dummy;
        while ($prev->next !== null) {
            if ($prev->next->val >= $mx) {
                $mx = $prev->next->val;
                $prev = $prev->next;
            } else {
                $prev->next = $prev->next->next;
            }
        }
        return $rev($dummy->next);
    }
}
''')

add("2488_count_subarrays_with_median_k", r'''<?php
// LeetCode 2488 - Count Subarrays With Median K
// https://leetcode.com/problems/count-subarrays-with-median-k/

class Solution {
    function countSubarrays($nums, $k) {
        $pos = 0;
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            if ($nums[$i] === $k) { $pos = $i; break; }
        }
        $bal = [];
        $bal[0] = 1;
        $cur = 0;
        for ($i = $pos - 1; $i >= 0; $i--) {
            $cur += $nums[$i] < $k ? -1 : 1;
            if (!isset($bal[$cur])) $bal[$cur] = 0;
            $bal[$cur]++;
        }
        $ans = (isset($bal[0]) ? $bal[0] : 0) + (isset($bal[1]) ? $bal[1] : 0);
        $cur = 0;
        for ($i = $pos + 1; $i < $n; $i++) {
            $cur += $nums[$i] < $k ? -1 : 1;
            $ans += (isset($bal[-$cur]) ? $bal[-$cur] : 0) + (isset($bal[1 - $cur]) ? $bal[1 - $cur] : 0);
        }
        return $ans;
    }
}
''')

add("2489_number_of_substrings_with_fixed_ratio", r'''<?php
// LeetCode 2489 - Number of Substrings With Fixed Ratio
// https://leetcode.com/problems/number-of-substrings-with-fixed-ratio/

class Solution {
    function fixedRatio($s, $num1, $num2) {
        $pref = [];
        $pref[0] = 1;
        $zeros = 0;
        $ones = 0;
        $ans = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            if ($s[$i] === '0') $zeros++;
            else $ones++;
            $key = $zeros * $num2 - $ones * $num1;
            $ans += isset($pref[$key]) ? $pref[$key] : 0;
            if (!isset($pref[$key])) $pref[$key] = 0;
            $pref[$key]++;
        }
        return $ans;
    }
}
''')

add("2490_circular_sentence", r'''<?php
// LeetCode 2490 - Circular Sentence
// https://leetcode.com/problems/circular-sentence/

class Solution {
    function isCircularSentence($sentence) {
        $n = strlen($sentence);
        if ($sentence[0] !== $sentence[$n - 1]) return false;
        for ($i = 0; $i < $n; $i++) {
            if ($sentence[$i] === ' ' && $sentence[$i - 1] !== $sentence[$i + 1]) return false;
        }
        return true;
    }
}
''')

add("2491_divide_players_into_teams_of_equal_skill", r'''<?php
// LeetCode 2491 - Divide Players Into Teams of Equal Skill
// https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution {
    function dividePlayers($skill) {
        sort($skill);
        $n = count($skill);
        $target = $skill[0] + $skill[$n - 1];
        $chem = 0;
        for ($i = 0; $i < intdiv($n, 2); $i++) {
            if ($skill[$i] + $skill[$n - 1 - $i] !== $target) return -1;
            $chem += $skill[$i] * $skill[$n - 1 - $i];
        }
        return $chem;
    }
}
''')

add("2492_minimum_score_of_a_path_between_two_cities", r'''<?php
// LeetCode 2492 - Minimum Score of a Path Between Two Cities
// https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/

class Solution {
    function minScore($n, $roads) {
        $g = array_fill(0, $n + 1, []);
        foreach ($roads as $r) {
            $g[$r[0]][] = [$r[1], $r[2]];
            $g[$r[1]][] = [$r[0], $r[2]];
        }
        $vis = array_fill(0, $n + 1, false);
        $ans = 1 << 30;
        $q = [1];
        $vis[1] = true;
        while (count($q)) {
            $u = array_shift($q);
            foreach ($g[$u] as $e) {
                $v = $e[0];
                $w = $e[1];
                if ($w < $ans) $ans = $w;
                if (!$vis[$v]) {
                    $vis[$v] = true;
                    $q[] = $v;
                }
            }
        }
        return $ans;
    }
}
''')

add("2493_divide_nodes_into_the_maximum_number_of_groups", r'''<?php
// LeetCode 2493 - Divide Nodes Into the Maximum Number of Groups
// https://leetcode.com/problems/divide-nodes-into-the-maximum-number-of-groups/

class Solution {
    function magnificentSets($n, $edges) {
        $g = array_fill(0, $n + 1, []);
        foreach ($edges as $e) {
            $g[$e[0]][] = $e[1];
            $g[$e[1]][] = $e[0];
        }
        $bfsDepth = function ($start) use ($n, &$g) {
            $dist = array_fill(0, $n + 1, -1);
            $q = [$start];
            $dist[$start] = 1;
            $best = 1;
            while (count($q)) {
                $u = array_shift($q);
                if ($dist[$u] > $best) $best = $dist[$u];
                foreach ($g[$u] as $v) {
                    if ($dist[$v] === -1) {
                        $dist[$v] = $dist[$u] + 1;
                        $q[] = $v;
                    }
                }
            }
            return $best;
        };
        $color = array_fill(0, $n + 1, -1);
        $components = [];
        for ($i = 1; $i <= $n; $i++) {
            if ($color[$i] !== -1) continue;
            $comp = [];
            $q = [$i];
            $color[$i] = 0;
            $bipartite = true;
            while (count($q)) {
                $u = array_shift($q);
                $comp[] = $u;
                foreach ($g[$u] as $v) {
                    if ($color[$v] === -1) {
                        $color[$v] = $color[$u] ^ 1;
                        $q[] = $v;
                    } elseif ($color[$v] === $color[$u]) {
                        $bipartite = false;
                    }
                }
            }
            if (!$bipartite) return -1;
            $components[] = $comp;
        }
        $ans = 0;
        foreach ($components as $comp) {
            $best = 0;
            foreach ($comp as $u) $best = max($best, $bfsDepth($u));
            $ans += $best;
        }
        return $ans;
    }
}
''')

add("2495_number_of_subarrays_having_even_product", r'''<?php
// LeetCode 2495 - Number of Subarrays Having Even Product
// https://leetcode.com/problems/number-of-subarrays-having-even-product/

class Solution {
    function evenProduct($nums) {
        $n = count($nums);
        $total = intdiv($n * ($n + 1), 2);
        $oddLen = 0;
        $odd = 0;
        foreach ($nums as $x) {
            if ($x % 2 === 1) {
                $odd++;
                $oddLen += $odd;
            } else $odd = 0;
        }
        return $total - $oddLen;
    }
}
''')

add("2496_maximum_value_of_a_string_in_an_array", r'''<?php
// LeetCode 2496 - Maximum Value of a String in an Array
// https://leetcode.com/problems/maximum-value-of-a-string-in-an-array/

class Solution {
    function maximumValue($strs) {
        $ans = 0;
        foreach ($strs as $s) {
            $allDigit = true;
            $val = 0;
            $len = strlen($s);
            for ($i = 0; $i < $len; $i++) {
                $c = $s[$i];
                if ($c < '0' || $c > '9') { $allDigit = false; break; }
                $val = $val * 10 + (ord($c) - 48);
            }
            if (!$allDigit) $val = $len;
            if ($val > $ans) $ans = $val;
        }
        return $ans;
    }
}
''')

add("2497_maximum_star_sum_of_a_graph", r'''<?php
// LeetCode 2497 - Maximum Star Sum of a Graph
// https://leetcode.com/problems/maximum-star-sum-of-a-graph/

class Solution {
    function maxStarSum($vals, $edges, $k) {
        $n = count($vals);
        $g = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $g[$e[0]][] = $e[1];
            $g[$e[1]][] = $e[0];
        }
        $ans = $vals[0];
        for ($i = 0; $i < $n; $i++) {
            $neigh = [];
            foreach ($g[$i] as $v) {
                if ($vals[$v] > 0) $neigh[] = $vals[$v];
            }
            rsort($neigh);
            $sum = $vals[$i];
            for ($j = 0; $j < count($neigh) && $j < $k; $j++) $sum += $neigh[$j];
            if ($sum > $ans) $ans = $sum;
        }
        return $ans;
    }
}
''')

add("2498_frog_jump_ii", r'''<?php
// LeetCode 2498 - Frog Jump II
// https://leetcode.com/problems/frog-jump-ii/

class Solution {
    function maxJump($stones) {
        $ans = $stones[1] - $stones[0];
        for ($i = 2; $i < count($stones); $i++) {
            $diff = $stones[$i] - $stones[$i - 2];
            if ($diff > $ans) $ans = $diff;
        }
        return $ans;
    }
}
''')

add("2499_minimum_total_cost_to_make_arrays_unequal", r'''<?php
// LeetCode 2499 - Minimum Total Cost to Make Arrays Unequal
// https://leetcode.com/problems/minimum-total-cost-to-make-arrays-unequal/

class Solution {
    function minimumTotalCost($nums1, $nums2) {
        $n = count($nums1);
        $freq = [];
        $ans = 0;
        $same = 0;
        for ($i = 0; $i < $n; $i++) {
            if ($nums1[$i] === $nums2[$i]) {
                $same++;
                if (!isset($freq[$nums1[$i]])) $freq[$nums1[$i]] = 0;
                $freq[$nums1[$i]]++;
                $ans += $i;
            }
        }
        $maxFreq = 0;
        $maxVal = 0;
        foreach ($freq as $key => $value) {
            if ($value > $maxFreq) {
                $maxFreq = $value;
                $maxVal = $key;
            }
        }
        $need = $maxFreq * 2 - $same;
        if ($need <= 0) return $ans;
        for ($i = 0; $i < $n && $need > 0; $i++) {
            if ($nums1[$i] !== $nums2[$i] && $nums1[$i] !== $maxVal && $nums2[$i] !== $maxVal) {
                $ans += $i;
                $need--;
            }
        }
        return $need > 0 ? -1 : $ans;
    }
}
''')

add("2500_delete_greatest_value_in_each_row", r'''<?php
// LeetCode 2500 - Delete Greatest Value in Each Row
// https://leetcode.com/problems/delete-greatest-value-in-each-row/

class Solution {
    function deleteGreatestValue($grid) {
        foreach ($grid as &$row) sort($row);
        unset($row);
        $ans = 0;
        $n = count($grid[0]);
        for ($c = 0; $c < $n; $c++) {
            $mx = 0;
            foreach ($grid as $row) if ($row[$c] > $mx) $mx = $row[$c];
            $ans += $mx;
        }
        return $ans;
    }
}
''')

add("2501_longest_square_streak_in_an_array", r'''<?php
// LeetCode 2501 - Longest Square Streak in an Array
// https://leetcode.com/problems/longest-square-streak-in-an-array/

class Solution {
    function longestSquareStreak($nums) {
        $set = [];
        foreach ($nums as $x) $set[$x] = true;
        $best = -1;
        foreach ($nums as $x) {
            if (!isset($set[$x])) continue;
            $length = 0;
            $cur = $x;
            while (isset($set[$cur])) {
                $length++;
                unset($set[$cur]);
                if ($cur > 100000) break;
                $cur = $cur * $cur;
            }
            if ($length >= 2 && $length > $best) $best = $length;
        }
        return $best;
    }
}
''')

add("2502_design_memory_allocator", r'''<?php
// LeetCode 2502 - Design Memory Allocator
// https://leetcode.com/problems/design-memory-allocator/

class Allocator {
    private $mem;

    function __construct($n) {
        $this->mem = array_fill(0, $n, 0);
    }

    function allocate($size, $mID) {
        $freeCnt = 0;
        $len = count($this->mem);
        for ($i = 0; $i < $len; $i++) {
            if ($this->mem[$i] === 0) {
                $freeCnt++;
                if ($freeCnt === $size) {
                    $start = $i - $size + 1;
                    for ($j = $start; $j <= $i; $j++) $this->mem[$j] = $mID;
                    return $start;
                }
            } else $freeCnt = 0;
        }
        return -1;
    }

    function freeMemory($mID) {
        $cnt = 0;
        $len = count($this->mem);
        for ($i = 0; $i < $len; $i++) {
            if ($this->mem[$i] === $mID) {
                $this->mem[$i] = 0;
                $cnt++;
            }
        }
        return $cnt;
    }
}
''')

add("2503_maximum_number_of_points_from_grid_queries", r'''<?php
// LeetCode 2503 - Maximum Number of Points From Grid Queries
// https://leetcode.com/problems/maximum-number-of-points-from-grid-queries/

class Solution {
    function maxPoints($grid, $queries) {
        $m = count($grid);
        $n = count($grid[0]);
        $order = range(0, count($queries) - 1);
        usort($order, function ($a, $b) use ($queries) {
            return $queries[$a] <=> $queries[$b];
        });
        $ans = array_fill(0, count($queries), 0);
        $visited = [];
        for ($i = 0; $i < $m; $i++) $visited[] = array_fill(0, $n, false);
        $pq = new SplPriorityQueue();
        $pq->insert([0, 0], -$grid[0][0]);
        $visited[0][0] = true;
        $points = 0;
        $dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];
        $peekVal = $grid[0][0];
        $pending = [[$grid[0][0], 0, 0]];
        $heap = new SplPriorityQueue();
        $heap->insert([$grid[0][0], 0, 0], -$grid[0][0]);
        foreach ($order as $qi) {
            $q = $queries[$qi];
            while (!$heap->isEmpty()) {
                $top = $heap->top();
                if ($top[0] >= $q) break;
                $cur = $heap->extract();
                $r = $cur[1];
                $c = $cur[2];
                $points++;
                foreach ($dirs as $d) {
                    $nr = $r + $d[0];
                    $nc = $c + $d[1];
                    if ($nr >= 0 && $nr < $m && $nc >= 0 && $nc < $n && !$visited[$nr][$nc]) {
                        $visited[$nr][$nc] = true;
                        $heap->insert([$grid[$nr][$nc], $nr, $nc], -$grid[$nr][$nc]);
                    }
                }
            }
            $ans[$qi] = $points;
        }
        return $ans;
    }
}
''')

add("2505_bitwise_or_of_all_subsequence_sums", r'''<?php
// LeetCode 2505 - Bitwise OR of All Subsequence Sums
// https://leetcode.com/problems/bitwise-or-of-all-subsequence-sums/

class Solution {
    function subsequenceSumOr($nums) {
        $ans = 0;
        $prefix = 0;
        foreach ($nums as $x) {
            $prefix += $x;
            $ans |= $x | $prefix;
        }
        return $ans;
    }
}
''')

add("2506_count_pairs_of_similar_strings", r'''<?php
// LeetCode 2506 - Count Pairs Of Similar Strings
// https://leetcode.com/problems/count-pairs-of-similar-strings/

class Solution {
    function similarPairs($words) {
        $freq = [];
        $ans = 0;
        foreach ($words as $w) {
            $mask = 0;
            $len = strlen($w);
            for ($i = 0; $i < $len; $i++) $mask |= 1 << (ord($w[$i]) - 97);
            $ans += isset($freq[$mask]) ? $freq[$mask] : 0;
            if (!isset($freq[$mask])) $freq[$mask] = 0;
            $freq[$mask]++;
        }
        return $ans;
    }
}
''')

add("2507_smallest_value_after_replacing_with_sum_of_prime_factors", r'''<?php
// LeetCode 2507 - Smallest Value After Replacing With Sum of Prime Factors
// https://leetcode.com/problems/smallest-value-after-replacing-with-sum-of-prime-factors/

class Solution {
    function smallestValue($n) {
        $sumPrimeFactors = function ($x) {
            $s = 0;
            for ($i = 2; $i * $i <= $x; $i++) {
                while ($x % $i === 0) {
                    $s += $i;
                    $x = intdiv($x, $i);
                }
            }
            if ($x > 1) $s += $x;
            return $s;
        };
        while (true) {
            $s = $sumPrimeFactors($n);
            if ($s === $n) return $n;
            $n = $s;
        }
    }
}
''')

add("2508_add_edges_to_make_degrees_of_all_nodes_even", r'''<?php
// LeetCode 2508 - Add Edges to Make Degrees of All Nodes Even
// https://leetcode.com/problems/add-edges-to-make-degrees-of-all-nodes-even/

class Solution {
    function isPossible($n, $edges) {
        $deg = array_fill(0, $n + 1, 0);
        $adj = array_fill(0, $n + 1, []);
        foreach ($edges as $e) {
            $u = $e[0];
            $v = $e[1];
            $deg[$u]++;
            $deg[$v]++;
            $adj[$u][$v] = true;
            $adj[$v][$u] = true;
        }
        $odd = [];
        for ($i = 1; $i <= $n; $i++) if ($deg[$i] % 2 === 1) $odd[] = $i;
        if (count($odd) === 0) return true;
        if (count($odd) === 2) {
            $a = $odd[0];
            $b = $odd[1];
            if (!isset($adj[$a][$b])) return true;
            for ($i = 1; $i <= $n; $i++) {
                if ($i !== $a && $i !== $b && !isset($adj[$a][$i]) && !isset($adj[$b][$i])) return true;
            }
            return false;
        }
        if (count($odd) === 4) {
            $a = $odd[0];
            $b = $odd[1];
            $c = $odd[2];
            $d = $odd[3];
            return (!isset($adj[$a][$b]) && !isset($adj[$c][$d])) ||
                   (!isset($adj[$a][$c]) && !isset($adj[$b][$d])) ||
                   (!isset($adj[$a][$d]) && !isset($adj[$b][$c]));
        }
        return false;
    }
}
''')

add("2509_cycle_length_queries_in_a_tree", r'''<?php
// LeetCode 2509 - Cycle Length Queries in a Tree
// https://leetcode.com/problems/cycle-length-queries-in-a-tree/

class Solution {
    function cycleLengthQueries($n, $queries) {
        $ans = array_fill(0, count($queries), 0);
        for ($i = 0; $i < count($queries); $i++) {
            $a = $queries[$i][0];
            $b = $queries[$i][1];
            $steps = 0;
            while ($a !== $b) {
                if ($a > $b) $a = intdiv($a, 2);
                else $b = intdiv($b, 2);
                $steps++;
            }
            $ans[$i] = $steps + 1;
        }
        return $ans;
    }
}
''')

add("2510_check_if_there_is_a_path_with_equal_number_of_0s_and_1s", r'''<?php
// LeetCode 2510 - Check if There is a Path With Equal Number of 0's And 1's
// https://leetcode.com/problems/check-if-there-is-a-path-with-equal-number-of-0s-and-1s/

class Solution {
    function isThereAPath($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        if (($m + $n - 1) % 2 !== 0) return false;
        $target = intdiv($m + $n - 1, 2);
        $memo = [];
        $dfs = function ($r, $c, $bal) use (&$dfs, $grid, $m, $n, $target, &$memo) {
            if ($r >= $m || $c >= $n) return false;
            $bal += $grid[$r][$c];
            if ($bal > $target || $bal + ($m - 1 - $r) + ($n - 1 - $c) < $target) return false;
            if ($r === $m - 1 && $c === $n - 1) return $bal === $target;
            $k = $r . ',' . $c . ',' . $bal;
            if (isset($memo[$k])) return $memo[$k];
            $ok = $dfs($r + 1, $c, $bal) || $dfs($r, $c + 1, $bal);
            $memo[$k] = $ok;
            return $ok;
        };
        return $dfs(0, 0, 0);
    }
}
''')

add("2511_maximum_enemy_forts_that_can_be_captured", r'''<?php
// LeetCode 2511 - Maximum Enemy Forts That Can Be Captured
// https://leetcode.com/problems/maximum-enemy-forts-that-can-be-captured/

class Solution {
    function captureForts($forts) {
        $ans = 0;
        $prev = -1;
        $n = count($forts);
        for ($i = 0; $i < $n; $i++) {
            if ($forts[$i] !== 0) {
                if ($prev >= 0 && $forts[$prev] === -$forts[$i]) {
                    if ($i - $prev - 1 > $ans) $ans = $i - $prev - 1;
                }
                $prev = $i;
            }
        }
        return $ans;
    }
}
''')

add("2512_reward_top_k_students", r'''<?php
// LeetCode 2512 - Reward Top K Students
// https://leetcode.com/problems/reward-top-k-students/

class Solution {
    function topStudents($positive_feedback, $negative_feedback, $report, $student_id, $k) {
        $pos = [];
        foreach ($positive_feedback as $w) $pos[$w] = true;
        $neg = [];
        foreach ($negative_feedback as $w) $neg[$w] = true;
        $arr = [];
        for ($i = 0; $i < count($report); $i++) {
            $score = 0;
            foreach (explode(' ', $report[$i]) as $w) {
                if ($w === '') continue;
                if (isset($pos[$w])) $score += 3;
                elseif (isset($neg[$w])) $score--;
            }
            $arr[] = [$student_id[$i], $score];
        }
        usort($arr, function ($a, $b) {
            if ($a[1] !== $b[1]) return $b[1] <=> $a[1];
            return $a[0] <=> $b[0];
        });
        $ans = [];
        for ($i = 0; $i < $k; $i++) $ans[] = $arr[$i][0];
        return $ans;
    }
}
''')

add("2513_minimize_the_maximum_of_two_arrays", r'''<?php
// LeetCode 2513 - Minimize the Maximum of Two Arrays
// https://leetcode.com/problems/minimize-the-maximum-of-two-arrays/

class Solution {
    function minimizeSet($divisor1, $divisor2, $uniqueCnt1, $uniqueCnt2) {
        $gcd = function ($a, $b) {
            while ($b !== 0) {
                $t = $a % $b;
                $a = $b;
                $b = $t;
            }
            return $a;
        };
        $lcm = intdiv($divisor1, $gcd($divisor1, $divisor2)) * $divisor2;
        $ok = function ($x) use ($divisor1, $divisor2, $lcm, $uniqueCnt1, $uniqueCnt2) {
            $a = $x - intdiv($x, $divisor1);
            $b = $x - intdiv($x, $divisor2);
            $both = $x - intdiv($x, $lcm);
            return $a >= $uniqueCnt1 && $b >= $uniqueCnt2 && $both >= $uniqueCnt1 + $uniqueCnt2;
        };
        $lo = 1;
        $hi = 1 << 62;
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi, 2);
            if ($ok($mid)) $hi = $mid;
            else $lo = $mid + 1;
        }
        return $lo;
    }
}
''')

add("2514_count_anagrams", r'''<?php
// LeetCode 2514 - Count Anagrams
// https://leetcode.com/problems/count-anagrams/

class Solution {
    function countAnagrams($s) {
        $MOD = 1000000007;
        $modPow = function ($a, $e) use ($MOD) {
            $res = 1;
            $a %= $MOD;
            while ($e > 0) {
                if ($e & 1) $res = ($res * $a) % $MOD;
                $a = ($a * $a) % $MOD;
                $e >>= 1;
            }
            return $res;
        };
        $trimmed = trim($s);
        $words = $trimmed === '' ? [] : preg_split('/\s+/', $trimmed);
        $maxN = 0;
        foreach ($words as $w) if (strlen($w) > $maxN) $maxN = strlen($w);
        $fact = array_fill(0, $maxN + 1, 0);
        $invFact = array_fill(0, $maxN + 1, 0);
        $fact[0] = 1;
        for ($i = 1; $i <= $maxN; $i++) $fact[$i] = ($fact[$i - 1] * $i) % $MOD;
        $invFact[$maxN] = $modPow($fact[$maxN], $MOD - 2);
        for ($i = $maxN; $i > 0; $i--) $invFact[$i - 1] = ($invFact[$i] * $i) % $MOD;
        $ans = 1;
        foreach ($words as $word) {
            $cnt = array_fill(0, 26, 0);
            $len = strlen($word);
            for ($i = 0; $i < $len; $i++) $cnt[ord($word[$i]) - 97]++;
            $cur = $fact[$len];
            foreach ($cnt as $c) $cur = ($cur * $invFact[$c]) % $MOD;
            $ans = ($ans * $cur) % $MOD;
        }
        return $ans;
    }
}
''')

add("2515_shortest_distance_to_target_string_in_a_circular_array", r'''<?php
// LeetCode 2515 - Shortest Distance to Target String in a Circular Array
// https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array/

class Solution {
    function closestTarget($words, $target, $startIndex) {
        $n = count($words);
        $best = -1;
        for ($i = 0; $i < $n; $i++) {
            if ($words[$i] === $target) {
                $d = $i - $startIndex;
                if ($d < 0) $d = -$d;
                if ($n - $d < $d) $d = $n - $d;
                if ($best < 0 || $d < $best) $best = $d;
            }
        }
        return $best;
    }
}
''')

add("2516_take_k_of_each_character_from_left_and_right", r'''<?php
// LeetCode 2516 - Take K of Each Character From Left and Right
// https://leetcode.com/problems/take-k-of-each-character-from-left-and-right/

class Solution {
    function takeCharacters($s, $k) {
        $n = strlen($s);
        $cnt = [0, 0, 0];
        for ($i = 0; $i < $n; $i++) $cnt[ord($s[$i]) - 97]++;
        if ($cnt[0] < $k || $cnt[1] < $k || $cnt[2] < $k) return -1;
        $need = [$cnt[0] - $k, $cnt[1] - $k, $cnt[2] - $k];
        $window = [0, 0, 0];
        $left = 0;
        $maxMid = 0;
        for ($right = 0; $right < $n; $right++) {
            $window[ord($s[$right]) - 97]++;
            while ($window[0] > $need[0] || $window[1] > $need[1] || $window[2] > $need[2]) {
                $window[ord($s[$left]) - 97]--;
                $left++;
            }
            if ($right - $left + 1 > $maxMid) $maxMid = $right - $left + 1;
        }
        return $n - $maxMid;
    }
}
''')

add("2517_maximum_tastiness_of_candy_basket", r'''<?php
// LeetCode 2517 - Maximum Tastiness of Candy Basket
// https://leetcode.com/problems/maximum-tastiness-of-candy-basket/

class Solution {
    function maximumTastiness($price, $k) {
        sort($price);
        $ok = function ($d) use ($price, $k) {
            $cnt = 1;
            $last = $price[0];
            for ($i = 1; $i < count($price); $i++) {
                if ($price[$i] - $last >= $d) {
                    $cnt++;
                    $last = $price[$i];
                    if ($cnt >= $k) return true;
                }
            }
            return false;
        };
        $lo = 0;
        $hi = $price[count($price) - 1] - $price[0];
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi + 1, 2);
            if ($ok($mid)) $lo = $mid;
            else $hi = $mid - 1;
        }
        return $lo;
    }
}
''')

add("2518_number_of_great_partitions", r'''<?php
// LeetCode 2518 - Number of Great Partitions
// https://leetcode.com/problems/number-of-great-partitions/

class Solution {
    function countPartitions($nums, $k) {
        $MOD = 1000000007;
        $sum = 0;
        foreach ($nums as $x) $sum += $x;
        if ($sum < 2 * $k) return 0;
        $dp = array_fill(0, $k, 0);
        $dp[0] = 1;
        foreach ($nums as $x) {
            for ($s = $k - 1; $s >= $x; $s--)
                $dp[$s] = ($dp[$s] + $dp[$s - $x]) % $MOD;
        }
        $bad = 0;
        foreach ($dp as $v) $bad = ($bad + $v) % $MOD;
        $total = 1;
        for ($i = 0; $i < count($nums); $i++) $total = ($total * 2) % $MOD;
        return ($total - (2 * $bad) % $MOD + $MOD) % $MOD;
    }
}
''')

add("2519_count_the_number_of_k_big_indices", r'''<?php
// LeetCode 2519 - Count the Number of K-Big Indices
// https://leetcode.com/problems/count-the-number-of-k-big-indices/

class Fenwick {
    public $bit;
    function __construct($n) {
        $this->bit = array_fill(0, $n + 2, 0);
    }
    function add($i, $v) {
        $len = count($this->bit);
        for (; $i < $len; $i += $i & -$i) $this->bit[$i] += $v;
    }
    function sum($i) {
        $s = 0;
        for (; $i > 0; $i -= $i & -$i) $s += $this->bit[$i];
        return $s;
    }
}

class Solution {
    function kBigIndices($nums, $k) {
        $n = count($nums);
        $uniq = $nums;
        sort($uniq);
        $m = 0;
        for ($i = 0; $i < count($uniq); $i++) {
            if ($i === 0 || $uniq[$i] !== $uniq[$i - 1]) $uniq[$m++] = $uniq[$i];
        }
        $rank = [];
        for ($i = 0; $i < $m; $i++) $rank[$uniq[$i]] = $i + 1;
        $left = array_fill(0, $n, 0);
        $right = array_fill(0, $n, 0);
        $ft = new Fenwick($m);
        for ($i = 0; $i < $n; $i++) {
            $r = $rank[$nums[$i]];
            $left[$i] = $ft->sum($r - 1);
            $ft->add($r, 1);
        }
        $ft = new Fenwick($m);
        for ($i = $n - 1; $i >= 0; $i--) {
            $r = $rank[$nums[$i]];
            $right[$i] = $ft->sum($r - 1);
            $ft->add($r, 1);
        }
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            if ($left[$i] >= $k && $right[$i] >= $k) $ans++;
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

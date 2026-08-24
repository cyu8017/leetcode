#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
SOLUTIONS = {}

def add(folder, body):
    SOLUTIONS[folder] = body if body.endswith("\n") else body + "\n"


MINHEAP = r'''
class MinHeap {
    public $a = [];
    public $cmp;
    function __construct($cmp = null) {
        $this->cmp = $cmp;
    }
    function _up($i) {
        $a = &$this->a;
        $cmp = $this->cmp;
        while ($i > 0) {
            $p = ($i - 1) >> 1;
            $c = $cmp ? $cmp($a[$i], $a[$p]) : ($a[$i] <=> $a[$p]);
            if ($c >= 0) break;
            $t = $a[$i]; $a[$i] = $a[$p]; $a[$p] = $t;
            $i = $p;
        }
    }
    function _down($i) {
        $a = &$this->a;
        $cmp = $this->cmp;
        $n = count($a);
        while (true) {
            $s = $i; $l = $i * 2 + 1; $r = $l + 1;
            if ($l < $n) {
                $c = $cmp ? $cmp($a[$l], $a[$s]) : ($a[$l] <=> $a[$s]);
                if ($c < 0) $s = $l;
            }
            if ($r < $n) {
                $c = $cmp ? $cmp($a[$r], $a[$s]) : ($a[$r] <=> $a[$s]);
                if ($c < 0) $s = $r;
            }
            if ($s === $i) break;
            $t = $a[$i]; $a[$i] = $a[$s]; $a[$s] = $t;
            $i = $s;
        }
    }
    function push($x) { $this->a[] = $x; $this->_up(count($this->a) - 1); }
    function pop() {
        $a = &$this->a;
        if (!$a) return null;
        $top = $a[0];
        $last = array_pop($a);
        if ($a) { $a[0] = $last; $this->_down(0); }
        return $top;
    }
    function peek() { return $this->a[0]; }
    function size() { return count($this->a); }
}
'''

BIT = r'''
class BIT {
    public $n;
    public $c;
    function __construct($n) {
        $this->n = $n;
        $this->c = array_fill(0, $n + 1, 0);
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
'''

add("3062_winner_of_the_linked_list_game", r'''<?php
// LeetCode 3062 - Winner of the Linked List Game
// https://leetcode.com/problems/winner-of-the-linked-list-game/

class ListNode {
    public $val = 0;
    public $next = null;
    function __construct($val = 0, $next = null) {
        $this->val = $val;
        $this->next = $next;
    }
}

class Solution {
    function gameResult($head) {
        $odd = 0;
        $even = 0;
        for (; $head !== null; $head = $head->next->next) {
            $a = $head->val;
            $b = $head->next->val;
            if ($a < $b) $odd++;
            if ($a > $b) $even++;
        }
        if ($odd > $even) return "Odd";
        if ($odd < $even) return "Even";
        return "Tie";
    }
}
''')

add("3063_linked_list_frequency", r'''<?php
// LeetCode 3063 - Linked List Frequency
// https://leetcode.com/problems/linked-list-frequency/

class ListNode {
    public $val = 0;
    public $next = null;
    function __construct($val = 0, $next = null) {
        $this->val = $val;
        $this->next = $next;
    }
}

class Solution {
    function frequenciesOfElements($head) {
        $cnt = [];
        for (; $head !== null; $head = $head->next) {
            $v = $head->val;
            $cnt[$v] = ($cnt[$v] ?? 0) + 1;
        }
        $dummy = new ListNode(0);
        foreach ($cnt as $val) {
            $dummy->next = new ListNode($val, $dummy->next);
        }
        return $dummy->next;
    }
}
''')

add("3064_guess_the_number_using_bitwise_questions_i", r'''<?php
// LeetCode 3064 - Guess the Number Using Bitwise Questions I
// https://leetcode.com/problems/guess-the-number-using-bitwise-questions-i/

function commonSetBits($num) {
    global $hiddenNumber;
    return substr_count(decbin(($hiddenNumber ?? 0) & $num), "1");
}

class Solution {
    function findNumber() {
        $n = 0;
        for ($i = 0; $i < 32; $i++) {
            if (commonSetBits(1 << $i) > 0) $n |= 1 << $i;
        }
        return $n;
    }
}
''')

add("3065_minimum_operations_to_exceed_threshold_value_i", r'''<?php
// LeetCode 3065 - Minimum Operations to Exceed Threshold Value I
// https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-i/

class Solution {
    function minOperations($nums, $k) {
        $ans = 0;
        foreach ($nums as $x) if ($x < $k) $ans++;
        return $ans;
    }
}
''')

add("3066_minimum_operations_to_exceed_threshold_value_ii", '''<?php
// LeetCode 3066 - Minimum Operations to Exceed Threshold Value II
// https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/
''' + MINHEAP + r'''
class Solution {
    function minOperations($nums, $k) {
        $pq = new MinHeap();
        foreach ($nums as $x) $pq->push($x);
        $ans = 0;
        while ($pq->size() > 1 && $pq->peek() < $k) {
            $x = $pq->pop();
            $y = $pq->pop();
            $pq->push($x * 2 + $y);
            $ans++;
        }
        return $ans;
    }
}
''')

add("3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network", r'''<?php
// LeetCode 3067 - Count Pairs of Connectable Servers in a Weighted Tree Network
// https://leetcode.com/problems/count-pairs-of-connectable-servers-in-a-weighted-tree-network/

class Solution {
    public $g;
    public $signalSpeed;
    function countPairsOfConnectableServers($edges, $signalSpeed) {
        $n = count($edges) + 1;
        $this->signalSpeed = $signalSpeed;
        $this->g = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $this->g[$e[0]][] = [$e[1], $e[2]];
            $this->g[$e[1]][] = [$e[0], $e[2]];
        }
        $ans = array_fill(0, $n, 0);
        for ($a = 0; $a < $n; $a++) {
            $s = 0;
            foreach ($this->g[$a] as $e) {
                $t = $this->dfs($e[0], $a, $e[1]);
                $ans[$a] += $s * $t;
                $s += $t;
            }
        }
        return $ans;
    }
    function dfs($a, $fa, $ws) {
        $cnt = $ws % $this->signalSpeed === 0 ? 1 : 0;
        foreach ($this->g[$a] as $e) {
            if ($e[0] !== $fa) $cnt += $this->dfs($e[0], $a, $ws + $e[1]);
        }
        return $cnt;
    }
}
''')

add("3068_find_the_maximum_sum_of_node_values", r'''<?php
// LeetCode 3068 - Find the Maximum Sum of Node Values
// https://leetcode.com/problems/find-the-maximum-sum-of-node-values/

class Solution {
    function maximumValueSum($nums, $k, $edges) {
        $f0 = 0;
        $f1 = PHP_INT_MIN;
        foreach ($nums as $x) {
            $nf0 = max($f0 + $x, $f1 + ($x ^ $k));
            $nf1 = max($f1 + $x, $f0 + ($x ^ $k));
            $f0 = $nf0;
            $f1 = $nf1;
        }
        return $f0;
    }
}
''')

add("3069_distribute_elements_into_two_arrays_i", r'''<?php
// LeetCode 3069 - Distribute Elements Into Two Arrays I
// https://leetcode.com/problems/distribute-elements-into-two-arrays-i/

class Solution {
    function resultArray($nums) {
        $arr1 = [$nums[0]];
        $arr2 = [$nums[1]];
        $n = count($nums);
        for ($i = 2; $i < $n; $i++) {
            if ($arr1[count($arr1) - 1] > $arr2[count($arr2) - 1]) $arr1[] = $nums[$i];
            else $arr2[] = $nums[$i];
        }
        return array_merge($arr1, $arr2);
    }
}
''')

add("3070_count_submatrices_with_top_left_element_and_sum_less_than_k", r'''<?php
// LeetCode 3070 - Count Submatrices With Top-Left Element and Sum Less Than k
// https://leetcode.com/problems/count-submatrices-with-top-left-element-and-sum-less-than-k/

class Solution {
    function countSubmatrices($grid, $k) {
        $n = count($grid);
        $m = count($grid[0]);
        $ans = 0;
        $s = [];
        for ($i = 0; $i <= $n; $i++) $s[] = array_fill(0, $m + 1, 0);
        for ($i = 0; $i < $n; $i++) {
            for ($j = 0; $j < $m; $j++) {
                $s[$i + 1][$j + 1] = $s[$i + 1][$j] + $s[$i][$j + 1] - $s[$i][$j] + $grid[$i][$j];
                if ($s[$i + 1][$j + 1] <= $k) $ans++;
            }
        }
        return $ans;
    }
}
''')

add("3071_minimum_operations_to_write_the_letter_y_on_a_grid", r'''<?php
// LeetCode 3071 - Minimum Operations to Write the Letter Y on a Grid
// https://leetcode.com/problems/minimum-operations-to-write-the-letter-y-on-a-grid/

class Solution {
    function minimumOperationsToWriteY($grid) {
        $n = count($grid);
        $cnt1 = [0, 0, 0];
        $cnt2 = [0, 0, 0];
        $half = intdiv($n, 2);
        for ($i = 0; $i < $n; $i++) {
            for ($j = 0; $j < $n; $j++) {
                $x = $grid[$i][$j];
                $a = $i === $j && $i <= $half;
                $b = $i + $j === $n - 1 && $i <= $half;
                $c = $j === $half && $i >= $half;
                if ($a || $b || $c) $cnt1[$x]++;
                else $cnt2[$x]++;
            }
        }
        $ans = $n * $n;
        for ($i = 0; $i < 3; $i++) {
            for ($j = 0; $j < 3; $j++) {
                if ($i !== $j) $ans = min($ans, $n * $n - $cnt1[$i] - $cnt2[$j]);
            }
        }
        return $ans;
    }
}
''')

add("3072_distribute_elements_into_two_arrays_ii", '''<?php
// LeetCode 3072 - Distribute Elements Into Two Arrays II
// https://leetcode.com/problems/distribute-elements-into-two-arrays-ii/
''' + BIT + r'''
class Solution {
    public $st;
    function resultArray($nums) {
        $this->st = $nums;
        sort($this->st);
        $n = count($this->st);
        $tree1 = new BIT($n + 1);
        $tree2 = new BIT($n + 1);
        $arr1 = [$nums[0]];
        $arr2 = [$nums[1]];
        $tree1->update($this->idx($nums[0]), 1);
        $tree2->update($this->idx($nums[1]), 1);
        $len = count($nums);
        for ($i = 2; $i < $len; $i++) {
            $x = $nums[$i];
            $id = $this->idx($x);
            $a = count($arr1) - $tree1->query($id);
            $b = count($arr2) - $tree2->query($id);
            if ($a > $b || ($a === $b && count($arr1) <= count($arr2))) {
                $arr1[] = $x;
                $tree1->update($id, 1);
            } else {
                $arr2[] = $x;
                $tree2->update($id, 1);
            }
        }
        return array_merge($arr1, $arr2);
    }
    function idx($x) {
        $lo = 0;
        $hi = count($this->st);
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi, 2);
            if ($this->st[$mid] < $x) $lo = $mid + 1;
            else $hi = $mid;
        }
        return $lo + 1;
    }
}
''')

add("3073_maximum_increasing_triplet_value", r'''<?php
// LeetCode 3073 - Maximum Increasing Triplet Value
// https://leetcode.com/problems/maximum-increasing-triplet-value/

class Solution {
    public $ts = [];
    function maximumTripletValue($nums) {
        $n = count($nums);
        $right = array_fill(0, $n, 0);
        $right[$n - 1] = $nums[$n - 1];
        for ($i = $n - 2; $i >= 0; $i--) $right[$i] = max($nums[$i], $right[$i + 1]);
        $this->ts = [];
        $this->add($nums[0]);
        $ans = 0;
        for ($j = 1; $j < $n - 1; $j++) {
            if ($right[$j + 1] > $nums[$j]) {
                $it = $this->lower($nums[$j]);
                if ($it !== null) $ans = max($ans, $it - $nums[$j] + $right[$j + 1]);
            }
            $this->add($nums[$j]);
        }
        return $ans;
    }
    function add($x) {
        $ts = &$this->ts;
        $lo = 0;
        $hi = count($ts);
        while ($lo < $hi) {
            $mid = ($lo + $hi) >> 1;
            if ($ts[$mid] < $x) $lo = $mid + 1;
            else $hi = $mid;
        }
        if ($lo === count($ts) || $ts[$lo] !== $x) array_splice($ts, $lo, 0, [$x]);
    }
    function lower($x) {
        $ts = $this->ts;
        $lo = 0;
        $hi = count($ts);
        while ($lo < $hi) {
            $mid = ($lo + $hi) >> 1;
            if ($ts[$mid] < $x) $lo = $mid + 1;
            else $hi = $mid;
        }
        return $lo > 0 ? $ts[$lo - 1] : null;
    }
}
''')

add("3074_apple_redistribution_into_boxes", r'''<?php
// LeetCode 3074 - Apple Redistribution into Boxes
// https://leetcode.com/problems/apple-redistribution-into-boxes/

class Solution {
    function minimumBoxes($apple, $capacity) {
        sort($capacity);
        $s = 0;
        foreach ($apple as $x) $s += $x;
        for ($i = 1; ; $i++) {
            $s -= $capacity[count($capacity) - $i];
            if ($s <= 0) return $i;
        }
    }
}
''')

add("3075_maximize_happiness_of_selected_children", r'''<?php
// LeetCode 3075 - Maximize Happiness of Selected Children
// https://leetcode.com/problems/maximize-happiness-of-selected-children/

class Solution {
    function maximumHappinessSum($happiness, $k) {
        sort($happiness);
        $ans = 0;
        $n = count($happiness);
        for ($i = 0; $i < $k; $i++) {
            $x = $happiness[$n - $i - 1] - $i;
            $ans += max($x, 0);
        }
        return $ans;
    }
}
''')

add("3076_shortest_uncommon_substring_in_an_array", r'''<?php
// LeetCode 3076 - Shortest Uncommon Substring in an Array
// https://leetcode.com/problems/shortest-uncommon-substring-in-an-array/

class Solution {
    function shortestSubstrings($arr) {
        $n = count($arr);
        $ans = array_fill(0, $n, "");
        for ($i = 0; $i < $n; $i++) {
            $s = $arr[$i];
            $m = strlen($s);
            for ($j = 1; $j <= $m && $ans[$i] === ""; $j++) {
                for ($l = 0; $l <= $m - $j; $l++) {
                    $sub = substr($s, $l, $j);
                    if ($ans[$i] === "" || $ans[$i] > $sub) {
                        $ok = true;
                        for ($k = 0; $k < $n; $k++) {
                            if ($k !== $i && str_contains($arr[$k], $sub)) { $ok = false; break; }
                        }
                        if ($ok) $ans[$i] = $sub;
                    }
                }
            }
        }
        return $ans;
    }
}
''')

add("3077_maximum_strength_of_k_disjoint_subarrays", r'''<?php
// LeetCode 3077 - Maximum Strength of K Disjoint Subarrays
// https://leetcode.com/problems/maximum-strength-of-k-disjoint-subarrays/

class Solution {
    function maximumStrength($nums, $k) {
        $n = count($nums);
        $INF = -4000000000000000000;
        $f = [];
        for ($i = 0; $i <= $n; $i++) {
            $f[$i] = [];
            for ($j = 0; $j <= $k; $j++) $f[$i][$j] = [$INF, $INF];
        }
        $f[0][0][0] = 0;
        for ($i = 1; $i <= $n; $i++) {
            $x = $nums[$i - 1];
            for ($j = 0; $j <= $k; $j++) {
                $sign = ($j & 1) !== 0 ? 1 : -1;
                $val = $sign * $x * ($k - $j + 1);
                $f[$i][$j][0] = max($f[$i - 1][$j][0], $f[$i - 1][$j][1]);
                $f[$i][$j][1] = max($f[$i][$j][1], $f[$i - 1][$j][1] + $val);
                if ($j > 0) {
                    $t = max($f[$i - 1][$j - 1][0], $f[$i - 1][$j - 1][1]) + $val;
                    $f[$i][$j][1] = max($f[$i][$j][1], $t);
                }
            }
        }
        return max($f[$n][$k][0], $f[$n][$k][1]);
    }
}
''')

add("3078_match_alphanumerical_pattern_in_matrix_i", r'''<?php
// LeetCode 3078 - Match Alphanumerical Pattern in Matrix I
// https://leetcode.com/problems/match-alphanumerical-pattern-in-matrix-i/

class Solution {
    public $board;
    public $pattern;
    public $r;
    public $c;
    function findPattern($board, $pattern) {
        $this->board = $board;
        $this->pattern = $pattern;
        $m = count($board);
        $n = count($board[0]);
        $this->r = count($pattern);
        $this->c = strlen($pattern[0]);
        for ($i = 0; $i < $m - $this->r + 1; $i++) {
            for ($j = 0; $j < $n - $this->c + 1; $j++) {
                if ($this->check($i, $j)) return [$i, $j];
            }
        }
        return [-1, -1];
    }
    function check($i, $j) {
        $d1 = array_fill(0, 26, 0);
        $d2 = array_fill(0, 10, 0);
        for ($a = 0; $a < $this->r; $a++) {
            for ($b = 0; $b < $this->c; $b++) {
                $x = $i + $a;
                $y = $j + $b;
                $ch = $this->pattern[$a][$b];
                if ($ch >= "0" && $ch <= "9") {
                    if (ord($ch) - 48 !== $this->board[$x][$y]) return false;
                } else {
                    $v = ord($ch) - 97;
                    if ($d1[$v] > 0 && $d1[$v] - 1 !== $this->board[$x][$y]) return false;
                    if ($d2[$this->board[$x][$y]] > 0 && $d2[$this->board[$x][$y]] - 1 !== $v) return false;
                    $d1[$v] = $this->board[$x][$y] + 1;
                    $d2[$this->board[$x][$y]] = $v + 1;
                }
            }
        }
        return true;
    }
}
''')

add("3079_find_the_sum_of_encrypted_integers", r'''<?php
// LeetCode 3079 - Find the Sum of Encrypted Integers
// https://leetcode.com/problems/find-the-sum-of-encrypted-integers/

class Solution {
    function sumOfEncryptedInt($nums) {
        $ans = 0;
        foreach ($nums as $x) $ans += $this->encrypt($x);
        return $ans;
    }
    function encrypt($x) {
        $mx = 0;
        $p = 0;
        for (; $x > 0; $x = intdiv($x, 10)) {
            $mx = max($mx, $x % 10);
            $p = $p * 10 + 1;
        }
        return $mx * $p;
    }
}
''')

add("3080_mark_elements_on_array_by_performing_queries", r'''<?php
// LeetCode 3080 - Mark Elements on Array by Performing Queries
// https://leetcode.com/problems/mark-elements-on-array-by-performing-queries/

class Solution {
    function unmarkedSumArray($nums, $queries) {
        $n = count($nums);
        $s = 0;
        foreach ($nums as $x) $s += $x;
        $mark = array_fill(0, $n, false);
        $arr = [];
        for ($i = 0; $i < $n; $i++) $arr[] = [$nums[$i], $i];
        usort($arr, function ($a, $b) {
            return $a[0] !== $b[0] ? $a[0] <=> $b[0] : $a[1] <=> $b[1];
        });
        $ans = array_fill(0, count($queries), 0);
        $j = 0;
        for ($qi = 0; $qi < count($queries); $qi++) {
            $index = $queries[$qi][0];
            $k = $queries[$qi][1];
            if (!$mark[$index]) {
                $mark[$index] = true;
                $s -= $nums[$index];
            }
            for (; $k > 0 && $j < $n; $j++) {
                if (!$mark[$arr[$j][1]]) {
                    $mark[$arr[$j][1]] = true;
                    $s -= $arr[$j][0];
                    $k--;
                }
            }
            $ans[$qi] = $s;
        }
        return $ans;
    }
}
''')

add("3081_replace_question_marks_in_string_to_minimize_its_value", '''<?php
// LeetCode 3081 - Replace Question Marks in String to Minimize Its Value
// https://leetcode.com/problems/replace-question-marks-in-string-to-minimize-its-value/
''' + MINHEAP + r'''
class Solution {
    function minimizeStringValue($s) {
        $cnt = array_fill(0, 26, 0);
        $k = 0;
        $len = strlen($s);
        for ($i = 0; $i < $len; $i++) {
            $c = $s[$i];
            if ($c === "?") $k++;
            else $cnt[ord($c) - 97]++;
        }
        $pq = new MinHeap(function ($a, $b) {
            return $a[0] !== $b[0] ? $a[0] <=> $b[0] : $a[1] <=> $b[1];
        });
        for ($i = 0; $i < 26; $i++) $pq->push([$cnt[$i], $i]);
        $t = array_fill(0, $k, 0);
        for ($i = 0; $i < $k; $i++) {
            $p = $pq->pop();
            $t[$i] = $p[1];
            $p[0]++;
            $pq->push($p);
        }
        sort($t);
        $arr = str_split($s);
        $j = 0;
        for ($i = 0; $i < count($arr); $i++) {
            if ($arr[$i] === "?") {
                $arr[$i] = chr($t[$j] + 97);
                $j++;
            }
        }
        return implode("", $arr);
    }
}
''')

add("3082_find_the_sum_of_the_power_of_all_subsequences", r'''<?php
// LeetCode 3082 - Find the Sum of the Power of All Subsequences
// https://leetcode.com/problems/find-the-sum-of-the-power-of-all-subsequences/

class Solution {
    function sumOfPower($nums, $k) {
        $MOD = 1000000007;
        $n = count($nums);
        $f = [];
        for ($i = 0; $i <= $n; $i++) $f[] = array_fill(0, $k + 1, 0);
        $f[0][0] = 1;
        for ($i = 1; $i <= $n; $i++) {
            for ($j = 0; $j <= $k; $j++) {
                $f[$i][$j] = ($f[$i - 1][$j] * 2) % $MOD;
                if ($j >= $nums[$i - 1])
                    $f[$i][$j] = ($f[$i][$j] + $f[$i - 1][$j - $nums[$i - 1]]) % $MOD;
            }
        }
        return $f[$n][$k];
    }
}
''')

add("3083_existence_of_a_substring_in_a_string_and_its_reverse", r'''<?php
// LeetCode 3083 - Existence of a Substring in a String and Its Reverse
// https://leetcode.com/problems/existence-of-a-substring-in-a-string-and-its-reverse/

class Solution {
    function isSubstringPresent($s) {
        $st = [];
        for ($i = 0; $i < 26; $i++) $st[] = array_fill(0, 26, false);
        $n = strlen($s);
        for ($i = 0; $i + 1 < $n; $i++)
            $st[ord($s[$i + 1]) - 97][ord($s[$i]) - 97] = true;
        for ($i = 0; $i + 1 < $n; $i++)
            if ($st[ord($s[$i]) - 97][ord($s[$i + 1]) - 97]) return true;
        return false;
    }
}
''')

add("3084_count_substrings_starting_and_ending_with_given_character", r'''<?php
// LeetCode 3084 - Count Substrings Starting and Ending with Given Character
// https://leetcode.com/problems/count-substrings-starting-and-ending-with-given-character/

class Solution {
    function countSubstrings($s, $c) {
        $cnt = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) if ($s[$i] === $c) $cnt++;
        return intdiv($cnt * ($cnt + 1), 2);
    }
}
''')

add("3085_minimum_deletions_to_make_string_k_special", r'''<?php
// LeetCode 3085 - Minimum Deletions to Make String K-Special
// https://leetcode.com/problems/minimum-deletions-to-make-string-k-special/

class Solution {
    function minimumDeletions($word, $k) {
        $freq = array_fill(0, 26, 0);
        $n = strlen($word);
        for ($i = 0; $i < $n; $i++) $freq[ord($word[$i]) - 97]++;
        $nums = [];
        foreach ($freq as $v) if ($v > 0) $nums[] = $v;
        $ans = $n;
        for ($i = 0; $i <= $n; $i++) {
            $cur = 0;
            foreach ($nums as $x) {
                if ($x < $i) $cur += $x;
                else if ($x > $i + $k) $cur += $x - $i - $k;
            }
            $ans = min($ans, $cur);
        }
        return $ans;
    }
}
''')

add("3086_minimum_moves_to_pick_k_ones", r'''<?php
// LeetCode 3086 - Minimum Moves to Pick K Ones
// https://leetcode.com/problems/minimum-moves-to-pick-k-ones/

class Solution {
    function minimumMoves($nums, $k, $maxChanges) {
        $n = count($nums);
        $cnt = array_fill(0, $n + 1, 0);
        $s = array_fill(0, $n + 1, 0);
        for ($i = 1; $i <= $n; $i++) {
            $cnt[$i] = $cnt[$i - 1] + $nums[$i - 1];
            $s[$i] = $s[$i - 1] + $i * $nums[$i - 1];
        }
        $ans = PHP_INT_MAX;
        for ($i = 1; $i <= $n; $i++) {
            $t = 0;
            $need = $k - $nums[$i - 1];
            foreach ([$i - 1, $i + 1] as $j) {
                if ($need > 0 && 1 <= $j && $j <= $n && $nums[$j - 1] === 1) {
                    $need--;
                    $t++;
                }
            }
            $c = min($need, $maxChanges);
            $need -= $c;
            $t += $c * 2;
            if ($need <= 0) {
                $ans = min($ans, $t);
                continue;
            }
            $l = 2;
            $r = max($i - 1, $n - $i);
            while ($l <= $r) {
                $mid = ($l + $r) >> 1;
                $l1 = max(1, $i - $mid);
                $r1 = max(0, $i - 2);
                $l2 = min($n + 1, $i + 2);
                $r2 = min($n, $i + $mid);
                $c1 = $cnt[$r1] - $cnt[$l1 - 1];
                $c2 = $cnt[$r2] - $cnt[$l2 - 1];
                if ($c1 + $c2 >= $need) {
                    $t1 = $c1 * $i - ($s[$r1] - $s[$l1 - 1]);
                    $t2 = $s[$r2] - $s[$l2 - 1] - $c2 * $i;
                    $ans = min($ans, $t + $t1 + $t2);
                    $r = $mid - 1;
                } else {
                    $l = $mid + 1;
                }
            }
        }
        return $ans;
    }
}
''')

if __name__ == "__main__":
    n = 0
    for folder, body in SOLUTIONS.items():
        p = ROOT / folder / "solution.php"
        p.write_text(body, encoding="utf-8")
        n += 1
        print("wrote", folder)
    print("written", n)

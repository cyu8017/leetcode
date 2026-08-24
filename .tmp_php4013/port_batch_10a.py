#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
SOLUTIONS = {}


def add(folder, body):
    SOLUTIONS[folder] = body if body.endswith("\n") else body + "\n"


TREE = r"""class TreeNode {
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

LISTN = r"""class ListNode {
    public $val = 0;
    public $next = null;
    function __construct($val = 0, $next = null) {
        $this->val = $val;
        $this->next = $next;
    }
}
"""

add("2620_counter", r'''<?php
// LeetCode 2620 - Counter
// https://leetcode.com/problems/counter/

class Solution {
    function createCounter($n) {
        return function() use (&$n) {
            return $n++;
        };
    }
}
''')

add("2621_sleep", r'''<?php
// LeetCode 2621 - Sleep
// https://leetcode.com/problems/sleep/

class Solution {
    function sleep($millis) {
        usleep((int)($millis * 1000));
        return null;
    }
}
''')

add("2622_cache_with_time_limit", r'''<?php
// LeetCode 2622 - Cache With Time Limit
// https://leetcode.com/problems/cache-with-time-limit/

class TimeLimitedCache {
    private $data = [];

    function set($key, $value, $duration) {
        $now = (int)round(microtime(true) * 1000);
        $alive = isset($this->data[$key]) && $this->data[$key]['expire'] > $now;
        $this->data[$key] = ['value' => $value, 'expire' => $now + $duration];
        return $alive;
    }

    function get($key) {
        $now = (int)round(microtime(true) * 1000);
        if (!isset($this->data[$key]) || $this->data[$key]['expire'] <= $now) return -1;
        return $this->data[$key]['value'];
    }

    function count() {
        $now = (int)round(microtime(true) * 1000);
        $cnt = 0;
        foreach ($this->data as $k => $e) {
            if ($e['expire'] > $now) $cnt++;
            else unset($this->data[$k]);
        }
        return $cnt;
    }
}

class Solution {
    function TimeLimitedCache() {
        return new TimeLimitedCache();
    }
}
''')

add("2623_memoize", r'''<?php
// LeetCode 2623 - Memoize
// https://leetcode.com/problems/memoize/

class Solution {
    function memoize($fn) {
        $cache = [];
        return function($x) use ($fn, &$cache) {
            $k = is_scalar($x) ? (string)$x : serialize($x);
            if (array_key_exists($k, $cache)) return $cache[$k];
            $r = $fn($x);
            $cache[$k] = $r;
            return $r;
        };
    }
}
''')

add("2624_snail_traversal", r'''<?php
// LeetCode 2624 - Snail Traversal
// https://leetcode.com/problems/snail-traversal/

class Solution {
    function snail($arr, $rowsCount, $colsCount) {
        if ($rowsCount * $colsCount !== count($arr)) return [];
        $ans = [];
        for ($r = 0; $r < $rowsCount; $r++) $ans[$r] = array_fill(0, $colsCount, 0);
        $idx = 0;
        for ($c = 0; $c < $colsCount; $c++) {
            if ($c % 2 === 0) {
                for ($r = 0; $r < $rowsCount; $r++) $ans[$r][$c] = $arr[$idx++];
            } else {
                for ($r = $rowsCount - 1; $r >= 0; $r--) $ans[$r][$c] = $arr[$idx++];
            }
        }
        return $ans;
    }
}
''')

add("2625_flatten_deeply_nested_array", r'''<?php
// LeetCode 2625 - Flatten Deeply Nested Array
// https://leetcode.com/problems/flatten-deeply-nested-array/

class Solution {
    function flat($arr, $n) {
        $res = [];
        $dfs = function($a, $depth) use (&$dfs, &$res, $n) {
            foreach ($a as $x) {
                if (is_array($x) && $depth < $n) $dfs($x, $depth + 1);
                else $res[] = $x;
            }
        };
        $dfs($arr, 0);
        return $res;
    }
}
''')

add("2626_array_reduce_transformation", r'''<?php
// LeetCode 2626 - Array Reduce Transformation
// https://leetcode.com/problems/array-reduce-transformation/

class Solution {
    function reduce($nums, $fn, $init) {
        $acc = $init;
        foreach ($nums as $x) $acc = $fn($acc, $x);
        return $acc;
    }
}
''')

add("2627_debounce", r'''<?php
// LeetCode 2627 - Debounce
// https://leetcode.com/problems/debounce/

class Solution {
    function debounce($fn, $t) {
        $timer = null;
        return function(...$args) use ($fn, $t, &$timer) {
            $timer = ['args' => $args, 't' => $t];
            return $fn(...$args);
        };
    }
}
''')

add("2628_json_deep_equal", r'''<?php
// LeetCode 2628 - JSON Deep Equal
// https://leetcode.com/problems/json-deep-equal/

class Solution {
    function areDeeplyEqual($o1, $o2) {
        if ($o1 === $o2) return true;
        if (gettype($o1) !== gettype($o2)) return false;
        if ($o1 === null || $o2 === null) return false;
        if (!is_array($o1)) return false;
        $a1 = array_is_list($o1);
        $a2 = array_is_list($o2);
        if ($a1 !== $a2) return false;
        if ($a1) {
            if (count($o1) !== count($o2)) return false;
            for ($i = 0; $i < count($o1); $i++) {
                if (!$this->areDeeplyEqual($o1[$i], $o2[$i])) return false;
            }
            return true;
        }
        $k1 = array_keys($o1);
        $k2 = array_keys($o2);
        if (count($k1) !== count($k2)) return false;
        foreach ($k1 as $k) {
            if (!array_key_exists($k, $o2) || !$this->areDeeplyEqual($o1[$k], $o2[$k])) return false;
        }
        return true;
    }
}
''')

add("2629_function_composition", r'''<?php
// LeetCode 2629 - Function Composition
// https://leetcode.com/problems/function-composition/

class Solution {
    function compose($functions) {
        return function($x) use ($functions) {
            for ($i = count($functions) - 1; $i >= 0; $i--) $x = $functions[$i]($x);
            return $x;
        };
    }
}
''')

add("2630_memoize_ii", r'''<?php
// LeetCode 2630 - Memoize II
// https://leetcode.com/problems/memoize-ii/

class Solution {
    function memoize($fn) {
        $root = [];
        $RES = '__res__';
        return function(...$args) use ($fn, &$root, $RES) {
            $node =& $root;
            foreach ($args as $a) {
                $k = is_scalar($a) ? gettype($a) . ':' . (string)$a : serialize($a);
                if (!isset($node[$k]) || !is_array($node[$k])) $node[$k] = [];
                $node =& $node[$k];
            }
            if (array_key_exists($RES, $node)) return $node[$RES];
            $v = $fn(...$args);
            $node[$RES] = $v;
            return $v;
        };
    }
}
''')

add("2631_group_by", r'''<?php
// LeetCode 2631 - Group By
// https://leetcode.com/problems/group-by/

class Solution {
    function groupBy($array, $fn) {
        $out = [];
        foreach ($array as $x) {
            $k = $fn($x);
            if (!isset($out[$k])) $out[$k] = [];
            $out[$k][] = $x;
        }
        return $out;
    }
}
''')

add("2632_curry", r'''<?php
// LeetCode 2632 - Curry
// https://leetcode.com/problems/curry/

class Solution {
    function curry($fn) {
        $arity = (new ReflectionFunction($fn instanceof Closure ? $fn : Closure::fromCallable($fn)))->getNumberOfParameters();
        $curried = null;
        $curried = function(...$args) use ($fn, $arity, &$curried) {
            if (count($args) >= $arity) return $fn(...$args);
            return function(...$next) use ($curried, $args) {
                return $curried(...array_merge($args, $next));
            };
        };
        return $curried;
    }
}
''')

add("2633_convert_object_to_json_string", r'''<?php
// LeetCode 2633 - Convert Object to JSON String
// https://leetcode.com/problems/convert-object-to-json-string/

class Solution {
    function jsonStringify($object) {
        if ($object === null) return "null";
        if (is_string($object)) return '"' . $object . '"';
        if (is_int($object) || is_float($object) || is_bool($object)) {
            if (is_bool($object)) return $object ? "true" : "false";
            return (string)$object;
        }
        if (is_array($object) && array_is_list($object)) {
            $parts = [];
            foreach ($object as $x) $parts[] = $this->jsonStringify($x);
            return "[" . implode(",", $parts) . "]";
        }
        $parts = [];
        foreach ($object as $k => $v) {
            $parts[] = '"' . $k . '":' . $this->jsonStringify($v);
        }
        return "{" . implode(",", $parts) . "}";
    }
}
''')

add("2634_filter_elements_from_array", r'''<?php
// LeetCode 2634 - Filter Elements from Array
// https://leetcode.com/problems/filter-elements-from-array/

class Solution {
    function filter($arr, $fn) {
        $out = [];
        for ($i = 0; $i < count($arr); $i++) {
            if ($fn($arr[$i], $i)) $out[] = $arr[$i];
        }
        return $out;
    }
}
''')

add("2635_apply_transform_over_each_element_in_array", r'''<?php
// LeetCode 2635 - Apply Transform Over Each Element in Array
// https://leetcode.com/problems/apply-transform-over-each-element-in-array/

class Solution {
    function map($arr, $fn) {
        $out = [];
        for ($i = 0; $i < count($arr); $i++) $out[$i] = $fn($arr[$i], $i);
        return $out;
    }
}
''')

add("2636_promise_pool", r'''<?php
// LeetCode 2636 - Promise Pool
// https://leetcode.com/problems/promise-pool/

class Solution {
    function promisePool($functions, $n) {
        $i = 0;
        $len = count($functions);
        $worker = function() use (&$i, $functions, $len) {
            while ($i < $len) {
                $cur = $i++;
                $functions[$cur]();
            }
        };
        $limit = min($n, $len);
        for ($k = 0; $k < $limit; $k++) $worker();
        return null;
    }
}
''')

add("2637_promise_time_limit", r'''<?php
// LeetCode 2637 - Promise Time Limit
// https://leetcode.com/problems/promise-time-limit/

class Solution {
    function timeLimit($fn, $t) {
        return function(...$args) use ($fn, $t) {
            $start = microtime(true);
            $res = $fn(...$args);
            if ((microtime(true) - $start) * 1000 > $t) {
                throw new Exception("Time Limit Exceeded");
            }
            return $res;
        };
    }
}
''')

add("2638_count_the_number_of_k_free_subsets", r'''<?php
// LeetCode 2638 - Count the Number of K-Free Subsets
// https://leetcode.com/problems/count-the-number-of-k-free-subsets/

class Solution {
    function countTheNumOfKFreeSubsets($nums, $k) {
        sort($nums);
        $groups = [];
        foreach ($nums as $x) {
            $key = $x % $k;
            if (!isset($groups[$key])) $groups[$key] = [];
            $groups[$key][] = $x;
        }
        $ans = 1;
        foreach ($groups as $g) {
            $prevVal = -1;
            $prevTake = 0;
            $prevSkip = 1;
            foreach ($g as $v) {
                $skip = $prevTake + $prevSkip;
                $take = ($prevVal + $k === $v) ? $prevSkip : ($prevTake + $prevSkip);
                $prevTake = $take;
                $prevSkip = $skip;
                $prevVal = $v;
            }
            $ans *= $prevTake + $prevSkip;
        }
        return $ans;
    }
}
''')

add("2639_find_the_width_of_columns_of_a_grid", r'''<?php
// LeetCode 2639 - Find the Width of Columns of a Grid
// https://leetcode.com/problems/find-the-width-of-columns-of-a-grid/

class Solution {
    function findColumnWidth($grid) {
        $n = count($grid[0]);
        $ans = array_fill(0, $n, 0);
        $width = function($x) {
            if ($x === 0) return 1;
            $w = 0;
            if ($x < 0) { $w++; $x = -$x; }
            while ($x > 0) { $w++; $x = intdiv($x, 10); }
            return $w;
        };
        foreach ($grid as $row) {
            for ($j = 0; $j < $n; $j++) $ans[$j] = max($ans[$j], $width($row[$j]));
        }
        return $ans;
    }
}
''')

add("2640_find_the_score_of_all_prefixes_of_an_array", r'''<?php
// LeetCode 2640 - Find the Score of All Prefixes of an Array
// https://leetcode.com/problems/find-the-score-of-all-prefixes-of-an-array/

class Solution {
    function findPrefixScore($nums) {
        $ans = [];
        $mx = 0;
        $sum = 0;
        for ($i = 0; $i < count($nums); $i++) {
            if ($nums[$i] > $mx) $mx = $nums[$i];
            $sum += $nums[$i] + $mx;
            $ans[$i] = $sum;
        }
        return $ans;
    }
}
''')

add("2641_cousins_in_binary_tree_ii", r'''<?php
// LeetCode 2641 - Cousins in Binary Tree II
// https://leetcode.com/problems/cousins-in-binary-tree-ii/

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
    function replaceValueInTree($root) {
        if ($root === null) return null;
        $root->val = 0;
        $q = [$root];
        while (count($q) > 0) {
            $sz = count($q);
            $levelSum = 0;
            $level = [];
            for ($i = 0; $i < $sz; $i++) {
                $node = array_shift($q);
                $level[] = $node;
                if ($node->left) $levelSum += $node->left->val;
                if ($node->right) $levelSum += $node->right->val;
            }
            foreach ($level as $node) {
                $cousin = $levelSum;
                if ($node->left) $cousin -= $node->left->val;
                if ($node->right) $cousin -= $node->right->val;
                if ($node->left) { $node->left->val = $cousin; $q[] = $node->left; }
                if ($node->right) { $node->right->val = $cousin; $q[] = $node->right; }
            }
        }
        return $root;
    }
}
''')

add("2642_design_graph_with_shortest_path_calculator", r'''<?php
// LeetCode 2642 - Design Graph With Shortest Path Calculator
// https://leetcode.com/problems/design-graph-with-shortest-path-calculator/

class Graph {
    private $g;

    function __construct($n, $edges) {
        $this->g = array_fill(0, $n, []);
        foreach ($edges as $e) $this->g[$e[0]][] = [$e[1], $e[2]];
    }

    function addEdge($edge) {
        $this->g[$edge[0]][] = [$edge[1], $edge[2]];
    }

    function shortestPath($node1, $node2) {
        $n = count($this->g);
        $dist = array_fill(0, $n, 1 << 30);
        $dist[$node1] = 0;
        $pq = new SplPriorityQueue();
        $pq->insert([$node1, 0], 0);
        while (!$pq->isEmpty()) {
            $cur = $pq->extract();
            $u = $cur[0];
            $d = $cur[1];
            if ($u === $node2) return $d;
            if ($d > $dist[$u]) continue;
            foreach ($this->g[$u] as $e) {
                $v = $e[0];
                $w = $e[1];
                $nd = $d + $w;
                if ($nd < $dist[$v]) {
                    $dist[$v] = $nd;
                    $pq->insert([$v, $nd], -$nd);
                }
            }
        }
        return -1;
    }
}
''')

add("2643_row_with_maximum_ones", r'''<?php
// LeetCode 2643 - Row With Maximum Ones
// https://leetcode.com/problems/row-with-maximum-ones/

class Solution {
    function rowAndMaximumOnes($mat) {
        $bestRow = 0;
        $bestCnt = -1;
        for ($i = 0; $i < count($mat); $i++) {
            $cnt = 0;
            foreach ($mat[$i] as $v) $cnt += $v;
            if ($cnt > $bestCnt) { $bestCnt = $cnt; $bestRow = $i; }
        }
        return [$bestRow, $bestCnt];
    }
}
''')

add("2644_find_the_maximum_divisibility_score", r'''<?php
// LeetCode 2644 - Find the Maximum Divisibility Score
// https://leetcode.com/problems/find-the-maximum-divisibility-score/

class Solution {
    function maxDivScore($nums, $divisors) {
        $best = $divisors[0];
        $bestScore = -1;
        foreach ($divisors as $d) {
            $score = 0;
            foreach ($nums as $x) if ($x % $d === 0) $score++;
            if ($score > $bestScore || ($score === $bestScore && $d < $best)) {
                $bestScore = $score;
                $best = $d;
            }
        }
        return $best;
    }
}
''')

add("2645_minimum_additions_to_make_valid_string", r'''<?php
// LeetCode 2645 - Minimum Additions to Make Valid String
// https://leetcode.com/problems/minimum-additions-to-make-valid-string/

class Solution {
    function addMinimum($word) {
        $ans = 0;
        $expect = 0;
        $i = 0;
        $n = strlen($word);
        while ($i < $n) {
            $need = chr(97 + $expect);
            if ($word[$i] === $need) $i++;
            else $ans++;
            $expect = ($expect + 1) % 3;
        }
        $ans += (3 - $expect) % 3;
        return $ans;
    }
}
''')

add("2646_minimize_the_total_price_of_the_trips", r'''<?php
// LeetCode 2646 - Minimize the Total Price of the Trips
// https://leetcode.com/problems/minimize-the-total-price-of-the-trips/

class Solution {
    function minimumTotalPrice($n, $edges, $price, $trips) {
        $g = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $g[$e[0]][] = $e[1];
            $g[$e[1]][] = $e[0];
        }
        $cnt = array_fill(0, $n, 0);
        $path = function($u, $p, $target) use (&$path, &$g, &$cnt) {
            if ($u === $target) { $cnt[$u]++; return true; }
            foreach ($g[$u] as $v) {
                if ($v === $p) continue;
                if ($path($v, $u, $target)) { $cnt[$u]++; return true; }
            }
            return false;
        };
        foreach ($trips as $t) $path($t[0], -1, $t[1]);
        $dfs = function($u, $p) use (&$dfs, &$g, &$price, &$cnt) {
            $full = $price[$u] * $cnt[$u];
            $half = intdiv($full, 2);
            foreach ($g[$u] as $v) {
                if ($v === $p) continue;
                $child = $dfs($v, $u);
                $full += min($child[0], $child[1]);
                $half += $child[0];
            }
            return [$full, $half];
        };
        $res = $dfs(0, -1);
        return min($res[0], $res[1]);
    }
}
''')

add("2647_color_the_triangle_red", r'''<?php
// LeetCode 2647 - Color the Triangle Red
// https://leetcode.com/problems/color-the-triangle-red/

class Solution {
    function colorRed($n) {
        $ans = [];
        for ($i = 1; $i <= $n; $i++) $ans[] = [$i, 1];
        for ($i = $n % 2 + 2; $i <= $n; $i += 2) {
            for ($j = 2; $j <= 2 * ($n - $i) + 2; $j++) $ans[] = [$i, $j];
        }
        return $ans;
    }
}
''')

add("2648_generate_fibonacci_sequence", r'''<?php
// LeetCode 2648 - Generate Fibonacci Sequence
// https://leetcode.com/problems/generate-fibonacci-sequence/

class Solution {
    function fibGenerator() {
        $a = 0;
        $b = 1;
        while (true) {
            yield $a;
            $tmp = $a + $b;
            $a = $b;
            $b = $tmp;
        }
    }
}
''')

add("2649_nested_array_generator", r'''<?php
// LeetCode 2649 - Nested Array Generator
// https://leetcode.com/problems/nested-array-generator/

class Solution {
    function inorderTraversal($arr) {
        foreach ($arr as $x) {
            if (is_array($x)) {
                yield from $this->inorderTraversal($x);
            } else {
                yield $x;
            }
        }
    }
}
''')

add("2650_design_cancellable_function", r'''<?php
// LeetCode 2650 - Design Cancellable Function
// https://leetcode.com/problems/design-cancellable-function/

class Solution {
    function cancellable($generator) {
        $cancelled = false;
        $cancel = function() use (&$cancelled) { $cancelled = true; };
        $run = function() use ($generator, &$cancelled) {
            if ($generator instanceof Generator) {
                $next = $generator->current();
                while ($generator->valid()) {
                    if ($cancelled) {
                        $generator->throw(new Exception("Cancelled"));
                        continue;
                    }
                    $generator->send($next);
                    $next = $generator->current();
                }
                return $generator->getReturn();
            }
            return $generator;
        };
        return [$cancel, $run];
    }
}
''')

add("2651_calculate_delayed_arrival_time", r'''<?php
// LeetCode 2651 - Calculate Delayed Arrival Time
// https://leetcode.com/problems/calculate-delayed-arrival-time/

class Solution {
    function findDelayedArrivalTime($arrivalTime, $delayedTime) {
        return ($arrivalTime + $delayedTime) % 24;
    }
}
''')

add("2652_sum_multiples", r'''<?php
// LeetCode 2652 - Sum Multiples
// https://leetcode.com/problems/sum-multiples/

class Solution {
    function sumOfMultiples($n) {
        $ans = 0;
        for ($i = 1; $i <= $n; $i++) {
            if ($i % 3 === 0 || $i % 5 === 0 || $i % 7 === 0) $ans += $i;
        }
        return $ans;
    }
}
''')

add("2653_sliding_subarray_beauty", r'''<?php
// LeetCode 2653 - Sliding Subarray Beauty
// https://leetcode.com/problems/sliding-subarray-beauty/

class Solution {
    function getSubarrayBeauty($nums, $k, $x) {
        $freq = array_fill(0, 101, 0);
        $ans = array_fill(0, count($nums) - $k + 1, 0);
        for ($i = 0; $i < count($nums); $i++) {
            $freq[$nums[$i] + 50]++;
            if ($i >= $k) $freq[$nums[$i - $k] + 50]--;
            if ($i >= $k - 1) {
                $need = $x;
                $val = 0;
                for ($j = 0; $j < 50; $j++) {
                    $need -= $freq[$j];
                    if ($need <= 0) { $val = $j - 50; break; }
                }
                $ans[$i - $k + 1] = $val;
            }
        }
        return $ans;
    }
}
''')

add("2654_minimum_number_of_operations_to_make_all_array_elements_equal_to_1", r'''<?php
// LeetCode 2654 - Minimum Number of Operations to Make All Array Elements Equal to 1
// https://leetcode.com/problems/minimum-number-of-operations-to-make-all-array-elements-equal-to-1/

class Solution {
    function minOperations($nums) {
        $gcd = function($a, $b) {
            while ($b) { $t = $a % $b; $a = $b; $b = $t; }
            return $a;
        };
        $n = count($nums);
        $ones = 0;
        foreach ($nums as $x) if ($x === 1) $ones++;
        if ($ones > 0) return $n - $ones;
        $best = $n + 1;
        for ($i = 0; $i < $n; $i++) {
            $g = 0;
            for ($j = $i; $j < $n; $j++) {
                $g = $gcd($g, $nums[$j]);
                if ($g === 1) { $best = min($best, $j - $i); break; }
            }
        }
        if ($best === $n + 1) return -1;
        return $best + $n - 1;
    }
}
''')

add("2655_find_maximal_uncovered_ranges", r'''<?php
// LeetCode 2655 - Find Maximal Uncovered Ranges
// https://leetcode.com/problems/find-maximal-uncovered-ranges/

class Solution {
    function findMaximalUncoveredRanges($n, $ranges) {
        usort($ranges, function($a, $b) { return $a[0] <=> $b[0]; });
        $ans = [];
        $cur = 0;
        foreach ($ranges as $r) {
            if ($r[0] > $cur) $ans[] = [$cur, $r[0] - 1];
            if ($r[1] + 1 > $cur) $cur = $r[1] + 1;
        }
        if ($cur < $n) $ans[] = [$cur, $n - 1];
        return $ans;
    }
}
''')

add("2656_maximum_sum_with_exactly_k_elements", r'''<?php
// LeetCode 2656 - Maximum Sum With Exactly K Elements
// https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/

class Solution {
    function maximizeSum($nums, $k) {
        $mx = $nums[0];
        foreach ($nums as $x) if ($x > $mx) $mx = $x;
        return $k * $mx + intdiv($k * ($k - 1), 2);
    }
}
''')

add("2657_find_the_prefix_common_array_of_two_arrays", r'''<?php
// LeetCode 2657 - Find the Prefix Common Array of Two Arrays
// https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/

class Solution {
    function findThePrefixCommonArray($A, $B) {
        $n = count($A);
        $seenA = array_fill(0, $n + 1, false);
        $seenB = array_fill(0, $n + 1, false);
        $ans = array_fill(0, $n, 0);
        $common = 0;
        for ($i = 0; $i < $n; $i++) {
            if ($seenB[$A[$i]]) $common++;
            $seenA[$A[$i]] = true;
            if ($seenA[$B[$i]]) $common++;
            $seenB[$B[$i]] = true;
            $ans[$i] = $common;
        }
        return $ans;
    }
}
''')

add("2658_maximum_number_of_fish_in_a_grid", r'''<?php
// LeetCode 2658 - Maximum Number of Fish in a Grid
// https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/

class Solution {
    function findMaxFish($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        $dfs = function($r, $c) use (&$dfs, &$grid, $m, $n) {
            if ($r < 0 || $r >= $m || $c < 0 || $c >= $n || $grid[$r][$c] === 0) return 0;
            $fish = $grid[$r][$c];
            $grid[$r][$c] = 0;
            return $fish + $dfs($r + 1, $c) + $dfs($r - 1, $c) + $dfs($r, $c + 1) + $dfs($r, $c - 1);
        };
        $best = 0;
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if ($grid[$i][$j] > 0) $best = max($best, $dfs($i, $j));
            }
        }
        return $best;
    }
}
''')

add("2659_make_array_empty", r'''<?php
// LeetCode 2659 - Make Array Empty
// https://leetcode.com/problems/make-array-empty/

class Solution {
    function countOperationsToEmptyArray($nums) {
        $n = count($nums);
        $idx = range(0, $n - 1);
        usort($idx, function($a, $b) use ($nums) { return $nums[$a] <=> $nums[$b]; });
        $ans = $n;
        for ($i = 1; $i < $n; $i++) {
            if ($idx[$i] < $idx[$i - 1]) $ans += $n - $i;
        }
        return $ans;
    }
}
''')

add("2660_determine_the_winner_of_a_bowling_game", r'''<?php
// LeetCode 2660 - Determine the Winner of a Bowling Game
// https://leetcode.com/problems/determine-the-winner-of-a-bowling-game/

class Solution {
    function isWinner($player1, $player2) {
        $score = function($p) {
            $s = 0;
            for ($i = 0; $i < count($p); $i++) {
                $mul = 1;
                if (($i > 0 && $p[$i - 1] === 10) || ($i > 1 && $p[$i - 2] === 10)) $mul = 2;
                $s += $mul * $p[$i];
            }
            return $s;
        };
        $a = $score($player1);
        $b = $score($player2);
        if ($a > $b) return 1;
        if ($b > $a) return 2;
        return 0;
    }
}
''')

add("2661_first_completely_painted_row_or_column", r'''<?php
// LeetCode 2661 - First Completely Painted Row or Column
// https://leetcode.com/problems/first-completely-painted-row-or-column/

class Solution {
    function firstCompleteIndex($arr, $mat) {
        $m = count($mat);
        $n = count($mat[0]);
        $posR = array_fill(0, $m * $n + 1, 0);
        $posC = array_fill(0, $m * $n + 1, 0);
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                $posR[$mat[$i][$j]] = $i;
                $posC[$mat[$i][$j]] = $j;
            }
        }
        $rowCnt = array_fill(0, $m, 0);
        $colCnt = array_fill(0, $n, 0);
        for ($i = 0; $i < count($arr); $i++) {
            $r = $posR[$arr[$i]];
            $c = $posC[$arr[$i]];
            $rowCnt[$r]++;
            $colCnt[$c]++;
            if ($rowCnt[$r] === $n || $colCnt[$c] === $m) return $i;
        }
        return -1;
    }
}
''')

add("2662_minimum_cost_of_a_path_with_special_roads", r'''<?php
// LeetCode 2662 - Minimum Cost of a Path With Special Roads
// https://leetcode.com/problems/minimum-cost-of-a-path-with-special-roads/

class Solution {
    function minimumCost($start, $target, $specialRoads) {
        $points = [$start, $target];
        foreach ($specialRoads as $r) {
            $points[] = [$r[0], $r[1]];
            $points[] = [$r[2], $r[3]];
        }
        $N = count($points);
        $man = function($a, $b) {
            return abs($a[0] - $b[0]) + abs($a[1] - $b[1]);
        };
        $g = array_fill(0, $N, []);
        for ($i = 0; $i < $N; $i++) {
            for ($j = 0; $j < $N; $j++) {
                if ($i !== $j) $g[$i][] = [$j, $man($points[$i], $points[$j])];
            }
        }
        foreach ($specialRoads as $r) {
            $u = -1;
            $v = -1;
            for ($i = 0; $i < $N; $i++) {
                $p = $points[$i];
                if ($p[0] === $r[0] && $p[1] === $r[1]) $u = $i;
                if ($p[0] === $r[2] && $p[1] === $r[3]) $v = $i;
            }
            if ($u >= 0 && $v >= 0) $g[$u][] = [$v, $r[4]];
        }
        $INF = PHP_INT_MAX >> 2;
        $dist = array_fill(0, $N, $INF);
        $dist[0] = 0;
        $pq = new SplPriorityQueue();
        $pq->insert([0, 0], 0);
        while (!$pq->isEmpty()) {
            $cur = $pq->extract();
            $id = $cur[0];
            $cost = $cur[1];
            if ($cost > $dist[$id]) continue;
            foreach ($g[$id] as $e) {
                $to = $e[0];
                $w = $e[1];
                if ($cost + $w < $dist[$to]) {
                    $dist[$to] = $cost + $w;
                    $pq->insert([$to, $dist[$to]], -$dist[$to]);
                }
            }
        }
        return $dist[1];
    }
}
''')

add("2663_lexicographically_smallest_beautiful_string", r'''<?php
// LeetCode 2663 - Lexicographically Smallest Beautiful String
// https://leetcode.com/problems/lexicographically-smallest-beautiful-string/

class Solution {
    function smallestBeautifulString($s, $k) {
        $n = strlen($s);
        $b = str_split($s);
        for ($i = $n - 1; $i >= 0; $i--) {
            for ($code = ord($b[$i]) + 1; $code < 97 + $k; $code++) {
                $c = chr($code);
                if (($i > 0 && $c === $b[$i - 1]) || ($i > 1 && $c === $b[$i - 2])) continue;
                $b[$i] = $c;
                for ($j = $i + 1; $j < $n; $j++) {
                    for ($nc = 97; $nc < 97 + $k; $nc++) {
                        $ch = chr($nc);
                        if (($j > 0 && $ch === $b[$j - 1]) || ($j > 1 && $ch === $b[$j - 2])) continue;
                        $b[$j] = $ch;
                        break;
                    }
                }
                return implode("", $b);
            }
        }
        return "";
    }
}
''')

add("2664_the_knights_tour", r'''<?php
// LeetCode 2664 - The Knight's Tour
// https://leetcode.com/problems/the-knights-tour/

class Solution {
    function tourOfKnight($m, $n, $r, $c) {
        $DIRS = [[1,2],[1,-2],[-1,2],[-1,-2],[2,1],[2,-1],[-2,1],[-2,-1]];
        $ans = [];
        for ($i = 0; $i < $m; $i++) $ans[$i] = array_fill(0, $n, -1);
        $dfs = function($x, $y, $step) use (&$dfs, &$ans, $DIRS, $m, $n) {
            $ans[$x][$y] = $step;
            if ($step === $m * $n - 1) return true;
            foreach ($DIRS as $d) {
                $nx = $x + $d[0];
                $ny = $y + $d[1];
                if ($nx >= 0 && $nx < $m && $ny >= 0 && $ny < $n && $ans[$nx][$ny] === -1) {
                    if ($dfs($nx, $ny, $step + 1)) return true;
                }
            }
            $ans[$x][$y] = -1;
            return false;
        };
        $dfs($r, $c, 0);
        return $ans;
    }
}
''')

add("2665_counter_ii", r'''<?php
// LeetCode 2665 - Counter II
// https://leetcode.com/problems/counter-ii/

class Solution {
    function createCounter($init) {
        $cur = $init;
        return [
            'increment' => function() use (&$cur) { return ++$cur; },
            'decrement' => function() use (&$cur) { return --$cur; },
            'reset' => function() use ($init, &$cur) { $cur = $init; return $cur; },
        ];
    }
}
''')

add("2666_allow_one_function_call", r'''<?php
// LeetCode 2666 - Allow One Function Call
// https://leetcode.com/problems/allow-one-function-call/

class Solution {
    function once($fn) {
        $called = false;
        $res = null;
        return function(...$args) use ($fn, &$called, &$res) {
            if ($called) return null;
            $called = true;
            $res = $fn(...$args);
            return $res;
        };
    }
}
''')

add("2667_create_hello_world_function", r'''<?php
// LeetCode 2667 - Create Hello World Function
// https://leetcode.com/problems/create-hello-world-function/

class Solution {
    function createHelloWorld($args = null) {
        return function(...$ignored) {
            return "Hello World";
        };
    }
}
''')

add("2670_find_the_distinct_difference_array", r'''<?php
// LeetCode 2670 - Find the Distinct Difference Array
// https://leetcode.com/problems/find-the-distinct-difference-array/

class Solution {
    function distinctDifferenceArray($nums) {
        $n = count($nums);
        $suf = array_fill(0, $n + 1, 0);
        $seen = [];
        for ($i = $n - 1; $i >= 0; $i--) {
            $seen[$nums[$i]] = true;
            $suf[$i] = count($seen);
        }
        $seen = [];
        $ans = array_fill(0, $n, 0);
        for ($i = 0; $i < $n; $i++) {
            $seen[$nums[$i]] = true;
            $ans[$i] = count($seen) - $suf[$i + 1];
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

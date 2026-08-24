#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
SOLUTIONS = {}


def add(folder, body):
    SOLUTIONS[folder] = body if body.endswith("\n") else body + "\n"


add("2671_frequency_tracker", r'''<?php
// LeetCode 2671 - Frequency Tracker
// https://leetcode.com/problems/frequency-tracker/

class FrequencyTracker {
    private $freq = [];
    private $count = [];

    function add($number) {
        $old = $this->freq[$number] ?? 0;
        if ($old > 0) $this->count[$old] = ($this->count[$old] ?? 0) - 1;
        $this->freq[$number] = $old + 1;
        $this->count[$old + 1] = ($this->count[$old + 1] ?? 0) + 1;
    }

    function deleteOne($number) {
        $old = $this->freq[$number] ?? 0;
        if ($old === 0) return;
        $this->count[$old] = ($this->count[$old] ?? 0) - 1;
        $this->freq[$number] = $old - 1;
        if ($old - 1 > 0) $this->count[$old - 1] = ($this->count[$old - 1] ?? 0) + 1;
    }

    function hasFrequency($frequency) {
        return ($this->count[$frequency] ?? 0) > 0;
    }
}
''')

add("2672_number_of_adjacent_elements_with_the_same_color", r'''<?php
// LeetCode 2672 - Number of Adjacent Elements With the Same Color
// https://leetcode.com/problems/number-of-adjacent-elements-with-the-same-color/

class Solution {
    function colorTheArray($n, $queries) {
        $colors = array_fill(0, $n, 0);
        $ans = array_fill(0, count($queries), 0);
        $same = 0;
        for ($i = 0; $i < count($queries); $i++) {
            $idx = $queries[$i][0];
            $color = $queries[$i][1];
            if ($colors[$idx] !== 0) {
                if ($idx > 0 && $colors[$idx] === $colors[$idx - 1]) $same--;
                if ($idx + 1 < $n && $colors[$idx] === $colors[$idx + 1]) $same--;
            }
            $colors[$idx] = $color;
            if ($idx > 0 && $colors[$idx] === $colors[$idx - 1]) $same++;
            if ($idx + 1 < $n && $colors[$idx] === $colors[$idx + 1]) $same++;
            $ans[$i] = $same;
        }
        return $ans;
    }
}
''')

add("2673_make_costs_of_paths_equal_in_a_binary_tree", r'''<?php
// LeetCode 2673 - Make Costs of Paths Equal in a Binary Tree
// https://leetcode.com/problems/make-costs-of-paths-equal-in-a-binary-tree/

class Solution {
    function minIncrements($n, $cost) {
        $ans = 0;
        for ($i = intdiv($n, 2) - 1; $i >= 0; $i--) {
            $l = 2 * $i + 1;
            $r = 2 * $i + 2;
            $ans += abs($cost[$l] - $cost[$r]);
            $cost[$i] += max($cost[$l], $cost[$r]);
        }
        return $ans;
    }
}
''')

add("2674_split_a_circular_linked_list", r'''<?php
// LeetCode 2674 - Split a Circular Linked List
// https://leetcode.com/problems/split-a-circular-linked-list/

class ListNode {
    public $val = 0;
    public $next = null;
    function __construct($val = 0, $next = null) {
        $this->val = $val;
        $this->next = $next;
    }
}

class Solution {
    function splitCircularLinkedList($list) {
        if ($list === null) return [null, null];
        $slow = $list;
        $fast = $list;
        while ($fast->next !== $list && $fast->next->next !== $list) {
            $slow = $slow->next;
            $fast = $fast->next->next;
        }
        if ($fast->next->next === $list) $fast = $fast->next;
        $head2 = $slow->next;
        $slow->next = $list;
        $fast->next = $head2;
        return [$list, $head2];
    }
}
''')

add("2675_array_of_objects_to_matrix", r'''<?php
// LeetCode 2675 - Array of Objects to Matrix
// https://leetcode.com/problems/array-of-objects-to-matrix/

class Solution {
    function jsonToMatrix($arr) {
        $isObj = function($x) {
            return is_array($x) && !array_is_list($x);
        };
        $flatten = function($obj, $prefix, &$out) use (&$flatten, $isObj) {
            if (!is_array($obj)) {
                $out[$prefix] = $obj;
                return;
            }
            if (array_is_list($obj)) {
                if (count($obj) === 0) return;
                for ($i = 0; $i < count($obj); $i++) {
                    $flatten($obj[$i], $prefix !== "" ? $prefix . "." . $i : (string)$i, $out);
                }
                return;
            }
            if (count($obj) === 0) return;
            foreach ($obj as $k => $v) {
                $flatten($v, $prefix !== "" ? $prefix . "." . $k : (string)$k, $out);
            }
        };
        $maps = [];
        foreach ($arr as $o) {
            $m = [];
            $flatten($o, "", $m);
            $maps[] = $m;
        }
        $keySet = [];
        foreach ($maps as $m) {
            foreach ($m as $k => $_) $keySet[$k] = true;
        }
        $keys = array_keys($keySet);
        sort($keys);
        $mat = [$keys];
        foreach ($maps as $m) {
            $row = [];
            foreach ($keys as $k) $row[] = array_key_exists($k, $m) ? $m[$k] : "";
            $mat[] = $row;
        }
        return $mat;
    }
}
''')

add("2676_throttle", r'''<?php
// LeetCode 2676 - Throttle
// https://leetcode.com/problems/throttle/

class Solution {
    function throttle($fn, $t) {
        $last = -INF;
        $pending = null;
        return function(...$args) use ($fn, $t, &$last, &$pending) {
            $now = (int)round(microtime(true) * 1000);
            $remaining = $t - ($now - $last);
            if ($remaining <= 0) {
                $last = $now;
                $pending = null;
                return $fn(...$args);
            }
            $pending = $args;
            return null;
        };
    }
}
''')

add("2677_chunk_array", r'''<?php
// LeetCode 2677 - Chunk Array
// https://leetcode.com/problems/chunk-array/

class Solution {
    function chunk($arr, $size) {
        $ans = [];
        for ($i = 0; $i < count($arr); $i += $size) {
            $ans[] = array_slice($arr, $i, $size);
        }
        return $ans;
    }
}
''')

add("2678_number_of_senior_citizens", r'''<?php
// LeetCode 2678 - Number of Senior Citizens
// https://leetcode.com/problems/number-of-senior-citizens/

class Solution {
    function countSeniors($details) {
        $ans = 0;
        foreach ($details as $d) {
            $age = (ord($d[11]) - 48) * 10 + (ord($d[12]) - 48);
            if ($age > 60) $ans++;
        }
        return $ans;
    }
}
''')

add("2679_sum_in_a_matrix", r'''<?php
// LeetCode 2679 - Sum in a Matrix
// https://leetcode.com/problems/sum-in-a-matrix/

class Solution {
    function matrixSum($nums) {
        foreach ($nums as &$row) sort($row);
        unset($row);
        $ans = 0;
        $n = count($nums[0]);
        for ($j = 0; $j < $n; $j++) {
            $mx = 0;
            foreach ($nums as $row) $mx = max($mx, $row[$j]);
            $ans += $mx;
        }
        return $ans;
    }
}
''')

add("2680_maximum_or", r'''<?php
// LeetCode 2680 - Maximum OR
// https://leetcode.com/problems/maximum-or/

class Solution {
    function maximumOr($nums, $k) {
        $n = count($nums);
        $pref = array_fill(0, $n + 1, 0);
        $suf = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; $i++) $pref[$i + 1] = $pref[$i] | $nums[$i];
        for ($i = $n - 1; $i >= 0; $i--) $suf[$i] = $suf[$i + 1] | $nums[$i];
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            $cur = $pref[$i] | ($nums[$i] * (1 << $k)) | $suf[$i + 1];
            if ($cur > $ans) $ans = $cur;
        }
        return $ans;
    }
}
''')

add("2681_power_of_heroes", r'''<?php
// LeetCode 2681 - Power of Heroes
// https://leetcode.com/problems/power-of-heroes/

class Solution {
    function sumOfPower($nums) {
        $MOD = 1000000007;
        sort($nums);
        $ans = 0;
        $s = 0;
        foreach ($nums as $x) {
            $ans = ($ans + (($s + $x) % $MOD) * $x % $MOD * $x) % $MOD;
            $s = ($s * 2 + $x) % $MOD;
        }
        return $ans;
    }
}
''')

add("2682_find_the_losers_of_the_circular_game", r'''<?php
// LeetCode 2682 - Find the Losers of the Circular Game
// https://leetcode.com/problems/find-the-losers-of-the-circular-game/

class Solution {
    function circularGameLosers($n, $k) {
        $seen = array_fill(0, $n + 1, false);
        $cur = 1;
        $step = 1;
        while (!$seen[$cur]) {
            $seen[$cur] = true;
            $cur = ($cur - 1 + $step * $k) % $n + 1;
            $step++;
        }
        $ans = [];
        for ($i = 1; $i <= $n; $i++) if (!$seen[$i]) $ans[] = $i;
        return $ans;
    }
}
''')

add("2683_neighboring_bitwise_xor", r'''<?php
// LeetCode 2683 - Neighboring Bitwise XOR
// https://leetcode.com/problems/neighboring-bitwise-xor/

class Solution {
    function doesValidArrayExist($derived) {
        $x = 0;
        foreach ($derived as $v) $x ^= $v;
        return $x === 0;
    }
}
''')

add("2684_maximum_number_of_moves_in_a_grid", r'''<?php
// LeetCode 2684 - Maximum Number of Moves in a Grid
// https://leetcode.com/problems/maximum-number-of-moves-in-a-grid/

class Solution {
    function maxMoves($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        $dp = array_fill(0, $m, 0);
        for ($c = $n - 2; $c >= 0; $c--) {
            $ndp = array_fill(0, $m, 0);
            for ($r = 0; $r < $m; $r++) {
                $best = 0;
                for ($dr = -1; $dr <= 1; $dr++) {
                    $nr = $r + $dr;
                    if ($nr >= 0 && $nr < $m && $grid[$nr][$c + 1] > $grid[$r][$c]) {
                        $best = max($best, 1 + $dp[$nr]);
                    }
                }
                $ndp[$r] = $best;
            }
            $dp = $ndp;
        }
        return max($dp);
    }
}
''')

add("2685_count_the_number_of_complete_components", r'''<?php
// LeetCode 2685 - Count the Number of Complete Components
// https://leetcode.com/problems/count-the-number-of-complete-components/

class Solution {
    function countCompleteComponents($n, $edges) {
        $g = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $g[$e[0]][] = $e[1];
            $g[$e[1]][] = $e[0];
        }
        $vis = array_fill(0, $n, false);
        $ans = 0;
        $dfs = function($u, &$nodes) use (&$dfs, &$g, &$vis) {
            $vis[$u] = true;
            $nodes[] = $u;
            foreach ($g[$u] as $v) if (!$vis[$v]) $dfs($v, $nodes);
        };
        for ($i = 0; $i < $n; $i++) {
            if ($vis[$i]) continue;
            $nodes = [];
            $dfs($i, $nodes);
            $ecount = 0;
            foreach ($nodes as $u) $ecount += count($g[$u]);
            $ecount = intdiv($ecount, 2);
            $sz = count($nodes);
            if ($ecount === intdiv($sz * ($sz - 1), 2)) $ans++;
        }
        return $ans;
    }
}
''')

add("2689_extract_kth_character_from_the_rope_tree", r'''<?php
// LeetCode 2689 - Extract Kth Character From The Rope Tree
// https://leetcode.com/problems/extract-kth-character-from-the-rope-tree/

class RopeTreeNode {
    public $len = 0;
    public $val = "";
    public $left = null;
    public $right = null;
    function __construct($len = 0, $val = "", $left = null, $right = null) {
        $this->len = $len;
        $this->val = $val;
        $this->left = $left;
        $this->right = $right;
    }
}

class Solution {
    function getKthCharacter($root, $k) {
        $dfs = function($node, $kk) use (&$dfs) {
            if ($node->left === null && $node->right === null) return $node->val;
            $leftLen = 0;
            if ($node->left) $leftLen = $node->left->len > 0 ? $node->left->len : 1;
            if ($kk <= $leftLen) return $dfs($node->left, $kk);
            return $dfs($node->right, $kk - $leftLen);
        };
        return $dfs($root, $k);
    }
}
''')

add("2690_infinite_method_object", r'''<?php
// LeetCode 2690 - Infinite Method Object
// https://leetcode.com/problems/infinite-method-object/

class InfiniteObject {
    function __call($name, $args) {
        return "Hello World";
    }
}

class Solution {
    function createInfiniteObject($method = null) {
        return new InfiniteObject();
    }
}
''')

add("2691_immutability_helper", r'''<?php
// LeetCode 2691 - Immutability Helper
// https://leetcode.com/problems/immutability-helper/

class ImmutableHelper {
    private $obj;

    function __construct($obj) {
        $this->obj = $obj;
    }

    function produce($mutator) {
        $copy = unserialize(serialize($this->obj));
        $mutator($copy);
        return $copy;
    }
}

class Solution {
    function ImmutableHelper($obj, $mutators = null) {
        return new ImmutableHelper($obj);
    }
}
''')

add("2692_make_object_immutable", r'''<?php
// LeetCode 2692 - Make Object Immutable
// https://leetcode.com/problems/make-object-immutable/

class ImmutableArray {
    private $data;
    function __construct($data) { $this->data = $data; }
    function __get($prop) {
        if (in_array($prop, ["pop", "push", "shift", "unshift", "splice", "sort", "reverse"], true)) {
            throw new Exception("Error Calling Method: " . $prop);
        }
        $v = $this->data[$prop] ?? null;
        if (is_array($v)) return (new Solution())->makeImmutable($v);
        return $v;
    }
    function __set($prop, $value) {
        throw new Exception("Error Modifying Index: " . $prop);
    }
}

class ImmutableObject {
    private $data;
    function __construct($data) { $this->data = $data; }
    function __get($prop) {
        $v = $this->data[$prop] ?? null;
        if (is_array($v)) return (new Solution())->makeImmutable($v);
        return $v;
    }
    function __set($prop, $value) {
        throw new Exception("Error Modifying: " . $prop);
    }
}

class Solution {
    function makeImmutable($obj) {
        if ($obj === null || !is_array($obj)) return $obj;
        if (array_is_list($obj)) return new ImmutableArray($obj);
        return new ImmutableObject($obj);
    }
}
''')

add("2693_call_function_with_custom_context", r'''<?php
// LeetCode 2693 - Call Function with Custom Context
// https://leetcode.com/problems/call-function-with-custom-context/

class Solution {
    function callPolyfill($fn, $obj, ...$args) {
        if ($fn instanceof Closure) {
            return $fn->call((object)$obj, ...$args);
        }
        return $fn(...$args);
    }
}
''')

add("2694_event_emitter", r'''<?php
// LeetCode 2694 - Event Emitter
// https://leetcode.com/problems/event-emitter/

class EventEmitter {
    private $handlers = [];

    function subscribe($eventName, $callback) {
        if (!isset($this->handlers[$eventName])) $this->handlers[$eventName] = [];
        $this->handlers[$eventName][] = $callback;
        $list =& $this->handlers[$eventName];
        return [
            'unsubscribe' => function() use (&$list, $callback) {
                $idx = array_search($callback, $list, true);
                if ($idx !== false) array_splice($list, $idx, 1);
            },
        ];
    }

    function emit($eventName, $args = []) {
        $list = $this->handlers[$eventName] ?? [];
        $out = [];
        foreach ($list as $cb) $out[] = $cb(...$args);
        return $out;
    }
}

class Solution {
    function EventEmitter($actions = null, $values = null) {
        return new EventEmitter();
    }
}
''')

add("2695_array_wrapper", r'''<?php
// LeetCode 2695 - Array Wrapper
// https://leetcode.com/problems/array-wrapper/

class ArrayWrapper {
    private $nums;

    function __construct($nums) {
        $this->nums = $nums;
    }

    function valueOf() {
        $s = 0;
        foreach ($this->nums as $x) $s += $x;
        return $s;
    }

    function __toString() {
        return "[" . implode(",", $this->nums) . "]";
    }
}

class Solution {
    function ArrayWrapper($nums) {
        return new ArrayWrapper($nums);
    }
}
''')

add("2696_minimum_string_length_after_removing_substrings", r'''<?php
// LeetCode 2696 - Minimum String Length After Removing Substrings
// https://leetcode.com/problems/minimum-string-length-after-removing-substrings/

class Solution {
    function minLength($s) {
        $st = [];
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $c = $s[$i];
            $last = count($st) ? $st[count($st) - 1] : null;
            if (count($st) && (($last === "A" && $c === "B") || ($last === "C" && $c === "D"))) {
                array_pop($st);
            } else {
                $st[] = $c;
            }
        }
        return count($st);
    }
}
''')

add("2697_lexicographically_smallest_palindrome", r'''<?php
// LeetCode 2697 - Lexicographically Smallest Palindrome
// https://leetcode.com/problems/lexicographically-smallest-palindrome/

class Solution {
    function makeSmallestPalindrome($s) {
        $arr = str_split($s);
        $n = count($arr);
        for ($i = 0; $i < intdiv($n, 2); $i++) {
            $c = $arr[$i] < $arr[$n - 1 - $i] ? $arr[$i] : $arr[$n - 1 - $i];
            $arr[$i] = $arr[$n - 1 - $i] = $c;
        }
        return implode("", $arr);
    }
}
''')

add("2698_find_the_punishment_number_of_an_integer", r'''<?php
// LeetCode 2698 - Find the Punishment Number of an Integer
// https://leetcode.com/problems/find-the-punishment-number-of-an-integer/

class Solution {
    function punishmentNumber($n) {
        $dfs = function($s, $i, $sum, $target) use (&$dfs) {
            if ($i === strlen($s)) return $sum === $target;
            $cur = 0;
            for ($j = $i; $j < strlen($s); $j++) {
                $cur = $cur * 10 + (ord($s[$j]) - 48);
                if ($sum + $cur > $target) break;
                if ($dfs($s, $j + 1, $sum + $cur, $target)) return true;
            }
            return false;
        };
        $ans = 0;
        for ($i = 1; $i <= $n; $i++) {
            $sq = $i * $i;
            if ($dfs((string)$sq, 0, 0, $i)) $ans += $sq;
        }
        return $ans;
    }
}
''')

add("2699_modify_graph_edge_weights", r'''<?php
// LeetCode 2699 - Modify Graph Edge Weights
// https://leetcode.com/problems/modify-graph-edge-weights/

class Solution {
    function modifiedGraphEdges($n, $edges, $source, $destination, $target) {
        $INF = 2000000000;
        $dijkstra = function($ignoreNeg) use ($n, &$edges, $source, $INF) {
            $dist = array_fill(0, $n, $INF);
            $dist[$source] = 0;
            $pq = new SplPriorityQueue();
            $pq->insert([$source, 0], 0);
            while (!$pq->isEmpty()) {
                $cur = $pq->extract();
                $u = $cur[0];
                $d = $cur[1];
                if ($d !== $dist[$u]) continue;
                foreach ($edges as $e) {
                    $a = $e[0];
                    $b = $e[1];
                    $w = $e[2];
                    if ($a !== $u && $b !== $u) continue;
                    $to = $a === $u ? $b : $a;
                    if ($w === -1) {
                        if ($ignoreNeg) continue;
                        $w = 1;
                    }
                    if ($d + $w < $dist[$to]) {
                        $dist[$to] = $d + $w;
                        $pq->insert([$to, $dist[$to]], -$dist[$to]);
                    }
                }
            }
            return $dist;
        };
        $d = $dijkstra(true);
        if ($d[$destination] < $target) return [];
        $matched = $d[$destination] === $target;
        for ($i = 0; $i < count($edges); $i++) {
            if ($edges[$i][2] !== -1) continue;
            if ($matched) {
                $edges[$i][2] = $INF;
                continue;
            }
            $edges[$i][2] = 1;
            $d = $dijkstra(false);
            if ($d[$destination] <= $target) {
                $edges[$i][2] += $target - $d[$destination];
                $matched = true;
            }
        }
        $d = $dijkstra(false);
        if ($d[$destination] !== $target) return [];
        return $edges;
    }
}
''')

add("2700_differences_between_two_objects", r'''<?php
// LeetCode 2700 - Differences Between Two Objects
// https://leetcode.com/problems/differences-between-two-objects/

class Solution {
    function objDiff($obj1, $obj2) {
        $diff = [];
        foreach ($obj1 as $k => $v1) {
            if (!array_key_exists($k, $obj2)) continue;
            $v2 = $obj2[$k];
            $bothObj = is_array($v1) && $v1 !== null && is_array($v2) && $v2 !== null
                && !array_is_list($v1) && !array_is_list($v2);
            $bothArr = is_array($v1) && is_array($v2) && array_is_list($v1) && array_is_list($v2);
            if ($bothObj || $bothArr) {
                $child = $this->objDiff($v1, $v2);
                if (count($child) > 0) $diff[$k] = $child;
            } else if ($v1 !== $v2) {
                $diff[$k] = [$v1, $v2];
            }
        }
        return $diff;
    }
}
''')

add("2702_minimum_operations_to_make_numbers_non_positive", r'''<?php
// LeetCode 2702 - Minimum Operations to Make Numbers Non-positive
// https://leetcode.com/problems/minimum-operations-to-make-numbers-non-positive/

class Solution {
    function minOperations($nums, $x, $y) {
        $lo = 0;
        $hi = 0;
        foreach ($nums as $v) {
            $hi = max($hi, (int)ceil($v / $y));
            $hi = max($hi, (int)ceil($v / $x));
        }
        $hi += count($nums);
        $ok = function($ops) use ($nums, $x, $y) {
            $extra = 0;
            foreach ($nums as $v) {
                $remain = $v - $ops * $y;
                if ($remain > 0) $extra += (int)ceil($remain / ($x - $y));
            }
            return $extra <= $ops;
        };
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi, 2);
            if ($ok($mid)) $hi = $mid;
            else $lo = $mid + 1;
        }
        return $lo;
    }
}
''')

add("2703_return_length_of_arguments_passed", r'''<?php
// LeetCode 2703 - Return Length of Arguments Passed
// https://leetcode.com/problems/return-length-of-arguments-passed/

class Solution {
    function argumentsLength(...$args) {
        return count($args);
    }
}
''')

add("2704_to_be_or_not_to_be", r'''<?php
// LeetCode 2704 - To Be Or Not To Be
// https://leetcode.com/problems/to-be-or-not-to-be/

class Solution {
    function expect($val) {
        return [
            'toBe' => function($other) use ($val) {
                if ($val === $other) return true;
                throw new Exception("Not Equal");
            },
            'notToBe' => function($other) use ($val) {
                if ($val !== $other) return true;
                throw new Exception("Equal");
            },
        ];
    }
}
''')

add("2705_compact_object", r'''<?php
// LeetCode 2705 - Compact Object
// https://leetcode.com/problems/compact-object/

class Solution {
    function compactObject($obj) {
        $truthy = function($v) {
            if (is_array($v)) return true;
            return (bool)$v;
        };
        if (is_array($obj) && array_is_list($obj)) {
            $out = [];
            foreach ($obj as $x) {
                $v = $this->compactObject($x);
                if ($truthy($v)) $out[] = $v;
            }
            return $out;
        }
        if (is_array($obj)) {
            $out = [];
            foreach ($obj as $k => $val) {
                $v = $this->compactObject($val);
                if ($truthy($v)) $out[$k] = $v;
            }
            return $out;
        }
        return $obj;
    }
}
''')

add("2706_buy_two_chocolates", r'''<?php
// LeetCode 2706 - Buy Two Chocolates
// https://leetcode.com/problems/buy-two-chocolates/

class Solution {
    function buyChoco($prices, $money) {
        sort($prices);
        $cost = $prices[0] + $prices[1];
        return $cost <= $money ? $money - $cost : $money;
    }
}
''')

add("2707_extra_characters_in_a_string", r'''<?php
// LeetCode 2707 - Extra Characters in a String
// https://leetcode.com/problems/extra-characters-in-a-string/

class Solution {
    function minExtraChar($s, $dictionary) {
        $dict = array_flip($dictionary);
        $n = strlen($s);
        $dp = array_fill(0, $n + 1, $n);
        $dp[0] = 0;
        for ($i = 0; $i < $n; $i++) {
            $dp[$i + 1] = min($dp[$i + 1], $dp[$i] + 1);
            for ($j = $i + 1; $j <= $n; $j++) {
                $sub = substr($s, $i, $j - $i);
                if (isset($dict[$sub])) $dp[$j] = min($dp[$j], $dp[$i]);
            }
        }
        return $dp[$n];
    }
}
''')

add("2708_maximum_strength_of_a_group", r'''<?php
// LeetCode 2708 - Maximum Strength of a Group
// https://leetcode.com/problems/maximum-strength-of-a-group/

class Solution {
    function maxStrength($nums) {
        sort($nums);
        $n = count($nums);
        if ($n === 1) return $nums[0];
        $prod = 1;
        $used = false;
        $i = 0;
        while ($i + 1 < $n && $nums[$i] < 0 && $nums[$i + 1] < 0) {
            $prod *= $nums[$i] * $nums[$i + 1];
            $used = true;
            $i += 2;
        }
        $negLeft = $i < $n && $nums[$i] < 0;
        for (; $i < $n; $i++) {
            if ($nums[$i] > 0) {
                $prod *= $nums[$i];
                $used = true;
            }
        }
        if (!$used) {
            if ($negLeft) {
                foreach ($nums as $x) if ($x === 0) return 0;
                return $nums[$n - 1];
            }
            return 0;
        }
        return $prod;
    }
}
''')

add("2709_greatest_common_divisor_traversal", r'''<?php
// LeetCode 2709 - Greatest Common Divisor Traversal
// https://leetcode.com/problems/greatest-common-divisor-traversal/

class Solution {
    function canTraverseAllPairs($nums) {
        $n = count($nums);
        if ($n === 1) return true;
        $mx = $nums[0];
        foreach ($nums as $x) if ($x > $mx) $mx = $x;
        $parent = range(0, $mx);
        $find = function($x) use (&$find, &$parent) {
            if ($parent[$x] !== $x) $parent[$x] = $find($parent[$x]);
            return $parent[$x];
        };
        $unite = function($a, $b) use ($find, &$parent) {
            $ra = $find($a);
            $rb = $find($b);
            if ($ra !== $rb) $parent[$ra] = $rb;
        };
        $has = array_fill(0, $mx + 1, false);
        foreach ($nums as $x) {
            if ($x === 1) return false;
            $has[$x] = true;
        }
        $sieve = array_fill(0, $mx + 1, 0);
        for ($i = 2; $i <= $mx; $i++) {
            if ($sieve[$i] === 0) {
                for ($j = $i; $j <= $mx; $j += $i) {
                    if ($sieve[$j] === 0) $sieve[$j] = $i;
                    if ($has[$j]) $unite($i, $j);
                }
            }
        }
        $root = $find($nums[0]);
        foreach ($nums as $x) if ($find($x) !== $root) return false;
        return true;
    }
}
''')

add("2710_remove_trailing_zeros_from_a_string", r'''<?php
// LeetCode 2710 - Remove Trailing Zeros From a String
// https://leetcode.com/problems/remove-trailing-zeros-from-a-string/

class Solution {
    function removeTrailingZeros($num) {
        $end = strlen($num);
        while ($end > 0 && $num[$end - 1] === "0") $end--;
        return substr($num, 0, $end);
    }
}
''')

add("2711_difference_of_number_of_distinct_values_on_diagonals", r'''<?php
// LeetCode 2711 - Difference of Number of Distinct Values on Diagonals
// https://leetcode.com/problems/difference-of-number-of-distinct-values-on-diagonals/

class Solution {
    function differenceOfDistinctValues($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        $ans = [];
        for ($i = 0; $i < $m; $i++) {
            $ans[$i] = array_fill(0, $n, 0);
            for ($j = 0; $j < $n; $j++) {
                $top = [];
                $bot = [];
                for ($r = $i - 1, $c = $j - 1; $r >= 0 && $c >= 0; $r--, $c--) $top[$grid[$r][$c]] = true;
                for ($r = $i + 1, $c = $j + 1; $r < $m && $c < $n; $r++, $c++) $bot[$grid[$r][$c]] = true;
                $ans[$i][$j] = abs(count($top) - count($bot));
            }
        }
        return $ans;
    }
}
''')

add("2712_minimum_cost_to_make_all_characters_equal", r'''<?php
// LeetCode 2712 - Minimum Cost to Make All Characters Equal
// https://leetcode.com/problems/minimum-cost-to-make-all-characters-equal/

class Solution {
    function minimumCost($s) {
        $n = strlen($s);
        $ans = 0;
        for ($i = 1; $i < $n; $i++) {
            if ($s[$i] !== $s[$i - 1]) $ans += min($i, $n - $i);
        }
        return $ans;
    }
}
''')

add("2713_maximum_strictly_increasing_cells_in_a_matrix", r'''<?php
// LeetCode 2713 - Maximum Strictly Increasing Cells in a Matrix
// https://leetcode.com/problems/maximum-strictly-increasing-cells-in-a-matrix/

class Solution {
    function maxIncreasingCells($mat) {
        $m = count($mat);
        $n = count($mat[0]);
        $cells = [];
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) $cells[] = [$mat[$i][$j], $i, $j];
        }
        usort($cells, function($a, $b) { return $a[0] <=> $b[0]; });
        $rowMax = array_fill(0, $m, 0);
        $colMax = array_fill(0, $n, 0);
        $dp = [];
        for ($i = 0; $i < $m; $i++) $dp[$i] = array_fill(0, $n, 0);
        $ans = 0;
        $len = count($cells);
        for ($i = 0; $i < $len; ) {
            $j = $i;
            while ($j < $len && $cells[$j][0] === $cells[$i][0]) $j++;
            $buf = [];
            for ($k = $i; $k < $j; $k++) {
                $r = $cells[$k][1];
                $c = $cells[$k][2];
                $best = max($rowMax[$r], $colMax[$c]);
                $dp[$r][$c] = $best + 1;
                $ans = max($ans, $dp[$r][$c]);
                $buf[] = [$r, $c, $dp[$r][$c]];
            }
            foreach ($buf as $t) {
                $rowMax[$t[0]] = max($rowMax[$t[0]], $t[2]);
                $colMax[$t[1]] = max($colMax[$t[1]], $t[2]);
            }
            $i = $j;
        }
        return $ans;
    }
}
''')

add("2714_find_shortest_path_with_k_hops", r'''<?php
// LeetCode 2714 - Find Shortest Path With K Hops
// https://leetcode.com/problems/find-shortest-path-with-k-hops/

class Solution {
    function shortestPathWithHops($n, $edges, $s, $d, $k) {
        $g = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $g[$e[0]][] = [$e[1], $e[2]];
            $g[$e[1]][] = [$e[0], $e[2]];
        }
        $INF = PHP_INT_MAX >> 2;
        $dist = [];
        for ($i = 0; $i < $n; $i++) $dist[$i] = array_fill(0, $k + 1, $INF);
        $dist[$s][0] = 0;
        $pq = new SplPriorityQueue();
        $pq->insert([$s, 0, 0], 0);
        while (!$pq->isEmpty()) {
            $cur = $pq->extract();
            $u = $cur[0];
            $hops = $cur[1];
            $cd = $cur[2];
            if ($u === $d) return $cd;
            if ($cd > $dist[$u][$hops]) continue;
            foreach ($g[$u] as $e) {
                $to = $e[0];
                $w = $e[1];
                if ($cd + $w < $dist[$to][$hops]) {
                    $dist[$to][$hops] = $cd + $w;
                    $pq->insert([$to, $hops, $dist[$to][$hops]], -$dist[$to][$hops]);
                }
                if ($hops < $k && $cd < $dist[$to][$hops + 1]) {
                    $dist[$to][$hops + 1] = $cd;
                    $pq->insert([$to, $hops + 1, $cd], -$cd);
                }
            }
        }
        return -1;
    }
}
''')

add("2715_timeout_cancellation", r'''<?php
// LeetCode 2715 - Timeout Cancellation
// https://leetcode.com/problems/timeout-cancellation/

class Solution {
    function cancellable($fn, $args, $t) {
        $cancelled = false;
        $run = function() use ($fn, $args, &$cancelled) {
            if (!$cancelled) $fn(...$args);
        };
        return function() use (&$cancelled) {
            $cancelled = true;
        };
    }
}
''')

add("2716_minimize_string_length", r'''<?php
// LeetCode 2716 - Minimize String Length
// https://leetcode.com/problems/minimize-string-length/

class Solution {
    function minimizedStringLength($s) {
        $seen = [];
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) $seen[$s[$i]] = true;
        return count($seen);
    }
}
''')

add("2717_semi_ordered_permutation", r'''<?php
// LeetCode 2717 - Semi-Ordered Permutation
// https://leetcode.com/problems/semi-ordered-permutation/

class Solution {
    function semiOrderedPermutation($nums) {
        $n = count($nums);
        $p1 = 0;
        $pn = 0;
        for ($i = 0; $i < $n; $i++) {
            if ($nums[$i] === 1) $p1 = $i;
            if ($nums[$i] === $n) $pn = $i;
        }
        $ans = $p1 + ($n - 1 - $pn);
        if ($p1 > $pn) $ans--;
        return $ans;
    }
}
''')

add("2718_sum_of_matrix_after_queries", r'''<?php
// LeetCode 2718 - Sum of Matrix After Queries
// https://leetcode.com/problems/sum-of-matrix-after-queries/

class Solution {
    function matrixSumQueries($n, $queries) {
        $rowDone = array_fill(0, $n, false);
        $colDone = array_fill(0, $n, false);
        $rowsLeft = $n;
        $colsLeft = $n;
        $ans = 0;
        for ($i = count($queries) - 1; $i >= 0; $i--) {
            $type = $queries[$i][0];
            $idx = $queries[$i][1];
            $val = $queries[$i][2];
            if ($type === 0) {
                if (!$rowDone[$idx]) {
                    $ans += $val * $colsLeft;
                    $rowDone[$idx] = true;
                    $rowsLeft--;
                }
            } else {
                if (!$colDone[$idx]) {
                    $ans += $val * $rowsLeft;
                    $colDone[$idx] = true;
                    $colsLeft--;
                }
            }
        }
        return $ans;
    }
}
''')

add("2719_count_of_integers", r'''<?php
// LeetCode 2719 - Count of Integers
// https://leetcode.com/problems/count-of-integers/

class Solution {
    function count($num1, $num2, $min_sum, $max_sum) {
        $MOD = 1000000007;
        $dec = function($s) {
            $arr = str_split($s);
            $i = count($arr) - 1;
            while ($i >= 0 && $arr[$i] === "0") { $arr[$i] = "9"; $i--; }
            if ($i >= 0) $arr[$i] = chr(ord($arr[$i]) - 1);
            $j = 0;
            while ($j < count($arr) - 1 && $arr[$j] === "0") $j++;
            return implode("", array_slice($arr, $j));
        };
        $dp = function($s) use ($min_sum, $max_sum, $MOD) {
            $memo = [];
            $dfs = function($pos, $sum, $tight) use (&$dfs, &$memo, $s, $min_sum, $max_sum, $MOD) {
                if ($sum > $max_sum) return 0;
                if ($pos === strlen($s)) return $sum >= $min_sum ? 1 : 0;
                $key = $pos . "," . $sum . "," . ($tight ? 1 : 0);
                if (isset($memo[$key])) return $memo[$key];
                $up = $tight ? ord($s[$pos]) - 48 : 9;
                $res = 0;
                for ($d = 0; $d <= $up; $d++) {
                    $res = ($res + $dfs($pos + 1, $sum + $d, $tight && $d === $up)) % $MOD;
                }
                $memo[$key] = $res;
                return $res;
            };
            return $dfs(0, 0, true);
        };
        return ($dp($num2) - $dp($dec($num1)) + $MOD) % $MOD;
    }
}
''')

add("2721_execute_asynchronous_functions_in_parallel", r'''<?php
// LeetCode 2721 - Execute Asynchronous Functions in Parallel
// https://leetcode.com/problems/execute-asynchronous-functions-in-parallel/

class Solution {
    function promiseAll($functions) {
        $n = count($functions);
        if ($n === 0) return [];
        $ans = array_fill(0, $n, null);
        for ($i = 0; $i < $n; $i++) $ans[$i] = $functions[$i]();
        return $ans;
    }
}
''')

add("2722_join_two_arrays_by_id", r'''<?php
// LeetCode 2722 - Join Two Arrays by ID
// https://leetcode.com/problems/join-two-arrays-by-id/

class Solution {
    function join($arr1, $arr2) {
        $byId = [];
        foreach ($arr1 as $obj) $byId[$obj['id']] = $obj;
        foreach ($arr2 as $obj) {
            $id = $obj['id'];
            if (isset($byId[$id])) $byId[$id] = array_merge($byId[$id], $obj);
            else $byId[$id] = $obj;
        }
        $vals = array_values($byId);
        usort($vals, function($a, $b) { return $a['id'] <=> $b['id']; });
        return $vals;
    }
}
''')

add("2723_add_two_promises", r'''<?php
// LeetCode 2723 - Add Two Promises
// https://leetcode.com/problems/add-two-promises/

class Solution {
    function addTwoPromises($promise1, $promise2) {
        $a = is_callable($promise1) ? $promise1() : $promise1;
        $b = is_callable($promise2) ? $promise2() : $promise2;
        return $a + $b;
    }
}
''')

add("2724_sort_by", r'''<?php
// LeetCode 2724 - Sort By
// https://leetcode.com/problems/sort-by/

class Solution {
    function sortBy($arr, $fn) {
        $out = $arr;
        usort($out, function($a, $b) use ($fn) { return $fn($a) <=> $fn($b); });
        return $out;
    }
}
''')

add("2725_interval_cancellation", r'''<?php
// LeetCode 2725 - Interval Cancellation
// https://leetcode.com/problems/interval-cancellation/

class Solution {
    function cancellable($fn, $args, $t) {
        $fn(...$args);
        $cancelled = false;
        return function() use (&$cancelled) {
            $cancelled = true;
        };
    }
}
''')

add("2726_calculator_with_method_chaining", r'''<?php
// LeetCode 2726 - Calculator with Method Chaining
// https://leetcode.com/problems/calculator-with-method-chaining/

class Calculator {
    private $val;

    function __construct($value) {
        $this->val = $value;
    }

    function add($value) {
        $this->val += $value;
        return $this;
    }

    function subtract($value) {
        $this->val -= $value;
        return $this;
    }

    function multiply($value) {
        $this->val *= $value;
        return $this;
    }

    function divide($value) {
        if ($value === 0) throw new Exception("Division by zero is not allowed");
        $this->val /= $value;
        return $this;
    }

    function power($value) {
        $this->val = $this->val ** $value;
        return $this;
    }

    function getResult() {
        return $this->val;
    }
}

class Solution {
    function Calculator($actions = null, $values = null) {
        return new Calculator($values[0] ?? 0);
    }
}
''')

written = 0
for folder, body in SOLUTIONS.items():
    path = ROOT / folder / "solution.php"
    path.write_text(body, encoding="utf-8", newline="\n")
    written += 1
print(f"wrote {written}")

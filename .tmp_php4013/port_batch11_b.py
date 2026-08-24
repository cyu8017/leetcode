#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
SOLUTIONS = {}

def add(folder, body):
    SOLUTIONS[folder] = body


add("2773_height_of_special_binary_tree", r'''<?php
// LeetCode 2773 - Height of Special Binary Tree
// https://leetcode.com/problems/height-of-special-binary-tree/

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
    function heightOfTree($root) {
        if (!$root) return -1;
        return $this->dfs($root);
    }
    function dfs($node) {
        if (!$node) return -1;
        if ($node->left && $node->left->right === $node) return $this->dfs($node->right) + 1;
        if ($node->right && $node->right->left === $node) return $this->dfs($node->left) + 1;
        return max($this->dfs($node->left), $this->dfs($node->right)) + 1;
    }
}
''')

add("2774_array_upper_bound", r'''<?php
// LeetCode 2774 - Array Upper Bound
// https://leetcode.com/problems/array-upper-bound/

class Solution {
    function upperBound($nums, $target) {
        $lo = 0;
        $hi = count($nums);
        while ($lo < $hi) {
            $mid = ($lo + $hi) >> 1;
            if ($nums[$mid] <= $target) $lo = $mid + 1;
            else $hi = $mid;
        }
        if ($lo === 0 || $nums[$lo - 1] !== $target) return -1;
        return $lo - 1;
    }
}
''')

add("2775_undefined_to_null", r'''<?php
// LeetCode 2775 - Undefined to Null
// https://leetcode.com/problems/undefined-to-null/

class Solution {
    function undefinedToNull($obj) {
        if ($obj === null) return null;
        if (!is_array($obj) && !is_object($obj)) return $obj;
        if (is_object($obj)) $obj = (array)$obj;
        $isList = $obj === [] || array_keys($obj) === range(0, count($obj) - 1);
        if ($isList) {
            foreach ($obj as $i => $v) $obj[$i] = $this->undefinedToNull($v);
            return $obj;
        }
        foreach ($obj as $k => $v) $obj[$k] = $this->undefinedToNull($v);
        return $obj;
    }
}
''')

add("2776_convert_callback_based_function_to_promise_based_function", r'''<?php
// LeetCode 2776 - Convert Callback Based Function to Promise Based Function
// https://leetcode.com/problems/convert-callback-based-function-to-promise-based-function/

class Solution {
    function promisify($fn) {
        return function(...$args) use ($fn) {
            $err = null;
            $result = null;
            $fn(function($e, $r = null) use (&$err, &$result) {
                $err = $e;
                $result = $r;
            }, ...$args);
            if ($err) throw new Exception(is_string($err) ? $err : json_encode($err));
            return $result;
        };
    }
}
''')

add("2777_date_range_generator", r'''<?php
// LeetCode 2777 - Date Range Generator
// https://leetcode.com/problems/date-range-generator/

class Solution {
    function dateRangeGenerator($start, $end, $step) {
        $cur = new DateTime($start);
        $last = new DateTime($end);
        $out = [];
        while ($cur <= $last) {
            $out[] = $cur->format('Y-m-d');
            $cur->modify('+' . $step . ' day');
        }
        return $out;
    }
}
''')

add("2778_sum_of_squares_of_special_elements", r'''<?php
// LeetCode 2778 - Sum of Squares of Special Elements
// https://leetcode.com/problems/sum-of-squares-of-special-elements/

class Solution {
    function sumOfSquares($nums) {
        $n = count($nums);
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            if ($n % ($i + 1) === 0) $ans += $nums[$i] * $nums[$i];
        }
        return $ans;
    }
}
''')

add("2779_maximum_beauty_of_an_array_after_applying_operation", r'''<?php
// LeetCode 2779 - Maximum Beauty of an Array After Applying Operation
// https://leetcode.com/problems/maximum-beauty-of-an-array-after-applying-operation/

class Solution {
    function maximumBeauty($nums, $k) {
        sort($nums);
        $ans = 0;
        $left = 0;
        for ($right = 0; $right < count($nums); $right++) {
            while ($nums[$right] - $nums[$left] > 2 * $k) $left++;
            $ans = max($ans, $right - $left + 1);
        }
        return $ans;
    }
}
''')

add("2780_minimum_index_of_a_valid_split", r'''<?php
// LeetCode 2780 - Minimum Index of a Valid Split
// https://leetcode.com/problems/minimum-index-of-a-valid-split/

class Solution {
    function minimumIndex($nums) {
        $freq = [];
        $dom = 0;
        $best = 0;
        foreach ($nums as $v) {
            $c = ($freq[$v] ?? 0) + 1;
            $freq[$v] = $c;
            if ($c > $best) { $best = $c; $dom = $v; }
        }
        $left = 0;
        $n = count($nums);
        for ($i = 0; $i < $n - 1; $i++) {
            if ($nums[$i] === $dom) $left++;
            $right = $best - $left;
            if ($left * 2 > $i + 1 && $right * 2 > $n - $i - 1) return $i;
        }
        return -1;
    }
}
''')

add("2781_length_of_the_longest_valid_substring", r'''<?php
// LeetCode 2781 - Length of the Longest Valid Substring
// https://leetcode.com/problems/length-of-the-longest-valid-substring/

class Solution {
    function longestValidSubstring($word, $forbidden) {
        $forbid = array_fill_keys($forbidden, true);
        $maxLen = 0;
        foreach ($forbidden as $f) $maxLen = max($maxLen, strlen($f));
        $ans = 0;
        $n = strlen($word);
        $right = $n - 1;
        for ($left = $n - 1; $left >= 0; $left--) {
            for ($k = $left; $k <= $right && $k - $left + 1 <= $maxLen; $k++) {
                if (isset($forbid[substr($word, $left, $k - $left + 1)])) {
                    $right = $k - 1;
                    break;
                }
            }
            $ans = max($ans, $right - $left + 1);
        }
        return $ans;
    }
}
''')

add("2782_number_of_unique_categories", r'''<?php
// LeetCode 2782 - Number of Unique Categories
// https://leetcode.com/problems/number-of-unique-categories/

class CategoryHandler {
    public $cats;
    function __construct($cats) {
        $this->cats = $cats;
    }
    function haveSameCategory($a, $b) {
        return $this->cats[$a] === $this->cats[$b];
    }
}

class Solution {
    function numberOfCategories($n, $categoryHandler) {
        if (is_array($categoryHandler)) $categoryHandler = new CategoryHandler($categoryHandler);
        $parent = range(0, $n - 1);
        $find = function($x) use (&$parent, &$find) {
            while ($parent[$x] !== $x) {
                $parent[$x] = $parent[$parent[$x]];
                $x = $parent[$x];
            }
            return $x;
        };
        for ($i = 0; $i < $n; $i++) {
            for ($j = $i + 1; $j < $n; $j++) {
                if ($categoryHandler->haveSameCategory($i, $j)) {
                    $a = $find($i);
                    $b = $find($j);
                    if ($a !== $b) $parent[$a] = $b;
                }
            }
        }
        $ans = 0;
        for ($i = 0; $i < $n; $i++) if ($find($i) === $i) $ans++;
        return $ans;
    }
}
''')

add("2784_check_if_array_is_good", r'''<?php
// LeetCode 2784 - Check if Array is Good
// https://leetcode.com/problems/check-if-array-is-good/

class Solution {
    function isGood($nums) {
        $n = count($nums) - 1;
        if ($n < 1) return false;
        $freq = array_fill(0, $n + 1, 0);
        foreach ($nums as $v) {
            if ($v < 1 || $v > $n) return false;
            $freq[$v]++;
        }
        for ($i = 1; $i < $n; $i++) if ($freq[$i] !== 1) return false;
        return $freq[$n] === 2;
    }
}
''')

add("2785_sort_vowels_in_a_string", r'''<?php
// LeetCode 2785 - Sort Vowels in a String
// https://leetcode.com/problems/sort-vowels-in-a-string/

class Solution {
    function sortVowels($s) {
        $isVowel = function($c) { return strpos('aeiouAEIOU', $c) !== false; };
        $vowels = [];
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) if ($isVowel($s[$i])) $vowels[] = $s[$i];
        sort($vowels);
        $arr = str_split($s);
        $vi = 0;
        for ($i = 0; $i < count($arr); $i++) if ($isVowel($arr[$i])) $arr[$i] = $vowels[$vi++];
        return implode('', $arr);
    }
}
''')

add("2786_visit_array_positions_to_maximize_score", r'''<?php
// LeetCode 2786 - Visit Array Positions to Maximize Score
// https://leetcode.com/problems/visit-array-positions-to-maximize-score/

class Solution {
    function maxScore($nums, $x) {
        $NEG = -1000000000000000000;
        $even = $nums[0];
        $odd = $nums[0];
        if ($nums[0] % 2 === 0) $odd = $NEG;
        else $even = $NEG;
        for ($i = 1; $i < count($nums); $i++) {
            $v = $nums[$i];
            if ($nums[$i] % 2 === 0) $even = max($even + $v, $odd + $v - $x);
            else $odd = max($odd + $v, $even + $v - $x);
        }
        return max($even, $odd);
    }
}
''')

add("2787_ways_to_express_an_integer_as_sum_of_powers", r'''<?php
// LeetCode 2787 - Ways to Express an Integer as Sum of Powers
// https://leetcode.com/problems/ways-to-express-an-integer-as-sum-of-powers/

class Solution {
    function numberOfWays($n, $x) {
        $MOD = 1000000007;
        $powers = [];
        for ($i = 1; ; $i++) {
            $p = 1;
            for ($j = 0; $j < $x; $j++) {
                $p *= $i;
                if ($p > $n) break;
            }
            if ($p > $n) break;
            $powers[] = $p;
        }
        $dp = array_fill(0, $n + 1, 0);
        $dp[0] = 1;
        foreach ($powers as $p) {
            for ($s = $n; $s >= $p; $s--) $dp[$s] = ($dp[$s] + $dp[$s - $p]) % $MOD;
        }
        return $dp[$n];
    }
}
''')

add("2788_split_strings_by_separator", r'''<?php
// LeetCode 2788 - Split Strings by Separator
// https://leetcode.com/problems/split-strings-by-separator/

class Solution {
    function splitWordsBySeparator($words, $separator) {
        $ans = [];
        foreach ($words as $w) {
            $start = 0;
            $len = strlen($w);
            for ($i = 0; $i <= $len; $i++) {
                if ($i === $len || $w[$i] === $separator) {
                    if ($i > $start) $ans[] = substr($w, $start, $i - $start);
                    $start = $i + 1;
                }
            }
        }
        return $ans;
    }
}
''')

add("2789_largest_element_in_an_array_after_merge_operations", r'''<?php
// LeetCode 2789 - Largest Element in an Array after Merge Operations
// https://leetcode.com/problems/largest-element-in-an-array-after-merge-operations/

class Solution {
    function maxArrayValue($nums) {
        $n = count($nums);
        $cur = $nums[$n - 1];
        $ans = $cur;
        for ($i = $n - 2; $i >= 0; $i--) {
            if ($nums[$i] <= $cur) $cur += $nums[$i];
            else $cur = $nums[$i];
            $ans = max($ans, $cur);
        }
        return $ans;
    }
}
''')

add("2790_maximum_number_of_groups_with_increasing_length", r'''<?php
// LeetCode 2790 - Maximum Number of Groups With Increasing Length
// https://leetcode.com/problems/maximum-number-of-groups-with-increasing-length/

class Solution {
    function maxIncreasingGroups($usageLimits) {
        $arr = $usageLimits;
        sort($arr);
        $ans = 0;
        $sum = 0;
        foreach ($arr as $v) {
            $sum += $v;
            $need = intdiv(($ans + 1) * ($ans + 2), 2);
            if ($sum >= $need) $ans++;
        }
        return $ans;
    }
}
''')

add("2791_count_paths_that_can_form_a_palindrome_in_a_tree", r'''<?php
// LeetCode 2791 - Count Paths That Can Form a Palindrome in a Tree
// https://leetcode.com/problems/count-paths-that-can-form-a-palindrome-in-a-tree/

class Solution {
    public $g;
    public $s;
    public $freq;
    public $ans;
    function countPalindromePaths($parent, $s) {
        $n = count($parent);
        $this->g = array_fill(0, $n, []);
        for ($i = 1; $i < $n; $i++) $this->g[$parent[$i]][] = $i;
        $this->s = $s;
        $this->freq = [0 => 1];
        $this->ans = 0;
        $this->dfs(0, 0);
        return $this->ans;
    }
    function dfs($u, $mask) {
        foreach ($this->g[$u] as $v) {
            $nm = $mask ^ (1 << (ord($this->s[$v]) - 97));
            $this->ans += $this->freq[$nm] ?? 0;
            for ($b = 0; $b < 26; $b++) $this->ans += $this->freq[$nm ^ (1 << $b)] ?? 0;
            $this->freq[$nm] = ($this->freq[$nm] ?? 0) + 1;
            $this->dfs($v, $nm);
        }
    }
}
''')

add("2792_count_nodes_that_are_great_enough", r'''<?php
// LeetCode 2792 - Count Nodes That Are Great Enough
// https://leetcode.com/problems/count-nodes-that-are-great-enough/

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
    public $ans;
    public $k;
    function countGreatEnoughNodes($root, $k) {
        $this->ans = 0;
        $this->k = $k;
        $this->dfs($root);
        return $this->ans;
    }
    function dfs($node) {
        if (!$node) return [];
        $vals = array_merge([$node->val], $this->dfs($node->left), $this->dfs($node->right));
        $smaller = 0;
        foreach ($vals as $v) if ($v < $node->val) $smaller++;
        if ($smaller >= $this->k) $this->ans++;
        return $vals;
    }
}
''')

add("2794_create_object_from_two_arrays", r'''<?php
// LeetCode 2794 - Create Object from Two Arrays
// https://leetcode.com/problems/create-object-from-two-arrays/

class Solution {
    function createObject($keysArr, $valuesArr) {
        $output = [];
        $n = min(count($keysArr), count($valuesArr));
        for ($i = 0; $i < $n; $i++) {
            $k = is_bool($keysArr[$i]) ? ($keysArr[$i] ? 'true' : 'false') : (string)$keysArr[$i];
            if (!array_key_exists($k, $output)) $output[$k] = $valuesArr[$i];
        }
        return $output;
    }
}
''')

add("2795_parallel_execution_of_promises_for_individual_results_retrieval", r'''<?php
// LeetCode 2795 - Parallel Execution of Promises for Individual Results Retrieval
// https://leetcode.com/problems/parallel-execution-of-promises-for-individual-results-retrieval/

class Solution {
    function promiseAllSettled($functions) {
        $out = [];
        foreach ($functions as $fn) {
            try {
                $value = $fn();
                $out[] = ['status' => 'fulfilled', 'value' => $value];
            } catch (Throwable $e) {
                $out[] = ['status' => 'rejected', 'reason' => $e->getMessage()];
            }
        }
        return $out;
    }
}
''')

add("2796_repeat_string", r'''<?php
// LeetCode 2796 - Repeat String
// https://leetcode.com/problems/repeat-string/

class Solution {
    function replicate($str, $times) {
        $res = '';
        for ($i = 0; $i < $times; $i++) $res .= $str;
        return $res;
    }
}
''')

add("2797_partial_function_with_placeholders", r'''<?php
// LeetCode 2797 - Partial Function with Placeholders
// https://leetcode.com/problems/partial-function-with-placeholders/

class Solution {
    function partial($fn, $args) {
        return function(...$restArgs) use ($fn, $args) {
            $full = [];
            $ri = 0;
            foreach ($args as $a) {
                if ($a === '_') {
                    if ($ri < count($restArgs)) $full[] = $restArgs[$ri++];
                } else {
                    $full[] = $a;
                }
            }
            while ($ri < count($restArgs)) $full[] = $restArgs[$ri++];
            return $fn(...$full);
        };
    }
}
''')

add("2798_number_of_employees_who_met_the_target", r'''<?php
// LeetCode 2798 - Number of Employees Who Met the Target
// https://leetcode.com/problems/number-of-employees-who-met-the-target/

class Solution {
    function numberOfEmployeesWhoMetTarget($hours, $target) {
        $ans = 0;
        foreach ($hours as $h) if ($h >= $target) $ans++;
        return $ans;
    }
}
''')

add("2799_count_complete_subarrays_in_an_array", r'''<?php
// LeetCode 2799 - Count Complete Subarrays in an Array
// https://leetcode.com/problems/count-complete-subarrays-in-an-array/

class Solution {
    function countCompleteSubarrays($nums) {
        $need = count(array_unique($nums));
        $ans = 0;
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            $seen = [];
            for ($j = $i; $j < $n; $j++) {
                $seen[$nums[$j]] = true;
                if (count($seen) === $need) {
                    $ans += $n - $j;
                    break;
                }
            }
        }
        return $ans;
    }
}
''')

add("2800_shortest_string_that_contains_three_strings", r'''<?php
// LeetCode 2800 - Shortest String That Contains Three Strings
// https://leetcode.com/problems/shortest-string-that-contains-three-strings/

class Solution {
    function minimumString($a, $b, $c) {
        $merge = function($x, $y) {
            if (strpos($x, $y) !== false) return $x;
            $best = $x . $y;
            $n = min(strlen($x), strlen($y));
            for ($i = $n; $i > 0; $i--) {
                if (substr($x, -$i) === substr($y, 0, $i)) {
                    $cand = $x . substr($y, $i);
                    if (strlen($cand) < strlen($best) || (strlen($cand) === strlen($best) && $cand < $best)) $best = $cand;
                    break;
                }
            }
            return $best;
        };
        $perms = [[$a,$b,$c],[$a,$c,$b],[$b,$a,$c],[$b,$c,$a],[$c,$a,$b],[$c,$b,$a]];
        $ans = '';
        foreach ($perms as $p) {
            $cur = $merge($merge($p[0], $p[1]), $p[2]);
            if ($ans === '' || strlen($cur) < strlen($ans) || (strlen($cur) === strlen($ans) && $cur < $ans)) $ans = $cur;
        }
        return $ans;
    }
}
''')

add("2801_count_stepping_numbers_in_range", r'''<?php
// LeetCode 2801 - Count Stepping Numbers in Range
// https://leetcode.com/problems/count-stepping-numbers-in-range/

class Solution {
    public $s;
    public $memo;
    function countSteppingNumbers($low, $high) {
        $MOD = 1000000007;
        $dec = function($s) {
            $arr = str_split($s);
            $i = count($arr) - 1;
            while ($i >= 0 && $arr[$i] === '0') {
                $arr[$i] = '9';
                $i--;
            }
            if ($i >= 0) $arr[$i] = chr(ord($arr[$i]) - 1);
            $j = 0;
            while ($j < count($arr) - 1 && $arr[$j] === '0') $j++;
            return implode('', array_slice($arr, $j));
        };
        $ans = ($this->countTo($high) - $this->countTo($dec($low))) % $MOD;
        if ($ans < 0) $ans += $MOD;
        return $ans;
    }
    function countTo($s) {
        $this->s = $s;
        $this->memo = [];
        return $this->dfs(0, 1, -1, 0);
    }
    function dfs($pos, $tight, $last, $started) {
        $MOD = 1000000007;
        if ($pos === strlen($this->s)) return $started;
        $key = $pos . ',' . $tight . ',' . $last . ',' . $started;
        if (isset($this->memo[$key])) return $this->memo[$key];
        $up = $tight ? ord($this->s[$pos]) - 48 : 9;
        $ans = 0;
        for ($d = 0; $d <= $up; $d++) {
            $nt = ($tight && $d === $up) ? 1 : 0;
            if (!$started) {
                if ($d === 0) $ans += $this->dfs($pos + 1, $nt, -1, 0);
                else $ans += $this->dfs($pos + 1, $nt, $d, 1);
            } else if (abs($d - $last) === 1) {
                $ans += $this->dfs($pos + 1, $nt, $d, 1);
            }
        }
        return $this->memo[$key] = $ans % $MOD;
    }
}
''')

add("2802_find_the_k_th_lucky_number", r'''<?php
// LeetCode 2802 - Find The K-th Lucky Number
// https://leetcode.com/problems/find-the-k-th-lucky-number/

class Solution {
    function kthLuckyNumber($k) {
        $k++;
        $bits = '';
        while ($k > 1) {
            if ($k % 2 === 0) $bits = '4' . $bits;
            else $bits = '7' . $bits;
            $k = intdiv($k, 2);
        }
        return $bits;
    }
}
''')

add("2803_factorial_generator", r'''<?php
// LeetCode 2803 - Factorial Generator
// https://leetcode.com/problems/factorial-generator/

class Solution {
    function factorialGenerator($n) {
        $out = [];
        $cur = 1;
        if ($n === 0) return [1];
        for ($i = 1; $i <= $n; $i++) {
            $cur *= $i;
            $out[] = $cur;
        }
        return $out;
    }
}
''')

add("2804_array_prototype_foreach", r'''<?php
// LeetCode 2804 - Array Prototype ForEach
// https://leetcode.com/problems/array-prototype-foreach/

class Solution {
    function forEachOnArray($arr, $callback, $context = null) {
        $n = count($arr);
        for ($i = 0; $i < $n; $i++) {
            if (is_callable($callback)) $callback($arr[$i], $i, $arr, $context);
        }
        return $arr;
    }
}
''')

add("2805_custom_interval", r'''<?php
// LeetCode 2805 - Custom Interval
// https://leetcode.com/problems/custom-interval/

class Solution {
    public $nextId = 1;
    public $cancelled = [];
    function customInterval($fn, $delay = null, $period = null) {
        if (!is_callable($fn)) {
            $cancelTime = $period;
            $period = $delay;
            $delay = $fn;
            $times = [];
            $count = 0;
            $t = 0;
            while (true) {
                $t += $delay + $period * $count;
                if ($cancelTime !== null && $t >= $cancelTime) break;
                $times[] = $t;
                $count++;
                if ($count > 100000) break;
            }
            return $times;
        }
        $id = $this->nextId++;
        $this->cancelled[$id] = false;
        return $id;
    }
    function customClearInterval($id) {
        $this->cancelled[$id] = true;
    }
}
''')


def main():
    written = 0
    for folder, body in SOLUTIONS.items():
        path = ROOT / folder / "solution.php"
        path.write_text(body, encoding="utf-8", newline="\n")
        written += 1
        print("wrote", folder)
    print("B written", written)

if __name__ == "__main__":
    main()

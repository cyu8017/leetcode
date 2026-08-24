#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOLUTIONS: dict[str, str] = {}


def add(name: str, content: str) -> None:
    SOLUTIONS[name] = content.strip() + "\n"


TREE = r"""
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
"""

add("0980_unique_paths_iii", r"""<?php
// LeetCode 0980 - Unique Paths III
// https://leetcode.com/problems/unique-paths-iii/

class Solution {
    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function uniquePathsIII($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        $empty = 0;
        $sr = 0;
        $sc = 0;
        $ans = 0;
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if ($grid[$i][$j] !== -1) $empty++;
                if ($grid[$i][$j] === 1) { $sr = $i; $sc = $j; }
            }
        }
        $dfs = null;
        $dfs = function ($r, $c, $remain) use (&$dfs, &$grid, &$ans, $m, $n) {
            if ($grid[$r][$c] === 2) {
                if ($remain === 1) $ans++;
                return;
            }
            $temp = $grid[$r][$c];
            $grid[$r][$c] = -1;
            $dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];
            foreach ($dirs as $d) {
                $nr = $r + $d[0];
                $nc = $c + $d[1];
                if ($nr >= 0 && $nr < $m && $nc >= 0 && $nc < $n && $grid[$nr][$nc] !== -1)
                    $dfs($nr, $nc, $remain - 1);
            }
            $grid[$r][$c] = $temp;
        };
        $dfs($sr, $sc, $empty);
        return $ans;
    }
}
""")

add("0981_time_based_key_value_store", r"""<?php
// LeetCode 0981 - Time Based Key-Value Store
// https://leetcode.com/problems/time-based-key-value-store/

class TimeMap {
    private $times = [];
    private $vals = [];

    function __construct() {
        $this->times = [];
        $this->vals = [];
    }

    /**
     * @param String $key
     * @param String $value
     * @param Integer $timestamp
     * @return NULL
     */
    function set($key, $value, $timestamp) {
        if (!isset($this->times[$key])) {
            $this->times[$key] = [];
            $this->vals[$key] = [];
        }
        $this->times[$key][] = $timestamp;
        $this->vals[$key][] = $value;
    }

    /**
     * @param String $key
     * @param Integer $timestamp
     * @return String
     */
    function get($key, $timestamp) {
        if (!isset($this->times[$key])) return "";
        $tarr = $this->times[$key];
        $varr = $this->vals[$key];
        $lo = 0;
        $hi = count($tarr) - 1;
        $ans = -1;
        while ($lo <= $hi) {
            $mid = ($lo + $hi) >> 1;
            if ($tarr[$mid] <= $timestamp) { $ans = $mid; $lo = $mid + 1; }
            else $hi = $mid - 1;
        }
        return $ans < 0 ? "" : $varr[$ans];
    }
}
""")

add("0982_triples_with_bitwise_and_equal_to_zero", r"""<?php
// LeetCode 0982 - Triples with Bitwise AND Equal To Zero
// https://leetcode.com/problems/triples-with-bitwise-and-equal-to-zero/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function countTriplets($nums) {
        $cnt = [];
        foreach ($nums as $a) {
            foreach ($nums as $b) {
                $k = $a & $b;
                $cnt[$k] = ($cnt[$k] ?? 0) + 1;
            }
        }
        $ans = 0;
        foreach ($nums as $c) {
            foreach ($cnt as $k => $v) {
                if (($k & $c) === 0) $ans += $v;
            }
        }
        return $ans;
    }
}
""")

add("0983_minimum_cost_for_tickets", r"""<?php
// LeetCode 0983 - Minimum Cost For Tickets
// https://leetcode.com/problems/minimum-cost-for-tickets/

class Solution {
    /**
     * @param Integer[] $days
     * @param Integer[] $costs
     * @return Integer
     */
    function mincostTickets($days, $costs) {
        $dayset = array_flip($days);
        $last = $days[count($days) - 1];
        $dp = array_fill(0, $last + 1, 0);
        for ($d = 1; $d <= $last; $d++) {
            if (!isset($dayset[$d])) $dp[$d] = $dp[$d - 1];
            else {
                $dp[$d] = min(
                    $dp[$d - 1] + $costs[0],
                    $dp[max(0, $d - 7)] + $costs[1],
                    $dp[max(0, $d - 30)] + $costs[2]
                );
            }
        }
        return $dp[$last];
    }
}
""")

add("0984_string_without_aaa_or_bbb", r"""<?php
// LeetCode 0984 - String Without AAA or BBB
// https://leetcode.com/problems/string-without-aaa-or-bbb/

class Solution {
    /**
     * @param Integer $a
     * @param Integer $b
     * @return String
     */
    function strWithout3a3b($a, $b) {
        $ans = "";
        while ($a > 0 || $b > 0) {
            $len = strlen($ans);
            if ($len >= 2 && $ans[$len - 1] === $ans[$len - 2])
                $writeA = $ans[$len - 1] === 'b';
            else
                $writeA = $a >= $b;
            if ($writeA) { $ans .= 'a'; $a--; }
            else { $ans .= 'b'; $b--; }
        }
        return $ans;
    }
}
""")

add("0985_sum_of_even_numbers_after_queries", r"""<?php
// LeetCode 0985 - Sum of Even Numbers After Queries
// https://leetcode.com/problems/sum-of-even-numbers-after-queries/

class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer[][] $queries
     * @return Integer[]
     */
    function sumEvenAfterQueries($nums, $queries) {
        $even = 0;
        foreach ($nums as $x) if ($x % 2 === 0) $even += $x;
        $ans = [];
        foreach ($queries as $qi => $q) {
            $val = $q[0];
            $i = $q[1];
            if ($nums[$i] % 2 === 0) $even -= $nums[$i];
            $nums[$i] += $val;
            if ($nums[$i] % 2 === 0) $even += $nums[$i];
            $ans[$qi] = $even;
        }
        return $ans;
    }
}
""")

add("0986_interval_list_intersections", r"""<?php
// LeetCode 0986 - Interval List Intersections
// https://leetcode.com/problems/interval-list-intersections/

class Solution {
    /**
     * @param Integer[][] $firstList
     * @param Integer[][] $secondList
     * @return Integer[][]
     */
    function intervalIntersection($firstList, $secondList) {
        $i = 0;
        $j = 0;
        $ans = [];
        while ($i < count($firstList) && $j < count($secondList)) {
            $lo = max($firstList[$i][0], $secondList[$j][0]);
            $hi = min($firstList[$i][1], $secondList[$j][1]);
            if ($lo <= $hi) $ans[] = [$lo, $hi];
            if ($firstList[$i][1] < $secondList[$j][1]) $i++;
            else $j++;
        }
        return $ans;
    }
}
""")

add("0987_vertical_order_traversal_of_a_binary_tree", r"""<?php
// LeetCode 0987 - Vertical Order Traversal of a Binary Tree
// https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

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
    /**
     * @param TreeNode $root
     * @return Integer[][]
     */
    function verticalTraversal($root) {
        $nodes = [];
        $dfs = null;
        $dfs = function ($node, $row, $col) use (&$dfs, &$nodes) {
            if ($node === null) return;
            $nodes[] = [$col, $row, $node->val];
            $dfs($node->left, $row + 1, $col - 1);
            $dfs($node->right, $row + 1, $col + 1);
        };
        $dfs($root, 0, 0);
        usort($nodes, function ($a, $b) {
            if ($a[0] !== $b[0]) return $a[0] <=> $b[0];
            if ($a[1] !== $b[1]) return $a[1] <=> $b[1];
            return $a[2] <=> $b[2];
        });
        $byCol = [];
        foreach ($nodes as $t) {
            $byCol[$t[0]][] = $t[2];
        }
        ksort($byCol);
        return array_values($byCol);
    }
}
""")

add("0988_smallest_string_starting_from_leaf", r"""<?php
// LeetCode 0988 - Smallest String Starting From Leaf
// https://leetcode.com/problems/smallest-string-starting-from-leaf/

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
    /**
     * @param TreeNode $root
     * @return String
     */
    function smallestFromLeaf($root) {
        $best = "~";
        $dfs = null;
        $dfs = function ($node, $path) use (&$dfs, &$best) {
            if ($node === null) return;
            $path = chr(97 + $node->val) . $path;
            if ($node->left === null && $node->right === null) {
                if ($path < $best) $best = $path;
                return;
            }
            $dfs($node->left, $path);
            $dfs($node->right, $path);
        };
        $dfs($root, "");
        return $best;
    }
}
""")

add("0989_add_to_array_form_of_integer", r"""<?php
// LeetCode 0989 - Add to Array-Form of Integer
// https://leetcode.com/problems/add-to-array-form-of-integer/

class Solution {
    /**
     * @param Integer[] $num
     * @param Integer $k
     * @return Integer[]
     */
    function addToArrayForm($num, $k) {
        $list = $num;
        $i = count($list) - 1;
        while ($k > 0 || $i >= 0) {
            if ($i >= 0) {
                $k += $list[$i];
                $list[$i] = $k % 10;
                $i--;
            } else {
                array_unshift($list, $k % 10);
            }
            $k = intdiv($k, 10);
        }
        return $list;
    }
}
""")

add("0990_satisfiability_of_equality_equations", r"""<?php
// LeetCode 0990 - Satisfiability of Equality Equations
// https://leetcode.com/problems/satisfiability-of-equality-equations/

class Solution {
    /**
     * @param String[] $equations
     * @return Boolean
     */
    function equationsPossible($equations) {
        $parent = range(0, 25);
        $find = null;
        $find = function ($x) use (&$parent, &$find) {
            if ($parent[$x] !== $x) $parent[$x] = $find($parent[$x]);
            return $parent[$x];
        };
        foreach ($equations as $eq) {
            if ($eq[1] === '=') $parent[$find(ord($eq[0]) - 97)] = $find(ord($eq[3]) - 97);
        }
        foreach ($equations as $eq) {
            if ($eq[1] === '!' && $find(ord($eq[0]) - 97) === $find(ord($eq[3]) - 97)) return false;
        }
        return true;
    }
}
""")

add("0991_broken_calculator", r"""<?php
// LeetCode 0991 - Broken Calculator
// https://leetcode.com/problems/broken-calculator/

class Solution {
    /**
     * @param Integer $startValue
     * @param Integer $target
     * @return Integer
     */
    function brokenCalc($startValue, $target) {
        $ans = 0;
        while ($target > $startValue) {
            if ($target % 2 === 1) $target++;
            else $target = intdiv($target, 2);
            $ans++;
        }
        return $ans + $startValue - $target;
    }
}
""")

add("0992_subarrays_with_k_different_integers", r"""<?php
// LeetCode 0992 - Subarrays with K Different Integers
// https://leetcode.com/problems/subarrays-with-k-different-integers/

class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer
     */
    function subarraysWithKDistinct($nums, $k) {
        $atMost = function ($m) use ($nums) {
            if ($m < 0) return 0;
            $count = [];
            $left = 0;
            $ans = 0;
            $n = count($nums);
            for ($right = 0; $right < $n; $right++) {
                $count[$nums[$right]] = ($count[$nums[$right]] ?? 0) + 1;
                while (count($count) > $m) {
                    $v = $nums[$left++];
                    $count[$v]--;
                    if ($count[$v] === 0) unset($count[$v]);
                }
                $ans += $right - $left + 1;
            }
            return $ans;
        };
        return $atMost($k) - $atMost($k - 1);
    }
}
""")

add("0993_cousins_in_binary_tree", r"""<?php
// LeetCode 0993 - Cousins in Binary Tree
// https://leetcode.com/problems/cousins-in-binary-tree/

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
    /**
     * @param TreeNode $root
     * @param Integer $x
     * @param Integer $y
     * @return Boolean
     */
    function isCousins($root, $x, $y) {
        $depth = [];
        $parent = [];
        $dfs = null;
        $dfs = function ($node, $p, $d) use (&$dfs, &$depth, &$parent) {
            if ($node === null) return;
            $depth[$node->val] = $d;
            $parent[$node->val] = $p;
            $dfs($node->left, $node, $d + 1);
            $dfs($node->right, $node, $d + 1);
        };
        $dfs($root, null, 0);
        return ($depth[$x] ?? null) === ($depth[$y] ?? null) && ($parent[$x] ?? null) !== ($parent[$y] ?? null);
    }
}
""")

add("0994_rotting_oranges", r"""<?php
// LeetCode 0994 - Rotting Oranges
// https://leetcode.com/problems/rotting-oranges/

class Solution {
    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function orangesRotting($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        $q = [];
        $fresh = 0;
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if ($grid[$i][$j] === 2) $q[] = [$i, $j];
                else if ($grid[$i][$j] === 1) $fresh++;
            }
        }
        $minutes = 0;
        $dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];
        while ($q && $fresh > 0) {
            $sz = count($q);
            for ($s = 0; $s < $sz; $s++) {
                [$cr, $cc] = array_shift($q);
                foreach ($dirs as $d) {
                    $nr = $cr + $d[0];
                    $nc = $cc + $d[1];
                    if ($nr >= 0 && $nr < $m && $nc >= 0 && $nc < $n && $grid[$nr][$nc] === 1) {
                        $grid[$nr][$nc] = 2;
                        $fresh--;
                        $q[] = [$nr, $nc];
                    }
                }
            }
            $minutes++;
        }
        return $fresh === 0 ? $minutes : -1;
    }
}
""")

add("0995_minimum_number_of_k_consecutive_bit_flips", r"""<?php
// LeetCode 0995 - Minimum Number of K Consecutive Bit Flips
// https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/

class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer
     */
    function minKBitFlips($nums, $k) {
        $n = count($nums);
        $flip = array_fill(0, $n, 0);
        $ans = 0;
        $flipped = 0;
        for ($i = 0; $i < $n; $i++) {
            if ($i >= $k) $flipped ^= $flip[$i - $k];
            if ($nums[$i] === $flipped) {
                if ($i + $k > $n) return -1;
                $ans++;
                $flipped ^= 1;
                $flip[$i] = 1;
            }
        }
        return $ans;
    }
}
""")

add("0996_number_of_squareful_arrays", r"""<?php
// LeetCode 0996 - Number of Squareful Arrays
// https://leetcode.com/problems/number-of-squareful-arrays/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function numSquarefulPerms($nums) {
        $count = [];
        foreach ($nums as $x) $count[$x] = ($count[$x] ?? 0) + 1;
        $graph = [];
        foreach ($count as $a => $_) $graph[$a] = [];
        foreach ($count as $a => $_) {
            foreach ($count as $b => $__) {
                $s = $a + $b;
                $r = (int)round(sqrt($s));
                if ($r * $r === $s) $graph[$a][] = $b;
            }
        }
        $ans = 0;
        $dfs = null;
        $dfs = function ($x, $remain) use (&$dfs, &$count, &$graph, &$ans) {
            if ($remain === 0) { $ans++; return; }
            foreach ($graph[$x] as $y) {
                if (($count[$y] ?? 0) > 0) {
                    $count[$y]--;
                    $dfs($y, $remain - 1);
                    $count[$y]++;
                }
            }
        };
        foreach (array_keys($count) as $x) {
            $count[$x]--;
            $dfs($x, count($nums) - 1);
            $count[$x]++;
        }
        return $ans;
    }
}
""")

add("0997_find_the_town_judge", r"""<?php
// LeetCode 0997 - Find the Town Judge
// https://leetcode.com/problems/find-the-town-judge/

class Solution {
    /**
     * @param Integer $n
     * @param Integer[][] $trust
     * @return Integer
     */
    function findJudge($n, $trust) {
        $score = array_fill(0, $n + 1, 0);
        foreach ($trust as $t) {
            $score[$t[0]]--;
            $score[$t[1]]++;
        }
        for ($i = 1; $i <= $n; $i++) if ($score[$i] === $n - 1) return $i;
        return -1;
    }
}
""")

add("0998_maximum_binary_tree_ii", r"""<?php
// LeetCode 0998 - Maximum Binary Tree II
// https://leetcode.com/problems/maximum-binary-tree-ii/

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
    /**
     * @param TreeNode $root
     * @param Integer $val
     * @return TreeNode
     */
    function insertIntoMaxTree($root, $val) {
        if ($root === null || $val > $root->val) {
            $node = new TreeNode($val);
            $node->left = $root;
            return $node;
        }
        $root->right = $this->insertIntoMaxTree($root->right, $val);
        return $root;
    }
}
""")

add("0999_available_captures_for_rook", r"""<?php
// LeetCode 0999 - Available Captures for Rook
// https://leetcode.com/problems/available-captures-for-rook/

class Solution {
    /**
     * @param String[][] $board
     * @return Integer
     */
    function numRookCaptures($board) {
        $m = count($board);
        $n = count($board[0]);
        $r = -1;
        $c = -1;
        for ($i = 0; $i < $m; $i++)
            for ($j = 0; $j < $n; $j++)
                if ($board[$i][$j] === 'R') { $r = $i; $c = $j; }
        if ($r < 0) return 0;
        $ans = 0;
        $dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];
        foreach ($dirs as $d) {
            $i = $r + $d[0];
            $j = $c + $d[1];
            while ($i >= 0 && $i < $m && $j >= 0 && $j < $n) {
                if ($board[$i][$j] === 'B') break;
                if ($board[$i][$j] === 'p') { $ans++; break; }
                $i += $d[0];
                $j += $d[1];
            }
        }
        return $ans;
    }
}
""")

add("2000_reverse_prefix_of_word", r"""<?php
// LeetCode 2000 - Reverse Prefix of Word
// https://leetcode.com/problems/reverse-prefix-of-word/

class Solution {
    /**
     * @param String $word
     * @param String $ch
     * @return String
     */
    function reversePrefix($word, $ch) {
        $pos = strpos($word, $ch);
        if ($pos === false) return $word;
        $arr = str_split($word);
        for ($l = 0, $r = $pos; $l < $r; $l++, $r--) {
            $tmp = $arr[$l];
            $arr[$l] = $arr[$r];
            $arr[$r] = $tmp;
        }
        return implode('', $arr);
    }
}
""")

add("2001_number_of_pairs_of_interchangeable_rectangles", r"""<?php
// LeetCode 2001 - Number of Pairs of Interchangeable Rectangles
// https://leetcode.com/problems/number-of-pairs-of-interchangeable-rectangles/

class Solution {
    /**
     * @param Integer[][] $rectangles
     * @return Integer
     */
    function interchangeableRectangles($rectangles) {
        $gcd = function ($a, $b) {
            while ($b !== 0) { $t = $a % $b; $a = $b; $b = $t; }
            return $a;
        };
        $freq = [];
        $ans = 0;
        foreach ($rectangles as $rect) {
            $g = $gcd($rect[0], $rect[1]);
            $key = intdiv($rect[0], $g) . "/" . intdiv($rect[1], $g);
            $f = $freq[$key] ?? 0;
            $ans += $f;
            $freq[$key] = $f + 1;
        }
        return $ans;
    }
}
""")

add("2002_maximum_product_of_the_length_of_two_palindromic_subsequences", r"""<?php
// LeetCode 2002 - Maximum Product of the Length of Two Palindromic Subsequences
// https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-subsequences/

class Solution {
    /**
     * @param String $s
     * @return Integer
     */
    function maxProduct($s) {
        $n = strlen($s);
        $palLen = function ($mask) use ($s, $n) {
            $chars = "";
            for ($i = 0; $i < $n; $i++)
                if (($mask & (1 << $i)) !== 0) $chars .= $s[$i];
            for ($l = 0, $r = strlen($chars) - 1; $l < $r; $l++, $r--)
                if ($chars[$l] !== $chars[$r]) return 0;
            return strlen($chars);
        };
        $best = 0;
        $total = 1 << $n;
        for ($mask1 = 1; $mask1 < $total; $mask1++) {
            $len1 = $palLen($mask1);
            if ($len1 === 0) continue;
            $remain = ($total - 1) ^ $mask1;
            for ($mask2 = $remain; $mask2 > 0; $mask2 = ($mask2 - 1) & $remain) {
                $len2 = $palLen($mask2);
                if ($len2 > 0 && $len1 * $len2 > $best) $best = $len1 * $len2;
            }
        }
        return $best;
    }
}
""")

add("2003_smallest_missing_genetic_value_in_each_subtree", r"""<?php
// LeetCode 2003 - Smallest Missing Genetic Value in Each Subtree
// https://leetcode.com/problems/smallest-missing-genetic-value-in-each-subtree/

class Solution {
    /**
     * @param Integer[] $parents
     * @param Integer[] $nums
     * @return Integer[]
     */
    function smallestMissingValueSubtree($parents, $nums) {
        $n = count($parents);
        $children = array_fill(0, $n, []);
        for ($i = 1; $i < $n; $i++) $children[$parents[$i]][] = $i;
        $ans = array_fill(0, $n, 1);
        $one = -1;
        for ($i = 0; $i < $n; $i++) if ($nums[$i] === 1) { $one = $i; break; }
        if ($one < 0) return $ans;
        $seen = [];
        $collect = null;
        $collect = function ($u) use (&$collect, &$seen, &$children, $nums) {
            if (isset($seen[$nums[$u]])) return;
            $seen[$nums[$u]] = true;
            foreach ($children[$u] as $v) $collect($v);
        };
        $miss = 1;
        $node = $one;
        $prev = -1;
        while ($node !== -1) {
            foreach ($children[$node] as $v) if ($v !== $prev) $collect($v);
            $seen[$nums[$node]] = true;
            while (isset($seen[$miss])) $miss++;
            $ans[$node] = $miss;
            $prev = $node;
            $node = $parents[$node];
        }
        return $ans;
    }
}
""")

add("2005_subtree_removal_game_with_fibonacci_tree", r"""<?php
// LeetCode 2005 - Subtree Removal Game with Fibonacci Tree
// https://leetcode.com/problems/subtree-removal-game-with-fibonacci-tree/

class Solution {
    /**
     * @param Integer $n
     * @return Boolean
     */
    function findGameWinner($n) {
        return $n % 6 !== 1;
    }
}
""")

add("2006_count_number_of_pairs_with_absolute_difference_k", r"""<?php
// LeetCode 2006 - Count Number of Pairs With Absolute Difference K
// https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/

class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer
     */
    function countKDifference($nums, $k) {
        $freq = [];
        $ans = 0;
        foreach ($nums as $x) {
            $ans += $freq[$x - $k] ?? 0;
            $ans += $freq[$x + $k] ?? 0;
            $freq[$x] = ($freq[$x] ?? 0) + 1;
        }
        return $ans;
    }
}
""")

add("2007_find_original_array_from_doubled_array", r"""<?php
// LeetCode 2007 - Find Original Array From Doubled Array
// https://leetcode.com/problems/find-original-array-from-doubled-array/

class Solution {
    /**
     * @param Integer[] $changed
     * @return Integer[]
     */
    function findOriginalArray($changed) {
        if (count($changed) % 2 !== 0) return [];
        sort($changed);
        $freq = [];
        foreach ($changed as $x) $freq[$x] = ($freq[$x] ?? 0) + 1;
        $ans = [];
        foreach ($changed as $x) {
            if (($freq[$x] ?? 0) === 0) continue;
            $freq[$x]--;
            if (($freq[2 * $x] ?? 0) === 0) return [];
            $freq[2 * $x]--;
            $ans[] = $x;
        }
        return $ans;
    }
}
""")

add("2008_maximum_earnings_from_taxi", r"""<?php
// LeetCode 2008 - Maximum Earnings From Taxi
// https://leetcode.com/problems/maximum-earnings-from-taxi/

class Solution {
    /**
     * @param Integer $n
     * @param Integer[][] $rides
     * @return Integer
     */
    function maxTaxiEarnings($n, $rides) {
        usort($rides, fn($a, $b) => $a[1] <=> $b[1]);
        $m = count($rides);
        $ends = array_map(fn($r) => $r[1], $rides);
        $dp = array_fill(0, $m + 1, 0);
        for ($i = 0; $i < $m; $i++) {
            [$start, $end, $tip] = $rides[$i];
            $earn = $end - $start + $tip;
            $lo = 0;
            $hi = $m;
            while ($lo < $hi) {
                $mid = ($lo + $hi) >> 1;
                if ($ends[$mid] <= $start) $lo = $mid + 1;
                else $hi = $mid;
            }
            $dp[$i + 1] = max($dp[$i], $earn + $dp[$lo]);
        }
        return $dp[$m];
    }
}
""")

add("2009_minimum_number_of_operations_to_make_array_continuous", r"""<?php
// LeetCode 2009 - Minimum Number of Operations to Make Array Continuous
// https://leetcode.com/problems/minimum-number-of-operations-to-make-array-continuous/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function minOperations($nums) {
        $n = count($nums);
        $uniq = array_values(array_unique($nums));
        sort($uniq);
        $ans = $n;
        $j = 0;
        $un = count($uniq);
        for ($i = 0; $i < $un; $i++) {
            while ($j < $un && $uniq[$j] - $uniq[$i] + 1 <= $n) $j++;
            $ans = min($ans, $n - ($j - $i));
        }
        return $ans;
    }
}
""")


def main() -> None:
    ported = 0
    for folder, content in SOLUTIONS.items():
        path = ROOT / folder / "solution.php"
        path.write_text(content, encoding="utf-8", newline="\n")
        ported += 1
        print(f"ported {folder}")
    print(f"ported={ported}")


if __name__ == "__main__":
    main()

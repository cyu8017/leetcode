#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
SOLUTIONS: dict[str, str] = {}


def add(name: str, content: str) -> None:
    SOLUTIONS[name] = content.strip() + "\n"


add("0855_exam_room", r"""<?php
// LeetCode 0855 - Exam Room
// https://leetcode.com/problems/exam-room/

class ExamRoom {
    public $n;
    public $seats;

    /**
     * @param Integer $n
     */
    function __construct($n) {
        $this->n = $n;
        $this->seats = [];
    }

    /**
     * @return Integer
     */
    function seat() {
        if (!count($this->seats)) {
            $this->seats[] = 0;
            return 0;
        }
        $bestSeat = 0;
        $bestDist = $this->seats[0];
        $prev = $this->seats[0];
        foreach ($this->seats as $cur) {
            if ($cur === $prev) continue;
            $dist = intdiv($cur - $prev, 2);
            if ($dist > $bestDist) {
                $bestDist = $dist;
                $bestSeat = $prev + $dist;
            }
            $prev = $cur;
        }
        if ($this->n - 1 - $this->seats[count($this->seats) - 1] > $bestDist) $bestSeat = $this->n - 1;
        $this->seats[] = $bestSeat;
        sort($this->seats);
        return $bestSeat;
    }

    /**
     * @param Integer $p
     * @return NULL
     */
    function leave($p) {
        $idx = array_search($p, $this->seats, true);
        if ($idx !== false) array_splice($this->seats, $idx, 1);
    }
}
""")

add("0856_score_of_parentheses", r"""<?php
// LeetCode 0856 - Score of Parentheses
// https://leetcode.com/problems/score-of-parentheses/

class Solution {
    /**
     * @param String $s
     * @return Integer
     */
    function scoreOfParentheses($s) {
        $stack = [0];
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            if ($s[$i] === '(') $stack[] = 0;
            else {
                $val = array_pop($stack);
                $stack[] = array_pop($stack) + max(2 * $val, 1);
            }
        }
        return $stack[count($stack) - 1];
    }
}
""")

add("0857_minimum_cost_to_hire_k_workers", r"""<?php
// LeetCode 0857 - Minimum Cost to Hire K Workers
// https://leetcode.com/problems/minimum-cost-to-hire-k-workers/

class Solution {
    /**
     * @param Integer[] $quality
     * @param Integer[] $wage
     * @param Integer $k
     * @return Float
     */
    function mincostToHireWorkers($quality, $wage, $k) {
        $n = count($quality);
        $workers = [];
        for ($i = 0; $i < $n; $i++) $workers[] = [$wage[$i] / $quality[$i], $quality[$i]];
        usort($workers, function($a, $b) { return $a[0] <=> $b[0]; });
        $heap = [];
        $push = function($q) use (&$heap) {
            $heap[] = $q;
            $i = count($heap) - 1;
            while ($i > 0) {
                $p = ($i - 1) >> 1;
                if ($heap[$i] <= $heap[$p]) break;
                $tmp = $heap[$i];
                $heap[$i] = $heap[$p];
                $heap[$p] = $tmp;
                $i = $p;
            }
        };
        $pop = function() use (&$heap) {
            $top = $heap[0];
            $last = array_pop($heap);
            if (count($heap)) {
                $heap[0] = $last;
                $i = 0;
                while (true) {
                    $largest = $i;
                    $l = $i * 2 + 1;
                    $r = $i * 2 + 2;
                    if ($l < count($heap) && $heap[$l] > $heap[$largest]) $largest = $l;
                    if ($r < count($heap) && $heap[$r] > $heap[$largest]) $largest = $r;
                    if ($largest === $i) break;
                    $tmp = $heap[$i];
                    $heap[$i] = $heap[$largest];
                    $heap[$largest] = $tmp;
                    $i = $largest;
                }
            }
            return $top;
        };
        $totalQ = 0;
        $ans = INF;
        foreach ($workers as $w) {
            $ratio = $w[0];
            $q = $w[1];
            $push($q);
            $totalQ += $q;
            if (count($heap) > $k) $totalQ -= $pop();
            if (count($heap) === $k) $ans = min($ans, $totalQ * $ratio);
        }
        return $ans;
    }
}
""")

add("0858_mirror_reflection", r"""<?php
// LeetCode 0858 - Mirror Reflection
// https://leetcode.com/problems/mirror-reflection/

class Solution {
    /**
     * @param Integer $p
     * @param Integer $q
     * @return Integer
     */
    function mirrorReflection($p, $q) {
        $gcd = function($a, $b) {
            while ($b !== 0) {
                $t = $a % $b;
                $a = $b;
                $b = $t;
            }
            return $a;
        };
        $g = $gcd($p, $q);
        $p = intdiv($p, $g);
        $q = intdiv($q, $g);
        if ($p % 2 === 0) return 2;
        if ($q % 2 === 0) return 0;
        return 1;
    }
}
""")

add("0859_buddy_strings", r"""<?php
// LeetCode 0859 - Buddy Strings
// https://leetcode.com/problems/buddy-strings/

class Solution {
    /**
     * @param String $s
     * @param String $goal
     * @return Boolean
     */
    function buddyStrings($s, $goal) {
        if (strlen($s) !== strlen($goal)) return false;
        if ($s === $goal) {
            $set = [];
            $n = strlen($s);
            for ($i = 0; $i < $n; $i++) {
                $ch = $s[$i];
                if (isset($set[$ch])) return true;
                $set[$ch] = true;
            }
            return false;
        }
        $diffs = [];
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            if ($s[$i] !== $goal[$i]) $diffs[] = [$s[$i], $goal[$i]];
        }
        return count($diffs) === 2 && $diffs[0][0] === $diffs[1][1] && $diffs[0][1] === $diffs[1][0];
    }
}
""")

add("0860_lemonade_change", r"""<?php
// LeetCode 0860 - Lemonade Change
// https://leetcode.com/problems/lemonade-change/

class Solution {
    /**
     * @param Integer[] $bills
     * @return Boolean
     */
    function lemonadeChange($bills) {
        $fives = 0;
        $tens = 0;
        foreach ($bills as $bill) {
            if ($bill === 5) $fives++;
            elseif ($bill === 10) {
                if ($fives === 0) return false;
                $fives--;
                $tens++;
            } else {
                if ($tens > 0 && $fives > 0) { $tens--; $fives--; }
                elseif ($fives >= 3) $fives -= 3;
                else return false;
            }
        }
        return true;
    }
}
""")

add("0861_score_after_flipping_matrix", r"""<?php
// LeetCode 0861 - Score After Flipping Matrix
// https://leetcode.com/problems/score-after-flipping-matrix/

class Solution {
    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function matrixScore($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        for ($i = 0; $i < $m; $i++) {
            if ($grid[$i][0] === 0) {
                for ($j = 0; $j < $n; $j++) $grid[$i][$j] ^= 1;
            }
        }
        $ans = $m * (1 << ($n - 1));
        for ($j = 1; $j < $n; $j++) {
            $ones = 0;
            for ($i = 0; $i < $m; $i++) $ones += $grid[$i][$j];
            $ans += max($ones, $m - $ones) * (1 << ($n - 1 - $j));
        }
        return $ans;
    }
}
""")

add("0862_shortest_subarray_with_sum_at_least_k", r"""<?php
// LeetCode 0862 - Shortest Subarray with Sum at Least K
// https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/

class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer
     */
    function shortestSubarray($nums, $k) {
        $n = count($nums);
        $prefix = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; $i++) $prefix[$i + 1] = $prefix[$i] + $nums[$i];
        $dq = [];
        $ans = $n + 1;
        for ($i = 0; $i <= $n; $i++) {
            while (count($dq) && $prefix[$i] - $prefix[$dq[0]] >= $k) {
                $ans = min($ans, $i - array_shift($dq));
            }
            while (count($dq) && $prefix[$i] <= $prefix[$dq[count($dq) - 1]]) array_pop($dq);
            $dq[] = $i;
        }
        return $ans <= $n ? $ans : -1;
    }
}
""")

add("0863_all_nodes_distance_k_in_binary_tree", r"""<?php
// LeetCode 0863 - All Nodes Distance K in Binary Tree
// https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

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
     * @param TreeNode $target
     * @param Integer $k
     * @return Integer[]
     */
    function distanceK($root, $target, $k) {
        $graph = [];
        $add = function($a, $b) use (&$graph) {
            $ida = spl_object_id($a);
            if (!isset($graph[$ida])) $graph[$ida] = [];
            $graph[$ida][] = $b;
        };
        $build = function($node, $parent) use (&$build, $add) {
            if ($node === null) return;
            if ($parent !== null) {
                $add($node, $parent);
                $add($parent, $node);
            }
            $build($node->left, $node);
            $build($node->right, $node);
        };
        $build($root, null);
        $queue = [$target];
        $seen = [spl_object_id($target) => true];
        $dist = 0;
        $qi = 0;
        while ($qi < count($queue)) {
            if ($dist === $k) {
                $vals = [];
                for ($j = $qi; $j < count($queue); $j++) $vals[] = $queue[$j]->val;
                return $vals;
            }
            $size = count($queue) - $qi;
            for ($i = 0; $i < $size; $i++) {
                $node = $queue[$qi++];
                foreach ($graph[spl_object_id($node)] ?? [] as $nei) {
                    $id = spl_object_id($nei);
                    if (!isset($seen[$id])) {
                        $seen[$id] = true;
                        $queue[] = $nei;
                    }
                }
            }
            $dist++;
        }
        return [];
    }
}
""")

add("0864_shortest_path_to_get_all_keys", r"""<?php
// LeetCode 0864 - Shortest Path to Get All Keys
// https://leetcode.com/problems/shortest-path-to-get-all-keys/

class Solution {
    /**
     * @param String[] $grid
     * @return Integer
     */
    function shortestPathAllKeys($grid) {
        $m = count($grid);
        $n = strlen($grid[0]);
        $allKeys = 0;
        $sr = 0;
        $sc = 0;
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                $ch = $grid[$i][$j];
                if ($ch === '@') { $sr = $i; $sc = $j; }
                elseif ($ch >= 'a' && $ch <= 'f') $allKeys |= 1 << (ord($ch) - 97);
            }
        }
        $encode = function($r, $c, $mask) {
            return ($r << 20) | ($c << 10) | $mask;
        };
        $queue = [[$sr, $sc, 0, 0]];
        $seen = [$encode($sr, $sc, 0) => true];
        $dr = [1, -1, 0, 0];
        $dc = [0, 0, 1, -1];
        $qi = 0;
        while ($qi < count($queue)) {
            $r = $queue[$qi][0];
            $c = $queue[$qi][1];
            $mask = $queue[$qi][2];
            $dist = $queue[$qi][3];
            $qi++;
            if ($mask === $allKeys) return $dist;
            for ($k = 0; $k < 4; $k++) {
                $nr = $r + $dr[$k];
                $nc = $c + $dc[$k];
                if ($nr < 0 || $nr >= $m || $nc < 0 || $nc >= $n || $grid[$nr][$nc] === '#') continue;
                $cell = $grid[$nr][$nc];
                $nmask = $mask;
                if ($cell >= 'a' && $cell <= 'f') $nmask |= 1 << (ord($cell) - 97);
                if ($cell >= 'A' && $cell <= 'F' && ($mask & (1 << (ord($cell) - 65))) === 0) continue;
                $key = $encode($nr, $nc, $nmask);
                if (!isset($seen[$key])) {
                    $seen[$key] = true;
                    $queue[] = [$nr, $nc, $nmask, $dist + 1];
                }
            }
        }
        return -1;
    }
}
""")

add("0865_smallest_subtree_with_all_the_deepest_nodes", r"""<?php
// LeetCode 0865 - Smallest Subtree with all the Deepest Nodes
// https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/

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
     * @return TreeNode
     */
    function subtreeWithAllDeepest($root) {
        $dfs = function($node) use (&$dfs) {
            if ($node === null) return [0, null];
            $left = $dfs($node->left);
            $right = $dfs($node->right);
            if ($left[0] > $right[0]) return [$left[0] + 1, $left[1]];
            if ($right[0] > $left[0]) return [$right[0] + 1, $right[1]];
            return [$left[0] + 1, $node];
        };
        return $dfs($root)[1];
    }
}
""")

add("0866_prime_palindrome", r"""<?php
// LeetCode 0866 - Prime Palindrome
// https://leetcode.com/problems/prime-palindrome/

class Solution {
    /**
     * @param Integer $n
     * @return Integer
     */
    function primePalindrome($n) {
        if ($n <= 2) return 2;
        if ($n <= 3) return 3;
        if ($n <= 5) return 5;
        if ($n <= 7) return 7;
        if ($n <= 11) return 11;
        $isPrime = function($x) {
            if ($x < 2) return false;
            if ($x % 2 === 0) return $x === 2;
            for ($d = 3; $d * $d <= $x; $d += 2) if ($x % $d === 0) return false;
            return true;
        };
        for ($length = 1; $length <= 5; $length++) {
            $start = (int)pow(10, $length - 1);
            $end = (int)pow(10, $length);
            for ($root = $start; $root < $end; $root++) {
                $s = (string)$root;
                $pal = $s;
                for ($i = strlen($s) - 2; $i >= 0; $i--) $pal .= $s[$i];
                $val = intval($pal);
                if ($val >= $n && $isPrime($val)) return $val;
            }
        }
        return 0;
    }
}
""")

add("0867_transpose_matrix", r"""<?php
// LeetCode 0867 - Transpose Matrix
// https://leetcode.com/problems/transpose-matrix/

class Solution {
    /**
     * @param Integer[][] $matrix
     * @return Integer[][]
     */
    function transpose($matrix) {
        $m = count($matrix);
        $n = count($matrix[0]);
        $ans = array_fill(0, $n, array_fill(0, $m, 0));
        for ($i = 0; $i < $m; $i++) for ($j = 0; $j < $n; $j++) $ans[$j][$i] = $matrix[$i][$j];
        return $ans;
    }
}
""")

add("0868_binary_gap", r"""<?php
// LeetCode 0868 - Binary Gap
// https://leetcode.com/problems/binary-gap/

class Solution {
    /**
     * @param Integer $n
     * @return Integer
     */
    function binaryGap($n) {
        $last = -1;
        $ans = 0;
        $bit = 0;
        while ($n !== 0) {
            if (($n & 1) === 1) {
                if ($last !== -1) $ans = max($ans, $bit - $last);
                $last = $bit;
            }
            $n >>= 1;
            $bit++;
        }
        return $ans;
    }
}
""")

add("0869_reordered_power_of_2", r"""<?php
// LeetCode 0869 - Reordered Power of 2
// https://leetcode.com/problems/reordered-power-of-2/

class Solution {
    /**
     * @param Integer $n
     * @return Boolean
     */
    function reorderedPowerOf2($n) {
        $sig = function($x) {
            $chars = str_split((string)$x);
            sort($chars);
            return implode('', $chars);
        };
        $target = $sig($n);
        for ($i = 0; $i < 31; $i++) if ($sig(1 << $i) === $target) return true;
        return false;
    }
}
""")

add("0870_advantage_shuffle", r"""<?php
// LeetCode 0870 - Advantage Shuffle
// https://leetcode.com/problems/advantage-shuffle/

class Solution {
    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @return Integer[]
     */
    function advantageCount($nums1, $nums2) {
        $dq = $nums1;
        sort($dq);
        $lo = 0;
        $hi = count($dq) - 1;
        $ans = array_fill(0, count($nums1), 0);
        $indexed = [];
        $n = count($nums2);
        for ($i = 0; $i < $n; $i++) $indexed[] = [$nums2[$i], $i];
        usort($indexed, function($a, $b) { return $b[0] <=> $a[0]; });
        foreach ($indexed as $item) {
            $val = $item[0];
            $i = $item[1];
            if ($dq[$hi] > $val) $ans[$i] = $dq[$hi--];
            else $ans[$i] = $dq[$lo++];
        }
        return $ans;
    }
}
""")

add("0871_minimum_number_of_refueling_stops", r"""<?php
// LeetCode 0871 - Minimum Number of Refueling Stops
// https://leetcode.com/problems/minimum-number-of-refueling-stops/

class Solution {
    /**
     * @param Integer $target
     * @param Integer $startFuel
     * @param Integer[][] $stations
     * @return Integer
     */
    function minRefuelStops($target, $startFuel, $stations) {
        $pq = [];
        $push = function($gas) use (&$pq) {
            $pq[] = $gas;
            $i = count($pq) - 1;
            while ($i > 0) {
                $p = ($i - 1) >> 1;
                if ($pq[$i] <= $pq[$p]) break;
                $tmp = $pq[$i];
                $pq[$i] = $pq[$p];
                $pq[$p] = $tmp;
                $i = $p;
            }
        };
        $pop = function() use (&$pq) {
            $top = $pq[0];
            $last = array_pop($pq);
            if (count($pq)) {
                $pq[0] = $last;
                $i = 0;
                while (true) {
                    $largest = $i;
                    $l = $i * 2 + 1;
                    $r = $i * 2 + 2;
                    if ($l < count($pq) && $pq[$l] > $pq[$largest]) $largest = $l;
                    if ($r < count($pq) && $pq[$r] > $pq[$largest]) $largest = $r;
                    if ($largest === $i) break;
                    $tmp = $pq[$i];
                    $pq[$i] = $pq[$largest];
                    $pq[$largest] = $tmp;
                    $i = $largest;
                }
            }
            return $top;
        };
        $all = $stations;
        $all[] = [$target, 0];
        $ans = 0;
        $prev = 0;
        $fuel = $startFuel;
        foreach ($all as $st) {
            $pos = $st[0];
            $gas = $st[1];
            $fuel -= $pos - $prev;
            while (count($pq) && $fuel < 0) {
                $fuel += $pop();
                $ans++;
            }
            if ($fuel < 0) return -1;
            $push($gas);
            $prev = $pos;
        }
        return $ans;
    }
}
""")

add("0872_leaf_similar_trees", r"""<?php
// LeetCode 0872 - Leaf-Similar Trees
// https://leetcode.com/problems/leaf-similar-trees/

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
     * @param TreeNode $root1
     * @param TreeNode $root2
     * @return Boolean
     */
    function leafSimilar($root1, $root2) {
        $leaves = function($node) {
            $result = [];
            $dfs = function($cur) use (&$dfs, &$result) {
                if ($cur === null) return;
                if ($cur->left === null && $cur->right === null) {
                    $result[] = $cur->val;
                    return;
                }
                $dfs($cur->left);
                $dfs($cur->right);
            };
            $dfs($node);
            return $result;
        };
        $a = $leaves($root1);
        $b = $leaves($root2);
        if (count($a) !== count($b)) return false;
        $n = count($a);
        for ($i = 0; $i < $n; $i++) if ($a[$i] !== $b[$i]) return false;
        return true;
    }
}
""")

add("0873_length_of_longest_fibonacci_subsequence", r"""<?php
// LeetCode 0873 - Length of Longest Fibonacci Subsequence
// https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/

class Solution {
    /**
     * @param Integer[] $arr
     * @return Integer
     */
    function lenLongestFibSubseq($arr) {
        $n = count($arr);
        $index = [];
        for ($i = 0; $i < $n; $i++) $index[$arr[$i]] = $i;
        $dp = array_fill(0, $n, array_fill(0, $n, 2));
        $ans = 0;
        for ($j = 0; $j < $n; $j++) {
            for ($i = 0; $i < $j; $i++) {
                $need = $arr[$j] - $arr[$i];
                if (isset($index[$need])) {
                    $k = $index[$need];
                    if ($k < $i) {
                        $dp[$i][$j] = $dp[$k][$i] + 1;
                        $ans = max($ans, $dp[$i][$j]);
                    }
                }
            }
        }
        return $ans >= 3 ? $ans : 0;
    }
}
""")

add("0874_walking_robot_simulation", r"""<?php
// LeetCode 0874 - Walking Robot Simulation
// https://leetcode.com/problems/walking-robot-simulation/

class Solution {
    /**
     * @param Integer[] $commands
     * @param Integer[][] $obstacles
     * @return Integer
     */
    function robotSim($commands, $obstacles) {
        $encode = function($x, $y) {
            return (($x + 30000) << 20) | ($y + 30000);
        };
        $blocked = [];
        foreach ($obstacles as $o) $blocked[$encode($o[0], $o[1])] = true;
        $dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]];
        $x = 0;
        $y = 0;
        $d = 0;
        $best = 0;
        foreach ($commands as $cmd) {
            if ($cmd === -1) $d = ($d + 1) % 4;
            elseif ($cmd === -2) $d = ($d + 3) % 4;
            else {
                $dx = $dirs[$d][0];
                $dy = $dirs[$d][1];
                for ($step = 0; $step < $cmd; $step++) {
                    $nx = $x + $dx;
                    $ny = $y + $dy;
                    if (isset($blocked[$encode($nx, $ny)])) break;
                    $x = $nx;
                    $y = $ny;
                }
                $best = max($best, $x * $x + $y * $y);
            }
        }
        return $best;
    }
}
""")

add("0875_koko_eating_bananas", r"""<?php
// LeetCode 0875 - Koko Eating Bananas
// https://leetcode.com/problems/koko-eating-bananas/

class Solution {
    /**
     * @param Integer[] $piles
     * @param Integer $h
     * @return Integer
     */
    function minEatingSpeed($piles, $h) {
        $lo = 1;
        $hi = 0;
        foreach ($piles as $p) $hi = max($hi, $p);
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi, 2);
            $hours = 0;
            foreach ($piles as $p) $hours += intdiv($p + $mid - 1, $mid);
            if ($hours <= $h) $hi = $mid;
            else $lo = $mid + 1;
        }
        return $lo;
    }
}
""")

add("0876_middle_of_the_linked_list", r"""<?php
// LeetCode 0876 - Middle of the Linked List
// https://leetcode.com/problems/middle-of-the-linked-list/

class ListNode {
    public $val = 0;
    public $next = null;
    function __construct($val = 0, $next = null) {
        $this->val = $val;
        $this->next = $next;
    }
}

class Solution {
    /**
     * @param ListNode $head
     * @return ListNode
     */
    function middleNode($head) {
        $slow = $head;
        $fast = $head;
        while ($fast !== null && $fast->next !== null) {
            $slow = $slow->next;
            $fast = $fast->next->next;
        }
        return $slow;
    }
}
""")

add("0877_stone_game", r"""<?php
// LeetCode 0877 - Stone Game
// https://leetcode.com/problems/stone-game/

class Solution {
    /**
     * @param Integer[] $piles
     * @return Boolean
     */
    function stoneGame($piles) {
        return true;
    }
}
""")

add("0878_nth_magical_number", r"""<?php
// LeetCode 0878 - Nth Magical Number
// https://leetcode.com/problems/nth-magical-number/

class Solution {
    /**
     * @param Integer $n
     * @param Integer $a
     * @param Integer $b
     * @return Integer
     */
    function nthMagicalNumber($n, $a, $b) {
        $MOD = 1000000007;
        $gcd = function($x, $y) {
            while ($y !== 0) {
                $t = $x % $y;
                $x = $y;
                $y = $t;
            }
            return $x;
        };
        $lcm = intdiv($a, $gcd($a, $b)) * $b;
        $lo = 1;
        $hi = $n * min($a, $b);
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi, 2);
            if (intdiv($mid, $a) + intdiv($mid, $b) - intdiv($mid, $lcm) >= $n) $hi = $mid;
            else $lo = $mid + 1;
        }
        return $lo % $MOD;
    }
}
""")

add("0879_profitable_schemes", r"""<?php
// LeetCode 0879 - Profitable Schemes
// https://leetcode.com/problems/profitable-schemes/

class Solution {
    /**
     * @param Integer $n
     * @param Integer $minProfit
     * @param Integer[] $group
     * @param Integer[] $profit
     * @return Integer
     */
    function profitableSchemes($n, $minProfit, $group, $profit) {
        $MOD = 1000000007;
        $dp = array_fill(0, $n + 1, array_fill(0, $minProfit + 1, 0));
        $dp[0][0] = 1;
        $gn = count($group);
        for ($i = 0; $i < $gn; $i++) {
            $members = $group[$i];
            $p = $profit[$i];
            for ($people = $n; $people >= $members; $people--) {
                for ($prof = $minProfit; $prof >= 0; $prof--) {
                    $np = min($minProfit, $prof + $p);
                    $dp[$people][$np] = ($dp[$people][$np] + $dp[$people - $members][$prof]) % $MOD;
                }
            }
        }
        $ans = 0;
        for ($people = 0; $people <= $n; $people++) $ans = ($ans + $dp[$people][$minProfit]) % $MOD;
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
        print(f"wrote {folder}")
    print(f"wrote={ported}")


if __name__ == "__main__":
    main()

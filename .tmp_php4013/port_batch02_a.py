#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
SOLUTIONS: dict[str, str] = {}


def add(name: str, content: str) -> None:
    SOLUTIONS[name] = content.strip() + "\n"


add("0780_reaching_points", r"""<?php
// LeetCode 0780 - Reaching Points
// https://leetcode.com/problems/reaching-points/

class Solution {
    /**
     * @param Integer $sx
     * @param Integer $sy
     * @param Integer $tx
     * @param Integer $ty
     * @return Boolean
     */
    function reachingPoints($sx, $sy, $tx, $ty) {
        while ($tx >= $sx && $ty >= $sy) {
            if ($tx === $sx && $ty === $sy) return true;
            if ($tx === $ty) break;
            if ($tx > $ty) {
                if ($ty > $sy) $tx %= $ty;
                else return ($tx - $sx) % $ty === 0;
            } else {
                if ($tx > $sx) $ty %= $tx;
                else return ($ty - $sy) % $tx === 0;
            }
        }
        return $tx === $sx && $ty === $sy;
    }
}
""")

add("0781_rabbits_in_forest", r"""<?php
// LeetCode 0781 - Rabbits in Forest
// https://leetcode.com/problems/rabbits-in-forest/

class Solution {
    /**
     * @param Integer[] $answers
     * @return Integer
     */
    function numRabbits($answers) {
        $counts = [];
        foreach ($answers as $answer) {
            $counts[$answer] = ($counts[$answer] ?? 0) + 1;
        }
        $total = 0;
        foreach ($counts as $key => $value) {
            $group = $key + 1;
            $groups = intdiv($value + $group - 1, $group);
            $total += $groups * $group;
        }
        return $total;
    }
}
""")

add("0782_transform_to_chessboard", r"""<?php
// LeetCode 0782 - Transform to Chessboard
// https://leetcode.com/problems/transform-to-chessboard/

class Solution {
    /**
     * @param Integer[][] $board
     * @return Integer
     */
    function movesToChessboard($board) {
        $n = count($board);
        for ($i = 0; $i < $n; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if (($board[0][0] ^ $board[$i][0] ^ $board[0][$j] ^ $board[$i][$j]) !== 0) return -1;
            }
        }
        $rowSum = 0;
        $colSum = 0;
        for ($i = 0; $i < $n; $i++) {
            $rowSum += $board[0][$i];
            $colSum += $board[$i][0];
        }
        if ($rowSum < ($n >> 1) || $rowSum > (($n + 1) >> 1)) return -1;
        if ($colSum < ($n >> 1) || $colSum > (($n + 1) >> 1)) return -1;
        $rowSwap = 0;
        $colSwap = 0;
        for ($i = 0; $i < $n; $i++) {
            if ($board[0][$i] !== $i % 2) $rowSwap++;
            if ($board[$i][0] !== $i % 2) $colSwap++;
        }
        if ($n % 2 === 1) {
            if ($rowSwap % 2 === 1) $rowSwap = $n - $rowSwap;
            if ($colSwap % 2 === 1) $colSwap = $n - $colSwap;
        } else {
            $rowSwap = min($rowSwap, $n - $rowSwap);
            $colSwap = min($colSwap, $n - $colSwap);
        }
        return ($rowSwap + $colSwap) >> 1;
    }
}
""")

add("0783_minimum_distance_between_bst_nodes", r"""<?php
// LeetCode 0783 - Minimum Distance Between BST Nodes
// https://leetcode.com/problems/minimum-distance-between-bst-nodes/

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
     * @return Integer
     */
    function minDiffInBST($root) {
        $hasPrev = false;
        $prev = 0;
        $best = PHP_INT_MAX;
        $inorder = function($node) use (&$inorder, &$hasPrev, &$prev, &$best) {
            if ($node === null) return;
            $inorder($node->left);
            if ($hasPrev) $best = min($best, $node->val - $prev);
            $prev = $node->val;
            $hasPrev = true;
            $inorder($node->right);
        };
        $inorder($root);
        return $best;
    }
}
""")

add("0784_letter_case_permutation", r"""<?php
// LeetCode 0784 - Letter Case Permutation
// https://leetcode.com/problems/letter-case-permutation/

class Solution {
    /**
     * @param String $s
     * @return String[]
     */
    function letterCasePermutation($s) {
        $result = [""];
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $ch = $s[$i];
            $next = [];
            if (ctype_alpha($ch)) {
                $lower = strtolower($ch);
                $upper = strtoupper($ch);
                foreach ($result as $prefix) {
                    $next[] = $prefix . $lower;
                    $next[] = $prefix . $upper;
                }
            } else {
                foreach ($result as $prefix) $next[] = $prefix . $ch;
            }
            $result = $next;
        }
        return $result;
    }
}
""")

add("0785_is_graph_bipartite", r"""<?php
// LeetCode 0785 - Is Graph Bipartite?
// https://leetcode.com/problems/is-graph-bipartite/

class Solution {
    /**
     * @param Integer[][] $graph
     * @return Boolean
     */
    function isBipartite($graph) {
        $n = count($graph);
        $color = array_fill(0, $n, -1);
        $dfs = function($node, $c) use (&$dfs, &$color, $graph) {
            $color[$node] = $c;
            foreach ($graph[$node] as $nei) {
                if ($color[$nei] === -1) {
                    if (!$dfs($nei, $c ^ 1)) return false;
                } elseif ($color[$nei] === $c) {
                    return false;
                }
            }
            return true;
        };
        for ($node = 0; $node < $n; $node++) {
            if ($color[$node] === -1 && !$dfs($node, 0)) return false;
        }
        return true;
    }
}
""")

add("0786_k_th_smallest_prime_fraction", r"""<?php
// LeetCode 0786 - K-th Smallest Prime Fraction
// https://leetcode.com/problems/k-th-smallest-prime-fraction/

class Solution {
    /**
     * @param Integer[] $arr
     * @param Integer $k
     * @return Integer[]
     */
    function kthSmallestPrimeFraction($arr, $k) {
        $n = count($arr);
        $heap = [];
        $push = function($i, $j) use (&$heap, $arr) {
            $heap[] = [$i, $j];
            $idx = count($heap) - 1;
            while ($idx > 0) {
                $p = ($idx - 1) >> 1;
                if ($arr[$heap[$idx][0]] / $arr[$heap[$idx][1]] >= $arr[$heap[$p][0]] / $arr[$heap[$p][1]]) break;
                $tmp = $heap[$idx];
                $heap[$idx] = $heap[$p];
                $heap[$p] = $tmp;
                $idx = $p;
            }
        };
        $pop = function() use (&$heap, $arr) {
            $top = $heap[0];
            $last = array_pop($heap);
            if (count($heap)) {
                $heap[0] = $last;
                $idx = 0;
                while (true) {
                    $smallest = $idx;
                    $l = $idx * 2 + 1;
                    $r = $idx * 2 + 2;
                    if ($l < count($heap) && $arr[$heap[$l][0]] / $arr[$heap[$l][1]] < $arr[$heap[$smallest][0]] / $arr[$heap[$smallest][1]]) $smallest = $l;
                    if ($r < count($heap) && $arr[$heap[$r][0]] / $arr[$heap[$r][1]] < $arr[$heap[$smallest][0]] / $arr[$heap[$smallest][1]]) $smallest = $r;
                    if ($smallest === $idx) break;
                    $tmp = $heap[$idx];
                    $heap[$idx] = $heap[$smallest];
                    $heap[$smallest] = $tmp;
                    $idx = $smallest;
                }
            }
            return $top;
        };
        for ($i = 0; $i < $n - 1; $i++) $push($i, $n - 1);
        for ($t = 0; $t < $k - 1; $t++) {
            [$i, $j] = $pop();
            if ($j - 1 > $i) $push($i, $j - 1);
        }
        [$i, $j] = $pop();
        return [$arr[$i], $arr[$j]];
    }
}
""")

add("0787_cheapest_flights_within_k_stops", r"""<?php
// LeetCode 0787 - Cheapest Flights Within K Stops
// https://leetcode.com/problems/cheapest-flights-within-k-stops/

class Solution {
    /**
     * @param Integer $n
     * @param Integer[][] $flights
     * @param Integer $src
     * @param Integer $dst
     * @param Integer $k
     * @return Integer
     */
    function findCheapestPrice($n, $flights, $src, $dst, $k) {
        $INF = intdiv(PHP_INT_MAX, 4);
        $dist = array_fill(0, $n, $INF);
        $dist[$src] = 0;
        for ($i = 0; $i <= $k; $i++) {
            $nxt = $dist;
            foreach ($flights as $f) {
                $u = $f[0];
                $v = $f[1];
                $price = $f[2];
                if ($dist[$u] !== $INF && $dist[$u] + $price < $nxt[$v]) {
                    $nxt[$v] = $dist[$u] + $price;
                }
            }
            $dist = $nxt;
        }
        return $dist[$dst] === $INF ? -1 : $dist[$dst];
    }
}
""")

add("0788_rotated_digits", r"""<?php
// LeetCode 0788 - Rotated Digits
// https://leetcode.com/problems/rotated-digits/

class Solution {
    /**
     * @param Integer $n
     * @return Integer
     */
    function rotatedDigits($n) {
        $count = 0;
        for ($num = 1; $num <= $n; $num++) {
            $s = (string)$num;
            $ok = true;
            $changed = false;
            $len = strlen($s);
            for ($i = 0; $i < $len; $i++) {
                $ch = $s[$i];
                if ($ch === '3' || $ch === '4' || $ch === '7') { $ok = false; break; }
                if ($ch === '2' || $ch === '5' || $ch === '6' || $ch === '9') $changed = true;
            }
            if ($ok && $changed) $count++;
        }
        return $count;
    }
}
""")

add("0789_escape_the_ghosts", r"""<?php
// LeetCode 0789 - Escape The Ghosts
// https://leetcode.com/problems/escape-the-ghosts/

class Solution {
    /**
     * @param Integer[][] $ghosts
     * @param Integer[] $target
     * @return Boolean
     */
    function escapeGhosts($ghosts, $target) {
        $targetDist = abs($target[0]) + abs($target[1]);
        foreach ($ghosts as $ghost) {
            if (abs($ghost[0] - $target[0]) + abs($ghost[1] - $target[1]) <= $targetDist) {
                return false;
            }
        }
        return true;
    }
}
""")

add("0790_domino_and_tromino_tiling", r"""<?php
// LeetCode 0790 - Domino and Tromino Tiling
// https://leetcode.com/problems/domino-and-tromino-tiling/

class Solution {
    /**
     * @param Integer $n
     * @return Integer
     */
    function numTilings($n) {
        $MOD = 1000000007;
        if ($n === 1) return 1;
        if ($n === 2) return 2;
        $dp = array_fill(0, $n + 1, 0);
        $dp[1] = 1;
        $dp[2] = 2;
        $dp[3] = 5;
        for ($i = 4; $i <= $n; $i++) $dp[$i] = (2 * $dp[$i - 1] + $dp[$i - 3]) % $MOD;
        return $dp[$n];
    }
}
""")

add("0791_custom_sort_string", r"""<?php
// LeetCode 0791 - Custom Sort String
// https://leetcode.com/problems/custom-sort-string/

class Solution {
    /**
     * @param String $order
     * @param String $s
     * @return String
     */
    function customSortString($order, $s) {
        $count = array_fill(0, 26, 0);
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) $count[ord($s[$i]) - 97]++;
        $sb = "";
        $on = strlen($order);
        for ($i = 0; $i < $on; $i++) {
            $ch = $order[$i];
            $idx = ord($ch) - 97;
            while ($count[$idx]-- > 0) $sb .= $ch;
        }
        for ($i = 0; $i < 26; $i++) {
            while ($count[$i]-- > 0) $sb .= chr(97 + $i);
        }
        return $sb;
    }
}
""")

add("0792_number_of_matching_subsequences", r"""<?php
// LeetCode 0792 - Number of Matching Subsequences
// https://leetcode.com/problems/number-of-matching-subsequences/

class Solution {
    /**
     * @param String $s
     * @param String[] $words
     * @return Integer
     */
    function numMatchingSubseq($s, $words) {
        $waiting = array_fill(0, 26, []);
        $wn = count($words);
        for ($i = 0; $i < $wn; $i++) {
            $w = $words[$i];
            $waiting[ord($w[0]) - 97][] = [$i, 0];
        }
        $ans = 0;
        $n = strlen($s);
        for ($si = 0; $si < $n; $si++) {
            $ch = $s[$si];
            $idxc = ord($ch) - 97;
            $cur = $waiting[$idxc];
            $waiting[$idxc] = [];
            foreach ($cur as $pair) {
                $wi = $pair[0];
                $idx = $pair[1] + 1;
                if ($idx === strlen($words[$wi])) $ans++;
                else $waiting[ord($words[$wi][$idx]) - 97][] = [$wi, $idx];
            }
        }
        return $ans;
    }
}
""")

add("0793_preimage_size_of_factorial_zeroes_function", r"""<?php
// LeetCode 0793 - Preimage Size of Factorial Zeroes Function
// https://leetcode.com/problems/preimage-size-of-factorial-zeroes-function/

class Solution {
    /**
     * @param Integer $k
     * @return Integer
     */
    function preimageSizeFZF($k) {
        $zeros = function($n) {
            $z = 0;
            while ($n > 0) {
                $n = intdiv($n, 5);
                $z += $n;
            }
            return $z;
        };
        $firstGe = function($target) use ($zeros) {
            $lo = 0;
            $hi = 5 * $target + 5;
            while ($lo < $hi) {
                $mid = intdiv($lo + $hi, 2);
                if ($zeros($mid) >= $target) $hi = $mid;
                else $lo = $mid + 1;
            }
            return $lo;
        };
        return $firstGe($k + 1) - $firstGe($k);
    }
}
""")

add("0794_valid_tic_tac_toe_state", r"""<?php
// LeetCode 0794 - Valid Tic-Tac-Toe State
// https://leetcode.com/problems/valid-tic-tac-toe-state/

class Solution {
    /**
     * @param String[] $board
     * @return Boolean
     */
    function validTicTacToe($board) {
        $x = 0;
        $o = 0;
        foreach ($board as $row) {
            $len = strlen($row);
            for ($i = 0; $i < $len; $i++) {
                $ch = $row[$i];
                if ($ch === 'X') $x++;
                elseif ($ch === 'O') $o++;
            }
        }
        if ($o > $x || $x - $o > 1) return false;
        $win = function($player) use ($board) {
            for ($i = 0; $i < 3; $i++) {
                if ($board[$i][0] === $player && $board[$i][1] === $player && $board[$i][2] === $player) return true;
                if ($board[0][$i] === $player && $board[1][$i] === $player && $board[2][$i] === $player) return true;
            }
            if ($board[0][0] === $player && $board[1][1] === $player && $board[2][2] === $player) return true;
            if ($board[0][2] === $player && $board[1][1] === $player && $board[2][0] === $player) return true;
            return false;
        };
        $xWin = $win('X');
        $oWin = $win('O');
        if ($xWin && $oWin) return false;
        if ($xWin && $x !== $o + 1) return false;
        if ($oWin && $x !== $o) return false;
        return true;
    }
}
""")

add("0795_number_of_subarrays_with_bounded_maximum", r"""<?php
// LeetCode 0795 - Number of Subarrays with Bounded Maximum
// https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/

class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $left
     * @param Integer $right
     * @return Integer
     */
    function numSubarrayBoundedMax($nums, $left, $right) {
        $countAtMost = function($bound) use ($nums) {
            $ans = 0;
            $cur = 0;
            foreach ($nums as $num) {
                if ($num <= $bound) {
                    $cur++;
                    $ans += $cur;
                } else {
                    $cur = 0;
                }
            }
            return $ans;
        };
        return $countAtMost($right) - $countAtMost($left - 1);
    }
}
""")

add("0796_rotate_string", r"""<?php
// LeetCode 0796 - Rotate String
// https://leetcode.com/problems/rotate-string/

class Solution {
    /**
     * @param String $s
     * @param String $goal
     * @return Boolean
     */
    function rotateString($s, $goal) {
        return strlen($s) === strlen($goal) && strpos($s . $s, $goal) !== false;
    }
}
""")

add("0797_all_paths_from_source_to_target", r"""<?php
// LeetCode 0797 - All Paths From Source to Target
// https://leetcode.com/problems/all-paths-from-source-to-target/

class Solution {
    /**
     * @param Integer[][] $graph
     * @return Integer[][]
     */
    function allPathsSourceTarget($graph) {
        $target = count($graph) - 1;
        $answer = [];
        $path = [0];
        $dfs = function($node) use (&$dfs, $graph, $target, &$answer, &$path) {
            if ($node === $target) {
                $answer[] = $path;
                return;
            }
            foreach ($graph[$node] as $nei) {
                $path[] = $nei;
                $dfs($nei);
                array_pop($path);
            }
        };
        $dfs(0);
        return $answer;
    }
}
""")

add("0798_smallest_rotation_with_highest_score", r"""<?php
// LeetCode 0798 - Smallest Rotation with Highest Score
// https://leetcode.com/problems/smallest-rotation-with-highest-score/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function bestRotation($nums) {
        $n = count($nums);
        $change = array_fill(0, $n, 1);
        for ($i = 0; $i < $n; $i++) $change[($i - $nums[$i] + 1 + $n) % $n] -= 1;
        for ($i = 1; $i < $n; $i++) $change[$i] += $change[$i - 1];
        $best = 0;
        for ($i = 1; $i < $n; $i++) if ($change[$i] > $change[$best]) $best = $i;
        return $best;
    }
}
""")

add("0799_champagne_tower", r"""<?php
// LeetCode 0799 - Champagne Tower
// https://leetcode.com/problems/champagne-tower/

class Solution {
    /**
     * @param Integer $poured
     * @param Integer $query_row
     * @param Integer $query_glass
     * @return Float
     */
    function champagneTower($poured, $query_row, $query_glass) {
        $row = [$poured];
        for ($r = 0; $r < $query_row; $r++) {
            $nextRow = array_fill(0, $r + 2, 0.0);
            $len = count($row);
            for ($i = 0; $i < $len; $i++) {
                $overflow = ($row[$i] - 1.0) / 2.0;
                if ($overflow > 0) {
                    $nextRow[$i] += $overflow;
                    $nextRow[$i + 1] += $overflow;
                }
            }
            $row = $nextRow;
        }
        return min(1.0, $row[$query_glass]);
    }
}
""")

add("0800_similar_rgb_color", r"""<?php
// LeetCode 0800 - Similar RGB Color
// https://leetcode.com/problems/similar-rgb-color/

class Solution {
    /**
     * @param String $color
     * @return String
     */
    function similarRGB($color) {
        $closest = function($component) {
            $value = hexdec($component);
            $rounded = intdiv($value + 8, 17);
            $hex = dechex($rounded);
            return $hex . $hex;
        };
        return "#" . $closest(substr($color, 1, 2)) . $closest(substr($color, 3, 2)) . $closest(substr($color, 5, 2));
    }
}
""")

add("0801_minimum_swaps_to_make_sequences_increasing", r"""<?php
// LeetCode 0801 - Minimum Swaps To Make Sequences Increasing
// https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/

class Solution {
    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @return Integer
     */
    function minSwap($nums1, $nums2) {
        $n = count($nums1);
        $swap = array_fill(0, $n, $n);
        $keep = array_fill(0, $n, $n);
        $swap[0] = 1;
        $keep[0] = 0;
        for ($i = 1; $i < $n; $i++) {
            if ($nums1[$i] > $nums1[$i - 1] && $nums2[$i] > $nums2[$i - 1]) {
                $keep[$i] = $keep[$i - 1];
                $swap[$i] = $swap[$i - 1] + 1;
            }
            if ($nums1[$i] > $nums2[$i - 1] && $nums2[$i] > $nums1[$i - 1]) {
                $keep[$i] = min($keep[$i], $swap[$i - 1]);
                $swap[$i] = min($swap[$i], $keep[$i - 1] + 1);
            }
        }
        return min($swap[$n - 1], $keep[$n - 1]);
    }
}
""")

add("0802_find_eventual_safe_states", r"""<?php
// LeetCode 0802 - Find Eventual Safe States
// https://leetcode.com/problems/find-eventual-safe-states/

class Solution {
    /**
     * @param Integer[][] $graph
     * @return Integer[]
     */
    function eventualSafeNodes($graph) {
        $n = count($graph);
        $color = array_fill(0, $n, 0);
        $dfs = function($node) use (&$dfs, $graph, &$color) {
            if ($color[$node] !== 0) return $color[$node] === 2;
            $color[$node] = 1;
            foreach ($graph[$node] as $nei) {
                if (!$dfs($nei)) return false;
            }
            $color[$node] = 2;
            return true;
        };
        $ans = [];
        for ($i = 0; $i < $n; $i++) if ($dfs($i)) $ans[] = $i;
        return $ans;
    }
}
""")

add("0803_bricks_falling_when_hit", r"""<?php
// LeetCode 0803 - Bricks Falling When Hit
// https://leetcode.com/problems/bricks-falling-when-hit/

class Solution {
    /**
     * @param Integer[][] $grid
     * @param Integer[][] $hits
     * @return Integer[]
     */
    function hitBricks($grid, $hits) {
        $m = count($grid);
        $n = count($grid[0]);
        $roof = $m * $n;
        $parent = [];
        $size = [];
        for ($i = 0; $i <= $roof; $i++) {
            $parent[$i] = $i;
            $size[$i] = 1;
        }
        $find = function($x) use (&$parent) {
            while ($parent[$x] !== $x) {
                $parent[$x] = $parent[$parent[$x]];
                $x = $parent[$x];
            }
            return $x;
        };
        $unite = function($a, $b) use (&$parent, &$size, $find) {
            $ra = $find($a);
            $rb = $find($b);
            if ($ra === $rb) return;
            $parent[$ra] = $rb;
            $size[$rb] += $size[$ra];
        };
        $idx = function($r, $c) use ($n) { return $r * $n + $c; };
        $status = [];
        foreach ($grid as $row) $status[] = $row;
        foreach ($hits as $hit) $status[$hit[0]][$hit[1]] = 0;
        $dr = [-1, 1, 0, 0];
        $dc = [0, 0, -1, 1];
        for ($r = 0; $r < $m; $r++) {
            for ($c = 0; $c < $n; $c++) {
                if ($status[$r][$c] === 0) continue;
                if ($r === 0) $unite($idx($r, $c), $roof);
                for ($k = 0; $k < 4; $k++) {
                    $nr = $r + $dr[$k];
                    $nc = $c + $dc[$k];
                    if ($nr >= 0 && $nr < $m && $nc >= 0 && $nc < $n && $status[$nr][$nc] === 1) {
                        $unite($idx($r, $c), $idx($nr, $nc));
                    }
                }
            }
        }
        $answer = array_fill(0, count($hits), 0);
        for ($i = count($hits) - 1; $i >= 0; $i--) {
            $r = $hits[$i][0];
            $c = $hits[$i][1];
            if ($grid[$r][$c] === 0) continue;
            $prev = $size[$find($roof)];
            $status[$r][$c] = 1;
            if ($r === 0) $unite($idx($r, $c), $roof);
            for ($k = 0; $k < 4; $k++) {
                $nr = $r + $dr[$k];
                $nc = $c + $dc[$k];
                if ($nr >= 0 && $nr < $m && $nc >= 0 && $nc < $n && $status[$nr][$nc] === 1) {
                    $unite($idx($r, $c), $idx($nr, $nc));
                }
            }
            $curr = $size[$find($roof)];
            $answer[$i] = max(0, $curr - $prev - 1);
        }
        return $answer;
    }
}
""")

add("0804_unique_morse_code_words", r"""<?php
// LeetCode 0804 - Unique Morse Code Words
// https://leetcode.com/problems/unique-morse-code-words/

class Solution {
    /**
     * @param String[] $words
     * @return Integer
     */
    function uniqueMorseRepresentations($words) {
        $codes = [
            ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---",
            "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-",
            "..-", "...-", ".--", "-..-", "-.--", "--.."
        ];
        $seen = [];
        foreach ($words as $word) {
            $code = "";
            $len = strlen($word);
            for ($i = 0; $i < $len; $i++) $code .= $codes[ord($word[$i]) - 97];
            $seen[$code] = true;
        }
        return count($seen);
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

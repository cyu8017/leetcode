#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
SOLUTIONS = {}

def add(folder, body):
    SOLUTIONS[folder] = body


add("3313_find_the_last_marked_nodes_in_tree", r'''<?php
// LeetCode 3313 - Find the Last Marked Nodes in Tree
// https://leetcode.com/problems/find-the-last-marked-nodes-in-tree/

class Solution {
    function lastMarkedNodes($edges) {
        $n = count($edges) + 1;
        $g = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $g[$e[0]][] = $e[1];
            $g[$e[1]][] = $e[0];
        }
        $ru = $this->bfs(0, $g, $n);
        $u = $ru[0];
        $ru = $this->bfs($u, $g, $n);
        $v = $ru[0];
        $du = $ru[1];
        $dv = $this->bfs($v, $g, $n)[1];
        $ans = [];
        for ($i = 0; $i < $n; $i++) $ans[$i] = $du[$i] >= $dv[$i] ? $u : $v;
        return $ans;
    }

    function bfs($start, $g, $n) {
        $dist = array_fill(0, $n, -1);
        $q = [$start];
        $dist[$start] = 0;
        $far = $start;
        $head = 0;
        while ($head < count($q)) {
            $u = $q[$head++];
            if ($dist[$u] > $dist[$far]) $far = $u;
            foreach ($g[$u] as $v) {
                if ($dist[$v] === -1) {
                    $dist[$v] = $dist[$u] + 1;
                    $q[] = $v;
                }
            }
        }
        return [$far, $dist];
    }
}
''')

add("3314_construct_the_minimum_bitwise_array_i", r'''<?php
// LeetCode 3314 - Construct the Minimum Bitwise Array I
// https://leetcode.com/problems/construct-the-minimum-bitwise-array-i/

class Solution {
    function minBitwiseArray($nums) {
        $ans = array_fill(0, count($nums), -1);
        for ($i = 0; $i < count($nums); $i++) {
            $n = $nums[$i];
            for ($x = 0; $x < $n; $x++) {
                if (($x | ($x + 1)) === $n) { $ans[$i] = $x; break; }
            }
        }
        return $ans;
    }
}
''')

add("3315_construct_the_minimum_bitwise_array_ii", r'''<?php
// LeetCode 3315 - Construct the Minimum Bitwise Array II
// https://leetcode.com/problems/construct-the-minimum-bitwise-array-ii/

class Solution {
    function minBitwiseArray($nums) {
        $ans = array_fill(0, count($nums), -1);
        for ($i = 0; $i < count($nums); $i++) {
            $n = $nums[$i];
            if ($n === 2) continue;
            for ($b = 0; $b < 31; $b++) {
                if ((($n >> $b) & 1) === 0) continue;
                $x = $n ^ (1 << $b);
                if (($x | ($x + 1)) === $n) { $ans[$i] = $x; break; }
            }
        }
        return $ans;
    }
}
''')

add("3316_find_maximum_removals_from_source_string", r'''<?php
// LeetCode 3316 - Find Maximum Removals From Source String
// https://leetcode.com/problems/find-maximum-removals-from-source-string/

class Solution {
    function ok($removeFirst, $source, $pattern, $targetIndices, $n) {
        $mark = array_fill(0, $n, false);
        for ($i = 0; $i < $removeFirst; $i++) $mark[$targetIndices[$i]] = true;
        $j = 0;
        $m = strlen($pattern);
        for ($i = 0; $i < $n && $j < $m; $i++) {
            if ($mark[$i]) continue;
            if ($source[$i] === $pattern[$j]) $j++;
        }
        return $j === $m;
    }

    function maxRemovals($source, $pattern, $targetIndices) {
        $n = strlen($source);
        $lo = 0;
        $hi = count($targetIndices);
        while ($lo < $hi) {
            $mid = ($lo + $hi + 1) >> 1;
            if ($this->ok($mid, $source, $pattern, $targetIndices, $n)) $lo = $mid;
            else $hi = $mid - 1;
        }
        return $lo;
    }
}
''')

add("3317_find_the_number_of_possible_ways_for_an_event", r'''<?php
// LeetCode 3317 - Find the Number of Possible Ways for an Event
// https://leetcode.com/problems/find-the-number-of-possible-ways-for-an-event/

class Solution {
    function modPow($a, $e, $mod) {
        $r = 1;
        $a %= $mod;
        while ($e > 0) {
            if ($e & 1) $r = $r * $a % $mod;
            $a = $a * $a % $mod;
            $e >>= 1;
        }
        return $r;
    }

    function numberOfWays($n, $x, $y) {
        $mod = 1000000007;
        $dp = [];
        for ($i = 0; $i <= $n; $i++) $dp[$i] = array_fill(0, $x + 1, 0);
        $dp[0][0] = 1;
        for ($i = 1; $i <= $n; $i++) {
            for ($j = 1; $j <= $x && $j <= $i; $j++) {
                $dp[$i][$j] = ($dp[$i - 1][$j - 1] + $j * $dp[$i - 1][$j] % $mod) % $mod;
            }
        }
        $fact = [1];
        for ($i = 1; $i <= $x; $i++) $fact[$i] = $fact[$i - 1] * $i % $mod;
        $ans = 0;
        $ypow = 1;
        for ($k = 1; $k <= $x && $k <= $n; $k++) {
            $ypow = $ypow * $y % $mod;
            $perm = $fact[$x] * $this->modPow($fact[$x - $k], $mod - 2, $mod) % $mod;
            $ans = ($ans + $dp[$n][$k] * $perm % $mod * $ypow % $mod) % $mod;
        }
        return $ans;
    }
}
''')

add("3318_find_x_sum_of_all_k_long_subarrays_i", r'''<?php
// LeetCode 3318 - Find X-Sum of All K-Long Subarrays I
// https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-i/

class Solution {
    function findXSum($nums, $k, $x) {
        $n = count($nums);
        $ans = [];
        for ($i = 0; $i <= $n - $k; $i++) {
            $freq = [];
            for ($j = $i; $j < $i + $k; $j++) $freq[$nums[$j]] = ($freq[$nums[$j]] ?? 0) + 1;
            $arr = [];
            foreach ($freq as $key => $val) $arr[] = [$key, $val];
            usort($arr, function($A, $B) {
                if ($B[1] !== $A[1]) return $B[1] <=> $A[1];
                return $B[0] <=> $A[0];
            });
            $lim = min($x, count($arr));
            $keep = [];
            for ($t = 0; $t < $lim; $t++) $keep[$arr[$t][0]] = true;
            $sum = 0;
            for ($j = $i; $j < $i + $k; $j++) if (isset($keep[$nums[$j]])) $sum += $nums[$j];
            $ans[$i] = $sum;
        }
        return $ans;
    }
}
''')

add("3319_k_th_largest_perfect_subtree_size_in_binary_tree", r'''<?php
// LeetCode 3319 - K-th Largest Perfect Subtree Size in Binary Tree
// https://leetcode.com/problems/k-th-largest-perfect-subtree-size-in-binary-tree/

class TreeNode {
    public $val;
    public $left;
    public $right;
    function __construct($val = 0, $left = null, $right = null) {
        $this->val = $val;
        $this->left = $left;
        $this->right = $right;
    }
}

class Solution {
    public $sizes;

    function dfs($node) {
        if (!$node) return [0, 0, 1];
        $L = $this->dfs($node->left);
        $R = $this->dfs($node->right);
        $sz = $L[1] + $R[1] + 1;
        $perf = $L[2] === 1 && $R[2] === 1 && $L[0] === $R[0];
        if ($perf) $this->sizes[] = $sz;
        return [max($L[0], $R[0]) + 1, $sz, $perf ? 1 : 0];
    }

    function kthLargestPerfectSubtree($root, $k) {
        $this->sizes = [];
        $this->dfs($root);
        rsort($this->sizes);
        if ($k > count($this->sizes)) return -1;
        return $this->sizes[$k - 1];
    }
}
''')

add("3320_count_the_number_of_winning_sequences", r'''<?php
// LeetCode 3320 - Count the Number of Winning Sequences
// https://leetcode.com/problems/count-the-number-of-winning-sequences/

class Solution {
    function countWinningSequences($s) {
        $mod = 1000000007;
        $n = strlen($s);
        $mp = ['F' => 0, 'W' => 1, 'E' => 2];
        $beat = [2, 0, 1];
        $score = [];
        for ($a = 0; $a < 3; $a++) {
            for ($b = 0; $b < 3; $b++) {
                if ($a === $b) $score[$a][$b] = 0;
                else if ($beat[$a] === $b) $score[$a][$b] = 1;
                else $score[$a][$b] = -1;
            }
        }
        $offset = $n;
        $dp = [];
        for ($a = 0; $a < 3; $a++) $dp[$a] = array_fill(0, 2 * $n + 1, 0);
        $b0 = $mp[$s[0]];
        for ($a = 0; $a < 3; $a++) $dp[$a][$score[$a][$b0] + $offset] = 1;
        for ($i = 1; $i < $n; $i++) {
            $ndp = [];
            for ($a = 0; $a < 3; $a++) $ndp[$a] = array_fill(0, 2 * $n + 1, 0);
            $b = $mp[$s[$i]];
            for ($last = 0; $last < 3; $last++) {
                for ($d = 0; $d <= 2 * $n; $d++) {
                    if ($dp[$last][$d] === 0) continue;
                    for ($a = 0; $a < 3; $a++) {
                        if ($a === $last) continue;
                        $nd = $d + $score[$a][$b];
                        if ($nd < 0 || $nd > 2 * $n) continue;
                        $ndp[$a][$nd] = ($ndp[$a][$nd] + $dp[$last][$d]) % $mod;
                    }
                }
            }
            $dp = $ndp;
        }
        $ans = 0;
        for ($a = 0; $a < 3; $a++) {
            for ($d = $offset + 1; $d <= 2 * $n; $d++) $ans = ($ans + $dp[$a][$d]) % $mod;
        }
        return $ans;
    }
}
''')

add("3321_find_x_sum_of_all_k_long_subarrays_ii", r'''<?php
// LeetCode 3321 - Find X-Sum of All K-Long Subarrays II
// https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-ii/

class Solution {
    function findXSum($nums, $k, $x) {
        $n = count($nums);
        $ans = [];
        for ($i = 0; $i <= $n - $k; $i++) {
            $freq = [];
            for ($j = $i; $j < $i + $k; $j++) $freq[$nums[$j]] = ($freq[$nums[$j]] ?? 0) + 1;
            $arr = [];
            foreach ($freq as $key => $val) $arr[] = [$key, $val];
            usort($arr, function($A, $B) {
                if ($B[1] !== $A[1]) return $B[1] <=> $A[1];
                return $B[0] <=> $A[0];
            });
            $lim = min($x, count($arr));
            $keep = [];
            for ($t = 0; $t < $lim; $t++) $keep[$arr[$t][0]] = true;
            $sum = 0;
            for ($j = $i; $j < $i + $k; $j++) if (isset($keep[$nums[$j]])) $sum += $nums[$j];
            $ans[$i] = $sum;
        }
        return $ans;
    }
}
''')

add("3323_minimize_connected_groups_by_inserting_interval", r'''<?php
// LeetCode 3323 - Minimize Connected Groups by Inserting Interval
// https://leetcode.com/problems/minimize-connected-groups-by-inserting-interval/

class Solution {
    function minConnectedGroups($intervals, $k) {
        usort($intervals, function($a, $b) { return $a[0] <=> $b[0]; });
        $merged = [];
        foreach ($intervals as $it) {
            if (!$merged || $it[0] > $merged[count($merged) - 1][1]) $merged[] = [$it[0], $it[1]];
            else if ($it[1] > $merged[count($merged) - 1][1]) $merged[count($merged) - 1][1] = $it[1];
        }
        $m = count($merged);
        $ans = $m;
        for ($i = 0; $i < $m; $i++) {
            $end = $merged[$i][1] + $k;
            $j = $i;
            while ($j < $m && $merged[$j][0] <= $end) $j++;
            $groups = $i + 1 + ($m - $j);
            if ($groups < $ans) $ans = $groups;
        }
        return $ans;
    }
}
''')

add("3324_find_the_sequence_of_strings_appeared_on_the_screen", r'''<?php
// LeetCode 3324 - Find the Sequence of Strings Appeared on the Screen
// https://leetcode.com/problems/find-the-sequence-of-strings-appeared-on-the-screen/

class Solution {
    function stringSequence($target) {
        $ans = [];
        $cur = '';
        $n = strlen($target);
        for ($p = 0; $p < $n; $p++) {
            $ch = $target[$p];
            $cur .= 'a';
            $ans[] = $cur;
            while ($cur[strlen($cur) - 1] !== $ch) {
                $last = chr(ord($cur[strlen($cur) - 1]) + 1);
                $cur = substr($cur, 0, -1) . $last;
                $ans[] = $cur;
            }
        }
        return $ans;
    }
}
''')

add("3325_count_substrings_with_k_frequency_characters_i", r'''<?php
// LeetCode 3325 - Count Substrings With K-Frequency Characters I
// https://leetcode.com/problems/count-substrings-with-k-frequency-characters-i/

class Solution {
    function numberOfSubstrings($s, $k) {
        $n = strlen($s);
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            $freq = array_fill(0, 26, 0);
            for ($j = $i; $j < $n; $j++) {
                $freq[ord($s[$j]) - 97]++;
                $ok = false;
                foreach ($freq as $f) if ($f >= $k) { $ok = true; break; }
                if ($ok) { $ans += $n - $j; break; }
            }
        }
        return $ans;
    }
}
''')

add("3326_minimum_division_operations_to_make_array_non_decreasing", r'''<?php
// LeetCode 3326 - Minimum Division Operations to Make Array Non Decreasing
// https://leetcode.com/problems/minimum-division-operations-to-make-array-non-decreasing/

class Solution {
    function smallestProperDivisor($x) {
        for ($d = 2; $d * $d <= $x; $d++) if ($x % $d === 0) return $d;
        return $x;
    }

    function minOperations($nums) {
        $ops = 0;
        for ($i = count($nums) - 2; $i >= 0; $i--) {
            if ($nums[$i] <= $nums[$i + 1]) continue;
            while ($nums[$i] > $nums[$i + 1]) {
                $d = $this->smallestProperDivisor($nums[$i]);
                if ($d === $nums[$i]) return -1;
                $nums[$i] = intdiv($nums[$i], $d);
                $ops++;
                if ($nums[$i] > $nums[$i + 1] && $this->smallestProperDivisor($nums[$i]) === $nums[$i]) return -1;
            }
        }
        return $ops;
    }
}
''')

add("3327_check_if_dfs_strings_are_palindromes", r'''<?php
// LeetCode 3327 - Check if DFS Strings Are Palindromes
// https://leetcode.com/problems/check-if-dfs-strings-are-palindromes/

class Solution {
    public $g;
    public $s;
    public $ans;

    function isPal($t) {
        for ($i = 0, $j = strlen($t) - 1; $i < $j; $i++, $j--) {
            if ($t[$i] !== $t[$j]) return false;
        }
        return true;
    }

    function dfsStr($u) {
        $out = '';
        foreach ($this->g[$u] as $v) $out .= $this->dfsStr($v);
        $out .= $this->s[$u];
        $this->ans[$u] = $this->isPal($out);
        return $out;
    }

    function findAnswer($parent, $s) {
        $n = count($parent);
        $this->g = array_fill(0, $n, []);
        for ($i = 1; $i < $n; $i++) $this->g[$parent[$i]][] = $i;
        $this->s = $s;
        $this->ans = array_fill(0, $n, false);
        $this->dfsStr(0);
        return $this->ans;
    }
}
''')

add("3329_count_substrings_with_k_frequency_characters_ii", r'''<?php
// LeetCode 3329 - Count Substrings With K-Frequency Characters II
// https://leetcode.com/problems/count-substrings-with-k-frequency-characters-ii/

class Solution {
    function numberOfSubstrings($s, $k) {
        $n = strlen($s);
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            $freq = array_fill(0, 26, 0);
            for ($j = $i; $j < $n; $j++) {
                $freq[ord($s[$j]) - 97]++;
                $ok = false;
                foreach ($freq as $f) if ($f >= $k) { $ok = true; break; }
                if ($ok) { $ans += $n - $j; break; }
            }
        }
        return $ans;
    }
}
''')

add("3330_find_the_original_typed_string_i", r'''<?php
// LeetCode 3330 - Find the Original Typed String I
// https://leetcode.com/problems/find-the-original-typed-string-i/

class Solution {
    function possibleStringCount($word) {
        $ans = 1;
        $n = strlen($word);
        for ($i = 1; $i < $n; $i++) {
            if ($word[$i] === $word[$i - 1]) $ans++;
        }
        return $ans;
    }
}
''')

add("3331_find_subtree_sizes_after_changes", r'''<?php
// LeetCode 3331 - Find Subtree Sizes After Changes
// https://leetcode.com/problems/find-subtree-sizes-after-changes/

class Solution {
    public $g;
    public $s;
    public $newParent;
    public $last;
    public $ng;
    public $ans;

    function dfs1($u) {
        $c = ord($this->s[$u]) - 97;
        $prev = $this->last[$c];
        if ($prev !== -1) $this->newParent[$u] = $prev;
        $this->last[$c] = $u;
        foreach ($this->g[$u] as $v) $this->dfs1($v);
        $this->last[$c] = $prev;
    }

    function dfs2($u) {
        $sz = 1;
        foreach ($this->ng[$u] as $v) $sz += $this->dfs2($v);
        return $this->ans[$u] = $sz;
    }

    function findSubtreeSizes($parent, $s) {
        $n = count($parent);
        $this->g = array_fill(0, $n, []);
        for ($i = 1; $i < $n; $i++) $this->g[$parent[$i]][] = $i;
        $this->newParent = $parent;
        $this->s = $s;
        $this->last = array_fill(0, 26, -1);
        $this->dfs1(0);
        $this->ng = array_fill(0, $n, []);
        for ($i = 1; $i < $n; $i++) $this->ng[$this->newParent[$i]][] = $i;
        $this->ans = array_fill(0, $n, 0);
        $this->dfs2(0);
        return $this->ans;
    }
}
''')

add("3332_maximum_points_tourist_can_earn", r'''<?php
// LeetCode 3332 - Maximum Points Tourist Can Earn
// https://leetcode.com/problems/maximum-points-tourist-can-earn/

class Solution {
    function maxScore($n, $k, $stayScore, $travelScore) {
        $dp = array_fill(0, $n, 0);
        for ($day = 0; $day < $k; $day++) {
            $ndp = array_fill(0, $n, -(1 << 30));
            for ($dest = 0; $dest < $n; $dest++) {
                $best = -(1 << 30);
                for ($src = 0; $src < $n; $src++) {
                    $val = $dp[$src];
                    if ($src === $dest) $val += $stayScore[$day][$dest];
                    else $val += $travelScore[$src][$dest];
                    if ($val > $best) $best = $val;
                }
                $ndp[$dest] = $best;
            }
            $dp = $ndp;
        }
        $ans = $dp[0];
        for ($i = 1; $i < $n; $i++) if ($dp[$i] > $ans) $ans = $dp[$i];
        return $ans;
    }
}
''')

add("3333_find_the_original_typed_string_ii", r'''<?php
// LeetCode 3333 - Find the Original Typed String II
// https://leetcode.com/problems/find-the-original-typed-string-ii/

class Solution {
    function possibleStringCount($word, $k) {
        $mod = 1000000007;
        $groups = [];
        $n = strlen($word);
        for ($i = 0; $i < $n; ) {
            $j = $i;
            while ($j < $n && $word[$j] === $word[$i]) $j++;
            $groups[] = $j - $i;
            $i = $j;
        }
        $total = 1;
        foreach ($groups as $g) $total = $total * $g % $mod;
        if ($k <= count($groups)) return $total;
        $need = $k - 1;
        $dp = array_fill(0, $need, 0);
        $dp[0] = 1;
        foreach ($groups as $g) {
            $ndp = array_fill(0, $need, 0);
            $pref = array_fill(0, $need + 1, 0);
            for ($i = 0; $i < $need; $i++) $pref[$i + 1] = ($pref[$i] + $dp[$i]) % $mod;
            for ($s = 0; $s < $need; $s++) {
                $lo = $s - $g;
                if ($lo < 0) $lo = 0;
                $hi = $s - 1;
                if ($hi >= 0) $ndp[$s] = ($pref[$hi + 1] - $pref[$lo] + $mod) % $mod;
            }
            $dp = $ndp;
        }
        $bad = 0;
        foreach ($dp as $v) $bad = ($bad + $v) % $mod;
        return ($total - $bad + $mod) % $mod;
    }
}
''')

add("3334_find_the_maximum_factor_score_of_array", r'''<?php
// LeetCode 3334 - Find the Maximum Factor Score of Array
// https://leetcode.com/problems/find-the-maximum-factor-score-of-array/

class Solution {
    function gcd($a, $b) {
        while ($b !== 0) { $t = $a % $b; $a = $b; $b = $t; }
        return $a;
    }

    function lcm($a, $b) {
        return intdiv($a, $this->gcd($a, $b)) * $b;
    }

    function maxScore($nums) {
        $n = count($nums);
        $gcdAll = $nums[0];
        $lcmAll = $nums[0];
        for ($i = 1; $i < $n; $i++) {
            $gcdAll = $this->gcd($gcdAll, $nums[$i]);
            $lcmAll = $this->lcm($lcmAll, $nums[$i]);
        }
        $ans = $gcdAll * $lcmAll;
        for ($skip = 0; $skip < $n; $skip++) {
            $g = 0;
            $l = 1;
            $first = true;
            for ($i = 0; $i < $n; $i++) {
                if ($i === $skip) continue;
                if ($first) { $g = $l = $nums[$i]; $first = false; }
                else { $g = $this->gcd($g, $nums[$i]); $l = $this->lcm($l, $nums[$i]); }
            }
            if ($first) continue;
            $v = $g * $l;
            if ($v > $ans) $ans = $v;
        }
        return $ans;
    }
}
''')

add("3335_total_characters_in_string_after_transformations_i", r'''<?php
// LeetCode 3335 - Total Characters in String After Transformations I
// https://leetcode.com/problems/total-characters-in-string-after-transformations-i/

class Solution {
    function lengthAfterTransformations($s, $t) {
        $mod = 1000000007;
        $cnt = array_fill(0, 26, 0);
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) $cnt[ord($s[$i]) - 97]++;
        for ($step = 0; $step < $t; $step++) {
            $ncnt = array_fill(0, 26, 0);
            for ($i = 0; $i < 25; $i++) $ncnt[$i + 1] = ($ncnt[$i + 1] + $cnt[$i]) % $mod;
            $ncnt[0] = ($ncnt[0] + $cnt[25]) % $mod;
            $ncnt[1] = ($ncnt[1] + $cnt[25]) % $mod;
            $cnt = $ncnt;
        }
        $ans = 0;
        foreach ($cnt as $v) $ans = ($ans + $v) % $mod;
        return $ans;
    }
}
''')

add("3336_find_the_number_of_subsequences_with_equal_gcd", r'''<?php
// LeetCode 3336 - Find the Number of Subsequences With Equal GCD
// https://leetcode.com/problems/find-the-number-of-subsequences-with-equal-gcd/

class Solution {
    function gcd($a, $b) {
        if ($a === 0) return $b;
        while ($b !== 0) { $t = $a % $b; $a = $b; $b = $t; }
        return $a;
    }

    function subsequencePairCount($nums) {
        $mod = 1000000007;
        $maxV = 0;
        foreach ($nums as $x) if ($x > $maxV) $maxV = $x;
        $dp = [];
        for ($a = 0; $a <= $maxV; $a++) $dp[$a] = array_fill(0, $maxV + 1, 0);
        $dp[0][0] = 1;
        foreach ($nums as $x) {
            $ndp = [];
            for ($a = 0; $a <= $maxV; $a++) {
                $ndp[$a] = [];
                for ($b = 0; $b <= $maxV; $b++) $ndp[$a][$b] = $dp[$a][$b];
            }
            for ($a = 0; $a <= $maxV; $a++) {
                for ($b = 0; $b <= $maxV; $b++) {
                    if ($dp[$a][$b] === 0) continue;
                    $na = $a === 0 ? $x : $this->gcd($a, $x);
                    $nb = $b === 0 ? $x : $this->gcd($b, $x);
                    $ndp[$na][$b] = ($ndp[$na][$b] + $dp[$a][$b]) % $mod;
                    $ndp[$a][$nb] = ($ndp[$a][$nb] + $dp[$a][$b]) % $mod;
                }
            }
            $dp = $ndp;
        }
        $ans = 0;
        for ($g = 1; $g <= $maxV; $g++) $ans = ($ans + $dp[$g][$g]) % $mod;
        return $ans;
    }
}
''')

add("3337_total_characters_in_string_after_transformations_ii", r'''<?php
// LeetCode 3337 - Total Characters in String After Transformations II
// https://leetcode.com/problems/total-characters-in-string-after-transformations-ii/

class Solution {
    function matMul($a, $b, $mod) {
        $n = count($a);
        $c = [];
        for ($i = 0; $i < $n; $i++) $c[$i] = array_fill(0, $n, 0);
        for ($i = 0; $i < $n; $i++) {
            for ($k = 0; $k < $n; $k++) {
                if ($a[$i][$k] === 0) continue;
                for ($j = 0; $j < $n; $j++) {
                    $c[$i][$j] = ($c[$i][$j] + $a[$i][$k] * $b[$k][$j] % $mod) % $mod;
                }
            }
        }
        return $c;
    }

    function matPow($a, $e, $mod) {
        $n = count($a);
        $r = [];
        for ($i = 0; $i < $n; $i++) {
            $r[$i] = array_fill(0, $n, 0);
            $r[$i][$i] = 1;
        }
        while ($e > 0) {
            if ($e & 1) $r = $this->matMul($r, $a, $mod);
            $a = $this->matMul($a, $a, $mod);
            $e >>= 1;
        }
        return $r;
    }

    function lengthAfterTransformations($s, $t, $nums) {
        $mod = 1000000007;
        $mat = [];
        for ($i = 0; $i < 26; $i++) $mat[$i] = array_fill(0, 26, 0);
        for ($i = 0; $i < 26; $i++) {
            for ($j = 1; $j <= $nums[$i]; $j++) $mat[$i][($i + $j) % 26] = 1;
        }
        $mat = $this->matPow($mat, $t, $mod);
        $cnt = array_fill(0, 26, 0);
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) $cnt[ord($s[$i]) - 97]++;
        $ans = 0;
        for ($i = 0; $i < 26; $i++) {
            for ($j = 0; $j < 26; $j++) {
                $ans = ($ans + $cnt[$i] * $mat[$i][$j] % $mod) % $mod;
            }
        }
        return $ans;
    }
}
''')

add("3339_find_the_number_of_k_even_arrays", r'''<?php
// LeetCode 3339 - Find the Number of K-Even Arrays
// https://leetcode.com/problems/find-the-number-of-k-even-arrays/

class Solution {
    function countOfArrays($n, $m, $k) {
        $mod = 1000000007;
        $even = intdiv($m, 2);
        $odd = $m - $even;
        $dp = [];
        for ($i = 0; $i <= $n; $i++) {
            $dp[$i] = [];
            for ($j = 0; $j <= $k; $j++) $dp[$i][$j] = [0, 0];
        }
        $dp[1][0][0] = $odd;
        $dp[1][0][1] = $even;
        for ($i = 1; $i < $n; $i++) {
            for ($j = 0; $j <= $k; $j++) {
                $dp[$i + 1][$j][0] = ($dp[$i + 1][$j][0] + (($dp[$i][$j][0] + $dp[$i][$j][1]) % $mod) * $odd % $mod) % $mod;
                $dp[$i + 1][$j][1] = ($dp[$i + 1][$j][1] + $dp[$i][$j][0] * $even % $mod) % $mod;
                if ($j < $k) {
                    $dp[$i + 1][$j + 1][1] = ($dp[$i + 1][$j + 1][1] + $dp[$i][$j][1] * $even % $mod) % $mod;
                }
            }
        }
        return ($dp[$n][$k][0] + $dp[$n][$k][1]) % $mod;
    }
}
''')

add("3340_check_balanced_string", r'''<?php
// LeetCode 3340 - Check Balanced String
// https://leetcode.com/problems/check-balanced-string/

class Solution {
    function isBalanced($num) {
        $even = 0;
        $odd = 0;
        $n = strlen($num);
        for ($i = 0; $i < $n; $i++) {
            if ($i % 2 === 0) $even += ord($num[$i]) - 48;
            else $odd += ord($num[$i]) - 48;
        }
        return $even === $odd;
    }
}
''')


written = 0
for folder, body in SOLUTIONS.items():
    path = ROOT / folder / "solution.php"
    path.write_text(body, encoding="utf-8", newline="\n")
    written += 1
print(f"wrote {written}")

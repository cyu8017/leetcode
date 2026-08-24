#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
SOLUTIONS = {}

def add(folder, body):
    SOLUTIONS[folder] = body


add("3849_maximum_bitwise_xor_after_rearrangement", r'''<?php
// LeetCode 3849 - Maximum Bitwise XOR After Rearrangement
// https://leetcode.com/problems/maximum-bitwise-xor-after-rearrangement/

class Solution {
    function maximumXor($s, $t) {
        $cnt = [0, 0];
        $nt = strlen($t);
        for ($i = 0; $i < $nt; $i++) $cnt[ord($t[$i]) - 48]++;
        $n = strlen($s);
        $ans = [];
        for ($i = 0; $i < $n; $i++) {
            $x = ord($s[$i]) - 48;
            if ($cnt[$x ^ 1] > 0) {
                $cnt[$x ^ 1]--;
                $ans[$i] = '1';
            } else {
                $cnt[$x]--;
                $ans[$i] = '0';
            }
        }
        return implode('', $ans);
    }
}
''')

add("3850_count_sequences_to_k", r'''<?php
// LeetCode 3850 - Count Sequences to K
// https://leetcode.com/problems/count-sequences-to-k/

class Solution {
    public $nums;
    public $k;
    public $f;
    function gcd($a, $b) {
        while ($b !== 0) {
            $t = $a % $b;
            $a = $b;
            $b = $t;
        }
        return $a;
    }
    function dfs($i, $p, $q) {
        if ($i === count($this->nums)) return ($p === $this->k && $q === 1) ? 1 : 0;
        $key = $i . ',' . $p . ',' . $q;
        if (isset($this->f[$key])) return $this->f[$key];
        $res = $this->dfs($i + 1, $p, $q);
        $x = $this->nums[$i];
        $g1 = $this->gcd($p * $x, $q);
        $res += $this->dfs($i + 1, intdiv($p * $x, $g1), intdiv($q, $g1));
        $g2 = $this->gcd($p, $q * $x);
        $res += $this->dfs($i + 1, intdiv($p, $g2), intdiv($q * $x, $g2));
        $this->f[$key] = $res;
        return $res;
    }
    function countSequences($nums, $k) {
        $this->nums = $nums;
        $this->k = $k;
        $this->f = [];
        return $this->dfs(0, 1, 1);
    }
}
''')

add("3851_maximum_requests_without_violating_the_limit", r'''<?php
// LeetCode 3851 - Maximum Requests Without Violating the Limit
// https://leetcode.com/problems/maximum-requests-without-violating-the-limit/

class Solution {
    function maxRequests($requests, $k, $window) {
        $g = [];
        foreach ($requests as $r) {
            $g[$r[0]][] = $r[1];
        }
        $ans = count($requests);
        foreach ($g as $ts) {
            sort($ts);
            $kept = [];
            foreach ($ts as $t) {
                while (count($kept) > 0 && $t - $kept[0] > $window) array_shift($kept);
                if (count($kept) < $k) $kept[] = $t;
                else $ans--;
            }
        }
        return $ans;
    }
}
''')

add("3852_smallest_pair_with_different_frequencies", r'''<?php
// LeetCode 3852 - Smallest Pair With Different Frequencies
// https://leetcode.com/problems/smallest-pair-with-different-frequencies/

class Solution {
    function minDistinctFreqPair($nums) {
        $cnt = [];
        foreach ($nums as $v) $cnt[$v] = ($cnt[$v] ?? 0) + 1;
        $x = $nums[0];
        foreach ($nums as $v) $x = min($x, $v);
        $minY = PHP_INT_MAX;
        foreach ($cnt as $y => $_) {
            if ($y < $minY && $cnt[$x] !== $cnt[$y]) $minY = $y;
        }
        if ($minY === PHP_INT_MAX) return [-1, -1];
        return [$x, $minY];
    }
}
''')

add("3853_merge_close_characters", r'''<?php
// LeetCode 3853 - Merge Close Characters
// https://leetcode.com/problems/merge-close-characters/

class Solution {
    function mergeCharacters($s, $k) {
        $last = [];
        $ans = '';
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $c = $s[$i];
            $cur = strlen($ans);
            if (isset($last[$c]) && $cur - $last[$c] <= $k) continue;
            $ans .= $c;
            $last[$c] = $cur;
        }
        return $ans;
    }
}
''')

add("3854_minimum_operations_to_make_array_parity_alternating", r'''<?php
// LeetCode 3854 - Minimum Operations to Make Array Parity Alternating
// https://leetcode.com/problems/minimum-operations-to-make-array-parity-alternating/

class Solution {
    function f($nums, $k, $mn, $mx) {
        $cnt = 0;
        $a = PHP_INT_MAX;
        $b = PHP_INT_MIN;
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            $x = $nums[$i];
            if ((($x - $i) & 1) !== $k) {
                $cnt++;
                if ($x === $mn) $x++;
                else if ($x === $mx) $x--;
            }
            $a = min($a, $x);
            $b = max($b, $x);
        }
        return [$cnt, max(1, $b - $a)];
    }
    function makeParityAlternating($nums) {
        if (count($nums) === 1) return [0, 0];
        $mn = $nums[0];
        $mx = $nums[0];
        foreach ($nums as $x) { $mn = min($mn, $x); $mx = max($mx, $x); }
        $r0 = $this->f($nums, 0, $mn, $mx);
        $r1 = $this->f($nums, 1, $mn, $mx);
        if ($r0[0] !== $r1[0]) return $r0[0] < $r1[0] ? $r0 : $r1;
        return $r0[1] <= $r1[1] ? $r0 : $r1;
    }
}
''')

add("3855_sum_of_k_digit_numbers_in_a_range", r'''<?php
// LeetCode 3855 - Sum of K Digit Numbers in a Range
// https://leetcode.com/problems/sum-of-k-digit-numbers-in-a-range/

class Solution {
    function qpow($a, $n, $mod) {
        $a %= $mod;
        $res = 1;
        while ($n > 0) {
            if ($n & 1) $res = $res * $a % $mod;
            $a = $a * $a % $mod;
            $n >>= 1;
        }
        return $res;
    }
    function sumOfNumbers($l, $r, $k) {
        $MOD = 1000000007;
        $n = $r - $l + 1;
        $sum = (int)((($l + $r) * $n / 2) % $MOD);
        $part1 = $this->qpow($n % $MOD, $k - 1, $MOD);
        $part2 = ($this->qpow(10, $k, $MOD) - 1 + $MOD) % $MOD;
        $inv9 = $this->qpow(9, $MOD - 2, $MOD);
        $ans = $sum;
        $ans = $ans * $part1 % $MOD;
        $ans = $ans * $part2 % $MOD;
        $ans = $ans * $inv9 % $MOD;
        return $ans;
    }
}
''')

add("3856_trim_trailing_vowels", r'''<?php
// LeetCode 3856 - Trim Trailing Vowels
// https://leetcode.com/problems/trim-trailing-vowels/

class Solution {
    function isVowel($c) {
        return $c === 'a' || $c === 'e' || $c === 'i' || $c === 'o' || $c === 'u';
    }
    function trimTrailingVowels($s) {
        $i = strlen($s) - 1;
        while ($i >= 0 && $this->isVowel($s[$i])) $i--;
        return substr($s, 0, $i + 1);
    }
}
''')

add("3857_minimum_cost_to_split_into_ones", r'''<?php
// LeetCode 3857 - Minimum Cost to Split Into Ones
// https://leetcode.com/problems/minimum-cost-to-split-into-ones/

class Solution {
    function minCost($n) {
        return $n * ($n - 1) / 2;
    }
}
''')

add("3858_minimum_bitwise_or_from_grid", r'''<?php
// LeetCode 3858 - Minimum Bitwise OR From Grid
// https://leetcode.com/problems/minimum-bitwise-or-from-grid/

class Solution {
    function bitLen($x) {
        if ($x === 0) return 0;
        $n = 0;
        while ($x > 0) { $n++; $x >>= 1; }
        return $n;
    }
    function minimumOR($grid) {
        $mx = 0;
        foreach ($grid as $row) foreach ($row as $x) $mx = max($mx, $x);
        $m = $this->bitLen($mx);
        $ans = 0;
        for ($i = $m - 1; $i >= 0; $i--) {
            $mask = $ans | ((1 << $i) - 1);
            foreach ($grid as $row) {
                $found = false;
                foreach ($row as $x) {
                    if (($x | $mask) === $mask) { $found = true; break; }
                }
                if (!$found) {
                    $ans |= 1 << $i;
                    break;
                }
            }
        }
        return $ans;
    }
}
''')

add("3859_count_subarrays_with_k_distinct_integers", r'''<?php
// LeetCode 3859 - Count Subarrays With K Distinct Integers
// https://leetcode.com/problems/count-subarrays-with-k-distinct-integers/

class Solution {
    public $nums;
    public $k;
    public $m;
    function f($lim) {
        $cnt = [];
        $ans = 0;
        $l = 0;
        $t = 0;
        foreach ($this->nums as $x) {
            $c = ($cnt[$x] ?? 0) + 1;
            $cnt[$x] = $c;
            if ($c === $this->m) $t++;
            while (count($cnt) >= $lim && $t >= $this->k) {
                $y = $this->nums[$l++];
                $cy = $cnt[$y] - 1;
                if ($cy === $this->m - 1) $t--;
                if ($cy === 0) unset($cnt[$y]);
                else $cnt[$y] = $cy;
            }
            $ans += $l;
        }
        return $ans;
    }
    function countSubarrays($nums, $k, $m) {
        $this->nums = $nums;
        $this->k = $k;
        $this->m = $m;
        return $this->f($k) - $this->f($k + 1);
    }
}
''')

add("3860_unique_email_groups", r'''<?php
// LeetCode 3860 - Unique Email Groups
// https://leetcode.com/problems/unique-email-groups/

class Solution {
    function uniqueEmailGroups($emails) {
        $st = [];
        foreach ($emails as $email) {
            $at = strpos($email, '@');
            $local = substr($email, 0, $at);
            $domain = strtolower(substr($email, $at + 1));
            $plus = strpos($local, '+');
            if ($plus !== false) $local = substr($local, 0, $plus);
            $cleaned = '';
            $len = strlen($local);
            for ($i = 0; $i < $len; $i++) {
                $c = $local[$i];
                if ($c !== '.') $cleaned .= strtolower($c);
            }
            $st[$cleaned . $domain] = true;
        }
        return count($st);
    }
}
''')

add("3861_minimum_capacity_box", r'''<?php
// LeetCode 3861 - Minimum Capacity Box
// https://leetcode.com/problems/minimum-capacity-box/

class Solution {
    function minimumIndex($capacity, $itemSize) {
        $ans = -1;
        $n = count($capacity);
        for ($i = 0; $i < $n; $i++) {
            if ($capacity[$i] >= $itemSize && ($ans === -1 || $capacity[$i] < $capacity[$ans])) $ans = $i;
        }
        return $ans;
    }
}
''')

add("3862_find_the_smallest_balanced_index", r'''<?php
// LeetCode 3862 - Find the Smallest Balanced Index
// https://leetcode.com/problems/find-the-smallest-balanced-index/

class Solution {
    function smallestBalancedIndex($nums) {
        $s = 0;
        $p = 1;
        foreach ($nums as $x) $s += $x;
        for ($i = count($nums) - 1; $i >= 0; $i--) {
            $s -= $nums[$i];
            if ($s === $p) return $i;
            $p *= $nums[$i];
            if ($p >= $s) break;
        }
        return -1;
    }
}
''')

add("3863_minimum_operations_to_sort_a_string", r'''<?php
// LeetCode 3863 - Minimum Operations to Sort a String
// https://leetcode.com/problems/minimum-operations-to-sort-a-string/

class Solution {
    function minOperations($s) {
        $n = strlen($s);
        $sorted = true;
        for ($i = 1; $i < $n; $i++) {
            if ($s[$i] < $s[$i - 1]) { $sorted = false; break; }
        }
        if ($sorted) return 0;
        if ($n === 2) return -1;
        $mn = $s[0];
        $mx = $s[0];
        for ($i = 0; $i < $n; $i++) {
            $c = $s[$i];
            if ($c < $mn) $mn = $c;
            if ($c > $mx) $mx = $c;
        }
        if ($s[0] === $mn || $s[$n - 1] === $mx) return 1;
        for ($i = 1; $i < $n - 1; $i++) {
            if ($s[$i] === $mn || $s[$i] === $mx) return 2;
        }
        return 3;
    }
}
''')

add("3864_minimum_cost_to_partition_a_binary_string", r'''<?php
// LeetCode 3864 - Minimum Cost to Partition a Binary String
// https://leetcode.com/problems/minimum-cost-to-partition-a-binary-string/

class Solution {
    public $pre;
    public $encCost;
    public $flatCost;
    function dfs($l, $r) {
        $x = $this->pre[$r] - $this->pre[$l];
        $res = $x !== 0 ? ($r - $l) * $x * $this->encCost : $this->flatCost;
        if (($r - $l) % 2 === 0) {
            $m = intdiv($l + $r, 2);
            $res = min($res, $this->dfs($l, $m) + $this->dfs($m, $r));
        }
        return $res;
    }
    function minCost($s, $encCost, $flatCost) {
        $n = strlen($s);
        $this->encCost = $encCost;
        $this->flatCost = $flatCost;
        $this->pre = array_fill(0, $n + 1, 0);
        for ($i = 1; $i <= $n; $i++) $this->pre[$i] = $this->pre[$i - 1] + (ord($s[$i - 1]) - 48);
        return $this->dfs(0, $n);
    }
}
''')

add("3865_reverse_k_subarrays", r'''<?php
// LeetCode 3865 - Reverse K Subarrays
// https://leetcode.com/problems/reverse-k-subarrays/

class Solution {
    function reverseSubarrays($nums, $k) {
        $n = count($nums);
        $m = intdiv($n, $k);
        for ($i = 0; $i < $n; $i += $m) {
            $lo = $i;
            $hi = $i + $m - 1;
            while ($lo < $hi) {
                $t = $nums[$lo];
                $nums[$lo] = $nums[$hi];
                $nums[$hi] = $t;
                $lo++;
                $hi--;
            }
        }
        return $nums;
    }
}
''')

add("3866_first_unique_even_element", r'''<?php
// LeetCode 3866 - First Unique Even Element
// https://leetcode.com/problems/first-unique-even-element/

class Solution {
    function firstUniqueEven($nums) {
        $cnt = array_fill(0, 101, 0);
        foreach ($nums as $x) $cnt[$x]++;
        foreach ($nums as $x) {
            if ($x % 2 === 0 && $cnt[$x] === 1) return $x;
        }
        return -1;
    }
}
''')

add("3867_sum_of_gcd_of_formed_pairs", r'''<?php
// LeetCode 3867 - Sum of GCD of Formed Pairs
// https://leetcode.com/problems/sum-of-gcd-of-formed-pairs/

class Solution {
    function Gcd($a, $b) {
        while ($b !== 0) {
            $t = $a % $b;
            $a = $b;
            $b = $t;
        }
        return $a;
    }
    function gcdSum($nums) {
        $n = count($nums);
        $prefixGcd = [];
        $mx = 0;
        for ($i = 0; $i < $n; $i++) {
            $mx = max($mx, $nums[$i]);
            $prefixGcd[$i] = $this->Gcd($nums[$i], $mx);
        }
        sort($prefixGcd);
        $ans = 0;
        for ($i = 0; $i < intdiv($n, 2); $i++) $ans += $this->Gcd($prefixGcd[$i], $prefixGcd[$n - $i - 1]);
        return $ans;
    }
}
''')

add("3868_minimum_cost_to_equalize_arrays_using_swaps", r'''<?php
// LeetCode 3868 - Minimum Cost to Equalize Arrays Using Swaps
// https://leetcode.com/problems/minimum-cost-to-equalize-arrays-using-swaps/

class Solution {
    function minCost($nums1, $nums2) {
        $cnt2 = [];
        foreach ($nums2 as $x) $cnt2[$x] = ($cnt2[$x] ?? 0) + 1;
        $cnt1 = [];
        foreach ($nums1 as $x) {
            $c = $cnt2[$x] ?? 0;
            if ($c > 0) $cnt2[$x] = $c - 1;
            else $cnt1[$x] = ($cnt1[$x] ?? 0) + 1;
        }
        $ans = 0;
        foreach ($cnt1 as $v) {
            if ($v % 2 === 1) return -1;
            $ans += intdiv($v, 2);
        }
        foreach ($cnt2 as $v) {
            if ($v % 2 === 1) return -1;
        }
        return $ans;
    }
}
''')

add("3869_count_fancy_numbers_in_a_range", r'''<?php
// LeetCode 3869 - Count Fancy Numbers in a Range
// https://leetcode.com/problems/count-fancy-numbers-in-a-range/

class Solution {
    public $num;
    public $n;
    public $f;
    function check($s) {
        if ($s < 100) return $s % 11 !== 0;
        $mid = intdiv($s, 10) % 10;
        $last = $s % 10;
        return $mid > 1 && $mid < $last;
    }
    function dfs($pos, $s, $prev, $st, $lim) {
        if ($pos >= $this->n) {
            if ($st !== 3) return 1;
            return $this->check($s) ? 1 : 0;
        }
        if (!$lim && $this->f[$pos][$s][$prev][$st] !== -1) return $this->f[$pos][$s][$prev][$st];
        $up = $lim ? ord($this->num[$pos]) - 48 : 9;
        $res = 0;
        for ($i = 0; $i <= $up; $i++) {
            $nxtSt = $st;
            if ($st === 0) {
                if ($prev === 0) $nxtSt = 0;
                else if ($i > $prev) $nxtSt = 1;
                else if ($i < $prev) $nxtSt = 2;
                else $nxtSt = 3;
            } else if ($st === 1) {
                $nxtSt = $i > $prev ? 1 : 3;
            } else if ($st === 2) {
                $nxtSt = $i < $prev ? 2 : 3;
            } else {
                $nxtSt = 3;
            }
            $res += $this->dfs($pos + 1, $s + $i, $i, $nxtSt, $lim && $i === $up);
        }
        if (!$lim) $this->f[$pos][$s][$prev][$st] = $res;
        return $res;
    }
    function calc($x) {
        if ($x < 0) return 0;
        $this->num = strval($x);
        $this->n = strlen($this->num);
        $this->f = [];
        for ($i = 0; $i < $this->n; $i++) {
            $this->f[$i] = [];
            for ($s = 0; $s <= 9 * $this->n; $s++) {
                $this->f[$i][$s] = [];
                for ($p = 0; $p < 10; $p++) $this->f[$i][$s][$p] = array_fill(0, 4, -1);
            }
        }
        return $this->dfs(0, 0, 0, 0, true);
    }
    function countFancy($l, $r) {
        return $this->calc($r) - $this->calc($l - 1);
    }
}
''')

add("3870_count_commas_in_range", r'''<?php
// LeetCode 3870 - Count Commas in Range
// https://leetcode.com/problems/count-commas-in-range/

class Solution {
    function countCommas($n) {
        return max(0, $n - 999);
    }
}
''')

add("3871_count_commas_in_range_ii", r'''<?php
// LeetCode 3871 - Count Commas in Range II
// https://leetcode.com/problems/count-commas-in-range-ii/

class Solution {
    function countCommas($n) {
        $ans = 0;
        for ($x = 1000; $x <= $n; $x *= 1000) $ans += $n - $x + 1;
        return $ans;
    }
}
''')

add("3872_longest_arithmetic_sequence_after_changing_at_most_one_element", r'''<?php
// LeetCode 3872 - Longest Arithmetic Sequence After Changing at Most One Element
// https://leetcode.com/problems/longest-arithmetic-sequence-after-changing-at-most-one-element/

class Solution {
    function longestArithmetic($nums) {
        $n = count($nums);
        $d = array_fill(0, $n, 0);
        for ($i = 1; $i < $n; $i++) $d[$i] = $nums[$i] - $nums[$i - 1];
        $f = array_fill(0, $n, 2);
        $g = array_fill(0, $n, 2);
        $f[0] = 1;
        $g[$n - 1] = 1;
        for ($i = 2; $i < $n; $i++) {
            if ($d[$i] === $d[$i - 1]) $f[$i] = $f[$i - 1] + 1;
        }
        for ($i = $n - 3; $i >= 0; $i--) {
            if ($d[$i + 1] === $d[$i + 2]) $g[$i] = $g[$i + 1] + 1;
        }
        $ans = 3;
        for ($i = 0; $i < $n; $i++) {
            $ans = max($ans, max($f[$i], $g[$i]));
            if ($i > 0) $ans = max($ans, $f[$i - 1] + 1);
            if ($i + 1 < $n) $ans = max($ans, $g[$i + 1] + 1);
            if ($i > 0 && $i < $n - 1) {
                $diff = $nums[$i + 1] - $nums[$i - 1];
                if ($diff % 2 === 0) {
                    $diff = intdiv($diff, 2);
                    $k = 3;
                    if ($i > 1 && $diff === $d[$i - 1]) $k += $f[$i - 1] - 1;
                    if ($i < $n - 2 && $diff === $d[$i + 2]) $k += $g[$i + 1] - 1;
                    $ans = max($ans, $k);
                }
            }
        }
        return $ans;
    }
}
''')

add("3873_maximum_points_activated_with_one_addition", r'''<?php
// LeetCode 3873 - Maximum Points Activated With One Addition
// https://leetcode.com/problems/maximum-points-activated-with-one-addition/

class Solution {
    public $p;
    public $size;
    function find($x) {
        if (!isset($this->p[$x])) { $this->p[$x] = $x; $this->size[$x] = 1; }
        if ($this->p[$x] !== $x) $this->p[$x] = $this->find($this->p[$x]);
        return $this->p[$x];
    }
    function unite($a, $b) {
        $pa = $this->find($a);
        $pb = $this->find($b);
        if ($pa === $pb) return false;
        if ($this->size[$pa] > $this->size[$pb]) {
            $this->p[$pb] = $pa;
            $this->size[$pa] += $this->size[$pb];
        } else {
            $this->p[$pa] = $pb;
            $this->size[$pb] += $this->size[$pa];
        }
        return true;
    }
    function maxActivated($points) {
        $this->p = [];
        $this->size = [];
        $m = 3000000000;
        foreach ($points as $pt) $this->unite($pt[0], $pt[1] + $m);
        $cnt = [];
        foreach ($points as $pt) {
            $r = $this->find($pt[0]);
            $cnt[$r] = ($cnt[$r] ?? 0) + 1;
        }
        $mx1 = 0;
        $mx2 = 0;
        foreach ($cnt as $x) {
            if ($mx1 < $x) { $mx2 = $mx1; $mx1 = $x; }
            else if ($mx2 < $x) $mx2 = $x;
        }
        return $mx1 + $mx2 + 1;
    }
}
''')

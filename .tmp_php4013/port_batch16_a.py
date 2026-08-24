#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
SOLUTIONS = {}

def add(folder, body):
    SOLUTIONS[folder] = body


add("3286_find_a_safe_walk_through_a_grid", r'''<?php
// LeetCode 3286 - Find a Safe Walk Through a Grid
// https://leetcode.com/problems/find-a-safe-walk-through-a-grid/

class Solution {
    function findSafeWalk($grid, $health) {
        $m = count($grid);
        $n = count($grid[0]);
        $vis = [];
        for ($i = 0; $i < $m; $i++) $vis[$i] = array_fill(0, $n, -1);
        $qh = $health - $grid[0][0];
        if ($qh <= 0) return false;
        $q = [[0, 0, $qh]];
        $vis[0][0] = $qh;
        $dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]];
        $head = 0;
        while ($head < count($q)) {
            $cur = $q[$head++];
            if ($cur[0] === $m - 1 && $cur[1] === $n - 1) return true;
            foreach ($dirs as $d) {
                $nr = $cur[0] + $d[0];
                $nc = $cur[1] + $d[1];
                if ($nr < 0 || $nc < 0 || $nr >= $m || $nc >= $n) continue;
                $nh = $cur[2] - $grid[$nr][$nc];
                if ($nh <= 0) continue;
                if ($nh > $vis[$nr][$nc]) {
                    $vis[$nr][$nc] = $nh;
                    $q[] = [$nr, $nc, $nh];
                }
            }
        }
        return false;
    }
}
''')

add("3287_find_the_maximum_sequence_value_of_array", r'''<?php
// LeetCode 3287 - Find the Maximum Sequence Value of Array
// https://leetcode.com/problems/find-the-maximum-sequence-value-of-array/

class Solution {
    function maxValue($nums, $k) {
        $n = count($nums);
        $MAX = 128;
        $left = [];
        for ($i = 0; $i <= $n; $i++) {
            $left[$i] = [];
            for ($j = 0; $j <= $k; $j++) $left[$i][$j] = array_fill(0, $MAX, false);
        }
        $left[0][0][0] = true;
        for ($i = 0; $i < $n; $i++) {
            for ($j = 0; $j <= $k; $j++) {
                for ($v = 0; $v < $MAX; $v++) {
                    if (!$left[$i][$j][$v]) continue;
                    $left[$i + 1][$j][$v] = true;
                    if ($j < $k) $left[$i + 1][$j + 1][$v | $nums[$i]] = true;
                }
            }
        }
        $right = [];
        for ($i = 0; $i <= $n; $i++) {
            $right[$i] = [];
            for ($j = 0; $j <= $k; $j++) $right[$i][$j] = array_fill(0, $MAX, false);
        }
        $right[$n][0][0] = true;
        for ($i = $n - 1; $i >= 0; $i--) {
            for ($j = 0; $j <= $k; $j++) {
                for ($v = 0; $v < $MAX; $v++) {
                    if (!$right[$i + 1][$j][$v]) continue;
                    $right[$i][$j][$v] = true;
                    if ($j < $k) $right[$i][$j + 1][$v | $nums[$i]] = true;
                }
            }
        }
        $ans = 0;
        for ($mid = $k; $mid + $k <= $n; $mid++) {
            for ($a = 0; $a < $MAX; $a++) {
                if (!$left[$mid][$k][$a]) continue;
                for ($b = 0; $b < $MAX; $b++) {
                    if ($right[$mid][$k][$b] && ($a ^ $b) > $ans) $ans = $a ^ $b;
                }
            }
        }
        return $ans;
    }
}
''')

add("3288_length_of_the_longest_increasing_path", r'''<?php
// LeetCode 3288 - Length of the Longest Increasing Path
// https://leetcode.com/problems/length-of-the-longest-increasing-path/

class Solution {
    function lis($a) {
        $tails = [];
        foreach ($a as $x) {
            $lo = 0;
            $hi = count($tails);
            while ($lo < $hi) {
                $mid = ($lo + $hi) >> 1;
                if ($tails[$mid] < $x) $lo = $mid + 1;
                else $hi = $mid;
            }
            if ($lo === count($tails)) $tails[] = $x;
            else $tails[$lo] = $x;
        }
        return count($tails);
    }

    function maxPathLength($coordinates, $k) {
        $n = count($coordinates);
        $arr = [];
        for ($i = 0; $i < $n; $i++) $arr[] = [$coordinates[$i][0], $coordinates[$i][1], $i];
        usort($arr, function($a, $b) {
            if ($a[0] === $b[0]) return $b[1] <=> $a[1];
            return $a[0] <=> $b[0];
        });
        $kx = $coordinates[$k][0];
        $ky = $coordinates[$k][1];
        $left = [];
        $right = [];
        foreach ($arr as $p) {
            if ($p[0] < $kx && $p[1] < $ky) $left[] = $p[1];
            if ($p[0] > $kx && $p[1] > $ky) $right[] = $p[1];
        }
        return $this->lis($left) + 1 + $this->lis($right);
    }
}
''')

add("3289_the_two_sneaky_numbers_of_digitville", r'''<?php
// LeetCode 3289 - The Two Sneaky Numbers of Digitville
// https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/

class Solution {
    function getSneakyNumbers($nums) {
        $seen = [];
        $ans = [];
        foreach ($nums as $x) {
            if (isset($seen[$x])) $ans[] = $x;
            else $seen[$x] = true;
        }
        return $ans;
    }
}
''')

add("3290_maximum_multiplication_score", r'''<?php
// LeetCode 3290 - Maximum Multiplication Score
// https://leetcode.com/problems/maximum-multiplication-score/

class Solution {
    function maxScore($a, $b) {
        $neg = -1 << 62;
        $dp = [0, $neg, $neg, $neg, $neg];
        foreach ($b as $x) {
            for ($k = 4; $k >= 1; $k--) {
                if ($dp[$k - 1] === $neg) continue;
                $v = $dp[$k - 1] + $a[$k - 1] * $x;
                if ($v > $dp[$k]) $dp[$k] = $v;
            }
        }
        return $dp[4];
    }
}
''')

add("3291_minimum_number_of_valid_strings_to_form_target_i", r'''<?php
// LeetCode 3291 - Minimum Number of Valid Strings to Form Target I
// https://leetcode.com/problems/minimum-number-of-valid-strings-to-form-target-i/

class Solution {
    function minValidStrings($words, $target) {
        $n = strlen($target);
        $inf = 1000000000;
        $dp = array_fill(0, $n + 1, $inf);
        $dp[0] = 0;
        $root = ['next' => array_fill(0, 26, null)];
        foreach ($words as $w) {
            $cur =& $root;
            $len = strlen($w);
            for ($i = 0; $i < $len; $i++) {
                $ci = ord($w[$i]) - 97;
                if ($cur['next'][$ci] === null) $cur['next'][$ci] = ['next' => array_fill(0, 26, null)];
                $cur =& $cur['next'][$ci];
            }
            unset($cur);
        }
        for ($i = 0; $i < $n; $i++) {
            if ($dp[$i] === $inf) continue;
            $cur =& $root;
            for ($j = $i; $j < $n; $j++) {
                $ci = ord($target[$j]) - 97;
                if ($cur['next'][$ci] === null) break;
                $cur =& $cur['next'][$ci];
                if ($dp[$i] + 1 < $dp[$j + 1]) $dp[$j + 1] = $dp[$i] + 1;
            }
            unset($cur);
        }
        return $dp[$n] === $inf ? -1 : $dp[$n];
    }
}
''')

add("3292_minimum_number_of_valid_strings_to_form_target_ii", r'''<?php
// LeetCode 3292 - Minimum Number of Valid Strings to Form Target II
// https://leetcode.com/problems/minimum-number-of-valid-strings-to-form-target-ii/

class Solution {
    function minValidStrings($words, $target) {
        $n = strlen($target);
        $inf = 1000000000;
        $dp = array_fill(0, $n + 1, $inf);
        $dp[0] = 0;
        $root = ['next' => array_fill(0, 26, null)];
        foreach ($words as $w) {
            $cur =& $root;
            $len = strlen($w);
            for ($i = 0; $i < $len; $i++) {
                $ci = ord($w[$i]) - 97;
                if ($cur['next'][$ci] === null) $cur['next'][$ci] = ['next' => array_fill(0, 26, null)];
                $cur =& $cur['next'][$ci];
            }
            unset($cur);
        }
        for ($i = 0; $i < $n; $i++) {
            if ($dp[$i] === $inf) continue;
            $cur =& $root;
            for ($j = $i; $j < $n; $j++) {
                $ci = ord($target[$j]) - 97;
                if ($cur['next'][$ci] === null) break;
                $cur =& $cur['next'][$ci];
                if ($dp[$i] + 1 < $dp[$j + 1]) $dp[$j + 1] = $dp[$i] + 1;
            }
            unset($cur);
        }
        return $dp[$n] === $inf ? -1 : $dp[$n];
    }
}
''')

add("3294_convert_doubly_linked_list_to_array_ii", r'''<?php
// LeetCode 3294 - Convert Doubly Linked List to Array II
// https://leetcode.com/problems/convert-doubly-linked-list-to-array-ii/

class Node {
    public $val;
    public $prev;
    public $next;
    function __construct($val = 0, $prev = null, $next = null) {
        $this->val = $val;
        $this->prev = $prev;
        $this->next = $next;
    }
}

class Solution {
    function toArray($node) {
        while ($node !== null && $node->prev !== null) $node = $node->prev;
        $ans = [];
        while ($node !== null) {
            $ans[] = $node->val;
            $node = $node->next;
        }
        return $ans;
    }
}
''')

add("3295_report_spam_message", r'''<?php
// LeetCode 3295 - Report Spam Message
// https://leetcode.com/problems/report-spam-message/

class Solution {
    function reportSpam($message, $bannedWords) {
        $ban = [];
        foreach ($bannedWords as $w) $ban[$w] = true;
        $cnt = 0;
        foreach ($message as $w) {
            if (isset($ban[$w])) {
                $cnt++;
                if ($cnt >= 2) return true;
            }
        }
        return false;
    }
}
''')

add("3296_minimum_number_of_seconds_to_make_mountain_height_zero", r'''<?php
// LeetCode 3296 - Minimum Number of Seconds to Make Mountain Height Zero
// https://leetcode.com/problems/minimum-number-of-seconds-to-make-mountain-height-zero/

class Solution {
    function ok($t, $mountainHeight, $workerTimes) {
        $total = 0;
        foreach ($workerTimes as $w) {
            $l = 0;
            $h = $mountainHeight;
            while ($l < $h) {
                $mid = intdiv($l + $h + 1, 2);
                if ($w * $mid * ($mid + 1) / 2 <= $t) $l = $mid;
                else $h = $mid - 1;
            }
            $total += $l;
            if ($total >= $mountainHeight) return true;
        }
        return $total >= $mountainHeight;
    }

    function minNumberOfSeconds($mountainHeight, $workerTimes) {
        $lo = 0;
        $hi = 1e18;
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi, 2);
            if ($this->ok($mid, $mountainHeight, $workerTimes)) $hi = $mid;
            else $lo = $mid + 1;
        }
        return $lo;
    }
}
''')

add("3297_count_substrings_that_can_be_rearranged_to_contain_a_string_i", r'''<?php
// LeetCode 3297 - Count Substrings That Can Be Rearranged to Contain a String I
// https://leetcode.com/problems/count-substrings-that-can-be-rearranged-to-contain-a-string-i/

class Solution {
    function validSubstringCount($word1, $word2) {
        $need = array_fill(0, 26, 0);
        $required = 0;
        $m = strlen($word2);
        for ($i = 0; $i < $m; $i++) {
            $idx = ord($word2[$i]) - 97;
            if ($need[$idx] === 0) $required++;
            $need[$idx]++;
        }
        $have = array_fill(0, 26, 0);
        $formed = 0;
        $ans = 0;
        $l = 0;
        $n = strlen($word1);
        for ($r = 0; $r < $n; $r++) {
            $c = ord($word1[$r]) - 97;
            $have[$c]++;
            if ($have[$c] === $need[$c] && $need[$c] > 0) $formed++;
            while ($formed === $required && $l <= $r) {
                $ans += $n - $r;
                $c2 = ord($word1[$l]) - 97;
                if ($have[$c2] === $need[$c2] && $need[$c2] > 0) $formed--;
                $have[$c2]--;
                $l++;
            }
        }
        return $ans;
    }
}
''')

add("3298_count_substrings_that_can_be_rearranged_to_contain_a_string_ii", r'''<?php
// LeetCode 3298 - Count Substrings That Can Be Rearranged to Contain a String II
// https://leetcode.com/problems/count-substrings-that-can-be-rearranged-to-contain-a-string-ii/

class Solution {
    function validSubstringCount($word1, $word2) {
        $need = array_fill(0, 26, 0);
        $required = 0;
        $m = strlen($word2);
        for ($i = 0; $i < $m; $i++) {
            $idx = ord($word2[$i]) - 97;
            if ($need[$idx] === 0) $required++;
            $need[$idx]++;
        }
        $have = array_fill(0, 26, 0);
        $formed = 0;
        $ans = 0;
        $l = 0;
        $n = strlen($word1);
        for ($r = 0; $r < $n; $r++) {
            $c = ord($word1[$r]) - 97;
            $have[$c]++;
            if ($have[$c] === $need[$c] && $need[$c] > 0) $formed++;
            while ($formed === $required && $l <= $r) {
                $ans += $n - $r;
                $c2 = ord($word1[$l]) - 97;
                if ($have[$c2] === $need[$c2] && $need[$c2] > 0) $formed--;
                $have[$c2]--;
                $l++;
            }
        }
        return $ans;
    }
}
''')

add("3299_sum_of_consecutive_subsequences", r'''<?php
// LeetCode 3299 - Sum of Consecutive Subsequences
// https://leetcode.com/problems/sum-of-consecutive-subsequences/

class Solution {
    function rangeSum($nums) {
        $mod = 1000000007;
        $cnt = [];
        $sum = [];
        $ans = 0;
        foreach ($nums as $x) {
            $cL = $cnt[$x - 1] ?? 0;
            $sL = $sum[$x - 1] ?? 0;
            $cR = $cnt[$x + 1] ?? 0;
            $sR = $sum[$x + 1] ?? 0;
            $c = (1 + $cL + $cR) % $mod;
            $s = ($x + $sL + ($cL * $x % $mod) + $sR + ($cR * $x % $mod)) % $mod;
            if ($cL > 0 && $cR > 0) {
                $c = ($c + ($cL * $cR % $mod)) % $mod;
                $s = ($s + ($sL * $cR % $mod) + ($sR * $cL % $mod) + ($cL * $cR % $mod * $x % $mod)) % $mod;
            }
            $cnt[$x] = (($cnt[$x] ?? 0) + $c) % $mod;
            $sum[$x] = (($sum[$x] ?? 0) + $s) % $mod;
            $ans = ($ans + $s) % $mod;
        }
        return $ans;
    }
}
''')

add("3300_minimum_element_after_replacement_with_digit_sum", r'''<?php
// LeetCode 3300 - Minimum Element After Replacement With Digit Sum
// https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/

class Solution {
    function minElement($nums) {
        $ans = 1000000000;
        foreach ($nums as $num) {
            $x = $num;
            $s = 0;
            while ($x > 0) {
                $s += $x % 10;
                $x = intdiv($x, 10);
            }
            if ($s < $ans) $ans = $s;
        }
        return $ans;
    }
}
''')

add("3301_maximize_the_total_height_of_unique_towers", r'''<?php
// LeetCode 3301 - Maximize the Total Height of Unique Towers
// https://leetcode.com/problems/maximize-the-total-height-of-unique-towers/

class Solution {
    function maximumTotalSum($maximumHeight) {
        rsort($maximumHeight);
        $ans = 0;
        $prev = 1e18;
        foreach ($maximumHeight as $h) {
            $cur = $h;
            if ($cur >= $prev) $cur = $prev - 1;
            if ($cur <= 0) return -1;
            $ans += $cur;
            $prev = $cur;
        }
        return $ans;
    }
}
''')

add("3302_find_the_lexicographically_smallest_valid_sequence", r'''<?php
// LeetCode 3302 - Find the Lexicographically Smallest Valid Sequence
// https://leetcode.com/problems/find-the-lexicographically-smallest-valid-sequence/

class Solution {
    function canFinish($w1, $w2, $i, $j, $usedSkip, $right) {
        $m = strlen($w2);
        if ($j >= $m) return true;
        if (!$usedSkip) {
            if ($right[$j] >= $i) return true;
            if ($j + 1 <= $m && $right[$j + 1] > $i) return true;
            if ($right[$j] > $i) return true;
            return false;
        }
        return $right[$j] >= $i;
    }

    function validSequence($word1, $word2) {
        $n = strlen($word1);
        $m = strlen($word2);
        $right = array_fill(0, $m + 1, 0);
        $right[$m] = $n;
        $j = $m - 1;
        for ($i = $n - 1; $i >= 0 && $j >= 0; $i--) {
            if ($word1[$i] === $word2[$j]) {
                $right[$j] = $i;
                $j--;
            }
        }
        for (; $j >= 0; $j--) $right[$j] = -1;
        $ans = array_fill(0, $m, 0);
        $usedSkip = false;
        $i = 0;
        for ($j = 0; $j < $m; $j++) {
            $found = false;
            while ($i < $n) {
                if ($word1[$i] === $word2[$j]) {
                    if ($this->canFinish($word1, $word2, $i + 1, $j + 1, $usedSkip, $right)) {
                        $ans[$j] = $i;
                        $i++;
                        $found = true;
                        break;
                    }
                } else if (!$usedSkip) {
                    if ($this->canFinish($word1, $word2, $i + 1, $j + 1, true, $right)) {
                        $ans[$j] = $i;
                        $i++;
                        $usedSkip = true;
                        $found = true;
                        break;
                    }
                }
                $i++;
            }
            if (!$found) return [];
        }
        return $ans;
    }
}
''')

add("3303_find_the_occurrence_of_first_almost_equal_substring", r'''<?php
// LeetCode 3303 - Find the Occurrence of First Almost Equal Substring
// https://leetcode.com/problems/find-the-occurrence-of-first-almost-equal-substring/

class Solution {
    function minStartingIndex($s, $pattern) {
        $n = strlen($s);
        $m = strlen($pattern);
        for ($i = 0; $i + $m <= $n; $i++) {
            $diff = 0;
            for ($j = 0; $j < $m; $j++) {
                if ($s[$i + $j] !== $pattern[$j]) {
                    $diff++;
                    if ($diff > 1) break;
                }
            }
            if ($diff <= 1) return $i;
        }
        return -1;
    }
}
''')

add("3304_find_the_k_th_character_in_string_game_i", r'''<?php
// LeetCode 3304 - Find the K-th Character in String Game I
// https://leetcode.com/problems/find-the-k-th-character-in-string-game-i/

class Solution {
    function kthCharacter($k) {
        $s = 'a';
        while (strlen($s) < $k) {
            $n = strlen($s);
            $add = '';
            for ($i = 0; $i < $n; $i++) {
                $add .= chr(97 + ((ord($s[$i]) - 97 + 1) % 26));
            }
            $s .= $add;
        }
        return $s[$k - 1];
    }
}
''')

add("3305_count_of_substrings_containing_every_vowel_and_k_consonants_i", r'''<?php
// LeetCode 3305 - Count of Substrings Containing Every Vowel and K Consonants I
// https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-i/

class Solution {
    function isVowel($c) {
        return $c === 'a' || $c === 'e' || $c === 'i' || $c === 'o' || $c === 'u';
    }

    function atLeast($word, $k) {
        $cnt = [];
        $cons = 0;
        $l = 0;
        $ans = 0;
        $n = strlen($word);
        for ($r = 0; $r < $n; $r++) {
            $c = $word[$r];
            if ($this->isVowel($c)) $cnt[$c] = ($cnt[$c] ?? 0) + 1;
            else $cons++;
            while (count($cnt) === 5 && $cons >= $k) {
                $ans += $n - $r;
                $c2 = $word[$l];
                if ($this->isVowel($c2)) {
                    $nv = $cnt[$c2] - 1;
                    if ($nv === 0) unset($cnt[$c2]);
                    else $cnt[$c2] = $nv;
                } else $cons--;
                $l++;
            }
        }
        return $ans;
    }

    function countOfSubstrings($word, $k) {
        return $this->atLeast($word, $k) - $this->atLeast($word, $k + 1);
    }
}
''')

add("3306_count_of_substrings_containing_every_vowel_and_k_consonants_ii", r'''<?php
// LeetCode 3306 - Count of Substrings Containing Every Vowel and K Consonants II
// https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii/

class Solution {
    function isVowel($c) {
        return $c === 'a' || $c === 'e' || $c === 'i' || $c === 'o' || $c === 'u';
    }

    function atLeast($word, $k) {
        $cnt = [];
        $cons = 0;
        $l = 0;
        $ans = 0;
        $n = strlen($word);
        for ($r = 0; $r < $n; $r++) {
            $c = $word[$r];
            if ($this->isVowel($c)) $cnt[$c] = ($cnt[$c] ?? 0) + 1;
            else $cons++;
            while (count($cnt) === 5 && $cons >= $k) {
                $ans += $n - $r;
                $c2 = $word[$l];
                if ($this->isVowel($c2)) {
                    $nv = $cnt[$c2] - 1;
                    if ($nv === 0) unset($cnt[$c2]);
                    else $cnt[$c2] = $nv;
                } else $cons--;
                $l++;
            }
        }
        return $ans;
    }

    function countOfSubstrings($word, $k) {
        return $this->atLeast($word, $k) - $this->atLeast($word, $k + 1);
    }
}
''')

add("3307_find_the_k_th_character_in_string_game_ii", r'''<?php
// LeetCode 3307 - Find the K-th Character in String Game II
// https://leetcode.com/problems/find-the-k-th-character-in-string-game-ii/

class Solution {
    function kthCharacter($k, $operations) {
        $shift = 0;
        $ops = $operations;
        while (count($ops)) {
            $op = array_pop($ops);
            $len = count($ops);
            $half = $len >= 62 ? INF : (1 << $len);
            if ($k > $half) {
                $k = $k - $half;
                if ($op === 1) $shift++;
            }
        }
        return chr(97 + ($shift % 26));
    }
}
''')

add("3309_maximum_possible_number_by_binary_concatenation", r'''<?php
// LeetCode 3309 - Maximum Possible Number by Binary Concatenation
// https://leetcode.com/problems/maximum-possible-number-by-binary-concatenation/

class Solution {
    function toBin($x) {
        if ($x === 0) return '0';
        $s = '';
        while ($x > 0) {
            $s = strval($x & 1) . $s;
            $x >>= 1;
        }
        return $s;
    }

    function perm($i, &$idx, $bs, &$ans) {
        if ($i === 3) {
            $s = $bs[$idx[0]] . $bs[$idx[1]] . $bs[$idx[2]];
            $v = 0;
            $len = strlen($s);
            for ($p = 0; $p < $len; $p++) $v = $v * 2 + (ord($s[$p]) - 48);
            if ($v > $ans[0]) $ans[0] = $v;
            return;
        }
        for ($j = $i; $j < 3; $j++) {
            $t = $idx[$i]; $idx[$i] = $idx[$j]; $idx[$j] = $t;
            $this->perm($i + 1, $idx, $bs, $ans);
            $t = $idx[$i]; $idx[$i] = $idx[$j]; $idx[$j] = $t;
        }
    }

    function maxGoodNumber($nums) {
        $bs = [$this->toBin($nums[0]), $this->toBin($nums[1]), $this->toBin($nums[2])];
        $idx = [0, 1, 2];
        $ans = [0];
        $this->perm(0, $idx, $bs, $ans);
        return $ans[0];
    }
}
''')

add("3310_remove_methods_from_project", r'''<?php
// LeetCode 3310 - Remove Methods From Project
// https://leetcode.com/problems/remove-methods-from-project/

class Solution {
    function remainingMethods($n, $k, $invocations) {
        $g = array_fill(0, $n, []);
        foreach ($invocations as $e) $g[$e[0]][] = $e[1];
        $sus = array_fill(0, $n, false);
        $this->dfs($k, $g, $sus);
        foreach ($invocations as $e) {
            if (!$sus[$e[0]] && $sus[$e[1]]) {
                $ans = [];
                for ($i = 0; $i < $n; $i++) $ans[] = $i;
                return $ans;
            }
        }
        $ans = [];
        for ($i = 0; $i < $n; $i++) if (!$sus[$i]) $ans[] = $i;
        return $ans;
    }

    function dfs($u, $g, &$sus) {
        if ($sus[$u]) return;
        $sus[$u] = true;
        foreach ($g[$u] as $v) $this->dfs($v, $g, $sus);
    }
}
''')

add("3311_construct_2d_grid_matching_graph_layout", r'''<?php
// LeetCode 3311 - Construct 2D Grid Matching Graph Layout
// https://leetcode.com/problems/construct-2d-grid-matching-graph-layout/

class Solution {
    function constructGridLayout($n, $edges) {
        $g = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $g[$e[0]][] = $e[1];
            $g[$e[1]][] = $e[0];
        }
        $deg = [];
        for ($i = 0; $i < $n; $i++) $deg[$i] = count($g[$i]);
        $start = 0;
        for ($i = 0; $i < $n; $i++) {
            if ($deg[$i] === 1) { $start = $i; break; }
            if ($deg[$i] === 2) $start = $i;
        }
        $vis = array_fill(0, $n, false);
        $row = [];
        $cur = $start;
        $prev = -1;
        for (;;) {
            $row[] = $cur;
            $vis[$cur] = true;
            $next = -1;
            foreach ($g[$cur] as $v) {
                if ($v !== $prev && !$vis[$v] && $deg[$v] <= 3) {
                    $next = $v;
                    if ($deg[$v] < 4) break;
                }
            }
            if ($next === -1) break;
            $prev = $cur;
            $cur = $next;
        }
        $width = count($row);
        $height = $width !== 0 ? intdiv($n, $width) : $n;
        if ($width === 0 || $width * $height !== $n) {
            for ($w = 1; $w <= $n; $w++) {
                if ($n % $w === 0) { $width = $w; $height = intdiv($n, $w); break; }
            }
        }
        $grid = [];
        for ($i = 0; $i < $height; $i++) $grid[$i] = array_fill(0, $width, 0);
        for ($i = 0; $i < $n; $i++) $grid[intdiv($i, $width)][$i % $width] = $i;
        return $grid;
    }
}
''')

add("3312_sorted_gcd_pair_queries", r'''<?php
// LeetCode 3312 - Sorted GCD Pair Queries
// https://leetcode.com/problems/sorted-gcd-pair-queries/

class Solution {
    function gcdValues($nums, $queries) {
        $maxV = 0;
        foreach ($nums as $x) if ($x > $maxV) $maxV = $x;
        $cnt = array_fill(0, $maxV + 1, 0);
        foreach ($nums as $x) $cnt[$x]++;
        $divCnt = array_fill(0, $maxV + 1, 0);
        for ($g = 1; $g <= $maxV; $g++) {
            $c = 0;
            for ($m = $g; $m <= $maxV; $m += $g) $c += $cnt[$m];
            $divCnt[$g] = $c * ($c - 1) / 2;
        }
        $exact = array_fill(0, $maxV + 1, 0);
        for ($g = $maxV; $g >= 1; $g--) {
            $exact[$g] = $divCnt[$g];
            for ($m = 2 * $g; $m <= $maxV; $m += $g) $exact[$g] -= $exact[$m];
        }
        $pref = array_fill(0, $maxV + 1, 0);
        for ($g = 1; $g <= $maxV; $g++) $pref[$g] = $pref[$g - 1] + $exact[$g];
        $ans = [];
        $qn = count($queries);
        for ($i = 0; $i < $qn; $i++) {
            $q = $queries[$i];
            $lo = 1;
            $hi = $maxV;
            while ($lo < $hi) {
                $mid = ($lo + $hi) >> 1;
                if ($pref[$mid] > $q) $hi = $mid;
                else $lo = $mid + 1;
            }
            $ans[$i] = $lo;
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

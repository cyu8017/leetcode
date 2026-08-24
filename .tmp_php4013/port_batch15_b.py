#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
SOLUTIONS = {}

def add(folder, body):
    SOLUTIONS[folder] = body


add("3201_find_the_maximum_length_of_valid_subsequence_i", r'''<?php
// LeetCode 3201 - Find the Maximum Length of Valid Subsequence I
// https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-i/

class Solution {
    function maximumLength($nums) {
        $k = 2;
        $f = [];
        for ($i = 0; $i < $k; $i++) $f[$i] = array_fill(0, $k, 0);
        $ans = 0;
        foreach ($nums as $raw) {
            $x = $raw % $k;
            for ($j = 0; $j < $k; $j++) {
                $y = ($j - $x + $k) % $k;
                $f[$x][$y] = $f[$y][$x] + 1;
                $ans = max($ans, $f[$x][$y]);
            }
        }
        return $ans;
    }
}
''')

add("3202_find_the_maximum_length_of_valid_subsequence_ii", r'''<?php
// LeetCode 3202 - Find the Maximum Length of Valid Subsequence II
// https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-ii/

class Solution {
    function maximumLength($nums, $k) {
        $f = [];
        for ($i = 0; $i < $k; $i++) $f[$i] = array_fill(0, $k, 0);
        $ans = 0;
        foreach ($nums as $raw) {
            $x = $raw % $k;
            for ($j = 0; $j < $k; $j++) {
                $y = ($j - $x + $k) % $k;
                $f[$x][$y] = $f[$y][$x] + 1;
                $ans = max($ans, $f[$x][$y]);
            }
        }
        return $ans;
    }
}
''')

add("3203_find_minimum_diameter_after_merging_two_trees", r'''<?php
// LeetCode 3203 - Find Minimum Diameter After Merging Two Trees
// https://leetcode.com/problems/find-minimum-diameter-after-merging-two-trees/

class Solution {
    private $ans;
    private $a;
    private $g;

    function minimumDiameterAfterMerge($edges1, $edges2) {
        $d1 = $this->treeDiameter($edges1);
        $d2 = $this->treeDiameter($edges2);
        return max($d1, $d2, intdiv($d1 + 1, 2) + intdiv($d2 + 1, 2) + 1);
    }

    private function dfs($i, $fa, $t) {
        foreach ($this->g[$i] as $j) if ($j !== $fa) $this->dfs($j, $i, $t + 1);
        if ($this->ans < $t) { $this->ans = $t; $this->a = $i; }
    }

    private function treeDiameter($edges) {
        $n = count($edges) + 1;
        $this->g = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $this->g[$e[0]][] = $e[1];
            $this->g[$e[1]][] = $e[0];
        }
        $this->ans = 0;
        $this->a = 0;
        $this->dfs(0, -1, 0);
        $this->dfs($this->a, -1, 0);
        return $this->ans;
    }
}
''')

add("3205_maximum_array_hopping_score_i", r'''<?php
// LeetCode 3205 - Maximum Array Hopping Score I
// https://leetcode.com/problems/maximum-array-hopping-score-i/

class Solution {
    private $nums;
    private $n;
    private $f;

    function maxScore($nums) {
        $this->nums = $nums;
        $this->n = count($nums);
        $this->f = array_fill(0, $this->n, 0);
        return $this->dfs(0);
    }

    private function dfs($i) {
        if ($this->f[$i] > 0) return $this->f[$i];
        for ($j = $i + 1; $j < $this->n; $j++) $this->f[$i] = max($this->f[$i], ($j - $i) * $this->nums[$j] + $this->dfs($j));
        return $this->f[$i];
    }
}
''')

add("3206_alternating_groups_i", r'''<?php
// LeetCode 3206 - Alternating Groups I
// https://leetcode.com/problems/alternating-groups-i/

class Solution {
    function numberOfAlternatingGroups($colors) {
        $k = 3;
        $n = count($colors);
        $cnt = 0;
        $ans = 0;
        for ($i = 0; $i < $n * 2; $i++) {
            if ($i > 0 && $colors[$i % $n] === $colors[($i - 1) % $n]) $cnt = 1;
            else $cnt++;
            if ($i >= $n && $cnt >= $k) $ans++;
        }
        return $ans;
    }
}
''')

add("3207_maximum_points_after_enemy_battles", r'''<?php
// LeetCode 3207 - Maximum Points After Enemy Battles
// https://leetcode.com/problems/maximum-points-after-enemy-battles/

class Solution {
    function maximumPoints($enemyEnergies, $currentEnergy) {
        sort($enemyEnergies);
        if ($currentEnergy < $enemyEnergies[0]) return 0;
        $ans = 0;
        for ($i = count($enemyEnergies) - 1; $i >= 0; $i--) {
            $ans += intdiv($currentEnergy, $enemyEnergies[0]);
            $currentEnergy %= $enemyEnergies[0];
            $currentEnergy += $enemyEnergies[$i];
        }
        return $ans;
    }
}
''')

add("3208_alternating_groups_ii", r'''<?php
// LeetCode 3208 - Alternating Groups II
// https://leetcode.com/problems/alternating-groups-ii/

class Solution {
    function numberOfAlternatingGroups($colors, $k) {
        $n = count($colors);
        $cnt = 0;
        $ans = 0;
        for ($i = 0; $i < $n * 2; $i++) {
            if ($i > 0 && $colors[$i % $n] === $colors[($i - 1) % $n]) $cnt = 1;
            else $cnt++;
            if ($i >= $n && $cnt >= $k) $ans++;
        }
        return $ans;
    }
}
''')

add("3209_number_of_subarrays_with_and_value_of_k", r'''<?php
// LeetCode 3209 - Number of Subarrays With AND Value of K
// https://leetcode.com/problems/number-of-subarrays-with-and-value-of-k/

class Solution {
    function countSubarrays($nums, $k) {
        $pre = [];
        $ans = 0;
        foreach ($nums as $x) {
            $cur = [];
            foreach ($pre as $key => $val) {
                $nk = $x & $key;
                $cur[$nk] = ($cur[$nk] ?? 0) + $val;
            }
            $cur[$x] = ($cur[$x] ?? 0) + 1;
            $ans += $cur[$k] ?? 0;
            $pre = $cur;
        }
        return $ans;
    }
}
''')

add("3210_find_the_encrypted_string", r'''<?php
// LeetCode 3210 - Find the Encrypted String
// https://leetcode.com/problems/find-the-encrypted-string/

class Solution {
    function getEncryptedString($s, $k) {
        $n = strlen($s);
        $out = '';
        for ($i = 0; $i < $n; $i++) $out .= $s[($i + $k) % $n];
        return $out;
    }
}
''')

add("3211_generate_binary_strings_without_adjacent_zeros", r'''<?php
// LeetCode 3211 - Generate Binary Strings Without Adjacent Zeros
// https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/

class Solution {
    private $n;
    private $ans;
    private $t;

    function validStrings($n) {
        $this->n = $n;
        $this->ans = [];
        $this->t = [];
        $this->dfs(0);
        return $this->ans;
    }

    private function dfs($i) {
        if ($i >= $this->n) { $this->ans[] = implode('', $this->t); return; }
        for ($j = 0; $j < 2; $j++) {
            if (($j === 0 && ($i === 0 || $this->t[$i - 1] === '1')) || $j === 1) {
                $this->t[] = (string)$j;
                $this->dfs($i + 1);
                array_pop($this->t);
            }
        }
    }
}
''')

add("3212_count_submatrices_with_equal_frequency_of_x_and_y", r'''<?php
// LeetCode 3212 - Count Submatrices With Equal Frequency of X and Y
// https://leetcode.com/problems/count-submatrices-with-equal-frequency-of-x-and-y/

class Solution {
    function numberOfSubmatrices($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        $s = [];
        for ($i = 0; $i <= $m; $i++) {
            $s[$i] = [];
            for ($j = 0; $j <= $n; $j++) $s[$i][$j] = [0, 0];
        }
        $ans = 0;
        for ($i = 1; $i <= $m; $i++) {
            for ($j = 1; $j <= $n; $j++) {
                $s[$i][$j][0] = $s[$i - 1][$j][0] + $s[$i][$j - 1][0] - $s[$i - 1][$j - 1][0];
                if ($grid[$i - 1][$j - 1] === 'X') $s[$i][$j][0]++;
                $s[$i][$j][1] = $s[$i - 1][$j][1] + $s[$i][$j - 1][1] - $s[$i - 1][$j - 1][1];
                if ($grid[$i - 1][$j - 1] === 'Y') $s[$i][$j][1]++;
                if ($s[$i][$j][0] > 0 && $s[$i][$j][0] === $s[$i][$j][1]) $ans++;
            }
        }
        return $ans;
    }
}
''')

add("3213_construct_string_with_minimum_cost", r'''<?php
// LeetCode 3213 - Construct String with Minimum Cost
// https://leetcode.com/problems/construct-string-with-minimum-cost/

class Solution {
    function minimumCost($target, $words, $costs) {
        $bas = 13331;
        $mod = 998244353;
        $inf = intdiv(PHP_INT_MAX, 2);
        $n = strlen($target);
        $p = array_fill(0, $n + 1, 0);
        $h = array_fill(0, $n + 1, 0);
        $p[0] = 1;
        $h[0] = 0;
        for ($i = 1; $i <= $n; $i++) {
            $p[$i] = ($p[$i - 1] * $bas) % $mod;
            $h[$i] = ($h[$i - 1] * $bas + ord($target[$i - 1])) % $mod;
        }
        $f = array_fill(0, $n + 1, $inf);
        $f[0] = 0;
        $ss = [];
        foreach ($words as $w) $ss[strlen($w)] = true;
        $lengths = array_keys($ss);
        sort($lengths);
        $d = [];
        for ($i = 0; $i < count($words); $i++) {
            $x = 0;
            $len = strlen($words[$i]);
            for ($c = 0; $c < $len; $c++) $x = ($x * $bas + ord($words[$i][$c])) % $mod;
            if (!isset($d[$x]) || $costs[$i] < $d[$x]) $d[$x] = $costs[$i];
        }
        for ($i = 1; $i <= $n; $i++) {
            foreach ($lengths as $j) {
                if ($j > $i) break;
                $x = ($h[$i] - ($h[$i - $j] * $p[$j]) % $mod + $mod) % $mod;
                if (isset($d[$x])) $f[$i] = min($f[$i], $f[$i - $j] + $d[$x]);
            }
        }
        return $f[$n] >= $inf ? -1 : $f[$n];
    }
}
''')

add("3215_count_triplets_with_even_xor_set_bits_ii", r'''<?php
// LeetCode 3215 - Count Triplets with Even XOR Set Bits II
// https://leetcode.com/problems/count-triplets-with-even-xor-set-bits-ii/

class Solution {
    function tripletCount($a, $b, $c) {
        $cnt1 = [0, 0];
        $cnt2 = [0, 0];
        $cnt3 = [0, 0];
        foreach ($a as $x) $cnt1[$this->bitCount($x) % 2]++;
        foreach ($b as $x) $cnt2[$this->bitCount($x) % 2]++;
        foreach ($c as $x) $cnt3[$this->bitCount($x) % 2]++;
        $ans = 0;
        for ($i = 0; $i < 2; $i++)
            for ($j = 0; $j < 2; $j++)
                for ($k = 0; $k < 2; $k++)
                    if (($i + $j + $k) % 2 === 0) $ans += $cnt1[$i] * $cnt2[$j] * $cnt3[$k];
        return $ans;
    }

    private function bitCount($x) {
        $n = 0;
        while ($x) { $n += $x & 1; $x >>= 1; }
        return $n;
    }
}
''')

add("3216_lexicographically_smallest_string_after_a_swap", r'''<?php
// LeetCode 3216 - Lexicographically Smallest String After a Swap
// https://leetcode.com/problems/lexicographically-smallest-string-after-a-swap/

class Solution {
    function getSmallestString($s) {
        $arr = str_split($s);
        $n = count($arr);
        for ($i = 1; $i < $n; $i++) {
            $a = $arr[$i - 1];
            $b = $arr[$i];
            if ($a > $b && (ord($a) % 2) === (ord($b) % 2)) {
                $arr[$i - 1] = $b;
                $arr[$i] = $a;
                return implode('', $arr);
            }
        }
        return $s;
    }
}
''')

add("3217_delete_nodes_from_linked_list_present_in_array", r'''<?php
// LeetCode 3217 - Delete Nodes From Linked List Present in Array
// https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/

class ListNode {
    public $val = 0;
    public $next = null;
    function __construct($val = 0, $next = null) {
        $this->val = $val;
        $this->next = $next;
    }
}

class Solution {
    function modifiedList($nums, $head) {
        $s = [];
        foreach ($nums as $x) $s[$x] = true;
        $dummy = new ListNode(0, $head);
        $pre = $dummy;
        while ($pre->next !== null) {
            if (isset($s[$pre->next->val])) $pre->next = $pre->next->next;
            else $pre = $pre->next;
        }
        return $dummy->next;
    }
}
''')

add("3218_minimum_cost_for_cutting_cake_i", r'''<?php
// LeetCode 3218 - Minimum Cost for Cutting Cake I
// https://leetcode.com/problems/minimum-cost-for-cutting-cake-i/

class Solution {
    function minimumCost($m, $n, $horizontalCut, $verticalCut) {
        rsort($horizontalCut);
        rsort($verticalCut);
        $i = 0;
        $j = 0;
        $h = 1;
        $v = 1;
        $ans = 0;
        while ($i < $m - 1 || $j < $n - 1) {
            if ($j === $n - 1 || ($i < $m - 1 && $horizontalCut[$i] > $verticalCut[$j])) {
                $ans += $horizontalCut[$i] * $v;
                $h++;
                $i++;
            } else {
                $ans += $verticalCut[$j] * $h;
                $v++;
                $j++;
            }
        }
        return $ans;
    }
}
''')

add("3219_minimum_cost_for_cutting_cake_ii", r'''<?php
// LeetCode 3219 - Minimum Cost for Cutting Cake II
// https://leetcode.com/problems/minimum-cost-for-cutting-cake-ii/

class Solution {
    function minimumCost($m, $n, $horizontalCut, $verticalCut) {
        rsort($horizontalCut);
        rsort($verticalCut);
        $i = 0;
        $j = 0;
        $h = 1;
        $v = 1;
        $ans = 0;
        while ($i < $m - 1 || $j < $n - 1) {
            if ($j === $n - 1 || ($i < $m - 1 && $horizontalCut[$i] > $verticalCut[$j])) {
                $ans += $horizontalCut[$i] * $v;
                $h++;
                $i++;
            } else {
                $ans += $verticalCut[$j] * $h;
                $v++;
                $j++;
            }
        }
        return $ans;
    }
}
''')

add("3221_maximum_array_hopping_score_ii", r'''<?php
// LeetCode 3221 - Maximum Array Hopping Score II
// https://leetcode.com/problems/maximum-array-hopping-score-ii/

class Solution {
    function maxScore($nums) {
        $stk = [];
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            while (count($stk) > 0 && $nums[$stk[count($stk) - 1]] <= $nums[$i]) array_pop($stk);
            $stk[] = $i;
        }
        $ans = 0;
        $cur = 0;
        foreach ($stk as $j) {
            $ans += ($j - $cur) * $nums[$j];
            $cur = $j;
        }
        return $ans;
    }
}
''')

add("3222_find_the_winning_player_in_coin_game", r'''<?php
// LeetCode 3222 - Find the Winning Player in Coin Game
// https://leetcode.com/problems/find-the-winning-player-in-coin-game/

class Solution {
    function winningPlayer($x, $y) {
        $k = min(intdiv($x, 2), intdiv($y, 8));
        $x -= 2 * $k;
        $y -= 8 * $k;
        if ($x > 0 && $y >= 4) return "Alice";
        return "Bob";
    }
}
''')

add("3223_minimum_length_of_string_after_operations", r'''<?php
// LeetCode 3223 - Minimum Length of String After Operations
// https://leetcode.com/problems/minimum-length-of-string-after-operations/

class Solution {
    function minimumLength($s) {
        $cnt = array_fill(0, 26, 0);
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) $cnt[ord($s[$i]) - 97]++;
        $ans = 0;
        foreach ($cnt as $x) {
            if ($x > 0) $ans += ($x & 1) !== 0 ? 1 : 2;
        }
        return $ans;
    }
}
''')

add("3224_minimum_array_changes_to_make_differences_equal", r'''<?php
// LeetCode 3224 - Minimum Array Changes to Make Differences Equal
// https://leetcode.com/problems/minimum-array-changes-to-make-differences-equal/

class Solution {
    function minChanges($nums, $k) {
        $d = array_fill(0, $k + 2, 0);
        $n = count($nums);
        for ($i = 0; $i * 2 < $n; $i++) {
            $x = $nums[$i];
            $y = $nums[$n - 1 - $i];
            if ($x > $y) { $t = $x; $x = $y; $y = $t; }
            $d[0] += 1;
            $d[$y - $x] -= 1;
            $d[$y - $x + 1] += 1;
            $mx = max($y, $k - $x);
            $d[$mx + 1] -= 1;
            $d[$mx + 1] += 2;
        }
        $ans = $n;
        $s = 0;
        foreach ($d as $x) {
            $s += $x;
            $ans = min($ans, $s);
        }
        return $ans;
    }
}
''')

add("3225_maximum_score_from_grid_operations", r'''<?php
// LeetCode 3225 - Maximum Score From Grid Operations
// https://leetcode.com/problems/maximum-score-from-grid-operations/

class Solution {
    function maximumScore($grid) {
        $n = count($grid);
        $prefix = [];
        for ($j = 0; $j < $n; $j++) {
            $prefix[$j] = array_fill(0, $n + 1, 0);
            for ($i = 0; $i < $n; $i++) $prefix[$j][$i + 1] = $prefix[$j][$i] + $grid[$i][$j];
        }
        $prevPick = array_fill(0, $n + 1, 0);
        $prevSkip = array_fill(0, $n + 1, 0);
        for ($j = 1; $j < $n; $j++) {
            $currPick = array_fill(0, $n + 1, 0);
            $currSkip = array_fill(0, $n + 1, 0);
            for ($curr = 0; $curr <= $n; $curr++) {
                for ($prev = 0; $prev <= $n; $prev++) {
                    if ($curr > $prev) {
                        $score = $prefix[$j - 1][$curr] - $prefix[$j - 1][$prev];
                        $currPick[$curr] = max($currPick[$curr], $prevSkip[$prev] + $score);
                        $currSkip[$curr] = max($currSkip[$curr], $prevSkip[$prev] + $score);
                    } else {
                        $score = $prefix[$j][$prev] - $prefix[$j][$curr];
                        $currPick[$curr] = max($currPick[$curr], $prevPick[$prev] + $score);
                        $currSkip[$curr] = max($currSkip[$curr], $prevPick[$prev]);
                    }
                }
            }
            $prevPick = $currPick;
            $prevSkip = $currSkip;
        }
        $ans = PHP_INT_MIN;
        foreach ($prevPick as $v) $ans = max($ans, $v);
        return $ans;
    }
}
''')

add("3226_number_of_bit_changes_to_make_two_integers_equal", r'''<?php
// LeetCode 3226 - Number of Bit Changes to Make Two Integers Equal
// https://leetcode.com/problems/number-of-bit-changes-to-make-two-integers-equal/

class Solution {
    function minChanges($n, $k) {
        if (($n & $k) !== $k) return -1;
        $x = $n ^ $k;
        $c = 0;
        while ($x) { $c += $x & 1; $x >>= 1; }
        return $c;
    }
}
''')

add("3227_vowels_game_in_a_string", r'''<?php
// LeetCode 3227 - Vowels Game in a String
// https://leetcode.com/problems/vowels-game-in-a-string/

class Solution {
    function doesAliceWin($s) {
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $c = $s[$i];
            if ($c === 'a' || $c === 'e' || $c === 'i' || $c === 'o' || $c === 'u') return true;
        }
        return false;
    }
}
''')

add("3228_maximum_number_of_operations_to_move_ones_to_the_end", r'''<?php
// LeetCode 3228 - Maximum Number of Operations to Move Ones to the End
// https://leetcode.com/problems/maximum-number-of-operations-to-move-ones-to-the-end/

class Solution {
    function maxOperations($s) {
        $ans = 0;
        $cnt = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            if ($s[$i] === '1') $cnt++;
            else if ($i > 0 && $s[$i - 1] === '1') $ans += $cnt;
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

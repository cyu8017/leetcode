#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")

def w(folder, body):
    (ROOT / folder / "solution.php").write_text(body if body.endswith("\n") else body + "\n", encoding="utf-8")
    print("wrote", folder)

w("3445_maximum_difference_between_even_and_odd_frequency_ii", r'''<?php
// LeetCode 3445 - Maximum Difference Between Even and Odd Frequency II
// https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-ii/

class Solution {
    function maxDifference($s, $k) {
        $n = strlen($s);
        $ans = -1e9;
        for ($a = 0; $a < 5; $a++) {
            for ($b = 0; $b < 5; $b++) {
                if ($a === $b) continue;
                $prefA = array_fill(0, $n + 1, 0);
                $prefB = array_fill(0, $n + 1, 0);
                for ($i = 0; $i < $n; $i++) {
                    $prefA[$i + 1] = $prefA[$i];
                    $prefB[$i + 1] = $prefB[$i];
                    if (ord($s[$i]) - 48 === $a) $prefA[$i + 1]++;
                    if (ord($s[$i]) - 48 === $b) $prefB[$i + 1]++;
                }
                for ($i = 0; $i < $n; $i++) {
                    for ($j = $i + $k - 1; $j < $n; $j++) {
                        $fa = $prefA[$j + 1] - $prefA[$i];
                        $fb = $prefB[$j + 1] - $prefB[$i];
                        if ($fa % 2 === 1 && $fb % 2 === 0 && $fb > 0) {
                            if ($fa - $fb > $ans) $ans = $fa - $fb;
                        }
                    }
                }
            }
        }
        return $ans;
    }
}
''')

w("3446_sort_matrix_by_diagonals", r'''<?php
// LeetCode 3446 - Sort Matrix by Diagonals
// https://leetcode.com/problems/sort-matrix-by-diagonals/

class Solution {
    function sortMatrix($grid) {
        $n = count($grid);
        $diags = [];
        for ($i = 0; $i < $n; $i++) {
            for ($j = 0; $j < $n; $j++) {
                $key = $i - $j;
                if (!isset($diags[$key])) $diags[$key] = [];
                $diags[$key][] = $grid[$i][$j];
            }
        }
        foreach ($diags as $key => &$list) {
            if ($key >= 0) rsort($list);
            else sort($list);
        }
        unset($list);
        $idx = [];
        for ($i = 0; $i < $n; $i++) {
            for ($j = 0; $j < $n; $j++) {
                $k = $i - $j;
                $pos = $idx[$k] ?? 0;
                $grid[$i][$j] = $diags[$k][$pos];
                $idx[$k] = $pos + 1;
            }
        }
        return $grid;
    }
}
''')

w("3447_assign_elements_to_groups_with_constraints", r'''<?php
// LeetCode 3447 - Assign Elements to Groups with Constraints
// https://leetcode.com/problems/assign-elements-to-groups-with-constraints/

class Solution {
    function assignElements($groups, $elements) {
        $maxV = 100001;
        $first = array_fill(0, $maxV, -1);
        for ($i = 0; $i < count($elements); $i++) {
            $e = $elements[$i];
            if ($e < $maxV && $first[$e] === -1) $first[$e] = $i;
        }
        $ans = array_fill(0, count($groups), -1);
        for ($gi = 0; $gi < count($groups); $gi++) {
            $g = $groups[$gi];
            $best = -1;
            for ($d = 1; $d * $d <= $g; $d++) {
                if ($g % $d === 0) {
                    if ($first[$d] !== -1 && ($best === -1 || $first[$d] < $best)) $best = $first[$d];
                    $other = intdiv($g, $d);
                    if ($first[$other] !== -1 && ($best === -1 || $first[$other] < $best)) $best = $first[$other];
                }
            }
            $ans[$gi] = $best;
        }
        return $ans;
    }
}
''')

w("3448_count_substrings_divisible_by_last_digit", r'''<?php
// LeetCode 3448 - Count Substrings Divisible By Last Digit
// https://leetcode.com/problems/count-substrings-divisible-by-last-digit/

class Solution {
    function countSubstrings($s) {
        $ans = 0;
        $n = strlen($s);
        for ($r = 0; $r < $n; $r++) {
            $last = ord($s[$r]) - 48;
            if ($last === 0) continue;
            $mod = 0;
            $p = 1 % $last;
            for ($l = $r; $l >= 0; $l--) {
                $mod = ($mod + (ord($s[$l]) - 48) * $p) % $last;
                $p = ($p * 10) % $last;
                if ($mod === 0) $ans++;
            }
        }
        return $ans;
    }
}
''')

w("3449_maximize_the_minimum_game_score", r'''<?php
// LeetCode 3449 - Maximize the Minimum Game Score
// https://leetcode.com/problems/maximize-the-minimum-game-score/

class Solution {
    function maxScore($points, $m) {
        $ok = function($mid) use ($points, $m) {
            $need = 0;
            $extra = 0;
            foreach ($points as $p) {
                $req = intdiv($mid + $p - 1, $p);
                if ($req > $extra) {
                    $visits = $req - $extra;
                    $need += 2 * $visits - 1;
                    $extra = $visits - 1;
                } else {
                    $need += 1;
                    $extra = 0;
                }
                if ($need > $m) return false;
            }
            return $need <= $m;
        };
        $lo = 0;
        $hi = 10 ** 18;
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi + 1, 2);
            if ($ok($mid)) $lo = $mid;
            else $hi = $mid - 1;
        }
        return $lo;
    }
}
''')

w("3450_maximum_students_on_a_single_bench", r'''<?php
// LeetCode 3450 - Maximum Students on a Single Bench
// https://leetcode.com/problems/maximum-students-on-a-single-bench/

class Solution {
    function maxStudentsOnBench($students) {
        $bench = [];
        foreach ($students as $s) {
            if (!isset($bench[$s[1]])) $bench[$s[1]] = [];
            $bench[$s[1]][$s[0]] = true;
        }
        $ans = 0;
        foreach ($bench as $set) {
            $sz = count($set);
            if ($sz > $ans) $ans = $sz;
        }
        return $ans;
    }
}
''')

w("3452_sum_of_good_numbers", r'''<?php
// LeetCode 3452 - Sum of Good Numbers
// https://leetcode.com/problems/sum-of-good-numbers/

class Solution {
    function sumOfGoodNumbers($nums, $k) {
        $ans = 0;
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            $x = $nums[$i];
            $good = true;
            if ($i - $k >= 0 && $x <= $nums[$i - $k]) $good = false;
            if ($i + $k < $n && $x <= $nums[$i + $k]) $good = false;
            if ($good) $ans += $x;
        }
        return $ans;
    }
}
''')

w("3453_separate_squares_i", r'''<?php
// LeetCode 3453 - Separate Squares I
// https://leetcode.com/problems/separate-squares-i/

class Solution {
    function separateSquares($squares) {
        $total = 0;
        foreach ($squares as $sq) {
            $l = $sq[2];
            $total += $l * $l;
        }
        $areaBelow = function($y) use ($squares) {
            $below = 0;
            foreach ($squares as $sq) {
                $yi = $sq[1];
                $l = $sq[2];
                $top = $yi + $l;
                if ($y <= $yi) continue;
                if ($y >= $top) $below += $l * $l;
                else $below += $l * ($y - $yi);
            }
            return $below;
        };
        $lo = 0.0;
        $hi = 2e9;
        for ($it = 0; $it < 60; $it++) {
            $mid = ($lo + $hi) / 2;
            if ($areaBelow($mid) * 2 < $total) $lo = $mid;
            else $hi = $mid;
        }
        return $hi;
    }
}
''')

w("3454_separate_squares_ii", r'''<?php
// LeetCode 3454 - Separate Squares II
// https://leetcode.com/problems/separate-squares-ii/

class Solution {
    function separateSquares($squares) {
        $total = 0;
        foreach ($squares as $sq) {
            $l = $sq[2];
            $total += $l * $l;
        }
        $areaBelow = function($y) use ($squares) {
            $below = 0;
            foreach ($squares as $sq) {
                $yi = $sq[1];
                $l = $sq[2];
                $top = $yi + $l;
                if ($y <= $yi) continue;
                else if ($y >= $top) $below += $l * $l;
                else $below += $l * ($y - $yi);
            }
            return $below;
        };
        $lo = 0.0;
        $hi = 2e9;
        for ($it = 0; $it < 60; $it++) {
            $mid = ($lo + $hi) / 2;
            if ($areaBelow($mid) * 2 < $total) $lo = $mid;
            else $hi = $mid;
        }
        return $hi;
    }
}
''')

w("3455_shortest_matching_substring", r'''<?php
// LeetCode 3455 - Shortest Matching Substring
// https://leetcode.com/problems/shortest-matching-substring/

class Solution {
    function shortestMatchingSubstring($s, $p) {
        $parts = [];
        $cur = "";
        $plen = strlen($p);
        for ($i = 0; $i < $plen; $i++) {
            $c = $p[$i];
            if ($c === "*") {
                $parts[] = $cur;
                $cur = "";
            } else $cur .= $c;
        }
        $parts[] = $cur;
        while (count($parts) < 3) $parts[] = "";
        $a = $parts[0];
        $b = $parts[1];
        $c = $parts[2];
        $n = strlen($s);
        $findAll = function($sub) use ($s, $n) {
            $res = [];
            $slen = strlen($sub);
            if ($slen === 0) {
                for ($i = 0; $i <= $n; $i++) $res[] = $i;
                return $res;
            }
            for ($i = 0; $i + $slen <= $n; $i++) {
                if (substr($s, $i, $slen) === $sub) $res[] = $i;
            }
            return $res;
        };
        $sortSearch = function($arr, $x) {
            $lo = 0;
            $hi = count($arr);
            while ($lo < $hi) {
                $mid = ($lo + $hi) >> 1;
                if ($arr[$mid] < $x) $lo = $mid + 1;
                else $hi = $mid;
            }
            return $lo;
        };
        $posA = $findAll($a);
        $posB = $findAll($b);
        $posC = $findAll($c);
        $ans = $n + 1;
        $alen = strlen($a);
        $blen = strlen($b);
        $clen = strlen($c);
        foreach ($posA as $ia) {
            $endA = $ia + $alen;
            $bi = $sortSearch($posB, $endA);
            for (; $bi < count($posB); $bi++) {
                $endB = $posB[$bi] + $blen;
                $ci = $sortSearch($posC, $endB);
                if ($ci < count($posC)) {
                    $length = $posC[$ci] + $clen - $ia;
                    if ($length < $ans) $ans = $length;
                }
                break;
            }
        }
        return $ans === $n + 1 ? -1 : $ans;
    }
}
''')

w("3456_find_special_substring_of_length_k", r'''<?php
// LeetCode 3456 - Find Special Substring of Length K
// https://leetcode.com/problems/find-special-substring-of-length-k/

class Solution {
    function hasSpecialSubstring($s, $k) {
        $n = strlen($s);
        for ($i = 0; $i + $k <= $n; $i++) {
            $ok = true;
            for ($j = $i + 1; $j < $i + $k; $j++) {
                if ($s[$j] !== $s[$i]) { $ok = false; break; }
            }
            if (!$ok) continue;
            if ($i > 0 && $s[$i - 1] === $s[$i]) continue;
            if ($i + $k < $n && $s[$i + $k] === $s[$i]) continue;
            return true;
        }
        return false;
    }
}
''')

w("3457_eat_pizzas", r'''<?php
// LeetCode 3457 - Eat Pizzas!
// https://leetcode.com/problems/eat-pizzas/

class Solution {
    function maxWeight($pizzas) {
        sort($pizzas);
        $n = count($pizzas);
        $days = intdiv($n, 4);
        $ans = 0;
        $oddDays = intdiv($days + 1, 2);
        $evenDays = intdiv($days, 2);
        $idx = $n - 1;
        for ($i = 0; $i < $oddDays; $i++) {
            $ans += $pizzas[$idx];
            $idx--;
        }
        for ($i = 0; $i < $evenDays; $i++) {
            $idx--;
            $ans += $pizzas[$idx];
            $idx--;
        }
        return $ans;
    }
}
''')

w("3458_select_k_disjoint_special_substrings", r'''<?php
// LeetCode 3458 - Select K Disjoint Special Substrings
// https://leetcode.com/problems/select-k-disjoint-special-substrings/

class Solution {
    function maxSubstringLength($s, $k) {
        $n = strlen($s);
        $first = array_fill(0, 26, $n);
        $last = array_fill(0, 26, -1);
        for ($i = 0; $i < $n; $i++) {
            $ci = ord($s[$i]) - 97;
            if ($first[$ci] === $n) $first[$ci] = $i;
            $last[$ci] = $i;
        }
        $segs = [];
        for ($c = 0; $c < 26; $c++) {
            if ($last[$c] === -1) continue;
            $l = $first[$c];
            $r = $last[$c];
            for ($i = $l; $i <= $r; $i++) {
                $ci = ord($s[$i]) - 97;
                if ($first[$ci] < $l) {
                    $l = $first[$ci];
                    $i = $l - 1;
                    continue;
                }
                if ($last[$ci] > $r) $r = $last[$ci];
            }
            if (!($l === 0 && $r === $n - 1)) $segs[] = [$l, $r];
        }
        $uniq = [];
        $arr = [];
        foreach ($segs as $sg) {
            $ks = $sg[0] . "," . $sg[1];
            if (!isset($uniq[$ks])) {
                $uniq[$ks] = true;
                $arr[] = $sg;
            }
        }
        usort($arr, function($a, $b) { return $a[1] <=> $b[1]; });
        $cnt = 0;
        $end = -1;
        foreach ($arr as $sg) {
            if ($sg[0] > $end) {
                $cnt++;
                $end = $sg[1];
            }
        }
        return $cnt >= $k;
    }
}
''')

w("3459_length_of_longest_v_shaped_diagonal_segment", r'''<?php
// LeetCode 3459 - Length of Longest V-Shaped Diagonal Segment
// https://leetcode.com/problems/length-of-longest-v-shaped-diagonal-segment/

class Solution {
    function lenOfVDiagonal($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        $dirs = [[1, 1], [1, -1], [-1, -1], [-1, 1]];
        $nextDir = [1, 2, 3, 0];
        $memo = [];
        $key = function($i, $j, $d, $turned, $expect) {
            return (((($i * 101 + $j) * 5 + $d) * 3 + $turned) * 5 + $expect);
        };
        $dfs = null;
        $dfs = function($i, $j, $d, $turned, $expect) use (&$dfs, $m, $n, $grid, $dirs, $nextDir, &$memo, $key) {
            if ($i < 0 || $j < 0 || $i >= $m || $j >= $n || $grid[$i][$j] !== $expect) return 0;
            $k = $key($i, $j, $d, $turned, $expect);
            if (isset($memo[$k])) return $memo[$k];
            $ni = $i + $dirs[$d][0];
            $nj = $j + $dirs[$d][1];
            $nx = $expect === 2 ? 0 : 2;
            $best = 1 + $dfs($ni, $nj, $d, $turned, $nx);
            if ($turned === 0) {
                $nd = $nextDir[$d];
                $ti = $i + $dirs[$nd][0];
                $tj = $j + $dirs[$nd][1];
                $cand = 1 + $dfs($ti, $tj, $nd, 1, $nx);
                if ($cand > $best) $best = $cand;
            }
            $memo[$k] = $best;
            return $best;
        };
        $ans = 0;
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if ($grid[$i][$j] !== 1) continue;
                for ($d = 0; $d < 4; $d++) {
                    $ni = $i + $dirs[$d][0];
                    $nj = $j + $dirs[$d][1];
                    $best = 1 + $dfs($ni, $nj, $d, 0, 2);
                    if ($best > $ans) $ans = $best;
                }
                if ($ans < 1) $ans = 1;
            }
        }
        return $ans;
    }
}
''')

w("3460_longest_common_prefix_after_at_most_one_removal", r'''<?php
// LeetCode 3460 - Longest Common Prefix After at Most One Removal
// https://leetcode.com/problems/longest-common-prefix-after-at-most-one-removal/

class Solution {
    function longestCommonPrefix($s, $t) {
        $i = 0;
        $j = 0;
        $removed = false;
        $sn = strlen($s);
        $tn = strlen($t);
        while ($i < $sn && $j < $tn) {
            if ($s[$i] === $t[$j]) {
                $i++;
                $j++;
                continue;
            }
            if ($removed) break;
            $removed = true;
            $i++;
        }
        return $j;
    }
}
''')

print("d done")

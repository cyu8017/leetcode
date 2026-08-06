#!/usr/bin/env python3
"""Port stub solution.php files for problems 1252-1269 (non-SQL)."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOLUTIONS: dict[str, str] = {}


def add(name: str, content: str) -> None:
    SOLUTIONS[name] = content.strip() + "\n"


add("1252_cells_with_odd_values_in_a_matrix", r"""<?php
// LeetCode 1252 - Cells with Odd Values in a Matrix
// https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/

class Solution {
    /**
     * @param Integer $m
     * @param Integer $n
     * @param Integer[][] $indices
     * @return Integer
     */
    function oddCells($m, $n, $indices) {
        $rows = array_fill(0, $m, 0);
        $cols = array_fill(0, $n, 0);
        foreach ($indices as [$r, $c]) {
            $rows[$r] ^= 1;
            $cols[$c] ^= 1;
        }
        $ans = 0;
        for ($r = 0; $r < $m; $r++) {
            for ($c = 0; $c < $n; $c++) {
                $ans += $rows[$r] ^ $cols[$c];
            }
        }
        return $ans;
    }
}
""")

add("1253_reconstruct_a_2_row_binary_matrix", r"""<?php
// LeetCode 1253 - Reconstruct a 2-Row Binary Matrix
// https://leetcode.com/problems/reconstruct-a-2-row-binary-matrix/

class Solution {
    /**
     * @param Integer $upper
     * @param Integer $lower
     * @param Integer[] $colsum
     * @return Integer[][]
     */
    function reconstructMatrix($upper, $lower, $colsum) {
        $len = count($colsum);
        $top = array_fill(0, $len, 0);
        $bottom = array_fill(0, $len, 0);
        for ($i = 0; $i < $len; $i++) {
            if ($colsum[$i] === 2) {
                $top[$i] = $bottom[$i] = 1;
                $upper--; $lower--;
            }
        }
        if ($upper < 0 || $lower < 0) return [];
        for ($i = 0; $i < $len; $i++) {
            if ($colsum[$i] === 1) {
                if ($upper > 0) { $top[$i] = 1; $upper--; }
                elseif ($lower > 0) { $bottom[$i] = 1; $lower--; }
                else return [];
            }
        }
        return ($upper === 0 && $lower === 0) ? [$top, $bottom] : [];
    }
}
""")

add("1254_number_of_closed_islands", r"""<?php
// LeetCode 1254 - Number of Closed Islands
// https://leetcode.com/problems/number-of-closed-islands/

class Solution {
    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function closedIsland($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        $flood = function ($sr, $sc) use (&$grid, $m, $n) {
            $stack = [[$sr, $sc]];
            $closed = true;
            $grid[$sr][$sc] = 1;
            while (!empty($stack)) {
                [$r, $c] = array_pop($stack);
                if ($r === 0 || $r === $m - 1 || $c === 0 || $c === $n - 1) $closed = false;
                foreach ([[1,0],[-1,0],[0,1],[0,-1]] as [$dr, $dc]) {
                    $nr = $r + $dr; $nc = $c + $dc;
                    if ($nr >= 0 && $nr < $m && $nc >= 0 && $nc < $n && $grid[$nr][$nc] === 0) {
                        $grid[$nr][$nc] = 1;
                        $stack[] = [$nr, $nc];
                    }
                }
            }
            return $closed;
        };
        $ans = 0;
        for ($r = 0; $r < $m; $r++) {
            for ($c = 0; $c < $n; $c++) {
                if ($grid[$r][$c] === 0 && $flood($r, $c)) $ans++;
            }
        }
        return $ans;
    }
}
""")

add("1255_maximum_score_words_formed_by_letters", r"""<?php
// LeetCode 1255 - Maximum Score Words Formed by Letters
// https://leetcode.com/problems/maximum-score-words-formed-by-letters/

class Solution {
    /**
     * @param String[] $words
     * @param String[] $letters
     * @param Integer[] $score
     * @return Integer
     */
    function maxScoreWords($words, $letters, $score) {
        $available = array_count_values($letters);
        $counts = [];
        $values = [];
        foreach ($words as $word) {
            $counts[] = array_count_values(str_split($word));
            $v = 0;
            $len = strlen($word);
            for ($i = 0; $i < $len; $i++) $v += $score[ord($word[$i]) - 97];
            $values[] = $v;
        }
        $dfs = function ($i) use (&$dfs, &$available, $counts, $values, $words) {
            if ($i === count($words)) return 0;
            $best = $dfs($i + 1);
            $ok = true;
            foreach ($counts[$i] as $ch => $need) {
                if (($available[$ch] ?? 0) < $need) { $ok = false; break; }
            }
            if ($ok) {
                foreach ($counts[$i] as $ch => $need) $available[$ch] -= $need;
                $best = max($best, $values[$i] + $dfs($i + 1));
                foreach ($counts[$i] as $ch => $need) $available[$ch] += $need;
            }
            return $best;
        };
        return $dfs(0);
    }
}
""")

add("1256_encode_number", r"""<?php
// LeetCode 1256 - Encode Number
// https://leetcode.com/problems/encode-number/

class Solution {
    /**
     * @param Integer $num
     * @return String
     */
    function encode($num) {
        return substr(decbin($num + 1), 1);
    }
}
""")

add("1257_smallest_common_region", r"""<?php
// LeetCode 1257 - Smallest Common Region
// https://leetcode.com/problems/smallest-common-region/

class Solution {
    /**
     * @param String[][] $regions
     * @param String $region1
     * @param String $region2
     * @return String
     */
    function findSmallestRegion($regions, $region1, $region2) {
        $parent = [];
        foreach ($regions as $group) {
            for ($i = 1; $i < count($group); $i++) {
                $parent[$group[$i]] = $group[0];
            }
        }
        $ancestors = [];
        while ($region1) {
            $ancestors[$region1] = true;
            $region1 = $parent[$region1] ?? null;
        }
        while (!isset($ancestors[$region2])) {
            $region2 = $parent[$region2];
        }
        return $region2;
    }
}
""")

add("1258_synonymous_sentences", r"""<?php
// LeetCode 1258 - Synonymous Sentences
// https://leetcode.com/problems/synonymous-sentences/

class Solution {
    /**
     * @param String[][] $synonyms
     * @param String $text
     * @return String[]
     */
    function generateSentences($synonyms, $text) {
        $parent = [];
        $find = function ($x) use (&$parent, &$find) {
            if (!isset($parent[$x])) $parent[$x] = $x;
            if ($parent[$x] !== $x) $parent[$x] = $find($parent[$x]);
            return $parent[$x];
        };
        foreach ($synonyms as [$a, $b]) {
            $ra = $find($a); $rb = $find($b);
            $parent[$ra] = $rb;
        }
        $groups = [];
        foreach ($parent as $word => $_) {
            $groups[$find($word)][] = $word;
        }
        foreach ($groups as &$g) sort($g);
        unset($g);
        $words = explode(' ', $text);
        $choices = [];
        foreach ($words as $w) {
            if (isset($parent[$w])) $choices[] = $groups[$find($w)];
            else $choices[] = [$w];
        }
        $result = [];
        $dfs = function ($i, $cur) use (&$dfs, &$result, $choices) {
            if ($i === count($choices)) {
                $result[] = implode(' ', $cur);
                return;
            }
            foreach ($choices[$i] as $w) {
                $cur[] = $w;
                $dfs($i + 1, $cur);
                array_pop($cur);
            }
        };
        $dfs(0, []);
        return $result;
    }
}
""")

add("1259_handshakes_that_dont_cross", r"""<?php
// LeetCode 1259 - Handshakes That Don't Cross
// https://leetcode.com/problems/handshakes-that-dont-cross/

class Solution {
    /**
     * @param Integer $numPeople
     * @return Integer
     */
    function numberOfWays($numPeople) {
        $mod = 1000000007;
        $dp = array_fill(0, $numPeople + 1, 0);
        $dp[0] = 1;
        for ($people = 2; $people <= $numPeople; $people += 2) {
            $sum = 0;
            for ($left = 0; $left < $people; $left += 2) {
                $sum = ($sum + $dp[$left] * $dp[$people - 2 - $left]) % $mod;
            }
            $dp[$people] = $sum;
        }
        return $dp[$numPeople];
    }
}
""")

add("1260_shift_2d_grid", r"""<?php
// LeetCode 1260 - Shift 2D Grid
// https://leetcode.com/problems/shift-2d-grid/

class Solution {
    /**
     * @param Integer[][] $grid
     * @param Integer $k
     * @return Integer[][]
     */
    function shiftGrid($grid, $k) {
        $m = count($grid);
        $n = count($grid[0]);
        $flat = [];
        foreach ($grid as $row) foreach ($row as $v) $flat[] = $v;
        $len = count($flat);
        $k %= $len;
        if ($k) $flat = array_merge(array_slice($flat, -$k), array_slice($flat, 0, $len - $k));
        $ans = [];
        for ($i = 0; $i < $m; $i++) $ans[] = array_slice($flat, $i * $n, $n);
        return $ans;
    }
}
""")

add("1261_find_elements_in_a_contaminated_binary_tree", r"""<?php
// LeetCode 1261 - Find Elements in a Contaminated Binary Tree
// https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/

class FindElements {
    private $values = [];

    /**
     * @param TreeNode $root
     */
    function __construct($root) {
        $recover = function ($node, $value) use (&$recover) {
            if ($node === null) return;
            $node->val = $value;
            $this->values[$value] = true;
            $recover($node->left, 2 * $value + 1);
            $recover($node->right, 2 * $value + 2);
        };
        $recover($root, 0);
    }

    /**
     * @param Integer $target
     * @return Boolean
     */
    function find($target) {
        return isset($this->values[$target]);
    }
}
""")

add("1262_greatest_sum_divisible_by_three", r"""<?php
// LeetCode 1262 - Greatest Sum Divisible by Three
// https://leetcode.com/problems/greatest-sum-divisible-by-three/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maxSumDivThree($nums) {
        $impossible = -1000000000000000000;
        $dp = [0, $impossible, $impossible];
        foreach ($nums as $value) {
            $old = $dp;
            foreach ($old as $total) {
                if ($total === $impossible) continue;
                $remainder = ($total + $value) % 3;
                $dp[$remainder] = max($dp[$remainder], $total + $value);
            }
        }
        return $dp[0];
    }
}
""")

add("1263_minimum_moves_to_move_a_box_to_their_target_location", r"""<?php
// LeetCode 1263 - Minimum Moves to Move a Box to Their Target Location
// https://leetcode.com/problems/minimum-moves-to-move-a-box-to-their-target-location/

class Solution {
    /**
     * @param String[][] $grid
     * @return Integer
     */
    function minPushBox($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        $box = $player = $target = null;
        for ($r = 0; $r < $m; $r++) {
            for ($c = 0; $c < $n; $c++) {
                if ($grid[$r][$c] === 'B') $box = [$r, $c];
                elseif ($grid[$r][$c] === 'S') $player = [$r, $c];
                elseif ($grid[$r][$c] === 'T') $target = [$r, $c];
            }
        }
        $reachable = function ($start, $blocked) use ($grid, $m, $n) {
            $seen = [$start[0] . ',' . $start[1] => true];
            $stack = [$start];
            while (!empty($stack)) {
                [$r, $c] = array_pop($stack);
                foreach ([[1,0],[-1,0],[0,1],[0,-1]] as [$dr, $dc]) {
                    $nr = $r + $dr; $nc = $c + $dc;
                    $key = "$nr,$nc";
                    if ($nr >= 0 && $nr < $m && $nc >= 0 && $nc < $n
                        && $grid[$nr][$nc] !== '#'
                        && !($nr === $blocked[0] && $nc === $blocked[1])
                        && !isset($seen[$key])) {
                        $seen[$key] = true;
                        $stack[] = [$nr, $nc];
                    }
                }
            }
            return $seen;
        };
        $queue = [[$box, $player, 0]];
        $seen = [$box[0] . ',' . $box[1] . ',' . $player[0] . ',' . $player[1] => true];
        $head = 0;
        while ($head < count($queue)) {
            [$b, $p, $pushes] = $queue[$head++];
            if ($b[0] === $target[0] && $b[1] === $target[1]) return $pushes;
            $canReach = $reachable($p, $b);
            foreach ([[1,0],[-1,0],[0,1],[0,-1]] as [$dr, $dc]) {
                $stand = [$b[0] - $dr, $b[1] - $dc];
                $nb = [$b[0] + $dr, $b[1] + $dc];
                $standKey = $stand[0] . ',' . $stand[1];
                if (isset($canReach[$standKey])
                    && $nb[0] >= 0 && $nb[0] < $m && $nb[1] >= 0 && $nb[1] < $n
                    && $grid[$nb[0]][$nb[1]] !== '#') {
                    $state = $nb[0] . ',' . $nb[1] . ',' . $b[0] . ',' . $b[1];
                    if (!isset($seen[$state])) {
                        $seen[$state] = true;
                        $queue[] = [$nb, $b, $pushes + 1];
                    }
                }
            }
        }
        return -1;
    }
}
""")

add("1265_print_immutable_linked_list_in_reverse", r"""<?php
// LeetCode 1265 - Print Immutable Linked List in Reverse
// https://leetcode.com/problems/print-immutable-linked-list-in-reverse/

class Solution {
    /**
     * @param ImmutableListNode $head
     * @return NULL
     */
    function printLinkedListInReverse($head) {
        if ($head === null) return;
        $this->printLinkedListInReverse($head->getNext());
        $head->printValue();
    }
}
""")

add("1266_minimum_time_visiting_all_points", r"""<?php
// LeetCode 1266 - Minimum Time Visiting All Points
// https://leetcode.com/problems/minimum-time-visiting-all-points/

class Solution {
    /**
     * @param Integer[][] $points
     * @return Integer
     */
    function minTimeToVisitAllPoints($points) {
        $ans = 0;
        $n = count($points);
        for ($i = 0; $i < $n - 1; $i++) {
            $ans += max(abs($points[$i][0] - $points[$i + 1][0]), abs($points[$i][1] - $points[$i + 1][1]));
        }
        return $ans;
    }
}
""")

add("1267_count_servers_that_communicate", r"""<?php
// LeetCode 1267 - Count Servers that Communicate
// https://leetcode.com/problems/count-servers-that-communicate/

class Solution {
    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function countServers($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        $rows = array_fill(0, $m, 0);
        $cols = array_fill(0, $n, 0);
        for ($r = 0; $r < $m; $r++) {
            for ($c = 0; $c < $n; $c++) {
                if ($grid[$r][$c]) { $rows[$r]++; $cols[$c]++; }
            }
        }
        $ans = 0;
        for ($r = 0; $r < $m; $r++) {
            for ($c = 0; $c < $n; $c++) {
                if ($grid[$r][$c] && ($rows[$r] > 1 || $cols[$c] > 1)) $ans++;
            }
        }
        return $ans;
    }
}
""")

add("1268_search_suggestions_system", r"""<?php
// LeetCode 1268 - Search Suggestions System
// https://leetcode.com/problems/search-suggestions-system/

class Solution {
    /**
     * @param String[] $products
     * @param String $searchWord
     * @return String[][]
     */
    function suggestedProducts($products, $searchWord) {
        sort($products);
        $answer = [];
        $prefix = '';
        $len = strlen($searchWord);
        for ($i = 0; $i < $len; $i++) {
            $prefix .= $searchWord[$i];
            $lo = 0; $hi = count($products);
            while ($lo < $hi) {
                $mid = ($lo + $hi) >> 1;
                if ($products[$mid] < $prefix) $lo = $mid + 1;
                else $hi = $mid;
            }
            $group = [];
            for ($j = $lo; $j < min($lo + 3, count($products)); $j++) {
                if (str_starts_with($products[$j], $prefix)) $group[] = $products[$j];
            }
            $answer[] = $group;
        }
        return $answer;
    }
}
""")

add("1269_number_of_ways_to_stay_in_the_same_place_after_some_steps", r"""<?php
// LeetCode 1269 - Number of Ways to Stay in the Same Place After Some Steps
// https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/

class Solution {
    /**
     * @param Integer $steps
     * @param Integer $arrLen
     * @return Integer
     */
    function numWays($steps, $arrLen) {
        $mod = 1000000007;
        $width = min($arrLen, intdiv($steps, 2) + 1);
        $dp = array_fill(0, $width, 0);
        $dp[0] = 1;
        for ($s = 0; $s < $steps; $s++) {
            $nxt = array_fill(0, $width, 0);
            for ($i = 0; $i < $width; $i++) {
                $nxt[$i] = $dp[$i];
                if ($i > 0) $nxt[$i] = ($nxt[$i] + $dp[$i - 1]) % $mod;
                if ($i + 1 < $width) $nxt[$i] = ($nxt[$i] + $dp[$i + 1]) % $mod;
            }
            $dp = $nxt;
        }
        return $dp[0];
    }
}
""")


def is_stub(path: Path) -> bool:
    return "function solve()" in path.read_text(encoding="utf-8")


def main() -> None:
    ported = 0
    for folder, content in SOLUTIONS.items():
        path = ROOT / folder / "solution.php"
        if not path.exists():
            print(f"MISSING {folder}")
            continue
        if not is_stub(path):
            print(f"skip done {folder}")
            continue
        path.write_text(content, encoding="utf-8", newline="\n")
        ported += 1
        print(f"ported {folder}")
    print(f"ported={ported} total={len(SOLUTIONS)}")


if __name__ == "__main__":
    main()

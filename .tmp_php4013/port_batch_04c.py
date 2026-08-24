#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOLUTIONS: dict[str, str] = {}


def add(name: str, content: str) -> None:
    SOLUTIONS[name] = content.strip() + "\n"


add("2052_minimum_cost_to_separate_sentence_into_rows", r"""<?php
// LeetCode 2052 - Minimum Cost to Separate Sentence Into Rows
// https://leetcode.com/problems/minimum-cost-to-separate-sentence-into-rows/

class Solution {
    /**
     * @param String $sentence
     * @param Integer $k
     * @return Integer
     */
    function minimumCost($sentence, $k) {
        $words = preg_split('/\s+/', trim($sentence));
        $n = count($words);
        $INF = PHP_INT_MAX / 4;
        $dp = array_fill(0, $n + 1, $INF);
        $dp[$n] = 0;
        for ($i = $n - 1; $i >= 0; $i--) {
            $length = -1;
            for ($j = $i; $j < $n; $j++) {
                $length += 1 + strlen($words[$j]);
                if ($length > $k) break;
                $cost = 0;
                if ($j < $n - 1) {
                    $extra = $k - $length;
                    $cost = $extra * $extra;
                }
                $dp[$i] = min($dp[$i], $cost + $dp[$j + 1]);
            }
        }
        return $dp[0];
    }
}
""")

add("2053_kth_distinct_string_in_an_array", r"""<?php
// LeetCode 2053 - Kth Distinct String in an Array
// https://leetcode.com/problems/kth-distinct-string-in-an-array/

class Solution {
    /**
     * @param String[] $arr
     * @param Integer $k
     * @return String
     */
    function kthDistinct($arr, $k) {
        $freq = [];
        foreach ($arr as $s) $freq[$s] = ($freq[$s] ?? 0) + 1;
        foreach ($arr as $s) if ($freq[$s] === 1 && --$k === 0) return $s;
        return "";
    }
}
""")

add("2054_two_best_non_overlapping_events", r"""<?php
// LeetCode 2054 - Two Best Non-Overlapping Events
// https://leetcode.com/problems/two-best-non-overlapping-events/

class Solution {
    /**
     * @param Integer[][] $events
     * @return Integer
     */
    function maxTwoEvents($events) {
        usort($events, fn($a, $b) => $a[0] <=> $b[0]);
        $n = count($events);
        $suffix = array_fill(0, $n + 1, 0);
        for ($i = $n - 1; $i >= 0; $i--) $suffix[$i] = max($suffix[$i + 1], $events[$i][2]);
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            $ans = max($ans, $events[$i][2]);
            $lo = $i + 1;
            $hi = $n;
            while ($lo < $hi) {
                $mid = ($lo + $hi) >> 1;
                if ($events[$mid][0] > $events[$i][1]) $hi = $mid;
                else $lo = $mid + 1;
            }
            if ($lo < $n) $ans = max($ans, $events[$i][2] + $suffix[$lo]);
        }
        return $ans;
    }
}
""")

add("2055_plates_between_candles", r"""<?php
// LeetCode 2055 - Plates Between Candles
// https://leetcode.com/problems/plates-between-candles/

class Solution {
    /**
     * @param String $s
     * @param Integer[][] $queries
     * @return Integer[]
     */
    function platesBetweenCandles($s, $queries) {
        $n = strlen($s);
        $pref = array_fill(0, $n + 1, 0);
        $left = array_fill(0, $n, -1);
        $right = array_fill(0, $n, -1);
        $last = -1;
        for ($i = 0; $i < $n; $i++) {
            $pref[$i + 1] = $pref[$i] + ($s[$i] === '*' ? 1 : 0);
            if ($s[$i] === '|') $last = $i;
            $left[$i] = $last;
        }
        $last = -1;
        for ($i = $n - 1; $i >= 0; $i--) {
            if ($s[$i] === '|') $last = $i;
            $right[$i] = $last;
        }
        $ans = [];
        foreach ($queries as $i => $q) {
            $l = $right[$q[0]];
            $r = $left[$q[1]];
            if ($l !== -1 && $r !== -1 && $l < $r) $ans[$i] = $pref[$r] - $pref[$l];
            else $ans[$i] = 0;
        }
        return $ans;
    }
}
""")

add("2056_number_of_valid_move_combinations_on_chessboard", r"""<?php
// LeetCode 2056 - Number of Valid Move Combinations On Chessboard
// https://leetcode.com/problems/number-of-valid-move-combinations-on-chessboard/

class Solution {
    /**
     * @param String[] $pieces
     * @param Integer[][] $positions
     * @return Integer
     */
    function countCombinations($pieces, $positions) {
        $dirs = [
            'rook' => [[1, 0], [-1, 0], [0, 1], [0, -1]],
            'bishop' => [[1, 1], [1, -1], [-1, 1], [-1, -1]],
            'queen' => [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]],
        ];
        $n = count($pieces);
        $allMoves = array_fill(0, $n, []);
        for ($i = 0; $i < $n; $i++) {
            $ms = [['dr' => 0, 'dc' => 0, 'steps' => 0]];
            $r = $positions[$i][0];
            $c = $positions[$i][1];
            foreach ($dirs[$pieces[$i]] as $d) {
                $nr = $r + $d[0];
                $nc = $c + $d[1];
                $step = 1;
                while ($nr >= 1 && $nr <= 8 && $nc >= 1 && $nc <= 8) {
                    $ms[] = ['dr' => $d[0], 'dc' => $d[1], 'steps' => $step];
                    $nr += $d[0];
                    $nc += $d[1];
                    $step++;
                }
            }
            $allMoves[$i] = $ms;
        }
        $chosen = array_fill(0, $n, null);
        $ans = 0;
        $okCombo = function ($end) use (&$chosen, $positions) {
            $maxT = 0;
            for ($i = 0; $i <= $end; $i++) $maxT = max($maxT, $chosen[$i]['steps']);
            for ($t = 1; $t <= $maxT; $t++) {
                $seen = [];
                for ($i = 0; $i <= $end; $i++) {
                    $m = $chosen[$i];
                    if ($m['steps'] === 0) { $pr = $positions[$i][0]; $pc = $positions[$i][1]; }
                    else {
                        $use = min($t, $m['steps']);
                        $pr = $positions[$i][0] + $m['dr'] * $use;
                        $pc = $positions[$i][1] + $m['dc'] * $use;
                    }
                    $key = $pr . "," . $pc;
                    if (isset($seen[$key])) return false;
                    $seen[$key] = true;
                }
            }
            return true;
        };
        $dfs = null;
        $dfs = function ($i) use (&$dfs, &$ans, &$chosen, &$allMoves, $pieces, $okCombo) {
            if ($i === count($pieces)) { $ans++; return; }
            foreach ($allMoves[$i] as $m) {
                $chosen[$i] = $m;
                if ($okCombo($i)) $dfs($i + 1);
            }
        };
        $dfs(0);
        return $ans;
    }
}
""")

add("2057_smallest_index_with_equal_value", r"""<?php
// LeetCode 2057 - Smallest Index With Equal Value
// https://leetcode.com/problems/smallest-index-with-equal-value/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function smallestEqual($nums) {
        $n = count($nums);
        for ($i = 0; $i < $n; $i++)
            if ($i % 10 === $nums[$i]) return $i;
        return -1;
    }
}
""")

add("2058_find_the_minimum_and_maximum_number_of_nodes_between_critical_points", r"""<?php
// LeetCode 2058 - Find the Minimum and Maximum Number of Nodes Between Critical Points
// https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/

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
     * @return Integer[]
     */
    function nodesBetweenCriticalPoints($head) {
        $crit = [];
        $prev = $head;
        $cur = $head->next;
        $idx = 1;
        while ($cur && $cur->next) {
            if (($cur->val > $prev->val && $cur->val > $cur->next->val) ||
                ($cur->val < $prev->val && $cur->val < $cur->next->val))
                $crit[] = $idx;
            $prev = $cur;
            $cur = $cur->next;
            $idx++;
        }
        if (count($crit) < 2) return [-1, -1];
        $mn = $crit[1] - $crit[0];
        $cn = count($crit);
        for ($i = 2; $i < $cn; $i++) $mn = min($mn, $crit[$i] - $crit[$i - 1]);
        return [$mn, $crit[$cn - 1] - $crit[0]];
    }
}
""")

add("2059_minimum_operations_to_convert_number", r"""<?php
// LeetCode 2059 - Minimum Operations to Convert Number
// https://leetcode.com/problems/minimum-operations-to-convert-number/

class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $start
     * @param Integer $goal
     * @return Integer
     */
    function minimumOperations($nums, $start, $goal) {
        if ($start === $goal) return 0;
        $vis = [$start => true];
        $q = [$start];
        $steps = 0;
        while ($q) {
            $steps++;
            $sz = count($q);
            while ($sz-- > 0) {
                $cur = array_shift($q);
                foreach ($nums as $x) {
                    foreach ([$cur + $x, $cur - $x, $cur ^ $x] as $nxt) {
                        if ($nxt === $goal) return $steps;
                        if ($nxt >= 0 && $nxt <= 1000 && !isset($vis[$nxt])) {
                            $vis[$nxt] = true;
                            $q[] = $nxt;
                        }
                    }
                }
            }
        }
        return -1;
    }
}
""")

add("2060_check_if_an_original_string_exists_given_two_encoded_strings", r"""<?php
// LeetCode 2060 - Check if an Original String Exists Given Two Encoded Strings
// https://leetcode.com/problems/check-if-an-original-string-exists-given-two-encoded-strings/

class Solution {
    /**
     * @param String $s1
     * @param String $s2
     * @return Boolean
     */
    function possiblyEquals($s1, $s2) {
        $memo = [];
        $isDigit = function ($c) { return $c >= '0' && $c <= '9'; };
        $dfs = null;
        $dfs = function ($i, $j, $diff) use (&$dfs, &$memo, $s1, $s2, $isDigit) {
            $key = $i . "," . $j . "," . $diff;
            if (isset($memo[$key])) return $memo[$key];
            $n = strlen($s1);
            $m = strlen($s2);
            if ($i === $n && $j === $m) { $memo[$key] = $diff === 0; return $diff === 0; }
            $res = false;
            if ($diff === 0 && $i < $n && $j < $m && !$isDigit($s1[$i]) && !$isDigit($s2[$j])) {
                if ($s1[$i] === $s2[$j]) $res = $dfs($i + 1, $j + 1, 0);
            } else if ($diff > 0 && $i < $n && !$isDigit($s1[$i])) {
                $res = $dfs($i + 1, $j, $diff - 1);
            } else if ($diff < 0 && $j < $m && !$isDigit($s2[$j])) {
                $res = $dfs($i, $j + 1, $diff + 1);
            }
            if (!$res && $i < $n && $isDigit($s1[$i])) {
                $val = 0;
                for ($p = $i; $p < $n && $isDigit($s1[$p]); $p++) {
                    $val = $val * 10 + (ord($s1[$p]) - 48);
                    if ($dfs($p + 1, $j, $diff + $val)) { $res = true; break; }
                }
            }
            if (!$res && $j < $m && $isDigit($s2[$j])) {
                $val = 0;
                for ($p = $j; $p < $m && $isDigit($s2[$p]); $p++) {
                    $val = $val * 10 + (ord($s2[$p]) - 48);
                    if ($dfs($i, $p + 1, $diff - $val)) { $res = true; break; }
                }
            }
            $memo[$key] = $res;
            return $res;
        };
        return $dfs(0, 0, 0);
    }
}
""")

add("2061_number_of_spaces_cleaning_robot_cleaned", r"""<?php
// LeetCode 2061 - Number of Spaces Cleaning Robot Cleaned
// https://leetcode.com/problems/number-of-spaces-cleaning-robot-cleaned/

class Solution {
    /**
     * @param Integer[][] $room
     * @return Integer
     */
    function numberOfCleanRooms($room) {
        $m = count($room);
        $n = count($room[0]);
        $dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]];
        $vis = [];
        $cleaned = ["0,0" => true];
        $r = 0;
        $c = 0;
        $d = 0;
        while (true) {
            $state = $r * 10000 + $c * 10 + $d;
            if (isset($vis[$state])) break;
            $vis[$state] = true;
            $nr = $r + $dirs[$d][0];
            $nc = $c + $dirs[$d][1];
            if ($nr >= 0 && $nr < $m && $nc >= 0 && $nc < $n && $room[$nr][$nc] === 0) {
                $r = $nr;
                $c = $nc;
                $cleaned[$r . "," . $c] = true;
            } else $d = ($d + 1) % 4;
        }
        return count($cleaned);
    }
}
""")

add("2062_count_vowel_substrings_of_a_string", r"""<?php
// LeetCode 2062 - Count Vowel Substrings of a String
// https://leetcode.com/problems/count-vowel-substrings-of-a-string/

class Solution {
    /**
     * @param String $word
     * @return Integer
     */
    function countVowelSubstrings($word) {
        $isVowel = function ($c) { return strpos("aeiou", $c) !== false; };
        $ans = 0;
        $n = strlen($word);
        for ($i = 0; $i < $n; $i++) {
            $seen = [];
            for ($j = $i; $j < $n && $isVowel($word[$j]); $j++) {
                $seen[$word[$j]] = true;
                if (count($seen) === 5) $ans++;
            }
        }
        return $ans;
    }
}
""")

add("2063_vowels_of_all_substrings", r"""<?php
// LeetCode 2063 - Vowels of All Substrings
// https://leetcode.com/problems/vowels-of-all-substrings/

class Solution {
    /**
     * @param String $word
     * @return Integer
     */
    function countVowels($word) {
        $n = strlen($word);
        $ans = 0;
        for ($i = 0; $i < $n; $i++)
            if (strpos("aeiou", $word[$i]) !== false) $ans += ($i + 1) * ($n - $i);
        return $ans;
    }
}
""")

add("2064_minimized_maximum_of_products_distributed_to_any_store", r"""<?php
// LeetCode 2064 - Minimized Maximum of Products Distributed to Any Store
// https://leetcode.com/problems/minimized-maximum-of-products-distributed-to-any-store/

class Solution {
    /**
     * @param Integer $n
     * @param Integer[] $quantities
     * @return Integer
     */
    function minimizedMaximum($n, $quantities) {
        $can = function ($x) use ($quantities, $n) {
            $need = 0;
            foreach ($quantities as $q) {
                $need += intdiv($q + $x - 1, $x);
                if ($need > $n) return false;
            }
            return true;
        };
        $lo = 1;
        $hi = 0;
        foreach ($quantities as $q) $hi = max($hi, $q);
        while ($lo < $hi) {
            $mid = ($lo + $hi) >> 1;
            if ($can($mid)) $hi = $mid;
            else $lo = $mid + 1;
        }
        return $lo;
    }
}
""")

add("2065_maximum_path_quality_of_a_graph", r"""<?php
// LeetCode 2065 - Maximum Path Quality of a Graph
// https://leetcode.com/problems/maximum-path-quality-of-a-graph/

class Solution {
    /**
     * @param Integer[] $values
     * @param Integer[][] $edges
     * @param Integer $maxTime
     * @return Integer
     */
    function maximalPathQuality($values, $edges, $maxTime) {
        $n = count($values);
        $g = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $g[$e[0]][] = [$e[1], $e[2]];
            $g[$e[1]][] = [$e[0], $e[2]];
        }
        $ans = 0;
        $vis = array_fill(0, $n, 0);
        $dfs = null;
        $dfs = function ($u, $time, $quality) use (&$dfs, &$ans, &$vis, $g, $values, $maxTime) {
            if ($time > $maxTime) return;
            $first = $vis[$u] === 0;
            if ($first) $quality += $values[$u];
            $vis[$u]++;
            if ($u === 0) $ans = max($ans, $quality);
            foreach ($g[$u] as $e) $dfs($e[0], $time + $e[1], $quality);
            $vis[$u]--;
        };
        $dfs(0, 0, 0);
        return $ans;
    }
}
""")

add("2067_number_of_equal_count_substrings", r"""<?php
// LeetCode 2067 - Number of Equal Count Substrings
// https://leetcode.com/problems/number-of-equal-count-substrings/

class Solution {
    /**
     * @param String $s
     * @param Integer $count
     * @return Integer
     */
    function equalCountSubstrings($s, $count) {
        $ans = 0;
        $n = strlen($s);
        $seen = array_fill(0, 26, false);
        $maxUnique = 0;
        for ($i = 0; $i < $n; $i++) {
            $idx = ord($s[$i]) - 97;
            if (!$seen[$idx]) { $seen[$idx] = true; $maxUnique++; }
        }
        for ($u = 1; $u <= $maxUnique; $u++) {
            $needLen = $u * $count;
            if ($needLen > $n) break;
            $freq = array_fill(0, 26, 0);
            $have = 0;
            for ($i = 0; $i < $n; $i++) {
                $c = ord($s[$i]) - 97;
                $freq[$c]++;
                if ($freq[$c] === $count) $have++;
                else if ($freq[$c] === $count + 1) $have--;
                if ($i >= $needLen) {
                    $p = ord($s[$i - $needLen]) - 97;
                    if ($freq[$p] === $count) $have--;
                    else if ($freq[$p] === $count + 1) $have++;
                    $freq[$p]--;
                }
                if ($i + 1 >= $needLen && $have === $u) $ans++;
            }
        }
        return $ans;
    }
}
""")

add("2068_check_whether_two_strings_are_almost_equivalent", r"""<?php
// LeetCode 2068 - Check Whether Two Strings Are Almost Equivalent
// https://leetcode.com/problems/check-whether-two-strings-are-almost-equivalent/

class Solution {
    /**
     * @param String $word1
     * @param String $word2
     * @return Boolean
     */
    function checkAlmostEquivalent($word1, $word2) {
        $freq = array_fill(0, 26, 0);
        $n = strlen($word1);
        for ($i = 0; $i < $n; $i++) {
            $freq[ord($word1[$i]) - 97]++;
            $freq[ord($word2[$i]) - 97]--;
        }
        foreach ($freq as $v) if ($v > 3 || $v < -3) return false;
        return true;
    }
}
""")

add("2069_walking_robot_simulation_ii", r"""<?php
// LeetCode 2069 - Walking Robot Simulation II
// https://leetcode.com/problems/walking-robot-simulation-ii/

class Robot {
    private $w;
    private $h;
    private $peri;
    private $pos = 0;
    private $moved = false;

    /**
     * @param Integer $width
     * @param Integer $height
     */
    function __construct($width, $height) {
        $this->w = $width;
        $this->h = $height;
        $this->peri = 2 * ($width + $height) - 4;
        $this->pos = 0;
        $this->moved = false;
    }

    private function getPosDir() {
        $p = $this->pos;
        if ($p === 0) {
            if (!$this->moved) return [0, 0, 0];
            return [0, 0, 3];
        }
        if ($p <= $this->w - 1) return [$p, 0, 0];
        $p -= $this->w - 1;
        if ($p <= $this->h - 1) return [$this->w - 1, $p, 1];
        $p -= $this->h - 1;
        if ($p <= $this->w - 1) return [$this->w - 1 - $p, $this->h - 1, 2];
        $p -= $this->w - 1;
        return [0, $this->h - 1 - $p, 3];
    }

    /**
     * @param Integer $num
     * @return NULL
     */
    function step($num) {
        $this->moved = true;
        $this->pos = ($this->pos + $num) % $this->peri;
    }

    /**
     * @return Integer[]
     */
    function getPos() {
        $pd = $this->getPosDir();
        return [$pd[0], $pd[1]];
    }

    /**
     * @return String
     */
    function getDir() {
        $names = ["East", "North", "West", "South"];
        return $names[$this->getPosDir()[2]];
    }
}
""")

add("2070_most_beautiful_item_for_each_query", r"""<?php
// LeetCode 2070 - Most Beautiful Item for Each Query
// https://leetcode.com/problems/most-beautiful-item-for-each-query/

class Solution {
    /**
     * @param Integer[][] $items
     * @param Integer[] $queries
     * @return Integer[]
     */
    function maximumBeauty($items, $queries) {
        usort($items, fn($a, $b) => $a[0] <=> $b[0]);
        $maxB = 0;
        foreach ($items as &$it) {
            $maxB = max($maxB, $it[1]);
            $it[1] = $maxB;
        }
        unset($it);
        $ans = [];
        $n = count($items);
        foreach ($queries as $i => $q) {
            $lo = 0;
            $hi = $n;
            while ($lo < $hi) {
                $mid = ($lo + $hi) >> 1;
                if ($items[$mid][0] <= $q) $lo = $mid + 1;
                else $hi = $mid;
            }
            $ans[$i] = $lo === 0 ? 0 : $items[$lo - 1][1];
        }
        return $ans;
    }
}
""")

add("2071_maximum_number_of_tasks_you_can_assign", r"""<?php
// LeetCode 2071 - Maximum Number of Tasks You Can Assign
// https://leetcode.com/problems/maximum-number-of-tasks-you-can-assign/

class Solution {
    /**
     * @param Integer[] $tasks
     * @param Integer[] $workers
     * @param Integer $pills
     * @param Integer $strength
     * @return Integer
     */
    function maxTaskAssign($tasks, $workers, $pills, $strength) {
        sort($tasks);
        sort($workers);
        $remove = function (&$ws, $x) {
            $ws[$x]--;
            if ($ws[$x] === 0) unset($ws[$x]);
        };
        $can = function ($k) use ($tasks, $workers, $pills, $strength, $remove) {
            if ($k === 0) return true;
            $ws = [];
            $wn = count($workers);
            for ($i = $wn - $k; $i < $wn; $i++)
                $ws[$workers[$i]] = ($ws[$workers[$i]] ?? 0) + 1;
            $p = $pills;
            for ($i = $k - 1; $i >= 0; $i--) {
                $task = $tasks[$i];
                $ks = array_keys($ws);
                sort($ks);
                $strongest = $ks[count($ks) - 1];
                if ($strongest >= $task) {
                    $remove($ws, $strongest);
                    continue;
                }
                if ($p === 0) return false;
                $need = $task - $strength;
                $found = null;
                foreach ($ks as $key) if ($key >= $need) { $found = $key; break; }
                if ($found === null) return false;
                $remove($ws, $found);
                $p--;
            }
            return true;
        };
        $lo = 0;
        $hi = min(count($tasks), count($workers));
        while ($lo < $hi) {
            $mid = ($lo + $hi + 1) >> 1;
            if ($can($mid)) $lo = $mid;
            else $hi = $mid - 1;
        }
        return $lo;
    }
}
""")

add("2073_time_needed_to_buy_tickets", r"""<?php
// LeetCode 2073 - Time Needed to Buy Tickets
// https://leetcode.com/problems/time-needed-to-buy-tickets/

class Solution {
    /**
     * @param Integer[] $tickets
     * @param Integer $k
     * @return Integer
     */
    function timeRequiredToBuy($tickets, $k) {
        $ans = 0;
        $n = count($tickets);
        for ($i = 0; $i < $n; $i++) {
            if ($i <= $k) $ans += min($tickets[$i], $tickets[$k]);
            else $ans += min($tickets[$i], $tickets[$k] - 1);
        }
        return $ans;
    }
}
""")

add("2074_reverse_nodes_in_even_length_groups", r"""<?php
// LeetCode 2074 - Reverse Nodes in Even Length Groups
// https://leetcode.com/problems/reverse-nodes-in-even-length-groups/

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
    function reverseEvenLengthGroups($head) {
        $dummy = new ListNode(0, $head);
        $prev = $dummy;
        $group = 1;
        while ($prev->next) {
            $cur = $prev->next;
            $cnt = 0;
            $node = $cur;
            while ($node && $cnt < $group) { $node = $node->next; $cnt++; }
            if ($cnt % 2 === 0) {
                $revPrev = $node;
                $p = $cur;
                for ($i = 0; $i < $cnt; $i++) {
                    $nxt = $p->next;
                    $p->next = $revPrev;
                    $revPrev = $p;
                    $p = $nxt;
                }
                $prev->next = $revPrev;
                $prev = $cur;
            } else {
                for ($i = 0; $i < $cnt; $i++) $prev = $prev->next;
            }
            $group++;
        }
        return $dummy->next;
    }
}
""")

add("2075_decode_the_slanted_ciphertext", r"""<?php
// LeetCode 2075 - Decode the Slanted Ciphertext
// https://leetcode.com/problems/decode-the-slanted-ciphertext/

class Solution {
    /**
     * @param String $encodedText
     * @param Integer $rows
     * @return String
     */
    function decodeCiphertext($encodedText, $rows) {
        if ($rows === 1) return $encodedText;
        $cols = intdiv(strlen($encodedText), $rows);
        $b = "";
        for ($c = 0; $c < $cols; $c++)
            for ($r = 0; $r < $rows && $c + $r < $cols; $r++)
                $b .= $encodedText[$r * $cols + $c + $r];
        return rtrim($b, ' ');
    }
}
""")

add("2076_process_restricted_friend_requests", r"""<?php
// LeetCode 2076 - Process Restricted Friend Requests
// https://leetcode.com/problems/process-restricted-friend-requests/

class Solution {
    /**
     * @param Integer $n
     * @param Integer[][] $restrictions
     * @param Integer[][] $requests
     * @return Boolean[]
     */
    function friendRequests($n, $restrictions, $requests) {
        $parent = range(0, $n - 1);
        $find = null;
        $find = function ($x) use (&$parent, &$find) {
            if ($parent[$x] !== $x) $parent[$x] = $find($parent[$x]);
            return $parent[$x];
        };
        $unite = function ($a, $b) use (&$parent, &$find) {
            $a = $find($a);
            $b = $find($b);
            if ($a !== $b) $parent[$a] = $b;
        };
        $ans = [];
        foreach ($requests as $i => $req) {
            $u = $find($req[0]);
            $v = $find($req[1]);
            $ok = true;
            if ($u !== $v) {
                foreach ($restrictions as $r) {
                    $x = $find($r[0]);
                    $y = $find($r[1]);
                    if (($x === $u && $y === $v) || ($x === $v && $y === $u)) { $ok = false; break; }
                }
            }
            $ans[$i] = $ok;
            if ($ok) $unite($u, $v);
        }
        return $ans;
    }
}
""")

add("2077_paths_in_maze_that_lead_to_same_room", r"""<?php
// LeetCode 2077 - Paths in Maze That Lead to Same Room
// https://leetcode.com/problems/paths-in-maze-that-lead-to-same-room/

class Solution {
    /**
     * @param Integer $n
     * @param Integer[][] $corridors
     * @return Integer
     */
    function numberOfPaths($n, $corridors) {
        $g = array_fill(0, $n + 1, []);
        foreach ($corridors as $e) {
            $g[$e[0]][$e[1]] = true;
            $g[$e[1]][$e[0]] = true;
        }
        $ans = 0;
        foreach ($corridors as $e) {
            $a = $e[0];
            $b = $e[1];
            foreach ($g[$a] as $c => $_) if (isset($g[$b][$c])) $ans++;
        }
        return intdiv($ans, 3);
    }
}
""")

add("2078_two_furthest_houses_with_different_colors", r"""<?php
// LeetCode 2078 - Two Furthest Houses With Different Colors
// https://leetcode.com/problems/two-furthest-houses-with-different-colors/

class Solution {
    /**
     * @param Integer[] $colors
     * @return Integer
     */
    function maxDistance($colors) {
        $n = count($colors);
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            if ($colors[$i] !== $colors[0]) $ans = max($ans, $i);
            if ($colors[$i] !== $colors[$n - 1]) $ans = max($ans, $n - 1 - $i);
        }
        return $ans;
    }
}
""")

add("2079_watering_plants", r"""<?php
// LeetCode 2079 - Watering Plants
// https://leetcode.com/problems/watering-plants/

class Solution {
    /**
     * @param Integer[] $plants
     * @param Integer $capacity
     * @return Integer
     */
    function wateringPlants($plants, $capacity) {
        $ans = 0;
        $cur = $capacity;
        $n = count($plants);
        for ($i = 0; $i < $n; $i++) {
            if ($cur < $plants[$i]) { $ans += $i * 2; $cur = $capacity; }
            $cur -= $plants[$i];
            $ans++;
        }
        return $ans;
    }
}
""")

add("2080_range_frequency_queries", r"""<?php
// LeetCode 2080 - Range Frequency Queries
// https://leetcode.com/problems/range-frequency-queries/

class RangeFreqQuery {
    private $pos = [];

    /**
     * @param Integer[] $arr
     */
    function __construct($arr) {
        $this->pos = [];
        $n = count($arr);
        for ($i = 0; $i < $n; $i++) $this->pos[$arr[$i]][] = $i;
    }

    private function lower($p, $x) {
        $lo = 0;
        $hi = count($p);
        while ($lo < $hi) {
            $mid = ($lo + $hi) >> 1;
            if ($p[$mid] < $x) $lo = $mid + 1;
            else $hi = $mid;
        }
        return $lo;
    }

    private function upper($p, $x) {
        $lo = 0;
        $hi = count($p);
        while ($lo < $hi) {
            $mid = ($lo + $hi) >> 1;
            if ($p[$mid] <= $x) $lo = $mid + 1;
            else $hi = $mid;
        }
        return $lo;
    }

    /**
     * @param Integer $left
     * @param Integer $right
     * @param Integer $value
     * @return Integer
     */
    function query($left, $right, $value) {
        if (!isset($this->pos[$value])) return 0;
        $p = $this->pos[$value];
        return $this->upper($p, $right) - $this->lower($p, $left);
    }
}
""")

add("2081_sum_of_k_mirror_numbers", r"""<?php
// LeetCode 2081 - Sum of k-Mirror Numbers
// https://leetcode.com/problems/sum-of-k-mirror-numbers/

class Solution {
    /**
     * @param Integer $k
     * @param Integer $n
     * @return Integer
     */
    function kMirror($k, $n) {
        $isPalBase = function ($x, $bas) {
            $digits = [];
            while ($x > 0) { $digits[] = $x % $bas; $x = intdiv($x, $bas); }
            for ($l = 0, $r = count($digits) - 1; $l < $r; $l++, $r--)
                if ($digits[$l] !== $digits[$r]) return false;
            return true;
        };
        $ans = 0;
        $count = 0;
        for ($length = 1; $count < $n; $length++) {
            $start = 1;
            $halfLen = intdiv($length + 1, 2);
            for ($i = 1; $i < $halfLen; $i++) $start *= 10;
            $end = $start * 10;
            for ($half = $start; $half < $end && $count < $n; $half++) {
                $pal = $half;
                if ($length % 2 === 0) {
                    $x = $half;
                    while ($x > 0) { $pal = $pal * 10 + $x % 10; $x = intdiv($x, 10); }
                } else {
                    $x = intdiv($half, 10);
                    while ($x > 0) { $pal = $pal * 10 + $x % 10; $x = intdiv($x, 10); }
                }
                if ($isPalBase($pal, $k)) { $ans += $pal; $count++; }
            }
        }
        return $ans;
    }
}
""")

add("2083_substrings_that_begin_and_end_with_the_same_letter", r"""<?php
// LeetCode 2083 - Substrings That Begin and End With the Same Letter
// https://leetcode.com/problems/substrings-that-begin-and-end-with-the-same-letter/

class Solution {
    /**
     * @param String $s
     * @return Integer
     */
    function numberOfSubstrings($s) {
        $freq = array_fill(0, 26, 0);
        $ans = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $idx = ord($s[$i]) - 97;
            $freq[$idx]++;
            $ans += $freq[$idx];
        }
        return $ans;
    }
}
""")

add("2085_count_common_words_with_one_occurrence", r"""<?php
// LeetCode 2085 - Count Common Words With One Occurrence
// https://leetcode.com/problems/count-common-words-with-one-occurrence/

class Solution {
    /**
     * @param String[] $words1
     * @param String[] $words2
     * @return Integer
     */
    function countWords($words1, $words2) {
        $f1 = [];
        $f2 = [];
        foreach ($words1 as $w) $f1[$w] = ($f1[$w] ?? 0) + 1;
        foreach ($words2 as $w) $f2[$w] = ($f2[$w] ?? 0) + 1;
        $ans = 0;
        foreach ($f1 as $k => $v)
            if ($v === 1 && ($f2[$k] ?? 0) === 1) $ans++;
        return $ans;
    }
}
""")

add("2086_minimum_number_of_food_buckets_to_feed_the_hamsters", r"""<?php
// LeetCode 2086 - Minimum Number of Food Buckets to Feed the Hamsters
// https://leetcode.com/problems/minimum-number-of-food-buckets-to-feed-the-hamsters/

class Solution {
    /**
     * @param String $hamsters
     * @return Integer
     */
    function minimumBuckets($hamsters) {
        $b = str_split($hamsters);
        $ans = 0;
        $n = count($b);
        for ($i = 0; $i < $n; $i++) {
            if ($b[$i] !== 'H') continue;
            if ($i > 0 && $b[$i - 1] === 'B') continue;
            if ($i + 1 < $n && $b[$i + 1] === '.') { $b[$i + 1] = 'B'; $ans++; }
            else if ($i > 0 && $b[$i - 1] === '.') { $b[$i - 1] = 'B'; $ans++; }
            else return -1;
        }
        return $ans;
    }
}
""")

add("2087_minimum_cost_homecoming_of_a_robot_in_a_grid", r"""<?php
// LeetCode 2087 - Minimum Cost Homecoming of a Robot in a Grid
// https://leetcode.com/problems/minimum-cost-homecoming-of-a-robot-in-a-grid/

class Solution {
    /**
     * @param Integer[] $startPos
     * @param Integer[] $homePos
     * @param Integer[] $rowCosts
     * @param Integer[] $colCosts
     * @return Integer
     */
    function minCost($startPos, $homePos, $rowCosts, $colCosts) {
        $ans = 0;
        $sr = $startPos[0];
        $sc = $startPos[1];
        $hr = $homePos[0];
        $hc = $homePos[1];
        if ($sr < $hr) for ($r = $sr + 1; $r <= $hr; $r++) $ans += $rowCosts[$r];
        else for ($r = $sr - 1; $r >= $hr; $r--) $ans += $rowCosts[$r];
        if ($sc < $hc) for ($c = $sc + 1; $c <= $hc; $c++) $ans += $colCosts[$c];
        else for ($c = $sc - 1; $c >= $hc; $c--) $ans += $colCosts[$c];
        return $ans;
    }
}
""")

add("2088_count_fertile_pyramids_in_a_land", r"""<?php
// LeetCode 2088 - Count Fertile Pyramids in a Land
// https://leetcode.com/problems/count-fertile-pyramids-in-a-land/

class Solution {
    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function countPyramids($grid) {
        $count = function ($g) {
            $m = count($g);
            $n = count($g[0]);
            $dp = [];
            for ($i = 0; $i < $m; $i++) $dp[$i] = $g[$i];
            $ans = 0;
            for ($i = $m - 2; $i >= 0; $i--) {
                for ($j = 1; $j < $n - 1; $j++) {
                    if ($g[$i][$j] === 1) {
                        $dp[$i][$j] = 1 + min($dp[$i + 1][$j - 1], $dp[$i + 1][$j], $dp[$i + 1][$j + 1]);
                        $ans += $dp[$i][$j] - 1;
                    }
                }
            }
            return $ans;
        };
        $ans = $count($grid);
        $m = count($grid);
        $rev = [];
        for ($i = 0; $i < $m; $i++) $rev[$i] = $grid[$m - 1 - $i];
        return $ans + $count($rev);
    }
}
""")

add("2089_find_target_indices_after_sorting_array", r"""<?php
// LeetCode 2089 - Find Target Indices After Sorting Array
// https://leetcode.com/problems/find-target-indices-after-sorting-array/

class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $target
     * @return Integer[]
     */
    function targetIndices($nums, $target) {
        $less = 0;
        $eq = 0;
        foreach ($nums as $x) {
            if ($x < $target) $less++;
            else if ($x === $target) $eq++;
        }
        $ans = [];
        for ($i = 0; $i < $eq; $i++) $ans[] = $less + $i;
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

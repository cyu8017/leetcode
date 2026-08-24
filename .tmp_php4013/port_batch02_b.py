#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
SOLUTIONS: dict[str, str] = {}


def add(name: str, content: str) -> None:
    SOLUTIONS[name] = content.strip() + "\n"


add("0805_split_array_with_same_average", r"""<?php
// LeetCode 0805 - Split Array With Same Average
// https://leetcode.com/problems/split-array-with-same-average/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Boolean
     */
    function splitArraySameAverage($nums) {
        $n = count($nums);
        $total = 0;
        foreach ($nums as $x) $total += $x;
        sort($nums);
        $memo = [];
        $find = function($target, $count, $index) use (&$find, &$memo, $nums, $n) {
            if ($count === 0) return $target === 0;
            if ($index === $n || $count + $index > $n || $target < 0) return false;
            $key = ($target * 1048576) + ($count * 1024) + $index;
            if (isset($memo[$key])) return false;
            if ($find($target - $nums[$index], $count - 1, $index + 1) || $find($target, $count, $index + 1)) {
                return true;
            }
            $memo[$key] = true;
            return false;
        };
        for ($size = 1; $size < $n; $size++) {
            if (($total * $size) % $n === 0 && $find(intdiv($total * $size, $n), $size, 0)) return true;
        }
        return false;
    }
}
""")

add("0806_number_of_lines_to_write_string", r"""<?php
// LeetCode 0806 - Number of Lines To Write String
// https://leetcode.com/problems/number-of-lines-to-write-string/

class Solution {
    /**
     * @param Integer[] $widths
     * @param String $s
     * @return Integer[]
     */
    function numberOfLines($widths, $s) {
        $lines = 1;
        $width = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $w = $widths[ord($s[$i]) - 97];
            if ($width + $w > 100) {
                $lines++;
                $width = $w;
            } else {
                $width += $w;
            }
        }
        return [$lines, $width];
    }
}
""")

add("0807_max_increase_to_keep_city_skyline", r"""<?php
// LeetCode 0807 - Max Increase to Keep City Skyline
// https://leetcode.com/problems/max-increase-to-keep-city-skyline/

class Solution {
    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function maxIncreaseKeepingSkyline($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        $rowMax = array_fill(0, $m, 0);
        $colMax = array_fill(0, $n, 0);
        for ($r = 0; $r < $m; $r++) {
            for ($c = 0; $c < $n; $c++) {
                $rowMax[$r] = max($rowMax[$r], $grid[$r][$c]);
                $colMax[$c] = max($colMax[$c], $grid[$r][$c]);
            }
        }
        $ans = 0;
        for ($r = 0; $r < $m; $r++) {
            for ($c = 0; $c < $n; $c++) {
                $ans += min($rowMax[$r], $colMax[$c]) - $grid[$r][$c];
            }
        }
        return $ans;
    }
}
""")

add("0808_soup_servings", r"""<?php
// LeetCode 0808 - Soup Servings
// https://leetcode.com/problems/soup-servings/

class Solution {
    /**
     * @param Integer $n
     * @return Float
     */
    function soupServings($n) {
        if ($n >= 4800) return 1.0;
        $units = intdiv($n + 24, 25);
        $memo = [];
        $dp = function($a, $b) use (&$dp, &$memo) {
            if ($a <= 0 && $b <= 0) return 0.5;
            if ($a <= 0) return 1.0;
            if ($b <= 0) return 0.0;
            $key = ($a << 16) | $b;
            if (isset($memo[$key])) return $memo[$key];
            $val = 0.25 * ($dp($a - 4, $b) + $dp($a - 3, $b - 1) + $dp($a - 2, $b - 2) + $dp($a - 1, $b - 3));
            $memo[$key] = $val;
            return $val;
        };
        return $dp($units, $units);
    }
}
""")

add("0809_expressive_words", r"""<?php
// LeetCode 0809 - Expressive Words
// https://leetcode.com/problems/expressive-words/

class Solution {
    /**
     * @param String $s
     * @param String[] $words
     * @return Integer
     */
    function expressiveWords($s, $words) {
        $groups = function($text) {
            $result = [];
            $i = 0;
            $n = strlen($text);
            while ($i < $n) {
                $j = $i;
                while ($j < $n && $text[$j] === $text[$i]) $j++;
                $result[] = [ord($text[$i]), $j - $i];
                $i = $j;
            }
            return $result;
        };
        $target = $groups($s);
        $ans = 0;
        foreach ($words as $word) {
            $source = $groups($word);
            if (count($source) !== count($target)) continue;
            $ok = true;
            $len = count($source);
            for ($i = 0; $i < $len; $i++) {
                if ($source[$i][0] !== $target[$i][0]) { $ok = false; break; }
                $c1 = $source[$i][1];
                $c2 = $target[$i][1];
                if ($c1 > $c2 || ($c1 !== $c2 && $c2 < 3)) { $ok = false; break; }
            }
            if ($ok) $ans++;
        }
        return $ans;
    }
}
""")

add("0810_chalkboard_xor_game", r"""<?php
// LeetCode 0810 - Chalkboard XOR Game
// https://leetcode.com/problems/chalkboard-xor-game/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Boolean
     */
    function xorGame($nums) {
        $x = 0;
        foreach ($nums as $num) $x ^= $num;
        return $x === 0 || count($nums) % 2 === 0;
    }
}
""")

add("0811_subdomain_visit_count", r"""<?php
// LeetCode 0811 - Subdomain Visit Count
// https://leetcode.com/problems/subdomain-visit-count/

class Solution {
    /**
     * @param String[] $cpdomains
     * @return String[]
     */
    function subdomainVisits($cpdomains) {
        $counts = [];
        foreach ($cpdomains as $item) {
            $space = strpos($item, ' ');
            $count = intval(substr($item, 0, $space));
            $domain = substr($item, $space + 1);
            while (true) {
                $counts[$domain] = ($counts[$domain] ?? 0) + $count;
                $dot = strpos($domain, '.');
                if ($dot === false) break;
                $domain = substr($domain, $dot + 1);
            }
        }
        $ans = [];
        foreach ($counts as $key => $value) $ans[] = $value . " " . $key;
        return $ans;
    }
}
""")

add("0812_largest_triangle_area", r"""<?php
// LeetCode 0812 - Largest Triangle Area
// https://leetcode.com/problems/largest-triangle-area/

class Solution {
    /**
     * @param Integer[][] $points
     * @return Float
     */
    function largestTriangleArea($points) {
        $best = 0.0;
        $n = count($points);
        for ($i = 0; $i < $n; $i++) {
            $x1 = $points[$i][0];
            $y1 = $points[$i][1];
            for ($j = $i + 1; $j < $n; $j++) {
                $x2 = $points[$j][0];
                $y2 = $points[$j][1];
                for ($k = $j + 1; $k < $n; $k++) {
                    $x3 = $points[$k][0];
                    $y3 = $points[$k][1];
                    $area = abs($x1 * ($y2 - $y3) + $x2 * ($y3 - $y1) + $x3 * ($y1 - $y2)) / 2.0;
                    $best = max($best, $area);
                }
            }
        }
        return $best;
    }
}
""")

add("0813_largest_sum_of_averages", r"""<?php
// LeetCode 0813 - Largest Sum of Averages
// https://leetcode.com/problems/largest-sum-of-averages/

class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Float
     */
    function largestSumOfAverages($nums, $k) {
        $n = count($nums);
        $prefix = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; $i++) $prefix[$i + 1] = $prefix[$i] + $nums[$i];
        $dp = array_fill(0, $n, 0.0);
        for ($i = 0; $i < $n; $i++) $dp[$i] = ($prefix[$i + 1] - $prefix[0]) / ($i + 1);
        for ($groups = 2; $groups <= $k; $groups++) {
            $nxt = array_fill(0, $n, 0.0);
            for ($i = $groups - 1; $i < $n; $i++) {
                $best = 0.0;
                for ($j = $groups - 2; $j < $i; $j++) {
                    $best = max($best, $dp[$j] + ($prefix[$i + 1] - $prefix[$j + 1]) / ($i - $j));
                }
                $nxt[$i] = $best;
            }
            $dp = $nxt;
        }
        return $dp[$n - 1];
    }
}
""")

add("0814_binary_tree_pruning", r"""<?php
// LeetCode 0814 - Binary Tree Pruning
// https://leetcode.com/problems/binary-tree-pruning/

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
    function pruneTree($root) {
        if ($root === null) return null;
        $root->left = $this->pruneTree($root->left);
        $root->right = $this->pruneTree($root->right);
        if ($root->val === 0 && $root->left === null && $root->right === null) return null;
        return $root;
    }
}
""")

add("0815_bus_routes", r"""<?php
// LeetCode 0815 - Bus Routes
// https://leetcode.com/problems/bus-routes/

class Solution {
    /**
     * @param Integer[][] $routes
     * @param Integer $source
     * @param Integer $target
     * @return Integer
     */
    function numBusesToDestination($routes, $source, $target) {
        if ($source === $target) return 0;
        $stopToBuses = [];
        $rn = count($routes);
        for ($bus = 0; $bus < $rn; $bus++) {
            foreach ($routes[$bus] as $stop) {
                if (!isset($stopToBuses[$stop])) $stopToBuses[$stop] = [];
                $stopToBuses[$stop][] = $bus;
            }
        }
        $queue = [[$source, 0]];
        $seenStops = [$source => true];
        $seenBuses = [];
        $qi = 0;
        while ($qi < count($queue)) {
            $stop = $queue[$qi][0];
            $busesTaken = $queue[$qi][1];
            $qi++;
            foreach ($stopToBuses[$stop] ?? [] as $bus) {
                if (isset($seenBuses[$bus])) continue;
                $seenBuses[$bus] = true;
                foreach ($routes[$bus] as $nxt) {
                    if ($nxt === $target) return $busesTaken + 1;
                    if (!isset($seenStops[$nxt])) {
                        $seenStops[$nxt] = true;
                        $queue[] = [$nxt, $busesTaken + 1];
                    }
                }
            }
        }
        return -1;
    }
}
""")

add("0816_ambiguous_coordinates", r"""<?php
// LeetCode 0816 - Ambiguous Coordinates
// https://leetcode.com/problems/ambiguous-coordinates/

class Solution {
    /**
     * @param String $s
     * @return String[]
     */
    function ambiguousCoordinates($s) {
        $digits = substr($s, 1, strlen($s) - 2);
        $candidates = function($frag) {
            $options = [];
            $len = strlen($frag);
            if ($len === 0 || ($len > 1 && $frag[0] === '0' && $frag[$len - 1] === '0')) return $options;
            if ($frag[0] === '0' && $len > 1) {
                if ($frag[$len - 1] !== '0') $options[] = "0." . substr($frag, 1);
                return $options;
            }
            $options[] = $frag;
            if ($frag[$len - 1] === '0') return $options;
            for ($i = 1; $i < $len; $i++) {
                $options[] = substr($frag, 0, $i) . "." . substr($frag, $i);
            }
            return $options;
        };
        $answer = [];
        $n = strlen($digits);
        for ($i = 1; $i < $n; $i++) {
            foreach ($candidates(substr($digits, 0, $i)) as $left) {
                foreach ($candidates(substr($digits, $i)) as $right) {
                    $answer[] = "(" . $left . ", " . $right . ")";
                }
            }
        }
        return $answer;
    }
}
""")

add("0817_linked_list_components", r"""<?php
// LeetCode 0817 - Linked List Components
// https://leetcode.com/problems/linked-list-components/

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
     * @param Integer[] $nums
     * @return Integer
     */
    function numComponents($head, $nums) {
        $present = [];
        foreach ($nums as $x) $present[$x] = true;
        $count = 0;
        $connected = false;
        while ($head !== null) {
            if (isset($present[$head->val])) {
                if (!$connected) {
                    $count++;
                    $connected = true;
                }
            } else {
                $connected = false;
            }
            $head = $head->next;
        }
        return $count;
    }
}
""")

add("0818_race_car", r"""<?php
// LeetCode 0818 - Race Car
// https://leetcode.com/problems/race-car/

class Solution {
    /**
     * @param Integer $target
     * @return Integer
     */
    function racecar($target) {
        $key = function($pos, $speed) {
            return ($pos * 1048576) ^ ($speed & 0xfffff);
        };
        $queue = [[0, 1, 0]];
        $seen = [$key(0, 1) => true];
        $qi = 0;
        while ($qi < count($queue)) {
            $pos = $queue[$qi][0];
            $speed = $queue[$qi][1];
            $steps = $queue[$qi][2];
            $qi++;
            if ($pos === $target) return $steps;
            $nxtPos = $pos + $speed;
            $nxtSpeed = $speed * 2;
            $k1 = $key($nxtPos, $nxtSpeed);
            if (!isset($seen[$k1]) && abs($nxtPos) < $target * 2) {
                $seen[$k1] = true;
                $queue[] = [$nxtPos, $nxtSpeed, $steps + 1];
            }
            $revSpeed = $speed > 0 ? -1 : 1;
            $k2 = $key($pos, $revSpeed);
            if (!isset($seen[$k2])) {
                $seen[$k2] = true;
                $queue[] = [$pos, $revSpeed, $steps + 1];
            }
        }
        return -1;
    }
}
""")

add("0819_most_common_word", r"""<?php
// LeetCode 0819 - Most Common Word
// https://leetcode.com/problems/most-common-word/

class Solution {
    /**
     * @param String $paragraph
     * @param String[] $banned
     * @return String
     */
    function mostCommonWord($paragraph, $banned) {
        $bannedSet = [];
        foreach ($banned as $b) $bannedSet[$b] = true;
        $counts = [];
        $word = "";
        $best = "";
        $bestCount = 0;
        $n = strlen($paragraph);
        for ($i = 0; $i <= $n; $i++) {
            $ch = $i < $n ? $paragraph[$i] : ' ';
            if (ctype_alpha($ch)) {
                $word .= strtolower($ch);
            } elseif (strlen($word) > 0) {
                $w = $word;
                $word = "";
                if (!isset($bannedSet[$w])) {
                    $c = ($counts[$w] ?? 0) + 1;
                    $counts[$w] = $c;
                    if ($c > $bestCount) {
                        $bestCount = $c;
                        $best = $w;
                    }
                }
            }
        }
        return $best;
    }
}
""")

add("0820_short_encoding_of_words", r"""<?php
// LeetCode 0820 - Short Encoding of Words
// https://leetcode.com/problems/short-encoding-of-words/

class Solution {
    /**
     * @param String[] $words
     * @return Integer
     */
    function minimumLengthEncoding($words) {
        $good = [];
        foreach ($words as $word) $good[$word] = true;
        foreach ($words as $word) {
            $len = strlen($word);
            for ($i = 1; $i < $len; $i++) unset($good[substr($word, $i)]);
        }
        $ans = 0;
        foreach ($good as $word => $_) $ans += strlen($word) + 1;
        return $ans;
    }
}
""")

add("0821_shortest_distance_to_a_character", r"""<?php
// LeetCode 0821 - Shortest Distance to a Character
// https://leetcode.com/problems/shortest-distance-to-a-character/

class Solution {
    /**
     * @param String $s
     * @param String $c
     * @return Integer[]
     */
    function shortestToChar($s, $c) {
        $n = strlen($s);
        $ans = array_fill(0, $n, 0);
        $prev = -$n;
        for ($i = 0; $i < $n; $i++) {
            if ($s[$i] === $c) $prev = $i;
            $ans[$i] = $i - $prev;
        }
        $prev = 2 * $n;
        for ($i = $n - 1; $i >= 0; $i--) {
            if ($s[$i] === $c) $prev = $i;
            $ans[$i] = min($ans[$i], $prev - $i);
        }
        return $ans;
    }
}
""")

add("0822_card_flipping_game", r"""<?php
// LeetCode 0822 - Card Flipping Game
// https://leetcode.com/problems/card-flipping-game/

class Solution {
    /**
     * @param Integer[] $fronts
     * @param Integer[] $backs
     * @return Integer
     */
    function flipgame($fronts, $backs) {
        $same = [];
        $n = count($fronts);
        for ($i = 0; $i < $n; $i++) {
            if ($fronts[$i] === $backs[$i]) $same[$fronts[$i]] = true;
        }
        $best = PHP_INT_MAX;
        foreach ($fronts as $x) if (!isset($same[$x])) $best = min($best, $x);
        foreach ($backs as $x) if (!isset($same[$x])) $best = min($best, $x);
        return $best === PHP_INT_MAX ? 0 : $best;
    }
}
""")

add("0823_binary_trees_with_factors", r"""<?php
// LeetCode 0823 - Binary Trees With Factors
// https://leetcode.com/problems/binary-trees-with-factors/

class Solution {
    /**
     * @param Integer[] $arr
     * @return Integer
     */
    function numFactoredBinaryTrees($arr) {
        $MOD = 1000000007;
        sort($arr);
        $index = [];
        $n = count($arr);
        for ($i = 0; $i < $n; $i++) $index[$arr[$i]] = $i;
        $dp = array_fill(0, $n, 1);
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            for ($j = 0; $j < $i; $j++) {
                if ($arr[$i] % $arr[$j] === 0) {
                    $right = intdiv($arr[$i], $arr[$j]);
                    if (isset($index[$right])) {
                        $dp[$i] = ($dp[$i] + $dp[$j] * $dp[$index[$right]]) % $MOD;
                    }
                }
            }
            $ans = ($ans + $dp[$i]) % $MOD;
        }
        return $ans;
    }
}
""")

add("0824_goat_latin", r"""<?php
// LeetCode 0824 - Goat Latin
// https://leetcode.com/problems/goat-latin/

class Solution {
    /**
     * @param String $sentence
     * @return String
     */
    function toGoatLatin($sentence) {
        $vowels = ['a'=>true,'e'=>true,'i'=>true,'o'=>true,'u'=>true,'A'=>true,'E'=>true,'I'=>true,'O'=>true,'U'=>true];
        $words = explode(' ', $sentence);
        $result = [];
        $n = count($words);
        for ($i = 0; $i < $n; $i++) {
            $w = $words[$i];
            if (isset($vowels[$w[0]])) $w = $w . "ma";
            else $w = substr($w, 1) . $w[0] . "ma";
            $w .= str_repeat("a", $i + 1);
            $result[] = $w;
        }
        return implode(' ', $result);
    }
}
""")

add("0825_friends_of_appropriate_ages", r"""<?php
// LeetCode 0825 - Friends Of Appropriate Ages
// https://leetcode.com/problems/friends-of-appropriate-ages/

class Solution {
    /**
     * @param Integer[] $ages
     * @return Integer
     */
    function numFriendRequests($ages) {
        $count = array_fill(0, 121, 0);
        foreach ($ages as $age) $count[$age]++;
        $ans = 0;
        for ($a = 1; $a <= 120; $a++) {
            if (!$count[$a]) continue;
            for ($b = 1; $b <= 120; $b++) {
                if (!$count[$b]) continue;
                if ($b <= 0.5 * $a + 7) continue;
                if ($b > $a) continue;
                if ($b > 100 && $a < 100) continue;
                $ans += $count[$a] * $count[$b];
                if ($a === $b) $ans -= $count[$a];
            }
        }
        return $ans;
    }
}
""")

add("0826_most_profit_assigning_work", r"""<?php
// LeetCode 0826 - Most Profit Assigning Work
// https://leetcode.com/problems/most-profit-assigning-work/

class Solution {
    /**
     * @param Integer[] $difficulty
     * @param Integer[] $profit
     * @param Integer[] $worker
     * @return Integer
     */
    function maxProfitAssignment($difficulty, $profit, $worker) {
        $jobs = [];
        $n = count($difficulty);
        for ($i = 0; $i < $n; $i++) $jobs[] = [$difficulty[$i], $profit[$i]];
        usort($jobs, function($a, $b) { return $a[0] <=> $b[0]; });
        sort($worker);
        $ans = 0;
        $best = 0;
        $i = 0;
        foreach ($worker as $ability) {
            while ($i < count($jobs) && $jobs[$i][0] <= $ability) {
                $best = max($best, $jobs[$i][1]);
                $i++;
            }
            $ans += $best;
        }
        return $ans;
    }
}
""")

add("0827_making_a_large_island", r"""<?php
// LeetCode 0827 - Making A Large Island
// https://leetcode.com/problems/making-a-large-island/

class Solution {
    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function largestIsland($grid) {
        $n = count($grid);
        $sizes = [0 => 0];
        $islandId = 2;
        $dfs = function($r, $c, $iid) use (&$dfs, &$grid, $n) {
            if ($r < 0 || $r >= $n || $c < 0 || $c >= $n || $grid[$r][$c] !== 1) return 0;
            $grid[$r][$c] = $iid;
            return 1 + $dfs($r + 1, $c, $iid) + $dfs($r - 1, $c, $iid) + $dfs($r, $c + 1, $iid) + $dfs($r, $c - 1, $iid);
        };
        for ($i = 0; $i < $n; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if ($grid[$i][$j] === 1) {
                    $sizes[$islandId] = $dfs($i, $j, $islandId);
                    $islandId++;
                }
            }
        }
        $ans = 0;
        foreach ($sizes as $v) $ans = max($ans, $v);
        $dr = [1, -1, 0, 0];
        $dc = [0, 0, 1, -1];
        for ($i = 0; $i < $n; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if ($grid[$i][$j] !== 0) continue;
                $seen = [];
                $total = 1;
                for ($k = 0; $k < 4; $k++) {
                    $ni = $i + $dr[$k];
                    $nj = $j + $dc[$k];
                    if ($ni >= 0 && $ni < $n && $nj >= 0 && $nj < $n) {
                        $iid = $grid[$ni][$nj];
                        if ($iid > 1 && !isset($seen[$iid])) {
                            $seen[$iid] = true;
                            $total += $sizes[$iid];
                        }
                    }
                }
                $ans = max($ans, $total);
            }
        }
        return $ans;
    }
}
""")

add("0828_count_unique_characters_of_all_substrings_of_a_given_string", r"""<?php
// LeetCode 0828 - Count Unique Characters of All Substrings of a Given String
// https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/

class Solution {
    /**
     * @param String $s
     * @return Integer
     */
    function uniqueLetterString($s) {
        $n = strlen($s);
        $last = [];
        for ($i = 0; $i < $n; $i++) {
            $ch = $s[$i];
            if (!isset($last[$ch])) $last[$ch] = [-1];
        }
        for ($i = 0; $i < $n; $i++) $last[$s[$i]][] = $i;
        foreach ($last as $ch => $_) $last[$ch][] = $n;
        $ans = 0;
        foreach ($last as $indices) {
            $len = count($indices);
            for ($k = 1; $k + 1 < $len; $k++) {
                $ans += ($indices[$k] - $indices[$k - 1]) * ($indices[$k + 1] - $indices[$k]);
            }
        }
        return $ans;
    }
}
""")

add("0829_consecutive_numbers_sum", r"""<?php
// LeetCode 0829 - Consecutive Numbers Sum
// https://leetcode.com/problems/consecutive-numbers-sum/

class Solution {
    /**
     * @param Integer $n
     * @return Integer
     */
    function consecutiveNumbersSum($n) {
        $ans = 0;
        for ($k = 1; $k * ($k - 1) / 2 < $n; $k++) {
            if (($n - $k * ($k - 1) / 2) % $k === 0) $ans++;
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
        print(f"wrote {folder}")
    print(f"wrote={ported}")


if __name__ == "__main__":
    main()

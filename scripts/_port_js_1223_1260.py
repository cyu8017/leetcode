#!/usr/bin/env python3
"""Port JS solutions for LeetCode stubs 1223-1260."""
from __future__ import annotations

import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SOLUTIONS: dict[str, str] = {
    "1223_dice_roll_simulation": r'''// LeetCode 1223 - Dice Roll Simulation
// https://leetcode.com/problems/dice-roll-simulation/

/**
 * @param {number} n
 * @param {number[]} rollMax
 * @return {number}
 */
var dieSimulator = function(n, rollMax) {
    const mod = 1000000007;
    let dp = rollMax.map((limit) => Array(limit + 1).fill(0));
    for (let j = 0; j < 6; j++) dp[j][1] = 1;
    for (let t = 1; t < n; t++) {
        const totals = dp.map((row) => row.reduce((s, v) => (s + v) % mod, 0));
        const nxt = rollMax.map((limit) => Array(limit + 1).fill(0));
        for (let j = 0; j < 6; j++) {
            nxt[j][1] = (totals.reduce((s, v) => (s + v) % mod, 0) - totals[j] + mod) % mod;
            for (let run = 2; run < dp[j].length; run++) {
                nxt[j][run] = dp[j][run - 1];
            }
        }
        dp = nxt;
    }
    return dp.reduce((s, row) => (s + row.reduce((a, b) => (a + b) % mod, 0)) % mod, 0);
};
''',
    "1224_maximum_equal_frequency": r'''// LeetCode 1224 - Maximum Equal Frequency
// https://leetcode.com/problems/maximum-equal-frequency/

/**
 * @param {number[]} nums
 * @return {number}
 */
var maxEqualFreq = function(nums) {
    const count = new Map();
    const frequencies = new Map();
    let answer = 0;
    for (let i = 0; i < nums.length; i++) {
        const x = nums[i];
        const old = count.get(x) || 0;
        if (old) frequencies.set(old, (frequencies.get(old) || 0) - 1);
        count.set(x, old + 1);
        frequencies.set(old + 1, (frequencies.get(old + 1) || 0) + 1);
        const high = Math.max(...frequencies.keys());
        if (
            high === 1 ||
            (frequencies.get(high) || 0) * high + 1 === i + 1 ||
            ((frequencies.get(high) || 0) === 1 && (frequencies.get(high - 1) || 0) * (high - 1) + high === i + 1)
        ) {
            answer = i + 1;
        }
    }
    return answer;
};
''',
    "1226_the_dining_philosophers": r'''// LeetCode 1226 - The Dining Philosophers
// https://leetcode.com/problems/the-dining-philosophers/

var DiningPhilosophers = function() {
    this.locks = Array.from({ length: 5 }, () => Promise.resolve());
};

/**
 * @param {number} philosopher
 * @param {function} pickLeftFork
 * @param {function} pickRightFork
 * @param {function} eat
 * @param {function} putLeftFork
 * @param {function} putRightFork
 * @return {Promise<void>}
 */
DiningPhilosophers.prototype.wantsToEat = async function(
    philosopher, pickLeftFork, pickRightFork, eat, putLeftFork, putRightFork
) {
    const left = philosopher;
    const right = (philosopher + 1) % 5;
    const [first, second] = philosopher % 2 === 0 ? [left, right] : [right, left];
    await (this.locks[first] = this.locks[first].then(pickLeftFork));
    await (this.locks[second] = this.locks[second].then(pickRightFork));
    eat();
    putLeftFork();
    putRightFork();
    this.locks[first] = Promise.resolve();
    this.locks[second] = Promise.resolve();
};
''',
    "1227_airplane_seat_assignment_probability": r'''// LeetCode 1227 - Airplane Seat Assignment Probability
// https://leetcode.com/problems/airplane-seat-assignment-probability/

/**
 * @param {number} n
 * @return {number}
 */
var nthPersonGetsNthSeat = function(n) {
    return n === 1 ? 1.0 : 0.5;
};
''',
    "1228_missing_number_in_arithmetic_progression": r'''// LeetCode 1228 - Missing Number In Arithmetic Progression
// https://leetcode.com/problems/missing-number-in-arithmetic-progression/

/**
 * @param {number[]} arr
 * @return {number}
 */
var missingNumber = function(arr) {
    const diff = (arr[arr.length - 1] - arr[0]) / arr.length;
    for (let i = 1; i < arr.length; i++) {
        const expected = arr[0] + i * diff;
        if (arr[i] !== expected) return expected;
    }
    return arr[0];
};
''',
    "1229_meeting_scheduler": r'''// LeetCode 1229 - Meeting Scheduler
// https://leetcode.com/problems/meeting-scheduler/

/**
 * @param {number[][]} slots1
 * @param {number[][]} slots2
 * @param {number} duration
 * @return {number[]}
 */
var minAvailableDuration = function(slots1, slots2, duration) {
    slots1.sort((a, b) => a[0] - b[0]);
    slots2.sort((a, b) => a[0] - b[0]);
    let i = 0, j = 0;
    while (i < slots1.length && j < slots2.length) {
        const start = Math.max(slots1[i][0], slots2[j][0]);
        const end = Math.min(slots1[i][1], slots2[j][1]);
        if (end - start >= duration) return [start, start + duration];
        if (slots1[i][1] < slots2[j][1]) i++;
        else j++;
    }
    return [];
};
''',
    "1230_toss_strange_coins": r'''// LeetCode 1230 - Toss Strange Coins
// https://leetcode.com/problems/toss-strange-coins/

/**
 * @param {number[]} prob
 * @param {number} target
 * @return {number}
 */
var probabilityOfHeads = function(prob, target) {
    const dp = Array(target + 1).fill(0);
    dp[0] = 1;
    for (const p of prob) {
        for (let heads = target; heads >= 0; heads--) {
            dp[heads] = dp[heads] * (1 - p) + (heads ? dp[heads - 1] * p : 0);
        }
    }
    return dp[target];
};
''',
    "1231_divide_chocolate": r'''// LeetCode 1231 - Divide Chocolate
// https://leetcode.com/problems/divide-chocolate/

/**
 * @param {number[]} sweetness
 * @param {number} k
 * @return {number}
 */
var maximizeSweetness = function(sweetness, k) {
    let lo = 1, hi = Math.floor(sweetness.reduce((s, v) => s + v, 0) / (k + 1));
    while (lo <= hi) {
        const mid = (lo + hi) >> 1;
        let pieces = 0, current = 0;
        for (const value of sweetness) {
            current += value;
            if (current >= mid) {
                pieces++;
                current = 0;
            }
        }
        if (pieces >= k + 1) lo = mid + 1;
        else hi = mid - 1;
    }
    return hi;
};
''',
    "1232_check_if_it_is_a_straight_line": r'''// LeetCode 1232 - Check If It Is A Straight Line
// https://leetcode.com/problems/check-if-it-is-a-straight-line/

/**
 * @param {number[][]} coordinates
 * @return {boolean}
 */
var checkStraightLine = function(coordinates) {
    const [x0, y0] = coordinates[0];
    const dx = coordinates[1][0] - x0;
    const dy = coordinates[1][1] - y0;
    for (let i = 2; i < coordinates.length; i++) {
        const [x, y] = coordinates[i];
        if ((x - x0) * dy !== (y - y0) * dx) return false;
    }
    return true;
};
''',
    "1233_remove_sub_folders_from_the_filesystem": r'''// LeetCode 1233 - Remove Sub-Folders From The Filesystem
// https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/

/**
 * @param {string[]} folder
 * @return {string[]}
 */
var removeSubfolders = function(folder) {
    const answer = [];
    for (const path of [...folder].sort()) {
        if (!answer.length || !path.startsWith(answer[answer.length - 1] + "/")) {
            answer.push(path);
        }
    }
    return answer;
};
''',
    "1234_replace_the_substring_for_balanced_string": r'''// LeetCode 1234 - Replace the Substring for Balanced String
// https://leetcode.com/problems/replace-the-substring-for-balanced-string/

/**
 * @param {string} s
 * @return {number}
 */
var balancedString = function(s) {
    const count = { Q: 0, W: 0, E: 0, R: 0 };
    for (const ch of s) count[ch]++;
    const limit = s.length / 4;
    let left = 0, answer = s.length;
    for (let right = 0; right < s.length; right++) {
        count[s[right]]--;
        while (left < s.length && count.Q <= limit && count.W <= limit && count.E <= limit && count.R <= limit) {
            answer = Math.min(answer, right - left + 1);
            count[s[left]]++;
            left++;
        }
    }
    return answer;
};
''',
    "1235_maximum_profit_in_job_scheduling": r'''// LeetCode 1235 - Maximum Profit in Job Scheduling
// https://leetcode.com/problems/maximum-profit-in-job-scheduling/

/**
 * @param {number[]} startTime
 * @param {number[]} endTime
 * @param {number[]} profit
 * @return {number}
 */
var jobScheduling = function(startTime, endTime, profit) {
    const jobs = endTime.map((end, i) => [end, startTime[i], profit[i]]).sort((a, b) => a[0] - b[0]);
    const ends = [0];
    const dp = [0];
    for (const [end, start, gain] of jobs) {
        let lo = 0, hi = ends.length - 1, idx = 0;
        while (lo <= hi) {
            const mid = (lo + hi) >> 1;
            if (ends[mid] <= start) {
                idx = mid;
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        ends.push(end);
        dp.push(Math.max(dp[dp.length - 1], dp[idx] + gain));
    }
    return dp[dp.length - 1];
};
''',
    "1236_web_crawler": r'''// LeetCode 1236 - Web Crawler
// https://leetcode.com/problems/web-crawler/

/**
 * @param {string} startUrl
 * @param {object} htmlParser
 * @return {string[]}
 */
var crawl = function(startUrl, htmlParser) {
    const hostOf = (url) => {
        const u = url.replace(/^https?:\/\//, "");
        const slash = u.indexOf("/");
        return slash >= 0 ? u.slice(0, slash) : u;
    };
    const host = hostOf(startUrl);
    const seen = new Set([startUrl]);
    const stack = [startUrl];
    while (stack.length) {
        const cur = stack.pop();
        for (const url of htmlParser.getUrls(cur)) {
            if (hostOf(url) === host && !seen.has(url)) {
                seen.add(url);
                stack.push(url);
            }
        }
    }
    return [...seen].sort();
};
''',
    "1237_find_positive_integer_solution_for_a_given_equation": r'''// LeetCode 1237 - Find Positive Integer Solution for a Given Equation
// https://leetcode.com/problems/find-positive-integer-solution-for-a-given-equation/

/**
 * @param {function} customfunction
 * @param {number} z
 * @return {number[][]}
 */
var findSolution = function(customfunction, z) {
    const answer = [];
    let x = 1, y = 1000;
    while (x <= 1000 && y >= 1) {
        const value = customfunction.f(x, y);
        if (value === z) {
            answer.push([x, y]);
            x++;
            y--;
        } else if (value < z) {
            x++;
        } else {
            y--;
        }
    }
    return answer;
};
''',
    "1238_circular_permutation_in_binary_representation": r'''// LeetCode 1238 - Circular Permutation in Binary Representation
// https://leetcode.com/problems/circular-permutation-in-binary-representation/

/**
 * @param {number} n
 * @param {number} start
 * @return {number[]}
 */
var circularPermutation = function(n, start) {
    const limit = 1 << n;
    const answer = [];
    for (let i = 0; i < limit; i++) {
        answer.push(start ^ i ^ (i >> 1));
    }
    return answer;
};
''',
    "1239_maximum_length_of_a_concatenated_string_with_unique_characters": r'''// LeetCode 1239 - Maximum Length of a Concatenated String with Unique Characters
// https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/

/**
 * @param {string[]} arr
 * @return {number}
 */
var maxLength = function(arr) {
    let masks = [[0, 0]];
    for (const word of arr) {
        let mask = 0;
        for (const ch of word) mask |= 1 << (ch.charCodeAt(0) - 97);
        if (popcount(mask) !== word.length) continue;
        masks = masks.concat(
            masks
                .filter(([used]) => !(used & mask))
                .map(([used, length]) => [used | mask, length + word.length])
        );
    }
    return Math.max(...masks.map(([, length]) => length));
};

function popcount(x) {
    let count = 0;
    while (x) {
        count += x & 1;
        x >>= 1;
    }
    return count;
}
''',
    "1240_tiling_a_rectangle_with_the_fewest_squares": r'''// LeetCode 1240 - Tiling a Rectangle with the Fewest Squares
// https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares/

/**
 * @param {number} n
 * @param {number} m
 * @return {number}
 */
var tilingRectangle = function(n, m) {
    if (n > m) [n, m] = [m, n];
    const heights = Array(m).fill(0);
    let best = n * m;
    function search(used) {
        if (used >= best) return;
        const low = Math.min(...heights);
        if (low === n) {
            best = used;
            return;
        }
        const left = heights.indexOf(low);
        let right = left;
        while (right < m && heights[right] === low) right++;
        const maxSize = Math.min(n - low, right - left);
        for (let size = maxSize; size >= 1; size--) {
            for (let i = left; i < left + size; i++) heights[i] = low + size;
            search(used + 1);
            for (let i = left; i < left + size; i++) heights[i] = low;
        }
    }
    search(0);
    return best;
};
''',
    "1242_web_crawler_multithreaded": r'''// LeetCode 1242 - Web Crawler Multithreaded
// https://leetcode.com/problems/web-crawler-multithreaded/

/**
 * @param {string} startUrl
 * @param {object} htmlParser
 * @return {string[]}
 */
var crawl = function(startUrl, htmlParser) {
    const hostOf = (url) => {
        const u = url.replace(/^https?:\/\//, "");
        const slash = u.indexOf("/");
        return slash >= 0 ? u.slice(0, slash) : u;
    };
    const host = hostOf(startUrl);
    const seen = new Set([startUrl]);
    let frontier = [startUrl];
    while (frontier.length) {
        const next = [];
        for (const cur of frontier) {
            for (const url of htmlParser.getUrls(cur)) {
                if (hostOf(url) === host && !seen.has(url)) {
                    seen.add(url);
                    next.push(url);
                }
            }
        }
        frontier = next;
    }
    return [...seen].sort();
};
''',
    "1243_array_transformation": r'''// LeetCode 1243 - Array Transformation
// https://leetcode.com/problems/array-transformation/

/**
 * @param {number[]} arr
 * @return {number[]}
 */
var transformArray = function(arr) {
    while (true) {
        const nxt = arr.slice();
        for (let i = 1; i < arr.length - 1; i++) {
            if (arr[i] < arr[i - 1] && arr[i] < arr[i + 1]) nxt[i]++;
            else if (arr[i] > arr[i - 1] && arr[i] > arr[i + 1]) nxt[i]--;
        }
        if (nxt.every((v, i) => v === arr[i])) return arr;
        arr = nxt;
    }
};
''',
    "1244_design_a_leaderboard": r'''// LeetCode 1244 - Design A Leaderboard
// https://leetcode.com/problems/design-a-leaderboard/

var Leaderboard = function() {
    this.scores = new Map();
};

/** 
 * @param {number} playerId
 * @param {number} score
 * @return {void}
 */
Leaderboard.prototype.addScore = function(playerId, score) {
    this.scores.set(playerId, (this.scores.get(playerId) || 0) + score);
};

/** 
 * @param {number} K
 * @return {number}
 */
Leaderboard.prototype.top = function(K) {
    return [...this.scores.values()].sort((a, b) => b - a).slice(0, K).reduce((s, v) => s + v, 0);
};

/** 
 * @param {number} playerId
 * @return {void}
 */
Leaderboard.prototype.reset = function(playerId) {
    this.scores.delete(playerId);
};
''',
    "1245_tree_diameter": r'''// LeetCode 1245 - Tree Diameter
// https://leetcode.com/problems/tree-diameter/

/**
 * @param {number[][]} edges
 * @return {number}
 */
var treeDiameter = function(edges) {
    if (!edges.length) return 0;
    const graph = new Map();
    for (const [a, b] of edges) {
        if (!graph.has(a)) graph.set(a, []);
        if (!graph.has(b)) graph.set(b, []);
        graph.get(a).push(b);
        graph.get(b).push(a);
    }
    const farthest = (start) => {
        const queue = [[start, 0]];
        const seen = new Set([start]);
        let last = [start, 0];
        while (queue.length) {
            last = queue.shift();
            for (const v of graph.get(last[0]) || []) {
                if (!seen.has(v)) {
                    seen.add(v);
                    queue.push([v, last[1] + 1]);
                }
            }
        }
        return last;
    };
    const endpoint = farthest(edges[0][0])[0];
    return farthest(endpoint)[1];
};
''',
    "1246_palindrome_removal": r'''// LeetCode 1246 - Palindrome Removal
// https://leetcode.com/problems/palindrome-removal/

/**
 * @param {number[]} arr
 * @return {number}
 */
var minimumMoves = function(arr) {
    const n = arr.length;
    const dp = Array.from({ length: n }, () => Array(n).fill(0));
    for (let i = 0; i < n; i++) dp[i][i] = 1;
    for (let length = 2; length <= n; length++) {
        for (let i = 0; i <= n - length; i++) {
            const j = i + length - 1;
            dp[i][j] = 1 + dp[i + 1][j];
            if (arr[i] === arr[i + 1]) {
                dp[i][j] = Math.min(dp[i][j], 1 + (i + 2 <= j ? dp[i + 2][j] : 0));
            }
            for (let k = i + 2; k <= j; k++) {
                if (arr[i] === arr[k]) {
                    dp[i][j] = Math.min(
                        dp[i][j],
                        dp[i + 1][k - 1] + (k < j ? dp[k + 1][j] : 0)
                    );
                }
            }
        }
    }
    return dp[0][n - 1];
};
''',
    "1247_minimum_swaps_to_make_strings_equal": r'''// LeetCode 1247 - Minimum Swaps to Make Strings Equal
// https://leetcode.com/problems/minimum-swaps-to-make-strings-equal/

/**
 * @param {string} s1
 * @param {string} s2
 * @return {number}
 */
var minimumSwap = function(s1, s2) {
    let xy = 0, yx = 0;
    for (let i = 0; i < s1.length; i++) {
        if (s1[i] === "x" && s2[i] === "y") xy++;
        if (s1[i] === "y" && s2[i] === "x") yx++;
    }
    if ((xy + yx) % 2) return -1;
    return (xy >> 1) + (yx >> 1) + 2 * (xy % 2);
};
''',
    "1248_count_number_of_nice_subarrays": r'''// LeetCode 1248 - Count Number of Nice Subarrays
// https://leetcode.com/problems/count-number-of-nice-subarrays/

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var numberOfSubarrays = function(nums, k) {
    const frequency = new Map([[0, 1]]);
    let odd = 0, answer = 0;
    for (const x of nums) {
        odd += x & 1;
        answer += frequency.get(odd - k) || 0;
        frequency.set(odd, (frequency.get(odd) || 0) + 1);
    }
    return answer;
};
''',
    "1249_minimum_remove_to_make_valid_parentheses": r'''// LeetCode 1249 - Minimum Remove to Make Valid Parentheses
// https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

/**
 * @param {string} s
 * @return {string}
 */
var minRemoveToMakeValid = function(s) {
    const chars = s.split("");
    const opens = [];
    for (let i = 0; i < chars.length; i++) {
        if (chars[i] === "(") opens.push(i);
        else if (chars[i] === ")") {
            if (opens.length) opens.pop();
            else chars[i] = "";
        }
    }
    for (const i of opens) chars[i] = "";
    return chars.join("");
};
''',
    "1250_check_if_it_is_a_good_array": r'''// LeetCode 1250 - Check If It Is a Good Array
// https://leetcode.com/problems/check-if-it-is-a-good-array/

/**
 * @param {number[]} nums
 * @return {boolean}
 */
var isGoodArray = function(nums) {
    let g = nums[0];
    for (let i = 1; i < nums.length; i++) g = gcd(g, nums[i]);
    return g === 1;
};

function gcd(a, b) {
    while (b) [a, b] = [b, a % b];
    return a;
}
''',
    "1252_cells_with_odd_values_in_a_matrix": r'''// LeetCode 1252 - Cells with Odd Values in a Matrix
// https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/

/**
 * @param {number} m
 * @param {number} n
 * @param {number[][]} indices
 * @return {number}
 */
var oddCells = function(m, n, indices) {
    const rows = Array(m).fill(0);
    const cols = Array(n).fill(0);
    for (const [r, c] of indices) {
        rows[r] ^= 1;
        cols[c] ^= 1;
    }
    let answer = 0;
    for (let r = 0; r < m; r++) {
        for (let c = 0; c < n; c++) {
            answer += rows[r] ^ cols[c];
        }
    }
    return answer;
};
''',
    "1253_reconstruct_a_2_row_binary_matrix": r'''// LeetCode 1253 - Reconstruct a 2-Row Binary Matrix
// https://leetcode.com/problems/reconstruct-a-2-row-binary-matrix/

/**
 * @param {number} upper
 * @param {number} lower
 * @param {number[]} colsum
 * @return {number[][]}
 */
var reconstructMatrix = function(upper, lower, colsum) {
    const top = Array(colsum.length).fill(0);
    const bottom = Array(colsum.length).fill(0);
    for (let i = 0; i < colsum.length; i++) {
        if (colsum[i] === 2) {
            top[i] = bottom[i] = 1;
            upper--;
            lower--;
        }
    }
    if (upper < 0 || lower < 0) return [];
    for (let i = 0; i < colsum.length; i++) {
        if (colsum[i] === 1) {
            if (upper) {
                top[i] = 1;
                upper--;
            } else if (lower) {
                bottom[i] = 1;
                lower--;
            } else {
                return [];
            }
        }
    }
    return upper === 0 && lower === 0 ? [top, bottom] : [];
};
''',
    "1254_number_of_closed_islands": r'''// LeetCode 1254 - Number of Closed Islands
// https://leetcode.com/problems/number-of-closed-islands/

/**
 * @param {number[][]} grid
 * @return {number}
 */
var closedIsland = function(grid) {
    const m = grid.length, n = grid[0].length;
    const flood = (sr, sc) => {
        const stack = [[sr, sc]];
        grid[sr][sc] = 1;
        let closed = true;
        while (stack.length) {
            const [r, c] = stack.pop();
            if (r === 0 || r === m - 1 || c === 0 || c === n - 1) closed = false;
            for (const [dr, dc] of [[1, 0], [-1, 0], [0, 1], [0, -1]]) {
                const nr = r + dr, nc = c + dc;
                if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] === 0) {
                    grid[nr][nc] = 1;
                    stack.push([nr, nc]);
                }
            }
        }
        return closed;
    };
    let answer = 0;
    for (let r = 0; r < m; r++) {
        for (let c = 0; c < n; c++) {
            if (grid[r][c] === 0 && flood(r, c)) answer++;
        }
    }
    return answer;
};
''',
    "1255_maximum_score_words_formed_by_letters": r'''// LeetCode 1255 - Maximum Score Words Formed by Letters
// https://leetcode.com/problems/maximum-score-words-formed-by-letters/

/**
 * @param {string[]} words
 * @param {char[]} letters
 * @param {number[]} score
 * @return {number}
 */
var maxScoreWords = function(words, letters, score) {
    const available = new Map();
    for (const ch of letters) available.set(ch, (available.get(ch) || 0) + 1);
    const counts = words.map((word) => {
        const map = new Map();
        for (const ch of word) map.set(ch, (map.get(ch) || 0) + 1);
        return map;
    });
    const values = words.map((word) => {
        let total = 0;
        for (const ch of word) total += score[ch.charCodeAt(0) - 97];
        return total;
    });
    const fits = (need) => {
        for (const [ch, count] of need) {
            if ((available.get(ch) || 0) < count) return false;
        }
        return true;
    };
    const subtract = (need) => {
        for (const [ch, count] of need) available.set(ch, available.get(ch) - count);
    };
    const addBack = (need) => {
        for (const [ch, count] of need) available.set(ch, (available.get(ch) || 0) + count);
    };
    const dfs = (i) => {
        if (i === words.length) return 0;
        let best = dfs(i + 1);
        if (fits(counts[i])) {
            subtract(counts[i]);
            best = Math.max(best, values[i] + dfs(i + 1));
            addBack(counts[i]);
        }
        return best;
    };
    return dfs(0);
};
''',
    "1256_encode_number": r'''// LeetCode 1256 - Encode Number
// https://leetcode.com/problems/encode-number/

/**
 * @param {number} num
 * @return {string}
 */
var encode = function(num) {
    return (num + 1).toString(2).slice(1);
};
''',
    "1257_smallest_common_region": r'''// LeetCode 1257 - Smallest Common Region
// https://leetcode.com/problems/smallest-common-region/

/**
 * @param {string[][]} regions
 * @param {string} region1
 * @param {string} region2
 * @return {string}
 */
var findSmallestRegion = function(regions, region1, region2) {
    const parent = new Map();
    for (const group of regions) {
        for (let i = 1; i < group.length; i++) parent.set(group[i], group[0]);
    }
    const ancestors = new Set();
    while (region1) {
        ancestors.add(region1);
        region1 = parent.get(region1);
    }
    while (!ancestors.has(region2)) region2 = parent.get(region2);
    return region2;
};
''',
    "1258_synonymous_sentences": r'''// LeetCode 1258 - Synonymous Sentences
// https://leetcode.com/problems/synonymous-sentences/

/**
 * @param {string[][]} synonyms
 * @param {string} text
 * @return {string[]}
 */
var generateSentences = function(synonyms, text) {
    const parent = new Map();
    const find = (x) => {
        if (!parent.has(x)) parent.set(x, x);
        if (parent.get(x) !== x) parent.set(x, find(parent.get(x)));
        return parent.get(x);
    };
    for (const [a, b] of synonyms) {
        const ra = find(a), rb = find(b);
        parent.set(ra, rb);
    }
    const groups = new Map();
    for (const word of parent.keys()) {
        const root = find(word);
        if (!groups.has(root)) groups.set(root, []);
        groups.get(root).push(word);
    }
    for (const list of groups.values()) list.sort();
    const words = text.split(" ");
    const choices = words.map((w) => (parent.has(w) ? groups.get(find(w)) : [w]));
    const answer = [];
    const build = (i, parts) => {
        if (i === choices.length) {
            answer.push(parts.join(" "));
            return;
        }
        for (const word of choices[i]) {
            parts.push(word);
            build(i + 1, parts);
            parts.pop();
        }
    };
    build(0, []);
    return answer;
};
''',
    "1259_handshakes_that_dont_cross": r'''// LeetCode 1259 - Handshakes That Don't Cross
// https://leetcode.com/problems/handshakes-that-dont-cross/

/**
 * @param {number} numPeople
 * @return {number}
 */
var numberOfWays = function(numPeople) {
    const mod = 1000000007;
    const dp = Array(numPeople + 1).fill(0);
    dp[0] = 1;
    for (let people = 2; people <= numPeople; people += 2) {
        let total = 0;
        for (let left = 0; left < people; left += 2) {
            total = (total + dp[left] * dp[people - 2 - left]) % mod;
        }
        dp[people] = total;
    }
    return dp[numPeople];
};
''',
    "1260_shift_2d_grid": r'''// LeetCode 1260 - Shift 2D Grid
// https://leetcode.com/problems/shift-2d-grid/

/**
 * @param {number[][]} grid
 * @param {number} k
 * @return {number[][]}
 */
var shiftGrid = function(grid, k) {
    const m = grid.length, n = grid[0].length;
    let flat = grid.flat();
    k %= flat.length;
    if (k) flat = flat.slice(-k).concat(flat.slice(0, -k));
    const answer = [];
    for (let i = 0; i < m; i++) answer.push(flat.slice(i * n, (i + 1) * n));
    return answer;
};
''',
}

SKIP_SQL = {
    "1225_report_contiguous_dates",
    "1241_number_of_comments_per_post",
    "1251_average_selling_price",
}


def is_stub(path: str) -> bool:
    with open(path, encoding="utf-8") as f:
        return "var solve = function" in f.read()


def main() -> None:
    ported = 0
    skipped_sql = 0
    skipped_done = 0
    stubs_found = 0

    for folder in sorted(SOLUTIONS):
        if folder in SKIP_SQL:
            skipped_sql += 1
            continue
        js_path = os.path.join(ROOT, folder, "solution.js")
        if not os.path.isfile(js_path):
            print(f"MISSING {folder}/solution.js")
            continue
        if not is_stub(js_path):
            skipped_done += 1
            continue
        stubs_found += 1
        with open(js_path, "w", encoding="utf-8", newline="\n") as f:
            f.write(SOLUTIONS[folder].strip() + "\n")
        ported += 1
        print(f"ported {folder}")

    print(f"stubs_found={stubs_found} ported={ported} skipped_sql={skipped_sql} skipped_done={skipped_done}")


if __name__ == "__main__":
    main()

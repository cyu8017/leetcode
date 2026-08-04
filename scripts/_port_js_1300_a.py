#!/usr/bin/env python3
"""Port JS solutions for LeetCode stubs batch A (1300-1340 range)."""
from __future__ import annotations

import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SOLUTIONS: dict[str, str] = {
    "1300_sum_of_mutated_array_closest_to_target": r'''// LeetCode 1300 - Sum of Mutated Array Closest to Target
// https://leetcode.com/problems/sum-of-mutated-array-closest-to-target/

/**
 * @param {number[]} arr
 * @param {number} target
 * @return {number}
 */
var findBestValue = function(arr, target) {
    let lo = 0, hi = Math.max(...arr);
    const sumAt = (v) => arr.reduce((s, x) => s + Math.min(x, v), 0);
    while (lo < hi) {
        const mid = (lo + hi) >> 1;
        if (sumAt(mid) < target) lo = mid + 1;
        else hi = mid;
    }
    const before = sumAt(lo - 1), after = sumAt(lo);
    return target - before <= after - target ? lo - 1 : lo;
};
''',
    "1301_number_of_paths_with_max_score": r'''// LeetCode 1301 - Number Of Paths With Max Score
// https://leetcode.com/problems/number-of-paths-with-max-score/

/**
 * @param {string[]} board
 * @return {number[]}
 */
var pathsWithMaxScore = function(board) {
    const mod = 1000000007;
    const n = board.length;
    const score = Array.from({ length: n }, () => Array(n).fill(-1));
    const ways = Array.from({ length: n }, () => Array(n).fill(0));
    score[n - 1][n - 1] = 0;
    ways[n - 1][n - 1] = 1;
    for (let r = n - 1; r >= 0; r--) {
        for (let c = n - 1; c >= 0; c--) {
            if (board[r][c] === "X" || (r === n - 1 && c === n - 1)) continue;
            let best = -1, count = 0;
            for (const [nr, nc] of [[r + 1, c], [r, c + 1], [r + 1, c + 1]]) {
                if (nr < n && nc < n && score[nr][nc] >= 0) {
                    if (score[nr][nc] > best) {
                        best = score[nr][nc];
                        count = ways[nr][nc];
                    } else if (score[nr][nc] === best) {
                        count = (count + ways[nr][nc]) % mod;
                    }
                }
            }
            if (best >= 0) {
                const ch = board[r][c];
                score[r][c] = best + (ch >= "0" && ch <= "9" ? Number(ch) : 0);
                ways[r][c] = count;
            }
        }
    }
    return [Math.max(score[0][0], 0), ways[0][0]];
};
''',
    "1302_deepest_leaves_sum": r'''// LeetCode 1302 - Deepest Leaves Sum
// https://leetcode.com/problems/deepest-leaves-sum/

/**
 * @param {TreeNode} root
 * @return {number}
 */
var deepestLeavesSum = function(root) {
    let level = [root], answer = 0;
    while (level.length) {
        answer = level.reduce((s, n) => s + n.val, 0);
        const next = [];
        for (const node of level) {
            if (node.left) next.push(node.left);
            if (node.right) next.push(node.right);
        }
        level = next;
    }
    return answer;
};
''',
    "1304_find_n_unique_integers_sum_up_to_zero": r'''// LeetCode 1304 - Find N Unique Integers Sum Up To Zero
// https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/

/**
 * @param {number} n
 * @return {number[]}
 */
var sumZero = function(n) {
    const answer = [];
    for (let value = 1; value <= (n >> 1); value++) {
        answer.push(-value, value);
    }
    if (n % 2) answer.push(0);
    return answer;
};
''',
    "1305_all_elements_in_two_binary_search_trees": r'''// LeetCode 1305 - All Elements In Two Binary Search Trees
// https://leetcode.com/problems/all-elements-in-two-binary-search-trees/

/**
 * @param {TreeNode} root1
 * @param {TreeNode} root2
 * @return {number[]}
 */
var getAllElements = function(root1, root2) {
    const inorder = (root) => {
        if (!root) return [];
        return [...inorder(root.left), root.val, ...inorder(root.right)];
    };
    const a = inorder(root1), b = inorder(root2);
    const answer = [];
    let i = 0, j = 0;
    while (i < a.length || j < b.length) {
        if (j === b.length || (i < a.length && a[i] <= b[j])) answer.push(a[i++]);
        else answer.push(b[j++]);
    }
    return answer;
};
''',
    "1306_jump_game_iii": r'''// LeetCode 1306 - Jump Game Iii
// https://leetcode.com/problems/jump-game-iii/

/**
 * @param {number[]} arr
 * @param {number} start
 * @return {boolean}
 */
var canReach = function(arr, start) {
    const stack = [start], seen = new Set();
    while (stack.length) {
        const i = stack.pop();
        if (seen.has(i) || i < 0 || i >= arr.length) continue;
        if (arr[i] === 0) return true;
        seen.add(i);
        stack.push(i - arr[i], i + arr[i]);
    }
    return false;
};
''',
    "1307_verbal_arithmetic_puzzle": r'''// LeetCode 1307 - Verbal Arithmetic Puzzle
// https://leetcode.com/problems/verbal-arithmetic-puzzle/

/**
 * @param {string[]} words
 * @param {string} result
 * @return {boolean}
 */
var isSolvable = function(words, result) {
    if (Math.max(...words.map((w) => w.length)) > result.length) return false;
    const letters = new Set((words.join("") + result).split(""));
    if (letters.size > 10) return false;
    const leading = new Set();
    for (const word of [...words, result]) {
        if (word.length > 1) leading.add(word[0]);
    }
    const value = new Map();
    const used = Array(10).fill(false);
    const width = result.length;

    const solve = (column, row, total) => {
        if (column === width) return total === 0;
        if (row < words.length) {
            if (column >= words[row].length) return solve(column, row + 1, total);
            const ch = words[row][words[row].length - 1 - column];
            if (value.has(ch)) return solve(column, row + 1, total + value.get(ch));
            for (let digit = 0; digit < 10; digit++) {
                if (!used[digit] && (digit || !leading.has(ch))) {
                    value.set(ch, digit);
                    used[digit] = true;
                    if (solve(column, row + 1, total + digit)) return true;
                    used[digit] = false;
                    value.delete(ch);
                }
            }
            return false;
        }
        const ch = result[result.length - 1 - column];
        const digit = total % 10;
        const carry = Math.floor(total / 10);
        if (value.has(ch)) return value.get(ch) === digit && solve(column + 1, 0, carry);
        if (used[digit] || (digit === 0 && leading.has(ch))) return false;
        value.set(ch, digit);
        used[digit] = true;
        const ok = solve(column + 1, 0, carry);
        used[digit] = false;
        value.delete(ch);
        return ok;
    };
    return solve(0, 0, 0);
};
''',
    "1309_decrypt_string_from_alphabet_to_integer_mapping": r'''// LeetCode 1309 - Decrypt String From Alphabet To Integer Mapping
// https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/

/**
 * @param {string} s
 * @return {string}
 */
var freqAlphabets = function(s) {
    const answer = [];
    let i = s.length - 1;
    while (i >= 0) {
        if (s[i] === "#") {
            answer.push(String.fromCharCode(96 + Number(s.slice(i - 2, i))));
            i -= 3;
        } else {
            answer.push(String.fromCharCode(96 + Number(s[i])));
            i -= 1;
        }
    }
    return answer.reverse().join("");
};
''',
    "1310_xor_queries_of_a_subarray": r'''// LeetCode 1310 - Xor Queries Of A Subarray
// https://leetcode.com/problems/xor-queries-of-a-subarray/

/**
 * @param {number[]} arr
 * @param {number[][]} queries
 * @return {number[]}
 */
var xorQueries = function(arr, queries) {
    const prefix = [0];
    for (const value of arr) prefix.push(prefix[prefix.length - 1] ^ value);
    return queries.map(([left, right]) => prefix[right + 1] ^ prefix[left]);
};
''',
    "1311_get_watched_videos_by_your_friends": r'''// LeetCode 1311 - Get Watched Videos By Your Friends
// https://leetcode.com/problems/get-watched-videos-by-your-friends/

/**
 * @param {string[][]} watchedVideos
 * @param {number[][]} friends
 * @param {number} id
 * @param {number} level
 * @return {string[]}
 */
var watchedVideosByFriends = function(watchedVideos, friends, id, level) {
    const queue = [[id, 0]], seen = new Set([id]), people = [];
    while (queue.length) {
        const [person, distance] = queue.shift();
        if (distance === level) {
            people.push(person);
            continue;
        }
        for (const friend of friends[person]) {
            if (!seen.has(friend)) {
                seen.add(friend);
                queue.push([friend, distance + 1]);
            }
        }
    }
    const counts = new Map();
    for (const person of people) {
        for (const video of watchedVideos[person]) {
            counts.set(video, (counts.get(video) || 0) + 1);
        }
    }
    return [...counts.keys()].sort((a, b) => counts.get(a) - counts.get(b) || (a < b ? -1 : a > b ? 1 : 0));
};
''',
    "1312_minimum_insertion_steps_to_make_a_string_palindrome": r'''// LeetCode 1312 - Minimum Insertion Steps To Make A String Palindrome
// https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/

/**
 * @param {string} s
 * @return {number}
 */
var minInsertions = function(s) {
    const n = s.length;
    const dp = Array(n).fill(0);
    for (let left = n - 2; left >= 0; left--) {
        let diagonal = 0;
        for (let right = left + 1; right < n; right++) {
            const old = dp[right];
            if (s[left] === s[right]) dp[right] = diagonal;
            else dp[right] = 1 + Math.min(dp[right], dp[right - 1]);
            diagonal = old;
        }
    }
    return dp.length ? dp[dp.length - 1] : 0;
};
''',
    "1313_decompress_run_length_encoded_list": r'''// LeetCode 1313 - Decompress Run Length Encoded List
// https://leetcode.com/problems/decompress-run-length-encoded-list/

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var decompressRLElist = function(nums) {
    const answer = [];
    for (let i = 0; i < nums.length; i += 2) {
        for (let j = 0; j < nums[i]; j++) answer.push(nums[i + 1]);
    }
    return answer;
};
''',
    "1314_matrix_block_sum": r'''// LeetCode 1314 - Matrix Block Sum
// https://leetcode.com/problems/matrix-block-sum/

/**
 * @param {number[][]} mat
 * @param {number} k
 * @return {number[][]}
 */
var matrixBlockSum = function(mat, k) {
    const m = mat.length, n = mat[0].length;
    const prefix = Array.from({ length: m + 1 }, () => Array(n + 1).fill(0));
    for (let r = 0; r < m; r++) {
        for (let c = 0; c < n; c++) {
            prefix[r + 1][c + 1] = mat[r][c] + prefix[r][c + 1] + prefix[r + 1][c] - prefix[r][c];
        }
    }
    const answer = Array.from({ length: m }, () => Array(n).fill(0));
    for (let r = 0; r < m; r++) {
        for (let c = 0; c < n; c++) {
            const r1 = Math.max(0, r - k), c1 = Math.max(0, c - k);
            const r2 = Math.min(m, r + k + 1), c2 = Math.min(n, c + k + 1);
            answer[r][c] = prefix[r2][c2] - prefix[r1][c2] - prefix[r2][c1] + prefix[r1][c1];
        }
    }
    return answer;
};
''',
    "1315_sum_of_nodes_with_even_valued_grandparent": r'''// LeetCode 1315 - Sum Of Nodes With Even Valued Grandparent
// https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/

/**
 * @param {TreeNode} root
 * @return {number}
 */
var sumEvenGrandparent = function(root) {
    const dfs = (node, parent, grandparent) => {
        if (!node) return 0;
        const add = grandparent && grandparent.val % 2 === 0 ? node.val : 0;
        return add + dfs(node.left, node, parent) + dfs(node.right, node, parent);
    };
    return dfs(root, null, null);
};
''',
    "1316_distinct_echo_substrings": r'''// LeetCode 1316 - Distinct Echo Substrings
// https://leetcode.com/problems/distinct-echo-substrings/

/**
 * @param {string} text
 * @return {number}
 */
var distinctEchoSubstrings = function(text) {
    const n = text.length;
    const mod1 = 1000000007, mod2 = 1000000009, base = 911382323;
    const h1 = Array(n + 1).fill(0), h2 = Array(n + 1).fill(0);
    const p1 = Array(n + 1).fill(1), p2 = Array(n + 1).fill(1);
    for (let i = 0; i < n; i++) {
        const code = text.charCodeAt(i);
        h1[i + 1] = (h1[i] * base + code) % mod1;
        h2[i + 1] = (h2[i] * base + code) % mod2;
        p1[i + 1] = (p1[i] * base) % mod1;
        p2[i + 1] = (p2[i] * base) % mod2;
    }
    const hashed = (left, right) => {
        const length = right - left;
        return [
            ((h1[right] - h1[left] * p1[length]) % mod1 + mod1) % mod1,
            ((h2[right] - h2[left] * p2[length]) % mod2 + mod2) % mod2,
        ];
    };
    const echoes = new Set();
    for (let half = 1; half <= (n >> 1); half++) {
        for (let left = 0; left <= n - 2 * half; left++) {
            const a = hashed(left, left + half);
            const b = hashed(left + half, left + 2 * half);
            if (a[0] === b[0] && a[1] === b[1]) {
                const full = hashed(left, left + 2 * half);
                echoes.add(`${2 * half},${full[0]},${full[1]}`);
            }
        }
    }
    return echoes.size;
};
''',
    "1317_convert_integer_to_the_sum_of_two_no_zero_integers": r'''// LeetCode 1317 - Convert Integer To The Sum Of Two No Zero Integers
// https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/

/**
 * @param {number} n
 * @return {number[]}
 */
var getNoZeroIntegers = function(n) {
    const valid = (value) => !String(value).includes("0");
    for (let first = 1; first < n; first++) {
        if (valid(first) && valid(n - first)) return [first, n - first];
    }
    return [];
};
''',
    "1318_minimum_flips_to_make_a_or_b_equal_to_c": r'''// LeetCode 1318 - Minimum Flips To Make A Or B Equal To C
// https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/

/**
 * @param {number} a
 * @param {number} b
 * @param {number} c
 * @return {number}
 */
var minFlips = function(a, b, c) {
    let flips = 0;
    while (a || b || c) {
        const x = a & 1, y = b & 1, z = c & 1;
        flips += z === 0 ? x + y : (x === 0 && y === 0 ? 1 : 0);
        a >>= 1; b >>= 1; c >>= 1;
    }
    return flips;
};
''',
    "1319_number_of_operations_to_make_network_connected": r'''// LeetCode 1319 - Number Of Operations To Make Network Connected
// https://leetcode.com/problems/number-of-operations-to-make-network-connected/

/**
 * @param {number} n
 * @param {number[][]} connections
 * @return {number}
 */
var makeConnected = function(n, connections) {
    if (connections.length < n - 1) return -1;
    const parent = Array.from({ length: n }, (_, i) => i);
    const find = (x) => {
        while (x !== parent[x]) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    };
    for (const [a, b] of connections) {
        const ra = find(a), rb = find(b);
        if (ra !== rb) parent[ra] = rb;
    }
    const roots = new Set();
    for (let i = 0; i < n; i++) roots.add(find(i));
    return roots.size - 1;
};
''',
    "1320_minimum_distance_to_type_a_word_using_two_fingers": r'''// LeetCode 1320 - Minimum Distance To Type A Word Using Two Fingers
// https://leetcode.com/problems/minimum-distance-to-type-a-word-using-two-fingers/

/**
 * @param {string} word
 * @return {number}
 */
var minimumDistance = function(word) {
    const distance = (a, b) => {
        if (a === 26) return 0;
        return Math.abs(Math.floor(a / 6) - Math.floor(b / 6)) + Math.abs(a % 6 - b % 6);
    };
    const letters = [...word].map((ch) => ch.charCodeAt(0) - 65);
    let dp = new Map([[26, 0]]);
    let previous = letters[0];
    for (let i = 1; i < letters.length; i++) {
        const current = letters[i];
        const nxt = new Map();
        for (const [free, cost] of dp) {
            nxt.set(free, Math.min(nxt.get(free) ?? 1e9, cost + distance(previous, current)));
            nxt.set(previous, Math.min(nxt.get(previous) ?? 1e9, cost + distance(free, current)));
        }
        dp = nxt;
        previous = current;
    }
    return Math.min(...dp.values());
};
''',
    "1323_maximum_69_number": r'''// LeetCode 1323 - Maximum 69 Number
// https://leetcode.com/problems/maximum-69-number/

/**
 * @param {number} num
 * @return {number}
 */
var maximum69Number = function(num) {
    return Number(String(num).replace("6", "9"));
};
''',
    "1324_print_words_vertically": r'''// LeetCode 1324 - Print Words Vertically
// https://leetcode.com/problems/print-words-vertically/

/**
 * @param {string} s
 * @return {string[]}
 */
var printVertically = function(s) {
    const words = s.split(" ");
    const maxLen = Math.max(...words.map((w) => w.length));
    const answer = [];
    for (let i = 0; i < maxLen; i++) {
        let row = "";
        for (const word of words) row += i < word.length ? word[i] : " ";
        answer.push(row.replace(/\s+$/, ""));
    }
    return answer;
};
''',
    "1325_delete_leaves_with_a_given_value": r'''// LeetCode 1325 - Delete Leaves With A Given Value
// https://leetcode.com/problems/delete-leaves-with-a-given-value/

/**
 * @param {TreeNode} root
 * @param {number} target
 * @return {TreeNode}
 */
var removeLeafNodes = function(root, target) {
    if (!root) return null;
    root.left = removeLeafNodes(root.left, target);
    root.right = removeLeafNodes(root.right, target);
    if (!root.left && !root.right && root.val === target) return null;
    return root;
};
''',
    "1326_minimum_number_of_taps_to_open_to_water_a_garden": r'''// LeetCode 1326 - Minimum Number Of Taps To Open To Water A Garden
// https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/

/**
 * @param {number} n
 * @param {number[]} ranges
 * @return {number}
 */
var minTaps = function(n, ranges) {
    const farthest = Array(n + 1).fill(0);
    for (let center = 0; center < ranges.length; center++) {
        const left = Math.max(0, center - ranges[center]);
        const right = Math.min(n, center + ranges[center]);
        farthest[left] = Math.max(farthest[left], right);
    }
    let taps = 0, end = 0, reach = 0;
    for (let position = 0; position < n; position++) {
        reach = Math.max(reach, farthest[position]);
        if (position === end) {
            if (reach <= position) return -1;
            taps++;
            end = reach;
        }
    }
    return taps;
};
''',
    "1328_break_a_palindrome": r'''// LeetCode 1328 - Break A Palindrome
// https://leetcode.com/problems/break-a-palindrome/

/**
 * @param {string} palindrome
 * @return {string}
 */
var breakPalindrome = function(palindrome) {
    if (palindrome.length === 1) return "";
    const chars = palindrome.split("");
    for (let i = 0; i < chars.length >> 1; i++) {
        if (chars[i] !== "a") {
            chars[i] = "a";
            return chars.join("");
        }
    }
    chars[chars.length - 1] = "b";
    return chars.join("");
};
''',
    "1329_sort_the_matrix_diagonally": r'''// LeetCode 1329 - Sort The Matrix Diagonally
// https://leetcode.com/problems/sort-the-matrix-diagonally/

/**
 * @param {number[][]} mat
 * @return {number[][]}
 */
var diagonalSort = function(mat) {
    const diagonals = new Map();
    for (let r = 0; r < mat.length; r++) {
        for (let c = 0; c < mat[0].length; c++) {
            const key = r - c;
            if (!diagonals.has(key)) diagonals.set(key, []);
            diagonals.get(key).push(mat[r][c]);
        }
    }
    for (const values of diagonals.values()) values.sort((a, b) => b - a);
    for (let r = 0; r < mat.length; r++) {
        for (let c = 0; c < mat[0].length; c++) {
            mat[r][c] = diagonals.get(r - c).pop();
        }
    }
    return mat;
};
''',
    "1330_reverse_subarray_to_maximize_array_value": r'''// LeetCode 1330 - Reverse Subarray To Maximize Array Value
// https://leetcode.com/problems/reverse-subarray-to-maximize-array-value/

/**
 * @param {number[]} nums
 * @return {number}
 */
var maxValueAfterReverse = function(nums) {
    let base = 0;
    for (let i = 0; i < nums.length - 1; i++) base += Math.abs(nums[i] - nums[i + 1]);
    let gain = 0, low = 1e9, high = -1e9;
    for (let i = 0; i < nums.length - 1; i++) {
        const a = nums[i], b = nums[i + 1];
        gain = Math.max(gain, Math.abs(nums[0] - b) - Math.abs(a - b), Math.abs(nums[nums.length - 1] - a) - Math.abs(a - b));
        low = Math.min(low, Math.max(a, b));
        high = Math.max(high, Math.min(a, b));
    }
    return base + Math.max(gain, 2 * (high - low));
};
''',
    "1331_rank_transform_of_an_array": r'''// LeetCode 1331 - Rank Transform Of An Array
// https://leetcode.com/problems/rank-transform-of-an-array/

/**
 * @param {number[]} arr
 * @return {number[]}
 */
var arrayRankTransform = function(arr) {
    const sorted = [...new Set(arr)].sort((a, b) => a - b);
    const rank = new Map(sorted.map((value, i) => [value, i + 1]));
    return arr.map((value) => rank.get(value));
};
''',
    "1332_remove_palindromic_subsequences": r'''// LeetCode 1332 - Remove Palindromic Subsequences
// https://leetcode.com/problems/remove-palindromic-subsequences/

/**
 * @param {string} s
 * @return {number}
 */
var removePalindromeSub = function(s) {
    if (!s) return 0;
    return s === s.split("").reverse().join("") ? 1 : 2;
};
''',
    "1333_filter_restaurants_by_vegan_friendly_price_and_distance": r'''// LeetCode 1333 - Filter Restaurants By Vegan Friendly Price And Distance
// https://leetcode.com/problems/filter-restaurants-by-vegan-friendly-price-and-distance/

/**
 * @param {number[][]} restaurants
 * @param {number} veganFriendly
 * @param {number} maxPrice
 * @param {number} maxDistance
 * @return {number[]}
 */
var filterRestaurants = function(restaurants, veganFriendly, maxPrice, maxDistance) {
    const valid = restaurants.filter((row) => (!veganFriendly || row[2]) && row[3] <= maxPrice && row[4] <= maxDistance);
    valid.sort((a, b) => b[1] - a[1] || b[0] - a[0]);
    return valid.map((row) => row[0]);
};
''',
    "1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance": r'''// LeetCode 1334 - Find The City With The Smallest Number Of Neighbors At A Threshold Distance
// https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/

/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {number} distanceThreshold
 * @return {number}
 */
var findTheCity = function(n, edges, distanceThreshold) {
    const inf = 1e15;
    const dist = Array.from({ length: n }, () => Array(n).fill(inf));
    for (let i = 0; i < n; i++) dist[i][i] = 0;
    for (const [a, b, weight] of edges) {
        dist[a][b] = dist[b][a] = weight;
    }
    for (let k = 0; k < n; k++) {
        for (let i = 0; i < n; i++) {
            for (let j = 0; j < n; j++) {
                dist[i][j] = Math.min(dist[i][j], dist[i][k] + dist[k][j]);
            }
        }
    }
    let bestCity = 0, bestCount = n;
    for (let city = 0; city < n; city++) {
        const count = dist[city].filter((d) => d <= distanceThreshold).length;
        if (count < bestCount || (count === bestCount && city > bestCity)) {
            bestCount = count;
            bestCity = city;
        }
    }
    return bestCity;
};
''',
    "1335_minimum_difficulty_of_a_job_schedule": r'''// LeetCode 1335 - Minimum Difficulty Of A Job Schedule
// https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/

/**
 * @param {number[]} jobDifficulty
 * @param {number} d
 * @return {number}
 */
var minDifficulty = function(jobDifficulty, d) {
    const n = jobDifficulty.length;
    if (n < d) return -1;
    let dp = Array(n).fill(1e9);
    let hardest = 0;
    for (let i = 0; i < n; i++) {
        hardest = Math.max(hardest, jobDifficulty[i]);
        dp[i] = hardest;
    }
    for (let day = 1; day < d; day++) {
        const nxt = Array(n).fill(1e9);
        for (let end = day; end < n; end++) {
            hardest = 0;
            for (let start = end; start >= day; start--) {
                hardest = Math.max(hardest, jobDifficulty[start]);
                nxt[end] = Math.min(nxt[end], dp[start - 1] + hardest);
            }
        }
        dp = nxt;
    }
    return dp[n - 1];
};
''',
    "1337_the_k_weakest_rows_in_a_matrix": r'''// LeetCode 1337 - The K Weakest Rows In A Matrix
// https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/

/**
 * @param {number[][]} mat
 * @param {number} k
 * @return {number[]}
 */
var kWeakestRows = function(mat, k) {
    return [...mat.keys()].sort((a, b) => mat[a].reduce((s, x) => s + x, 0) - mat[b].reduce((s, x) => s + x, 0) || a - b).slice(0, k);
};
''',
    "1338_reduce_array_size_to_the_half": r'''// LeetCode 1338 - Reduce Array Size To The Half
// https://leetcode.com/problems/reduce-array-size-to-the-half/

/**
 * @param {number[]} arr
 * @return {number}
 */
var minSetSize = function(arr) {
    const counts = new Map();
    for (const value of arr) counts.set(value, (counts.get(value) || 0) + 1);
    const freqs = [...counts.values()].sort((a, b) => b - a);
    let removed = 0;
    for (let i = 0; i < freqs.length; i++) {
        removed += freqs[i];
        if (removed * 2 >= arr.length) return i + 1;
    }
    return 0;
};
''',
    "1339_maximum_product_of_splitted_binary_tree": r'''// LeetCode 1339 - Maximum Product Of Splitted Binary Tree
// https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/

/**
 * @param {TreeNode} root
 * @return {number}
 */
var maxProduct = function(root) {
    const sums = [];
    const total = (node) => {
        if (!node) return 0;
        const value = node.val + total(node.left) + total(node.right);
        sums.push(value);
        return value;
    };
    const whole = total(root);
    let best = 0;
    for (const value of sums) best = Math.max(best, value * (whole - value));
    return best % 1000000007;
};
''',
    "1340_jump_game_v": r'''// LeetCode 1340 - Jump Game V
// https://leetcode.com/problems/jump-game-v/

/**
 * @param {number[]} arr
 * @param {number} d
 * @return {number}
 */
var maxJumps = function(arr, d) {
    const dp = Array(arr.length).fill(1);
    const order = arr.map((value, i) => [value, i]).sort((a, b) => a[0] - b[0]);
    for (const [, i] of order) {
        for (const step of [-1, 1]) {
            let j = i + step;
            while (j >= 0 && j < arr.length && Math.abs(j - i) <= d && arr[j] < arr[i]) {
                dp[i] = Math.max(dp[i], 1 + dp[j]);
                j += step;
            }
        }
    }
    return Math.max(...dp);
};
''',
}


def main() -> None:
    written = 0
    for folder, content in SOLUTIONS.items():
        path = os.path.join(ROOT, folder, "solution.js")
        if not os.path.isdir(os.path.join(ROOT, folder)):
            raise SystemExit(f"missing folder: {folder}")
        with open(path, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(content)
        written += 1
        print(f"wrote {folder}")
    print(f"done: {written}")


if __name__ == "__main__":
    main()

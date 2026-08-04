#!/usr/bin/env python3
"""Port JS solutions for LeetCode stubs 1938-1969 (non-SQL)."""
from __future__ import annotations

import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SOLUTIONS: dict[str, str] = {
    "1938_maximum_genetic_difference_query": r'''// LeetCode 1938 - Maximum Genetic Difference Query
// https://leetcode.com/problems/maximum-genetic-difference-query/

/**
 * @param {number[]} parents
 * @param {number[][]} queries
 * @return {number[]}
 */
var maxGeneticDifference = function(parents, queries) {
    const n = parents.length;
    const children = Array.from({ length: n }, () => []);
    let root = 0;
    for (let i = 0; i < n; i++) {
        if (parents[i] === -1) root = i;
        else children[parents[i]].push(i);
    }
    const qmap = Array.from({ length: n }, () => []);
    for (let i = 0; i < queries.length; i++) qmap[queries[i][0]].push([i, queries[i][1]]);
    const ans = new Array(queries.length).fill(0);
    const BITS = 17;
    const makeNode = () => ({ child: [null, null], cnt: 0 });
    const trieRoot = makeNode();
    const trieUpdate = (num, delta) => {
        let node = trieRoot;
        for (let b = BITS; b >= 0; b--) {
            const bit = (num >> b) & 1;
            if (!node.child[bit]) node.child[bit] = makeNode();
            node = node.child[bit];
            node.cnt += delta;
        }
    };
    const trieMaxXor = (num) => {
        let node = trieRoot, res = 0;
        for (let b = BITS; b >= 0; b--) {
            const bit = (num >> b) & 1;
            const want = 1 - bit;
            if (node.child[want] && node.child[want].cnt > 0) {
                res |= 1 << b;
                node = node.child[want];
            } else {
                node = node.child[bit];
            }
        }
        return res;
    };
    const dfs = (u) => {
        trieUpdate(u, 1);
        for (const [qi, val] of qmap[u]) ans[qi] = trieMaxXor(val);
        for (const v of children[u]) dfs(v);
        trieUpdate(u, -1);
    };
    dfs(root);
    return ans;
};
''',
    "1940_longest_common_subsequence_between_sorted_arrays": r'''// LeetCode 1940 - Longest Common Subsequence Between Sorted Arrays
// https://leetcode.com/problems/longest-common-subsequence-between-sorted-arrays/

/**
 * @param {number[][]} arrays
 * @return {number[]}
 */
var longestCommonSubsequence = function(arrays) {
    const cnt = new Map();
    for (const arr of arrays) {
        for (const x of arr) cnt.set(x, (cnt.get(x) || 0) + 1);
    }
    const m = arrays.length;
    return arrays[0].filter((x) => cnt.get(x) === m);
};
''',
    "1941_check_if_all_characters_have_equal_number_of_occurrences": r'''// LeetCode 1941 - Check if All Characters Have Equal Number of Occurrences
// https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/

/**
 * @param {string} s
 * @return {boolean}
 */
var areOccurrencesEqual = function(s) {
    const freq = new Map();
    for (const c of s) freq.set(c, (freq.get(c) || 0) + 1);
    return new Set(freq.values()).size === 1;
};
''',
    "1942_the_number_of_the_smallest_unoccupied_chair": r'''// LeetCode 1942 - The Number of the Smallest Unoccupied Chair
// https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair/

/**
 * @param {number[][]} times
 * @param {number} targetFriend
 * @return {number}
 */
var smallestChair = function(times, targetFriend) {
    const order = [...times.keys()].sort((a, b) => times[a][0] - times[b][0]);
    const free = [];
    let nextChair = 0;
    const leaving = [];
    const push = (heap, item, cmp) => {
        heap.push(item);
        let i = heap.length - 1;
        while (i > 0) {
            const p = (i - 1) >> 1;
            if (cmp(heap[p], heap[i]) <= 0) break;
            [heap[p], heap[i]] = [heap[i], heap[p]];
            i = p;
        }
    };
    const pop = (heap, cmp) => {
        const top = heap[0];
        const last = heap.pop();
        if (!heap.length) return top;
        heap[0] = last;
        let i = 0;
        while (true) {
            let s = i;
            const l = 2 * i + 1, r = 2 * i + 2;
            if (l < heap.length && cmp(heap[l], heap[s]) < 0) s = l;
            if (r < heap.length && cmp(heap[r], heap[s]) < 0) s = r;
            if (s === i) break;
            [heap[s], heap[i]] = [heap[i], heap[s]];
            i = s;
        }
        return top;
    };
    const cmpNum = (a, b) => a - b;
    const cmpLeave = (a, b) => a[0] - b[0];
    for (const i of order) {
        const [arr, leave] = times[i];
        while (leaving.length && leaving[0][0] <= arr) push(free, pop(leaving, cmpLeave)[1], cmpNum);
        let chair;
        if (free.length) chair = pop(free, cmpNum);
        else chair = nextChair++;
        if (i === targetFriend) return chair;
        push(leaving, [leave, chair], cmpLeave);
    }
    return -1;
};
''',
    "1943_describe_the_painting": r'''// LeetCode 1943 - Describe the Painting
// https://leetcode.com/problems/describe-the-painting/

/**
 * @param {number[][]} segments
 * @return {number[][]}
 */
var splitPainting = function(segments) {
    const diff = new Map();
    for (const [s, e, c] of segments) {
        diff.set(s, (diff.get(s) || 0) + c);
        diff.set(e, (diff.get(e) || 0) - c);
    }
    const points = [...diff.keys()].sort((a, b) => a - b);
    const ans = [];
    let cur = 0;
    for (let i = 0; i < points.length - 1; i++) {
        cur += diff.get(points[i]);
        if (cur) ans.push([points[i], points[i + 1], cur]);
    }
    return ans;
};
''',
    "1944_number_of_visible_people_in_a_queue": r'''// LeetCode 1944 - Number of Visible People in a Queue
// https://leetcode.com/problems/number-of-visible-people-in-a-queue/

/**
 * @param {number[]} heights
 * @return {number[]}
 */
var canSeePersonsCount = function(heights) {
    const n = heights.length;
    const ans = new Array(n).fill(0);
    const stack = [];
    for (let i = n - 1; i >= 0; i--) {
        let count = 0;
        while (stack.length && heights[i] > stack[stack.length - 1]) {
            stack.pop();
            count++;
        }
        if (stack.length) count++;
        ans[i] = count;
        stack.push(heights[i]);
    }
    return ans;
};
''',
    "1945_sum_of_digits_of_string_after_convert": r'''// LeetCode 1945 - Sum of Digits of String After Convert
// https://leetcode.com/problems/sum-of-digits-of-string-after-convert/

/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var getLucky = function(s, k) {
    let num = [...s].map((c) => String(c.charCodeAt(0) - 96)).join("");
    for (let i = 0; i < k; i++) {
        let sum = 0;
        for (const d of num) sum += d.charCodeAt(0) - 48;
        num = String(sum);
    }
    return Number(num);
};
''',
    "1946_largest_number_after_mutating_substring": r'''// LeetCode 1946 - Largest Number After Mutating Substring
// https://leetcode.com/problems/largest-number-after-mutating-substring/

/**
 * @param {string} num
 * @param {number[]} change
 * @return {string}
 */
var maximumNumber = function(num, change) {
    const chars = num.split("");
    let started = false;
    for (let i = 0; i < chars.length; i++) {
        const d = chars[i].charCodeAt(0) - 48;
        const mapped = change[d];
        if (mapped > d) {
            chars[i] = String(mapped);
            started = true;
        } else if (mapped < d && started) break;
    }
    return chars.join("");
};
''',
    "1947_maximum_compatibility_score_sum": r'''// LeetCode 1947 - Maximum Compatibility Score Sum
// https://leetcode.com/problems/maximum-compatibility-score-sum/

/**
 * @param {number[][]} students
 * @param {number[][]} mentors
 * @return {number}
 */
var maxCompatibilitySum = function(students, mentors) {
    const m = students.length;
    const score = Array.from({ length: m }, () => new Array(m).fill(0));
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < m; j++) {
            let s = 0;
            for (let k = 0; k < students[i].length; k++) if (students[i][k] === mentors[j][k]) s++;
            score[i][j] = s;
        }
    }
    const memo = new Map();
    const dp = (i, mask) => {
        if (i === m) return 0;
        const key = `${i},${mask}`;
        if (memo.has(key)) return memo.get(key);
        let best = 0;
        for (let j = 0; j < m; j++) {
            if ((mask & (1 << j)) === 0) best = Math.max(best, score[i][j] + dp(i + 1, mask | (1 << j)));
        }
        memo.set(key, best);
        return best;
    };
    return dp(0, 0);
};
''',
    "1948_delete_duplicate_folders_in_system": r'''// LeetCode 1948 - Delete Duplicate Folders in System
// https://leetcode.com/problems/delete-duplicate-folders-in-system/

/**
 * @param {string[][]} paths
 * @return {string[][]}
 */
var deleteDuplicateFolder = function(paths) {
    const root = new Map();
    for (const path of paths) {
        let node = root;
        for (const folder of path) {
            if (!node.has(folder)) node.set(folder, new Map());
            node = node.get(folder);
        }
    }
    const dup = new Map();
    const serialOf = new WeakMap();
    const serialize = (node) => {
        if (!node.size) return "";
        const parts = [];
        for (const name of [...node.keys()].sort()) {
            parts.push(name + "(" + serialize(node.get(name)) + ")");
        }
        const serial = parts.join("");
        if (serial) {
            dup.set(serial, dup.has(serial));
            serialOf.set(node, serial);
        }
        return serial;
    };
    serialize(root);
    const ans = [];
    const collect = (node, path) => {
        for (const [name, child] of node) {
            const serial = serialOf.get(child) || "";
            if (serial && dup.get(serial)) continue;
            path.push(name);
            ans.push(path.slice());
            collect(child, path);
            path.pop();
        }
    };
    collect(root, []);
    return ans;
};
''',
    "1950_maximum_of_minimum_values_in_all_subarrays": r'''// LeetCode 1950 - Maximum of Minimum Values in All Subarrays
// https://leetcode.com/problems/maximum-of-minimum-values-in-all-subarrays/

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findMaximums = function(nums) {
    const n = nums.length;
    const left = new Array(n).fill(-1);
    const right = new Array(n).fill(n);
    let stack = [];
    for (let i = 0; i < n; i++) {
        while (stack.length && nums[stack[stack.length - 1]] >= nums[i]) stack.pop();
        left[i] = stack.length ? stack[stack.length - 1] : -1;
        stack.push(i);
    }
    stack = [];
    for (let i = n - 1; i >= 0; i--) {
        while (stack.length && nums[stack[stack.length - 1]] >= nums[i]) stack.pop();
        right[i] = stack.length ? stack[stack.length - 1] : n;
        stack.push(i);
    }
    const ans = new Array(n).fill(0);
    for (let i = 0; i < n; i++) {
        const length = right[i] - left[i] - 1;
        ans[length - 1] = Math.max(ans[length - 1], nums[i]);
    }
    for (let i = n - 2; i >= 0; i--) ans[i] = Math.max(ans[i], ans[i + 1]);
    return ans;
};
''',
    "1952_three_divisors": r'''// LeetCode 1952 - Three Divisors
// https://leetcode.com/problems/three-divisors/

/**
 * @param {number} n
 * @return {boolean}
 */
var isThree = function(n) {
    const root = Math.floor(Math.sqrt(n));
    if (root * root !== n || root < 2) return false;
    for (let i = 2; i * i <= root; i++) if (root % i === 0) return false;
    return true;
};
''',
    "1953_maximum_number_of_weeks_for_which_you_can_work": r'''// LeetCode 1953 - Maximum Number of Weeks for Which You Can Work
// https://leetcode.com/problems/maximum-number-of-weeks-for-which-you-can-work/

/**
 * @param {number[]} milestones
 * @return {number}
 */
var numberOfWeeks = function(milestones) {
    const total = milestones.reduce((a, b) => a + b, 0);
    const mx = Math.max(...milestones);
    const rest = total - mx;
    if (mx > rest + 1) return 2 * rest + 1;
    return total;
};
''',
    "1954_minimum_garden_perimeter_to_collect_enough_apples": r'''// LeetCode 1954 - Minimum Garden Perimeter to Collect Enough Apples
// https://leetcode.com/problems/minimum-garden-perimeter-to-collect-enough-apples/

/**
 * @param {number} neededApples
 * @return {number}
 */
var minimumPerimeter = function(neededApples) {
    let lo = 1, hi = 100000;
    while (lo < hi) {
        const mid = Math.floor((lo + hi) / 2);
        const apples = 2 * mid * (mid + 1) * (2 * mid + 1);
        if (apples >= neededApples) hi = mid;
        else lo = mid + 1;
    }
    return 8 * lo;
};
''',
    "1955_count_number_of_special_subsequences": r'''// LeetCode 1955 - Count Number of Special Subsequences
// https://leetcode.com/problems/count-number-of-special-subsequences/

/**
 * @param {number[]} nums
 * @return {number}
 */
var countSpecialSubsequences = function(nums) {
    const MOD = 1000000007;
    let a = 0, b = 0, c = 0;
    for (const x of nums) {
        if (x === 0) a = (a * 2 + 1) % MOD;
        else if (x === 1) b = (b * 2 + a) % MOD;
        else c = (c * 2 + b) % MOD;
    }
    return c;
};
''',
    "1956_minimum_time_for_k_virus_variants_to_spread": r'''// LeetCode 1956 - Minimum Time For K Virus Variants to Spread
// https://leetcode.com/problems/minimum-time-for-k-virus-variants-to-spread/

/**
 * @param {number[][]} points
 * @param {number} k
 * @return {number}
 */
var minDayskVariants = function(points, k) {
    let ans = Infinity;
    for (let x = 1; x <= 100; x++) {
        for (let y = 1; y <= 100; y++) {
            const dists = points.map(([px, py]) => Math.abs(px - x) + Math.abs(py - y)).sort((a, b) => a - b);
            ans = Math.min(ans, dists[k - 1]);
        }
    }
    return ans;
};
''',
    "1957_delete_characters_to_make_fancy_string": r'''// LeetCode 1957 - Delete Characters to Make Fancy String
// https://leetcode.com/problems/delete-characters-to-make-fancy-string/

/**
 * @param {string} s
 * @return {string}
 */
var makeFancyString = function(s) {
    const ans = [];
    for (const c of s) {
        if (ans.length >= 2 && ans[ans.length - 1] === c && ans[ans.length - 2] === c) continue;
        ans.push(c);
    }
    return ans.join("");
};
''',
    "1958_check_if_move_is_legal": r'''// LeetCode 1958 - Check if Move is Legal
// https://leetcode.com/problems/check-if-move-is-legal/

/**
 * @param {character[][]} board
 * @param {number} rMove
 * @param {number} cMove
 * @param {character} color
 * @return {boolean}
 */
var checkMove = function(board, rMove, cMove, color) {
    const opp = color === "B" ? "W" : "B";
    const dirs = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]];
    for (const [dr, dc] of dirs) {
        let r = rMove + dr, c = cMove + dc, steps = 0;
        while (r >= 0 && r < 8 && c >= 0 && c < 8 && board[r][c] === opp) {
            r += dr;
            c += dc;
            steps++;
        }
        if (steps && r >= 0 && r < 8 && c >= 0 && c < 8 && board[r][c] === color) return true;
    }
    return false;
};
''',
    "1959_minimum_total_space_wasted_with_k_resizing_operations": r'''// LeetCode 1959 - Minimum Total Space Wasted With K Resizing Operations
// https://leetcode.com/problems/minimum-total-space-wasted-with-k-resizing-operations/

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var minSpaceWastedKResizing = function(nums, k) {
    const n = nums.length;
    const INF = Number.MAX_SAFE_INTEGER;
    const waste = Array.from({ length: n }, () => new Array(n).fill(0));
    for (let i = 0; i < n; i++) {
        let mx = 0, total = 0;
        for (let j = i; j < n; j++) {
            mx = Math.max(mx, nums[j]);
            total += nums[j];
            waste[i][j] = mx * (j - i + 1) - total;
        }
    }
    const segments = k + 1;
    const dp = Array.from({ length: n + 1 }, () => new Array(segments + 1).fill(INF));
    dp[0][0] = 0;
    for (let i = 1; i <= n; i++) {
        for (let s = 1; s <= Math.min(segments, i); s++) {
            for (let p = s - 1; p < i; p++) {
                dp[i][s] = Math.min(dp[i][s], dp[p][s - 1] + waste[p][i - 1]);
            }
        }
    }
    let ans = INF;
    for (let s = 1; s <= segments; s++) ans = Math.min(ans, dp[n][s]);
    return ans;
};
''',
    "1960_maximum_product_of_the_length_of_two_palindromic_substrings": r'''// LeetCode 1960 - Maximum Product of the Length of Two Palindromic Substrings
// https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-substrings/

/**
 * @param {string} s
 * @return {number}
 */
var maxProduct = function(s) {
    const n = s.length;
    const radius = new Array(n).fill(0);
    let center = 0, right = 0;
    for (let i = 0; i < n; i++) {
        if (i < right) radius[i] = Math.min(right - i, radius[2 * center - i]);
        while (i - radius[i] - 1 >= 0 && i + radius[i] + 1 < n && s[i - radius[i] - 1] === s[i + radius[i] + 1]) {
            radius[i]++;
        }
        if (i + radius[i] > right) {
            center = i;
            right = i + radius[i];
        }
    }
    const end = new Array(n).fill(1);
    const start = new Array(n).fill(1);
    for (let i = 0; i < n; i++) {
        const r = radius[i];
        end[i + r] = Math.max(end[i + r], 2 * r + 1);
        start[i - r] = Math.max(start[i - r], 2 * r + 1);
    }
    for (let i = n - 2; i >= 0; i--) end[i] = Math.max(end[i], end[i + 1] - 2);
    for (let i = 1; i < n; i++) start[i] = Math.max(start[i], start[i - 1] - 2);
    const pre = new Array(n).fill(0);
    pre[0] = end[0];
    for (let i = 1; i < n; i++) pre[i] = Math.max(pre[i - 1], end[i]);
    const suf = new Array(n).fill(0);
    suf[n - 1] = start[n - 1];
    for (let i = n - 2; i >= 0; i--) suf[i] = Math.max(suf[i + 1], start[i]);
    let ans = 0;
    for (let i = 0; i < n - 1; i++) ans = Math.max(ans, pre[i] * suf[i + 1]);
    return ans;
};
''',
    "1961_check_if_string_is_a_prefix_of_array": r'''// LeetCode 1961 - Check If String Is a Prefix of Array
// https://leetcode.com/problems/check-if-string-is-a-prefix-of-array/

/**
 * @param {string} s
 * @param {string[]} words
 * @return {boolean}
 */
var isPrefixString = function(s, words) {
    let cur = "";
    for (const w of words) {
        cur += w;
        if (cur === s) return true;
        if (cur.length > s.length || !s.startsWith(cur)) return false;
    }
    return false;
};
''',
    "1962_remove_stones_to_minimize_the_total": r'''// LeetCode 1962 - Remove Stones to Minimize the Total
// https://leetcode.com/problems/remove-stones-to-minimize-the-total/

/**
 * @param {number[]} piles
 * @param {number} k
 * @return {number}
 */
var minStoneSum = function(piles, k) {
    const heap = piles.map((p) => -p);
    const siftUp = (i) => {
        while (i > 0) {
            const p = (i - 1) >> 1;
            if (heap[p] <= heap[i]) break;
            [heap[p], heap[i]] = [heap[i], heap[p]];
            i = p;
        }
    };
    const siftDown = (i) => {
        while (true) {
            let s = i;
            const l = 2 * i + 1, r = 2 * i + 2;
            if (l < heap.length && heap[l] < heap[s]) s = l;
            if (r < heap.length && heap[r] < heap[s]) s = r;
            if (s === i) break;
            [heap[s], heap[i]] = [heap[i], heap[s]];
            i = s;
        }
    };
    for (let i = (heap.length >> 1) - 1; i >= 0; i--) siftDown(i);
    for (let t = 0; t < k; t++) {
        const x = -heap[0];
        heap[0] = -(x - Math.floor(x / 2));
        siftDown(0);
    }
    return -heap.reduce((a, b) => a + b, 0);
};
''',
    "1963_minimum_number_of_swaps_to_make_the_string_balanced": r'''// LeetCode 1963 - Minimum Number of Swaps to Make the String Balanced
// https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/

/**
 * @param {string} s
 * @return {number}
 */
var minSwaps = function(s) {
    let bal = 0, mx = 0;
    for (const ch of s) {
        if (ch === "[") bal++;
        else bal--;
        mx = Math.min(mx, bal);
    }
    return Math.floor((-mx + 1) / 2);
};
''',
    "1964_find_the_longest_valid_obstacle_course_at_each_position": r'''// LeetCode 1964 - Find the Longest Valid Obstacle Course at Each Position
// https://leetcode.com/problems/find-the-longest-valid-obstacle-course-at-each-position/

/**
 * @param {number[]} obstacles
 * @return {number[]}
 */
var longestObstacleCourseAtEachPosition = function(obstacles) {
    const tails = [];
    const ans = [];
    for (const x of obstacles) {
        let lo = 0, hi = tails.length;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (tails[mid] <= x) lo = mid + 1;
            else hi = mid;
        }
        if (lo === tails.length) tails.push(x);
        else tails[lo] = x;
        ans.push(lo + 1);
    }
    return ans;
};
''',
    "1966_binary_searchable_numbers_in_an_unsorted_array": r'''// LeetCode 1966 - Binary Searchable Numbers in an Unsorted Array
// https://leetcode.com/problems/binary-searchable-numbers-in-an-unsorted-array/

/**
 * @param {number[]} nums
 * @return {number}
 */
var binarySearchableNumbers = function(nums) {
    const n = nums.length;
    const ok = new Array(n).fill(1);
    let mx = -Infinity, mi = Infinity;
    for (let i = 0; i < n; i++) {
        if (nums[i] < mx) ok[i] = 0;
        else mx = nums[i];
    }
    for (let i = n - 1; i >= 0; i--) {
        if (nums[i] > mi) ok[i] = 0;
        else mi = nums[i];
    }
    return ok.reduce((a, b) => a + b, 0);
};
''',
    "1967_number_of_strings_that_appear_as_substrings_in_word": r'''// LeetCode 1967 - Number of Strings That Appear as Substrings in Word
// https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/

/**
 * @param {string[]} patterns
 * @param {string} word
 * @return {number}
 */
var numOfStrings = function(patterns, word) {
    return patterns.filter((p) => word.includes(p)).length;
};
''',
    "1968_array_with_elements_not_equal_to_average_of_neighbors": r'''// LeetCode 1968 - Array With Elements Not Equal to Average of Neighbors
// https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors/

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var rearrangeArray = function(nums) {
    nums = nums.slice().sort((a, b) => a - b);
    const n = nums.length;
    const mid = Math.floor((n + 1) / 2);
    const small = nums.slice(0, mid), large = nums.slice(mid);
    const ans = [];
    let i = 0, j = 0;
    while (i < small.length || j < large.length) {
        if (i < small.length) ans.push(small[i++]);
        if (j < large.length) ans.push(large[j++]);
    }
    return ans;
};
''',
    "1969_minimum_non_zero_product_of_the_array_elements": r'''// LeetCode 1969 - Minimum Non-Zero Product of the Array Elements
// https://leetcode.com/problems/minimum-non-zero-product-of-the-array-elements/

/**
 * @param {number} p
 * @return {number}
 */
var minNonZeroProduct = function(p) {
    const MOD = 1000000007n;
    const mx = (1n << BigInt(p)) - 1n;
    const modPow = (base, exp) => {
        let r = 1n, b = base % MOD, e = exp;
        while (e > 0n) {
            if (e & 1n) r = r * b % MOD;
            b = b * b % MOD;
            e >>= 1n;
        }
        return r;
    };
    return Number(mx % MOD * modPow(mx - 1n, (1n << BigInt(p - 1)) - 1n) % MOD);
};
''',
}


def main() -> None:
    written = 0
    for folder, content in SOLUTIONS.items():
        if content.startswith("PLACEHOLDER"):
            print(f"skip placeholder {folder}")
            continue
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

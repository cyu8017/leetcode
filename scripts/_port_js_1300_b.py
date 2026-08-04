#!/usr/bin/env python3
"""Port JS solutions batch B (1342-1381)."""
from __future__ import annotations
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SOLUTIONS: dict[str, str] = {
    "1342_number_of_steps_to_reduce_a_number_to_zero": r'''// LeetCode 1342 - Number Of Steps To Reduce A Number To Zero
// https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

/**
 * @param {number} num
 * @return {number}
 */
var numberOfSteps = function(num) {
    let steps = 0;
    while (num) {
        num = num % 2 === 0 ? num / 2 : num - 1;
        steps++;
    }
    return steps;
};
''',
    "1343_number_of_sub_arrays_of_size_k_and_average_greater_than_or_equal_to_threshold": r'''// LeetCode 1343 - Number Of Sub Arrays Of Size K And Average Greater Than Or Equal To Threshold
// https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/

/**
 * @param {number[]} arr
 * @param {number} k
 * @param {number} threshold
 * @return {number}
 */
var numOfSubarrays = function(arr, k, threshold) {
    let window = 0;
    for (let i = 0; i < k; i++) window += arr[i];
    let answer = window >= k * threshold ? 1 : 0;
    for (let i = k; i < arr.length; i++) {
        window += arr[i] - arr[i - k];
        if (window >= k * threshold) answer++;
    }
    return answer;
};
''',
    "1344_angle_between_hands_of_a_clock": r'''// LeetCode 1344 - Angle Between Hands Of A Clock
// https://leetcode.com/problems/angle-between-hands-of-a-clock/

/**
 * @param {number} hour
 * @param {number} minutes
 * @return {number}
 */
var angleClock = function(hour, minutes) {
    const difference = Math.abs((hour % 12) * 30 + minutes * 0.5 - minutes * 6);
    return Math.min(difference, 360 - difference);
};
''',
    "1345_jump_game_iv": r'''// LeetCode 1345 - Jump Game Iv
// https://leetcode.com/problems/jump-game-iv/

/**
 * @param {number[]} arr
 * @return {number}
 */
var minJumps = function(arr) {
    const positions = new Map();
    for (let i = 0; i < arr.length; i++) {
        if (!positions.has(arr[i])) positions.set(arr[i], []);
        positions.get(arr[i]).push(i);
    }
    const queue = [0], seen = new Set([0]);
    let steps = 0;
    while (queue.length) {
        const size = queue.length;
        for (let s = 0; s < size; s++) {
            const i = queue.shift();
            if (i === arr.length - 1) return steps;
            const next = (positions.get(arr[i]) || []).concat([i - 1, i + 1]);
            positions.delete(arr[i]);
            for (const j of next) {
                if (j >= 0 && j < arr.length && !seen.has(j)) {
                    seen.add(j);
                    queue.push(j);
                }
            }
        }
        steps++;
    }
    return -1;
};
''',
    "1346_check_if_n_and_its_double_exist": r'''// LeetCode 1346 - Check If N And Its Double Exist
// https://leetcode.com/problems/check-if-n-and-its-double-exist/

/**
 * @param {number[]} arr
 * @return {boolean}
 */
var checkIfExist = function(arr) {
    const seen = new Set();
    for (const value of arr) {
        if (seen.has(2 * value) || (value % 2 === 0 && seen.has(value / 2))) return true;
        seen.add(value);
    }
    return false;
};
''',
    "1347_minimum_number_of_steps_to_make_two_strings_anagram": r'''// LeetCode 1347 - Minimum Number Of Steps To Make Two Strings Anagram
// https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/

/**
 * @param {string} s
 * @param {string} t
 * @return {number}
 */
var minSteps = function(s, t) {
    const count = Array(26).fill(0);
    for (let i = 0; i < s.length; i++) {
        count[s.charCodeAt(i) - 97]++;
        count[t.charCodeAt(i) - 97]--;
    }
    return count.reduce((sum, c) => sum + Math.max(c, 0), 0);
};
''',
    "1348_tweet_counts_per_frequency": r'''// LeetCode 1348 - Tweet Counts Per Frequency
// https://leetcode.com/problems/tweet-counts-per-frequency/

var TweetCounts = function() {
    this.times = new Map();
};

/** 
 * @param {string} tweetName 
 * @param {number} time
 * @return {void}
 */
TweetCounts.prototype.recordTweet = function(tweetName, time) {
    if (!this.times.has(tweetName)) this.times.set(tweetName, []);
    const arr = this.times.get(tweetName);
    let lo = 0, hi = arr.length;
    while (lo < hi) {
        const mid = (lo + hi) >> 1;
        if (arr[mid] < time) lo = mid + 1;
        else hi = mid;
    }
    arr.splice(lo, 0, time);
};

/** 
 * @param {string} freq 
 * @param {string} tweetName 
 * @param {number} startTime 
 * @param {number} endTime
 * @return {number[]}
 */
TweetCounts.prototype.getTweetCountsPerFrequency = function(freq, tweetName, startTime, endTime) {
    const size = { minute: 60, hour: 3600, day: 86400 }[freq];
    const times = this.times.get(tweetName) || [];
    const answer = [];
    const lower = (x) => {
        let lo = 0, hi = times.length;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (times[mid] < x) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    };
    const upper = (x) => {
        let lo = 0, hi = times.length;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (times[mid] <= x) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    };
    for (let start = startTime; start <= endTime; start += size) {
        const end = Math.min(endTime, start + size - 1);
        answer.push(upper(end) - lower(start));
    }
    return answer;
};
''',
    "1349_maximum_students_taking_exam": r'''// LeetCode 1349 - Maximum Students Taking Exam
// https://leetcode.com/problems/maximum-students-taking-exam/

/**
 * @param {character[][]} seats
 * @return {number}
 */
var maxStudents = function(seats) {
    const rows = seats.length, cols = seats[0].length;
    const validRows = seats.map((row) => {
        let available = 0;
        for (let c = 0; c < cols; c++) if (row[c] === ".") available |= 1 << c;
        const masks = [];
        for (let mask = 0; mask < (1 << cols); mask++) {
            if ((mask & ~available) === 0 && (mask & (mask << 1)) === 0) masks.push(mask);
        }
        return masks;
    });
    let dp = new Map([[0, 0]]);
    for (const masks of validRows) {
        const nxt = new Map();
        for (const mask of masks) {
            for (const [previous, count] of dp) {
                if ((mask & (previous << 1)) === 0 && (mask & (previous >> 1)) === 0) {
                    const bits = mask.toString(2).split("1").length - 1;
                    nxt.set(mask, Math.max(nxt.get(mask) || 0, count + bits));
                }
            }
        }
        dp = nxt;
    }
    return Math.max(...dp.values());
};
''',
    "1351_count_negative_numbers_in_a_sorted_matrix": r'''// LeetCode 1351 - Count Negative Numbers In A Sorted Matrix
// https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

/**
 * @param {number[][]} grid
 * @return {number}
 */
var countNegatives = function(grid) {
    let answer = 0;
    for (const row of grid) {
        let lo = 0, hi = row.length;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (row[mid] < 0) hi = mid;
            else lo = mid + 1;
        }
        answer += row.length - lo;
    }
    return answer;
};
''',
    "1352_product_of_the_last_k_numbers": r'''// LeetCode 1352 - Product Of The Last K Numbers
// https://leetcode.com/problems/product-of-the-last-k-numbers/

var ProductOfNumbers = function() {
    this.p = [1];
};

/** 
 * @param {number} num
 * @return {void}
 */
ProductOfNumbers.prototype.add = function(num) {
    if (num === 0) this.p = [1];
    else this.p.push(this.p[this.p.length - 1] * num);
};

/** 
 * @param {number} k
 * @return {number}
 */
ProductOfNumbers.prototype.getProduct = function(k) {
    if (k >= this.p.length) return 0;
    return this.p[this.p.length - 1] / this.p[this.p.length - 1 - k];
};
''',
    "1353_maximum_number_of_events_that_can_be_attended": r'''// LeetCode 1353 - Maximum Number Of Events That Can Be Attended
// https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/

/**
 * @param {number[][]} events
 * @return {number}
 */
var maxEvents = function(events) {
    events.sort((a, b) => a[0] - b[0]);
    const heap = [];
    const push = (x) => {
        heap.push(x);
        let i = heap.length - 1;
        while (i > 0) {
            const p = (i - 1) >> 1;
            if (heap[p] <= heap[i]) break;
            [heap[p], heap[i]] = [heap[i], heap[p]];
            i = p;
        }
    };
    const pop = () => {
        const top = heap[0];
        const last = heap.pop();
        if (heap.length) {
            heap[0] = last;
            let i = 0;
            while (true) {
                let s = i;
                const l = 2 * i + 1, r = 2 * i + 2;
                if (l < heap.length && heap[l] < heap[s]) s = l;
                if (r < heap.length && heap[r] < heap[s]) s = r;
                if (s === i) break;
                [heap[i], heap[s]] = [heap[s], heap[i]];
                i = s;
            }
        }
        return top;
    };
    let i = 0, ans = 0, day = 0;
    while (i < events.length || heap.length) {
        if (!heap.length) day = Math.max(day, events[i][0]);
        while (i < events.length && events[i][0] <= day) push(events[i++][1]);
        while (heap.length && heap[0] < day) pop();
        if (heap.length) {
            pop();
            ans++;
            day++;
        }
    }
    return ans;
};
''',
    "1354_construct_target_array_with_multiple_sums": r'''// LeetCode 1354 - Construct Target Array With Multiple Sums
// https://leetcode.com/problems/construct-target-array-with-multiple-sums/

/**
 * @param {number[]} target
 * @return {boolean}
 */
var isPossible = function(target) {
    if (target.length === 1) return target[0] === 1;
    const heap = [];
    const push = (x) => {
        heap.push(x);
        let i = heap.length - 1;
        while (i > 0) {
            const p = (i - 1) >> 1;
            if (heap[p] >= heap[i]) break;
            [heap[p], heap[i]] = [heap[i], heap[p]];
            i = p;
        }
    };
    const pop = () => {
        const top = heap[0];
        const last = heap.pop();
        if (heap.length) {
            heap[0] = last;
            let i = 0;
            while (true) {
                let s = i;
                const l = 2 * i + 1, r = 2 * i + 2;
                if (l < heap.length && heap[l] > heap[s]) s = l;
                if (r < heap.length && heap[r] > heap[s]) s = r;
                if (s === i) break;
                [heap[i], heap[s]] = [heap[s], heap[i]];
                i = s;
            }
        }
        return top;
    };
    let total = 0;
    for (const x of target) {
        total += x;
        push(x);
    }
    while (true) {
        const x = pop();
        const rest = total - x;
        if (x === 1 || rest === 1) return true;
        if (rest === 0 || x <= rest) return false;
        const prev = x % rest;
        if (prev === 0) return false;
        total = rest + prev;
        push(prev);
    }
};
''',
    "1356_sort_integers_by_the_number_of_1_bits": r'''// LeetCode 1356 - Sort Integers By The Number Of 1 Bits
// https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/

/**
 * @param {number[]} arr
 * @return {number[]}
 */
var sortByBits = function(arr) {
    const bitCount = (x) => {
        let c = 0;
        while (x) {
            c += x & 1;
            x >>= 1;
        }
        return c;
    };
    return [...arr].sort((a, b) => bitCount(a) - bitCount(b) || a - b);
};
''',
    "1357_apply_discount_every_n_orders": r'''// LeetCode 1357 - Apply Discount Every N Orders
// https://leetcode.com/problems/apply-discount-every-n-orders/

/**
 * @param {number} n
 * @param {number} discount
 * @param {number[]} products
 * @param {number[]} prices
 */
var Cashier = function(n, discount, products, prices) {
    this.n = n;
    this.discount = discount;
    this.price = new Map();
    for (let i = 0; i < products.length; i++) this.price.set(products[i], prices[i]);
    this.count = 0;
};

/** 
 * @param {number[]} product 
 * @param {number[]} amount
 * @return {number}
 */
Cashier.prototype.getBill = function(product, amount) {
    this.count++;
    let total = 0;
    for (let i = 0; i < product.length; i++) total += this.price.get(product[i]) * amount[i];
    return this.count % this.n === 0 ? total * (100 - this.discount) / 100 : total;
};
''',
    "1358_number_of_substrings_containing_all_three_characters": r'''// LeetCode 1358 - Number Of Substrings Containing All Three Characters
// https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/

/**
 * @param {string} s
 * @return {number}
 */
var numberOfSubstrings = function(s) {
    const last = [-1, -1, -1];
    let ans = 0;
    for (let i = 0; i < s.length; i++) {
        last[s.charCodeAt(i) - 97] = i;
        ans += Math.min(...last) + 1;
    }
    return ans;
};
''',
    "1359_count_all_valid_pickup_and_delivery_options": r'''// LeetCode 1359 - Count All Valid Pickup And Delivery Options
// https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/

/**
 * @param {number} n
 * @return {number}
 */
var countOrders = function(n) {
    let ans = 1;
    const mod = 1000000007;
    for (let i = 1; i <= n; i++) ans = ans * i * (2 * i - 1) % mod;
    return ans;
};
''',
    "1360_number_of_days_between_two_dates": r'''// LeetCode 1360 - Number Of Days Between Two Dates
// https://leetcode.com/problems/number-of-days-between-two-dates/

/**
 * @param {string} date1
 * @param {string} date2
 * @return {number}
 */
var daysBetweenDates = function(date1, date2) {
    const toDays = (s) => Math.floor(Date.parse(s + "T00:00:00Z") / 86400000);
    return Math.abs(toDays(date1) - toDays(date2));
};
''',
    "1361_validate_binary_tree_nodes": r'''// LeetCode 1361 - Validate Binary Tree Nodes
// https://leetcode.com/problems/validate-binary-tree-nodes/

/**
 * @param {number} n
 * @param {number[]} leftChild
 * @param {number[]} rightChild
 * @return {boolean}
 */
var validateBinaryTreeNodes = function(n, leftChild, rightChild) {
    const indeg = Array(n).fill(0);
    for (const x of leftChild.concat(rightChild)) {
        if (x !== -1) {
            indeg[x]++;
            if (indeg[x] > 1) return false;
        }
    }
    const roots = [];
    for (let i = 0; i < n; i++) if (indeg[i] === 0) roots.push(i);
    if (roots.length !== 1) return false;
    const seen = new Set();
    const st = [...roots];
    while (st.length) {
        const u = st.pop();
        if (seen.has(u)) return false;
        seen.add(u);
        for (const v of [leftChild[u], rightChild[u]]) if (v !== -1) st.push(v);
    }
    return seen.size === n;
};
''',
    "1362_closest_divisors": r'''// LeetCode 1362 - Closest Divisors
// https://leetcode.com/problems/closest-divisors/

/**
 * @param {number} num
 * @return {number[]}
 */
var closestDivisors = function(num) {
    let best = null;
    for (const x of [num + 1, num + 2]) {
        for (let a = Math.floor(Math.sqrt(x)); a >= 1; a--) {
            if (x % a === 0) {
                const pair = [a, x / a];
                if (!best || pair[1] - pair[0] < best[1] - best[0]) best = pair;
                break;
            }
        }
    }
    return best;
};
''',
    "1363_largest_multiple_of_three": r'''// LeetCode 1363 - Largest Multiple Of Three
// https://leetcode.com/problems/largest-multiple-of-three/

/**
 * @param {number[]} digits
 * @return {string}
 */
var largestMultipleOfThree = function(digits) {
    const cnt = Array(10).fill(0);
    let rem = 0;
    for (const d of digits) {
        cnt[d]++;
        rem += d;
    }
    rem %= 3;
    const remove = (r, k) => {
        for (let d = r; d < 10; d += 3) {
            while (cnt[d] && k) {
                cnt[d]--;
                k--;
            }
            if (!k) return true;
        }
        return false;
    };
    if (rem && !remove(rem, 1)) remove(3 - rem, 2);
    let s = "";
    for (let d = 9; d >= 0; d--) s += String(d).repeat(cnt[d]);
    return s && s[0] === "0" ? "0" : s;
};
''',
    "1365_how_many_numbers_are_smaller_than_the_current_number": r'''// LeetCode 1365 - How Many Numbers Are Smaller Than The Current Number
// https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var smallerNumbersThanCurrent = function(nums) {
    const sorted = [...nums].sort((a, b) => a - b);
    return nums.map((x) => sorted.indexOf(x));
};
''',
    "1366_rank_teams_by_votes": r'''// LeetCode 1366 - Rank Teams By Votes
// https://leetcode.com/problems/rank-teams-by-votes/

/**
 * @param {string[]} votes
 * @return {string}
 */
var rankTeams = function(votes) {
    const m = votes[0].length;
    const count = new Map();
    for (const c of votes[0]) count.set(c, Array(m).fill(0));
    for (const v of votes) {
        for (let i = 0; i < v.length; i++) count.get(v[i])[i]++;
    }
    return [...count.keys()].sort((a, b) => {
        const ca = count.get(a), cb = count.get(b);
        for (let i = 0; i < m; i++) if (ca[i] !== cb[i]) return cb[i] - ca[i];
        return a < b ? -1 : a > b ? 1 : 0;
    }).join("");
};
''',
    "1367_linked_list_in_binary_tree": r'''// LeetCode 1367 - Linked List In Binary Tree
// https://leetcode.com/problems/linked-list-in-binary-tree/

/**
 * @param {ListNode} head
 * @param {TreeNode} root
 * @return {boolean}
 */
var isSubPath = function(head, root) {
    const match = (a, b) => !a || Boolean(b && a.val === b.val && (match(a.next, b.left) || match(a.next, b.right)));
    return Boolean(root && (match(head, root) || isSubPath(head, root.left) || isSubPath(head, root.right)));
};
''',
    "1368_minimum_cost_to_make_at_least_one_valid_path_in_a_grid": r'''// LeetCode 1368 - Minimum Cost To Make At Least One Valid Path In A Grid
// https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/

/**
 * @param {number[][]} grid
 * @return {number}
 */
var minCost = function(grid) {
    const m = grid.length, n = grid[0].length;
    const dist = Array.from({ length: m }, () => Array(n).fill(1e9));
    dist[0][0] = 0;
    const q = [[0, 0]];
    const dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]];
    while (q.length) {
        const [r, c] = q.shift();
        for (let k = 0; k < 4; k++) {
            const [dr, dc] = dirs[k];
            const x = r + dr, y = c + dc;
            if (x >= 0 && x < m && y >= 0 && y < n) {
                const w = (k + 1) !== grid[r][c] ? 1 : 0;
                const nd = dist[r][c] + w;
                if (nd < dist[x][y]) {
                    dist[x][y] = nd;
                    if (w) q.push([x, y]);
                    else q.unshift([x, y]);
                }
            }
        }
    }
    return dist[m - 1][n - 1];
};
''',
    "1370_increasing_decreasing_string": r'''// LeetCode 1370 - Increasing Decreasing String
// https://leetcode.com/problems/increasing-decreasing-string/

/**
 * @param {string} s
 * @return {string}
 */
var sortString = function(s) {
    const c = Array(26).fill(0);
    for (const ch of s) c[ch.charCodeAt(0) - 97]++;
    const out = [];
    while (out.length < s.length) {
        for (let i = 0; i < 26; i++) if (c[i]) { out.push(String.fromCharCode(97 + i)); c[i]--; }
        for (let i = 25; i >= 0; i--) if (c[i]) { out.push(String.fromCharCode(97 + i)); c[i]--; }
    }
    return out.join("");
};
''',
    "1371_find_the_longest_substring_containing_vowels_in_even_counts": r'''// LeetCode 1371 - Find The Longest Substring Containing Vowels In Even Counts
// https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/

/**
 * @param {string} s
 * @return {number}
 */
var findTheLongestSubstring = function(s) {
    const first = new Map([[0, -1]]);
    let mask = 0, ans = 0;
    const vowels = "aeiou";
    for (let i = 0; i < s.length; i++) {
        const idx = vowels.indexOf(s[i]);
        if (idx >= 0) mask ^= 1 << idx;
        if (first.has(mask)) ans = Math.max(ans, i - first.get(mask));
        else first.set(mask, i);
    }
    return ans;
};
''',
    "1372_longest_zigzag_path_in_a_binary_tree": r'''// LeetCode 1372 - Longest Zigzag Path In A Binary Tree
// https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/

/**
 * @param {TreeNode} root
 * @return {number}
 */
var longestZigZag = function(root) {
    let ans = 0;
    const dfs = (node) => {
        if (!node) return [-1, -1];
        const l = dfs(node.left), r = dfs(node.right);
        const a = l[1] + 1, b = r[0] + 1;
        ans = Math.max(ans, a, b);
        return [a, b];
    };
    dfs(root);
    return ans;
};
''',
    "1373_maximum_sum_bst_in_binary_tree": r'''// LeetCode 1373 - Maximum Sum Bst In Binary Tree
// https://leetcode.com/problems/maximum-sum-bst-in-binary-tree/

/**
 * @param {TreeNode} root
 * @return {number}
 */
var maxSumBST = function(root) {
    let ans = 0;
    const dfs = (node) => {
        if (!node) return [true, Infinity, -Infinity, 0];
        const [a, lx, lh, ls] = dfs(node.left);
        const [b, rx, rh, rs] = dfs(node.right);
        if (a && b && lh < node.val && node.val < rx) {
            const s = ls + rs + node.val;
            ans = Math.max(ans, s);
            return [true, Math.min(lx, node.val), Math.max(rh, node.val), s];
        }
        return [false, 0, 0, 0];
    };
    dfs(root);
    return ans;
};
''',
    "1374_generate_a_string_with_characters_that_have_odd_counts": r'''// LeetCode 1374 - Generate A String With Characters That Have Odd Counts
// https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts/

/**
 * @param {number} n
 * @return {string}
 */
var generateTheString = function(n) {
    return n % 2 ? "a".repeat(n) : "a".repeat(n - 1) + "b";
};
''',
    "1375_number_of_times_binary_string_is_prefix_aligned": r'''// LeetCode 1375 - Number Of Times Binary String Is Prefix Aligned
// https://leetcode.com/problems/number-of-times-binary-string-is-prefix-aligned/

/**
 * @param {number[]} flips
 * @return {number}
 */
var numTimesAllBlue = function(flips) {
    let ans = 0, mx = 0;
    for (let i = 0; i < flips.length; i++) {
        mx = Math.max(mx, flips[i]);
        if (mx === i + 1) ans++;
    }
    return ans;
};
''',
    "1376_time_needed_to_inform_all_employees": r'''// LeetCode 1376 - Time Needed To Inform All Employees
// https://leetcode.com/problems/time-needed-to-inform-all-employees/

/**
 * @param {number} n
 * @param {number} headID
 * @param {number[]} manager
 * @param {number[]} informTime
 * @return {number}
 */
var numOfMinutes = function(n, headID, manager, informTime) {
    const children = Array.from({ length: n }, () => []);
    for (let i = 0; i < n; i++) if (manager[i] !== -1) children[manager[i]].push(i);
    const dfs = (u) => {
        let best = 0;
        for (const v of children[u]) best = Math.max(best, dfs(v));
        return informTime[u] + best;
    };
    return dfs(headID);
};
''',
    "1377_frog_position_after_t_seconds": r'''// LeetCode 1377 - Frog Position After T Seconds
// https://leetcode.com/problems/frog-position-after-t-seconds/

/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {number} t
 * @param {number} target
 * @return {number}
 */
var frogPosition = function(n, edges, t, target) {
    const g = Array.from({ length: n + 1 }, () => []);
    for (const [a, b] of edges) {
        g[a].push(b);
        g[b].push(a);
    }
    const dfs = (u, p, time, prob) => {
        const kids = g[u].filter((v) => v !== p);
        if (time === t || !kids.length) return u === target ? prob : 0;
        let sum = 0;
        for (const v of kids) sum += dfs(v, u, time + 1, prob / kids.length);
        return sum;
    };
    return dfs(1, 0, 0, 1.0);
};
''',
    "1379_find_a_corresponding_node_of_a_binary_tree_in_a_clone_of_that_tree": r'''// LeetCode 1379 - Find A Corresponding Node Of A Binary Tree In A Clone Of That Tree
// https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/

/**
 * @param {TreeNode} original
 * @param {TreeNode} cloned
 * @param {TreeNode} target
 * @return {TreeNode}
 */
var getTargetCopy = function(original, cloned, target) {
    const wanted = typeof target === "number" ? target : target.val;
    const stack = [[original, cloned]];
    while (stack.length) {
        const [a, b] = stack.pop();
        if (a.val === wanted) return typeof target === "number" ? b.val : b;
        if (a.left) stack.push([a.left, b.left]);
        if (a.right) stack.push([a.right, b.right]);
    }
};
''',
    "1380_lucky_numbers_in_a_matrix": r'''// LeetCode 1380 - Lucky Numbers In A Matrix
// https://leetcode.com/problems/lucky-numbers-in-a-matrix/

/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
var luckyNumbers = function(matrix) {
    const mins = new Set(matrix.map((r) => Math.min(...r)));
    const cols = matrix[0].length;
    const maxs = new Set();
    for (let c = 0; c < cols; c++) {
        let mx = -Infinity;
        for (let r = 0; r < matrix.length; r++) mx = Math.max(mx, matrix[r][c]);
        maxs.add(mx);
    }
    return [...mins].filter((x) => maxs.has(x));
};
''',
    "1381_design_a_stack_with_increment_operation": r'''// LeetCode 1381 - Design A Stack With Increment Operation
// https://leetcode.com/problems/design-a-stack-with-increment-operation/

/**
 * @param {number} maxSize
 */
var CustomStack = function(maxSize) {
    this.maxSize = maxSize;
    this.a = [];
};

/** 
 * @param {number} x
 * @return {void}
 */
CustomStack.prototype.push = function(x) {
    if (this.a.length < this.maxSize) this.a.push(x);
};

/**
 * @return {number}
 */
CustomStack.prototype.pop = function() {
    return this.a.length ? this.a.pop() : -1;
};

/** 
 * @param {number} k 
 * @param {number} val
 * @return {void}
 */
CustomStack.prototype.increment = function(k, val) {
    for (let i = 0; i < Math.min(k, this.a.length); i++) this.a[i] += val;
};
''',
}


def main() -> None:
    written = 0
    for folder, content in SOLUTIONS.items():
        path = os.path.join(ROOT, folder, "solution.js")
        with open(path, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(content)
        written += 1
        print(f"wrote {folder}")
    print(f"done: {written}")


if __name__ == "__main__":
    main()

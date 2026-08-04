#!/usr/bin/env python3
"""Port JS solutions for LeetCode stubs 1700 + 1901-1945 (non-SQL)."""
from __future__ import annotations

import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SOLUTIONS: dict[str, str] = {
    "1700_number_of_students_unable_to_eat_lunch": r'''// LeetCode 1700 - Number of Students Unable to Eat Lunch
// https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/

/**
 * @param {number[]} students
 * @param {number[]} sandwiches
 * @return {number}
 */
var countStudents = function(students, sandwiches) {
    const c = new Map();
    for (const x of students) c.set(x, (c.get(x) || 0) + 1);
    for (let i = 0; i < sandwiches.length; i++) {
        const x = sandwiches[i];
        if (!c.get(x)) return students.length - i;
        c.set(x, c.get(x) - 1);
    }
    return 0;
};
''',
    "1901_find_a_peak_element_ii": r'''// LeetCode 1901 - Find a Peak Element II
// https://leetcode.com/problems/find-a-peak-element-ii/

/**
 * @param {number[][]} mat
 * @return {number[]}
 */
var findPeakGrid = function(mat) {
    const rows = mat.length, cols = mat[0].length;
    let lo = 0, hi = cols - 1;
    while (lo <= hi) {
        const mid = (lo + hi) >> 1;
        let maxRow = 0;
        for (let r = 1; r < rows; r++) {
            if (mat[r][mid] > mat[maxRow][mid]) maxRow = r;
        }
        const left = mid ? mat[maxRow][mid - 1] : -1;
        const right = mid + 1 < cols ? mat[maxRow][mid + 1] : -1;
        if (mat[maxRow][mid] >= left && mat[maxRow][mid] >= right) return [maxRow, mid];
        if (left > mat[maxRow][mid]) hi = mid - 1;
        else lo = mid + 1;
    }
    return [0, 0];
};
''',
    "1902_depth_of_bst_given_insertion_order": r'''// LeetCode 1902 - Depth of BST Given Insertion Order
// https://leetcode.com/problems/depth-of-bst-given-insertion-order/

/**
 * @param {number[]} order
 * @return {number}
 */
var maxDepthBST = function(order) {
    const nodes = [];
    let ans = 0;
    for (const value of order) {
        let lo = 0, hi = nodes.length;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (nodes[mid][0] < value) lo = mid + 1;
            else hi = mid;
        }
        const i = lo;
        let depth = 1;
        if (i) depth = Math.max(depth, nodes[i - 1][1] + 1);
        if (i < nodes.length) depth = Math.max(depth, nodes[i][1] + 1);
        nodes.splice(i, 0, [value, depth]);
        ans = Math.max(ans, depth);
    }
    return ans;
};
''',
    "1903_largest_odd_number_in_string": r'''// LeetCode 1903 - Largest Odd Number in String
// https://leetcode.com/problems/largest-odd-number-in-string/

/**
 * @param {string} num
 * @return {string}
 */
var largestOddNumber = function(num) {
    for (let i = num.length - 1; i >= 0; i--) {
        if ((num.charCodeAt(i) - 48) % 2) return num.slice(0, i + 1);
    }
    return "";
};
''',
    "1904_the_number_of_full_rounds_you_have_played": r'''// LeetCode 1904 - The Number of Full Rounds You Have Played
// https://leetcode.com/problems/the-number-of-full-rounds-you-have-played/

/**
 * @param {string} loginTime
 * @param {string} logoutTime
 * @return {number}
 */
var numberOfRounds = function(loginTime, logoutTime) {
    const toMin = (t) => {
        const [h, m] = t.split(":").map(Number);
        return h * 60 + m;
    };
    let start = toMin(loginTime), end = toMin(logoutTime);
    if (end < start) end += 24 * 60;
    start = Math.floor((start + 14) / 15) * 15;
    end = Math.floor(end / 15) * 15;
    return Math.max(0, Math.floor((end - start) / 15));
};
''',
    "1905_count_sub_islands": r'''// LeetCode 1905 - Count Sub Islands
// https://leetcode.com/problems/count-sub-islands/

/**
 * @param {number[][]} grid1
 * @param {number[][]} grid2
 * @return {number}
 */
var countSubIslands = function(grid1, grid2) {
    const rows = grid2.length, cols = grid2[0].length;
    const dfs = (r, c) => {
        if (r < 0 || c < 0 || r >= rows || c >= cols || grid2[r][c] === 0) return true;
        grid2[r][c] = 0;
        let ok = grid1[r][c] === 1;
        for (const [nr, nc] of [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]) {
            if (!dfs(nr, nc)) ok = false;
        }
        return ok;
    };
    let ans = 0;
    for (let r = 0; r < rows; r++) {
        for (let c = 0; c < cols; c++) {
            if (grid2[r][c] === 1 && dfs(r, c)) ans++;
        }
    }
    return ans;
};
''',
    "1906_minimum_absolute_difference_queries": r'''// LeetCode 1906 - Minimum Absolute Difference Queries
// https://leetcode.com/problems/minimum-absolute-difference-queries/

/**
 * @param {number[]} nums
 * @param {number[][]} queries
 * @return {number[]}
 */
var minDifference = function(nums, queries) {
    const n = nums.length;
    const pref = Array.from({ length: n + 1 }, () => new Array(101).fill(0));
    for (let i = 0; i < n; i++) {
        for (let v = 0; v < 101; v++) pref[i + 1][v] = pref[i][v];
        pref[i + 1][nums[i]]++;
    }
    const ans = [];
    for (const [left, right] of queries) {
        let prev = -1, best = Infinity;
        for (let value = 1; value <= 100; value++) {
            if (pref[right + 1][value] - pref[left][value] > 0) {
                if (prev !== -1) best = Math.min(best, value - prev);
                prev = value;
            }
        }
        ans.push(best === Infinity ? -1 : best);
    }
    return ans;
};
''',
    "1908_game_of_nim": r'''// LeetCode 1908 - Game of Nim
// https://leetcode.com/problems/game-of-nim/

/**
 * @param {number[]} piles
 * @return {boolean}
 */
var nimGame = function(piles) {
    let x = 0;
    for (const p of piles) x ^= p;
    return x !== 0;
};
''',
    "1909_remove_one_element_to_make_the_array_strictly_increasing": r'''// LeetCode 1909 - Remove One Element to Make the Array Strictly Increasing
// https://leetcode.com/problems/remove-one-element-to-make-the-array-strictly-increasing/

/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canBeIncreasing = function(nums) {
    const check = (skip) => {
        let prev = null;
        for (let i = 0; i < nums.length; i++) {
            if (i === skip) continue;
            if (prev !== null && nums[i] <= prev) return false;
            prev = nums[i];
        }
        return true;
    };
    for (let i = 1; i < nums.length; i++) {
        if (nums[i] <= nums[i - 1]) return check(i - 1) || check(i);
    }
    return true;
};
''',
    "1910_remove_all_occurrences_of_a_substring": r'''// LeetCode 1910 - Remove All Occurrences of a Substring
// https://leetcode.com/problems/remove-all-occurrences-of-a-substring/

/**
 * @param {string} s
 * @param {string} part
 * @return {string}
 */
var removeOccurrences = function(s, part) {
    const stack = [];
    const m = part.length;
    for (const ch of s) {
        stack.push(ch);
        if (stack.length >= m && stack.slice(-m).join("") === part) stack.length -= m;
    }
    return stack.join("");
};
''',
    "1911_maximum_alternating_subsequence_sum": r'''// LeetCode 1911 - Maximum Alternating Subsequence Sum
// https://leetcode.com/problems/maximum-alternating-subsequence-sum/

/**
 * @param {number[]} nums
 * @return {number}
 */
var maxAlternatingSum = function(nums) {
    let even = 0, odd = 0;
    for (const x of nums) {
        const ne = Math.max(even, odd + x);
        const no = Math.max(odd, even - x);
        even = ne;
        odd = no;
    }
    return even;
};
''',
    "1912_design_movie_rental_system": r'''// LeetCode 1912 - Design Movie Rental System
// https://leetcode.com/problems/design-movie-rental-system/

class MovieRentingSystem {
    /**
     * @param {number} n
     * @param {number[][]} entries
     */
    constructor(n, entries) {
        this.price = new Map();
        this.available = new Map();
        this.rented = [];
        for (const [shop, movie, price] of entries) {
            this.price.set(`${shop},${movie}`, price);
            if (!this.available.has(movie)) this.available.set(movie, []);
            this._insort(this.available.get(movie), [price, shop], (a, b) => a[0] - b[0] || a[1] - b[1]);
        }
    }

    _insort(arr, item, cmp) {
        let lo = 0, hi = arr.length;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (cmp(arr[mid], item) < 0) lo = mid + 1;
            else hi = mid;
        }
        arr.splice(lo, 0, item);
    }

    _remove(arr, item, eq) {
        const i = arr.findIndex((x) => eq(x, item));
        if (i >= 0) arr.splice(i, 1);
    }

    /**
     * @param {number} movie
     * @return {number[]}
     */
    search(movie) {
        return (this.available.get(movie) || []).slice(0, 5).map((x) => x[1]);
    }

    /**
     * @param {number} shop
     * @param {number} movie
     * @return {void}
     */
    rent(shop, movie) {
        const price = this.price.get(`${shop},${movie}`);
        this._remove(this.available.get(movie), [price, shop], (a, b) => a[0] === b[0] && a[1] === b[1]);
        this._insort(this.rented, [price, shop, movie], (a, b) => a[0] - b[0] || a[1] - b[1] || a[2] - b[2]);
    }

    /**
     * @param {number} shop
     * @param {number} movie
     * @return {void}
     */
    drop(shop, movie) {
        const price = this.price.get(`${shop},${movie}`);
        this._remove(this.rented, [price, shop, movie], (a, b) => a[0] === b[0] && a[1] === b[1] && a[2] === b[2]);
        this._insort(this.available.get(movie), [price, shop], (a, b) => a[0] - b[0] || a[1] - b[1]);
    }

    /**
     * @return {number[][]}
     */
    report() {
        return this.rented.slice(0, 5).map((x) => [x[1], x[2]]);
    }
}

module.exports = { MovieRentingSystem };
'''
    "1913_maximum_product_difference_between_two_pairs": r'''// LeetCode 1913 - Maximum Product Difference Between Two Pairs
// https://leetcode.com/problems/maximum-product-difference-between-two-pairs/

/**
 * @param {number[]} nums
 * @return {number}
 */
var maxProductDifference = function(nums) {
    let a = 0, b = 0, c = 1e5, d = 1e5;
    for (const x of nums) {
        if (x > a) { b = a; a = x; }
        else if (x > b) b = x;
        if (x < c) { d = c; c = x; }
        else if (x < d) d = x;
    }
    return a * b - c * d;
};
''',
    "1914_cyclically_rotating_a_grid": r'''// LeetCode 1914 - Cyclically Rotating a Grid
// https://leetcode.com/problems/cyclically-rotating-a-grid/

/**
 * @param {number[][]} grid
 * @param {number} k
 * @return {number[][]}
 */
var rotateGrid = function(grid, k) {
    const m = grid.length, n = grid[0].length;
    const layers = Math.floor(Math.min(m, n) / 2);
    for (let layer = 0; layer < layers; layer++) {
        const vals = [];
        for (let c = layer; c < n - layer; c++) vals.push(grid[layer][c]);
        for (let r = layer + 1; r < m - layer; r++) vals.push(grid[r][n - layer - 1]);
        if (m - 2 * layer > 1) {
            for (let c = n - layer - 2; c >= layer; c--) vals.push(grid[m - layer - 1][c]);
        }
        if (n - 2 * layer > 1) {
            for (let r = m - layer - 2; r > layer; r--) vals.push(grid[r][layer]);
        }
        const shift = k % vals.length;
        const rotated = vals.slice(shift).concat(vals.slice(0, shift));
        let idx = 0;
        for (let c = layer; c < n - layer; c++) grid[layer][c] = rotated[idx++];
        for (let r = layer + 1; r < m - layer; r++) grid[r][n - layer - 1] = rotated[idx++];
        if (m - 2 * layer > 1) {
            for (let c = n - layer - 2; c >= layer; c--) grid[m - layer - 1][c] = rotated[idx++];
        }
        if (n - 2 * layer > 1) {
            for (let r = m - layer - 2; r > layer; r--) grid[r][layer] = rotated[idx++];
        }
    }
    return grid;
};
''',
    "1915_number_of_wonderful_substrings": r'''// LeetCode 1915 - Number of Wonderful Substrings
// https://leetcode.com/problems/number-of-wonderful-substrings/

/**
 * @param {string} word
 * @return {number}
 */
var wonderfulSubstrings = function(word) {
    const count = new Array(1024).fill(0);
    count[0] = 1;
    let mask = 0, ans = 0;
    for (const ch of word) {
        mask ^= 1 << (ch.charCodeAt(0) - 97);
        ans += count[mask];
        for (let bit = 0; bit < 10; bit++) ans += count[mask ^ (1 << bit)];
        count[mask]++;
    }
    return ans;
};
''',
    "1916_count_ways_to_build_rooms_in_an_ant_colony": r'''// LeetCode 1916 - Count Ways to Build Rooms in an Ant Colony
// https://leetcode.com/problems/count-ways-to-build-rooms-in-an-ant-colony/

/**
 * @param {number[]} prevRoom
 * @return {number}
 */
var waysToBuildRooms = function(prevRoom) {
    const MOD = 1000000007;
    const n = prevRoom.length;
    const children = Array.from({ length: n }, () => []);
    for (let room = 0; room < n; room++) {
        if (prevRoom[room] !== -1) children[prevRoom[room]].push(room);
    }
    const fact = new Array(n + 1).fill(1);
    const invFact = new Array(n + 1).fill(1);
    for (let i = 1; i <= n; i++) fact[i] = fact[i - 1] * i % MOD;
    const modPow = (a, e) => {
        let r = 1n, base = BigInt(a), exp = BigInt(e), mod = BigInt(MOD);
        while (exp > 0n) {
            if (exp & 1n) r = r * base % mod;
            base = base * base % mod;
            exp >>= 1n;
        }
        return Number(r);
    };
    invFact[n] = modPow(fact[n], MOD - 2);
    for (let i = n; i > 0; i--) invFact[i - 1] = invFact[i] * i % MOD;
    const comb = (a, b) => fact[a] * invFact[b] % MOD * invFact[a - b] % MOD;
    const dfs = (node) => {
        let size = 0, ways = 1;
        for (const child of children[node]) {
            const [childSize, childWays] = dfs(child);
            ways = ways * childWays % MOD * comb(size + childSize, childSize) % MOD;
            size += childSize;
        }
        return [size + 1, ways];
    };
    return dfs(0)[1];
};
''',
    "1918_kth_smallest_subarray_sum": r'''// LeetCode 1918 - Kth Smallest Subarray Sum
// https://leetcode.com/problems/kth-smallest-subarray-sum/

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var kthSmallestSubarraySum = function(nums, k) {
    const count = (limit) => {
        let total = 0, left = 0, ans = 0;
        for (let right = 0; right < nums.length; right++) {
            total += nums[right];
            while (total > limit) total -= nums[left++];
            ans += right - left + 1;
        }
        return ans;
    };
    let lo = Math.min(...nums), hi = nums.reduce((a, b) => a + b, 0);
    while (lo < hi) {
        const mid = Math.floor((lo + hi) / 2);
        if (count(mid) >= k) hi = mid;
        else lo = mid + 1;
    }
    return lo;
};
''',
    "1920_build_array_from_permutation": r'''// LeetCode 1920 - Build Array from Permutation
// https://leetcode.com/problems/build-array-from-permutation/

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var buildArray = function(nums) {
    return nums.map((x) => nums[x]);
};
''',
    "1921_eliminate_maximum_number_of_monsters": r'''// LeetCode 1921 - Eliminate Maximum Number of Monsters
// https://leetcode.com/problems/eliminate-maximum-number-of-monsters/

/**
 * @param {number[]} dist
 * @param {number[]} speed
 * @return {number}
 */
var eliminateMaximum = function(dist, speed) {
    const arrival = dist.map((d, i) => Math.ceil(d / speed[i])).sort((a, b) => a - b);
    for (let i = 0; i < arrival.length; i++) {
        if (arrival[i] <= i) return i;
    }
    return arrival.length;
};
''',
    "1922_count_good_numbers": r'''// LeetCode 1922 - Count Good Numbers
// https://leetcode.com/problems/count-good-numbers/

/**
 * @param {number} n
 * @return {number}
 */
var countGoodNumbers = function(n) {
    const MOD = 1000000007n;
    const modPow = (base, exp) => {
        let r = 1n, b = BigInt(base), e = BigInt(exp);
        while (e > 0n) {
            if (e & 1n) r = r * b % MOD;
            b = b * b % MOD;
            e >>= 1n;
        }
        return r;
    };
    const nn = BigInt(n);
    return Number(modPow(5, (nn + 1n) / 2n) * modPow(4, nn / 2n) % MOD);
};
''',
    "1923_longest_common_subpath": r'''// LeetCode 1923 - Longest Common Subpath
// https://leetcode.com/problems/longest-common-subpath/

/**
 * @param {number} n
 * @param {number[][]} paths
 * @return {number}
 */
var longestCommonSubpath = function(n, paths) {
    const BASE1 = 911382323n, MOD1 = 1000000007n;
    const BASE2 = 972663749n, MOD2 = 1000000009n;
    const modPow = (base, exp, mod) => {
        let r = 1n, b = base, e = BigInt(exp);
        while (e > 0n) {
            if (e & 1n) r = r * b % mod;
            b = b * b % mod;
            e >>= 1n;
        }
        return r;
    };
    const hasCommon = (length) => {
        if (length === 0) return true;
        let common = null;
        const pow1 = modPow(BASE1, length, MOD1);
        const pow2 = modPow(BASE2, length, MOD2);
        for (const path of paths) {
            if (path.length < length) return false;
            let h1 = 0n, h2 = 0n;
            const seen = new Set();
            for (let i = 0; i < path.length; i++) {
                h1 = (h1 * BASE1 + BigInt(path[i] + 1)) % MOD1;
                h2 = (h2 * BASE2 + BigInt(path[i] + 1)) % MOD2;
                if (i >= length) {
                    h1 = (h1 - BigInt(path[i - length] + 1) * pow1 % MOD1 + MOD1) % MOD1;
                    h2 = (h2 - BigInt(path[i - length] + 1) * pow2 % MOD2 + MOD2) % MOD2;
                }
                if (i >= length - 1) seen.add(`${h1},${h2}`);
            }
            if (common === null) common = seen;
            else {
                const next = new Set();
                for (const x of common) if (seen.has(x)) next.add(x);
                common = next;
            }
            if (!common.size) return false;
        }
        return true;
    };
    let lo = 0, hi = Math.min(...paths.map((p) => p.length));
    while (lo < hi) {
        const mid = Math.floor((lo + hi + 1) / 2);
        if (hasCommon(mid)) lo = mid;
        else hi = mid - 1;
    }
    return lo;
};
''',
    "1924_erect_the_fence_ii": r'''// LeetCode 1924 - Erect the Fence II
// https://leetcode.com/problems/erect-the-fence-ii/

/**
 * @param {number[][]} trees
 * @return {number[]}
 */
var outerTrees = function(trees) {
    const pts = trees.map((p) => [p[0], p[1]]);
    for (let i = pts.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [pts[i], pts[j]] = [pts[j], pts[i]];
    }
    const dist = (a, b) => Math.hypot(a[0] - b[0], a[1] - b[1]);
    const circle2 = (a, b) => {
        const c = [(a[0] + b[0]) / 2, (a[1] + b[1]) / 2];
        return [c, dist(a, b) / 2];
    };
    const circle3 = (a, b, c) => {
        const [ax, ay] = a, [bx, by] = b, [cx, cy] = c;
        const d = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by));
        if (Math.abs(d) < 1e-12) {
            const candidates = [circle2(a, b), circle2(a, c), circle2(b, c)];
            return candidates.reduce((best, cur) => (cur[1] < best[1] ? cur : best));
        }
        const ux = ((ax * ax + ay * ay) * (by - cy) + (bx * bx + by * by) * (cy - ay) + (cx * cx + cy * cy) * (ay - by)) / d;
        const uy = ((ax * ax + ay * ay) * (cx - bx) + (bx * bx + by * by) * (ax - cx) + (cx * cx + cy * cy) * (bx - ax)) / d;
        const center = [ux, uy];
        return [center, dist(center, a)];
    };
    const inside = (cir, p) => cir && dist(cir[0], p) <= cir[1] + 1e-9;
    let circle = null;
    for (let i = 0; i < pts.length; i++) {
        const p = pts[i];
        if (!circle || !inside(circle, p)) {
            circle = [p, 0.0];
            for (let j = 0; j < i; j++) {
                const q = pts[j];
                if (!inside(circle, q)) {
                    circle = circle2(p, q);
                    for (let k = 0; k < j; k++) {
                        const r = pts[k];
                        if (!inside(circle, r)) circle = circle3(p, q, r);
                    }
                }
            }
        }
    }
    return [circle[0][0], circle[0][1], circle[1]];
};
''',
    "1925_count_square_sum_triples": r'''// LeetCode 1925 - Count Square Sum Triples
// https://leetcode.com/problems/count-square-sum-triples/

/**
 * @param {number} n
 * @return {number}
 */
var countTriples = function(n) {
    const squares = new Set();
    for (let i = 1; i <= n; i++) squares.add(i * i);
    let ans = 0;
    for (let a = 1; a <= n; a++) {
        for (let b = 1; b <= n; b++) {
            if (squares.has(a * a + b * b)) ans++;
        }
    }
    return ans;
};
''',
    "1926_nearest_exit_from_entrance_in_maze": r'''// LeetCode 1926 - Nearest Exit from Entrance in Maze
// https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/

/**
 * @param {character[][]} maze
 * @param {number[]} entrance
 * @return {number}
 */
var nearestExit = function(maze, entrance) {
    const m = maze.length, n = maze[0].length;
    const [er, ec] = entrance;
    const q = [[er, ec, 0]];
    maze[er][ec] = "+";
    for (let qi = 0; qi < q.length; qi++) {
        const [r, c, d] = q[qi];
        for (const [nr, nc] of [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]) {
            if (nr >= 0 && nr < m && nc >= 0 && nc < n && maze[nr][nc] === ".") {
                if (nr === 0 || nr === m - 1 || nc === 0 || nc === n - 1) return d + 1;
                maze[nr][nc] = "+";
                q.push([nr, nc, d + 1]);
            }
        }
    }
    return -1;
};
''',
    "1927_sum_game": r'''// LeetCode 1927 - Sum Game
// https://leetcode.com/problems/sum-game/

/**
 * @param {string} num
 * @return {boolean}
 */
var sumGame = function(num) {
    const half = num.length >> 1;
    const score = (s) => {
        let q = 0, dig = 0;
        for (const c of s) {
            if (c === "?") q++;
            else dig += c.charCodeAt(0) - 48;
        }
        return dig * 2 + q * 9;
    };
    return score(num.slice(0, half)) !== score(num.slice(half));
};
''',
    "1928_minimum_cost_to_reach_destination_in_time": r'''// LeetCode 1928 - Minimum Cost to Reach Destination in Time
// https://leetcode.com/problems/minimum-cost-to-reach-destination-in-time/

/**
 * @param {number} maxTime
 * @param {number[][]} edges
 * @param {number[]} passingFee
 * @return {number}
 */
var minCost = function(maxTime, edges, passingFee) {
    const n = passingFee.length;
    const graph = Array.from({ length: n }, () => []);
    for (const [u, v, t] of edges) {
        graph[u].push([v, t]);
        graph[v].push([u, t]);
    }
    const minTime = new Array(n).fill(maxTime + 1);
    const pq = [[passingFee[0], 0, 0]];
    const push = (item) => {
        pq.push(item);
        let i = pq.length - 1;
        while (i > 0) {
            const p = (i - 1) >> 1;
            if (pq[p][0] <= pq[i][0]) break;
            [pq[p], pq[i]] = [pq[i], pq[p]];
            i = p;
        }
    };
    const pop = () => {
        const top = pq[0];
        const last = pq.pop();
        if (!pq.length) return top;
        pq[0] = last;
        let i = 0;
        while (true) {
            let smallest = i;
            const l = 2 * i + 1, r = 2 * i + 2;
            if (l < pq.length && pq[l][0] < pq[smallest][0]) smallest = l;
            if (r < pq.length && pq[r][0] < pq[smallest][0]) smallest = r;
            if (smallest === i) break;
            [pq[smallest], pq[i]] = [pq[i], pq[smallest]];
            i = smallest;
        }
        return top;
    };
    while (pq.length) {
        const [cost, time, u] = pop();
        if (time >= minTime[u]) continue;
        minTime[u] = time;
        if (u === n - 1) return cost;
        for (const [v, dt] of graph[u]) {
            const nt = time + dt;
            if (nt <= maxTime && nt < minTime[v]) push([cost + passingFee[v], nt, v]);
        }
    }
    return -1;
};
''',
    "1929_concatenation_of_array": r'''// LeetCode 1929 - Concatenation of Array
// https://leetcode.com/problems/concatenation-of-array/

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var getConcatenation = function(nums) {
    return nums.concat(nums);
};
''',
    "1930_unique_length_3_palindromic_subsequences": r'''// LeetCode 1930 - Unique Length-3 Palindromic Subsequences
// https://leetcode.com/problems/unique-length-3-palindromic-subsequences/

/**
 * @param {string} s
 * @return {number}
 */
var countPalindromicSubsequence = function(s) {
    const first = new Map(), last = new Map();
    for (let i = 0; i < s.length; i++) {
        if (!first.has(s[i])) first.set(s[i], i);
        last.set(s[i], i);
    }
    let ans = 0;
    for (const [c, f] of first) {
        const l = last.get(c);
        if (l - f > 1) ans += new Set(s.slice(f + 1, l)).size;
    }
    return ans;
};
''',
    "1931_painting_a_grid_with_three_different_colors": r'''// LeetCode 1931 - Painting a Grid With Three Different Colors
// https://leetcode.com/problems/painting-a-grid-with-three-different-colors/

/**
 * @param {number} m
 * @param {number} n
 * @return {number}
 */
var colorTheGrid = function(m, n) {
    const MOD = 1000000007;
    const validColumn = (mask) => {
        let prev = -1, x = mask;
        for (let i = 0; i < m; i++) {
            const c = x % 3;
            if (c === prev) return false;
            prev = c;
            x = Math.floor(x / 3);
        }
        return true;
    };
    const getColors = (mask) => {
        const cols = [];
        let x = mask;
        for (let i = 0; i < m; i++) {
            cols.push(x % 3);
            x = Math.floor(x / 3);
        }
        return cols;
    };
    const states = [];
    for (let s = 0; s < 3 ** m; s++) if (validColumn(s)) states.push(s);
    const compat = new Map(states.map((s) => [s, []]));
    for (const a of states) {
        const ca = getColors(a);
        for (const b of states) {
            const cb = getColors(b);
            if (ca.every((x, i) => x !== cb[i])) compat.get(a).push(b);
        }
    }
    const memo = new Map();
    const dp = (col, prev) => {
        const key = `${col},${prev}`;
        if (memo.has(key)) return memo.get(key);
        if (col === n) return 1;
        let total = 0;
        const options = prev === -1 ? states : compat.get(prev);
        for (const cur of options) total = (total + dp(col + 1, cur)) % MOD;
        memo.set(key, total);
        return total;
    };
    return dp(0, -1);
};
''',
    "1932_merge_bsts_to_create_single_bst": r'''// LeetCode 1932 - Merge BSTs to Create Single BST
// https://leetcode.com/problems/merge-bsts-to-create-single-bst/

/**
 * @param {TreeNode[]} trees
 * @return {TreeNode}
 */
var canMerge = function(trees) {
    const valueToRoot = new Map();
    const count = new Map();
    for (const tree of trees) {
        valueToRoot.set(tree.val, tree);
        count.set(tree.val, (count.get(tree.val) || 0) + 1);
        if (tree.left) count.set(tree.left.val, (count.get(tree.left.val) || 0) + 1);
        if (tree.right) count.set(tree.right.val, (count.get(tree.right.val) || 0) + 1);
    }
    const roots = trees.filter((t) => count.get(t.val) === 1);
    if (roots.length !== 1) return null;
    const root = roots[0];
    const merge = (node) => {
        if (!node) return true;
        if (node.left && valueToRoot.has(node.left.val)) {
            node.left = valueToRoot.get(node.left.val);
            valueToRoot.delete(node.left.val);
        }
        if (node.right && valueToRoot.has(node.right.val)) {
            node.right = valueToRoot.get(node.right.val);
            valueToRoot.delete(node.right.val);
        }
        return merge(node.left) && merge(node.right);
    };
    valueToRoot.delete(root.val);
    if (!merge(root) || valueToRoot.size) return null;
    const isValidBst = (node, lo, hi) => {
        if (!node) return true;
        if (!(lo < node.val && node.val < hi)) return false;
        return isValidBst(node.left, lo, node.val) && isValidBst(node.right, node.val, hi);
    };
    return isValidBst(root, -Infinity, Infinity) ? root : null;
};
''',
    "1933_check_if_string_is_decomposable_into_value_equal_substrings": r'''// LeetCode 1933 - Check if String Is Decomposable Into Value-Equal Substrings
// https://leetcode.com/problems/check-if-string-is-decomposable-into-value-equal-substrings/

/**
 * @param {string} s
 * @return {boolean}
 */
var isDecomposable = function(s) {
    const n = s.length;
    let i = 0, twos = 0;
    while (i < n) {
        let j = i;
        while (j < n && s[j] === s[i]) j++;
        const length = j - i;
        if (length % 3 === 1) return false;
        if (length % 3 === 2) {
            twos++;
            if (twos > 1) return false;
        }
        i = j;
    }
    return twos === 1;
};
''',
    "1935_maximum_number_of_words_you_can_type": r'''// LeetCode 1935 - Maximum Number of Words You Can Type
// https://leetcode.com/problems/maximum-number-of-words-you-can-type/

/**
 * @param {string} text
 * @param {string} brokenLetters
 * @return {number}
 */
var canBeTypedWords = function(text, brokenLetters) {
    const broken = new Set(brokenLetters);
    return text.split(" ").filter((w) => ![...w].some((ch) => broken.has(ch))).length;
};
''',
    "1936_add_minimum_number_of_rungs": r'''// LeetCode 1936 - Add Minimum Number of Rungs
// https://leetcode.com/problems/add-minimum-number-of-rungs/

/**
 * @param {number[]} rungs
 * @param {number} dist
 * @return {number}
 */
var addRungs = function(rungs, dist) {
    let prev = 0, ans = 0;
    for (const r of rungs) {
        ans += Math.floor((r - prev - 1) / dist);
        prev = r;
    }
    return ans;
};
''',
    "1937_maximum_number_of_points_with_cost": r'''// LeetCode 1937 - Maximum Number of Points with Cost
// https://leetcode.com/problems/maximum-number-of-points-with-cost/

/**
 * @param {number[][]} points
 * @return {number}
 */
var maxPoints = function(points) {
    const m = points.length, n = points[0].length;
    let prev = points[0].slice();
    for (let r = 1; r < m; r++) {
        const left = new Array(n), right = new Array(n), cur = new Array(n);
        left[0] = prev[0];
        for (let c = 1; c < n; c++) left[c] = Math.max(left[c - 1] - 1, prev[c]);
        right[n - 1] = prev[n - 1];
        for (let c = n - 2; c >= 0; c--) right[c] = Math.max(right[c + 1] - 1, prev[c]);
        for (let c = 0; c < n; c++) cur[c] = points[r][c] + Math.max(left[c], right[c]);
        prev = cur;
    }
    return Math.max(...prev);
};
''',
}

# Fill remaining entries for 1936 if missing from py - already included.
# Continue 1938-1945 in this file after reading sources.


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

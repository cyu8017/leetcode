#!/usr/bin/env python3
"""Port JS solutions for LeetCode stubs 1970-1999 (non-SQL)."""
from __future__ import annotations

import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SOLUTIONS: dict[str, str] = {
    "1970_last_day_where_you_can_still_cross": r'''// LeetCode 1970 - Last Day Where You Can Still Cross
// https://leetcode.com/problems/last-day-where-you-can-still-cross/

/**
 * @param {number} row
 * @param {number} col
 * @param {number[][]} cells
 * @return {number}
 */
var latestDayToCross = function(row, col, cells) {
    const can = (day) => {
        const blocked = new Set();
        for (let i = 0; i < day; i++) blocked.add(`${cells[i][0] - 1},${cells[i][1] - 1}`);
        const stack = [];
        const seen = new Set();
        for (let c = 0; c < col; c++) {
            if (!blocked.has(`0,${c}`)) {
                stack.push([0, c]);
                seen.add(`0,${c}`);
            }
        }
        while (stack.length) {
            const [r, c] = stack.pop();
            if (r === row - 1) return true;
            for (const [nr, nc] of [[r - 1, c], [r + 1, c], [r, c - 1], [r, c + 1]]) {
                const key = `${nr},${nc}`;
                if (nr >= 0 && nr < row && nc >= 0 && nc < col && !blocked.has(key) && !seen.has(key)) {
                    seen.add(key);
                    stack.push([nr, nc]);
                }
            }
        }
        return false;
    };
    let lo = 1, hi = cells.length, ans = 0;
    while (lo <= hi) {
        const mid = (lo + hi) >> 1;
        if (can(mid)) {
            ans = mid;
            lo = mid + 1;
        } else hi = mid - 1;
    }
    return ans;
};
''',
    "1971_find_if_path_exists_in_graph": r'''// LeetCode 1971 - Find if Path Exists in Graph
// https://leetcode.com/problems/find-if-path-exists-in-graph/

/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {number} source
 * @param {number} destination
 * @return {boolean}
 */
var validPath = function(n, edges, source, destination) {
    if (source === destination) return true;
    const g = Array.from({ length: n }, () => []);
    for (const [a, b] of edges) {
        g[a].push(b);
        g[b].push(a);
    }
    const stack = [source];
    const seen = new Set([source]);
    while (stack.length) {
        const u = stack.pop();
        if (u === destination) return true;
        for (const v of g[u]) {
            if (!seen.has(v)) {
                seen.add(v);
                stack.push(v);
            }
        }
    }
    return false;
};
''',
    "1973_count_nodes_equal_to_sum_of_descendants": r'''// LeetCode 1973 - Count Nodes Equal to Sum of Descendants
// https://leetcode.com/problems/count-nodes-equal-to-sum-of-descendants/

/**
 * @param {TreeNode} root
 * @return {number}
 */
var equalToDescendants = function(root) {
    let ans = 0;
    const dfs = (node) => {
        if (!node) return 0;
        const total = dfs(node.left) + dfs(node.right);
        if (total === node.val) ans++;
        return total + node.val;
    };
    dfs(root);
    return ans;
};
''',
    "1974_minimum_time_to_type_word_using_special_typewriter": r'''// LeetCode 1974 - Minimum Time to Type Word Using Special Typewriter
// https://leetcode.com/problems/minimum-time-to-type-word-using-special-typewriter/

/**
 * @param {string} word
 * @return {number}
 */
var minTimeToType = function(word) {
    let cur = "a", ans = 0;
    for (const ch of word) {
        const d = Math.abs(ch.charCodeAt(0) - cur.charCodeAt(0));
        ans += Math.min(d, 26 - d) + 1;
        cur = ch;
    }
    return ans;
};
''',
    "1975_maximum_matrix_sum": r'''// LeetCode 1975 - Maximum Matrix Sum
// https://leetcode.com/problems/maximum-matrix-sum/

/**
 * @param {number[][]} matrix
 * @return {number}
 */
var maxMatrixSum = function(matrix) {
    let total = 0, neg = 0, mn = Infinity;
    for (const row of matrix) {
        for (const x of row) {
            if (x < 0) neg++;
            const ax = Math.abs(x);
            total += ax;
            mn = Math.min(mn, ax);
        }
    }
    return neg % 2 === 0 ? total : total - 2 * mn;
};
''',
    "1976_number_of_ways_to_arrive_at_destination": r'''// LeetCode 1976 - Number of Ways to Arrive at Destination
// https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/

/**
 * @param {number} n
 * @param {number[][]} roads
 * @return {number}
 */
var countPaths = function(n, roads) {
    const MOD = 1000000007;
    const g = Array.from({ length: n }, () => []);
    for (const [u, v, t] of roads) {
        g[u].push([v, t]);
        g[v].push([u, t]);
    }
    const dist = new Array(n).fill(Infinity);
    const ways = new Array(n).fill(0);
    dist[0] = 0;
    ways[0] = 1;
    const pq = [[0, 0]];
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
            let s = i;
            const l = 2 * i + 1, r = 2 * i + 2;
            if (l < pq.length && pq[l][0] < pq[s][0]) s = l;
            if (r < pq.length && pq[r][0] < pq[s][0]) s = r;
            if (s === i) break;
            [pq[s], pq[i]] = [pq[i], pq[s]];
            i = s;
        }
        return top;
    };
    while (pq.length) {
        const [d, u] = pop();
        if (d > dist[u]) continue;
        for (const [v, w] of g[u]) {
            const nd = d + w;
            if (nd < dist[v]) {
                dist[v] = nd;
                ways[v] = ways[u];
                push([nd, v]);
            } else if (nd === dist[v]) {
                ways[v] = (ways[v] + ways[u]) % MOD;
            }
        }
    }
    return ways[n - 1];
};
''',
    "1977_number_of_ways_to_separate_numbers": r'''// LeetCode 1977 - Number of Ways to Separate Numbers
// https://leetcode.com/problems/number-of-ways-to-separate-numbers/

/**
 * @param {string} num
 * @return {number}
 */
var numberOfCombinations = function(num) {
    const MOD = 1000000007;
    const n = num.length;
    if (num[0] === "0") return 0;
    const lcp = Array.from({ length: n + 1 }, () => new Array(n + 1).fill(0));
    for (let i = n - 1; i >= 0; i--) {
        for (let j = n - 1; j >= 0; j--) {
            if (num[i] === num[j]) lcp[i][j] = lcp[i + 1][j + 1] + 1;
        }
    }
    const le = (a, b, length) => {
        const common = lcp[a][b];
        if (common >= length) return true;
        return num[a + common] < num[b + common];
    };
    const dp = Array.from({ length: n + 1 }, () => new Array(n + 1).fill(0));
    const pref = Array.from({ length: n + 1 }, () => new Array(n + 1).fill(0));
    for (let i = 1; i <= n; i++) {
        for (let l = 1; l <= i; l++) {
            const start = i - l;
            if (num[start] === "0") dp[i][l] = 0;
            else if (start === 0) dp[i][l] = 1;
            else {
                let ways = l > 1 ? pref[start][Math.min(l - 1, start)] : 0;
                if (start >= l && le(start - l, start, l)) ways = (ways + dp[start][l]) % MOD;
                dp[i][l] = ways;
            }
        }
        for (let l = 1; l <= n; l++) {
            pref[i][l] = (pref[i][l - 1] + (l <= i ? dp[i][l] : 0)) % MOD;
        }
    }
    return pref[n][n];
};
''',
    "1979_find_greatest_common_divisor_of_array": r'''// LeetCode 1979 - Find Greatest Common Divisor of Array
// https://leetcode.com/problems/find-greatest-common-divisor-of-array/

/**
 * @param {number[]} nums
 * @return {number}
 */
var findGCD = function(nums) {
    const gcd = (a, b) => (b === 0 ? a : gcd(b, a % b));
    return gcd(Math.min(...nums), Math.max(...nums));
};
''',
    "1980_find_unique_binary_string": r'''// LeetCode 1980 - Find Unique Binary String
// https://leetcode.com/problems/find-unique-binary-string/

/**
 * @param {string[]} nums
 * @return {string}
 */
var findDifferentBinaryString = function(nums) {
    const s = new Set(nums);
    const n = nums.length;
    const preferred = ["11", "101", "00", "10", "01", "000", "001", "010", "011", "100", "110", "111"];
    for (const cand of preferred) {
        if (cand.length === n && !s.has(cand)) return cand;
    }
    for (let i = 0; i < (1 << n); i++) {
        const cand = i.toString(2).padStart(n, "0");
        if (!s.has(cand)) return cand;
    }
    return "0".repeat(n);
};
''',
    "1981_minimize_the_difference_between_target_and_chosen_elements": r'''// LeetCode 1981 - Minimize the Difference Between Target and Chosen Elements
// https://leetcode.com/problems/minimize-the-difference-between-target-and-chosen-elements/

/**
 * @param {number[][]} mat
 * @param {number} target
 * @return {number}
 */
var minimizeTheDifference = function(mat, target) {
    let possible = new Set([0]);
    for (const row of mat) {
        const uniq = [...new Set(row)];
        const nxt = new Set();
        for (const s of possible) for (const x of uniq) nxt.add(s + x);
        const kept = new Set([...nxt].filter((v) => v <= target));
        const above = [...nxt].filter((v) => v > target);
        if (above.length) kept.add(Math.min(...above));
        possible = kept.size ? kept : new Set([Math.min(...nxt)]);
    }
    let best = Infinity;
    for (const v of possible) best = Math.min(best, Math.abs(v - target));
    return best;
};
''',
    "1982_find_array_given_subset_sums": r'''// LeetCode 1982 - Find Array Given Subset Sums
// https://leetcode.com/problems/find-array-given-subset-sums/

/**
 * @param {number} n
 * @param {number[]} sums
 * @return {number[]}
 */
var recoverArray = function(n, sums) {
    sums = sums.slice().sort((a, b) => a - b);
    const ans = [];
    for (let t = 0; t < n; t++) {
        const d = sums[1] - sums[0];
        const count = new Map();
        for (const x of sums) count.set(x, (count.get(x) || 0) + 1);
        const without = [], withD = [];
        for (const x of sums) {
            if ((count.get(x) || 0) === 0) continue;
            count.set(x, count.get(x) - 1);
            count.set(x + d, count.get(x + d) - 1);
            without.push(x);
            withD.push(x + d);
        }
        if (without.includes(0)) {
            ans.push(d);
            sums = without;
        } else {
            ans.push(-d);
            sums = withD;
        }
    }
    return ans;
};
''',
    "1983_widest_pair_of_indices_with_equal_range_sum": r'''// LeetCode 1983 - Widest Pair of Indices With Equal Range Sum
// https://leetcode.com/problems/widest-pair-of-indices-with-equal-range-sum/

/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var widestPairOfIndices = function(nums1, nums2) {
    const first = new Map([[0, -1]]);
    let ans = 0, s = 0;
    for (let i = 0; i < nums1.length; i++) {
        s += nums1[i] - nums2[i];
        if (first.has(s)) ans = Math.max(ans, i - first.get(s));
        else first.set(s, i);
    }
    return ans;
};
''',
    "1984_minimum_difference_between_highest_and_lowest_of_k_scores": r'''// LeetCode 1984 - Minimum Difference Between Highest and Lowest of K Scores
// https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var minimumDifference = function(nums, k) {
    nums = nums.slice().sort((a, b) => a - b);
    let ans = Infinity;
    for (let i = 0; i + k - 1 < nums.length; i++) ans = Math.min(ans, nums[i + k - 1] - nums[i]);
    return ans;
};
''',
    "1985_find_the_kth_largest_integer_in_the_array": r'''// LeetCode 1985 - Find the Kth Largest Integer in the Array
// https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/

/**
 * @param {string[]} nums
 * @param {number} k
 * @return {string}
 */
var kthLargestNumber = function(nums, k) {
    return nums.slice().sort((a, b) => (a.length !== b.length ? b.length - a.length : b.localeCompare(a)))[k - 1];
};
''',
    "1986_minimum_number_of_work_sessions_to_finish_the_tasks": r'''// LeetCode 1986 - Minimum Number of Work Sessions to Finish the Tasks
// https://leetcode.com/problems/minimum-number-of-work-sessions-to-finish-the-tasks/

/**
 * @param {number[]} tasks
 * @param {number} sessionTime
 * @return {number}
 */
var minSessions = function(tasks, sessionTime) {
    const n = tasks.length;
    const INF = [n + 1, 0];
    const dp = Array.from({ length: 1 << n }, () => INF.slice());
    dp[0] = [1, 0];
    for (let mask = 0; mask < (1 << n); mask++) {
        const [sessions, used] = dp[mask];
        if (sessions > n) continue;
        for (let i = 0; i < n; i++) {
            if (mask & (1 << i)) continue;
            const t = tasks[i];
            const nmask = mask | (1 << i);
            const cand = used + t <= sessionTime ? [sessions, used + t] : [sessions + 1, t];
            if (cand[0] < dp[nmask][0] || (cand[0] === dp[nmask][0] && cand[1] < dp[nmask][1])) {
                dp[nmask] = cand;
            }
        }
    }
    return dp[(1 << n) - 1][0];
};
''',
    "1987_number_of_unique_good_subsequences": r'''// LeetCode 1987 - Number of Unique Good Subsequences
// https://leetcode.com/problems/number-of-unique-good-subsequences/

/**
 * @param {string} binary
 * @return {number}
 */
var numberOfUniqueGoodSubsequences = function(binary) {
    const MOD = 1000000007;
    let ends0 = 0, ends1 = 0, has0 = false;
    for (const ch of binary) {
        if (ch === "0") {
            has0 = true;
            ends0 = (ends0 + ends1) % MOD;
        } else {
            ends1 = (ends0 + ends1 + 1) % MOD;
        }
    }
    return (ends0 + ends1 + (has0 ? 1 : 0)) % MOD;
};
''',
    "1989_maximum_number_of_people_that_can_be_caught_in_tag": r'''// LeetCode 1989 - Maximum Number of People That Can Be Caught in Tag
// https://leetcode.com/problems/maximum-number-of-people-that-can-be-caught-in-tag/

/**
 * @param {number[]} team
 * @param {number} dist
 * @return {number}
 */
var catchMaximumAmountofPeople = function(team, dist) {
    let ans = 0, j = 0;
    const n = team.length;
    for (let i = 0; i < n; i++) {
        if (!team[i]) continue;
        while (j < n && (team[j] || i - j > dist)) j++;
        if (j < n && Math.abs(i - j) <= dist) {
            ans++;
            j++;
        }
    }
    return ans;
};
''',
    "1991_find_the_middle_index_in_array": r'''// LeetCode 1991 - Find the Middle Index in Array
// https://leetcode.com/problems/find-the-middle-index-in-array/

/**
 * @param {number[]} nums
 * @return {number}
 */
var findMiddleIndex = function(nums) {
    const total = nums.reduce((a, b) => a + b, 0);
    let left = 0;
    for (let i = 0; i < nums.length; i++) {
        if (left === total - left - nums[i]) return i;
        left += nums[i];
    }
    return -1;
};
''',
    "1992_find_all_groups_of_farmland": r'''// LeetCode 1992 - Find All Groups of Farmland
// https://leetcode.com/problems/find-all-groups-of-farmland/

/**
 * @param {number[][]} land
 * @return {number[][]}
 */
var findFarmland = function(land) {
    const m = land.length, n = land[0].length;
    const ans = [];
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (land[i][j] === 1 && (i === 0 || land[i - 1][j] === 0) && (j === 0 || land[i][j - 1] === 0)) {
                let r = i, c = j;
                while (r + 1 < m && land[r + 1][j] === 1) r++;
                while (c + 1 < n && land[i][c + 1] === 1) c++;
                ans.push([i, j, r, c]);
            }
        }
    }
    return ans;
};
''',
    "1993_operations_on_tree": r'''// LeetCode 1993 - Operations on Tree
// https://leetcode.com/problems/operations-on-tree/

class LockingTree {
    /**
     * @param {number[]} parent
     */
    constructor(parent) {
        const n = parent.length;
        this.locked = new Array(n).fill(-1);
        this.parent = parent;
        this.children = Array.from({ length: n }, () => []);
        for (let son = 1; son < n; son++) this.children[parent[son]].push(son);
    }

    /**
     * @param {number} num
     * @param {number} user
     * @return {boolean}
     */
    lock(num, user) {
        if (this.locked[num] === -1) {
            this.locked[num] = user;
            return true;
        }
        return false;
    }

    /**
     * @param {number} num
     * @param {number} user
     * @return {boolean}
     */
    unlock(num, user) {
        if (this.locked[num] === user) {
            this.locked[num] = -1;
            return true;
        }
        return false;
    }

    /**
     * @param {number} num
     * @param {number} user
     * @return {boolean}
     */
    upgrade(num, user) {
        let x = num;
        while (x !== -1) {
            if (this.locked[x] !== -1) return false;
            x = this.parent[x];
        }
        let find = false;
        const dfs = (u) => {
            for (const v of this.children[u]) {
                if (this.locked[v] !== -1) {
                    this.locked[v] = -1;
                    find = true;
                }
                dfs(v);
            }
        };
        dfs(num);
        if (!find) return false;
        this.locked[num] = user;
        return true;
    }
}
''',
    "1994_the_number_of_good_subsets": r'''// LeetCode 1994 - The Number of Good Subsets
// https://leetcode.com/problems/the-number-of-good-subsets/

/**
 * @param {number[]} nums
 * @return {number}
 */
var numberOfGoodSubsets = function(nums) {
    const MOD = 1000000007n;
    const primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29];
    const masks = new Array(31).fill(0);
    for (let x = 2; x <= 30; x++) {
        let m = 0, y = x, ok = true;
        for (let i = 0; i < primes.length; i++) {
            const p = primes[i];
            if (y % p === 0) {
                if (Math.floor(y / p) % p === 0) {
                    ok = false;
                    break;
                }
                m |= 1 << i;
                y = Math.floor(y / p);
            }
        }
        masks[x] = ok ? m : -1;
    }
    const cnt = new Array(31).fill(0);
    for (const v of nums) cnt[v]++;
    const dp = new Array(1 << primes.length).fill(0n);
    dp[0] = 1n;
    for (let x = 2; x <= 30; x++) {
        if (cnt[x] === 0 || masks[x] < 0) continue;
        const m = masks[x];
        for (let state = (1 << primes.length) - 1; state >= 0; state--) {
            if (state & m) continue;
            dp[state | m] = (dp[state | m] + dp[state] * BigInt(cnt[x])) % MOD;
        }
    }
    let ans = 0n;
    for (let i = 1; i < dp.length; i++) ans = (ans + dp[i]) % MOD;
    let mul = 1n;
    for (let i = 0; i < cnt[1]; i++) mul = mul * 2n % MOD;
    return Number(ans * mul % MOD);
};
''',
    "1995_count_special_quadruplets": r'''// LeetCode 1995 - Count Special Quadruplets
// https://leetcode.com/problems/count-special-quadruplets/

/**
 * @param {number[]} nums
 * @return {number}
 */
var countQuadruplets = function(nums) {
    const n = nums.length;
    let ans = 0;
    for (let a = 0; a < n; a++) {
        for (let b = a + 1; b < n; b++) {
            for (let c = b + 1; c < n; c++) {
                const s = nums[a] + nums[b] + nums[c];
                for (let d = c + 1; d < n; d++) if (nums[d] === s) ans++;
            }
        }
    }
    return ans;
};
''',
    "1996_the_number_of_weak_characters_in_the_game": r'''// LeetCode 1996 - The Number of Weak Characters in the Game
// https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/

/**
 * @param {number[][]} properties
 * @return {number}
 */
var numberOfWeakCharacters = function(properties) {
    properties = properties.slice().sort((a, b) => (a[0] !== b[0] ? a[0] - b[0] : b[1] - a[1]));
    let ans = 0, maxDef = 0;
    for (let i = properties.length - 1; i >= 0; i--) {
        if (properties[i][1] < maxDef) ans++;
        else maxDef = properties[i][1];
    }
    return ans;
};
''',
    "1997_first_day_where_you_have_been_in_all_the_rooms": r'''// LeetCode 1997 - First Day Where You Have Been in All the Rooms
// https://leetcode.com/problems/first-day-where-you-have-been-in-all-the-rooms/

/**
 * @param {number[]} nextVisit
 * @return {number}
 */
var firstDayBeenInAllRooms = function(nextVisit) {
    const MOD = 1000000007;
    const n = nextVisit.length;
    const dp = new Array(n).fill(0);
    for (let i = 1; i < n; i++) {
        dp[i] = (2 * dp[i - 1] - dp[nextVisit[i - 1]] + 2) % MOD;
        if (dp[i] < 0) dp[i] += MOD;
    }
    return dp[n - 1];
};
''',
    "1998_gcd_sort_of_an_array": r'''// LeetCode 1998 - GCD Sort of an Array
// https://leetcode.com/problems/gcd-sort-of-an-array/

/**
 * @param {number[]} nums
 * @return {boolean}
 */
var gcdSort = function(nums) {
    const m = Math.max(...nums);
    const parent = Array.from({ length: m + 1 }, (_, i) => i);
    const find = (x) => {
        while (parent[x] !== x) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    };
    const union = (a, b) => {
        const ra = find(a), rb = find(b);
        if (ra !== rb) parent[rb] = ra;
    };
    const spf = Array.from({ length: m + 1 }, (_, i) => i);
    for (let i = 2; i * i <= m; i++) {
        if (spf[i] === i) {
            for (let j = i * i; j <= m; j += i) {
                if (spf[j] === j) spf[j] = i;
            }
        }
    }
    for (const x of new Set(nums)) {
        let y = x;
        while (y > 1) {
            const p = spf[y];
            union(x, p);
            while (y % p === 0) y = Math.floor(y / p);
        }
    }
    const sorted = nums.slice().sort((a, b) => a - b);
    for (let i = 0; i < nums.length; i++) {
        if (find(nums[i]) !== find(sorted[i])) return false;
    }
    return true;
};
''',
    "1999_smallest_greater_multiple_made_of_two_digits": r'''// LeetCode 1999 - Smallest Greater Multiple Made of Two Digits
// https://leetcode.com/problems/smallest-greater-multiple-made-of-two-digits/

/**
 * @param {number} k
 * @param {number} digit1
 * @param {number} digit2
 * @return {number}
 */
var findInteger = function(k, digit1, digit2) {
    const digits = [...new Set([digit1, digit2])].sort((a, b) => a - b);
    const q = [];
    const seen = new Set();
    for (const d of digits) {
        if (d !== 0) {
            q.push(d);
            seen.add(d);
        }
    }
    if (!q.length) return -1;
    const LIMIT = 2147483647;
    for (let qi = 0; qi < q.length; qi++) {
        const x = q[qi];
        if (x > k && x % k === 0) return x;
        for (const d of digits) {
            const nx = x * 10 + d;
            if (nx <= LIMIT && !seen.has(nx)) {
                seen.add(nx);
                q.push(nx);
            }
        }
    }
    return -1;
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

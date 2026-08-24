
================================================================================
FILE: 3450_maximum_students_on_a_single_bench
================================================================================
// LeetCode 3450 - Maximum Students on a Single Bench
// https://leetcode.com/problems/maximum-students-on-a-single-bench/

var maxStudentsOnBench = function(students) {
    const bench = new Map();
    for (const s of students) {
        if (!bench.has(s[1])) bench.set(s[1], new Set());
        bench.get(s[1]).add(s[0]);
    }
    let ans = 0;
    for (const set of bench.values()) {
        if (set.size > ans) ans = set.size;
    }
    return ans;
};

================================================================================
FILE: 3452_sum_of_good_numbers
================================================================================
// LeetCode 3452 - Sum of Good Numbers
// https://leetcode.com/problems/sum-of-good-numbers/

var sumOfGoodNumbers = function(nums, k) {
    let ans = 0;
    const n = nums.length;
    for (let i = 0; i < n; i++) {
        const x = nums[i];
        let good = true;
        if (i - k >= 0 && x <= nums[i - k]) good = false;
        if (i + k < n && x <= nums[i + k]) good = false;
        if (good) ans += x;
    }
    return ans;
};

================================================================================
FILE: 3453_separate_squares_i
================================================================================
// LeetCode 3453 - Separate Squares I
// https://leetcode.com/problems/separate-squares-i/

var separateSquares = function(squares) {
    let total = 0;
    for (const sq of squares) {
        const l = sq[2];
        total += l * l;
    }
    const areaBelow = (y) => {
        let below = 0;
        for (const sq of squares) {
            const yi = sq[1], l = sq[2];
            const top = yi + l;
            if (y <= yi) continue;
            if (y >= top) below += l * l;
            else below += l * (y - yi);
        }
        return below;
    };
    let lo = 0.0, hi = 2e9;
    for (let it = 0; it < 60; it++) {
        const mid = (lo + hi) / 2;
        if (areaBelow(mid) * 2 < total) lo = mid;
        else hi = mid;
    }
    return hi;
};

================================================================================
FILE: 3454_separate_squares_ii
================================================================================
// LeetCode 3454 - Separate Squares II
// https://leetcode.com/problems/separate-squares-ii/

var separateSquares = function(squares) {
    let total = 0;
    for (const sq of squares) {
        const l = sq[2];
        total += l * l;
    }
    const areaBelow = (y) => {
        let below = 0;
        for (const sq of squares) {
            const yi = sq[1], l = sq[2];
            const top = yi + l;
            if (y <= yi) continue;
            else if (y >= top) below += l * l;
            else below += l * (y - yi);
        }
        return below;
    };
    let lo = 0.0, hi = 2e9;
    for (let it = 0; it < 60; it++) {
        const mid = (lo + hi) / 2;
        if (areaBelow(mid) * 2 < total) lo = mid;
        else hi = mid;
    }
    return hi;
};

================================================================================
FILE: 3455_shortest_matching_substring
================================================================================
// LeetCode 3455 - Shortest Matching Substring
// https://leetcode.com/problems/shortest-matching-substring/

var shortestMatchingSubstring = function(s, p) {
    const parts = [];
    let cur = "";
    for (const c of p) {
        if (c === "*") {
            parts.push(cur);
            cur = "";
        } else cur += c;
    }
    parts.push(cur);
    while (parts.length < 3) parts.push("");
    const a = parts[0], b = parts[1], c = parts[2];
    const n = s.length;
    const findAll = (sub) => {
        const res = [];
        if (sub.length === 0) {
            for (let i = 0; i <= n; i++) res.push(i);
            return res;
        }
        for (let i = 0; i + sub.length <= n; i++) {
            if (s.startsWith(sub, i)) res.push(i);
        }
        return res;
    };
    const sortSearch = (arr, x) => {
        let lo = 0, hi = arr.length;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (arr[mid] < x) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    };
    const posA = findAll(a), posB = findAll(b), posC = findAll(c);
    let ans = n + 1;
    for (const ia of posA) {
        const endA = ia + a.length;
        let bi = sortSearch(posB, endA);
        for (; bi < posB.length; bi++) {
            const endB = posB[bi] + b.length;
            const ci = sortSearch(posC, endB);
            if (ci < posC.length) {
                const length = posC[ci] + c.length - ia;
                if (length < ans) ans = length;
            }
            break;
        }
    }
    return ans === n + 1 ? -1 : ans;
};

================================================================================
FILE: 3456_find_special_substring_of_length_k
================================================================================
// LeetCode 3456 - Find Special Substring of Length K
// https://leetcode.com/problems/find-special-substring-of-length-k/

var hasSpecialSubstring = function(s, k) {
    const n = s.length;
    for (let i = 0; i + k <= n; i++) {
        let ok = true;
        for (let j = i + 1; j < i + k; j++) {
            if (s[j] !== s[i]) { ok = false; break; }
        }
        if (!ok) continue;
        if (i > 0 && s[i - 1] === s[i]) continue;
        if (i + k < n && s[i + k] === s[i]) continue;
        return true;
    }
    return false;
};

================================================================================
FILE: 3457_eat_pizzas
================================================================================
// LeetCode 3457 - Eat Pizzas!
// https://leetcode.com/problems/eat-pizzas/

var maxWeight = function(pizzas) {
    pizzas = pizzas.slice().sort((a, b) => a - b);
    const n = pizzas.length;
    const days = Math.floor(n / 4);
    let ans = 0;
    const oddDays = Math.floor((days + 1) / 2);
    const evenDays = Math.floor(days / 2);
    let idx = n - 1;
    for (let i = 0; i < oddDays; i++) {
        ans += pizzas[idx];
        idx--;
    }
    for (let i = 0; i < evenDays; i++) {
        idx--;
        ans += pizzas[idx];
        idx--;
    }
    return ans;
};

================================================================================
FILE: 3458_select_k_disjoint_special_substrings
================================================================================
// LeetCode 3458 - Select K Disjoint Special Substrings
// https://leetcode.com/problems/select-k-disjoint-special-substrings/

var maxSubstringLength = function(s, k) {
    const n = s.length;
    const first = new Array(26).fill(n), last = new Array(26).fill(-1);
    for (let i = 0; i < n; i++) {
        const ci = s.charCodeAt(i) - 97;
        if (first[ci] === n) first[ci] = i;
        last[ci] = i;
    }
    const segs = [];
    for (let c = 0; c < 26; c++) {
        if (last[c] === -1) continue;
        let l = first[c], r = last[c];
        for (let i = l; i <= r; i++) {
            const ci = s.charCodeAt(i) - 97;
            if (first[ci] < l) {
                l = first[ci];
                i = l - 1;
                continue;
            }
            if (last[ci] > r) r = last[ci];
        }
        if (!(l === 0 && r === n - 1)) segs.push([l, r]);
    }
    const uniq = new Set();
    const arr = [];
    for (const sg of segs) {
        const key = (BigInt(sg[0]) << 32n) | BigInt(sg[1] >>> 0);
        const ks = key.toString();
        if (!uniq.has(ks)) {
            uniq.add(ks);
            arr.push(sg);
        }
    }
    arr.sort((a, b) => a[1] - b[1]);
    let cnt = 0, end = -1;
    for (const sg of arr) {
        if (sg[0] > end) {
            cnt++;
            end = sg[1];
        }
    }
    return cnt >= k;
};

================================================================================
FILE: 3459_length_of_longest_v_shaped_diagonal_segment
================================================================================
// LeetCode 3459 - Length of Longest V-Shaped Diagonal Segment
// https://leetcode.com/problems/length-of-longest-v-shaped-diagonal-segment/

var lenOfVDiagonal = function(grid) {
    const m = grid.length, n = grid[0].length;
    const dirs = [[1, 1], [1, -1], [-1, -1], [-1, 1]];
    const nextDir = [1, 2, 3, 0];
    const memo = new Map();
    const key = (i, j, d, turned, expect) =>
        ((((i * 101 + j) * 5 + d) * 3 + turned) * 5 + expect);
    const dfs = (i, j, d, turned, expect) => {
        if (i < 0 || j < 0 || i >= m || j >= n || grid[i][j] !== expect) return 0;
        const k = key(i, j, d, turned, expect);
        if (memo.has(k)) return memo.get(k);
        const ni = i + dirs[d][0], nj = j + dirs[d][1];
        const nx = expect === 2 ? 0 : 2;
        let best = 1 + dfs(ni, nj, d, turned, nx);
        if (turned === 0) {
            const nd = nextDir[d];
            const ti = i + dirs[nd][0], tj = j + dirs[nd][1];
            const cand = 1 + dfs(ti, tj, nd, 1, nx);
            if (cand > best) best = cand;
        }
        memo.set(k, best);
        return best;
    };
    let ans = 0;
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (grid[i][j] !== 1) continue;
            for (let d = 0; d < 4; d++) {
                const ni = i + dirs[d][0], nj = j + dirs[d][1];
                const best = 1 + dfs(ni, nj, d, 0, 2);
                if (best > ans) ans = best;
            }
            if (ans < 1) ans = 1;
        }
    }
    return ans;
};

================================================================================
FILE: 3460_longest_common_prefix_after_at_most_one_removal
================================================================================
// LeetCode 3460 - Longest Common Prefix After at Most One Removal
// https://leetcode.com/problems/longest-common-prefix-after-at-most-one-removal/

var longestCommonPrefix = function(s, t) {
    let i = 0, j = 0;
    let removed = false;
    while (i < s.length && j < t.length) {
        if (s[i] === t[j]) {
            i++;
            j++;
            continue;
        }
        if (removed) break;
        removed = true;
        i++;
    }
    return j;
};

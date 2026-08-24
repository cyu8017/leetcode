
================================================================================
FILE: 3515_shortest_path_in_a_weighted_tree
================================================================================
// LeetCode 3515 - Shortest Path in a Weighted Tree
// https://leetcode.com/problems/shortest-path-in-a-weighted-tree/

var treeQueries = function(n, edges, queries) {
    const g = Array.from({length: n + 1}, () => []);
    const weight = new Map();
    for (const e of edges) {
        const u = e[0], v = e[1], w = e[2];
        g[u].push([v, w]);
        g[v].push([u, w]);
        const a = Math.min(u, v), b = Math.max(u, v);
        weight.set((BigInt(a) << 32n) | BigInt(b), w);
    }
    const inT = new Array(n + 1).fill(0);
    const outT = new Array(n + 1).fill(0);
    const dist = new Array(n + 1).fill(0);
    const parent = new Array(n + 1).fill(0);
    let time = 0;
    function dfs(u, p) {
        inT[u] = time++;
        for (const e of g[u]) {
            const to = e[0], w = e[1];
            if (to === p) continue;
            parent[to] = u;
            dist[to] = dist[u] + w;
            dfs(to, u);
        }
        outT[u] = time - 1;
    }
    dfs(1, 0);
    const bit = new Array(n + 2).fill(0);
    function add(i, v) {
        for (; i <= n; i += i & -i) bit[i] += v;
    }
    function rangeAdd(l, r, v) {
        add(l + 1, v);
        add(r + 2, -v);
    }
    function point(i) {
        let s = 0;
        for (i++; i > 0; i -= i & -i) s += bit[i];
        return s;
    }
    for (let i = 1; i <= n; i++) rangeAdd(inT[i], inT[i], dist[i]);
    const ans = [];
    for (const q of queries) {
        if (q[0] === 1) {
            const u = q[1], v = q[2], nw = q[3];
            const a = Math.min(u, v), b = Math.max(u, v);
            const key = (BigInt(a) << 32n) | BigInt(b);
            const ow = weight.get(key);
            const delta = nw - ow;
            weight.set(key, nw);
            const child = parent[u] === v ? u : v;
            rangeAdd(inT[child], outT[child], delta);
        } else {
            ans.push(point(inT[q[1]]));
        }
    }
    return ans;
};

================================================================================
FILE: 3516_find_closest_person
================================================================================
// LeetCode 3516 - Find Closest Person
// https://leetcode.com/problems/find-closest-person/

var findClosest = function(x, y, z) {
    const a = Math.abs(x - z), b = Math.abs(y - z);
    if (a === b) return 0;
    return a < b ? 1 : 2;
};

================================================================================
FILE: 3517_smallest_palindromic_rearrangement_i
================================================================================
// LeetCode 3517 - Smallest Palindromic Rearrangement I
// https://leetcode.com/problems/smallest-palindromic-rearrangement-i/

var smallestPalindrome = function(s) {
    const cnt = new Array(26).fill(0);
    for (const c of s) cnt[c.charCodeAt(0) - 97]++;
    let t = '';
    let ch = '';
    for (let i = 0; i < 26; i++) {
        const c = String.fromCharCode(97 + i);
        const v = Math.floor(cnt[i] / 2);
        t += c.repeat(v);
        cnt[i] -= v * 2;
        if (cnt[i] === 1) ch = c;
    }
    let sb = t;
    if (ch) sb += ch;
    for (let i = t.length - 1; i >= 0; i--) sb += t[i];
    return sb;
};

================================================================================
FILE: 3518_smallest_palindromic_rearrangement_ii
================================================================================
// LeetCode 3518 - Smallest Palindromic Rearrangement II
// https://leetcode.com/problems/smallest-palindromic-rearrangement-ii/

const MAX = 1000001;
function nCk(n, kk) {
    if (kk < 0 || kk > n) return 0;
    let res = 1;
    if (kk > n - kk) kk = n - kk;
    for (let i = 1; i <= kk; i++) {
        res = Math.floor(res * (n - i + 1) / i);
        if (res >= MAX) return MAX;
    }
    return res;
}
function countArr(h) {
    let total = 0;
    for (const f of h) total += f;
    let res = 1;
    for (const f of h) {
        res *= nCk(total, f);
        if (res >= MAX) return MAX;
        total -= f;
    }
    return res;
}
var smallestPalindrome = function(s, k) {
    const cnt = new Array(26).fill(0);
    for (const c of s) cnt[c.charCodeAt(0) - 97]++;
    let odd = 0;
    for (const c of cnt) if (c % 2 !== 0) odd++;
    if (odd > 1) return '';
    const half = new Array(26).fill(0);
    let mid = '';
    for (let i = 0; i < 26; i++) {
        half[i] = Math.floor(cnt[i] / 2);
        if (cnt[i] % 2 !== 0) mid = String.fromCharCode(97 + i);
    }
    if (countArr(half) < k) return '';
    let halfLen = 0;
    for (const f of half) halfLen += f;
    let left = '';
    for (let t = 0; t < halfLen; t++) {
        for (let i = 0; i < 26; i++) {
            if (half[i] === 0) continue;
            half[i]--;
            const arr = countArr(half);
            if (arr >= k) {
                left += String.fromCharCode(97 + i);
                break;
            }
            k -= arr;
            half[i]++;
        }
    }
    let res = left;
    if (mid) res += mid;
    for (let i = left.length - 1; i >= 0; i--) res += left[i];
    return res;
};

================================================================================
FILE: 3519_count_numbers_with_non_decreasing_digits
================================================================================
// LeetCode 3519 - Count Numbers with Non-Decreasing Digits
// https://leetcode.com/problems/count-numbers-with-non-decreasing-digits/

const MOD = 1000000007;
function toDigits(s, b) {
    if (s === '0') return [0];
    const digs = [];
    while (!(s.length === 1 && s[0] === '0')) {
        let rem = 0;
        let q = '';
        for (const c of s) {
            const cur = rem * 10 + (c.charCodeAt(0) - 48);
            const d = Math.floor(cur / b);
            rem = cur % b;
            if (q.length > 0 || d !== 0) q += String(d);
        }
        digs.push(rem);
        s = q.length === 0 ? '0' : q;
    }
    digs.reverse();
    return digs;
}
function dec(s) {
    const a = s.split('');
    let i = a.length - 1;
    while (i >= 0 && a[i] === '0') { a[i] = '9'; i--; }
    if (i < 0) return '0';
    a[i] = String(a[i].charCodeAt(0) - 49);
    let t = a.join('');
    let p = 0;
    while (p + 1 < t.length && t[p] === '0') p++;
    return t.substring(p);
}
function countUpto(digs, b) {
    const m = digs.length;
    const memo = new Map();
    function dfs(pos, last, tight) {
        if (pos === m) return 1;
        const key = pos + ',' + last + ',' + (tight ? 1 : 0);
        if (memo.has(key)) return memo.get(key);
        const up = tight ? digs[pos] : b - 1;
        let res = 0;
        for (let d = last; d <= up; d++)
            res = (res + dfs(pos + 1, d, tight && d === up)) % MOD;
        memo.set(key, res);
        return res;
    }
    return dfs(0, 0, true);
}
var countNumbers = function(l, r, b) {
    const rd = toDigits(r, b);
    const ld = toDigits(dec(l), b);
    return (countUpto(rd, b) - countUpto(ld, b) + MOD) % MOD;
};

================================================================================
FILE: 3520_minimum_threshold_for_inversion_pairs_count
================================================================================
// LeetCode 3520 - Minimum Threshold for Inversion Pairs Count
// https://leetcode.com/problems/minimum-threshold-for-inversion-pairs-count/

function upperBound(a, target) {
    let lo = 0, hi = a.length;
    while (lo < hi) {
        const mid = (lo + hi) >> 1;
        if (a[mid] <= target) lo = mid + 1;
        else hi = mid;
    }
    return lo;
}
function countInv(nums, k, threshold) {
    const sorted = [];
    let inv = 0;
    for (const num of nums) {
        const left = upperBound(sorted, num);
        const right = upperBound(sorted, num + threshold);
        inv += right - left;
        sorted.splice(upperBound(sorted, num), 0, num);
    }
    return inv >= k;
}
var minThreshold = function(nums, k) {
    let mx = 0;
    for (const v of nums) if (v > mx) mx = v;
    let l = 0, r = mx + 1;
    while (l < r) {
        const m = (l + r) >> 1;
        if (countInv(nums, k, m)) r = m;
        else l = m + 1;
    }
    return l > mx ? -1 : l;
};

================================================================================
FILE: 3522_calculate_score_after_performing_instructions
================================================================================
// LeetCode 3522 - Calculate Score After Performing Instructions
// https://leetcode.com/problems/calculate-score-after-performing-instructions/

var calculateScore = function(instructions, values) {
    const n = values.length;
    const vis = new Array(n).fill(false);
    let ans = 0, i = 0;
    while (i >= 0 && i < n && !vis[i]) {
        vis[i] = true;
        if (instructions[i][0] === 'a') {
            ans += values[i];
            i += 1;
        } else {
            i += values[i];
        }
    }
    return ans;
};

================================================================================
FILE: 3523_make_array_non_decreasing
================================================================================
// LeetCode 3523 - Make Array Non-decreasing
// https://leetcode.com/problems/make-array-non-decreasing/

var maximumPossibleSize = function(nums) {
    let ans = 0, mx = 0;
    for (const x of nums) {
        if (mx <= x) {
            ans++;
            mx = x;
        }
    }
    return ans;
};

================================================================================
FILE: 3524_find_x_value_of_array_i
================================================================================
// LeetCode 3524 - Find X Value of Array I
// https://leetcode.com/problems/find-x-value-of-array-i/

var resultArray = function(nums, k) {
    const ans = new Array(k).fill(0);
    let dp = new Array(k).fill(0);
    for (const num of nums) {
        const newDp = new Array(k).fill(0);
        const nm = num % k;
        newDp[nm] = 1;
        for (let i = 0; i < k; i++) newDp[(i * nm) % k] += dp[i];
        for (let i = 0; i < k; i++) ans[i] += newDp[i];
        dp = newDp;
    }
    return ans;
};

================================================================================
FILE: 3525_find_x_value_of_array_ii
================================================================================
// LeetCode 3525 - Find X Value of Array II
// https://leetcode.com/problems/find-x-value-of-array-ii/

var resultArray = function(nums, k, queries) {
    const n = nums.length;
    const ans = new Array(queries.length);
    for (let qi = 0; qi < queries.length; qi++) {
        const idx = queries[qi][0], val = queries[qi][1], start = queries[qi][2], x = queries[qi][3];
        nums[idx] = val;
        let prod = 1, cnt = 0;
        for (let i = start; i < n; i++) {
            prod = prod * (nums[i] % k) % k;
            if (prod === x) cnt++;
        }
        ans[qi] = cnt;
    }
    return ans;
};

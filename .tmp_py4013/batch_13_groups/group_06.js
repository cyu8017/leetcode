
================================================================================
FILE: 3484_design_spreadsheet
================================================================================
// LeetCode 3484 - Design Spreadsheet
// https://leetcode.com/problems/design-spreadsheet/

class Spreadsheet {
    /**
     * @param {number} rows
     */
    constructor(rows) {
        this.cells = new Map();
    }

    /**
     * @param {string} cell
     * @param {number} value
     * @return {void}
     */
    setCell(cell, value) {
        this.cells.set(cell, value);
    }

    /**
     * @param {string} cell
     * @return {void}
     */
    resetCell(cell) {
        this.cells.delete(cell);
    }

    /**
     * @param {string} formula
     * @return {number}
     */
    getValue(formula) {
        if (formula.length && formula[0] === "=") formula = formula.substring(1);
        let sum = 0;
        let start = 0;
        while (start < formula.length) {
            const plus = formula.indexOf("+", start);
            const p = plus < 0 ? formula.substring(start) : formula.substring(start, plus);
            let isNum = p.length && ((p[0] >= "0" && p[0] <= "9") || (p[0] === "-" && p.length > 1));
            if (isNum) {
                for (let i = 1; i < p.length; i++) {
                    if (p[i] < "0" || p[i] > "9") { isNum = false; break; }
                }
            }
            if (isNum) sum += parseInt(p, 10);
            else sum += this.cells.get(p) || 0;
            if (plus < 0) break;
            start = plus + 1;
        }
        return sum;
    }
}

================================================================================
FILE: 3485_longest_common_prefix_of_k_strings_after_removal
================================================================================
// LeetCode 3485 - Longest Common Prefix of K Strings After Removal
// https://leetcode.com/problems/longest-common-prefix-of-k-strings-after-removal/

var longestCommonPrefix = function(words, k) {
    const lcpOf = (a) => {
        if (!a.length) return 0;
        let pref = a[0];
        for (let t = 1; t < a.length; t++) {
            const s = a[t];
            let i = 0;
            while (i < pref.length && i < s.length && pref[i] === s[i]) i++;
            pref = pref.substring(0, i);
            if (!pref.length) return 0;
        }
        return pref.length;
    };
    const n = words.length;
    const ans = new Array(n);
    for (let i = 0; i < n; i++) {
        const rest = [];
        for (let j = 0; j < n; j++) if (j !== i) rest.push(words[j]);
        if (rest.length < k) { ans[i] = 0; continue; }
        rest.sort();
        let best = 0;
        for (let j = 0; j + k - 1 < rest.length; j++) {
            best = Math.max(best, lcpOf(rest.slice(j, j + k)));
        }
        ans[i] = best;
    }
    return ans;
};

================================================================================
FILE: 3486_longest_special_path_ii
================================================================================
// LeetCode 3486 - Longest Special Path II
// https://leetcode.com/problems/longest-special-path-ii/

var longestSpecialPath = function(edges, nums) {
    const n = nums.length;
    const g = Array.from({ length: n }, () => []);
    for (const e of edges) {
        g[e[0]].push([e[1], e[2]]);
        g[e[1]].push([e[0], e[2]]);
    }
    let bestLen = 0, bestNodes = 1;
    const dfs = (u, p, dist, pathVals, pathDist) => {
        pathVals.push(nums[u]);
        pathDist.push(dist);
        const freq = new Map();
        let dups = 0, left = 0;
        for (let right = 0; right < pathVals.length; right++) {
            const v = pathVals[right];
            freq.set(v, (freq.get(v) || 0) + 1);
            if (freq.get(v) === 2) dups++;
            while (dups > 1) {
                const lv = pathVals[left];
                if (freq.get(lv) === 2) dups--;
                freq.set(lv, freq.get(lv) - 1);
                left++;
            }
        }
        const length = dist - pathDist[left];
        const nodes = pathVals.length - left;
        if (length > bestLen || (length === bestLen && nodes < bestNodes)) {
            bestLen = length;
            bestNodes = nodes;
        }
        for (const e of g[u]) {
            if (e[0] === p) continue;
            dfs(e[0], u, dist + e[1], pathVals, pathDist);
        }
        pathVals.pop();
        pathDist.pop();
    };
    dfs(0, -1, 0, [], []);
    return [bestLen, bestNodes];
};

================================================================================
FILE: 3487_maximum_unique_subarray_sum_after_deletion
================================================================================
// LeetCode 3487 - Maximum Unique Subarray Sum After Deletion
// https://leetcode.com/problems/maximum-unique-subarray-sum-after-deletion/

var maxSum = function(nums) {
    const seen = new Set();
    let sum = 0;
    let hasPos = false;
    let maxNeg = -1e9;
    for (const x of nums) {
        if (x < 0) {
            if (x > maxNeg) maxNeg = x;
            continue;
        }
        hasPos = true;
        if (!seen.has(x)) {
            seen.add(x);
            sum += x;
        }
    }
    return hasPos ? sum : maxNeg;
};

================================================================================
FILE: 3488_closest_equal_element_queries
================================================================================
// LeetCode 3488 - Closest Equal Element Queries
// https://leetcode.com/problems/closest-equal-element-queries/

var solveQueries = function(nums, queries) {
    const n = nums.length;
    const pos = new Map();
    for (let i = 0; i < n; i++) {
        if (!pos.has(nums[i])) pos.set(nums[i], []);
        pos.get(nums[i]).push(i);
    }
    const ans = new Array(queries.length);
    for (let qi = 0; qi < queries.length; qi++) {
        const idx = queries[qi];
        const x = nums[idx];
        const arr = pos.get(x);
        if (arr.length === 1) { ans[qi] = -1; continue; }
        let best = n;
        for (const p of arr) {
            if (p === idx) continue;
            let d = Math.abs(p - idx);
            d = Math.min(d, n - d);
            if (d < best) best = d;
        }
        ans[qi] = best;
    }
    return ans;
};

================================================================================
FILE: 3489_zero_array_transformation_iv
================================================================================
// LeetCode 3489 - Zero Array Transformation IV
// https://leetcode.com/problems/zero-array-transformation-iv/

var minZeroArray = function(nums, queries) {
    const canSubsetSum = (vals, target) => {
        if (target === 0) return true;
        const dp = new Array(target + 1).fill(false);
        dp[0] = true;
        for (const v of vals) {
            for (let s = target; s >= v; s--) if (dp[s - v]) dp[s] = true;
        }
        return dp[target];
    };
    const ok = (k) => {
        for (let i = 0; i < nums.length; i++) {
            if (nums[i] === 0) continue;
            const vals = [];
            for (let q = 0; q < k; q++) {
                const l = queries[q][0], r = queries[q][1], v = queries[q][2];
                if (l <= i && i <= r) vals.push(v);
            }
            if (!canSubsetSum(vals, nums[i])) return false;
        }
        return true;
    };
    if (ok(0)) return 0;
    let lo = 1, hi = queries.length + 1;
    while (lo < hi) {
        const mid = Math.floor((lo + hi) / 2);
        if (mid <= queries.length && ok(mid)) hi = mid;
        else lo = mid + 1;
    }
    return lo > queries.length ? -1 : lo;
};

================================================================================
FILE: 3490_count_beautiful_numbers
================================================================================
// LeetCode 3490 - Count Beautiful Numbers
// https://leetcode.com/problems/count-beautiful-numbers/

var beautifulNumbers = function(l, r) {
    const countBeautiful = (n) => {
        if (n <= 0) return 0;
        const s = String(n);
        const dfs = (pos, tight, sum, prod, started) => {
            if (pos === s.length) {
                if (!started) return 0;
                return (sum > 0 && prod % sum === 0) ? 1 : 0;
            }
            const up = tight ? (s.charCodeAt(pos) - 48) : 9;
            let ans = 0;
            for (let d = 0; d <= up; d++) {
                const nt = tight && d === up;
                if (!started && d === 0) ans += dfs(pos + 1, nt, 0, 1, false);
                else {
                    const ns = sum + d;
                    const np = !started ? d : prod * d;
                    ans += dfs(pos + 1, nt, ns, np, true);
                }
            }
            return ans;
        };
        return dfs(0, true, 0, 1, false);
    };
    return countBeautiful(r) - countBeautiful(l - 1);
};

================================================================================
FILE: 3491_phone_number_prefix
================================================================================
// LeetCode 3491 - Phone Number Prefix
// https://leetcode.com/problems/phone-number-prefix/

var phonePrefix = function(numbers) {
    numbers = numbers.slice().sort();
    for (let i = 0; i + 1 < numbers.length; i++) {
        if (numbers[i].length <= numbers[i + 1].length && numbers[i + 1].startsWith(numbers[i]))
            return false;
    }
    return true;
};

================================================================================
FILE: 3492_maximum_containers_on_a_ship
================================================================================
// LeetCode 3492 - Maximum Containers on a Ship
// https://leetcode.com/problems/maximum-containers-on-a-ship/

var maxContainers = function(n, w, maxWeight) {
    const cap = n * n;
    const byW = Math.floor(maxWeight / w);
    return cap < byW ? cap : byW;
};

================================================================================
FILE: 3493_properties_graph
================================================================================
// LeetCode 3493 - Properties Graph
// https://leetcode.com/problems/properties-graph/

var numberOfComponents = function(properties, k) {
    const n = properties.length;
    const sets = properties.map((row) => new Set(row));
    const parent = Array.from({ length: n }, (_, i) => i);
    const find = (x) => {
        if (parent[x] !== x) parent[x] = find(parent[x]);
        return parent[x];
    };
    const unite = (a, b) => {
        const ra = find(a), rb = find(b);
        if (ra !== rb) parent[ra] = rb;
    };
    for (let i = 0; i < n; i++) {
        for (let j = i + 1; j < n; j++) {
            let cnt = 0;
            for (const v of sets[i]) if (sets[j].has(v)) cnt++;
            if (cnt >= k) unite(i, j);
        }
    }
    const comp = new Set();
    for (let i = 0; i < n; i++) comp.add(find(i));
    return comp.size;
};


================================================================================
FILE: 3418_maximum_amount_of_money_robot_can_earn
================================================================================
// LeetCode 3418 - Maximum Amount of Money Robot Can Earn
// https://leetcode.com/problems/maximum-amount-of-money-robot-can-earn/

var maximumAmount = function(coins) {
    const m = coins.length, n = coins[0].length;
    const neg = -(1 << 30);
    const dp = Array.from({ length: m }, () =>
        Array.from({ length: n }, () => new Array(3).fill(neg))
    );
    if (coins[0][0] < 0) {
        dp[0][0][0] = coins[0][0];
        dp[0][0][1] = 0;
        dp[0][0][2] = 0;
    } else {
        dp[0][0][0] = coins[0][0];
        dp[0][0][1] = coins[0][0];
        dp[0][0][2] = coins[0][0];
    }
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (i === 0 && j === 0) continue;
            for (let k = 0; k < 3; k++) {
                let best = neg;
                if (i > 0) best = Math.max(best, dp[i - 1][j][k]);
                if (j > 0) best = Math.max(best, dp[i][j - 1][k]);
                if (best === neg) continue;
                if (coins[i][j] >= 0) dp[i][j][k] = best + coins[i][j];
                else dp[i][j][k] = Math.max(dp[i][j][k], best + coins[i][j]);
            }
            for (let k = 1; k < 3; k++) {
                let best = neg;
                if (i > 0) best = Math.max(best, dp[i - 1][j][k - 1]);
                if (j > 0) best = Math.max(best, dp[i][j - 1][k - 1]);
                if (best !== neg && coins[i][j] < 0)
                    dp[i][j][k] = Math.max(dp[i][j][k], best);
            }
        }
    }
    return Math.max(dp[m - 1][n - 1][0], Math.max(dp[m - 1][n - 1][1], dp[m - 1][n - 1][2]));
};

================================================================================
FILE: 3419_minimize_the_maximum_edge_weight_of_graph
================================================================================
// LeetCode 3419 - Minimize the Maximum Edge Weight of Graph
// https://leetcode.com/problems/minimize-the-maximum-edge-weight-of-graph/

var minMaxWeight = function(n, edges, threshold) {
    const ok = (mid) => {
        const g = Array.from({ length: n }, () => []);
        for (const e of edges) {
            if (e[2] <= mid) g[e[1]].push(e[0]);
        }
        const vis = new Array(n).fill(false);
        const q = [0];
        vis[0] = true;
        let cnt = 1;
        while (q.length) {
            const u = q.shift();
            for (const v of g[u]) {
                if (!vis[v]) {
                    vis[v] = true;
                    cnt++;
                    q.push(v);
                }
            }
        }
        return cnt === n;
    };
    let lo = 1, hi = 1000001, ans = -1;
    while (lo < hi) {
        const mid = Math.floor((lo + hi) / 2);
        if (ok(mid)) {
            ans = mid;
            hi = mid;
        } else lo = mid + 1;
    }
    return ans;
};

================================================================================
FILE: 3420_count_non_decreasing_subarrays_after_k_operations
================================================================================
// LeetCode 3420 - Count Non-Decreasing Subarrays After K Operations
// https://leetcode.com/problems/count-non-decreasing-subarrays-after-k-operations/

var countNonDecreasingSubarrays = function(nums, k) {
    const n = nums.length;
    let ans = 0;
    for (let i = 0; i < n; i++) {
        let cost = 0;
        let maxV = nums[i];
        for (let j = i; j < n; j++) {
            if (nums[j] >= maxV) maxV = nums[j];
            else cost += maxV - nums[j];
            if (cost > k) break;
            ans++;
        }
    }
    return ans;
};

================================================================================
FILE: 3422_minimum_operations_to_make_subarray_elements_equal
================================================================================
// LeetCode 3422 - Minimum Operations to Make Subarray Elements Equal
// https://leetcode.com/problems/minimum-operations-to-make-subarray-elements-equal/

var minOperations = function(nums, k) {
    const n = nums.length;
    let ans = Number.MAX_SAFE_INTEGER;
    for (let i = 0; i + k <= n; i++) {
        const sub = nums.slice(i, i + k).sort((a, b) => a - b);
        const med = sub[Math.floor(k / 2)];
        let cost = 0;
        for (const x of sub) cost += Math.abs(x - med);
        if (cost < ans) ans = cost;
    }
    return ans;
};

================================================================================
FILE: 3423_maximum_difference_between_adjacent_elements_in_a_circular_array
================================================================================
// LeetCode 3423 - Maximum Difference Between Adjacent Elements in a Circular Array
// https://leetcode.com/problems/maximum-difference-between-adjacent-elements-in-a-circular-array/

var maxAdjacentDistance = function(nums) {
    let ans = 0;
    const n = nums.length;
    for (let i = 0; i < n; i++) {
        const d = Math.abs(nums[i] - nums[(i + 1) % n]);
        if (d > ans) ans = d;
    }
    return ans;
};

================================================================================
FILE: 3424_minimum_cost_to_make_arrays_identical
================================================================================
// LeetCode 3424 - Minimum Cost to Make Arrays Identical
// https://leetcode.com/problems/minimum-cost-to-make-arrays-identical/

var minCost = function(arr, brr, k) {
    let noSwap = 0;
    for (let i = 0; i < arr.length; i++) noSwap += Math.abs(arr[i] - brr[i]);
    const a2 = arr.slice().sort((a, b) => a - b);
    const b2 = brr.slice().sort((a, b) => a - b);
    let withSwap = k;
    for (let i = 0; i < a2.length; i++) withSwap += Math.abs(a2[i] - b2[i]);
    return noSwap < withSwap ? noSwap : withSwap;
};

================================================================================
FILE: 3425_longest_special_path
================================================================================
// LeetCode 3425 - Longest Special Path
// https://leetcode.com/problems/longest-special-path/

var longestSpecialPath = function(edges, nums) {
    const n = nums.length;
    const g = Array.from({ length: n }, () => []);
    for (const e of edges) {
        g[e[0]].push([e[1], e[2]]);
        g[e[1]].push([e[0], e[2]]);
    }
    let bestLen = 0, bestNodes = 1;
    const last = new Map();
    const path = [];
    const dfs = (u, p, dist, left) => {
        const seen = last.has(nums[u]);
        const prevPos = seen ? last.get(nums[u]) : -1;
        last.set(nums[u], path.length);
        let newLeft = left;
        if (seen && prevPos >= left) newLeft = prevPos + 1;
        path.push(dist);
        const length = dist - path[newLeft];
        const nodes = path.length - newLeft;
        if (length > bestLen || (length === bestLen && nodes < bestNodes)) {
            bestLen = length;
            bestNodes = nodes;
        }
        for (const e of g[u]) {
            if (e[0] === p) continue;
            dfs(e[0], u, dist + e[1], newLeft);
        }
        path.pop();
        if (seen) last.set(nums[u], prevPos);
        else last.delete(nums[u]);
    };
    dfs(0, -1, 0, 0);
    return [bestLen, bestNodes];
};

================================================================================
FILE: 3426_manhattan_distances_of_all_arrangements_of_pieces
================================================================================
// LeetCode 3426 - Manhattan Distances of All Arrangements of Pieces
// https://leetcode.com/problems/manhattan-distances-of-all-arrangements-of-pieces/

var distanceSum = function(m, n, k) {
    const mod = 1000000007;
    const modPow = (a, e) => {
        let r = 1n;
        let base = BigInt(a % mod);
        let exp = BigInt(e);
        const MOD = BigInt(mod);
        while (exp > 0n) {
            if (exp & 1n) r = (r * base) % MOD;
            base = (base * base) % MOD;
            exp >>= 1n;
        }
        return Number(r);
    };
    const comb = (nn, kk) => {
        if (kk < 0 || kk > nn) return 0;
        let num = 1, den = 1;
        for (let i = 0; i < kk; i++) {
            num = Number(BigInt(num) * BigInt(nn - i) % BigInt(mod));
            den = Number(BigInt(den) * BigInt(i + 1) % BigInt(mod));
        }
        return Number(BigInt(num) * BigInt(modPow(den, mod - 2)) % BigInt(mod));
    };
    if (k < 2) return 0;
    const totalCells = m * n;
    const pairChoose = comb(totalCells - 2, k - 2);
    let sumDist = 0n;
    for (let d = 1; d < m; d++) sumDist += BigInt(d) * BigInt(m - d) * BigInt(n) * BigInt(n);
    for (let d = 1; d < n; d++) sumDist += BigInt(d) * BigInt(n - d) * BigInt(m) * BigInt(m);
    return Number(sumDist % BigInt(mod) * BigInt(pairChoose) % BigInt(mod));
};

================================================================================
FILE: 3427_sum_of_variable_length_subarrays
================================================================================
// LeetCode 3427 - Sum of Variable Length Subarrays
// https://leetcode.com/problems/sum-of-variable-length-subarrays/

var subarraySum = function(nums) {
    const n = nums.length;
    const pref = new Array(n + 1).fill(0);
    for (let i = 0; i < n; i++) pref[i + 1] = pref[i] + nums[i];
    let ans = 0;
    for (let i = 0; i < n; i++) {
        let start = i - nums[i];
        if (start < 0) start = 0;
        ans += pref[i + 1] - pref[start];
    }
    return ans;
};

================================================================================
FILE: 3428_maximum_and_minimum_sums_of_at_most_size_k_subsequences
================================================================================
// LeetCode 3428 - Maximum and Minimum Sums of at Most Size K Subsequences
// https://leetcode.com/problems/maximum-and-minimum-sums-of-at-most-size-k-subsequences/

var minMaxSums = function(nums, k) {
    const mod = 1000000007;
    nums = nums.slice().sort((a, b) => a - b);
    const n = nums.length;
    const C = Array.from({ length: n + 1 }, () => new Array(k).fill(0));
    for (let i = 0; i <= n; i++) {
        C[i][0] = 1;
        for (let j = 1; j < k && j <= i; j++) C[i][j] = (C[i - 1][j] + C[i - 1][j - 1]) % mod;
    }
    let ans = 0;
    for (let i = 0; i < n; i++) {
        let waysMax = 0;
        for (let j = 0; j < k && j <= i; j++) waysMax = (waysMax + C[i][j]) % mod;
        let waysMin = 0;
        const right = n - i - 1;
        for (let j = 0; j < k && j <= right; j++) waysMin = (waysMin + C[right][j]) % mod;
        ans = (ans + nums[i] * waysMax % mod + nums[i] * waysMin % mod) % mod;
    }
    return ans;
};


================================================================================
# 3635_earliest_finish_time_for_land_and_water_rides_ii
# README: # 3635. Earliest Finish Time for Land and Water Rides II
================================================================================
// LeetCode 3635 - Earliest Finish Time for Land and Water Rides II
// https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-ii/

var earliestFinishTime = function(landStartTime, landDuration, waterStartTime, waterDuration) {
    const calc = (a1, t1, a2, t2) => {
        let minEnd = Infinity;
        for (let i = 0; i < a1.length; i++) minEnd = Math.min(minEnd, a1[i] + t1[i]);
        let ans = Infinity;
        for (let i = 0; i < a2.length; i++) ans = Math.min(ans, Math.max(minEnd, a2[i]) + t2[i]);
        return ans;
    };
    return Math.min(
        calc(landStartTime, landDuration, waterStartTime, waterDuration),
        calc(waterStartTime, waterDuration, landStartTime, landDuration));
};


================================================================================
# 3636_threshold_majority_queries
# README: # 3636. Threshold Majority Queries
================================================================================
// LeetCode 3636 - Threshold Majority Queries
// https://leetcode.com/problems/threshold-majority-queries/

var subarrayMajority = function(nums, queries) {
    const ans = new Array(queries.length);
    for (let qi = 0; qi < queries.length; qi++) {
        const l = queries[qi][0], r = queries[qi][1], t = queries[qi][2];
        const cnt = new Map();
        for (let i = l; i <= r; i++) cnt.set(nums[i], (cnt.get(nums[i]) || 0) + 1);
        let best = -1, bestC = 0;
        for (const [v, c] of cnt) {
            if (c >= t && (c > bestC || (c === bestC && (best === -1 || v < best)))) {
                bestC = c;
                best = v;
            }
        }
        ans[qi] = best;
    }
    return ans;
};


================================================================================
# 3637_trionic_array_i
# README: # 3637. Trionic Array I
================================================================================
// LeetCode 3637 - Trionic Array I
// https://leetcode.com/problems/trionic-array-i/

var isTrionic = function(nums) {
    const n = nums.length;
    let p = 0;
    while (p < n - 2 && nums[p] < nums[p + 1]) p++;
    if (p === 0) return false;
    let q = p;
    while (q < n - 1 && nums[q] > nums[q + 1]) q++;
    if (q === p || q === n - 1) return false;
    while (q < n - 1 && nums[q] < nums[q + 1]) q++;
    return q === n - 1;
};


================================================================================
# 3638_maximum_balanced_shipments
# README: # 3638. Maximum Balanced Shipments
================================================================================
// LeetCode 3638 - Maximum Balanced Shipments
// https://leetcode.com/problems/maximum-balanced-shipments/

var maxBalancedShipments = function(weight) {
    let ans = 0, mx = 0;
    for (const x of weight) {
        mx = Math.max(mx, x);
        if (x < mx) {
            ans++;
            mx = 0;
        }
    }
    return ans;
};


================================================================================
# 3639_minimum_time_to_activate_string
# README: # 3639. Minimum Time to Activate String
================================================================================
// LeetCode 3639 - Minimum Time to Activate String
// https://leetcode.com/problems/minimum-time-to-activate-string/

var minTime = function(s, order, k) {
    const n = s.length;
    const total = n * (n + 1) / 2;
    if (k > total) return -1;
    const countValid = (t) => {
        const star = new Array(n).fill(false);
        for (let i = 0; i <= t; i++) star[order[i]] = true;
        let invalid = 0;
        for (let i = 0; i < n;) {
            if (star[i]) { i++; continue; }
            let j = i;
            while (j < n && !star[j]) j++;
            const L = j - i;
            invalid += L * (L + 1) / 2;
            i = j;
        }
        return total - invalid;
    };
    let lo = 0, hi = n - 1, ans = -1;
    while (lo <= hi) {
        const mid = (lo + hi) >> 1;
        if (countValid(mid) >= k) {
            ans = mid;
            hi = mid - 1;
        } else lo = mid + 1;
    }
    return ans;
};


================================================================================
# 3640_trionic_array_ii
# README: # 3640. Trionic Array II
================================================================================
// LeetCode 3640 - Trionic Array II
// https://leetcode.com/problems/trionic-array-ii/

var maxSumTrionic = function(nums) {
    const n = nums.length;
    let i = 0;
    let ans = -Infinity;
    while (i < n) {
        const l = i;
        for (i++; i < n && nums[i - 1] < nums[i];) i++;
        if (i === l + 1) continue;
        const p = i - 1;
        let s = nums[p - 1] + nums[p];
        while (i < n && nums[i - 1] > nums[i]) {
            s += nums[i];
            i++;
        }
        if (i === p + 1 || i === n || nums[i - 1] === nums[i]) continue;
        const q = i - 1;
        s += nums[i];
        i++;
        let mx = 0, t = 0;
        while (i < n && nums[i - 1] < nums[i]) {
            t += nums[i];
            i++;
            mx = Math.max(mx, t);
        }
        s += mx;
        mx = t = 0;
        for (let j = p - 2; j >= l; j--) {
            t += nums[j];
            mx = Math.max(mx, t);
        }
        s += mx;
        ans = Math.max(ans, s);
        i = q;
    }
    return ans;
};


================================================================================
# 3641_longest_semi_repeating_subarray
# README: # 3641. Longest Semi-Repeating Subarray
================================================================================
// LeetCode 3641 - Longest Semi-Repeating Subarray
// https://leetcode.com/problems/longest-semi-repeating-subarray/

var longestSubarray = function(nums, k) {
    const cnt = new Map();
    let ans = 0, cur = 0, l = 0;
    for (let r = 0; r < nums.length; r++) {
        const c = (cnt.get(nums[r]) || 0) + 1;
        cnt.set(nums[r], c);
        if (c === 2) cur++;
        while (cur > k) {
            const c2 = (cnt.get(nums[l]) || 0) - 1;
            cnt.set(nums[l], c2);
            if (c2 === 1) cur--;
            l++;
        }
        ans = Math.max(ans, r - l + 1);
    }
    return ans;
};


================================================================================
# 3643_flip_square_submatrix_vertically
# README: # 3643. Flip Square Submatrix Vertically
================================================================================
// LeetCode 3643 - Flip Square Submatrix Vertically
// https://leetcode.com/problems/flip-square-submatrix-vertically/

var reverseSubmatrix = function(grid, x, y, k) {
    for (let i = x; i < x + Math.floor(k / 2); i++) {
        const i2 = x + k - 1 - (i - x);
        for (let j = y; j < y + k; j++) {
            const tmp = grid[i][j];
            grid[i][j] = grid[i2][j];
            grid[i2][j] = tmp;
        }
    }
    return grid;
};


================================================================================
# 3644_maximum_k_to_sort_a_permutation
# README: # 3644. Maximum K to Sort a Permutation
================================================================================
// LeetCode 3644 - Maximum K to Sort a Permutation
// https://leetcode.com/problems/maximum-k-to-sort-a-permutation/

var sortPermutation = function(nums) {
    let ans = -1;
    for (let i = 0; i < nums.length; i++)
        if (i !== nums[i]) ans &= nums[i];
    return Math.max(ans, 0);
};


================================================================================
# 3645_maximum_total_from_optimal_activation_order
# README: # 3645. Maximum Total from Optimal Activation Order
================================================================================
// LeetCode 3645 - Maximum Total from Optimal Activation Order
// https://leetcode.com/problems/maximum-total-from-optimal-activation-order/

var maxTotal = function(value, limit) {
    const g = new Map();
    for (let i = 0; i < value.length; i++) {
        if (!g.has(limit[i])) g.set(limit[i], []);
        g.get(limit[i]).push(value[i]);
    }
    let ans = 0;
    for (const [lim, vs] of g) {
        vs.sort((a, b) => b - a);
        for (let i = 0; i < Math.min(lim, vs.length); i++) ans += vs[i];
    }
    return ans;
};


================================================================================
# 3646_next_special_palindrome_number
# README: # 3646. Next Special Palindrome Number
================================================================================
// LeetCode 3646 - Next Special Palindrome Number
// https://leetcode.com/problems/next-special-palindrome-number/

var specialPalindrome = function(n) {
    const cands = [];
    let halfCnt, mid, halfLen;
    const dfs = (pos, cur) => {
        if (pos === halfLen) {
            const left = cur.join('');
            let s = left;
            if (mid > 0) s += mid;
            for (let i = left.length - 1; i >= 0; i--) s += left[i];
            cands.push(Number(s));
            return;
        }
        for (let d = 1; d <= 9; d++) {
            if (halfCnt[d] === 0) continue;
            halfCnt[d]--;
            cur.push(d);
            dfs(pos + 1, cur);
            cur.pop();
            halfCnt[d]++;
        }
    };
    const gen = (mask) => {
        let total = 0, odd = 0;
        for (let d = 1; d <= 9; d++) {
            if (((mask >> d) & 1) !== 0) {
                total += d;
                if (d % 2 === 1) odd++;
            }
        }
        if (total === 0 || total > 18 || odd > 1) return;
        halfCnt = new Array(10).fill(0);
        mid = 0;
        for (let d = 1; d <= 9; d++) {
            if (((mask >> d) & 1) === 0) continue;
            halfCnt[d] = Math.floor(d / 2);
            if (d % 2 === 1) mid = d;
        }
        halfLen = Math.floor(total / 2);
        dfs(0, []);
    };
    for (let mask = 1; mask < (1 << 10); mask++) {
        if ((mask & 1) !== 0) continue;
        gen(mask);
    }
    cands.sort((a, b) => a - b);
    for (const v of cands)
        if (v > n) return v;
    return -1;
};


================================================================================
# 3647_maximum_weight_in_two_bags
# README: # 3647. Maximum Weight in Two Bags
================================================================================
// LeetCode 3647 - Maximum Weight in Two Bags
// https://leetcode.com/problems/maximum-weight-in-two-bags/

var maxWeight = function(weights, w1, w2) {
    const f = Array.from({length: w1 + 1}, () => new Array(w2 + 1).fill(0));
    for (const x of weights) {
        for (let j = w1; j >= 0; j--) {
            for (let k = w2; k >= 0; k--) {
                if (x <= j) f[j][k] = Math.max(f[j][k], f[j - x][k] + x);
                if (x <= k) f[j][k] = Math.max(f[j][k], f[j][k - x] + x);
            }
        }
    }
    return f[w1][w2];
};


================================================================================
# 3648_minimum_sensors_to_cover_grid
# README: # 3648. Minimum Sensors to Cover Grid
================================================================================
// LeetCode 3648 - Minimum Sensors to Cover Grid
// https://leetcode.com/problems/minimum-sensors-to-cover-grid/

var minSensors = function(n, m, k) {
    const cover = 2 * k + 1;
    return Math.ceil(n / cover) * Math.ceil(m / cover);
};


================================================================================
# 3649_number_of_perfect_pairs
# README: # 3649. Number of Perfect Pairs
================================================================================
// LeetCode 3649 - Number of Perfect Pairs
// https://leetcode.com/problems/number-of-perfect-pairs/

var perfectPairs = function(nums) {
    const n = nums.length;
    const absNums = nums.map(Math.abs).sort((a, b) => a - b);
    let ans = 0, j = 0;
    for (let i = 0; i < n; i++) {
        if (j < i + 1) j = i + 1;
        while (j < n && absNums[j] <= 2 * absNums[i]) j++;
        ans += j - i - 1;
    }
    return ans;
};


================================================================================
# 3650_minimum_cost_path_with_edge_reversals
# README: # 3650. Minimum Cost Path with Edge Reversals
================================================================================
// LeetCode 3650 - Minimum Cost Path with Edge Reversals
// https://leetcode.com/problems/minimum-cost-path-with-edge-reversals/

var minCost = function(n, edges) {
    const g = Array.from({length: n}, () => []);
    for (const e of edges) {
        const u = e[0], v = e[1], w = e[2];
        g[u].push([v, w]);
        g[v].push([u, w * 2]);
    }
    const inf = 1073741823;
    const dist = new Array(n).fill(inf);
    dist[0] = 0;
    const pq = [[0, 0]];
    while (pq.length) {
        pq.sort((a, b) => a[0] - b[0]);
        const cur = pq.shift();
        const d = cur[0], u = cur[1];
        if (d > dist[u]) continue;
        if (u === n - 1) return d;
        for (const e of g[u]) {
            const v = e[0], w = e[1];
            const nd = d + w;
            if (nd < dist[v]) {
                dist[v] = nd;
                pq.push([nd, v]);
            }
        }
    }
    return -1;
};


================================================================================
# 3651_minimum_cost_path_with_teleportations
# README: # 3651. Minimum Cost Path with Teleportations
================================================================================
// LeetCode 3651 - Minimum Cost Path with Teleportations
// https://leetcode.com/problems/minimum-cost-path-with-teleportations/

var minCost = function(grid, k) {
    const m = grid.length, n = grid[0].length;
    const inf = 536870911;
    const f = Array.from({length: k + 1}, () =>
        Array.from({length: m}, () => new Array(n).fill(inf)));
    f[0][0][0] = 0;
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (i > 0) f[0][i][j] = Math.min(f[0][i][j], f[0][i - 1][j] + grid[i][j]);
            if (j > 0) f[0][i][j] = Math.min(f[0][i][j], f[0][i][j - 1] + grid[i][j]);
        }
    }
    const g = new Map();
    for (let i = 0; i < m; i++)
        for (let j = 0; j < n; j++) {
            if (!g.has(grid[i][j])) g.set(grid[i][j], []);
            g.get(grid[i][j]).push([i, j]);
        }
    const keys = [...g.keys()].sort((a, b) => b - a);
    for (let t = 1; t <= k; t++) {
        let mn = inf;
        for (const key of keys) {
            const pos = g.get(key);
            for (const p of pos) mn = Math.min(mn, f[t - 1][p[0]][p[1]]);
            for (const p of pos) f[t][p[0]][p[1]] = mn;
        }
        for (let i = 0; i < m; i++) {
            for (let j = 0; j < n; j++) {
                if (i > 0) f[t][i][j] = Math.min(f[t][i][j], f[t][i - 1][j] + grid[i][j]);
                if (j > 0) f[t][i][j] = Math.min(f[t][i][j], f[t][i][j - 1] + grid[i][j]);
            }
        }
    }
    let ans = inf;
    for (let t = 0; t <= k; t++) ans = Math.min(ans, f[t][m - 1][n - 1]);
    return ans;
};


================================================================================
# 3652_best_time_to_buy_and_sell_stock_using_strategy
# README: # 3652. Best Time to Buy and Sell Stock using Strategy
================================================================================
// LeetCode 3652 - Best Time to Buy and Sell Stock using Strategy
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-using-strategy/

var maxProfit = function(prices, strategy, k) {
    const n = prices.length;
    const s = new Array(n + 1).fill(0);
    const t = new Array(n + 1).fill(0);
    for (let i = 1; i <= n; i++) {
        s[i] = s[i - 1] + prices[i - 1] * strategy[i - 1];
        t[i] = t[i - 1] + prices[i - 1];
    }
    let ans = s[n];
    for (let i = k; i <= n; i++)
        ans = Math.max(ans, s[n] - (s[i] - s[i - k]) + (t[i] - t[i - Math.floor(k / 2)]));
    return ans;
};


================================================================================
# 3653_xor_after_range_multiplication_queries_i
# README: # 3653. XOR After Range Multiplication Queries I
================================================================================
// LeetCode 3653 - XOR After Range Multiplication Queries I
// https://leetcode.com/problems/xor-after-range-multiplication-queries-i/

var xorAfterQueries = function(nums, queries) {
    const mod = 1000000007;
    for (const q of queries) {
        const l = q[0], r = q[1], k = q[2], v = q[3];
        for (let idx = l; idx <= r; idx += k)
            nums[idx] = Number(BigInt(nums[idx]) * BigInt(v) % BigInt(mod));
    }
    let ans = 0;
    for (const x of nums) ans ^= x;
    return ans;
};


================================================================================
# 3654_minimum_sum_after_divisible_sum_deletions
# README: # 3654. Minimum Sum After Divisible Sum Deletions
================================================================================
// LeetCode 3654 - Minimum Sum After Divisible Sum Deletions
// https://leetcode.com/problems/minimum-sum-after-divisible-sum-deletions/

var minArraySum = function(nums, k) {
    const n = nums.length;
    const prefix = new Array(n + 1).fill(0);
    for (let i = 0; i < n; i++) prefix[i + 1] = (prefix[i] + nums[i]) % k;
    const inf = Number.MAX_SAFE_INTEGER / 2;
    const dp = new Array(n + 1).fill(0);
    const best = new Array(k).fill(inf);
    best[0] = 0;
    for (let i = 1; i <= n; i++) {
        dp[i] = dp[i - 1] + nums[i - 1];
        if (best[prefix[i]] < dp[i]) dp[i] = best[prefix[i]];
        if (dp[i] < best[prefix[i]]) best[prefix[i]] = dp[i];
    }
    return dp[n];
};


================================================================================
# 3655_xor_after_range_multiplication_queries_ii
# README: # 3655. XOR After Range Multiplication Queries II
================================================================================
// LeetCode 3655 - XOR After Range Multiplication Queries II
// https://leetcode.com/problems/xor-after-range-multiplication-queries-ii/

var xorAfterQueries = function(nums, queries) {
    const MOD = 1000000007n;
    const n = nums.length;
    const byK = new Map();
    for (const q of queries) {
        if (!byK.has(q[2])) byK.set(q[2], []);
        byK.get(q[2]).push(q);
    }
    const res = nums.slice();
    for (const [, list] of byK) {
        const fac = new Array(n).fill(1n);
        for (const u of list)
            for (let i = u[0]; i <= u[1]; i += u[2])
                fac[i] = fac[i] * BigInt(u[3]) % MOD;
        for (let i = 0; i < n; i++)
            res[i] = Number(BigInt(res[i]) * fac[i] % MOD);
    }
    let ans = 0;
    for (const v of res) ans ^= v;
    return ans;
};


================================================================================
# 3656_determine_if_a_simple_graph_exists
# README: # 3656. Determine if a Simple Graph Exists
================================================================================
// LeetCode 3656 - Determine if a Simple Graph Exists
// https://leetcode.com/problems/determine-if-a-simple-graph-exists/

var simpleGraphExists = function(degrees) {
    const n = degrees.length;
    const d = degrees.slice().sort((a, b) => a - b);
    for (let i = 0, j = n - 1; i < j; i++, j--) {
        const tmp = d[i]; d[i] = d[j]; d[j] = tmp;
    }
    let sum = 0;
    for (const x of d) {
        if (x < 0 || x >= n) return false;
        sum += x;
    }
    if (sum % 2 === 1) return false;
    const prefix = new Array(n + 1).fill(0);
    for (let i = 0; i < n; i++) prefix[i + 1] = prefix[i] + d[i];
    for (let k = 1; k <= n; k++) {
        let right = 0;
        for (let i = k; i < n; i++) right += d[i] < k ? d[i] : k;
        if (prefix[k] > k * (k - 1) + right) return false;
    }
    return true;
};


================================================================================
# 3658_gcd_of_odd_and_even_sums
# README: # 3658. GCD of Odd and Even Sums
================================================================================
// LeetCode 3658 - GCD of Odd and Even Sums
// https://leetcode.com/problems/gcd-of-odd-and-even-sums/

var gcdOfOddEvenSums = function(n) { return n; };


================================================================================
# 3659_partition_array_into_k_distinct_groups
# README: # 3659. Partition Array Into K-Distinct Groups
================================================================================
// LeetCode 3659 - Partition Array Into K-Distinct Groups
// https://leetcode.com/problems/partition-array-into-k-distinct-groups/

var partitionArray = function(nums, k) {
    const n = nums.length;
    if (n % k !== 0) return false;
    const m = n / k;
    let mx = 0;
    for (const x of nums) mx = Math.max(mx, x);
    const cnt = new Array(mx + 1).fill(0);
    for (const x of nums)
        if (++cnt[x] > m) return false;
    return true;
};


================================================================================
# 3660_jump_game_ix
# README: # 3660. Jump Game IX
================================================================================
// LeetCode 3660 - Jump Game IX
// https://leetcode.com/problems/jump-game-ix/

var maxValue = function(nums) {
    const n = nums.length;
    const ans = new Array(n);
    const preMax = new Array(n);
    preMax[0] = nums[0];
    for (let i = 1; i < n; i++) preMax[i] = Math.max(preMax[i - 1], nums[i]);
    let sufMin = 1073741823;
    for (let i = n - 1; i >= 0; i--) {
        if (preMax[i] > sufMin) ans[i] = ans[i + 1];
        else ans[i] = preMax[i];
        sufMin = Math.min(sufMin, nums[i]);
    }
    return ans;
};


================================================================================
# 3661_maximum_walls_destroyed_by_robots
# README: # 3661. Maximum Walls Destroyed by Robots
================================================================================
// LeetCode 3661 - Maximum Walls Destroyed by Robots
// https://leetcode.com/problems/maximum-walls-destroyed-by-robots/

var maxWalls = function(robots, distance, walls) {
    const n = robots.length;
    const arr = Array.from({length: n}, (_, i) => [robots[i], distance[i]]);
    arr.sort((a, b) => a[0] - b[0]);
    walls = walls.slice().sort((a, b) => a - b);
    const lowerBound = (a, target) => {
        let lo = 0, hi = a.length;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (a[mid] < target) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    };
    const memo = new Map();
    const dfs = (i, j) => {
        if (i < 0) return 0;
        const key = (i << 1) | j;
        if (memo.has(key)) return memo.get(key);
        let left = arr[i][0] - arr[i][1];
        if (i > 0) left = Math.max(left, arr[i - 1][0] + 1);
        let l = lowerBound(walls, left);
        let r = lowerBound(walls, arr[i][0] + 1);
        let ans = dfs(i - 1, 0) + (r - l);
        let right = arr[i][0] + arr[i][1];
        if (i + 1 < arr.length) {
            if (j === 0) right = Math.min(right, arr[i + 1][0] - arr[i + 1][1] - 1);
            else right = Math.min(right, arr[i + 1][0] - 1);
        }
        l = lowerBound(walls, arr[i][0]);
        r = lowerBound(walls, right + 1);
        ans = Math.max(ans, dfs(i - 1, 1) + (r - l));
        memo.set(key, ans);
        return ans;
    };
    return dfs(n - 1, 1);
};


================================================================================
# 3662_filter_characters_by_frequency
# README: # 3662. Filter Characters by Frequency
================================================================================
// LeetCode 3662 - Filter Characters by Frequency
// https://leetcode.com/problems/filter-characters-by-frequency/

var filterCharacters = function(s, k) {
    const cnt = new Array(26).fill(0);
    for (const c of s) cnt[c.charCodeAt(0) - 97]++;
    let ans = '';
    for (const c of s)
        if (cnt[c.charCodeAt(0) - 97] < k) ans += c;
    return ans;
};


================================================================================
# 3663_find_the_least_frequent_digit
# README: # 3663. Find The Least Frequent Digit
================================================================================
// LeetCode 3663 - Find The Least Frequent Digit
// https://leetcode.com/problems/find-the-least-frequent-digit/

var getLeastFrequentDigit = function(n) {
    const cnt = new Array(10).fill(0);
    let ans = 0, f = 1 << 30;
    for (; n > 0; n = Math.floor(n / 10)) cnt[n % 10]++;
    for (let x = 0; x < 10; x++) {
        if (cnt[x] > 0 && cnt[x] < f) {
            f = cnt[x];
            ans = x;
        }
    }
    return ans;
};


================================================================================
# 3664_two_letter_card_game
# README: # 3664. Two-Letter Card Game
================================================================================
// LeetCode 3664 - Two-Letter Card Game
// https://leetcode.com/problems/two-letter-card-game/

var score = function(cards, x) {
    const pairGroup = (arr) => {
        let total = 0, mx = 0;
        for (let i = 0; i < 26; i++) {
            total += arr[i];
            mx = Math.max(mx, arr[i]);
        }
        let pairs = Math.floor(total / 2);
        if (total - mx < pairs) pairs = total - mx;
        return [pairs, total - 2 * pairs];
    };
    let xx = 0;
    const left = new Array(26).fill(0), right = new Array(26).fill(0);
    for (const c of cards) {
        const a = c[0], b = c[1];
        if (a === x && b === x) xx++;
        else if (a === x) left[b.charCodeAt(0) - 97]++;
        else if (b === x) right[a.charCodeAt(0) - 97]++;
    }
    const lp = pairGroup(left), rp = pairGroup(right);
    let ans = lp[0] + rp[0];
    const rem = lp[1] + rp[1];
    const use = Math.min(xx, rem);
    ans += use;
    xx -= use;
    ans += Math.floor(xx / 2);
    return ans;
};


================================================================================
# 3665_twisted_mirror_path_count
# README: # 3665. Twisted Mirror Path Count
================================================================================
// LeetCode 3665 - Twisted Mirror Path Count
// https://leetcode.com/problems/twisted-mirror-path-count/

var uniquePaths = function(grid) {
    const MOD = 1000000007;
    const m = grid.length, n = grid[0].length;
    const nextCell = (i, j, di, dj) => {
        let ni = i + di, nj = j + dj;
        while (ni >= 0 && nj >= 0 && ni < m && nj < n && grid[ni][nj] === 1) {
            if (dj === 1) { di = 1; dj = 0; }
            else { di = 0; dj = 1; }
            ni += di;
            nj += dj;
        }
        if (ni < 0 || nj < 0 || ni >= m || nj >= n) return null;
        return [ni, nj];
    };
    const dp = Array.from({length: m}, () => new Array(n).fill(0));
    if (grid[0][0] === 1) return 0;
    dp[0][0] = 1;
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (grid[i][j] === 1 || dp[i][j] === 0) continue;
            const a = nextCell(i, j, 0, 1);
            if (a) dp[a[0]][a[1]] = (dp[a[0]][a[1]] + dp[i][j]) % MOD;
            const b = nextCell(i, j, 1, 0);
            if (b) dp[b[0]][b[1]] = (dp[b[0]][b[1]] + dp[i][j]) % MOD;
        }
    }
    return dp[m - 1][n - 1];
};


================================================================================
# 3666_minimum_operations_to_equalize_binary_string
# README: # 3666. Minimum Operations to Equalize Binary String
================================================================================
// LeetCode 3666 - Minimum Operations to Equalize Binary String
// https://leetcode.com/problems/minimum-operations-to-equalize-binary-string/

var minOperations = function(s, k) {
    const n = s.length;
    const ts = [new Set(), new Set()];
    for (let i = 0; i <= n; i++) ts[i % 2].add(i);
    let cnt0 = 0;
    for (const c of s) if (c === '0') cnt0++;
    ts[cnt0 % 2].delete(cnt0);
    let q = [cnt0];
    let ans = 0;
    while (q.length) {
        const nq = [];
        for (const cur of q) {
            if (cur === 0) return ans;
            const l = cur + k - 2 * Math.min(cur, k);
            const r = cur + k - 2 * Math.max(k - n + cur, 0);
            const t = ts[l % 2];
            const sorted = [...t].sort((a, b) => a - b);
            for (const it of sorted) {
                if (it < l) continue;
                if (it > r) break;
                nq.push(it);
                t.delete(it);
            }
        }
        q = nq;
        ans++;
    }
    return -1;
};


================================================================================
# 3667_sort_array_by_absolute_value
# README: # 3667. Sort Array By Absolute Value
================================================================================
// LeetCode 3667 - Sort Array By Absolute Value
// https://leetcode.com/problems/sort-array-by-absolute-value/

var sortByAbsoluteValue = function(nums) {
    nums.sort((a, b) => Math.abs(a) - Math.abs(b));
    return nums;
};


================================================================================
# 3668_restore_finishing_order
# README: # 3668. Restore Finishing Order
================================================================================
// LeetCode 3668 - Restore Finishing Order
// https://leetcode.com/problems/restore-finishing-order/

var recoverOrder = function(order, friends) {
    const n = order.length;
    const d = new Array(n + 1).fill(0);
    for (let i = 0; i < n; i++) d[order[i]] = i;
    friends.sort((a, b) => d[a] - d[b]);
    return friends;
};


================================================================================
# 3669_balanced_k_factor_decomposition
# README: # 3669. Balanced K-Factor Decomposition
================================================================================
// LeetCode 3669 - Balanced K-Factor Decomposition
// https://leetcode.com/problems/balanced-k-factor-decomposition/

var minDifference = function(n, k) {
    const MX = 100001;
    if (!minDifference._g) {
        const g = Array.from({length: MX}, () => []);
        for (let i = 1; i < MX; i++)
            for (let j = i; j < MX; j += i) g[j].push(i);
        minDifference._g = g;
    }
    const g = minDifference._g;
    let cur = Infinity;
    let ans = [];
    const path = new Array(k);
    const dfs = (i, x, mi, mx) => {
        if (i === 0) {
            const d = Math.max(mx, x) - Math.min(mi, x);
            if (d < cur) {
                cur = d;
                path[i] = x;
                ans = path.slice();
            }
            return;
        }
        for (const y of g[x]) {
            path[i] = y;
            dfs(i - 1, Math.floor(x / y), Math.min(mi, y), Math.max(mx, y));
        }
    };
    dfs(k - 1, n, Infinity, 0);
    return ans;
};


================================================================================
# 3670_maximum_product_of_two_integers_with_no_common_bits
# README: # 3670. Maximum Product of Two Integers With No Common Bits
================================================================================
// LeetCode 3670 - Maximum Product of Two Integers With No Common Bits
// https://leetcode.com/problems/maximum-product-of-two-integers-with-no-common-bits/

var maxProduct = function(nums) {
    let maxV = 0;
    for (const v of nums) if (v > maxV) maxV = v;
    let bitsN = 0;
    for (let x = maxV; x > 0; x >>= 1) bitsN++;
    if (bitsN === 0) bitsN = 1;
    const size = 1 << bitsN;
    const best = new Array(size).fill(0);
    for (const v of nums) if (v > best[v]) best[v] = v;
    for (let mask = 0; mask < size; mask++) {
        for (let b = 0; b < bitsN; b++) {
            if ((mask & (1 << b)) !== 0) {
                const sub = mask ^ (1 << b);
                if (best[sub] > best[mask]) best[mask] = best[sub];
            }
        }
    }
    let ans = 0;
    for (const v of nums) {
        const comp = (size - 1) ^ v;
        if (best[comp] > 0) {
            const p = v * best[comp];
            if (p > ans) ans = p;
        }
    }
    return ans;
};


================================================================================
# 3671_sum_of_beautiful_subsequences
# README: # 3671. Sum of Beautiful Subsequences
================================================================================
// LeetCode 3671 - Sum of Beautiful Subsequences
// https://leetcode.com/problems/sum-of-beautiful-subsequences/

var totalBeauty = function(nums) {
    const MOD = 1000000007;
    let mx = 0;
    for (const v of nums) if (v > mx) mx = v;
    const pos = Array.from({length: mx + 1}, () => []);
    for (let i = 0; i < nums.length; i++) pos[nums[i]].push(i);
    const cnt = new Array(mx + 1).fill(0);
    for (let g = 1; g <= mx; g++) {
        const seq = [];
        for (let m = g; m <= mx; m += g) seq.push(...pos[m]);
        if (seq.length === 0) continue;
        seq.sort((a, b) => a - b);
        let ways = 1;
        for (let i = 0; i < seq.length; i++) ways = (ways * 2) % MOD;
        cnt[g] = (ways - 1 + MOD) % MOD;
    }
    let ans = 0;
    for (let g = mx; g >= 1; g--) {
        for (let m = 2 * g; m <= mx; m += g)
            cnt[g] = (cnt[g] - cnt[m] + MOD) % MOD;
        ans = (ans + cnt[g] * g) % MOD;
    }
    return ans;
};


================================================================================
# 3672_sum_of_weighted_modes_in_subarrays
# README: # 3672. Sum of Weighted Modes in Subarrays
================================================================================
// LeetCode 3672 - Sum of Weighted Modes in Subarrays
// https://leetcode.com/problems/sum-of-weighted-modes-in-subarrays/

var modeWeight = function(nums, k) {
    const cnt = new Map();
    const pq = [];
    const push = (freq, val) => {
        pq.push([freq, -val]);
        pq.sort((a, b) => a[0] !== b[0] ? b[0] - a[0] : a[1] - b[1]);
    };
    const getMode = () => {
        while (true) {
            const top = pq[0];
            const freq = top[0], val = -top[1];
            if ((cnt.get(val) || 0) === freq) return freq * val;
            pq.shift();
        }
    };
    for (let i = 0; i < k; i++) {
        const x = nums[i];
        cnt.set(x, (cnt.get(x) || 0) + 1);
        push(cnt.get(x), x);
    }
    let ans = getMode();
    for (let i = k; i < nums.length; i++) {
        const x = nums[i], y = nums[i - k];
        cnt.set(x, (cnt.get(x) || 0) + 1);
        cnt.set(y, (cnt.get(y) || 0) - 1);
        push(cnt.get(x), x);
        push(cnt.get(y), y);
        ans += getMode();
    }
    return ans;
};


================================================================================
# 3674_minimum_operations_to_equalize_array
# README: # 3674. Minimum Operations to Equalize Array
================================================================================
// LeetCode 3674 - Minimum Operations to Equalize Array
// https://leetcode.com/problems/minimum-operations-to-equalize-array/

var minOperations = function(nums) {
    for (const x of nums) if (x !== nums[0]) return 1;
    return 0;
};


================================================================================
# 3675_minimum_operations_to_transform_string
# README: # 3675. Minimum Operations to Transform String
================================================================================
// LeetCode 3675 - Minimum Operations to Transform String
// https://leetcode.com/problems/minimum-operations-to-transform-string/

var minOperations = function(s) {
    let ans = 0;
    for (const c of s) {
        if (c !== 'a') ans = Math.max(ans, 26 - (c.charCodeAt(0) - 97));
    }
    return ans;
};


================================================================================
# 3676_count_bowl_subarrays
# README: # 3676. Count Bowl Subarrays
================================================================================
// LeetCode 3676 - Count Bowl Subarrays
// https://leetcode.com/problems/count-bowl-subarrays/

var bowlSubarrays = function(nums) {
    const n = nums.length;
    let ans = 0;
    const ngr = new Array(n).fill(-1);
    const ngl = new Array(n).fill(-1);
    const stack = [];
    for (let i = n - 1; i >= 0; i--) {
        while (stack.length && nums[stack[stack.length - 1]] < nums[i]) stack.pop();
        if (stack.length) ngr[i] = stack[stack.length - 1];
        stack.push(i);
    }
    stack.length = 0;
    for (let i = 0; i < n; i++) {
        while (stack.length && nums[stack[stack.length - 1]] < nums[i]) stack.pop();
        if (stack.length) ngl[i] = stack[stack.length - 1];
        stack.push(i);
    }
    for (let i = 0; i < n; i++) {
        if (ngr[i] !== -1 && ngr[i] - i >= 2) ans++;
        if (ngl[i] !== -1 && i - ngl[i] >= 2) ans++;
    }
    return ans;
};


================================================================================
# 3677_count_binary_palindromic_numbers
# README: # 3677. Count Binary Palindromic Numbers
================================================================================
// LeetCode 3677 - Count Binary Palindromic Numbers
// https://leetcode.com/problems/count-binary-palindromic-numbers/

var countBinaryPalindromes = function(n) {
    if (n === 0) return 1;
    let ans = 1;
    let s = '';
    for (let x = n; x > 0; x = Math.floor(x / 2)) s += String(x & 1);
    s = s.split('').reverse().join('');
    const L = s.length;
    for (let len = 1; len < L; len++) {
        const half = Math.floor((len + 1) / 2);
        ans += 1 << (half - 1);
    }
    const half = Math.floor((L + 1) / 2);
    const prefix = s.substring(0, half);
    const start = 1 << (half - 1);
    let prefVal = 0;
    for (const c of prefix) prefVal = (prefVal << 1) | (c.charCodeAt(0) - 48);
    ans += prefVal - start;
    let pal = prefix;
    for (let i = half - 1 - (L % 2); i >= 0; i--) pal += prefix[i];
    let pval = 0;
    for (const c of pal) pval = (pval << 1) | (c.charCodeAt(0) - 48);
    if (pval <= n) ans++;
    return ans;
};


================================================================================
# 3678_smallest_absent_positive_greater_than_average
# README: # 3678. Smallest Absent Positive Greater Than Average
================================================================================
// LeetCode 3678 - Smallest Absent Positive Greater Than Average
// https://leetcode.com/problems/smallest-absent-positive-greater-than-average/

var smallestAbsent = function(nums) {
    const s = new Set();
    let sum = 0;
    for (const x of nums) {
        s.add(x);
        sum += x;
    }
    let ans = Math.max(1, Math.floor(sum / nums.length) + 1);
    while (s.has(ans)) ans++;
    return ans;
};


================================================================================
# 3679_minimum_discards_to_balance_inventory
# README: # 3679.  Minimum Discards to Balance Inventory
================================================================================
// LeetCode 3679 - Minimum Discards to Balance Inventory
// https://leetcode.com/problems/minimum-discards-to-balance-inventory/

var minArrivalsToDiscard = function(arrivals, w, m) {
    const cnt = new Map();
    const n = arrivals.length;
    const marked = new Array(n).fill(0);
    let ans = 0;
    for (let i = 0; i < n; i++) {
        const x = arrivals[i];
        if (i >= w) cnt.set(arrivals[i - w], (cnt.get(arrivals[i - w]) || 0) - marked[i - w]);
        if ((cnt.get(x) || 0) >= m) ans++;
        else {
            marked[i] = 1;
            cnt.set(x, (cnt.get(x) || 0) + 1);
        }
    }
    return ans;
};


================================================================================
# 3680_generate_schedule
# README: # 3680. Generate Schedule
================================================================================
// LeetCode 3680 - Generate Schedule
// https://leetcode.com/problems/generate-schedule/

var generateSchedule = function(n) {
    if (n < 5) return [];
    const matches = [];
    for (let i = 0; i < n; i++)
        for (let j = 0; j < n; j++)
            if (i !== j) matches.push([i, j]);
    const used = new Array(matches.length).fill(false);
    const sched = [];
    let last0 = -1, last1 = -1;
    const dfs = () => {
        if (sched.length === matches.length) return true;
        for (let i = 0; i < matches.length; i++) {
            if (used[i]) continue;
            const m = matches[i];
            if (m[0] === last0 || m[0] === last1 || m[1] === last0 || m[1] === last1) continue;
            used[i] = true;
            sched.push(m);
            const p0 = last0, p1 = last1;
            last0 = m[0];
            last1 = m[1];
            if (dfs()) return true;
            last0 = p0;
            last1 = p1;
            sched.pop();
            used[i] = false;
        }
        return false;
    };
    if (dfs()) return sched;
    return [];
};


================================================================================
# 3681_maximum_xor_of_subsequences
# README: # 3681. Maximum XOR of Subsequences
================================================================================
// LeetCode 3681 - Maximum XOR of Subsequences
// https://leetcode.com/problems/maximum-xor-of-subsequences/

var maxXorSubsequences = function(nums) {
    const basis = new Array(32).fill(0);
    for (const x of nums) {
        let cur = x;
        for (let b = 31; b >= 0; b--) {
            if ((cur & (1 << b)) === 0) continue;
            if (basis[b] === 0) {
                basis[b] = cur;
                break;
            }
            cur ^= basis[b];
        }
    }
    let ans = 0;
    for (let b = 31; b >= 0; b--) {
        if ((ans ^ basis[b]) > ans) ans ^= basis[b];
    }
    return ans;
};


================================================================================
# 3682_minimum_index_sum_of_common_elements
# README: # 3682. Minimum Index Sum of Common Elements
================================================================================
// LeetCode 3682 - Minimum Index Sum of Common Elements
// https://leetcode.com/problems/minimum-index-sum-of-common-elements/

var minimumSum = function(nums1, nums2) {
    const inf = 1 << 30;
    const d = new Map();
    for (let i = 0; i < nums2.length; i++)
        if (!d.has(nums2[i])) d.set(nums2[i], i);
    let ans = inf;
    for (let i = 0; i < nums1.length; i++) {
        if (d.has(nums1[i])) ans = Math.min(ans, i + d.get(nums1[i]));
    }
    return ans === inf ? -1 : ans;
};


================================================================================
# 3683_earliest_time_to_finish_one_task
# README: # 3683. Earliest Time to Finish One Task
================================================================================
// LeetCode 3683 - Earliest Time to Finish One Task
// https://leetcode.com/problems/earliest-time-to-finish-one-task/

var earliestTime = function(tasks) {
    let ans = 200;
    for (const task of tasks) ans = Math.min(ans, task[0] + task[1]);
    return ans;
};


================================================================================
# 3684_maximize_sum_of_at_most_k_distinct_elements
# README: # 3684. Maximize Sum of At Most K Distinct Elements
================================================================================
// LeetCode 3684 - Maximize Sum of At Most K Distinct Elements
// https://leetcode.com/problems/maximize-sum-of-at-most-k-distinct-elements/

var maxKDistinct = function(nums, k) {
    nums.sort((a, b) => a - b);
    const n = nums.length;
    const ans = [];
    for (let i = n - 1; i >= 0; i--) {
        if (i + 1 < n && nums[i] === nums[i + 1]) continue;
        ans.push(nums[i]);
        if (--k === 0) break;
    }
    return ans;
};


================================================================================
# 3685_subsequence_sum_after_capping_elements
# README: # 3685. Subsequence Sum After Capping Elements
================================================================================
// LeetCode 3685 - Subsequence Sum After Capping Elements
// https://leetcode.com/problems/subsequence-sum-after-capping-elements/

var subsequenceSumAfterCapping = function(nums, k) {
    const n = nums.length;
    const sorted = nums.slice().sort((a, b) => a - b);
    const ans = new Array(n);
    const reach = new Array(k + 1).fill(false);
    reach[0] = true;
    let idx = 0;
    for (let x = 1; x <= n; x++) {
        while (idx < n && sorted[idx] <= x) {
            const v = sorted[idx];
            for (let s = k; s >= v; s--) {
                if (reach[s - v]) reach[s] = true;
            }
            idx++;
        }
        const tmp = reach.slice();
        const rem = n - idx;
        for (let s = 0; s <= k; s++) {
            if (!reach[s]) continue;
            for (let t = 1; t <= rem && s + t * x <= k; t++) tmp[s + t * x] = true;
        }
        ans[x - 1] = tmp[k];
    }
    return ans;
};


================================================================================
# 3686_number_of_stable_subsequences
# README: # 3686. Number of Stable Subsequences
================================================================================
// LeetCode 3686 - Number of Stable Subsequences
// https://leetcode.com/problems/number-of-stable-subsequences/

var countStableSubsequences = function(nums) {
    const MOD = 1000000007;
    let a1 = 0, a2 = 0, b1 = 0, b2 = 0;
    for (const x of nums) {
        if (x % 2 === 1) {
            const na1 = (1 + b1 + b2) % MOD;
            const na2 = a1;
            a1 = (a1 + na1) % MOD;
            a2 = (a2 + na2) % MOD;
        } else {
            const nb1 = (1 + a1 + a2) % MOD;
            const nb2 = b1;
            b1 = (b1 + nb1) % MOD;
            b2 = (b2 + nb2) % MOD;
        }
    }
    return (((a1 + a2) % MOD + b1) % MOD + b2) % MOD;
};


================================================================================
# 3687_library_late_fee_calculator
# README: # 3687. Library Late Fee Calculator
================================================================================
// LeetCode 3687 - Library Late Fee Calculator
// https://leetcode.com/problems/library-late-fee-calculator/

var lateFee = function(daysLate) {
    const fee = (x) => {
        if (x === 1) return 1;
        if (x > 5) return 3 * x;
        return 2 * x;
    };
    let ans = 0;
    for (const x of daysLate) ans += fee(x);
    return ans;
};


================================================================================
# 3688_bitwise_or_of_even_numbers_in_an_array
# README: # 3688. Bitwise OR of Even Numbers in an Array
================================================================================
// LeetCode 3688 - Bitwise OR of Even Numbers in an Array
// https://leetcode.com/problems/bitwise-or-of-even-numbers-in-an-array/

var evenNumberBitwiseORs = function(nums) {
    let ans = 0;
    for (const x of nums) if (x % 2 === 0) ans |= x;
    return ans;
};


================================================================================
# 3689_maximum_total_subarray_value_i
# README: # 3689. Maximum Total Subarray Value I
================================================================================
// LeetCode 3689 - Maximum Total Subarray Value I
// https://leetcode.com/problems/maximum-total-subarray-value-i/

var maxTotalValue = function(nums, k) {
    let mn = nums[0], mx = nums[0];
    for (const x of nums) {
        mn = Math.min(mn, x);
        mx = Math.max(mx, x);
    }
    return k * (mx - mn);
};


================================================================================
# 3690_split_and_merge_array_transformation
# README: # 3690. Split and Merge Array Transformation
================================================================================
// LeetCode 3690 - Split and Merge Array Transformation
// https://leetcode.com/problems/split-and-merge-array-transformation/

var minSplitMerge = function(nums1, nums2) {
    const n = nums1.length;
    const toArr = (nums) => {
        const t = new Array(6).fill(0);
        for (let i = 0; i < n; i++) t[i] = nums[i];
        return t;
    };
    const key = (a) => a.join(',');
    const start = toArr(nums1);
    const target = toArr(nums2);
    const vis = new Set([key(start)]);
    let q = [start];
    for (let ans = 0; ; ans++) {
        const nq = [];
        for (const cur of q) {
            if (key(cur) === key(target)) return ans;
            for (let l = 0; l < n; l++) {
                for (let r = l; r < n; r++) {
                    const remain = [];
                    const sub = [];
                    for (let i = 0; i < l; i++) remain.push(cur[i]);
                    for (let i = r + 1; i < n; i++) remain.push(cur[i]);
                    for (let i = l; i <= r; i++) sub.push(cur[i]);
                    for (let pos = 0; pos <= remain.length; pos++) {
                        const nxtSlice = remain.slice(0, pos).concat(sub).concat(remain.slice(pos));
                        const nxt = toArr(nxtSlice);
                        const k = key(nxt);
                        if (!vis.has(k)) {
                            vis.add(k);
                            nq.push(nxt);
                        }
                    }
                }
            }
        }
        q = nq;
    }
};


================================================================================
# 3691_maximum_total_subarray_value_ii
# README: # 3691. Maximum Total Subarray Value II
================================================================================
// LeetCode 3691 - Maximum Total Subarray Value II
// https://leetcode.com/problems/maximum-total-subarray-value-ii/

var maxTotalValue = function(nums, k) {
    class SparseTableRMQ {
        constructor(data) {
            this.n = data.length;
            let maxLog = 0;
            while ((1 << maxLog) <= this.n) maxLog++;
            maxLog++;
            this.fMax = Array.from({length: this.n}, () => new Array(maxLog).fill(0));
            this.fMin = Array.from({length: this.n}, () => new Array(maxLog).fill(0));
            this.lg = new Array(this.n + 1).fill(0);
            for (let i = 2; i <= this.n; i++) this.lg[i] = this.lg[i >> 1] + 1;
            for (let i = 0; i < this.n; i++) {
                this.fMax[i][0] = data[i];
                this.fMin[i][0] = data[i];
            }
            for (let j = 1; j < maxLog; j++) {
                for (let i = 0; i <= this.n - (1 << j); i++) {
                    this.fMax[i][j] = Math.max(this.fMax[i][j - 1], this.fMax[i + (1 << (j - 1))][j - 1]);
                    this.fMin[i][j] = Math.min(this.fMin[i][j - 1], this.fMin[i + (1 << (j - 1))][j - 1]);
                }
            }
        }
        queryMax(l, r) {
            const k = this.lg[r - l + 1];
            return Math.max(this.fMax[l][k], this.fMax[r - (1 << k) + 1][k]);
        }
        queryMin(l, r) {
            const k = this.lg[r - l + 1];
            return Math.min(this.fMin[l][k], this.fMin[r - (1 << k) + 1][k]);
        }
    }
    const n = nums.length;
    const st = new SparseTableRMQ(nums);
    const pq = [];
    for (let l = 0; l < n; l++) {
        const val = st.queryMax(l, n - 1) - st.queryMin(l, n - 1);
        pq.push([val, l, n - 1]);
    }
    pq.sort((a, b) => b[0] - a[0]);
    let ans = 0;
    for (let i = 0; i < k; i++) {
        const top = pq.shift();
        const val = top[0], l = top[1], r = top[2];
        ans += val;
        if (r > l) {
            const nextVal = st.queryMax(l, r - 1) - st.queryMin(l, r - 1);
            pq.push([nextVal, l, r - 1]);
            pq.sort((a, b) => b[0] - a[0]);
        }
    }
    return ans;
};


================================================================================
# 3692_majority_frequency_characters
# README: # 3692. Majority Frequency Characters
================================================================================
// LeetCode 3692 - Majority Frequency Characters
// https://leetcode.com/problems/majority-frequency-characters/

var majorityFrequencyGroup = function(s) {
    const cnt = new Array(26).fill(0);
    for (const c of s) cnt[c.charCodeAt(0) - 97]++;
    const f = new Map();
    for (let i = 0; i < 26; i++) {
        if (cnt[i] > 0) {
            if (!f.has(cnt[i])) f.set(cnt[i], '');
            f.set(cnt[i], f.get(cnt[i]) + String.fromCharCode(97 + i));
        }
    }
    let mx = 0, mv = 0, ans = '';
    for (const [v, cs] of f) {
        if (cs.length > mx || (cs.length === mx && v > mv)) {
            mx = cs.length;
            mv = v;
            ans = cs;
        }
    }
    return ans;
};


================================================================================
# 3693_climbing_stairs_ii
# README: # 3693. Climbing Stairs II
================================================================================
// LeetCode 3693 - Climbing Stairs II
// https://leetcode.com/problems/climbing-stairs-ii/

var climbStairs = function(n, costs) {
    const inf = 1e9;
    const f = new Array(n + 1).fill(inf);
    f[0] = 0;
    for (let i = 1; i <= n; i++) {
        const x = costs[i - 1];
        for (let j = Math.max(0, i - 3); j < i; j++) {
            f[i] = Math.min(f[i], f[j] + x + (i - j) * (i - j));
        }
    }
    return f[n];
};


================================================================================
# 3694_distinct_points_reachable_after_substring_removal
# README: # 3694. Distinct Points Reachable After Substring Removal
================================================================================
// LeetCode 3694 - Distinct Points Reachable After Substring Removal
// https://leetcode.com/problems/distinct-points-reachable-after-substring-removal/

var distinctPoints = function(s, k) {
    const n = s.length;
    const f = new Array(n + 1).fill(0);
    const g = new Array(n + 1).fill(0);
    let x = 0, y = 0;
    for (let i = 1; i <= n; i++) {
        const c = s[i - 1];
        if (c === 'U') y++;
        else if (c === 'D') y--;
        else if (c === 'L') x--;
        else x++;
        f[i] = x;
        g[i] = y;
    }
    const st = new Set();
    for (let i = k; i <= n; i++) {
        const a = f[n] - (f[i] - f[i - k]);
        const b = g[n] - (g[i] - g[i - k]);
        st.add(a + ',' + b);
    }
    return st.size;
};


================================================================================
# 3695_maximize_alternating_sum_using_swaps
# README: # 3695. Maximize Alternating Sum Using Swaps
================================================================================
// LeetCode 3695 - Maximize Alternating Sum Using Swaps
// https://leetcode.com/problems/maximize-alternating-sum-using-swaps/

var maxAlternatingSum = function(nums, swaps) {
    const n = nums.length;
    const parent = Array.from({length: n}, (_, i) => i);
    const find = (x) => {
        if (parent[x] !== x) parent[x] = find(parent[x]);
        return parent[x];
    };
    for (const s of swaps) {
        const a = find(s[0]), b = find(s[1]);
        if (a !== b) parent[a] = b;
    }
    const compVals = new Map();
    const compIdx = new Map();
    for (let i = 0; i < n; i++) {
        const r = find(i);
        if (!compVals.has(r)) { compVals.set(r, []); compIdx.set(r, []); }
        compVals.get(r).push(nums[i]);
        compIdx.get(r).push(i);
    }
    const arr = new Array(n);
    for (const [r, vals] of compVals) {
        const idxs = compIdx.get(r);
        vals.sort((a, b) => b - a);
        const even = [], odd = [];
        for (const i of idxs) {
            if (i % 2 === 0) even.push(i);
            else odd.push(i);
        }
        even.sort((a, b) => a - b);
        odd.sort((a, b) => a - b);
        let ei = 0;
        for (const v of vals) {
            if (ei < even.length) {
                arr[even[ei]] = v;
                ei++;
            } else {
                arr[odd[ei - even.length]] = v;
                ei++;
            }
        }
    }
    let ans = 0;
    for (let i = 0; i < n; i++) {
        if (i % 2 === 0) ans += arr[i];
        else ans -= arr[i];
    }
    return ans;
};


================================================================================
# 3696_maximum_distance_between_unequal_words_in_array_i
# README: # 3696. Maximum Distance Between Unequal Words in Array I
================================================================================
// LeetCode 3696 - Maximum Distance Between Unequal Words in Array I
// https://leetcode.com/problems/maximum-distance-between-unequal-words-in-array-i/

var maxDistance = function(words) {
    const n = words.length;
    let ans = 0;
    for (let i = 0; i < n; i++) {
        if (words[i] !== words[0]) ans = Math.max(ans, i + 1);
        if (words[i] !== words[n - 1]) ans = Math.max(ans, n - i);
    }
    return ans;
};


================================================================================
# 3697_compute_decimal_representation
# README: # 3697. Compute Decimal Representation
================================================================================
// LeetCode 3697 - Compute Decimal Representation
// https://leetcode.com/problems/compute-decimal-representation/

var decimalRepresentation = function(n) {
    const ans = [];
    let p = 1;
    while (n > 0) {
        const v = n % 10;
        n = Math.floor(n / 10);
        if (v !== 0) ans.push(p * v);
        p *= 10;
    }
    ans.reverse();
    return ans;
};


================================================================================
# 3698_split_array_with_minimum_difference
# README: # 3698. Split Array With Minimum Difference
================================================================================
// LeetCode 3698 - Split Array With Minimum Difference
// https://leetcode.com/problems/split-array-with-minimum-difference/

var splitArray = function(nums) {
    const n = nums.length;
    const s = new Array(n);
    const f = new Array(n).fill(true);
    const g = new Array(n).fill(true);
    s[0] = nums[0];
    for (let i = 1; i < n; i++) {
        s[i] = s[i - 1] + nums[i];
        f[i] = f[i - 1];
        if (nums[i] <= nums[i - 1]) f[i] = false;
    }
    for (let i = n - 2; i >= 0; i--) {
        g[i] = g[i + 1];
        if (nums[i] <= nums[i + 1]) g[i] = false;
    }
    const inf = Number.MAX_SAFE_INTEGER / 4;
    let ans = inf;
    for (let i = 0; i < n - 1; i++) {
        if (f[i] && g[i + 1]) {
            const s1 = s[i], s2 = s[n - 1] - s[i];
            ans = Math.min(ans, Math.abs(s1 - s2));
        }
    }
    return ans < inf ? ans : -1;
};


================================================================================
# 3699_number_of_zigzag_arrays_i
# README: # 3699. Number of ZigZag Arrays I
================================================================================
// LeetCode 3699 - Number of ZigZag Arrays I
// https://leetcode.com/problems/number-of-zigzag-arrays-i/

var zigZagArrays = function(n, l, r) {
    const MOD = 1000000007;
    const m = r - l + 1;
    if (n === 1) return m % MOD;
    let up = new Array(m).fill(1);
    let down = new Array(m).fill(1);
    for (let len_ = 2; len_ <= n; len_++) {
        const prefDown = new Array(m + 1).fill(0);
        for (let j = 0; j < m; j++) prefDown[j + 1] = (prefDown[j] + down[j]) % MOD;
        const nup = new Array(m);
        for (let j = 0; j < m; j++) nup[j] = prefDown[j];
        const sufUp = new Array(m + 1).fill(0);
        for (let j = m - 1; j >= 0; j--) sufUp[j] = (sufUp[j + 1] + up[j]) % MOD;
        const ndown = new Array(m);
        for (let j = 0; j < m; j++) ndown[j] = sufUp[j + 1];
        up = nup;
        down = ndown;
    }
    let ans = 0;
    for (let j = 0; j < m; j++) {
        ans = (ans + up[j]) % MOD;
        ans = (ans + down[j]) % MOD;
    }
    return ans;
};


================================================================================
# 3700_number_of_zigzag_arrays_ii
# README: # 3700. Number of ZigZag Arrays II
================================================================================
// LeetCode 3700 - Number of ZigZag Arrays II
// https://leetcode.com/problems/number-of-zigzag-arrays-ii/

var zigZagArrays = function(n, l, r) {
    const MOD = 1000000007;
    const m = r - l + 1;
    if (n === 1) return m % MOD;
    let up = new Array(m).fill(1);
    let down = new Array(m).fill(1);
    for (let length = 2; length <= n; length++) {
        const pref = new Array(m + 1).fill(0);
        for (let j = 0; j < m; j++) pref[j + 1] = (pref[j] + down[j]) % MOD;
        const nup = new Array(m);
        for (let j = 0; j < m; j++) nup[j] = pref[j];
        const suf = new Array(m + 1).fill(0);
        for (let j = m - 1; j >= 0; j--) suf[j] = (suf[j + 1] + up[j]) % MOD;
        const ndown = new Array(m);
        for (let j = 0; j < m; j++) ndown[j] = suf[j + 1];
        up = nup;
        down = ndown;
    }
    let ans = 0;
    for (let j = 0; j < m; j++) {
        ans = (ans + up[j]) % MOD;
        ans = (ans + down[j]) % MOD;
    }
    return ans;
};


================================================================================
# 3701_compute_alternating_sum
# README: # 3701. Compute Alternating Sum
================================================================================
// LeetCode 3701 - Compute Alternating Sum
// https://leetcode.com/problems/compute-alternating-sum/

var alternatingSum = function(nums) {
    let ans = 0;
    for (let i = 0; i < nums.length; i++) {
        if (i % 2 === 0) ans += nums[i];
        else ans -= nums[i];
    }
    return ans;
};


================================================================================
# 3702_longest_subsequence_with_non_zero_bitwise_xor
# README: # 3702. Longest Subsequence With Non-Zero Bitwise XOR
================================================================================
// LeetCode 3702 - Longest Subsequence With Non-Zero Bitwise XOR
// https://leetcode.com/problems/longest-subsequence-with-non-zero-bitwise-xor/

var longestSubsequence = function(nums) {
    let xorv = 0, cnt0 = 0;
    for (const x of nums) {
        xorv ^= x;
        if (x === 0) cnt0++;
    }
    const n = nums.length;
    if (xorv !== 0) return n;
    if (cnt0 === n) return 0;
    return n - 1;
};


================================================================================
# 3703_remove_k_balanced_substrings
# README: # 3703. Remove K-Balanced Substrings
================================================================================
// LeetCode 3703 - Remove K-Balanced Substrings
// https://leetcode.com/problems/remove-k-balanced-substrings/

var removeSubstring = function(s, k) {
    const stk = [];
    for (const c of s) {
        if (stk.length && stk[stk.length - 1][0] === c)
            stk[stk.length - 1][1]++;
        else stk.push([c, 1]);
        if (c === ')' && stk.length > 1) {
            const top = stk[stk.length - 1];
            const prev = stk[stk.length - 2];
            if (top[1] === k && prev[1] >= k) {
                stk.pop();
                prev[1] -= k;
                if (prev[1] === 0) stk.pop();
            }
        }
    }
    let res = '';
    for (const p of stk)
        for (let i = 0; i < p[1]; i++) res += p[0];
    return res;
};


================================================================================
# 3704_count_no_zero_pairs_that_sum_to_n
# README: # 3704. Count No-Zero Pairs That Sum to N
================================================================================
// LeetCode 3704 - Count No-Zero Pairs That Sum to N
// https://leetcode.com/problems/count-no-zero-pairs-that-sum-to-n/

var countNoZeroPairs = function(n) {
    const s = String(n);
    const m = s.length;
    const digits = new Array(m + 1).fill(0);
    for (let i = 0; i < m; i++) digits[i] = s.charCodeAt(m - 1 - i) - 48;
    let dp = Array.from({length: 2}, () => Array.from({length: 2}, () => [0, 0]));
    dp[0][1][1] = 1;
    for (let pos = 0; pos < m + 1; pos++) {
        const ndp = Array.from({length: 2}, () => Array.from({length: 2}, () => [0, 0]));
        const target = digits[pos];
        for (let carry = 0; carry <= 1; carry++) {
            for (let aliveA = 0; aliveA <= 1; aliveA++) {
                for (let aliveB = 0; aliveB <= 1; aliveB++) {
                    const ways = dp[carry][aliveA][aliveB];
                    if (ways === 0) continue;
                    const A = [];
                    if (aliveA === 1) {
                        for (let d = 1; d <= 9; d++) A.push([d, 1]);
                        if (pos > 0) A.push([0, 0]);
                    } else {
                        A.push([0, 0]);
                    }
                    const B = [];
                    if (aliveB === 1) {
                        for (let d = 1; d <= 9; d++) B.push([d, 1]);
                        if (pos > 0) B.push([0, 0]);
                    } else {
                        B.push([0, 0]);
                    }
                    for (const [da, na] of A) {
                        for (const [db, nb] of B) {
                            const sum = da + db + carry;
                            if (sum % 10 !== target) continue;
                            const ncarry = Math.floor(sum / 10);
                            ndp[ncarry][na][nb] += ways;
                        }
                    }
                }
            }
        }
        dp = ndp;
    }
    return dp[0][0][0];
};


================================================================================
# 3706_maximum_distance_between_unequal_words_in_array_ii
# README: # 3706. Maximum Distance Between Unequal Words in Array II
================================================================================
// LeetCode 3706 - Maximum Distance Between Unequal Words in Array II
// https://leetcode.com/problems/maximum-distance-between-unequal-words-in-array-ii/

var maxDistance = function(words) {
    const n = words.length;
    let ans = 0;
    for (let i = 0; i < n; i++) {
        if (words[i] !== words[0]) ans = Math.max(ans, i + 1);
        if (words[i] !== words[n - 1]) ans = Math.max(ans, n - i);
    }
    return ans;
};


================================================================================
# 3707_equal_score_substrings
# README: # 3707. Equal Score Substrings
================================================================================
// LeetCode 3707 - Equal Score Substrings
// https://leetcode.com/problems/equal-score-substrings/

var scoreBalance = function(s) {
    let l = 0, r = 0;
    for (const c of s) r += (c.charCodeAt(0) - 97) + 1;
    for (let i = 0; i + 1 < s.length; i++) {
        const x = (s.charCodeAt(i) - 97) + 1;
        l += x;
        r -= x;
        if (l === r) return true;
    }
    return false;
};


================================================================================
# 3708_longest_fibonacci_subarray
# README: # 3708. Longest Fibonacci Subarray
================================================================================
// LeetCode 3708 - Longest Fibonacci Subarray
// https://leetcode.com/problems/longest-fibonacci-subarray/

var longestSubarray = function(nums) {
    let f = 2, ans = f;
    for (let i = 2; i < nums.length; i++) {
        if (nums[i] === nums[i - 1] + nums[i - 2]) {
            f++;
            ans = Math.max(ans, f);
        } else f = 2;
    }
    return ans;
};


================================================================================
# 3709_design_exam_scores_tracker
# README: # 3709. Design Exam Scores Tracker
================================================================================
// LeetCode 3709 - Design Exam Scores Tracker
// https://leetcode.com/problems/design-exam-scores-tracker/

var ExamTracker = function() {
    this.times = [0];
    this.pre = [0];
};

ExamTracker.prototype.record = function(time, score) {
    this.times.push(time);
    this.pre.push(this.pre[this.pre.length - 1] + score);
};

ExamTracker.prototype.totalScore = function(startTime, endTime) {
    const lowerBound = (a, target) => {
        let lo = 0, hi = a.length;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (a[mid] < target) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    };
    const l = lowerBound(this.times, startTime) - 1;
    const r = lowerBound(this.times, endTime + 1) - 1;
    return this.pre[r] - this.pre[l];
};


================================================================================
# 3710_maximum_partition_factor
# README: # 3710. Maximum Partition Factor
================================================================================
// LeetCode 3710 - Maximum Partition Factor
// https://leetcode.com/problems/maximum-partition-factor/

var maxPartitionFactor = function(points) {
    const n = points.length;
    if (n === 2) return 0;
    const dist = (i, j) => Math.abs(points[i][0] - points[j][0]) + Math.abs(points[i][1] - points[j][1]);
    const ok = (d) => {
        const g = Array.from({length: n}, () => []);
        for (let i = 0; i < n; i++) {
            for (let j = i + 1; j < n; j++) {
                if (dist(i, j) < d) {
                    g[i].push(j);
                    g[j].push(i);
                }
            }
        }
        const color = new Array(n).fill(-1);
        for (let i = 0; i < n; i++) {
            if (color[i] !== -1) continue;
            const q = [i];
            color[i] = 0;
            while (q.length) {
                const u = q.shift();
                for (const v of g[u]) {
                    if (color[v] === -1) {
                        color[v] = color[u] ^ 1;
                        q.push(v);
                    } else if (color[v] === color[u]) return false;
                }
            }
        }
        return true;
    };
    let lo = 0, hi = 0;
    for (let i = 0; i < n; i++)
        for (let j = i + 1; j < n; j++)
            hi = Math.max(hi, dist(i, j));
    while (lo < hi) {
        const mid = Math.floor((lo + hi + 1) / 2);
        if (ok(mid)) lo = mid;
        else hi = mid - 1;
    }
    return lo;
};


================================================================================
# 3711_maximum_transactions_without_negative_balance
# README: # 3711. Maximum Transactions Without Negative Balance
================================================================================
// LeetCode 3711 - Maximum Transactions Without Negative Balance
// https://leetcode.com/problems/maximum-transactions-without-negative-balance/

var maxTransactions = function(transactions) {
    const tm = new Map();
    let ans = transactions.length;
    let s = 0;
    const firstKey = () => {
        let mn = Infinity;
        for (const k of tm.keys()) if (k < mn) mn = k;
        return mn;
    };
    for (const x of transactions) {
        s += x;
        tm.set(x, (tm.get(x) || 0) + 1);
        while (s < 0) {
            const y = firstKey();
            s -= y;
            ans--;
            const c = tm.get(y);
            if (c === 1) tm.delete(y);
            else tm.set(y, c - 1);
        }
    }
    return ans;
};


================================================================================
# 3712_sum_of_elements_with_frequency_divisible_by_k
# README: # 3712. Sum of Elements With Frequency Divisible by K
================================================================================
// LeetCode 3712 - Sum of Elements With Frequency Divisible by K
// https://leetcode.com/problems/sum-of-elements-with-frequency-divisible-by-k/

var sumDivisibleByK = function(nums, k) {
    const cnt = new Map();
    for (const x of nums) cnt.set(x, (cnt.get(x) || 0) + 1);
    let ans = 0;
    for (const [key, val] of cnt) {
        if (val % k === 0) ans += key * val;
    }
    return ans;
};


================================================================================
# 3713_longest_balanced_substring_i
# README: # 3713. Longest Balanced Substring I
================================================================================
// LeetCode 3713 - Longest Balanced Substring I
// https://leetcode.com/problems/longest-balanced-substring-i/

var longestBalanced = function(s) {
    const n = s.length;
    let ans = 0;
    for (let i = 0; i < n; i++) {
        const cnt = new Array(26).fill(0);
        let mx = 0, v = 0;
        for (let j = i; j < n; j++) {
            const c = s.charCodeAt(j) - 97;
            cnt[c]++;
            if (cnt[c] === 1) v++;
            mx = Math.max(mx, cnt[c]);
            if (mx * v === j - i + 1) ans = Math.max(ans, j - i + 1);
        }
    }
    return ans;
};


================================================================================
# 3714_longest_balanced_substring_ii
# README: # 3714. Longest Balanced Substring II
================================================================================
// LeetCode 3714 - Longest Balanced Substring II
// https://leetcode.com/problems/longest-balanced-substring-ii/

var longestBalanced = function(s) {
    const calc1 = (str) => {
        let res = 0, n = str.length, i = 0;
        while (i < n) {
            let j = i + 1;
            while (j < n && str[j] === str[i]) j++;
            res = Math.max(res, j - i);
            i = j;
        }
        return res;
    };
    const calc2 = (str, a, b) => {
        let res = 0, n = str.length, i = 0;
        while (i < n) {
            while (i < n && str[i] !== a && str[i] !== b) i++;
            const pos = new Map();
            pos.set(0, i - 1);
            let d = 0;
            while (i < n && (str[i] === a || str[i] === b)) {
                if (str[i] === a) d++;
                else d--;
                if (pos.has(d)) res = Math.max(res, i - pos.get(d));
                else pos.set(d, i);
                i++;
            }
        }
        return res;
    };
    const calc3 = (str) => {
        const pos = new Map();
        pos.set('0,0', -1);
        const cnt = [0, 0, 0];
        let res = 0;
        for (let i = 0; i < str.length; i++) {
            cnt[str.charCodeAt(i) - 97]++;
            const x = cnt[0] - cnt[1], y = cnt[1] - cnt[2];
            const k = x + ',' + y;
            if (pos.has(k)) res = Math.max(res, i - pos.get(k));
            else pos.set(k, i);
        }
        return res;
    };
    const x = calc1(s);
    const y = Math.max(calc2(s, 'a', 'b'), Math.max(calc2(s, 'b', 'c'), calc2(s, 'a', 'c')));
    const z = calc3(s);
    return Math.max(x, Math.max(y, z));
};


================================================================================
# 3715_sum_of_perfect_square_ancestors
# README: # 3715. Sum of Perfect Square Ancestors
================================================================================
// LeetCode 3715 - Sum of Perfect Square Ancestors
// https://leetcode.com/problems/sum-of-perfect-square-ancestors/

var sumOfAncestors = function(n, edges, nums) {
    const graph = Array.from({length: n}, () => []);
    for (const e of edges) {
        graph[e[0]].push(e[1]);
        graph[e[1]].push(e[0]);
    }
    const kernel = (x) => {
        let res = 1;
        for (let p = 2; p * p <= x; p++) {
            let cnt = 0;
            while (x % p === 0) {
                x = Math.floor(x / p);
                cnt++;
            }
            if (cnt % 2 === 1) res *= p;
        }
        if (x > 1) res *= x;
        return res;
    };
    const ks = new Array(n);
    for (let i = 0; i < n; i++) ks[i] = kernel(nums[i]);
    const freq = new Map();
    let ans = 0;
    const dfs = (u, p) => {
        ans += freq.get(ks[u]) || 0;
        freq.set(ks[u], (freq.get(ks[u]) || 0) + 1);
        for (const v of graph[u]) if (v !== p) dfs(v, u);
        freq.set(ks[u], (freq.get(ks[u]) || 0) - 1);
    };
    dfs(0, -1);
    return ans;
};


================================================================================
# 3717_minimum_operations_to_make_the_array_beautiful
# README: # 3717. Minimum Operations to Make the Array Beautiful
================================================================================
// LeetCode 3717 - Minimum Operations to Make the Array Beautiful
// https://leetcode.com/problems/minimum-operations-to-make-the-array-beautiful/

var minOperations = function(nums) {
    let f = new Map();
    f.set(nums[0], 0);
    for (let i = 1; i < nums.length; i++) {
        const x = nums[i];
        const g = new Map();
        for (const [pre, s] of f) {
            let cur = Math.ceil(x / pre) * pre;
            while (cur <= 100) {
                const val = s + (cur - x);
                const old = g.get(cur);
                if (old === undefined || old > val) g.set(cur, val);
                cur += pre;
            }
        }
        f = g;
    }
    let ans = Infinity;
    for (const v of f.values()) ans = Math.min(ans, v);
    return ans;
};


================================================================================
# 3718_smallest_missing_multiple_of_k
# README: # 3718. Smallest Missing Multiple of K
================================================================================
// LeetCode 3718 - Smallest Missing Multiple of K
// https://leetcode.com/problems/smallest-missing-multiple-of-k/

var missingMultiple = function(nums, k) {
    const s = new Set(nums);
    for (let i = 1; ; i++) {
        const x = k * i;
        if (!s.has(x)) return x;
    }
};


================================================================================
# 3719_longest_balanced_subarray_i
# README: # 3719. Longest Balanced Subarray I
================================================================================
// LeetCode 3719 - Longest Balanced Subarray I
// https://leetcode.com/problems/longest-balanced-subarray-i/

var longestBalanced = function(nums) {
    const n = nums.length;
    let ans = 0;
    for (let i = 0; i < n; i++) {
        const vis = new Set();
        const cnt = [0, 0];
        for (let j = i; j < n; j++) {
            if (!vis.has(nums[j])) {
                vis.add(nums[j]);
                cnt[nums[j] & 1]++;
            }
            if (cnt[0] === cnt[1]) ans = Math.max(ans, j - i + 1);
        }
    }
    return ans;
};


================================================================================
# 3720_lexicographically_smallest_permutation_greater_than_target
# README: # 3720. Lexicographically Smallest Permutation Greater Than Target
================================================================================
// LeetCode 3720 - Lexicographically Smallest Permutation Greater Than Target
// https://leetcode.com/problems/lexicographically_smallest_permutation_greater_than_target/

var lexGreaterPermutation = function(s, target) {
    const cnt = new Array(26).fill(0);
    for (const c of s) cnt[c.charCodeAt(0) - 97]++;
    const n = s.length;
    const ans = new Array(n);
    const dfs = (pos, greater) => {
        if (pos === n) return greater;
        const start = greater ? 0 : (target.charCodeAt(pos) - 97);
        for (let c = start; c < 26; c++) {
            if (cnt[c] === 0) continue;
            cnt[c]--;
            ans[pos] = String.fromCharCode(97 + c);
            const ng = greater || c > (target.charCodeAt(pos) - 97);
            if (dfs(pos + 1, ng)) return true;
            cnt[c]++;
        }
        return false;
    };
    if (dfs(0, false)) return ans.join('');
    return "";
};


================================================================================
# 3721_longest_balanced_subarray_ii
# README: # 3721. Longest Balanced Subarray II
================================================================================
// LeetCode 3721 - Longest Balanced Subarray Ii
// https://leetcode.com/problems/longest_balanced_subarray_ii/

var longestBalanced = function(nums) {
    class Node {
        constructor() { this.l = 0; this.r = 0; this.mn = 0; this.mx = 0; this.lazy = 0; }
    }
    class SegmentTree {
        constructor(n) {
            this.tr = Array.from({length: n << 2}, () => new Node());
            this.build(1, 0, n);
        }
        build(u, l, r) {
            const tr = this.tr;
            tr[u].l = l; tr[u].r = r; tr[u].mn = 0; tr[u].mx = 0; tr[u].lazy = 0;
            if (l === r) return;
            const mid = (l + r) >> 1;
            this.build(u << 1, l, mid);
            this.build(u << 1 | 1, mid + 1, r);
        }
        apply(u, v) {
            this.tr[u].mn += v;
            this.tr[u].mx += v;
            this.tr[u].lazy += v;
        }
        pushup(u) {
            const tr = this.tr;
            tr[u].mn = Math.min(tr[u << 1].mn, tr[u << 1 | 1].mn);
            tr[u].mx = Math.max(tr[u << 1].mx, tr[u << 1 | 1].mx);
        }
        pushdown(u) {
            if (this.tr[u].lazy !== 0) {
                const v = this.tr[u].lazy;
                this.apply(u << 1, v);
                this.apply(u << 1 | 1, v);
                this.tr[u].lazy = 0;
            }
        }
        modify(u, l, r, v) {
            const tr = this.tr;
            if (tr[u].l >= l && tr[u].r <= r) {
                this.apply(u, v);
                return;
            }
            this.pushdown(u);
            const mid = (tr[u].l + tr[u].r) >> 1;
            if (l <= mid) this.modify(u << 1, l, r, v);
            if (r > mid) this.modify(u << 1 | 1, l, r, v);
            this.pushup(u);
        }
        query(u, target) {
            const tr = this.tr;
            if (tr[u].l === tr[u].r) return tr[u].l;
            this.pushdown(u);
            const left = u << 1, right = u << 1 | 1;
            if (tr[left].mn <= target && target <= tr[left].mx) return this.query(left, target);
            return this.query(right, target);
        }
    }
    const n = nums.length;
    const st = new SegmentTree(n);
    const last = new Map();
    let now = 0, ans = 0;
    for (let i = 1; i <= n; i++) {
        const x = nums[i - 1];
        const det = (x & 1) !== 0 ? 1 : -1;
        if (last.has(x)) {
            st.modify(1, last.get(x), n, -det);
            now -= det;
        }
        last.set(x, i);
        st.modify(1, i, n, det);
        now += det;
        const pos = st.query(1, now);
        ans = Math.max(ans, i - pos);
    }
    return ans;
};


================================================================================
# 3722_lexicographically_smallest_string_after_reverse
# README: # 3722. Lexicographically Smallest String After Reverse
================================================================================
// LeetCode 3722 - Lexicographically Smallest String After Reverse
// https://leetcode.com/problems/lexicographically-smallest-string-after-reverse/

var lexSmallest = function(s) {
    let ans = s;
    const n = s.length;
    const reverse = (a, l, r) => {
        for (let i = l, j = r - 1; i < j; i++, j--) {
            const t = a[i]; a[i] = a[j]; a[j] = t;
        }
    };
    for (let k = 1; k <= n; k++) {
        const a1 = s.split('');
        reverse(a1, 0, k);
        const t1 = a1.join('');
        const a2 = s.split('');
        reverse(a2, n - k, n);
        const t2 = a2.join('');
        if (t1 < ans) ans = t1;
        if (t2 < ans) ans = t2;
    }
    return ans;
};


================================================================================
# 3723_maximize_sum_of_squares_of_digits
# README: # 3723. Maximize Sum of Squares of Digits
================================================================================
// LeetCode 3723 - Maximize Sum Of Squares Of Digits
// https://leetcode.com/problems/maximize_sum_of_squares_of_digits/

var maxSumOfSquares = function(num, sum) {
    if (num * 9 < sum) return "";
    const k = Math.floor(sum / 9), s = sum % 9;
    let ans = '';
    for (let i = 0; i < k; i++) ans += '9';
    if (s > 0) ans += String.fromCharCode(48 + s);
    while (ans.length < num) ans += '0';
    return ans;
};


================================================================================
# 3724_minimum_operations_to_transform_array
# README: # 3724. Minimum Operations to Transform Array
================================================================================
// LeetCode 3724 - Minimum Operations to Transform Array
// https://leetcode.com/problems/minimum-operations-to-transform-array/

var minOperations = function(nums1, nums2) {
    let ans = 1;
    const n = nums1.length;
    let ok = false;
    let d = 1 << 30;
    for (let i = 0; i < n; i++) {
        const x = Math.max(nums1[i], nums2[i]);
        const y = Math.min(nums1[i], nums2[i]);
        ans += x - y;
        d = Math.min(d, Math.min(Math.abs(x - nums2[n]), Math.abs(y - nums2[n])));
        if (nums2[n] >= y && nums2[n] <= x) ok = true;
    }
    if (!ok) ans += d;
    return ans;
};


================================================================================
# 3725_count_ways_to_choose_coprime_integers_from_rows
# README: # 3725. Count Ways to Choose Coprime Integers from Rows
================================================================================
// LeetCode 3725 - Count Ways To Choose Coprime Integers From Rows
// https://leetcode.com/problems/count_ways_to_choose_coprime_integers_from_rows/

var countCoprime = function(mat) {
    const MOD = 1000000007;
    const m = mat.length;
    const gcd = (a, b) => {
        while (b !== 0) {
            const t = a % b;
            a = b;
            b = t;
        }
        return a;
    };
    let dp = new Map();
    for (const v of mat[0]) dp.set(v, (dp.get(v) || 0) + 1);
    for (let i = 1; i < m; i++) {
        const ndp = new Map();
        for (const v of mat[i]) {
            for (const [key, val] of dp) {
                const ng = gcd(key, v);
                ndp.set(ng, ((ndp.get(ng) || 0) + val) % MOD);
            }
        }
        dp = ndp;
    }
    return dp.get(1) || 0;
};


================================================================================
# 3726_remove_zeros_in_decimal_representation
# README: # 3726. Remove Zeros in Decimal Representation
================================================================================
// LeetCode 3726 - Remove Zeros in Decimal Representation
// https://leetcode.com/problems/remove-zeros-in-decimal-representation/

var removeZeros = function(n) {
    let ans = 0, k = 1;
    while (n > 0) {
        const x = n % 10;
        if (x > 0) {
            ans = k * x + ans;
            k *= 10;
        }
        n = Math.floor(n / 10);
    }
    return ans;
};


================================================================================
# 3727_maximum_alternating_sum_of_squares
# README: # 3727. Maximum Alternating Sum of Squares
================================================================================
// LeetCode 3727 - Maximum Alternating Sum of Squares
// https://leetcode.com/problems/maximum-alternating-sum-of-squares/

var maxAlternatingSum = function(nums) {
    const a = nums.map(x => x * x);
    a.sort((x, y) => x - y);
    const m = Math.floor(a.length / 2);
    let ans = 0;
    for (let i = 0; i < m; i++) ans -= a[i];
    for (let i = m; i < a.length; i++) ans += a[i];
    return ans;
};


================================================================================
# 3728_stable_subarrays_with_equal_boundary_and_interior_sum
# README: # 3728. Stable Subarrays With Equal Boundary and Interior Sum
================================================================================
// LeetCode 3728 - Stable Subarrays With Equal Boundary And Interior Sum
// https://leetcode.com/problems/stable_subarrays_with_equal_boundary_and_interior_sum/

var countStableSubarrays = function(capacity) {
    const n = capacity.length;
    const s = new Array(n + 1).fill(0);
    for (let i = 1; i <= n; i++) s[i] = s[i - 1] + capacity[i - 1];
    const cnt = new Map();
    let ans = 0;
    for (let r = 2; r < n; r++) {
        const l = r - 2;
        const keyL = capacity[l] + "#" + (capacity[l] + s[l + 1]);
        cnt.set(keyL, (cnt.get(keyL) || 0) + 1);
        const keyR = capacity[r] + "#" + s[r];
        ans += cnt.get(keyR) || 0;
    }
    return ans;
};


================================================================================
# 3729_count_distinct_subarrays_divisible_by_k_in_sorted_array
# README: # 3729. Count Distinct Subarrays Divisible by K in Sorted Array
================================================================================
// LeetCode 3729 - Count Distinct Subarrays Divisible By K In Sorted Array
// https://leetcode.com/problems/count_distinct_subarrays_divisible_by_k_in_sorted_array/

var numGoodSubarrays = function(nums, k) {
    let ans = 0;
    let s = 0;
    const cnt = new Map();
    cnt.set(0, 1);
    for (const x of nums) {
        s = (s + x) % k;
        ans += cnt.get(s) || 0;
        cnt.set(s, (cnt.get(s) || 0) + 1);
    }
    const n = nums.length;
    for (let i = 0; i < n; ) {
        let j = i + 1;
        while (j < n && nums[j] === nums[i]) j++;
        const m = j - i;
        for (let h = 1; h <= m; h++) {
            if ((nums[i] * h) % k === 0) ans -= (m - h);
        }
        i = j;
    }
    return ans;
};


================================================================================
# 3730_maximum_calories_burnt_from_jumps
# README: # 3730. Maximum Calories Burnt from Jumps
================================================================================
// LeetCode 3730 - Maximum Calories Burnt from Jumps
// https://leetcode.com/problems/maximum-calories-burnt-from-jumps/

var maxCaloriesBurnt = function(heights) {
    heights = heights.slice().sort((a, b) => a - b);
    let ans = 0;
    let pre = 0, l = 0, r = heights.length - 1;
    while (l < r) {
        const d1 = heights[r] - pre;
        ans += d1 * d1;
        const d2 = heights[l] - heights[r];
        ans += d2 * d2;
        pre = heights[l];
        l++;
        r--;
    }
    const d = heights[r] - pre;
    ans += d * d;
    return ans;
};


================================================================================
# 3731_find_missing_elements
# README: # 3731. Find Missing Elements
================================================================================
// LeetCode 3731 - Find Missing Elements
// https://leetcode.com/problems/find-missing-elements/

var findMissingElements = function(nums) {
    let mn = 100, mx = 0;
    const s = new Set();
    for (const x of nums) {
        mn = Math.min(mn, x);
        mx = Math.max(mx, x);
        s.add(x);
    }
    const ans = [];
    for (let x = mn + 1; x < mx; x++) {
        if (!s.has(x)) ans.push(x);
    }
    return ans;
};


================================================================================
# 3732_maximum_product_of_three_elements_after_one_replacement
# README: # 3732. Maximum Product of Three Elements After One Replacement
================================================================================
// LeetCode 3732 - Maximum Product of Three Elements After One Replacement
// https://leetcode.com/problems/maximum-product-of-three-elements-after-one-replacement/

var maxProduct = function(nums) {
    const a = nums.slice().sort((x, y) => x - y);
    const n = a.length;
    const A = a[0], B = a[1], C = a[n - 2], D = a[n - 1];
    const x = 100000;
    return Math.max(Math.max(A * B * x, C * D * x), -A * D * x);
};


================================================================================
# 3733_minimum_time_to_complete_all_deliveries
# README: # 3733. Minimum Time to Complete All Deliveries
================================================================================
// LeetCode 3733 - Minimum Time To Complete All Deliveries
// https://leetcode.com/problems/minimum_time_to_complete_all_deliveries/

var minimumTime = function(d, r) {
    const ok = (T) => {
        const w0 = T - Math.floor(T / r[0]);
        const w1 = T - Math.floor(T / r[1]);
        return w0 + w1 >= d[0] + d[1];
    };
    let lo = 1, hi = Number.MAX_SAFE_INTEGER;
    while (lo < hi) {
        const mid = lo + Math.floor((hi - lo) / 2);
        if (ok(mid)) hi = mid;
        else lo = mid + 1;
    }
    return lo;
};


================================================================================
# 3734_lexicographically_smallest_palindromic_permutation_greater_than_target
# README: # 3734. Lexicographically Smallest Palindromic Permutation Greater Than Target
================================================================================
// LeetCode 3734 - Lexicographically Smallest Palindromic Permutation Greater Than Target
// https://leetcode.com/problems/lexicographically_smallest_palindromic_permutation_greater_than_target/

var lexPalindromicPermutation = function(s, target) {
    const cnt = new Array(26).fill(0);
    for (const c of s) cnt[c.charCodeAt(0) - 97]++;
    let odd = 0, mid = -1;
    for (let i = 0; i < 26; i++) {
        if (cnt[i] % 2 === 1) { odd++; mid = i; }
    }
    if (odd > 1) return "";
    const half = new Array(26).fill(0);
    for (let i = 0; i < 26; i++) half[i] = Math.floor(cnt[i] / 2);
    const n = s.length;
    const halfLen = Math.floor(n / 2);
    const left = new Array(halfLen);
    const dfs = (pos, greater) => {
        if (pos === halfLen) {
            if (mid >= 0) {
                if (greater) return true;
                return String.fromCharCode(97 + mid) > target[halfLen];
            }
            return greater;
        }
        const start = greater ? 0 : (target.charCodeAt(pos) - 97);
        for (let c = start; c < 26; c++) {
            if (half[c] === 0) continue;
            half[c]--;
            left[pos] = String.fromCharCode(97 + c);
            if (dfs(pos + 1, greater || c > (target.charCodeAt(pos) - 97))) return true;
            half[c]++;
        }
        return false;
    };
    if (!dfs(0, false)) return "";
    let res = left.join('');
    if (mid >= 0) res += String.fromCharCode(97 + mid);
    for (let i = halfLen - 1; i >= 0; i--) res += left[i];
    if (res <= target) return "";
    return res;
};


================================================================================
# 3735_lexicographically_smallest_string_after_reverse_ii
# README: # 3735. Lexicographically Smallest String After Reverse II
================================================================================
// LeetCode 3735 - Lexicographically Smallest String After Reverse II
// https://leetcode.com/problems/lexicographically-smallest-string-after-reverse-ii/

var lexSmallest = function(s) {
    const n = s.length;
    let best = s;
    const reverse = (a, l, r) => {
        for (let i = l, j = r - 1; i < j; i++, j--) {
            const t = a[i]; a[i] = a[j]; a[j] = t;
        }
    };
    for (let i = 1; i <= n; i++) {
        const t = s.split('');
        reverse(t, 0, i);
        const ts = t.join('');
        if (ts < best) best = ts;
    }
    for (let i = 0; i < n; i++) {
        const t = s.split('');
        reverse(t, i, n);
        const ts = t.join('');
        if (ts < best) best = ts;
    }
    return best;
};


================================================================================
# 3736_minimum_moves_to_equal_array_elements_iii
# README: # 3736. Minimum Moves to Equal Array Elements III
================================================================================
// LeetCode 3736 - Minimum Moves to Equal Array Elements III
// https://leetcode.com/problems/minimum-moves-to-equal-array-elements-iii/

var minMoves = function(nums) {
    let mx = 0, s = 0;
    for (const x of nums) {
        mx = Math.max(mx, x);
        s += x;
    }
    return mx * nums.length - s;
};


================================================================================
# 3737_count_subarrays_with_majority_element_i
# README: # 3737. Count Subarrays With Majority Element I
================================================================================
// LeetCode 3737 - Count Subarrays With Majority Element I
// https://leetcode.com/problems/count-subarrays-with-majority-element-i/

var countMajoritySubarrays = function(nums, target) {
    const n = nums.length;
    let ans = 0;
    for (let i = 0; i < n; i++) {
        let cnt = 0;
        for (let j = i; j < n; j++) {
            if (nums[j] === target) cnt++;
            if (cnt * 2 > j - i + 1) ans++;
        }
    }
    return ans;
};


================================================================================
# 3738_longest_non_decreasing_subarray_after_replacing_at_most_one_element
# README: # 3738. Longest Non-Decreasing Subarray After Replacing at Most One Element
================================================================================
// LeetCode 3738 - Longest Non-Decreasing Subarray After Replacing at Most One Element
// https://leetcode.com/problems/longest-non-decreasing-subarray-after-replacing-at-most-one-element/

var longestSubarray = function(nums) {
    const n = nums.length;
    const left = new Array(n).fill(1);
    const right = new Array(n).fill(1);
    for (let i = 1; i < n; i++) {
        if (nums[i] >= nums[i - 1]) left[i] = left[i - 1] + 1;
    }
    for (let i = n - 2; i >= 0; i--) {
        if (nums[i] <= nums[i + 1]) right[i] = right[i + 1] + 1;
    }
    let ans = 0;
    for (const v of left) ans = Math.max(ans, v);
    for (let i = 0; i < n; i++) {
        const a = i > 0 ? left[i - 1] : 0;
        const b = i + 1 < n ? right[i + 1] : 0;
        if (i > 0 && i + 1 < n && nums[i - 1] > nums[i + 1]) {
            ans = Math.max(ans, Math.max(a + 1, b + 1));
        } else {
            ans = Math.max(ans, a + b + 1);
        }
    }
    return ans;
};


================================================================================
# 3739_count_subarrays_with_majority_element_ii
# README: # 3739. Count Subarrays With Majority Element II
================================================================================
// LeetCode 3739 - Count Subarrays With Majority Element II
// https://leetcode.com/problems/count-subarrays-with-majority-element-ii/

var countMajoritySubarrays = function(nums, target) {
    class BIT {
        constructor(n_) {
            this.n = n_;
            this.c = new Array(n_ + 1).fill(0);
        }
        update(x, delta) {
            for (; x <= this.n; x += x & -x) this.c[x] += delta;
        }
        query(x) {
            let s = 0;
            for (; x > 0; x -= x & -x) s += this.c[x];
            return s;
        }
    }
    const n = nums.length;
    const tree = new BIT(2 * n + 1);
    let s = n + 1;
    tree.update(s, 1);
    let ans = 0;
    for (const x of nums) {
        if (x === target) s++;
        else s--;
        ans += tree.query(s - 1);
        tree.update(s, 1);
    }
    return ans;
};

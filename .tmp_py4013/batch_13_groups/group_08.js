
================================================================================
FILE: 3505_minimum_operations_to_make_elements_within_k_subarrays_equal
================================================================================
// LeetCode 3505 - Minimum Operations to Make Elements Within K Subarrays Equal
// https://leetcode.com/problems/minimum-operations-to-make-elements-within-k-subarrays-equal/

var minOperations = function(nums, x, k) {
    const n = nums.length;
    const minOps = new Array(n - x + 1);
    for (let i = 0; i + x <= n; i++) {
        const w = nums.slice(i, i + x).sort((a, b) => a - b);
        const med = w[Math.floor((x - 1) / 2)];
        let ops = 0;
        for (const v of w) ops += Math.abs(v - med);
        minOps[i] = ops;
    }
    const Inf = Number.MAX_SAFE_INTEGER;
    const dp = Array.from({length: n + 1}, () => new Array(k + 1).fill(Inf));
    dp[n][0] = 0;
    for (let i = n - 1; i >= 0; i--) {
        for (let j = 0; j <= k; j++) {
            dp[i][j] = dp[i + 1][j];
            if (j > 0 && i + x <= n && minOps[i] + dp[i + x][j - 1] < dp[i][j])
                dp[i][j] = minOps[i] + dp[i + x][j - 1];
        }
    }
    return dp[0][k];
};

================================================================================
FILE: 3506_find_time_required_to_eliminate_bacterial_strains
================================================================================
// LeetCode 3506 - Find Time Required to Eliminate Bacterial Strains
// https://leetcode.com/problems/find-time-required-to-eliminate-bacterial-strains/

var minEliminationTime = function(timeReq, splitTime) {
    const pq = timeReq.slice().sort((a, b) => a - b);
    while (pq.length > 1) {
        pq.shift();
        const x = pq.shift();
        const v = x + splitTime;
        let lo = 0, hi = pq.length;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (pq[mid] < v) lo = mid + 1;
            else hi = mid;
        }
        pq.splice(lo, 0, v);
    }
    return pq[0];
};

================================================================================
FILE: 3507_minimum_pair_removal_to_sort_array_i
================================================================================
// LeetCode 3507 - Minimum Pair Removal to Sort Array I
// https://leetcode.com/problems/minimum-pair-removal-to-sort-array-i/

function isNonDecreasing(a) {
    for (let i = 1; i < a.length; i++) if (a[i] < a[i - 1]) return false;
    return true;
}
var minimumPairRemoval = function(nums) {
    const arr = nums.slice();
    let ans = 0;
    while (!isNonDecreasing(arr)) {
        let k = 0, s = arr[0] + arr[1];
        for (let i = 1; i + 1 < arr.length; i++) {
            const t = arr[i] + arr[i + 1];
            if (s > t) { s = t; k = i; }
        }
        arr[k] = s;
        arr.splice(k + 1, 1);
        ans++;
    }
    return ans;
};

================================================================================
FILE: 3508_implement_router
================================================================================
// LeetCode 3508 - Implement Router
// https://leetcode.com/problems/implement-router/

var Router = function(memoryLimit) {
    this.lim = memoryLimit;
    this.vis = new Set();
    this.q = [];
    this.idx = new Map();
    this.d = new Map();
};

Router.prototype.f = function(a, b, c) {
    return (BigInt(a) << 46n) | (BigInt(b) << 29n) | BigInt(c);
};

Router.prototype.addPacket = function(source, destination, timestamp) {
    const x = this.f(source, destination, timestamp);
    if (this.vis.has(x)) return false;
    this.vis.add(x);
    if (this.q.length >= this.lim) this.forwardPacket();
    this.q.push([source, destination, timestamp]);
    if (!this.d.has(destination)) this.d.set(destination, []);
    this.d.get(destination).push(timestamp);
    return true;
};

Router.prototype.forwardPacket = function() {
    if (this.q.length === 0) return [];
    const packet = this.q.shift();
    const s = packet[0], dest = packet[1], t = packet[2];
    this.vis.delete(this.f(s, dest, t));
    this.idx.set(dest, (this.idx.get(dest) || 0) + 1);
    return [s, dest, t];
};

Router.prototype.getCount = function(destination, startTime, endTime) {
    const ls = this.d.get(destination);
    if (!ls) return 0;
    const k = this.idx.get(destination) || 0;
    return lowerBound(ls, k, endTime + 1) - lowerBound(ls, k, startTime);
};

function lowerBound(a, from, target) {
    let lo = from, hi = a.length;
    while (lo < hi) {
        const mid = (lo + hi) >> 1;
        if (a[mid] < target) lo = mid + 1;
        else hi = mid;
    }
    return lo;
}

================================================================================
FILE: 3509_maximum_product_of_subsequences_with_an_alternating_sum_equal_to_k
================================================================================
// LeetCode 3509 - Maximum Product of Subsequences With an Alternating Sum Equal to K
// https://leetcode.com/problems/maximum-product-of-subsequences-with-an-alternating-sum-equal-to-k/

var maxProduct = function(nums, k, limit) {
    const MIN = -5000;
    const memo = new Map();
    let sumAll = 0;
    for (const v of nums) sumAll += v;
    if (Math.abs(k) > sumAll) return -1;
    function dp(i, product, state, kk) {
        if (i === nums.length) {
            if (kk === 0 && state !== 0 && product <= limit) return product;
            return MIN;
        }
        const key = i + ',' + product + ',' + state + ',' + kk;
        if (memo.has(key)) return memo.get(key);
        let res = dp(i + 1, product, state, kk);
        if (state === 0) res = Math.max(res, dp(i + 1, nums[i], 1, kk - nums[i]));
        if (state === 1) {
            let np = product * nums[i];
            if (np > limit + 1) np = limit + 1;
            res = Math.max(res, dp(i + 1, np, 2, kk + nums[i]));
        }
        if (state === 2) {
            let np = product * nums[i];
            if (np > limit + 1) np = limit + 1;
            res = Math.max(res, dp(i + 1, np, 1, kk - nums[i]));
        }
        memo.set(key, res);
        return res;
    }
    const ans = dp(0, 1, 0, k);
    return ans === MIN ? -1 : ans;
};

================================================================================
FILE: 3510_minimum_pair_removal_to_sort_array_ii
================================================================================
// LeetCode 3510 - Minimum Pair Removal to Sort Array II
// https://leetcode.com/problems/minimum-pair-removal-to-sort-array-ii/

var minimumPairRemoval = function(nums) {
    const n = nums.length;
    let inv = 0, ans = 0;
    const sl = [];
    const idx = new Set();
    for (let i = 0; i < n; i++) idx.add(i);
    const key = (sum, i) => sum * 1000000007 + i;
    const slMap = new Map();
    function addSl(sum, i) {
        const k = key(sum, i);
        slMap.set(k, [sum, i]);
        let lo = 0, hi = sl.length;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (sl[mid][0] < sum || (sl[mid][0] === sum && sl[mid][1] < i)) lo = mid + 1;
            else hi = mid;
        }
        sl.splice(lo, 0, [sum, i]);
    }
    function remSl(sum, i) {
        const k = key(sum, i);
        if (!slMap.has(k)) return;
        slMap.delete(k);
        for (let t = 0; t < sl.length; t++) {
            if (sl[t][0] === sum && sl[t][1] === i) { sl.splice(t, 1); break; }
        }
    }
    function ceiling(set, x) {
        let best = null;
        for (const v of set) if (v >= x && (best === null || v < best)) best = v;
        return best;
    }
    function floor(set, x) {
        let best = null;
        for (const v of set) if (v <= x && (best === null || v > best)) best = v;
        return best;
    }
    for (let i = 0; i < n - 1; i++) {
        if (nums[i] > nums[i + 1]) inv++;
        addSl(nums[i] + nums[i + 1], i);
    }
    while (inv > 0) {
        ans++;
        const p = sl.shift();
        slMap.delete(key(p[0], p[1]));
        const s = p[0], i = p[1];
        const j = ceiling(idx, i + 1);
        if (nums[i] > nums[j]) inv--;
        const h = floor(idx, i - 1);
        if (h !== null) {
            if (nums[h] > nums[i]) inv--;
            remSl(nums[h] + nums[i], h);
            if (nums[h] > s) inv++;
            addSl(nums[h] + s, h);
        }
        const kk = ceiling(idx, j + 1);
        if (kk !== null) {
            if (nums[j] > nums[kk]) inv--;
            remSl(nums[j] + nums[kk], j);
            if (s > nums[kk]) inv++;
            addSl(s + nums[kk], i);
        }
        nums[i] = s;
        idx.delete(j);
    }
    return ans;
};

================================================================================
FILE: 3511_make_a_positive_array
================================================================================
// LeetCode 3511 - Make a Positive Array
// https://leetcode.com/problems/make-a-positive-array/

var makeArrayPositive = function(nums) {
    let ans = 0, l = -1;
    let preMx = 0, s = 0;
    for (let r = 0; r < nums.length; r++) {
        s += nums[r];
        if (r - l > 2 && s <= preMx) {
            ans++;
            l = r;
            preMx = 0;
            s = 0;
        } else if (r - l >= 2) {
            preMx = Math.max(preMx, s - nums[r] - nums[r - 1]);
        }
    }
    return ans;
};

================================================================================
FILE: 3512_minimum_operations_to_make_array_sum_divisible_by_k
================================================================================
// LeetCode 3512 - Minimum Operations to Make Array Sum Divisible by K
// https://leetcode.com/problems/minimum-operations-to-make-array-sum-divisible-by-k/

var minOperations = function(nums, k) {
    let ans = 0;
    for (const x of nums) ans = (ans + x) % k;
    return ans;
};

================================================================================
FILE: 3513_number_of_unique_xor_triplets_i
================================================================================
// LeetCode 3513 - Number of Unique XOR Triplets I
// https://leetcode.com/problems/number-of-unique-xor-triplets-i/

var uniqueXorTriplets = function(nums) {
    const n = nums.length;
    if (n <= 2) return n;
    let x = n, len = 0;
    while (x !== 0) { len++; x >>= 1; }
    return 1 << len;
};

================================================================================
FILE: 3514_number_of_unique_xor_triplets_ii
================================================================================
// LeetCode 3514 - Number of Unique XOR Triplets II
// https://leetcode.com/problems/number-of-unique-xor-triplets-ii/

var uniqueXorTriplets = function(nums) {
    let mx = 0;
    for (const v of nums) mx = Math.max(mx, v);
    mx <<= 1;
    const st = new Array(mx).fill(false);
    for (const a of nums) for (const b of nums) st[a ^ b] = true;
    const s = new Array(mx).fill(0);
    for (let ab = 0; ab < mx; ab++) {
        if (st[ab]) for (const c of nums) s[ab ^ c] = 1;
    }
    let ans = 0;
    for (const v of s) ans += v;
    return ans;
};

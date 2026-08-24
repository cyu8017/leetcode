
================================================================================
FILE: 3461_check_if_digits_are_equal_in_string_after_operations_i
================================================================================
// LeetCode 3461 - Check If Digits Are Equal in String After Operations I
// https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i/

var hasSameDigits = function(s) {
    let b = s.split("");
    while (b.length > 2) {
        const nb = new Array(b.length - 1);
        for (let i = 0; i + 1 < b.length; i++) {
            nb[i] = String((b[i].charCodeAt(0) - 48 + b[i + 1].charCodeAt(0) - 48) % 10);
        }
        b = nb;
    }
    return b[0] === b[1];
};

================================================================================
FILE: 3462_maximum_sum_with_at_most_k_elements
================================================================================
// LeetCode 3462 - Maximum Sum With at Most K Elements
// https://leetcode.com/problems/maximum-sum-with-at-most-k-elements/

var maxSum = function(grid, limits, k) {
    const h = [];
    let sum = 0;
    const push = (v) => {
        h.push(v);
        h.sort((a, b) => a - b);
    };
    const poll = () => h.shift();
    for (let i = 0; i < grid.length; i++) {
        const r = grid[i].slice().sort((a, b) => a - b);
        let lim = limits[i];
        if (lim > r.length) lim = r.length;
        for (let j = 0; j < lim; j++) {
            const val = r[r.length - 1 - j];
            push(val);
            sum += val;
            if (h.length > k) sum -= poll();
        }
    }
    return sum;
};

================================================================================
FILE: 3463_check_if_digits_are_equal_in_string_after_operations_ii
================================================================================
// LeetCode 3463 - Check If Digits Are Equal in String After Operations II
// https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-ii/

var hasSameDigits = function(s) {
    const modPowP = (a, e, p) => {
        let r = 1;
        while (e > 0) {
            if (e % 2 === 1) r = r * a % p;
            a = a * a % p;
            e = Math.floor(e / 2);
        }
        return r;
    };
    const modInvPrime = (a, p) => modPowP(a, p - 2, p);
    const binomMod = (n, k, p) => {
        if (k < 0 || k > n) return 0;
        let num = 1, den = 1;
        for (let i = 0; i < k; i++) {
            num = num * (n - i) % p;
            den = den * (i + 1) % p;
        }
        return num * modInvPrime(den, p) % p;
    };
    const crt = (a1, m1, a2, m2) => {
        for (let x = 0; x < m1 * m2; x++) {
            if (x % m1 === a1 && x % m2 === a2) return x;
        }
        return 0;
    };
    const binomMod10 = (n, k) => crt(binomMod(n, k, 2), 2, binomMod(n, k, 5), 5);
    const combineDigit = (offset) => {
        const n = s.length;
        let sum = 0;
        for (let i = 0; i <= n - 2; i++) {
            sum = (sum + binomMod10(n - 2, i) * (s.charCodeAt(i + offset) - 48)) % 10;
        }
        return sum;
    };
    return combineDigit(0) === combineDigit(1);
};

================================================================================
FILE: 3464_maximize_the_distance_between_points_on_a_square
================================================================================
// LeetCode 3464 - Maximize the Distance Between Points on a Square
// https://leetcode.com/problems/maximize-the-distance-between-points-on-a-square/

var maxDistance = function(side, points, k) {
    const canPlace = (arr, perim, mid) => {
        const n = arr.length;
        for (let s = 0; s < n; s++) {
            let cnt = 1;
            let last = arr[s];
            let idx = s;
            for (; cnt < k; ) {
                const target = last + mid;
                let found = false;
                for (let step = 1; step < n; step++) {
                    const ni = (idx + step) % n;
                    const val = arr[ni];
                    const add = ni <= idx ? perim : 0;
                    if (val + add >= target) {
                        last = val + add;
                        idx = ni;
                        cnt++;
                        found = true;
                        break;
                    }
                }
                if (!found) break;
            }
            if (cnt === k && last - arr[s] <= perim - mid) return true;
        }
        return false;
    };
    const arr = new Array(points.length);
    for (let i = 0; i < points.length; i++) {
        const x = points[i][0], y = points[i][1];
        let d;
        if (y === 0) d = x;
        else if (x === side) d = side + y;
        else if (y === side) d = 2 * side + (side - x);
        else d = 3 * side + (side - y);
        arr[i] = d;
    }
    arr.sort((a, b) => a - b);
    const perim = 4 * side;
    let lo = 0, hi = 2 * side;
    while (lo < hi) {
        const mid = Math.floor((lo + hi + 1) / 2);
        if (canPlace(arr, perim, mid)) lo = mid;
        else hi = mid - 1;
    }
    return lo;
};

================================================================================
FILE: 3466_maximum_coin_collection
================================================================================
// LeetCode 3466 - Maximum Coin Collection
// https://leetcode.com/problems/maximum-coin-collection/

var maxCoins = function(lane1, lane2) {
    const n = lane1.length;
    const neg = Number.MIN_SAFE_INTEGER / 4;
    let dp = [[lane1[0], neg], [lane2[0], neg]];
    let ans = Math.max(dp[0][0], dp[1][0]);
    for (let i = 1; i < n; i++) {
        const ndp = [[0, 0], [0, 0]];
        ndp[0][0] = Math.max(dp[0][0], 0) + lane1[i];
        ndp[1][0] = Math.max(dp[1][0], 0) + lane2[i];
        ndp[0][1] = Math.max(dp[0][1], dp[1][0]) + lane1[i];
        ndp[1][1] = Math.max(dp[1][1], dp[0][0]) + lane2[i];
        if (lane1[i] > ndp[0][0]) ndp[0][0] = lane1[i];
        if (lane2[i] > ndp[1][0]) ndp[1][0] = lane2[i];
        for (let a = 0; a < 2; a++)
            for (let b = 0; b < 2; b++) {
                dp[a][b] = ndp[a][b];
                if (dp[a][b] > ans) ans = dp[a][b];
            }
    }
    return ans;
};

================================================================================
FILE: 3467_transform_array_by_parity
================================================================================
// LeetCode 3467 - Transform Array by Parity
// https://leetcode.com/problems/transform-array-by-parity/

var transformArray = function(nums) {
    for (let i = 0; i < nums.length; i++) nums[i] %= 2;
    let j = 0;
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] === 0) {
            const t = nums[i]; nums[i] = nums[j]; nums[j] = t;
            j++;
        }
    }
    return nums;
};

================================================================================
FILE: 3468_find_the_number_of_copy_arrays
================================================================================
// LeetCode 3468 - Find the Number of Copy Arrays
// https://leetcode.com/problems/find-the-number-of-copy-arrays/

var countArrays = function(original, bounds) {
    const n = original.length;
    let lo = bounds[0][0], hi = bounds[0][1];
    for (let i = 1; i < n; i++) {
        const diff = original[i] - original[i - 1];
        const lo2 = bounds[i][0], hi2 = bounds[i][1];
        let nlo = lo + diff, nhi = hi + diff;
        if (nlo < lo2) nlo = lo2;
        if (nhi > hi2) nhi = hi2;
        if (nlo > nhi) return 0;
        lo = nlo;
        hi = nhi;
    }
    return hi - lo + 1;
};

================================================================================
FILE: 3469_find_minimum_cost_to_remove_array_elements
================================================================================
// LeetCode 3469 - Find Minimum Cost to Remove Array Elements
// https://leetcode.com/problems/find-minimum-cost-to-remove-array-elements/

var minCost = function(nums) {
    const n = nums.length;
    const memo = new Map();
    const max2 = (a, b) => (a > b ? a : b);
    const min3 = (a, b, c) => Math.min(a, Math.min(b, c));
    const key = (i, prev) => (BigInt(i) << 32n) | BigInt(prev >>> 0);
    const dfs = (i, prev) => {
        if (i >= n) return prev === -1 ? 0 : nums[prev];
        const k = key(i, prev).toString();
        if (memo.has(k)) return memo.get(k);
        let res;
        if (prev === -1) {
            if (i + 1 >= n) res = nums[i];
            else if (i + 2 >= n) res = max2(nums[i], nums[i + 1]);
            else {
                const a = nums[i], b = nums[i + 1], c = nums[i + 2];
                res = min3(max2(b, c) + dfs(i + 3, i), max2(a, c) + dfs(i + 3, i + 1), max2(a, b) + dfs(i + 3, i + 2));
            }
        } else {
            if (i + 1 >= n) res = max2(nums[prev], nums[i]);
            else {
                const a = nums[prev], b = nums[i], c = nums[i + 1];
                res = min3(max2(b, c) + dfs(i + 2, prev), max2(a, c) + dfs(i + 2, i), max2(a, b) + dfs(i + 2, i + 1));
            }
        }
        memo.set(k, res);
        return res;
    };
    return dfs(0, -1);
};

================================================================================
FILE: 3470_permutations_iv
================================================================================
// LeetCode 3470 - Permutations IV
// https://leetcode.com/problems/permutations-iv/

var permute = function(n, k) {
    const fact = new Array(n + 1);
    fact[0] = 1n;
    for (let i = 1; i <= n; i++) {
        fact[i] = fact[i - 1] * BigInt(i);
        if (fact[i] > 10n ** 18n) fact[i] = 10n ** 18n + 1n;
    }
    const used = new Array(n + 1).fill(false);
    const ans = [];
    let kk = BigInt(k);
    const dfs = (pos) => {
        if (pos === n) return true;
        for (let x = 1; x <= n; x++) {
            if (used[x]) continue;
            if (pos > 0 && (ans[pos - 1] % 2 === x % 2)) continue;
            const rem = n - pos - 1;
            const cnt = fact[rem];
            if (cnt >= kk) {
                used[x] = true;
                ans.push(x);
                if (dfs(pos + 1)) return true;
                ans.pop();
                used[x] = false;
            } else {
                kk -= cnt;
            }
        }
        return false;
    };
    if (!dfs(0)) return [];
    return ans;
};

================================================================================
FILE: 3471_find_the_largest_almost_missing_integer
================================================================================
// LeetCode 3471 - Find the Largest Almost Missing Integer
// https://leetcode.com/problems/find-the-largest-almost-missing-integer/

var largestInteger = function(nums, k) {
    const n = nums.length;
    const cnt = new Map();
    for (let i = 0; i + k <= n; i++) {
        const seen = new Set();
        for (let j = i; j < i + k; j++) seen.add(nums[j]);
        for (const x of seen) cnt.set(x, (cnt.get(x) || 0) + 1);
    }
    let ans = -1;
    for (const [key, value] of cnt) {
        if (value === 1 && key > ans) ans = key;
    }
    return ans;
};

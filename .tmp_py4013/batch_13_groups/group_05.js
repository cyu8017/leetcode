
================================================================================
FILE: 3472_longest_palindromic_subsequence_after_at_most_k_operations
================================================================================
// LeetCode 3472 - Longest Palindromic Subsequence After at Most K Operations
// https://leetcode.com/problems/longest-palindromic-subsequence-after-at-most-k-operations/

var longestPalindromicSubsequence = function(s, k) {
    const n = s.length;
    const dp = Array.from({ length: n }, () =>
        Array.from({ length: n }, () => new Array(k + 1).fill(-1))
    );
    const distCirc = (a, b) => {
        const d = Math.abs(a.charCodeAt(0) - b.charCodeAt(0));
        return Math.min(d, 26 - d);
    };
    const dfs = (i, j, ops) => {
        if (i > j) return 0;
        if (i === j) return 1;
        if (dp[i][j][ops] !== -1) return dp[i][j][ops];
        let best = dfs(i + 1, j, ops);
        best = Math.max(best, dfs(i, j - 1, ops));
        const cost = distCirc(s[i], s[j]);
        if (cost <= ops) best = Math.max(best, 2 + dfs(i + 1, j - 1, ops - cost));
        return (dp[i][j][ops] = best);
    };
    return dfs(0, n - 1, k);
};

================================================================================
FILE: 3473_sum_of_k_subarrays_with_length_at_least_m
================================================================================
// LeetCode 3473 - Sum of K Subarrays With Length at Least M
// https://leetcode.com/problems/sum-of-k-subarrays-with-length-at-least-m/

var maxSum = function(nums, k, m) {
    const n = nums.length;
    const pref = new Array(n + 1).fill(0);
    for (let i = 0; i < n; i++) pref[i + 1] = pref[i] + nums[i];
    const neg = Number.MIN_SAFE_INTEGER / 4;
    const dp = Array.from({ length: k + 1 }, () => new Array(n + 1).fill(neg));
    for (let i = 0; i <= n; i++) dp[0][i] = 0;
    for (let t = 1; t <= k; t++) {
        let best = neg;
        for (let i = t * m; i <= n; i++) {
            const j = i - m;
            best = Math.max(best, dp[t - 1][j] - pref[j]);
            dp[t][i] = best + pref[i];
        }
        for (let i = 1; i <= n; i++) dp[t][i] = Math.max(dp[t][i], dp[t][i - 1]);
    }
    return dp[k][n];
};

================================================================================
FILE: 3474_lexicographically_smallest_generated_string
================================================================================
// LeetCode 3474 - Lexicographically Smallest Generated String
// https://leetcode.com/problems/lexicographically-smallest-generated-string/

var generateString = function(str1, str2) {
    const n = str1.length, m = str2.length;
    const L = n + m - 1;
    const ans = new Array(L).fill("?");
    for (let i = 0; i < n; i++) {
        if (str1[i] === "T") {
            for (let j = 0; j < m; j++) {
                if (ans[i + j] !== "?" && ans[i + j] !== str2[j]) return "";
                ans[i + j] = str2[j];
            }
        }
    }
    for (let i = 0; i < L; i++) if (ans[i] === "?") ans[i] = "a";
    for (let i = 0; i < n; i++) {
        if (str1[i] === "F") {
            let match = true;
            for (let j = 0; j < m; j++) if (ans[i + j] !== str2[j]) { match = false; break; }
            if (match) {
                let changed = false;
                for (let j = m - 1; j >= 0; j--) {
                    const pos = i + j;
                    let forced = false;
                    for (let t = 0; t < n; t++) {
                        if (str1[t] === "T" && pos >= t && pos < t + m) { forced = true; break; }
                    }
                    if (!forced) {
                        ans[pos] = "b";
                        changed = true;
                        break;
                    }
                }
                if (!changed) return "";
            }
        }
    }
    for (let i = 0; i < n; i++) {
        let match = true;
        for (let j = 0; j < m; j++) if (ans[i + j] !== str2[j]) { match = false; break; }
        if (str1[i] === "T" && !match) return "";
        if (str1[i] === "F" && match) return "";
    }
    return ans.join("");
};

================================================================================
FILE: 3476_maximize_profit_from_task_assignment
================================================================================
// LeetCode 3476 - Maximize Profit from Task Assignment
// https://leetcode.com/problems/maximize-profit-from-task-assignment/

var maxProfit = function(workers, tasks) {
    workers = workers.slice().sort((a, b) => a - b);
    tasks = tasks.slice().sort((a, b) => a[0] - b[0]);
    let ans = 0;
    const used = new Array(tasks.length).fill(false);
    for (const w of workers) {
        let best = -1, bi = -1;
        for (let i = 0; i < tasks.length; i++) {
            if (used[i]) continue;
            if (tasks[i][0] > w) break;
            if (tasks[i][1] > best) {
                best = tasks[i][1];
                bi = i;
            }
        }
        if (bi >= 0) {
            used[bi] = true;
            ans += best;
        }
    }
    return ans;
};

================================================================================
FILE: 3477_fruits_into_baskets_ii
================================================================================
// LeetCode 3477 - Fruits Into Baskets II
// https://leetcode.com/problems/fruits-into-baskets-ii/

var numOfUnplacedFruits = function(fruits, baskets) {
    const used = new Array(baskets.length).fill(false);
    let unplaced = 0;
    for (const f of fruits) {
        let placed = false;
        for (let j = 0; j < baskets.length; j++) {
            if (!used[j] && baskets[j] >= f) {
                used[j] = true;
                placed = true;
                break;
            }
        }
        if (!placed) unplaced++;
    }
    return unplaced;
};

================================================================================
FILE: 3478_choose_k_elements_with_maximum_sum
================================================================================
// LeetCode 3478 - Choose K Elements With Maximum Sum
// https://leetcode.com/problems/choose-k-elements-with-maximum-sum/

var findMaxSum = function(nums1, nums2, k) {
    const n = nums1.length;
    const arr = [];
    for (let i = 0; i < n; i++) arr.push([nums1[i], nums2[i], i]);
    arr.sort((a, b) => a[0] - b[0]);
    const ans = new Array(n);
    const h = [];
    let sum = 0;
    const push = (v) => { h.push(v); h.sort((a, b) => a - b); };
    const poll = () => h.shift();
    for (let i = 0; i < n; ) {
        const v = arr[i][0];
        const start = i;
        while (i < n && arr[i][0] === v) i++;
        for (let t = start; t < i; t++) ans[arr[t][2]] = sum;
        for (let t = start; t < i; t++) {
            push(arr[t][1]);
            sum += arr[t][1];
            if (h.length > k) sum -= poll();
        }
    }
    return ans;
};

================================================================================
FILE: 3479_fruits_into_baskets_iii
================================================================================
// LeetCode 3479 - Fruits Into Baskets III
// https://leetcode.com/problems/fruits-into-baskets-iii/

var numOfUnplacedFruits = function(fruits, baskets) {
    const n = baskets.length;
    let size = 1;
    while (size < n) size <<= 1;
    const tree = new Array(size * 2).fill(0);
    for (let i = 0; i < n; i++) tree[size + i] = baskets[i];
    for (let i = size - 1; i > 0; i--) tree[i] = Math.max(tree[i * 2], tree[i * 2 + 1]);
    const find = (node, nl, nr, need) => {
        if (tree[node] < need) return -1;
        if (nl === nr) return nl;
        const mid = Math.floor((nl + nr) / 2);
        const left = find(node * 2, nl, mid, need);
        if (left !== -1) return left;
        return find(node * 2 + 1, mid + 1, nr, need);
    };
    const update = (idx) => {
        let p = size + idx;
        tree[p] = -1;
        for (p >>= 1; p > 0; p >>= 1) tree[p] = Math.max(tree[p * 2], tree[p * 2 + 1]);
    };
    let unplaced = 0;
    for (const f of fruits) {
        const idx = find(1, 0, size - 1, f);
        if (idx === -1 || idx >= n) unplaced++;
        else update(idx);
    }
    return unplaced;
};

================================================================================
FILE: 3480_maximize_subarrays_after_removing_one_conflicting_pair
================================================================================
// LeetCode 3480 - Maximize Subarrays After Removing One Conflicting Pair
// https://leetcode.com/problems/maximize-subarrays-after-removing-one-conflicting-pair/

var maxSubarrays = function(n, conflictingPairs) {
    const m = conflictingPairs.length;
    let best = 0;
    for (let skip = 0; skip < m; skip++) {
        const rightLimit = new Array(n + 2).fill(n + 1);
        for (let i = 0; i < m; i++) {
            if (i === skip) continue;
            let a = conflictingPairs[i][0], b = conflictingPairs[i][1];
            if (a > b) { const t = a; a = b; b = t; }
            if (b < rightLimit[a]) rightLimit[a] = b;
        }
        let minRight = n + 1;
        let cnt = 0;
        for (let l = n; l >= 1; l--) {
            if (rightLimit[l] < minRight) minRight = rightLimit[l];
            cnt += minRight - l;
        }
        if (cnt > best) best = cnt;
    }
    return best;
};

================================================================================
FILE: 3481_apply_substitutions
================================================================================
// LeetCode 3481 - Apply Substitutions
// https://leetcode.com/problems/apply-substitutions/

var applySubstitutions = function(replacements, text) {
    const mp = new Map();
    for (const r of replacements) mp.set(r[0], r[1]);
    const resolve = (s) => {
        let out = "";
        for (let i = 0; i < s.length; ) {
            if (s[i] === "%") {
                let j = i + 1;
                while (j < s.length && s[j] !== "%") j++;
                const key = s.substring(i + 1, j);
                out += resolve(mp.get(key));
                i = j + 1;
            } else {
                out += s[i];
                i++;
            }
        }
        return out;
    };
    return resolve(text);
};

================================================================================
FILE: 3483_unique_3_digit_even_numbers
================================================================================
// LeetCode 3483 - Unique 3-Digit Even Numbers
// https://leetcode.com/problems/unique-3-digit-even-numbers/

var totalNumbers = function(digits) {
    const seen = new Set();
    const n = digits.length;
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            if (j === i) continue;
            for (let k = 0; k < n; k++) {
                if (k === i || k === j) continue;
                if (digits[i] === 0) continue;
                if (digits[k] % 2 !== 0) continue;
                seen.add(digits[i] * 100 + digits[j] * 10 + digits[k]);
            }
        }
    }
    return seen.size;
};

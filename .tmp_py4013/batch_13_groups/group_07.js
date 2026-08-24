
================================================================================
FILE: 3494_find_the_minimum_amount_of_time_to_brew_potions
================================================================================
// LeetCode 3494 - Find the Minimum Amount of Time to Brew Potions
// https://leetcode.com/problems/find-the-minimum-amount-of-time-to-brew-potions/

var minTime = function(skill, mana) {
    const n = skill.length, m = mana.length;
    const done = new Array(n).fill(0);
    for (let j = 0; j < m; j++) {
        let t = 0;
        for (let i = 0; i < n; i++) {
            if (done[i] > t) t = done[i];
            t += skill[i] * mana[j];
            done[i] = t;
        }
        for (let i = n - 2; i >= 0; i--)
            done[i] = done[i + 1] - skill[i + 1] * mana[j];
    }
    return done[n - 1];
};

================================================================================
FILE: 3495_minimum_operations_to_make_array_elements_zero
================================================================================
// LeetCode 3495 - Minimum Operations to Make Array Elements Zero
// https://leetcode.com/problems/minimum-operations-to-make-array-elements-zero/

var minOperations = function(queries) {
    const opsToZero = (x) => {
        let ops = 0;
        while (x > 0) { x = Math.floor(x / 4); ops++; }
        return ops;
    };
    let ans = 0;
    for (const q of queries) {
        const l = q[0], r = q[1];
        let sum = 0;
        for (let x = l; x <= r; x++) sum += opsToZero(x);
        ans += Math.floor((sum + 1) / 2);
    }
    return ans;
};

================================================================================
FILE: 3496_maximize_score_after_pair_deletions
================================================================================
// LeetCode 3496 - Maximize Score After Pair Deletions
// https://leetcode.com/problems/maximize-score-after-pair-deletions/

var maximizeScore = function(nums) {
    const n = nums.length;
    let total = 0;
    for (const x of nums) total += x;
    if (n % 2 === 1) {
        let mn = nums[0];
        for (const x of nums) if (x < mn) mn = x;
        return total - mn;
    }
    let mn = nums[0] + nums[1];
    for (let i = 0; i + 1 < n; i++) mn = Math.min(mn, nums[i] + nums[i + 1]);
    return total - mn;
};

================================================================================
FILE: 3498_reverse_degree_of_a_string
================================================================================
// LeetCode 3498 - Reverse Degree of a String
// https://leetcode.com/problems/reverse-degree-of-a-string/

var reverseDegree = function(s) {
    let ans = 0;
    for (let i = 0; i < s.length; i++)
        ans += (26 - (s.charCodeAt(i) - 97)) * (i + 1);
    return ans;
};

================================================================================
FILE: 3499_maximize_active_section_with_trade_i
================================================================================
// LeetCode 3499 - Maximize Active Section with Trade I
// https://leetcode.com/problems/maximize-active-section-with-trade-i/

var maxActiveSectionsAfterTrade = function(s) {
    let ones = 0;
    for (const c of s) if (c === "1") ones++;
    const zeros = [];
    const n = s.length;
    for (let i = 0; i < n; ) {
        if (s[i] !== "0") { i++; continue; }
        let j = i;
        while (j < n && s[j] === "0") j++;
        zeros.push([i, j - 1]);
        i = j;
    }
    let best = 0;
    for (let i = 0; i + 1 < zeros.length; i++) {
        const gain = (zeros[i][1] - zeros[i][0] + 1) + (zeros[i + 1][1] - zeros[i + 1][0] + 1);
        if (gain > best) best = gain;
    }
    return ones + best;
};

================================================================================
FILE: 3500_minimum_cost_to_divide_array_into_subarrays
================================================================================
// LeetCode 3500 - Minimum Cost to Divide Array Into Subarrays
// https://leetcode.com/problems/minimum-cost-to-divide-array-into-subarrays/

var minimumCost = function(nums, cost, k) {
    const n = nums.length;
    const pn = new Array(n + 1).fill(0), pc = new Array(n + 1).fill(0);
    for (let i = 0; i < n; i++) {
        pn[i + 1] = pn[i] + nums[i];
        pc[i + 1] = pc[i] + cost[i];
    }
    const inf = Number.MAX_SAFE_INTEGER / 4;
    const dp = new Array(n + 1).fill(0);
    for (let i = 0; i < n; i++) dp[i] = inf;
    for (let i = n - 1; i >= 0; i--) {
        for (let j = i; j < n; j++) {
            const cand = pn[j + 1] * (pc[j + 1] - pc[i]) + k * (pc[n] - pc[i]) + dp[j + 1];
            if (cand < dp[i]) dp[i] = cand;
        }
    }
    return dp[0];
};

================================================================================
FILE: 3501_maximize_active_section_with_trade_ii
================================================================================
// LeetCode 3501 - Maximize Active Section with Trade II
// https://leetcode.com/problems/maximize-active-section-with-trade-ii/

var maxActiveSectionsAfterTrade = function(s, queries) {
    let ones = 0;
    for (const c of s) if (c === "1") ones++;
    const ans = new Array(queries.length);
    for (let i = 0; i < ans.length; i++) ans[i] = ones;
    return ans;
};

================================================================================
FILE: 3502_minimum_cost_to_reach_every_position
================================================================================
// LeetCode 3502 - Minimum Cost to Reach Every Position
// https://leetcode.com/problems/minimum-cost-to-reach-every-position/

var minCosts = function(cost) {
    const n = cost.length;
    const ans = new Array(n);
    let mi = cost[0];
    for (let i = 0; i < n; i++) {
        mi = Math.min(mi, cost[i]);
        ans[i] = mi;
    }
    return ans;
};

================================================================================
FILE: 3503_longest_palindrome_after_substring_concatenation_i
================================================================================
// LeetCode 3503 - Longest Palindrome After Substring Concatenation I
// https://leetcode.com/problems/longest-palindrome-after-substring-concatenation-i/

var longestPalindrome = function(s, t) {
    const expand = (str, g, l, r) => {
        while (l >= 0 && r < str.length && str[l] === str[r]) {
            g[l] = Math.max(g[l], r - l + 1);
            l--; r++;
        }
    };
    const calc = (str) => {
        const n = str.length;
        const g = new Array(n).fill(0);
        for (let i = 0; i < n; i++) {
            expand(str, g, i, i);
            expand(str, g, i, i + 1);
        }
        return g;
    };
    const m = s.length, n = t.length;
    t = t.split("").reverse().join("");
    const g1 = calc(s), g2 = calc(t);
    let ans = 0;
    for (const v of g1) ans = Math.max(ans, v);
    for (const v of g2) ans = Math.max(ans, v);
    const f = Array.from({ length: m + 1 }, () => new Array(n + 1).fill(0));
    for (let i = 1; i <= m; i++) {
        for (let j = 1; j <= n; j++) {
            if (s[i - 1] === t[j - 1]) {
                f[i][j] = f[i - 1][j - 1] + 1;
                const a = i < m ? g1[i] : 0;
                const b = j < n ? g2[j] : 0;
                ans = Math.max(ans, f[i][j] * 2 + a);
                ans = Math.max(ans, f[i][j] * 2 + b);
            }
        }
    }
    return ans;
};

================================================================================
FILE: 3504_longest_palindrome_after_substring_concatenation_ii
================================================================================
// LeetCode 3504 - Longest Palindrome After Substring Concatenation II
// https://leetcode.com/problems/longest-palindrome-after-substring-concatenation-ii/

function expand(s, g, l, r) {
    while (l >= 0 && r < s.length && s[l] === s[r]) {
        g[l] = Math.max(g[l], r - l + 1);
        l--; r++;
    }
}
function calc(s) {
    const n = s.length;
    const g = new Array(n).fill(0);
    for (let i = 0; i < n; i++) {
        expand(s, g, i, i);
        expand(s, g, i, i + 1);
    }
    return g;
}
var longestPalindrome = function(s, t) {
    const m = s.length, n = t.length;
    t = t.split('').reverse().join('');
    const g1 = calc(s), g2 = calc(t);
    let ans = 0;
    for (const v of g1) ans = Math.max(ans, v);
    for (const v of g2) ans = Math.max(ans, v);
    const f = Array.from({length: m + 1}, () => new Array(n + 1).fill(0));
    for (let i = 1; i <= m; i++) {
        for (let j = 1; j <= n; j++) {
            if (s[i - 1] === t[j - 1]) {
                f[i][j] = f[i - 1][j - 1] + 1;
                const a = i < m ? g1[i] : 0;
                const b = j < n ? g2[j] : 0;
                ans = Math.max(ans, f[i][j] * 2 + a);
                ans = Math.max(ans, f[i][j] * 2 + b);
            }
        }
    }
    return ans;
};

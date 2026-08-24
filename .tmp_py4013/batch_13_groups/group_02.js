
================================================================================
FILE: 3440_reschedule_meetings_for_maximum_free_time_ii
================================================================================
// LeetCode 3440 - Reschedule Meetings for Maximum Free Time II
// https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-ii/

var maxFreeTime = function(eventTime, startTime, endTime) {
    const n = startTime.length;
    const gaps = new Array(n + 1);
    gaps[0] = startTime[0];
    for (let i = 1; i < n; i++) gaps[i] = startTime[i] - endTime[i - 1];
    gaps[n] = eventTime - endTime[n - 1];
    let ans = 0;
    for (const g of gaps) if (g > ans) ans = g;
    const leftMax = new Array(n + 1), rightMax = new Array(n + 1);
    for (let i = 0; i <= n; i++) {
        leftMax[i] = gaps[i];
        if (i > 0 && leftMax[i - 1] > leftMax[i]) leftMax[i] = leftMax[i - 1];
    }
    for (let i = n; i >= 0; i--) {
        rightMax[i] = gaps[i];
        if (i < n && rightMax[i + 1] > rightMax[i]) rightMax[i] = rightMax[i + 1];
    }
    for (let i = 0; i < n; i++) {
        const dur = endTime[i] - startTime[i];
        const merged = gaps[i] + gaps[i + 1];
        let bestOther = 0;
        if (i > 0 && leftMax[i - 1] > bestOther) bestOther = leftMax[i - 1];
        if (i + 2 <= n && rightMax[i + 2] > bestOther) bestOther = rightMax[i + 2];
        let cand = merged;
        if (bestOther >= dur) cand = merged + dur;
        if (cand > ans) ans = cand;
    }
    return ans;
};

================================================================================
FILE: 3441_minimum_cost_good_caption
================================================================================
// LeetCode 3441 - Minimum Cost Good Caption
// https://leetcode.com/problems/minimum-cost-good-caption/

var minCostGoodCaption = function(caption) {
    const n = caption.length;
    if (n < 3) return "";
    const ans = caption.split("");
    let i = 0;
    while (i < n) {
        let j = i;
        while (j < n && ans[j] === ans[i]) j++;
        if (j - i >= 3) { i = j; continue; }
        const need = 3 - (j - i);
        if (j + need <= n) {
            for (let t = 0; t < need; t++) ans[j + t] = ans[i];
            i = j + need;
        } else {
            let ch = "a";
            if (i > 0) ch = ans[i - 1];
            else if (j < n) ch = caption[j];
            for (let t = i; t < n; t++) ans[t] = ch;
            break;
        }
    }
    i = 0;
    while (i < n) {
        let j = i;
        while (j < n && ans[j] === ans[i]) j++;
        if (j - i < 3) return "";
        i = j;
    }
    return ans.join("");
};

================================================================================
FILE: 3442_maximum_difference_between_even_and_odd_frequency_i
================================================================================
// LeetCode 3442 - Maximum Difference Between Even and Odd Frequency I
// https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i/

var maxDifference = function(s) {
    const freq = new Array(26).fill(0);
    for (const c of s) freq[c.charCodeAt(0) - 97]++;
    let maxOdd = 0, minEven = 1e9;
    for (const f of freq) {
        if (f === 0) continue;
        if (f % 2 === 1) {
            if (f > maxOdd) maxOdd = f;
        } else if (f < minEven) minEven = f;
    }
    return maxOdd - minEven;
};

================================================================================
FILE: 3443_maximum_manhattan_distance_after_k_changes
================================================================================
// LeetCode 3443 - Maximum Manhattan Distance After K Changes
// https://leetcode.com/problems/maximum-manhattan-distance-after-k-changes/

var maxDistance = function(s, k) {
    let ans = 0;
    let lat = 0, lon = 0;
    for (let i = 0; i < s.length; i++) {
        const c = s[i];
        if (c === "N") lat++;
        else if (c === "S") lat--;
        else if (c === "E") lon++;
        else lon--;
        const md = Math.abs(lat) + Math.abs(lon);
        const steps = i + 1;
        let cur = md + 2 * k;
        if (cur > steps) cur = steps;
        if (cur > ans) ans = cur;
    }
    return ans;
};

================================================================================
FILE: 3444_minimum_increments_for_target_multiples_in_an_array
================================================================================
// LeetCode 3444 - Minimum Increments for Target Multiples in an Array
// https://leetcode.com/problems/minimum-increments-for-target-multiples-in-an-array/

var minimumIncrements = function(nums, target) {
    const gcd = (a, b) => { while (b) { const t = a % b; a = b; b = t; } return a; };
    const lcm = (a, b) => a / gcd(a, b) * b;
    const m = target.length;
    const N = 1 << m;
    const inf = 1e18;
    let dp = new Array(N).fill(inf);
    dp[0] = 0;
    for (const x of nums) {
        const ndp = dp.slice();
        for (let mask = 0; mask < N; mask++) {
            for (let sub = 1; sub < N; sub++) {
                let L = 1;
                let ok = true;
                for (let i = 0; i < m; i++) {
                    if (sub & (1 << i)) {
                        L = lcm(L, target[i]);
                        if (L > 1000000000) { ok = false; break; }
                    }
                }
                if (!ok) continue;
                const cost = (L - x % L) % L;
                const nmask = mask | sub;
                if (dp[mask] + cost < ndp[nmask]) ndp[nmask] = dp[mask] + cost;
            }
        }
        dp = ndp;
    }
    return dp[N - 1];
};

================================================================================
FILE: 3445_maximum_difference_between_even_and_odd_frequency_ii
================================================================================
// LeetCode 3445 - Maximum Difference Between Even and Odd Frequency II
// https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-ii/

var maxDifference = function(s, k) {
    const n = s.length;
    let ans = -1e9;
    for (let a = 0; a < 5; a++) {
        for (let b = 0; b < 5; b++) {
            if (a === b) continue;
            const prefA = new Array(n + 1).fill(0), prefB = new Array(n + 1).fill(0);
            for (let i = 0; i < n; i++) {
                prefA[i + 1] = prefA[i];
                prefB[i + 1] = prefB[i];
                if (s.charCodeAt(i) - 48 === a) prefA[i + 1]++;
                if (s.charCodeAt(i) - 48 === b) prefB[i + 1]++;
            }
            for (let i = 0; i < n; i++) {
                for (let j = i + k - 1; j < n; j++) {
                    const fa = prefA[j + 1] - prefA[i];
                    const fb = prefB[j + 1] - prefB[i];
                    if (fa % 2 === 1 && fb % 2 === 0 && fb > 0) {
                        if (fa - fb > ans) ans = fa - fb;
                    }
                }
            }
        }
    }
    return ans;
};

================================================================================
FILE: 3446_sort_matrix_by_diagonals
================================================================================
// LeetCode 3446 - Sort Matrix by Diagonals
// https://leetcode.com/problems/sort-matrix-by-diagonals/

var sortMatrix = function(grid) {
    const n = grid.length;
    const diags = new Map();
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            const key = i - j;
            if (!diags.has(key)) diags.set(key, []);
            diags.get(key).push(grid[i][j]);
        }
    }
    for (const [key, list] of diags) {
        if (key >= 0) list.sort((a, b) => b - a);
        else list.sort((a, b) => a - b);
    }
    const idx = new Map();
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            const k = i - j;
            const pos = idx.get(k) || 0;
            grid[i][j] = diags.get(k)[pos];
            idx.set(k, pos + 1);
        }
    }
    return grid;
};

================================================================================
FILE: 3447_assign_elements_to_groups_with_constraints
================================================================================
// LeetCode 3447 - Assign Elements to Groups with Constraints
// https://leetcode.com/problems/assign-elements-to-groups-with-constraints/

var assignElements = function(groups, elements) {
    const maxV = 100001;
    const first = new Array(maxV).fill(-1);
    for (let i = 0; i < elements.length; i++) {
        const e = elements[i];
        if (e < maxV && first[e] === -1) first[e] = i;
    }
    const ans = new Array(groups.length);
    for (let gi = 0; gi < groups.length; gi++) {
        const g = groups[gi];
        let best = -1;
        for (let d = 1; d * d <= g; d++) {
            if (g % d === 0) {
                if (first[d] !== -1 && (best === -1 || first[d] < best)) best = first[d];
                const other = Math.floor(g / d);
                if (first[other] !== -1 && (best === -1 || first[other] < best)) best = first[other];
            }
        }
        ans[gi] = best;
    }
    return ans;
};

================================================================================
FILE: 3448_count_substrings_divisible_by_last_digit
================================================================================
// LeetCode 3448 - Count Substrings Divisible By Last Digit
// https://leetcode.com/problems/count-substrings-divisible-by-last-digit/

var countSubstrings = function(s) {
    let ans = 0;
    const n = s.length;
    for (let r = 0; r < n; r++) {
        const last = s.charCodeAt(r) - 48;
        if (last === 0) continue;
        let mod = 0;
        let p = 1 % last;
        for (let l = r; l >= 0; l--) {
            mod = (mod + (s.charCodeAt(l) - 48) * p) % last;
            p = (p * 10) % last;
            if (mod === 0) ans++;
        }
    }
    return ans;
};

================================================================================
FILE: 3449_maximize_the_minimum_game_score
================================================================================
// LeetCode 3449 - Maximize the Minimum Game Score
// https://leetcode.com/problems/maximize-the-minimum-game-score/

var maxScore = function(points, m) {
    const ok = (mid) => {
        let need = 0n, extra = 0n;
        const mm = BigInt(m);
        for (const p of points) {
            const pp = BigInt(p);
            const req = (mid + pp - 1n) / pp;
            if (req > extra) {
                const visits = req - extra;
                need += 2n * visits - 1n;
                extra = visits - 1n;
            } else {
                need += 1n;
                extra = 0n;
            }
            if (need > mm) return false;
        }
        return need <= mm;
    };
    let lo = 0n, hi = 10n ** 18n;
    while (lo < hi) {
        const mid = (lo + hi + 1n) / 2n;
        if (ok(mid)) lo = mid;
        else hi = mid - 1n;
    }
    return Number(lo);
};

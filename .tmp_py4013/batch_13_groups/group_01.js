
================================================================================
FILE: 3429_paint_house_iv
================================================================================
// LeetCode 3429 - Paint House IV
// https://leetcode.com/problems/paint-house-iv/

var minCost = function(n, cost) {
    const inf = Number.MAX_SAFE_INTEGER / 4;
    const m = Math.floor(n / 2);
    let dp = Array.from({ length: 3 }, () => new Array(3).fill(0));
    for (let a = 0; a < 3; a++) {
        for (let b = 0; b < 3; b++) {
            dp[a][b] = (a === b) ? inf : cost[0][a] + cost[n - 1][b];
        }
    }
    for (let i = 1; i < m; i++) {
        const ndp = Array.from({ length: 3 }, () => new Array(3).fill(inf));
        for (let pa = 0; pa < 3; pa++) {
            for (let pb = 0; pb < 3; pb++) {
                if (dp[pa][pb] >= inf) continue;
                for (let a = 0; a < 3; a++) {
                    if (a === pa) continue;
                    for (let b = 0; b < 3; b++) {
                        if (b === pb || a === b) continue;
                        const v = dp[pa][pb] + cost[i][a] + cost[n - 1 - i][b];
                        if (v < ndp[a][b]) ndp[a][b] = v;
                    }
                }
            }
        }
        dp = ndp;
    }
    let ans = inf;
    for (let a = 0; a < 3; a++) for (let b = 0; b < 3; b++) if (dp[a][b] < ans) ans = dp[a][b];
    return ans;
};

================================================================================
FILE: 3430_maximum_and_minimum_sums_of_at_most_size_k_subarrays
================================================================================
// LeetCode 3430 - Maximum and Minimum Sums of at Most Size K Subarrays
// https://leetcode.com/problems/maximum-and-minimum-sums-of-at-most-size-k-subarrays/

var minMaxSubarraySum = function(nums, k) {
    const n = nums.length;
    let ans = 0;
    for (let i = 0; i < n; i++) {
        let mn = nums[i], mx = nums[i];
        for (let j = i; j < n && j - i + 1 <= k; j++) {
            if (nums[j] < mn) mn = nums[j];
            if (nums[j] > mx) mx = nums[j];
            ans += mn + mx;
        }
    }
    return ans;
};

================================================================================
FILE: 3431_minimum_unlocked_indices_to_sort_nums
================================================================================
// LeetCode 3431 - Minimum Unlocked Indices to Sort Nums
// https://leetcode.com/problems/minimum-unlocked-indices-to-sort-nums/

var minUnlockedIndices = function(nums, locked) {
    const n = nums.length;
    let need = false;
    for (let i = 1; i < n; i++) {
        if (nums[i] < nums[i - 1]) { need = true; break; }
    }
    if (!need) return 0;
    let left = n, right = -1;
    for (let i = 0; i < n; i++) {
        for (let j = i + 1; j < n; j++) {
            if (nums[i] > nums[j]) {
                if (i < left) left = i;
                if (j > right) right = j;
            }
        }
    }
    if (right < left) return 0;
    let ans = 0;
    for (let i = left; i <= right; i++) if (locked[i] === 1) ans++;
    const tmp = nums.slice();
    const lock = locked.slice();
    for (let i = left; i <= right; i++) lock[i] = 0;
    let changed = true;
    while (changed) {
        changed = false;
        for (let i = 0; i + 1 < n; i++) {
            if (lock[i] === 0 && lock[i + 1] === 0 && tmp[i] > tmp[i + 1]) {
                const t = tmp[i]; tmp[i] = tmp[i + 1]; tmp[i + 1] = t;
                changed = true;
            }
        }
    }
    for (let i = 1; i < n; i++) if (tmp[i] < tmp[i - 1]) return -1;
    return ans;
};

================================================================================
FILE: 3432_count_partitions_with_even_sum_difference
================================================================================
// LeetCode 3432 - Count Partitions with Even Sum Difference
// https://leetcode.com/problems/count-partitions-with-even-sum-difference/

var countPartitions = function(nums) {
    let total = 0;
    for (const x of nums) total += x;
    let ans = 0, left = 0;
    for (let i = 0; i < nums.length - 1; i++) {
        left += nums[i];
        if ((left - (total - left)) % 2 === 0) ans++;
    }
    return ans;
};

================================================================================
FILE: 3433_count_mentions_per_user
================================================================================
// LeetCode 3433 - Count Mentions Per User
// https://leetcode.com/problems/count-mentions-per-user/

var countMentions = function(numberOfUsers, events) {
    events = events.slice().sort((a, b) => {
        const ti = parseInt(a[1], 10), tj = parseInt(b[1], 10);
        if (ti !== tj) return ti - tj;
        return b[0].localeCompare(a[0]);
    });
    const online = new Array(numberOfUsers).fill(true);
    const offlineUntil = new Array(numberOfUsers).fill(0);
    const ans = new Array(numberOfUsers).fill(0);
    for (const e of events) {
        const t = parseInt(e[1], 10);
        for (let i = 0; i < numberOfUsers; i++) {
            if (!online[i] && offlineUntil[i] <= t) online[i] = true;
        }
        if (e[0] === "OFFLINE") {
            const id = parseInt(e[2], 10);
            online[id] = false;
            offlineUntil[id] = t + 60;
        } else {
            const msg = e[2];
            if (msg === "ALL") {
                for (let i = 0; i < numberOfUsers; i++) ans[i]++;
            } else if (msg === "HERE") {
                for (let i = 0; i < numberOfUsers; i++) if (online[i]) ans[i]++;
            } else {
                for (const part of msg.split(" ")) {
                    const id = parseInt(part.substring(2), 10);
                    ans[id]++;
                }
            }
        }
    }
    return ans;
};

================================================================================
FILE: 3434_maximum_frequency_after_subarray_operation
================================================================================
// LeetCode 3434 - Maximum Frequency After Subarray Operation
// https://leetcode.com/problems/maximum-frequency-after-subarray-operation/

var maxFrequency = function(nums, k) {
    let base = 0;
    for (const x of nums) if (x === k) base++;
    let ans = base;
    const uniq = new Set(nums);
    for (const v of uniq) {
        if (v === k) continue;
        let best = 0, cur = 0;
        for (const x of nums) {
            let delta = 0;
            if (x === v) delta = 1;
            else if (x === k) delta = -1;
            cur += delta;
            if (cur < 0) cur = 0;
            if (cur > best) best = cur;
        }
        if (base + best > ans) ans = base + best;
    }
    return ans;
};

================================================================================
FILE: 3435_frequencies_of_shortest_supersequences
================================================================================
// LeetCode 3435 - Frequencies of Shortest Supersequences
// https://leetcode.com/problems/frequencies-of-shortest-supersequences/

var supersequences = function(words) {
    const used = new Array(26).fill(false);
    for (const w of words) {
        used[w.charCodeAt(0) - 97] = true;
        used[w.charCodeAt(1) - 97] = true;
    }
    const letters = [];
    for (let i = 0; i < 26; i++) if (used[i]) letters.push(i);
    const m = letters.length;
    const freq = new Array(26).fill(0);
    let best = 1e9;
    let bestFreqs = [];
    const dfs = (i) => {
        if (i === m) {
            for (const w of words) {
                const a = w.charCodeAt(0) - 97, b = w.charCodeAt(1) - 97;
                if (a === b) {
                    if (freq[a] < 2) return;
                } else if (freq[a] < 1 || freq[b] < 1) return;
            }
            let sum = 0;
            const f = freq.slice();
            for (let j = 0; j < 26; j++) sum += freq[j];
            if (sum < best) {
                best = sum;
                bestFreqs = [f];
            } else if (sum === best) bestFreqs.push(f);
            return;
        }
        const L = letters[i];
        for (let c = 1; c <= 2; c++) {
            freq[L] = c;
            dfs(i + 1);
        }
        freq[L] = 0;
    };
    dfs(0);
    return bestFreqs;
};

================================================================================
FILE: 3437_permutations_iii
================================================================================
// LeetCode 3437 - Permutations III
// https://leetcode.com/problems/permutations-iii/

var permute = function(n) {
    const ans = [];
    const used = new Array(n + 1).fill(false);
    const cur = [];
    const dfs = () => {
        if (cur.length === n) {
            ans.push(cur.slice());
            return;
        }
        for (let i = 1; i <= n; i++) {
            if (used[i]) continue;
            if (cur.length && (cur[cur.length - 1] % 2 === i % 2)) continue;
            used[i] = true;
            cur.push(i);
            dfs();
            cur.pop();
            used[i] = false;
        }
    };
    dfs();
    return ans;
};

================================================================================
FILE: 3438_find_valid_pair_of_adjacent_digits_in_string
================================================================================
// LeetCode 3438 - Find Valid Pair of Adjacent Digits in String
// https://leetcode.com/problems/find-valid-pair-of-adjacent-digits-in-string/

var findValidPair = function(s) {
    const freq = new Array(10).fill(0);
    for (const c of s) freq[c.charCodeAt(0) - 48]++;
    for (let i = 0; i + 1 < s.length; i++) {
        const a = s.charCodeAt(i) - 48, b = s.charCodeAt(i + 1) - 48;
        if (a !== b && freq[a] === a && freq[b] === b) return s.substring(i, i + 2);
    }
    return "";
};

================================================================================
FILE: 3439_reschedule_meetings_for_maximum_free_time_i
================================================================================
// LeetCode 3439 - Reschedule Meetings for Maximum Free Time I
// https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-i/

var maxFreeTime = function(eventTime, k, startTime, endTime) {
    const n = startTime.length;
    const gaps = new Array(n + 1);
    gaps[0] = startTime[0];
    for (let i = 1; i < n; i++) gaps[i] = startTime[i] - endTime[i - 1];
    gaps[n] = eventTime - endTime[n - 1];
    const window = k + 1;
    let sum = 0;
    for (let i = 0; i < window && i < gaps.length; i++) sum += gaps[i];
    let ans = sum;
    for (let i = window; i < gaps.length; i++) {
        sum += gaps[i] - gaps[i - window];
        if (sum > ans) ans = sum;
    }
    return ans;
};

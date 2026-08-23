// LeetCode 3957 - Maximum Sum of M Non-Overlapping Subarrays II
// https://leetcode.com/problems/maximum-sum-of-m-non-overlapping-subarrays-ii/

function State(value, count) {
    this.value = value || 0;
    this.count = count || 0;
}

function better(a, b) {
    return a.value > b.value || (a.value === b.value && a.count > b.count);
}

function candidateBetter(dp, prefix, a, b) {
    const left = new State(dp[a].value - prefix[a], dp[a].count);
    const right = new State(dp[b].value - prefix[b], dp[b].count);
    return better(left, right);
}

function run(prefix, n, l, r, penalty) {
    const dp = Array.from({length: n + 1}, () => new State());
    const deque = [];
    for (let end = 1; end <= n; end++) {
        const addIndex = end - l;
        if (addIndex >= 0) {
            while (deque.length > 0 && candidateBetter(dp, prefix, addIndex, deque[deque.length - 1])) deque.pop();
            deque.push(addIndex);
        }
        const minIndex = end - r;
        while (deque.length > 0 && deque[0] < minIndex) deque.shift();
        dp[end] = new State(dp[end - 1].value, dp[end - 1].count);
        if (deque.length > 0) {
            const start = deque[0];
            const take = new State(dp[start].value + prefix[end] - prefix[start] - penalty, dp[start].count + 1);
            if (better(take, dp[end])) dp[end] = take;
        }
    }
    return dp[n];
}

var maxSum = function(nums, m, l, r) {
    const n = nums.length;
    const prefix = new Array(n + 1).fill(0);
    for (let i = 0; i < n; i++) prefix[i + 1] = prefix[i] + nums[i];

    const unconstrained = run(prefix, n, l, r, 0);
    if (unconstrained.count > 0 && unconstrained.count <= m) return unconstrained.value;
    if (unconstrained.count > m) {
        let bound = 0;
        for (const value of nums) bound += value >= 0 ? value : -value;
        let low = 0, high = bound + 1;
        while (low < high) {
            const mid = low + Math.floor((high - low + 1) / 2);
            if (run(prefix, n, l, r, mid).count >= m) low = mid;
            else high = mid - 1;
        }
        const state = run(prefix, n, l, r, low);
        return state.value + low * m;
    }
    const infinity = 2 ** 60;
    let bestSingle = -infinity;
    const deque = [];
    for (let end = 1; end <= n; end++) {
        const addIndex = end - l;
        if (addIndex >= 0) {
            while (deque.length > 0 && prefix[deque[deque.length - 1]] >= prefix[addIndex]) deque.pop();
            deque.push(addIndex);
        }
        const minIndex = end - r;
        while (deque.length > 0 && deque[0] < minIndex) deque.shift();
        if (deque.length > 0) {
            const sum = prefix[end] - prefix[deque[0]];
            if (sum > bestSingle) bestSingle = sum;
        }
    }
    return bestSingle;
};

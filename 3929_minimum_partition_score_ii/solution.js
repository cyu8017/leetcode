// LeetCode 3929 - Minimum Partition Score II
// https://leetcode.com/problems/minimum-partition-score-ii/

function Line(slope, intercept, count, valid) {
    this.slope = slope || 0;
    this.intercept = intercept || 0;
    this.count = count || 0;
    this.valid = !!valid;
}
function State(value, count, valid) {
    this.value = value || 0;
    this.count = count || 0;
    this.valid = !!valid;
}

function better(a, b) {
    if (!a.valid) return b;
    if (!b.valid) return a;
    if (a.value !== b.value) return a.value < b.value ? a : b;
    return a.count >= b.count ? a : b;
}

function evaluate(line, x) {
    if (!line.valid) return new State();
    return new State(line.slope * x + line.intercept, line.count, true);
}

var minPartitionScore = function(nums, k) {
    const n = nums.length;
    const prefix = new Array(n + 1).fill(0);
    for (let i = 0; i < n; i++) prefix[i + 1] = prefix[i] + nums[i];

    function insert(tree, node, left, right, line) {
        if (!tree[node].valid) {
            tree[node] = line;
            return;
        }
        const mid = Math.floor((left + right) / 2);
        const xLeft = prefix[left], xMid = prefix[mid];
        const leftBetter = better(evaluate(line, xLeft), evaluate(tree[node], xLeft));
        const midBetter = better(evaluate(line, xMid), evaluate(tree[node], xMid));
        const lineWinsLeft = leftBetter.value === evaluate(line, xLeft).value && leftBetter.count === line.count;
        const lineWinsMid = midBetter.value === evaluate(line, xMid).value && midBetter.count === line.count;
        if (lineWinsMid) {
            const tmp = tree[node];
            tree[node] = line;
            line = tmp;
        }
        if (left === right) return;
        if (lineWinsLeft !== lineWinsMid) insert(tree, node * 2, left, mid, line);
        else insert(tree, node * 2 + 1, mid + 1, right, line);
    }

    function query(tree, node, left, right, index) {
        let result = evaluate(tree[node], prefix[index]);
        if (left === right) return result;
        const mid = Math.floor((left + right) / 2);
        if (index <= mid) return better(result, query(tree, node * 2, left, mid, index));
        return better(result, query(tree, node * 2 + 1, mid + 1, right, index));
    }

    function run(penalty) {
        const tree = Array.from({length: 4 * (n + 1)}, () => new Line());
        insert(tree, 1, 0, n, new Line(0, 0, 0, true));
        let current = new State();
        for (let i = 1; i <= n; i++) {
            const best = query(tree, 1, 0, n, i);
            const x = prefix[i];
            current = new State(best.value + x * x + x + penalty, best.count + 1, true);
            insert(tree, 1, 0, n, new Line(-2 * x, current.value + x * x - x, current.count, true));
        }
        return current;
    }

    const bound = prefix[n] * prefix[n] + prefix[n] + 1;
    let low = 0, high = bound;
    while (low < high) {
        const mid = low + Math.floor((high - low + 1) / 2);
        if (run(mid).count >= k) low = mid;
        else high = mid - 1;
    }
    const state = run(low);
    return Math.floor((state.value - low * k) / 2);
};

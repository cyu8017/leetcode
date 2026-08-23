// LeetCode 3763 - Maximum Total Sum With Threshold Constraints
// https://leetcode.com/problems/maximum_total_sum_with_threshold_constraints/

var maxSum = function(nums, threshold) {
    const n = nums.length;
    const idx = Array.from({length: n}, (_, i) => i);
    idx.sort((a, b) => threshold[a] - threshold[b]);
    const tree = [];
    const push = (x) => {
        tree.push(x);
        let i = tree.length - 1;
        while (i > 0) {
            const p = (i - 1) >> 1;
            if (tree[i] <= tree[p]) break;
            [tree[i], tree[p]] = [tree[p], tree[i]];
            i = p;
        }
    };
    const pop = () => {
        const top = tree[0];
        const last = tree.pop();
        if (tree.length) {
            tree[0] = last;
            let i = 0;
            while (true) {
                let s = i, l = i * 2 + 1, r = l + 1;
                if (l < tree.length && tree[l] > tree[s]) s = l;
                if (r < tree.length && tree[r] > tree[s]) s = r;
                if (s === i) break;
                [tree[i], tree[s]] = [tree[s], tree[i]];
                i = s;
            }
        }
        return top;
    };
    let ans = 0;
    let i = 0;
    for (let step = 1; ; step++) {
        while (i < n && threshold[idx[i]] <= step) {
            push(nums[idx[i]]);
            i++;
        }
        if (!tree.length) break;
        ans += pop();
    }
    return ans;
};

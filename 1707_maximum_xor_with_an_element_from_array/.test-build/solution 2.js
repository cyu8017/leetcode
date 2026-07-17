"use strict";
// LeetCode 1707 - Maximum XOR With an Element From Array
// https://leetcode.com/problems/maximum-xor-with-an-element-from-array/
function maximizeXor(nums, queries) {
    nums.sort((a, b) => a - b);
    const order = queries.map((_, i) => i).sort((a, b) => queries[a][1] - queries[b][1]);
    const ans = new Array(queries.length).fill(-1);
    const children = [[-1, -1]];
    let added = 0;
    const insert = (num) => {
        let node = 0;
        for (let bit = 31; bit >= 0; bit--) {
            const b = (num >> bit) & 1;
            if (children[node][b] === -1) {
                children[node][b] = children.length;
                children.push([-1, -1]);
            }
            node = children[node][b];
        }
    };
    for (const qi of order) {
        const [x, limit] = queries[qi];
        while (added < nums.length && nums[added] <= limit) {
            insert(nums[added]);
            added++;
        }
        if (added === 0) {
            continue;
        }
        let node = 0;
        let value = 0;
        for (let bit = 31; bit >= 0; bit--) {
            const b = (x >> bit) & 1;
            const want = b ^ 1;
            if (children[node][want] !== -1) {
                value |= 1 << bit;
                node = children[node][want];
            }
            else {
                node = children[node][b];
            }
        }
        ans[qi] = value;
    }
    return ans;
}

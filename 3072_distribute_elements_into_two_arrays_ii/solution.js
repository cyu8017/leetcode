// LeetCode 3072 - Distribute Elements Into Two Arrays II
// https://leetcode.com/problems/distribute-elements-into-two-arrays-ii/

function BIT(n) {
    this.n = n;
    this.c = new Array(n + 1).fill(0);
}
BIT.prototype.update = function(x, delta) {
    for (; x <= this.n; x += x & -x) this.c[x] += delta;
};
BIT.prototype.query = function(x) {
    let s = 0;
    for (; x > 0; x -= x & -x) s += this.c[x];
    return s;
};

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var resultArray = function(nums) {
    const st = nums.slice().sort((a, b) => a - b);
    const n = st.length;
    const tree1 = new BIT(n + 1), tree2 = new BIT(n + 1);
    const idx = (x) => {
        let lo = 0, hi = st.length;
        while (lo < hi) {
            const mid = Math.floor((lo + hi) / 2);
            if (st[mid] < x) lo = mid + 1;
            else hi = mid;
        }
        return lo + 1;
    };
    const arr1 = [nums[0]], arr2 = [nums[1]];
    tree1.update(idx(nums[0]), 1);
    tree2.update(idx(nums[1]), 1);
    for (let i = 2; i < nums.length; i++) {
        const x = nums[i];
        const id = idx(x);
        const a = arr1.length - tree1.query(id);
        const b = arr2.length - tree2.query(id);
        if (a > b || (a === b && arr1.length <= arr2.length)) {
            arr1.push(x);
            tree1.update(id, 1);
        } else {
            arr2.push(x);
            tree2.update(id, 1);
        }
    }
    return arr1.concat(arr2);
};

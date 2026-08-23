// LeetCode 3739 - Count Subarrays With Majority Element II
// https://leetcode.com/problems/count-subarrays-with-majority-element-ii/

var countMajoritySubarrays = function(nums, target) {
    class BIT {
        constructor(n_) {
            this.n = n_;
            this.c = new Array(n_ + 1).fill(0);
        }
        update(x, delta) {
            for (; x <= this.n; x += x & -x) this.c[x] += delta;
        }
        query(x) {
            let s = 0;
            for (; x > 0; x -= x & -x) s += this.c[x];
            return s;
        }
    }
    const n = nums.length;
    const tree = new BIT(2 * n + 1);
    let s = n + 1;
    tree.update(s, 1);
    let ans = 0;
    for (const x of nums) {
        if (x === target) s++;
        else s--;
        ans += tree.query(s - 1);
        tree.update(s, 1);
    }
    return ans;
};

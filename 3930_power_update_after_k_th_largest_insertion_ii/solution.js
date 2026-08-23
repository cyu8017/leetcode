// LeetCode 3930 - Power Update After K-th Largest Insertion II
// https://leetcode.com/problems/power-update-after-k-th-largest-insertion-ii/
var powerUpdate = function(nums, p, queries) {
        let mod = 1000000007;
        let vals = nums.slice(0, nums.length + queries.length);
        for (let i = 0; i < queries.length; i++) vals[nums.length + i] = queries[i][0];
        vals.sort((a,b)=>a-b);
        let uniq = 0;
        for (let i = 0; i < vals.length; i++) {
            if (uniq == 0 || vals[i] != vals[uniq - 1]) vals[uniq++] = vals[i];
        }
        vals = vals.slice(0, uniq);
        let bit = new Array(vals.length + 1).fill(0);
        for (const x of nums) add(bit, lowerBound(vals, x) + 1);
        let ans = new Array(queries.length).fill(0);
        let size = nums.length;
        let cur = p;
        for (let i = 0; i < queries.length; i++) {
            add(bit, lowerBound(vals, queries[i][0]) + 1);
            size++;
            let x = kth(bit, vals, size - queries[i][1] + 1);
            cur = powm(cur, x, mod);
            ans[i] = cur;
        }
        return ans;
    
};
var add = function(bit, i) {
        for (; i < bit.length; i += i & -i) bit[i]++;
    
};
var kth = function(bit, vals, rank) {
        let idx = 0;
        let step = 1;
        while ((step << 1) < bit.length) step <<= 1;
        for (; step > 0; step >>= 1) {
            let next = idx + step;
            if (next < bit.length && bit[next] < rank) {
                idx = next;
                rank -= bit[next];
            }
        }
        return vals[idx];
    
};
var lowerBound = function(vals, x) {
        let lo = 0, hi = vals.length;
        while (lo < hi) {
            let mid = (lo + hi) >>> 1;
            if (vals[mid] < x) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    
};
var powm = function(a, e, mod) {
        let res = 1;
        while (e > 0) {
            if ((e & 1) != 0) res = res * a % mod;
            a = a * a % mod;
            e >>= 1;
        }
        return res;
    
};

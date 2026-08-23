// LeetCode 3962 - Maximum Subarray Sum After at Most K Swaps
// https://leetcode.com/problems/maximum-subarray-sum-after-at-most-k-swaps/
var maxSubarraySum = function(nums, k) {
        let n = nums.length;
        unique = nums.slice();
        unique.sort((a,b)=>a-b);
        let u = 0;
        for (let i = 0; i < unique.length; i++) {
            if (u == 0 || unique[i] != unique[u - 1]) unique[u++] = unique[i];
        }
        unique = unique.slice(0, u);
        let rank = new Array(n).fill(0);
        let globalCount = new Array(unique.length + 1).fill(0);
        let globalSum = new Array(unique.length + 1).fill(0);
        for (let i = 0; i < n; i++) {
            rank[i] = lowerBound(unique, nums[i]) + 1;
            add(globalCount, globalSum, rank[i], 1);
        }
        let answer = -(1 << 60);
        for (let left = 0; left < n; left++) {
            let insideCount = new Array(unique.length + 1).fill(0);
            let insideSum = new Array(unique.length + 1).fill(0);
            let outsideCount = globalCount.slice();
            let outsideSum = globalSum.slice();
            let subarraySum = 0;
            for (let right = left; right < n; right++) {
                add(outsideCount, outsideSum, rank[right], -1);
                add(insideCount, insideSum, rank[right], 1);
                subarraySum += nums[right];
                let insideSize = right - left + 1;
                let outsideSize = n - insideSize;
                let limit = Math.min(k, Math.min(insideSize, outsideSize));
                let low = 0, high = limit;
                while (low < high) {
                    let mid = (low + high + 1) / 2;
                    let insideValue = unique[kth(insideCount, mid) - 1];
                    let outsideOrder = outsideSize - mid + 1;
                    let outsideValue = unique[kth(outsideCount, outsideOrder) - 1];
                    if (outsideValue > insideValue) low = mid;
                    else high = mid - 1;
                }
                let swaps = low;
                let gain = 0;
                if (swaps > 0) {
                    let smallInside = sumSmallest(insideCount, insideSum, swaps);
                    let totalOutside = querySum(outsideSum, unique.length);
                    let largeOutside = totalOutside - sumSmallest(outsideCount, outsideSum, outsideSize - swaps);
                    gain = largeOutside - smallInside;
                }
                answer = Math.max(answer, subarraySum + gain);
            }
        }
        return answer;
    
};
var add = function(count, sum, index, delta) {
        let value = unique[index - 1];
        for (; index < count.length; index += index & -index) {
            count[index] += delta;
            sum[index] += delta * value;
        }
    
};
var queryCount = function(bit, index) {
        let result = 0;
        for (; index > 0; index -= index & -index) result += bit[index];
        return result;
    
};
var querySum = function(bit, index) {
        let result = 0;
        for (; index > 0; index -= index & -index) result += bit[index];
        return result;
    
};
var kth = function(bit, order) {
        let index = 0, step = 1;
        while ((step << 1) < bit.length) step <<= 1;
        for (; step > 0; step >>= 1) {
            let next = index + step;
            if (next < bit.length && bit[next] < order) {
                index = next;
                order -= bit[next];
            }
        }
        return index + 1;
    
};
var sumSmallest = function(count, sum, amount) {
        if (amount <= 0) return 0;
        let index = kth(count, amount);
        let countBefore = queryCount(count, index - 1);
        let sumBefore = querySum(sum, index - 1);
        return sumBefore + (amount - countBefore) * unique[index - 1];
    
};
var lowerBound = function(a, x) {
        let lo = 0, hi = a.length;
        while (lo < hi) {
            let mid = (lo + hi) >>> 1;
            if (a[mid] < x) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    
};

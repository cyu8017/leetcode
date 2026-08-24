// LeetCode 3971 - Maximum Total Value
// https://leetcode.com/problems/maximum-total-value/

export function maximumTotalValue(value: any, decay: any, m: any): any {
        let mod = 1000000007;
        if (countAtLeast(value, decay, 1) <= m) {
            let sum = 0;
            for (let i = 0; i < value.length; i++) {
                let terms = (value[i] - 1) / decay[i] + 1;
                sum = (sum + terms * value[i] - decay[i] * terms * (terms - 1) / 2) % mod;
            }
            return sum;
        }
        let high = 0;
        for (const v of value) if (v > high) high = v;
        let low = 1;
        while (low < high) {
            let mid = (low + high + 1) / 2;
            if (countAtLeast(value, decay, mid) >= m) low = mid;
            else high = mid - 1;
        }
        let threshold = low;
        let count = 0, sum = 0;
        for (let i = 0; i < value.length; i++) {
            if (value[i] < threshold) continue;
            let terms = (value[i] - threshold) / decay[i] + 1;
            count += terms;
            sum = (sum + (terms * value[i] - decay[i] * terms * (terms - 1) / 2) % mod) % mod;
        }
        sum = (sum - ((count - m) % mod) * (threshold % mod)) % mod;
        if (sum < 0) sum += mod;
        return sum;
    
}export function countAtLeast(value: any, decay: any, threshold: any): any {
        let count = 0;
        for (let i = 0; i < value.length; i++) {
            if (value[i] >= threshold) count += (value[i] - threshold) / decay[i] + 1;
        }
        return count;
    
}

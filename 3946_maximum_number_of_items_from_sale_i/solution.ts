// LeetCode 3946 - Maximum Number Of Items From Sale I
// https://leetcode.com/problems/maximum-number-of-items-from-sale-i/

export function maximumSaleItems(items: any, budget: any): any {
        let f = new Array(budget + 1).fill(0);
        let mn = 2147483647;
        for (const item of items) {
            let factor = item[0], price = item[1];
            mn = Math.min(mn, price);
            let cnt = 0;
            for (const jItem of items) {
                if (jItem[0] % factor == 0) cnt++;
            }
            for (let j = budget; j >= price; j--) {
                f[j] = Math.max(f[j], f[j - price] + cnt);
            }
        }
        let ans = 0;
        for (let i = 0; i <= budget; i++) {
            let extra = (budget - i) / mn;
            ans = Math.max(ans, f[i] + extra);
        }
        return ans;
    
}

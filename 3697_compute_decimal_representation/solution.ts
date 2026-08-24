// LeetCode 3697 - Compute Decimal Representation
// https://leetcode.com/problems/compute-decimal-representation/

export function decimalRepresentation(n: any): any {
    const ans = [];
    let p = 1;
    while (n > 0) {
        const v = n % 10;
        n = Math.floor(n / 10);
        if (v !== 0) ans.push(p * v);
        p *= 10;
    }
    ans.reverse();
    return ans;
}

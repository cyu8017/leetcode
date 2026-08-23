// LeetCode 3896 - Minimum Operations To Transform Array Into Alternating Prime
// https://leetcode.com/problems/minimum-operations-to-transform-array-into-alternating-prime/

const MX3896 = 200000;
let isPrime3896 = null, primes3896 = null;
function init3896() {
    if (isPrime3896) return;
    isPrime3896 = new Array(MX3896 + 1).fill(true);
    isPrime3896[0] = isPrime3896[1] = false;
    for (let i = 2; i * i <= MX3896; i++) {
        if (isPrime3896[i]) {
            for (let j = i * i; j <= MX3896; j += i) isPrime3896[j] = false;
        }
    }
    primes3896 = [];
    for (let i = 2; i <= MX3896; i++) if (isPrime3896[i]) primes3896.push(i);
}
var minOperations = function(nums) {
    init3896();
    let ans = 0;
    for (let i = 0; i < nums.length; i++) {
        const x = nums[i];
        if (i % 2 === 0) {
            let lo = 0, hi = primes3896.length;
            while (lo < hi) {
                const mid = (lo + hi) >> 1;
                if (primes3896[mid] < x) lo = mid + 1;
                else hi = mid;
            }
            ans += primes3896[lo] - x;
        } else if (isPrime3896[x]) {
            ans += (x === 2) ? 2 : 1;
        }
    }
    return ans;
};

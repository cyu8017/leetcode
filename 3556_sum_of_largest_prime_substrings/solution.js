// LeetCode 3556 - Sum of Largest Prime Substrings
// https://leetcode.com/problems/sum-of-largest-prime-substrings/

function isPrime3556(x) {
    if (x < 2) return false;
    const sqrtX = Math.floor(Math.sqrt(x));
    for (let i = 2; i <= sqrtX; i++) if (x % i === 0) return false;
    return true;
}
var sumOfLargestPrimes = function(s) {
    const st = new Set();
    const n = s.length;
    for (let i = 0; i < n; i++) {
        let x = 0;
        for (let j = i; j < n; j++) {
            x = x * 10 + (s.charCodeAt(j) - 48);
            if (isPrime3556(x)) st.add(x);
        }
    }
    const nums = [...st].sort((a, b) => a - b);
    let ans = 0;
    for (let i = nums.length - 1; i >= 0 && nums.length - i <= 3; i--)
        ans += nums[i];
    return ans;
};

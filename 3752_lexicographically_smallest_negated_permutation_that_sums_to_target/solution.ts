// LeetCode 3752 - Lexicographically Smallest Negated Permutation that Sums to Target
// https://leetcode.com/problems/lexicographically-smallest-negated-permutation-that-sums-to-target/

export function lexicographicallySmallest(n: any, target: any): any {
    const total = n * (n + 1) / 2;
    if (target < -total || target > total || (total - target) % 2 !== 0) return [];
    let remaining = (total - target) / 2;
    const negative = new Array(n + 1).fill(false);
    for (let value = n; value >= 1; value--) {
        if (value <= remaining) {
            negative[value] = true;
            remaining -= value;
        }
    }
    const answer = [];
    for (let value = n; value >= 1; value--) {
        if (negative[value]) answer.push(-value);
    }
    for (let value = 1; value <= n; value++) {
        if (!negative[value]) answer.push(value);
    }
    return answer;
}

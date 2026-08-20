// LeetCode 1304 - Find N Unique Integers Sum Up To Zero
// https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/

function sumZero(n: number): number[] {
    const answer: any[] = [];
    for (let value = 1; value <= (n >> 1); value++) {
        answer.push(-value, value);
    }
    if (n % 2) answer.push(0);
    return answer;
}

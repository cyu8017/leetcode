// LeetCode 0135 - Candy
// https://leetcode.com/problems/candy/

export function candy(ratings: number[]): number {
    const candies = Array<number>(ratings.length).fill(1);

    for (let i = 1; i < ratings.length; i += 1) {
        if (ratings[i] > ratings[i - 1]) {
            candies[i] = candies[i - 1] + 1;
        }
    }
    for (let i = ratings.length - 2; i >= 0; i -= 1) {
        if (ratings[i] > ratings[i + 1]) {
            candies[i] = Math.max(candies[i], candies[i + 1] + 1);
        }
    }

    return candies.reduce((total, amount) => total + amount, 0);
}
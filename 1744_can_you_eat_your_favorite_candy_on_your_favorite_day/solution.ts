// LeetCode 1744 - Can You Eat Your Favorite Candy on Your Favorite Day?
// https://leetcode.com/problems/can-you-eat-your-favorite-candy-on-your-favorite-day/

function canEat(candiesCount: number[], queries: number[][]): boolean[] {
    const prefix: number[] = [0];
    for (const count of candiesCount) {
        prefix.push(prefix[prefix.length - 1] + count);
    }
    const ans: boolean[] = [];
    for (const [candyType, day, cap] of queries) {
        const minEaten = day + 1;
        const maxEaten = (day + 1) * cap;
        ans.push(maxEaten > prefix[candyType] && minEaten <= prefix[candyType + 1]);
    }
    return ans;
}

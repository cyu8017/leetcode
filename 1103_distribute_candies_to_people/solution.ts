// LeetCode 1103 - Distribute Candies to People
// https://leetcode.com/problems/distribute-candies-to-people/

function distributeCandies(candies: number, num_people: number): number[] {
    const ans = Array(num_people).fill(0);
    let give = 1, i = 0;
    while (candies > 0) {
        const take = Math.min(give, candies);
        ans[i] += take;
        candies -= take;
        give++;
        i = (i + 1) % num_people;
    }
    return ans;
}

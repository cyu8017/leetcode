// LeetCode 0904 - Fruit Into Baskets
// https://leetcode.com/problems/fruit-into-baskets/

export function totalFruit(fruits: number[]): number {
    const count = new Map();
    let left = 0, ans = 0;
    for (let right = 0; right < fruits.length; right++) {
        count.set(fruits[right], (count.get(fruits[right]) || 0) + 1);
        while (count.size > 2) {
            const c = count.get(fruits[left]) - 1;
            if (c === 0) count.delete(fruits[left]);
            else count.set(fruits[left], c);
            left++;
        }
        ans = Math.max(ans, right - left + 1);
    }
    return ans;
}

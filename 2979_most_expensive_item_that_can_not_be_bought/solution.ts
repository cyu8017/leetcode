// LeetCode 2979 - Most Expensive Item That Can Not Be Bought
// https://leetcode.com/problems/most-expensive-item-that-can-not-be-bought/

export function mostExpensiveItem(primeOne: any, primeTwo: any): any {
    return primeOne * primeTwo - primeOne - primeTwo;
}

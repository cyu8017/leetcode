"use strict";
function findDiagonalOrder(nums) {
    const diagonals = new Map(), answer = [];
    for (let r = 0; r < nums.length; r++)
        for (let c = 0; c < nums[r].length; c++) {
            const d = r + c;
            if (!diagonals.has(d))
                diagonals.set(d, []);
            diagonals.get(d).push(nums[r][c]);
        }
    for (let d = 0; diagonals.has(d); d++)
        answer.push(...diagonals.get(d).reverse());
    return answer;
}

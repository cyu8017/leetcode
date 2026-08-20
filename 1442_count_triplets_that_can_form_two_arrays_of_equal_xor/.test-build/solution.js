"use strict";
function countTriplets(arr) {
    let answer = 0, xor = 0;
    const count = new Map([[0, 1]]), indices = new Map([[0, 0]]);
    for (let i = 0; i < arr.length; i++) {
        xor ^= arr[i];
        answer += (count.get(xor) || 0) * i - (indices.get(xor) || 0);
        count.set(xor, (count.get(xor) || 0) + 1);
        indices.set(xor, (indices.get(xor) || 0) + i + 1);
    }
    return answer;
}

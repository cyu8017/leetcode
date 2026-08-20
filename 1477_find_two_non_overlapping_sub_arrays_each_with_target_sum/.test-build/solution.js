"use strict";
function minSumOfLengths(arr, target) {
    const inf = Infinity, shortest = Array(arr.length).fill(inf);
    let left = 0, sum = 0, best = inf, answer = inf;
    for (let right = 0; right < arr.length; right++) {
        sum += arr[right];
        while (sum > target)
            sum -= arr[left++];
        if (sum === target) {
            const length = right - left + 1;
            if (left > 0)
                answer = Math.min(answer, length + shortest[left - 1]);
            best = Math.min(best, length);
        }
        shortest[right] = best;
    }
    return answer === inf ? -1 : answer;
}

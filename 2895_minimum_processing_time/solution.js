// LeetCode 2895 - Minimum Processing Time
// https://leetcode.com/problems/minimum-processing-time/

/**
 * @param {number[]} processorTime
 * @param {number[]} tasks
 * @return {number}
 */
var minProcessingTime = function(processorTime, tasks) {
    processorTime = [...processorTime].sort((a, b) => a - b);
    tasks = [...tasks].sort((a, b) => b - a);
    let ans = 0;
    for (let i = 0; i < processorTime.length; i++) {
        const fin = processorTime[i] + tasks[i * 4];
        if (fin > ans) ans = fin;
    }
    return ans;
};

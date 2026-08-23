// LeetCode 3767 - Maximize Points After Choosing K Tasks
// https://leetcode.com/problems/maximize_points_after_choosing_k_tasks/

var maxPoints = function(technique1, technique2, k) {
    const n = technique1.length;
    const idx = Array.from({length: n}, (_, i) => i);
    idx.sort((i, j) => (technique1[j] - technique2[j]) - (technique1[i] - technique2[i]));
    let ans = 0;
    for (const x of technique2) ans += x;
    for (let i = 0; i < k; i++) {
        const index = idx[i];
        ans -= technique2[index];
        ans += technique1[index];
    }
    for (let i = k; i < n; i++) {
        const index = idx[i];
        if (technique1[index] >= technique2[index]) {
            ans -= technique2[index];
            ans += technique1[index];
        }
    }
    return ans;
};

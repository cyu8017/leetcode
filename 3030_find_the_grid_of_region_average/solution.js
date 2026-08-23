// LeetCode 3030 - Find the Grid of Region Average
// https://leetcode.com/problems/find-the-grid-of-region-average/

var resultGrid = function(image, threshold) {
    const n = image.length, m = image[0].length;
    const ans = Array.from({length: n}, () => new Array(m).fill(0));
    const ct = Array.from({length: n}, () => new Array(m).fill(0));
    for (let i = 0; i + 2 < n; i++) {
        for (let j = 0; j + 2 < m; j++) {
            let region = true;
            for (let k = 0; k < 3; k++)
                for (let l = 0; l < 2; l++)
                    region = region && Math.abs(image[i + k][j + l] - image[i + k][j + l + 1]) <= threshold;
            for (let k = 0; k < 2; k++)
                for (let l = 0; l < 3; l++)
                    region = region && Math.abs(image[i + k][j + l] - image[i + k + 1][j + l]) <= threshold;
            if (region) {
                let tot = 0;
                for (let k = 0; k < 3; k++)
                    for (let l = 0; l < 3; l++)
                        tot += image[i + k][j + l];
                for (let k = 0; k < 3; k++)
                    for (let l = 0; l < 3; l++) {
                        ct[i + k][j + l]++;
                        ans[i + k][j + l] += (tot / 9) | 0;
                    }
            }
        }
    }
    for (let i = 0; i < n; i++)
        for (let j = 0; j < m; j++) {
            if (ct[i][j] === 0) ans[i][j] = image[i][j];
            else ans[i][j] = (ans[i][j] / ct[i][j]) | 0;
        }
    return ans;
};

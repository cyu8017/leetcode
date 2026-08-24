// LeetCode 0661 - Image Smoother
// https://leetcode.com/problems/image-smoother/

export function imageSmoother(img: number[][]): number[][] {
    const m = img.length, n = img[0].length;
    const out = Array.from({ length: m }, () => Array(n).fill(0));
    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < n; ++j) {
            let total = 0, count = 0;
            for (let di = -1; di <= 1; ++di) {
                for (let dj = -1; dj <= 1; ++dj) {
                    const ni = i + di, nj = j + dj;
                    if (ni >= 0 && ni < m && nj >= 0 && nj < n) {
                        total += img[ni][nj];
                        ++count;
                    }
                }
            }
            out[i][j] = Math.floor(total / count);
        }
    }
    return out;
}

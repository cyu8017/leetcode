// LeetCode 0832 - Flipping an Image
// https://leetcode.com/problems/flipping-an-image/

export function flipAndInvertImage(image: number[][]): number[][] {
    for (const row of image) {
        for (let i = 0, j = row.length - 1; i <= j; i++, j--) {
            const a = 1 - row[i], b = 1 - row[j];
            row[i] = b;
            row[j] = a;
        }
    }
    return image;
}

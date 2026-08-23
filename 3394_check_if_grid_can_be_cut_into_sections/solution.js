// LeetCode 3394 - Check if Grid can be Cut into Sections
// https://leetcode.com/problems/check-if-grid-can-be-cut-into-sections/

function checkCut(rects, axis) {
    const arr = rects.map((r) => axis === 0 ? [r[0], r[2]] : [r[1], r[3]]);
    arr.sort((x, y) => x[0] === y[0] ? x[1] - y[1] : x[0] - y[0]);
    let cuts = 0;
    let end = arr[0][1];
    for (let i = 1; i < arr.length; i++) {
        if (arr[i][0] >= end) {
            cuts++;
            end = arr[i][1];
            if (cuts >= 2) return true;
        } else if (arr[i][1] > end) {
            end = arr[i][1];
        }
    }
    return false;
}
var checkValidCuts = function(n, rectangles) {
    return checkCut(rectangles, 0) || checkCut(rectangles, 1);
};

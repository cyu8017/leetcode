// LeetCode 2878 - Get the Size of a DataFrame
// https://leetcode.com/problems/get-the-size-of-a-dataframe/

/**
 * @param {object[]|any[][]} df
 * @return {number[]}
 */
var getDataframeSize = function(df) {
    if (!df || df.length === 0) return [0, 0];
    const rows = df.length;
    const cols = Array.isArray(df[0]) ? df[0].length : Object.keys(df[0]).length;
    return [rows, cols];
};

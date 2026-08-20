// LeetCode 1313 - Decompress Run Length Encoded List
// https://leetcode.com/problems/decompress-run-length-encoded-list/

function decompressRLElist(nums: number[]): number[] {
    const answer: any[] = [];
    for (let i = 0; i < nums.length; i += 2) {
        for (let j = 0; j < nums[i]; j++) answer.push(nums[i + 1]);
    }
    return answer;
}

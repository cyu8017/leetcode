// LeetCode 3992 - Rearrange String to Avoid Character Pair
// https://leetcode.com/problems/rearrange-string-to-avoid-character-pair/
var rearrangeString = function(s, x, y) {
        let arr = s.split('');
        let i = 0;
        for (let j = 0; j < arr.length; j++) {
            if (arr[j] == y) {
                let tmp = arr[i];
                arr[i] = arr[j];
                arr[j] = tmp;
                i++;
            }
        }
        return new String(arr);
    
};

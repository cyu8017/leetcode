// LeetCode 3823 - Reverse Letters Then Special Characters In A String
// https://leetcode.com/problems/reverse_letters_then_special_characters_in_a_string/

export function reverseByType(s: any): any {
    const a = [], b = [];
    for (const c of s) {
        if ((c >= 'A' && c <= 'Z') || (c >= 'a' && c <= 'z')) a.push(c);
        else b.push(c);
    }
    let j = a.length, k = b.length;
    const arr = s.split('');
    for (let i = 0; i < arr.length; i++) {
        if ((arr[i] >= 'A' && arr[i] <= 'Z') || (arr[i] >= 'a' && arr[i] <= 'z')) arr[i] = a[--j];
        else arr[i] = b[--k];
    }
    return arr.join('');
}

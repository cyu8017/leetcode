// LeetCode 2618 - Check if Object Instance of Class
// https://leetcode.com/problems/check-if-object-instance-of-class/

class Solution {
    func checkIfInstanceOf(_ obj: Any?, _ classFunction: Any.Type?) -> Bool {
        guard obj != nil, let classFunction else { return false }
        return type(of: obj!) == classFunction || (obj as AnyObject) is AnyClass
    }
}

// LeetCode 1108 - Defanging an IP Address
// https://leetcode.com/problems/defanging-an-ip-address/

impl Solution {
    pub fn defang_i_paddr(address: String) -> String {
        address.replace('.', "[.]")
    }
}

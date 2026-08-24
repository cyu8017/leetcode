// LeetCode 1693 - Daily Leads And Partners
// https://leetcode.com/problems/daily-leads-and-partners/

class Solution {
    companion object {
        const val QUERY = "SELECT date_id, make_name, COUNT(DISTINCT lead_id) unique_leads,\n" +
            "COUNT(DISTINCT partner_id) unique_partners FROM DailySales GROUP BY date_id, make_name"
    }
}

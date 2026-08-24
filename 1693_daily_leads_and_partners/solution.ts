// LeetCode 1693 - Daily Leads And Partners
// https://leetcode.com/problems/daily-leads-and-partners/

export const QUERY = `SELECT date_id, make_name, COUNT(DISTINCT lead_id) unique_leads,
COUNT(DISTINCT partner_id) unique_partners FROM DailySales GROUP BY date_id, make_name`;

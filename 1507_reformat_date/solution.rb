# LeetCode 1507 - Reformat Date
# https://leetcode.com/problems/reformat-date/

# @param {String} date
# @return {String}
def reformat_date(date)
  months = %w[Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec]
  day, month, year = date.split
  format('%s-%02d-%02d', year, months.index(month) + 1, day[0...-2].to_i)
end

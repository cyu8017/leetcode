# LeetCode 0552 - Student Attendance Record II
# https://leetcode.com/problems/student-attendance-record-ii/

# @param {Integer} n
# @return {Integer}
def check_record(n)
  mod = 10**9 + 7
  dp = Array.new(2) { [0, 0, 0] }
  dp[0][0] = 1

  n.times do
    nxt = Array.new(2) { [0, 0, 0] }
    2.times do |absences|
      3.times do |lates|
        ways = dp[absences][lates]
        next if ways.zero?

        nxt[absences][0] = (nxt[absences][0] + ways) % mod
        nxt[1][0] = (nxt[1][0] + ways) % mod if absences.zero?
        nxt[absences][lates + 1] = (nxt[absences][lates + 1] + ways) % mod if lates < 2
      end
    end
    dp = nxt
  end

  dp.flatten.sum % mod
end

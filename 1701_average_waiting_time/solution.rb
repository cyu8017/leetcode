# LeetCode 1701 - Average Waiting Time
# https://leetcode.com/problems/average-waiting-time/

# @param {Integer[][]} customers
# @return {Float}
def average_waiting_time(customers)
  current = 0
  total = 0
  customers.each do |arrival, cook|
    current = [current, arrival].max + cook
    total += current - arrival
  end
  total.to_f / customers.length
end
